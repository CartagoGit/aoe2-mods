"""Compose design-only finale contracts from canonical identities and authored text.

No campaign variables are written here. Native implementation and save/load QA
remain separate gates; a draft recommendation never grants content approval.
"""

import copy


def entry_screens(contract):
    """Return shared entry screen specifications without writing progress."""
    screens = [("predecessor-recap", contract["recap"],
                "entry recap available before fact-intro; skippable", "collection-narrator"),
               ("entry-chronology", contract["chronologyWarning"],
                "entry before fact-intro; never blocks starting", "none")]
    for predecessor in contract["predecessors"]:
        title = predecessor["title"]
        text = {locale: (
            f"Recommended before this campaign: {title[locale]} ({predecessor['publicId']}). You may start now or read the recap."
            if locale == "en" else
            f"Se recomienda completar antes {title[locale]} ({predecessor['publicId']}). Puedes comenzar ahora o leer la recapitulación."
        ) for locale in ("en", "es-ES")}
        screens.append((f"recommended-{predecessor['campaignId']}-{predecessor['route']}", text,
                        f"entry before fact-intro; if {predecessor['progressKey']} != 1; nonblocking", "none"))
    return screens


def build_entry(campaign, selection, authored, baseline):
    if baseline is None:
        raise ValueError("entry needs canonical campaign context")
    first = min(campaign["episodeSelection"], key=lambda row: row["order"])
    if selection["id"] != first["id"] or selection["order"] != first["order"]:
        raise ValueError("entry must belong to first episode")
    canonical = next(row for row in baseline if row["id"] == campaign["campaignId"])
    previous = canonical["recommendedPrevious"]
    if previous != campaign["continuityContract"]["recommendedPrevious"]:
        raise ValueError("entry predecessor identities differ from canonical catalogue")
    for field in ("recap", "chronologyWarning"):
        if set(authored[field]) != {"en", "es-ES"} or not all(authored[field].values()):
            raise ValueError("incomplete entry localization")
    targets = {row["id"]: row for row in baseline}
    predecessors = []
    for item in previous:
        target = targets[item["campaignId"]]
        route = next(row for row in target["routes"] if row["id"] == item["route"])
        if route["next"] != campaign["campaignId"]:
            raise ValueError("predecessor route does not recommend this campaign")
        predecessors.append({**copy.deepcopy(item), "publicId": target["publicId"],
                             "title": copy.deepcopy(target["title"]), "progressKey": route["key"]})
    return {
        "classification": "design-only; native variable/menu adapter and game QA pending",
        "predecessors": predecessors,
        "recap": copy.deepcopy(authored["recap"]),
        "chronologyWarning": copy.deepcopy(authored["chronologyWarning"]),
        "enforcePrerequisite": False, "proceedWithoutPredecessor": True,
        "recapAvailableAlways": True, "writesProgress": False,
        "onMissingProgress": "show recommendation; allow start or recap",
        "onCancel": "return to campaign menu; no progress write",
        "onSaveLoad": "preserve briefing state; never restart the mission or write progress",
    }


def audit_entry(episode, campaign, baseline):
    label = episode["id"]
    entry = episode.get("entryContract")
    if not entry:
        if campaign and baseline and campaign["continuityContract"]["recommendedPrevious"] and episode["id"] == min(campaign["episodeSelection"], key=lambda row: row["order"])["id"]:
            return [f"{label}: first episode needs a predecessor entry contract"]
        return []
    if campaign is None or baseline is None:
        return [f"{label}: entry needs canonical campaign context"]
    try:
        expected = build_entry(campaign, episode, entry, baseline)
    except (KeyError, ValueError, StopIteration) as error:
        return [f"{label}: invalid entry context: {error}"]
    errors = [] if entry == expected else [f"{label}: unsafe entry predecessor or prerequisite policy"]
    screens = {screen["id"]: screen for screen in episode["screens"]}
    for sid, text, condition, narrator in entry_screens(expected):
        actual = screens.get(sid)
        if actual is None or any(actual[key] != value for key, value in
                                 (("text", text), ("condition", condition), ("narrator", narrator))):
            errors.append(f"{label}: missing or incorrect entry screen {sid}")
    return errors


