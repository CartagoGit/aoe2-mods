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
from secondary import RESOURCES, bilingual, build_optional_objectives

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
            "roughDurationMinutes": authored.get("durationMinutesByDifficulty", {}).get(level, duration),
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
    if episode.get("deadlinePlan"):
        result += [
            add("deadline-help", authored["deadlinePlan"]["helpText"], "briefing before clock starts; help repeatable"),
            add("deadline-warning", authored["deadlinePlan"]["warningText"],
                "authored phase warning once; remaining game time, never dialogue wall time"),
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
        **{
            key: copy.deepcopy(authored[key])
            for key in ("presencePlan", "checkpointPresencePlan", "deadlinePlan")
            if authored.get(key)
        },
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
                **({"instruction": copy.deepcopy(task["instruction"])} if "instruction" in task else {}),
                **({"placement": copy.deepcopy(task["placement"])} if "placement" in task else {}),
                **(
                    {"information": copy.deepcopy(task["information"])}
                    if "information" in task
                    else {}
                ),
                **(
                    {"resourceReward": copy.deepcopy(task["resourceReward"])}
                    if "resourceReward" in task
                    else {}
                ),
            }
        )
    draft["secondaryObjectives"] = build_optional_objectives(draft, recipes)
    rewards = total([
        effect.get("resources", {})
        for objective in draft["secondaryObjectives"]
        for effect in objective["effects"]
    ])
    costs = total([
        requirement.get("resources", {})
        for objective in draft["secondaryObjectives"]
        for requirement in objective["predicate"]["requirements"]
        if requirement["kind"] == "atomic-payment"
    ])
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


FULFILLMENT_BLUEPRINT_FIELDS = {
    "designProfile", "episodeId", "referenceCapabilityProfile", "accountsByDifficulty",
    "mapSize", "hubs", "pointZoneBindings", "recipeBindings", "serviceBindings",
    "planScreenIds", "screens", "dossierMetadata",
}
FULFILLMENT_METADATA_FIELDS = {
    "factualIntro", "factualOutro", "dramatizationNotice", "mapPlan",
    "historicalMaterialPolicyByEntity", "artDirection", "failureRecovery",
    "requiredCapabilities", "qaCases", "playstyles", "gameplayIdentity",
    "editorialReviewNotes", "screenRoles", "continuation",
}
FULFILLMENT_MAP_FIELDS = {
    "bbox", "terrainProfile", "orientation", "projection", "hubs", "points",
    "corridors", "terrainInstructions", "geographicLayers", "geometryStatus", "asset",
    "corridorStraightLengthsTiles", "interestSpacingTiles", "minimumUsableAreaFraction",
    "activeAreaPolicy", "schematicWaterControl", "performanceBudget", "sourceBindings",
}
FULFILLMENT_SCREEN_ROLES = {
    "title", "factualIntro", "handover", "personalIntro", "factualOutro",
    "personalOutro", "defeat", "continuation",
}


def _require_exact_keys(value, expected, label, episode_id):
    if not isinstance(value, dict):
        raise ValueError(f"{episode_id}: {label} must be an object")
    missing, extra = expected - set(value), set(value) - expected
    if missing or extra:
        raise ValueError(
            f"{episode_id}: unsupported {label} fields; missing={sorted(missing)}, unknown={sorted(extra)}"
        )


def _nonempty_bilingual(value, label, episode_id):
    if (not isinstance(value, dict) or set(value) != {"en", "es-ES"}
            or any(not isinstance(text, str) or not text.strip() for text in value.values())):
        raise ValueError(f"{episode_id}: {label} must contain nonempty exact EN/es-ES text")


