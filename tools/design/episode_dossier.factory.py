"""Materialize explicitly authored episode plans as design-only dossiers.

Authors supply facts, voices, geographic districts, object groups and predicates.
This module shares identity, accounting and caption mechanics; it never chooses
historical events, infers goals from prose, or emits native campaign content.
"""

import copy
import math
import runpy
from pathlib import Path
from geography import tile_point
from secondary import RESOURCES, REWARDS, COSTS, bilingual, build_optional_objectives

continuity = runpy.run_path(str(Path(__file__).with_name("odyssey_continuity.helper.py")))
transport = runpy.run_path(str(Path(__file__).with_name("transport_journey.helper.py")))
build_finale = continuity["build_finale"]
build_entry = continuity["build_entry"]
entry_screens = continuity["entry_screens"]


def amounts(values=None):
    return {key: (values or {}).get(key, 0) for key in RESOURCES}


def total(rows):
    return {key: sum(row.get(key, 0) for row in rows) for key in RESOURCES}


def world_and_objectives(cid, selection, authored, hubs):
    namespace = f"{cid}.{selection['id']}"
    groups = {}
    entities = []
    for group in authored["objectGroups"]:
        ids = [f"{namespace}.{group['key']}-{i}" for i in range(1, group["count"] + 1)]
        groups[group["key"]] = ids
        origin_offset = group.get("offsetBaseTiles", [-10, 8])
        for number, entity_id in enumerate(ids):
            entities.append(
                {
                    "id": entity_id,
                    "role": group["role"],
                    "initialHub": group["originHub"],
                    "offsetTiles": [
                        origin_offset[0] + 2 * (number % 4),
                        origin_offset[1] + 2 * (number // 4),
                    ],
                    "identity": "explicitly fictional gameplay identity",
                    "finite": True,
                    "replacement": "none; no free resurrection",
                    "initiallyDelivered": False,
                    "originRule": "separate pickup position outside every receiving zone",
                    "generationPolicy": group.get(
                        "generationPolicy", "preplaced and available"
                    ),
                    "historicalMaterialPolicy": group["historicalMaterialPolicy"],
                }
            )
    zones = [
        {
            "id": f"{namespace}.destination-{i}",
            "hub": hub["id"],
            "offsetTiles": [0, 0],
            "radiusTiles": 3,
            "purpose": "fictional receiving district; not an excavated ancient address",
        }
        for i, hub in enumerate(hubs, 1)
    ]
    destinations = {z["hub"]: z["id"] for z in zones}
    objectives = []
    for order, spec in enumerate(authored["mainObjectives"], 1):
        requirements = []
        for number, authored_req in enumerate(spec["requirements"], 1):
            req = copy.deepcopy(authored_req)
            req["id"] = req.get("id", f"req-{number}")
            group = req.pop("group", None)
            if group:
                req["entities"] = groups[group]
            if req["kind"] == "transport-journey":
                transport["materialize_requirement"](req, groups, destinations)
            if "departingGroup" in req:
                req["departingEntities"] = groups[req.pop("departingGroup")]
            destination = req.pop("destinationHub", None)
            if destination:
                req["destinations"] = {
                    entity_id: destinations[destination]
                    for entity_id in req["entities"]
                }
            assigned_hubs = req.pop("destinationHubsByOrdinal", None)
            if assigned_hubs:
                if len(assigned_hubs) != len(req["entities"]):
                    raise ValueError("Every delivery identity needs one assigned hub")
                req["destinations"] = {
                    entity_id: destinations[hub]
                    for entity_id, hub in zip(req["entities"], assigned_hubs)
                }
            if req["kind"] == "area-state":
                req["zones"] = [destinations[hub] for hub in req.pop("zoneHubs")]
                if "blockingEnemyGroups" in req:
                    req["blockingEnemies"] = [
                        entity_id for key in req.pop("blockingEnemyGroups")
                        for entity_id in groups[key]
                    ]
            if "inputGroups" in req:
                inputs = req.pop("inputGroups")
                field = (
                    "inputEntities"
                    if req["kind"] == "derived-token"
                    else "inputRecords"
                )
                req[field] = [entity_id for key in inputs for entity_id in groups[key]]
            if "outputGroup" in req:
                req["outputEntities"] = groups[req.pop("outputGroup")]
            if req["kind"] == "derived-token":
                refs = req.pop("requiredPaymentRequirements", None)
                if refs is None:
                    raise ValueError(
                        "Derivation needs an explicit payment policy; [] means authored unfunded derivation"
                    )
                req["_paymentRefs"] = refs
            if req["kind"] == "resource-transaction":
                req["receivingZones"] = [
                    destinations[hub] for hub in req.pop("receivingHubs")
                ]
                req["allocations"] = {
                    destinations[hub]: value
                    for hub, value in req.pop("allocationByHub").items()
                }
                req.update(
                    account="spendable",
                    paidFlag=f"{namespace}.o{order}.{req['id']}.paid",
                    once=True,
                    atomic=True,
                )
            if req["kind"] == "entity-state":
                req["oncePerEntity"] = True
            requirements.append(req)
        objectives.append(
            {
                "id": f"o{order}",
                "phase": f"phase-{order}",
                "after": [] if order == 1 else [f"o{order - 1}"],
                "text": spec["text"],
                "predicate": {
                    "operator": "all",
                    "requirements": requirements,
                    "neverUseTimerInstead": True,
                },
                "receiptText": spec["receiptText"],
                "personaReaction": spec["personaReaction"],
            }
        )
        if authored.get("exportedLedgers", {}).get(f"o{order}"):
            objectives[-1]["predicate"]["exportedLedgers"] = authored[
                "exportedLedgers"
            ][f"o{order}"]
    for objective in objectives:
        for requirement in objective["predicate"]["requirements"]:
            if requirement["kind"] != "derived-token":
                continue
            references = requirement.pop("_paymentRefs")
            receipts = []
            for reference in references:
                producer = next(
                    (o for o in objectives if o["id"] == reference["objective"]), None
                )
                payment = (
                    next(
                        (
                            r
                            for r in producer["predicate"]["requirements"]
                            if r["id"] == reference["requirement"]
                        ),
                        None,
                    )
                    if producer
                    else None
                )
                if not payment or payment["kind"] != "resource-transaction":
                    raise ValueError(
                        "Derived payment reference must name a resource transaction"
                    )
                receipts.append(
                    {
                        "flag": payment["paidFlag"],
                        "fromObjective": producer["id"],
                        "amounts": copy.deepcopy(payment["amounts"]),
                        "newDebit": False,
                    }
                )
            if receipts:
                requirement["requiredPaymentReceipts"] = receipts
    return {
        "version": 1,
        "classification": "authored design specification; not native implementation",
        "entities": entities,
        "zones": zones,
        "objectGroups": groups,
        "survivorGroups": [
            {
                "entities": groups[row["group"]],
                "minimumAliveOrAlreadySafe": row["minimumAliveOrAlreadySafe"],
            }
            for row in authored.get("survivorGroups", [])
        ],
        "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit",
    }, objectives


def map_plan(cid, selection, authored, profile):
    size = authored["mapSize"]
    bbox = authored.get("mapBBox", profile["bbox"])
    west, south, east, north = bbox
    parent_west, parent_south, parent_east, parent_north = profile["bbox"]
    if not (
        parent_west <= west < east <= parent_east
        and parent_south <= south < north <= parent_north
    ):
        raise ValueError("Episode framing must remain within its geographic region")
    hubs = [
        {
            "id": f"hub-{i}",
            "centre": tile_point(bbox, district["lonLat"], size),
            "lonLat": district["lonLat"],
            "name": district["name"],
            "radiusTiles": 12,
            "certainty": "architect fictional activity district within real geography; footprint pending",
        }
        for i, district in enumerate(authored["districts"], 1)
    ]
    return {
        "bbox": bbox,
        "terrainProfile": selection["geographyId"],
        "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
        "projection": "WGS84, cosine-corrected longitude, square padding",
        "hubs": hubs,
        "corridors": authored["corridors"],
        "terrainInstructions": authored["terrainInstructions"],
        "corridorStraightLengthsTiles": {
            corridor["id"]: round(
                sum(
                    math.dist(
                        next(h["centre"] for h in hubs if h["id"] == start),
                        next(h["centre"] for h in hubs if h["id"] == end),
                    )
                    for start, end in zip(
                        corridor["hubOrder"], corridor["hubOrder"][1:]
                    )
                ),
                2,
            )
            for corridor in authored["corridors"]
        },
        "interestSpacingTiles": [25, 55],
        "minimumUsableAreaFraction": 0.45,
        "activeAreaPolicy": "main districts, finite supply hinterland and six optional circuits; survey usable terrain, not rectangle area",
        "geometryStatus": "georeferenced proposal; neither raster/DEM nor native footprint/pathfinding certified",
        "geographicLayers": [
            {
                "assetId": "ne-odyssey-coastline",
                "interpretation": "modern regional shoreline control; not ancient harbor geometry",
            },
            {
                "assetId": "regional-rivers_lake_centerlines",
                "interpretation": "modern regional river controls where available; minor channels and ancient courses require separate evidence",
            },
        ],
        "schematicWaterControl": copy.deepcopy(profile.get("waterControlLine")),
        "performanceBudget": {
            "activeMilitaryCap": 240,
            "activeCivilianCap": 80,
            "decorativeObjectsCap": 1600,
            "activeTriggersTargetMax": 350,
            "benchmarkStatus": "pending game measurement",
        },
        "asset": f"docs/design/maps/{cid}/odyssey/{selection['id']}.svg",
    }


def difficulty_profiles(authored, reward_stock, optional_cost):
    main_cost = total(
        [
            r.get("amounts", {})
            for objective in authored["mainObjectives"]
            for r in objective["requirements"]
            if r["kind"] == "resource-transaction"
        ]
    )
    result = {}
    for level, multiplier, workers, duration in [
        ("easy", 1.15, 12, [30, 55]),
        ("standard", 1, 9, [35, 65]),
        ("hard", 0.85, 6, [40, 75]),
    ]:
        start = {
            key: int(authored["startingResources"].get(key, 0) * multiplier)
            for key in RESOURCES
        }
        recovery = amounts(authored["protectedRecoveryStock"])
        replacement = amounts(authored["replacementBudget"])
        margins = amounts(authored["discretionaryMargin"])
        bank = {
            key: main_cost[key]
            + recovery[key]
            + replacement[key]
            + reward_stock[key]
            + margins[key]
            - start[key]
            for key in RESOURCES
        }
        if min(bank.values()) < 0:
            raise ValueError("Authored resources exceed explicit funding envelope")
        accessible = {
            key: start[key] + bank[key] - reward_stock[key] for key in RESOURCES
        }
        result[level] = {
            "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
            "startingResources": start,
            "gatherableBank": bank,
            "mandatoryDeliveries": main_cost,
            "protectedRecoveryStock": recovery,
            "replacementBudget": replacement,
            "supplyMargins": margins,
            "accessibleWithoutOptionalRewards": accessible,
            "maxVillagers": workers,
            "enemyTotalCap": authored["enemyCounts"][level],
            "enemyProduction": False,
            "regeneratingResources": False,
            "roughDurationMinutes": duration,
            "difficultyLevers": authored["difficultyLevers"][level],
            "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
            "mainFeasibleSkippingAllOptionals": all(
                accessible[key] >= main_cost[key] + recovery[key] + replacement[key]
                for key in RESOURCES
            ),
            "allOptionalCostsAffordable": all(
                margins[key] >= reward_stock[key] + optional_cost[key]
                for key in RESOURCES
            ),
        }
    return result


def screen(cid, episode_id, sid, text, condition="always", narrator="none"):
    return {
        "id": sid,
        "key": f"scenario.{cid}.{episode_id}.odyssey.{sid}",
        "text": text,
        "condition": condition,
        "narrator": narrator,
        "skippable": True,
        "captionPolicy": "split into consecutive captions without dropping qualifications; keep accents",
        "captionSegments": {
            locale: [
                " ".join(value.split()[i : i + 32])
                for i in range(0, len(value.split()), 32)
            ]
            for locale, value in text.items()
        },
        "nativeSurface": "pending certified SequenceItems/message adapter",
        "voiceDurationSecondsEstimated": max(
            2, math.ceil(max(len(t.split()) for t in text.values()) / 130 * 60)
        ),
    }


def dossier_screens(cid, selection, authored, episode, narrator_id, next_selection):
    sid = selection["id"]
    add = lambda key, text, condition="always", voice="none": screen(
        cid, sid, key, text, condition, voice
    )
    result = [
        add("title", selection["title"]),
        add(
            "fact-intro", authored["factualIntro"], "intro first", "collection-narrator"
        ),
        add(
            "handover",
            authored.get(
                "handover",
                bilingual(
                    "The campaign narrator now speaks from inherited records and accounts.",
                    "El narrador de la campaña toma la palabra a partir de escritos y relatos heredados.",
                ),
            ),
            "after fact-intro",
            "collection-narrator",
        ),
        add("persona-intro", authored["personalIntro"], "after handover", narrator_id),
        add(
            "historical-license", authored["dramatizationNotice"], "after persona-intro"
        ),
        add(
            "route-help",
            authored["routeHelp"],
            "available from start; repeatable without effect",
        ),
        add(
            "economy-help",
            bilingual(
                "Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once.",
                "Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez.",
            ),
        ),
    ]
    if episode.get("entryContract"):
        result += [add(key, text, condition, voice)
                   for key, text, condition, voice in entry_screens(episode["entryContract"])]
    for objective in episode["objectivePlan"]:
        result += [
            add(
                f"{objective['id']}-goal",
                objective["text"],
                f"{objective['phase']} active",
            ),
            add(
                f"{objective['id']}-receipt",
                objective["receiptText"],
                f"{objective['id']} latched once",
            ),
            add(
                f"{objective['id']}-reaction",
                objective["personaReaction"],
                f"after {objective['id']} receipt",
                narrator_id,
            ),
        ]
    for side in episode["secondaryObjectives"]:
        result += [
            add(f"{side['id']}-goal", side["text"], "optional list from start"),
            add(
                f"{side['id']}-complete",
                bilingual(
                    f"{side['title']['en']} completed. Its stated benefit has been granted once.",
                    f"{side['title']['es-ES']}: completado. Su ventaja indicada se ha concedido una vez.",
                ),
                f"{side['id']} completed",
            ),
            add(
                f"{side['id']}-lost",
                bilingual(
                    f"{side['title']['en']} is unavailable after the loss of its unique participant or object. The main mission continues.",
                    f"{side['title']['es-ES']}: no disponible tras perder a su participante u objeto único. La misión principal continúa.",
                ),
                f"{side['id']} failed-optional",
            ),
        ]
    result += [
        add(
            "fact-outro",
            authored["factualOutro"],
            "victory first",
            "collection-narrator",
        ),
        add(
            "persona-outro", authored["personalOutro"], "after fact-outro", narrator_id
        ),
        add("defeat", authored["defeatText"], "main defeat; close side rewards first"),
        add(
            "recovery-help",
            authored["recoveryText"],
            "help; never implies an unsupported recovery action",
        ),
    ]
    if next_selection:
        result.append(
            add(
                "next-episode",
                bilingual(
                    f"Continue with {next_selection['title']['en']}. This episode does not complete the campaign.",
                    f"Continúa con {next_selection['title']['es-ES']}. Este episodio no termina la campaña.",
                ),
                "after persona-outro",
            )
        )
    if authored.get("actTransition"):
        result.append(
            add(
                "act-turning-point",
                authored["actTransition"],
                "after next-episode",
                "collection-narrator",
            )
        )
    finale = episode.get("finaleContract")
    if finale:
        result += [
            add("route-choice", finale["choicePrompt"], "route-selection active; no progress write"),
            add("campaign-complete", finale["completionMessage"], "after persona-outro"),
        ]
        for route in finale["routeChoices"]:
            result.append(add(f"choose-{route['id']}", route["choiceLabel"],
                              "route-selection active; selectable without prior completion"))
            target = route["successor"]
            recommendation = {
                locale: (f"{target['title'][locale]} ({target['publicId']}). " if target else "")
                + route["chronologyWarning"][locale]
                for locale in ("en", "es-ES")
            }
            result.append(add(f"next-campaign-{route['id']}", recommendation,
                              f"after campaign-complete; selected or accumulated route {route['id']}"))
    return result


def build_dossier(campaign, selection, authored, profile, next_selection, baseline=None):
    cid = campaign["campaignId"]
    plan = map_plan(cid, selection, authored, profile)
    world, objectives = world_and_objectives(cid, selection, authored, plan["hubs"])
    draft = {
        "id": selection["id"],
        "order": selection["order"],
        "actId": selection["actId"],
        "title": selection["title"],
        "dateRange": selection["date"],
        "event": authored["factualIntro"],
        "historicalOutcome": authored["factualOutro"],
        "sourcePassages": ([{
            "classification": "architect interpretation; independent historical approval pending",
            "selectedClaim": selection["historicalSelection"]["selectedClaim"],
            "architectCorrection": selection["historicalSelection"]["architectCorrection"],
        }] if selection["historicalSelection"].get("architectCorrection") else []) + [
            selection["historicalSelection"].get(
                "sourceConsultation", selection["historicalSelection"]
            )
        ]
        + selection["historicalSelection"].get("additionalConsultations", []),
        "knowledgeBasis": selection["knowledgeBasis"],
        "coreMechanic": selection["coreMechanic"],
        "geographyId": selection["geographyId"],
        "mapSize": authored["mapSize"],
        "mapPlan": plan,
        "worldContract": world,
        "objectivePlan": objectives,
        "goals": [o["text"] for o in objectives],
        "historicalBrief": authored["factualIntro"],
        "sourceIds": [f"odyssey-source.{cid}.{selection['id']}"],
        "dramatizationNotice": authored["dramatizationNotice"],
        "historicalPersonPolicy": selection["historicalPersonPolicy"],
        "editorialReviewNotes": authored.get("editorialReviewNotes", []),
        "status": "authored-dossier; source approval, map geometry, native capabilities and game balance pending",
        "artDirection": authored["artDirection"],
        "failureRecovery": authored["failureRecovery"],
        "requiredCapabilities": authored["requiredCapabilities"],
        "qa": {
            "staticStatus": "checked separately by dossier validator",
            "nativeStatus": "pending",
            "gameVerified": False,
            "cases": authored["qaCases"]
            + [
                "skip all optional objectives and win at each difficulty",
                "complete all optionals at each difficulty without spending protected recovery stock",
                "save/load before and after every delivery, payment, optional reward and terminal latch",
                "lose an optional identity: only that task fails",
                "test every corridor and receiving footprint in the real map",
            ],
        },
    }
    if "transportPlan" in authored:
        draft["transportPlan"] = copy.deepcopy(authored["transportPlan"])
        draft["transportPlan"]["capacityByCarrier"] = {
            entity: row["capacity"]
            for row in draft["transportPlan"].pop("carrierGroups")
            for entity in world["objectGroups"][row["group"]]
        }
    recipes = []
    for task in authored["optionalTasks"]:
        if task["kind"] in ("scout", "watch", "guide") and "information" not in task:
            raise ValueError(
                "Expanded information task requires its authored real target and bilingual benefit"
            )
        recipes.append(
            {
                "kind": task["kind"],
                "title": task["title"],
                "subject": task["subject"],
                "rationale": task["rationale"],
                "corridorIds": task["corridorIds"],
                **({"placement": copy.deepcopy(task["placement"])} if "placement" in task else {}),
                **(
                    {"information": copy.deepcopy(task["information"])}
                    if "information" in task
                    else {}
                ),
            }
        )
    draft["secondaryObjectives"] = build_optional_objectives(draft, recipes)
    rewards = total([REWARDS[task["kind"]] for task in authored["optionalTasks"]])
    costs = total([COSTS.get(task["kind"], {}) for task in authored["optionalTasks"]])
    draft["secondaryBudget"] = {
        "reservedRewards": rewards,
        "maxOptionalCosts": costs,
        "reallocatedCacheAllowance": amounts({"food": 600, "wood": 300, "gold": 150}),
        "fundingPolicy": "reward stock is segregated from the finite total bank; no duplicate caches",
        "nativeStatus": "design-only; requires certified reusable predicates and native QA",
    }
    draft["difficulty"] = difficulty_profiles(authored, rewards, costs)
    draft["playstyles"] = copy.deepcopy(authored["playstyles"])
    draft["gameplayIdentity"] = copy.deepcopy(authored.get("gameplayIdentity", {}))
    if "oppositionPlan" in authored:
        draft["oppositionPlan"] = copy.deepcopy(authored["oppositionPlan"])
        for roster in draft["oppositionPlan"]["byDifficulty"].values():
            roster["initialEntityIds"] = [
                entity
                for key, count in roster.pop("initialGroups").items()
                for entity in world["objectGroups"][key][:count]
            ]
    draft["stateMachine"] = {
        "states": ["briefing"]
        + [o["phase"] for o in objectives]
        + ["victory", "defeat"],
        "phaseTransitions": [
            {"from": "briefing", "to": "phase-1", "on": "intro-accepted"}
        ]
        + [
            {
                "from": o["phase"],
                "to": objectives[i + 1]["phase"]
                if i + 1 < len(objectives)
                else "victory",
                "on": "objective-latched",
                "objectiveId": o["id"],
            }
            for i, o in enumerate(objectives)
        ],
        "terminalPriority": "defeat first; close side rewards; one terminal latch",
        "saveLoad": "persist object identities, arrivals, collected facts, receipts, phase elapsed time and side reward balances",
        "campaignProgressWrite": False,
    }
    if authored.get("entry"):
        draft["entryContract"] = build_entry(campaign, selection, authored["entry"], baseline)
    if authored.get("finale"):
        finale = build_finale(campaign, selection, authored["finale"], baseline)
        draft["finaleContract"] = finale
        machine = draft["stateMachine"]
        machine["campaignProgressWrite"] = True
        machine["states"].insert(-2, "route-selection")
        machine["phaseTransitions"][-1]["to"] = "route-selection"
        machine["phaseTransitions"].append({
            "from": "route-selection", "to": "victory", "on": "valid-route-selected",
        })
    draft["screens"] = dossier_screens(
        cid,
        selection,
        authored,
        draft,
        campaign["editorialContract"]["narratorId"],
        next_selection,
    )
    return draft