def build_finale(campaign, selection, authored, baseline):
    if not authored:
        return None
    if baseline is None:
        raise ValueError("finale needs canonical campaign context")
    final = max(campaign["episodeSelection"], key=lambda row: row["order"])
    if selection["id"] != final["id"] or selection["order"] != final["order"]:
        raise ValueError("intermediate episode can end campaign")
    canonical = next(row for row in baseline if row["id"] == campaign["campaignId"])
    routes = campaign["continuityContract"]["nextRoutes"]
    if routes != canonical["routes"]:
        raise ValueError("finale route identities differ from canonical catalogue")
    targets = {row["id"]: row for row in baseline}
    ids = {route["id"] for route in routes}
    if set(authored["routeLabels"]) != ids or set(authored["chronologyByRoute"]) != ids:
        raise ValueError("finale must describe every canonical route")
    choices = []
    for route in routes:
        target = targets.get(route["next"])
        choices.append({
            "id": route["id"],
            "progressKey": route["key"],
            "choiceLabel": copy.deepcopy(authored["routeLabels"][route["id"]]),
            "chronologyWarning": copy.deepcopy(authored["chronologyByRoute"][route["id"]]),
            "successor": None if target is None else {
                "campaignId": target["id"], "publicId": target["publicId"],
                "title": copy.deepcopy(target["title"]),
            },
        })
    return {
        "classification": "design-only; native variable/menu adapter and game QA pending",
        "selectionState": "route-selection",
        "choicePrompt": copy.deepcopy(authored["choicePrompt"]),
        "completionMessage": copy.deepcopy(authored["completionMessage"]),
        "routeChoices": choices,
        "selectionPolicy": {
            "requiredCount": 1, "allowPreviouslyCompletedRoute": True,
            "onCancel": "remain in route-selection; no progress write",
            "writesProgress": False,
            "closeSideRewardsOnEntry": True,
        },
        "victoryCommit": {
            "on": "victory terminal latch after all mandatory objectives and one valid selected route",
            "write": "selected route progressKey = 1",
            "oncePerRun": True, "preserveOtherKeys": True,
            "resetOtherKeys": False, "onDefeat": "no progress write",
            "onSaveLoad": "restore pending choice or committed latch; never debit or write twice",
        },
        "recommendationPolicy": {
            "primary": "route selected in this victory",
            "otherCompletedRoutes": "show every accumulated completed route as an additional recommendation",
            "withoutCurrentChoice": "show all accumulated routes; never guess a selected route",
            "autoLaunch": False, "enforcePrerequisite": False,
            "successorEntry": "show recommended predecessor and recap; allow starting without predecessor",
        },
    }


def audit_finale(episode, campaign, baseline):
    label = episode["id"]
    finale = episode.get("finaleContract")
    writes = episode["stateMachine"].get("campaignProgressWrite")
    if not finale:
        if campaign and episode["id"] == max(campaign["episodeSelection"], key=lambda row: row["order"])["id"]:
            return [f"{label}: final episode needs a finale contract"]
        return [] if writes is False else [f"{label}: intermediate episode can end campaign"]
    if campaign is None or baseline is None:
        return [f"{label}: finale needs canonical campaign context"]
    # Rebuild from canonical routes, using only the author-supplied bilingual prose.
    try:
        authored = {
            "choicePrompt": finale["choicePrompt"],
            "completionMessage": finale["completionMessage"],
            "routeLabels": {r["id"]: r["choiceLabel"] for r in finale["routeChoices"]},
            "chronologyByRoute": {r["id"]: r["chronologyWarning"] for r in finale["routeChoices"]},
        }
        expected = build_finale(campaign, episode, authored, baseline)
    except (KeyError, ValueError, StopIteration) as error:
        return [f"{label}: invalid finale context: {error}"]
    errors = []
    if finale != expected or writes is not True:
        errors.append(f"{label}: unsafe finale route, recommendation or progress policy")
    bilingual = [expected["choicePrompt"], expected["completionMessage"]]
    for route in expected["routeChoices"]:
        bilingual += [route["choiceLabel"], route["chronologyWarning"]]
    if any(set(text) != {"en", "es-ES"} or not all(text.values()) for text in bilingual):
        errors.append(f"{label}: incomplete finale localization")
        return errors
    state = episode["stateMachine"]
    transitions = state["phaseTransitions"]
    final_id = episode["objectivePlan"][-1]["id"]
    expected_last = [
        {"from": episode["objectivePlan"][-1]["phase"], "to": "route-selection",
         "on": "objective-latched", "objectiveId": final_id},
        {"from": "route-selection", "to": "victory", "on": "valid-route-selected"},
    ]
    if transitions[-2:] != expected_last or state["states"].count("route-selection") != 1:
        errors.append(f"{label}: finale bypasses pending route selection")
    screens = {screen["id"]: screen for screen in episode["screens"]}
    if "next-episode" in screens:
        errors.append(f"{label}: finale still advertises an intermediate episode")
    required = {"campaign-complete": ("after persona-outro", expected["completionMessage"]),
                "route-choice": ("route-selection active; no progress write", expected["choicePrompt"])}
    for route in expected["routeChoices"]:
        target = route["successor"]
        text = {locale: (f"{target['title'][locale]} ({target['publicId']}). " if target else "")
                + route["chronologyWarning"][locale] for locale in ("en", "es-ES")}
        required[f"next-campaign-{route['id']}"] = (
            f"after campaign-complete; selected or accumulated route {route['id']}", text)
        required[f"choose-{route['id']}"] = ("route-selection active; selectable without prior completion", route["choiceLabel"])
    for sid, (condition, text) in required.items():
        if sid not in screens or screens[sid]["condition"] != condition or screens[sid]["text"] != text:
            errors.append(f"{label}: missing or incorrect finale screen {sid}")
    return errors