def _validate_fulfillment_envelope(campaign, selection, blueprint, geography_profile,
                                   previous_selection, next_selection):
    episode_id = selection["id"]
    _require_exact_keys(blueprint, FULFILLMENT_BLUEPRINT_FIELDS, "fulfillment blueprint", episode_id)
    if blueprint["designProfile"] != "alternative-fulfillment-v3":
        raise ValueError(f"{episode_id}: unsupported designProfile {blueprint['designProfile']!r}")
    if blueprint["episodeId"] != episode_id:
        raise ValueError(f"{episode_id}: blueprint episodeId does not match selected episode")
    metadata = blueprint["dossierMetadata"]
    _require_exact_keys(metadata, FULFILLMENT_METADATA_FIELDS, "dossierMetadata", episode_id)
    for field in ("factualIntro", "factualOutro", "dramatizationNotice"):
        _nonempty_bilingual(metadata[field], field, episode_id)
    map_plan = metadata["mapPlan"]
    if not isinstance(map_plan, dict) or set(map_plan) - FULFILLMENT_MAP_FIELDS:
        unknown = sorted(set(map_plan) - FULFILLMENT_MAP_FIELDS) if isinstance(map_plan, dict) else []
        raise ValueError(f"{episode_id}: unsupported mapPlan fields {unknown}")
    required_map = {"bbox", "terrainProfile", "orientation", "projection", "hubs", "points",
                    "corridors", "terrainInstructions", "geographicLayers", "geometryStatus", "asset"}
    if required_map - set(map_plan):
        raise ValueError(f"{episode_id}: mapPlan missing fields {sorted(required_map - set(map_plan))}")
    if not isinstance(map_plan["terrainInstructions"], str) or not map_plan["terrainInstructions"].strip():
        raise ValueError(f"{episode_id}: mapPlan terrainInstructions must be authored text")
    bbox = map_plan["bbox"]
    if (not isinstance(bbox, list) or len(bbox) != 4
            or any(not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value) for value in bbox)
            or not bbox[0] < bbox[2] or not bbox[1] < bbox[3]):
        raise ValueError(f"{episode_id}: mapPlan bbox must contain four finite ordered bounds")
    if not isinstance(map_plan["hubs"], list) or not isinstance(map_plan["points"], list) or not isinstance(map_plan["corridors"], list):
        raise ValueError(f"{episode_id}: mapPlan hubs, points and corridors must be arrays")
    for row in map_plan["hubs"]:
        if not isinstance(row, dict) or set(row) != {"id", "centre", "lonLat", "name", "radiusTiles", "certainty"}:
            raise ValueError(f"{episode_id}: mapPlan hub has an incomplete or unknown shape")
    for row in map_plan["points"]:
        if not isinstance(row, dict) or set(row) != {"id", "lonLat", "tile", "name", "certainty"}:
            raise ValueError(f"{episode_id}: mapPlan point has an incomplete or unknown shape")
    for row in map_plan["corridors"]:
        if not isinstance(row, dict) or set(row) != {"id", "hubOrder", "mode", "widthTiles"}:
            raise ValueError(f"{episode_id}: mapPlan corridor has an incomplete or unknown shape")
    if map_plan["terrainProfile"] != selection["geographyId"]:
        raise ValueError(f"{episode_id}: mapPlan terrainProfile must equal selected geographyId")
    if not previous_selection or not next_selection:
        raise ValueError(f"{episode_id}: v3 composer accepts intermediate selections with real previous and next episodes only")
    continuation = metadata["continuation"]
    if (not isinstance(continuation, dict)
            or continuation.get("nextEpisodeId") != next_selection["id"]
            or continuation.get("campaignComplete") is not False):
        raise ValueError(f"{episode_id}: continuation must name the actual next selection and remain nonfinal")
    narrator_id = campaign.get("editorialContract", {}).get("narratorId")
    if not isinstance(narrator_id, str) or not narrator_id:
        raise ValueError(f"{episode_id}: selected campaign narrator is unavailable")
    return metadata, narrator_id


def _validate_fulfillment_metadata(campaign, selection, blueprint, metadata, narrator_id,
                                   geography_profile):
    episode_id = selection["id"]
    map_plan = metadata["mapPlan"]
    profile = blueprint["referenceCapabilityProfile"]
    if not isinstance(profile, dict) or profile.get("schemaVersion") != 3:
        raise ValueError(f"{episode_id}: referenceCapabilityProfile must explicitly have schemaVersion 3")
    entities = profile.get("worldContract", {}).get("entities", [])
    entity_ids = {row.get("id") for row in entities if isinstance(row, dict)}
    policies = metadata["historicalMaterialPolicyByEntity"]
    if (not isinstance(policies, dict) or set(policies) != entity_ids
            or any(not isinstance(value, str) or not value.strip() for value in policies.values())):
        raise ValueError(f"{episode_id}: historicalMaterialPolicyByEntity must exactly cover main-world entities")
    if not isinstance(metadata["failureRecovery"], dict) or not metadata["failureRecovery"] or any(
        not isinstance(value, str) or not value.strip() for value in metadata["failureRecovery"].values()
    ):
        raise ValueError(f"{episode_id}: failureRecovery requires named documentary policies")
    if not isinstance(metadata["gameplayIdentity"], dict) or not metadata["gameplayIdentity"]:
        raise ValueError(f"{episode_id}: gameplayIdentity requires documentary policies")
    for field in ("problem", "decision", "density", "replay"):
        if not isinstance(metadata["gameplayIdentity"].get(field), str) or not metadata["gameplayIdentity"][field].strip():
            raise ValueError(f"{episode_id}: gameplayIdentity requires authored {field} policy")
    if not isinstance(metadata["editorialReviewNotes"], dict):
        raise ValueError(f"{episode_id}: editorialReviewNotes must be a documentary object")
    art = metadata["artDirection"]
    if (not isinstance(art, dict) or art.get("productionApproved") is not False
            or not all(key in art for key in ("style", "historicalControls", "referenceAssets"))):
        raise ValueError(f"{episode_id}: artDirection must remain documentary with productionApproved=false")
    capabilities = metadata["requiredCapabilities"]
    if not isinstance(capabilities, list) or not capabilities:
        raise ValueError(f"{episode_id}: requiredCapabilities must be a nonempty list")
    cap_ids = [row.get("id") for row in capabilities if isinstance(row, dict)]
    if len(cap_ids) != len(capabilities) or len(set(cap_ids)) != len(cap_ids):
        raise ValueError(f"{episode_id}: requiredCapabilities need unique ids")
    for row in capabilities:
        if not isinstance(row.get("status"), str) or any(token in row["status"].lower() for token in ("native approved", "game verified", "production approved")):
            raise ValueError(f"{episode_id}: capability status cannot claim native/game approval")
    if not isinstance(metadata["qaCases"], list) or not metadata["qaCases"] or any(
        not isinstance(case, str) or not case.strip() for case in metadata["qaCases"]
    ):
        raise ValueError(f"{episode_id}: qaCases must be explicit nonempty authored cases")
    playstyles = metadata["playstyles"]
    if not isinstance(playstyles, list) or len(playstyles) < 3:
        raise ValueError(f"{episode_id}: at least three authored playstyles are required")
    side_ids = {row.get("id") for row in profile.get("secondaryObjectives", []) if isinstance(row, dict)}
    playstyle_ids = []
    for style in playstyles:
        if not isinstance(style, dict) or set(style) != {"id", "optionalObjectives", "costOfOpportunity", "mainObjectivesUnchanged", "historicalOutcomeUnchanged"}:
            raise ValueError(f"{episode_id}: playstyle shape is incomplete or has unknown fields")
        playstyle_ids.append(style["id"])
        if (style["mainObjectivesUnchanged"] is not True or style["historicalOutcomeUnchanged"] is not True
                or not isinstance(style["optionalObjectives"], list)
                or len(style["optionalObjectives"]) != len(set(style["optionalObjectives"]))
                or not isinstance(style["costOfOpportunity"], str) or not style["costOfOpportunity"].strip()
                or not set(style["optionalObjectives"]) <= side_ids):
            raise ValueError(f"{episode_id}: playstyle {style['id']} has invalid optional references or changes fixed outcomes")
    if len(set(playstyle_ids)) != len(playstyle_ids):
        raise ValueError(f"{episode_id}: playstyle ids must be distinct")
    portfolio_signatures = {
        frozenset(style["optionalObjectives"]) for style in playstyles
    }
    if len(portfolio_signatures) != len(playstyles):
        raise ValueError(f"{episode_id}: playstyle portfolios must be distinct")

    screens = blueprint["screens"]
    if not isinstance(screens, list) or not screens:
        raise ValueError(f"{episode_id}: authored screens are required")
    screen_map = {row.get("id"): row for row in screens if isinstance(row, dict)}
    if len(screen_map) != len(screens):
        raise ValueError(f"{episode_id}: screen ids must be unique")
    roles = metadata["screenRoles"]
    if not isinstance(roles, dict) or set(roles) != FULFILLMENT_SCREEN_ROLES:
        raise ValueError(f"{episode_id}: screenRoles must contain exactly {sorted(FULFILLMENT_SCREEN_ROLES)}")
    role_order = [roles[key] for key in ("title", "factualIntro", "handover", "personalIntro")]
    if [row.get("id") for row in screens[:4]] != role_order:
        raise ValueError(f"{episode_id}: first four screens must bind title/factualIntro/handover/personalIntro in order")
    if any(screen_id not in screen_map for screen_id in roles.values()):
        raise ValueError(f"{episode_id}: screenRoles contains an unknown screen ID")
    if len(set(roles.values())) != len(roles):
        raise ValueError(f"{episode_id}: all eight screenRoles must use distinct screen IDs")
    for role, text_field in (("factualIntro", "factualIntro"), ("factualOutro", "factualOutro")):
        _nonempty_bilingual(metadata[text_field], text_field, episode_id)
        if screen_map[roles[role]].get("text") != metadata[text_field]:
            raise ValueError(f"{episode_id}: {role} screen text must equal dossierMetadata.{text_field}")
    for role in ("factualIntro", "factualOutro", "handover"):
        if screen_map[roles[role]].get("narrator") != "collection-narrator":
            raise ValueError(f"{episode_id}: {role} screen must use collection-narrator")
    for role in ("personalIntro", "personalOutro"):
        if screen_map[roles[role]].get("narrator") != narrator_id:
            raise ValueError(f"{episode_id}: {role} screen must use the selected campaign narrator")
    continuation = metadata["continuation"]
    if (not isinstance(continuation, dict) or set(continuation) != {"nextEpisodeId", "campaignComplete", "sourceScreenId"}
            or continuation["campaignComplete"] is not False or continuation["sourceScreenId"] != roles["continuation"]):
        raise ValueError(f"{episode_id}: continuation must be an explicit nonfinal next-episode screen")
    return map_plan


def build_fulfillment_dossier(campaign, selection, blueprint, projection, geography_profile,
                              previous_selection, next_selection, baseline=None):
    """Compose only the closed intermediate v3 design envelope, never legacy mechanics."""
    metadata, narrator_id = _validate_fulfillment_envelope(
        campaign, selection, blueprint, geography_profile, previous_selection, next_selection
    )
    map_plan = _validate_fulfillment_metadata(campaign, selection, blueprint, metadata,
                                               narrator_id, geography_profile)
    episode_id = selection["id"]
    if projection.get("episodeId") != episode_id:
        raise ValueError(f"{episode_id}: typed projection episode identity mismatch")
    profile = projection["referenceCapabilityProfile"]
    for key, view in (("worldContract", "worldContract"), ("objectivePlan", "objectivePlan"),
                      ("stateMachine", "stateMachine"), ("secondaryObjectives", "secondaryObjectives"),
                      ("secondaryBudget", "secondaryBudget")):
        if projection[view] != profile[key]:
            raise ValueError(f"{episode_id}: projected {view} has drifted from referenceCapabilityProfile")
    points = map_plan["points"]
    point_by_id = {row["id"]: row for row in points}
    if len(point_by_id) != len(points):
        raise ValueError(f"{episode_id}: duplicate authored map point ID")
    bindings_by_point = {row["pointId"]: row for row in blueprint["pointZoneBindings"]}
    if len(bindings_by_point) != len(blueprint["pointZoneBindings"]):
        raise ValueError(f"{episode_id}: duplicate pointZoneBinding pointId")
    if set(bindings_by_point) - set(point_by_id):
        raise ValueError(f"{episode_id}: pointZoneBinding references unknown mapPlan.points ID")
    for point_id, binding in bindings_by_point.items():
        if point_by_id[point_id]["tile"] != binding["tile"]:
            raise ValueError(f"{episode_id}: point {point_id} tile differs from authored mapPlan.points tile")
    if not isinstance(blueprint["hubs"], list) or len(blueprint["hubs"]) != len(map_plan["hubs"]):
        raise ValueError(f"{episode_id}: projected hub list does not match mapPlan.hubs")
    projected_hubs = {row["id"]: row["centre"] for row in blueprint["hubs"]}
    authored_hubs = {row["id"]: row["centre"] for row in map_plan["hubs"]}
    if projected_hubs != authored_hubs:
        raise ValueError(f"{episode_id}: projected hubs differ from mapPlan.hubs IDs/centres")
    region_bbox = geography_profile["bbox"]
    bbox = map_plan["bbox"]
    if not (region_bbox[0] <= bbox[0] < bbox[2] <= region_bbox[2]
            and region_bbox[1] <= bbox[1] < bbox[3] <= region_bbox[3]):
        raise ValueError(f"{episode_id}: mapPlan bbox is outside the selected geographic profile")
    for label, rows in (("hub", map_plan["hubs"]), ("point", points)):
        for row in rows:
            expected = tile_point(bbox, row["lonLat"], blueprint["mapSize"])
            actual = row["centre"] if label == "hub" else row["tile"]
            if actual != expected:
                raise ValueError(f"{episode_id}: {label} {row['id']} tile does not match authored lonLat and map frame")
            if (not isinstance(actual, list) or len(actual) != 2
                    or any(not isinstance(value, (int, float)) or isinstance(value, bool)
                           or not math.isfinite(value) or value < 0 or value > blueprint["mapSize"] - 1
                           for value in actual)):
                raise ValueError(f"{episode_id}: {label} {row['id']} lies outside map tile bounds")
            if label == "hub":
                radius = row["radiusTiles"]
                if (not isinstance(radius, (int, float)) or isinstance(radius, bool)
                        or not math.isfinite(radius) or radius < 0
                        or any(value - radius < 0 or value + radius > blueprint["mapSize"] - 1
                               for value in actual)):
                    raise ValueError(f"{episode_id}: hub {row['id']} footprint outside map tile bounds")
    hub_ids = set(authored_hubs)
    corridor_ids = set()
    for corridor in map_plan["corridors"]:
        if corridor["id"] in corridor_ids:
            raise ValueError(f"{episode_id}: duplicate corridor ID {corridor['id']}")
        corridor_ids.add(corridor["id"])
        if (corridor["mode"] not in ("land", "water") or not isinstance(corridor["widthTiles"], (int, float))
                or isinstance(corridor["widthTiles"], bool) or not math.isfinite(corridor["widthTiles"])
                or corridor["widthTiles"] <= 0 or len(corridor["hubOrder"]) < 2
                or any(hub not in hub_ids for hub in corridor["hubOrder"])):
            raise ValueError(f"{episode_id}: corridor {corridor['id']} has invalid hubOrder, mode or width")
    for side in profile.get("secondaryObjectives", []):
        reachability = side.get("reachability", {})
        if (reachability.get("originHub") not in hub_ids
                or reachability.get("receivingHub") not in hub_ids
                or not set(reachability.get("corridorIds", [])) <= corridor_ids):
            raise ValueError(f"{episode_id}: optional task {side.get('id')} references an undeclared hub or corridor")
        for effect in side.get("effects", []):
            if effect.get("kind") == "mark-alternative-route" and effect.get("corridorId") not in corridor_ids:
                raise ValueError(f"{episode_id}: optional task {side.get('id')} references an undeclared information corridor")
    for key in ("factualIntro", "factualOutro", "dramatizationNotice"):
        _nonempty_bilingual(metadata[key], key, episode_id)
    source_passages = ([{
        "classification": "architect interpretation; independent historical approval pending",
        "selectedClaim": selection["historicalSelection"]["selectedClaim"],
        "architectCorrection": selection["historicalSelection"]["architectCorrection"],
    }] if selection["historicalSelection"].get("architectCorrection") else []) + [
        selection["historicalSelection"].get("sourceConsultation", selection["historicalSelection"])
    ] + selection["historicalSelection"].get("additionalConsultations", [])
    screens = blueprint["screens"]
    return {
        "designProfile": blueprint["designProfile"],
        "id": episode_id,
        "order": selection["order"],
        "actId": selection["actId"],
        "title": selection["title"],
        "dateRange": selection["date"],
        "event": metadata["factualIntro"],
        "historicalOutcome": metadata["factualOutro"],
        "historicalBrief": metadata["factualIntro"],
        "dramatizationNotice": metadata["dramatizationNotice"],
        "sourcePassages": source_passages,
        "knowledgeBasis": selection["knowledgeBasis"],
        "coreMechanic": selection["coreMechanic"],
        "geographyId": selection["geographyId"],
        "mapSize": blueprint["mapSize"],
        "mapPlan": map_plan,
        "authoringPresentationBindings": {
            "recipeBindings": copy.deepcopy(blueprint["recipeBindings"]),
            "serviceBindings": copy.deepcopy(blueprint["serviceBindings"]),
            "planScreenIds": copy.deepcopy(blueprint["planScreenIds"]),
        },
        "mapBindings": projection["mapBindings"],
        "referenceCapabilityProfile": profile,
        "worldContract": projection["worldContract"],
        "objectivePlan": projection["objectivePlan"],
        "goals": [objective["text"] for objective in projection["objectivePlan"]],
        "stateMachine": projection["stateMachine"],
        "secondaryObjectives": projection["secondaryObjectives"],
        "secondaryBudget": projection["secondaryBudget"],
        "fulfillmentServices": projection["fulfillmentServices"],
        "selectionAnalysisByDifficulty": projection["selectionAnalysisByDifficulty"],
        "optionalFinancialInputs": projection["optionalFinancialInputs"],
        "difficulty": copy.deepcopy(projection["selectionAnalysisByDifficulty"]),
        "optionalPrefixAnalysisByDifficulty": projection["optionalPrefixAnalysisByDifficulty"],
        "planScreenIds": projection["planScreenIds"],
        "accountsByDifficulty": blueprint["accountsByDifficulty"],
        "sourceIds": [f"odyssey-source.{campaign['campaignId']}.{episode_id}"],
        "historicalPersonPolicy": selection["historicalPersonPolicy"],
        "historicalMaterialPolicyByEntity": metadata["historicalMaterialPolicyByEntity"],
        "artDirection": metadata["artDirection"],
        "failureRecovery": metadata["failureRecovery"],
        "requiredCapabilities": metadata["requiredCapabilities"],
        "qa": {"staticStatus": "typed v3 profile and dossier bindings checked", "nativeStatus": "pending", "gameVerified": False, "cases": metadata["qaCases"]},
        "playstyles": metadata["playstyles"],
        "gameplayIdentity": metadata["gameplayIdentity"],
        "editorialReviewNotes": metadata["editorialReviewNotes"],
        "screens": screens,
        "screenRoles": metadata["screenRoles"],
        "continuation": metadata["continuation"],
        "status": "authored-dossier; source approval, map geometry, native capabilities and game balance pending",
    }
