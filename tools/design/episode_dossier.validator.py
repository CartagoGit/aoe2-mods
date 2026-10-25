"""Check authored episode contracts without asserting native behavior or balance."""

import math
import runpy
from pathlib import Path
from secondary import check_optional_objectives, audit_objective_numbers

continuity = runpy.run_path(str(Path(__file__).with_name("odyssey_continuity.helper.py")))
transport = runpy.run_path(str(Path(__file__).with_name("transport_journey.helper.py")))
audit_finale = continuity["audit_finale"]
audit_entry = continuity["audit_entry"]


def audit_dossier(episode, campaign=None, baseline=None):
    if "designProfile" in episode:
        if episode.get("designProfile") != "alternative-fulfillment-v3":
            return [f"{episode.get('id', 'unknown-episode')}: unsupported designProfile {episode.get('designProfile')!r}"]
        return audit_fulfillment_dossier(episode)
    failures = audit_objective_numbers(episode)
    if failures:
        return failures

    def check(condition, message):
        if not condition:
            failures.append(message)

    label = episode["id"]
    check(
        300 <= episode["mapSize"] <= 400,
        f"{label}: historical map outside 300–400 range",
    )
    for field in ("event", "historicalOutcome", "title", "dramatizationNotice"):
        check(
            set(episode[field]) == {"en", "es-ES"} and all(episode[field].values()),
            f"{label}: missing bilingual {field}",
        )
    entities = {e["id"]: e for e in episode["worldContract"]["entities"]}
    zones = {z["id"]: z for z in episode["worldContract"]["zones"]}
    check(
        len(entities) == len(episode["worldContract"]["entities"]),
        f"{label}: duplicate main identity",
    )
    check(
        all(entity.get("historicalMaterialPolicy") for entity in entities.values()),
        f"{label}: missing fictional material chronology policy",
    )
    check(
        len(zones) == len(episode["worldContract"]["zones"]),
        f"{label}: duplicate main zone",
    )
    objectives = {o["id"]: o for o in episode["objectivePlan"]}
    check(
        len(objectives) == len(episode["objectivePlan"]),
        f"{label}: duplicate main objective",
    )
    failures.extend(audit_finale(episode, campaign, baseline))
    failures.extend(audit_entry(episode, campaign, baseline))
    check(
        episode["qa"]["gameVerified"] is False,
        f"{label}: design promoted to game verification",
    )
    for position, objective in enumerate(episode["objectivePlan"]):
        context = f"{label}/{objective['id']}"
        check(
            objective["after"]
            == (
                [] if position == 0 else [episode["objectivePlan"][position - 1]["id"]]
            ),
            f"{context}: broken main dependency",
        )
        check(
            objective["predicate"]["operator"] == "all",
            f"{context}: compound predicate reduced to alternatives",
        )
        requirements = {r["id"]: r for r in objective["predicate"]["requirements"]}
        check(
            len(requirements) == len(objective["predicate"]["requirements"]),
            f"{context}: duplicate main requirement",
        )
        for req in requirements.values():
            if req["kind"] == "current-entity-presence":
                check(
                    len(set(req["entities"])) == len(req["entities"])
                    and set(req["entities"]) <= set(entities)
                    and 0 < req["requiredCount"] <= len(req["entities"])
                    and set(req.get("destinations", {})) == set(req["entities"])
                    and set(req.get("destinations", {}).values()) <= set(zones),
                    f"{context}: invalid current presence identities or zones",
                )
                capability = next(
                    (c for c in episode["requiredCapabilities"]
                     if c["id"] == "live-entity-presence"), None
                )
                check(
                    req.get("observable") == "current-alive-position"
                    and req.get("reevaluateBeforeTerminal") is True
                    and req.get("deliveryLedgerSubstitute") is False
                    and req.get("implementationStatus") == "unimplemented"
                    and req.get("proposalId") == "i00005"
                    and capability is not None
                    and capability.get("status") == "reference model implemented; native implementation pending",
                    f"{context}: current presence needs its unimplemented capability gate",
                )
            elif req["kind"] == "checkpoint-entity-presence":
                check(
                    len(set(req["entities"])) == len(req["entities"])
                    and set(req["entities"]) <= set(entities)
                    and 0 < req["requiredCount"] <= len(req["entities"])
                    and set(req.get("destinations", {})) == set(req["entities"])
                    and set(req.get("destinations", {}).values()) <= set(zones),
                    f"{context}: invalid checkpoint presence identities or zones",
                )
                check(
                    not any(
                        transition.get("to") == "victory"
                        and transition.get("objectiveId") == objective["id"]
                        for transition in episode["stateMachine"]["phaseTransitions"]
                    ),
                    f"{context}: checkpoint presence must be an intermediate objective",
                )
                capability = next(
                    (c for c in episode["requiredCapabilities"]
                     if c["id"] == "checkpoint-entity-presence"), None
                )
                check(
                    req.get("observable") == "current-alive-position"
                    and req.get("latchAtObjectiveCompletion") is True
                    and req.get("deliveryLedgerSubstitute") is False
                    and req.get("implementationStatus") == "unimplemented"
                    and req.get("proposalId") == "i00006"
                    and capability is not None
                    and capability.get("status") == "reference model implemented; native implementation pending",
                    f"{context}: checkpoint presence needs its i00006 pending gate",
                )
            elif req["kind"] == "entity-state":
                check(
                    len(set(req["entities"])) == len(req["entities"]),
                    f"{context}: duplicate entity in counter",
                )
                check(
                    set(req["entities"]) <= set(entities)
                    and req["requiredCount"] <= len(req["entities"]),
                    f"{context}: impossible counter",
                )
                if req["state"] == "arrived":
                    check(
                        set(req.get("destinations", {})) == set(req["entities"]),
                        f"{context}: incomplete receiving map",
                    )
                    check(
                        set(req.get("destinations", {}).values()) <= set(zones),
                        f"{context}: unknown receiving zone",
                    )
                    for eid, zid in req.get("destinations", {}).items():
                        if eid not in entities or zid not in zones:
                            continue
                        entity, zone = entities[eid], zones[zid]
                        check(
                            entity["initialHub"] != zone["hub"]
                            or math.dist(entity["offsetTiles"], zone["offsetTiles"])
                            > zone["radiusTiles"],
                            f"{context}: initial arrival incorrectly counts",
                        )
                if req.get("eligibleEntitiesFromLedger"):
                    ref = req["eligibleEntitiesFromLedger"]
                    source = objectives.get(ref["objective"])
                    ledgers = (
                        source["predicate"].get("exportedLedgers", []) if source else []
                    )
                    ledger = next(
                        (l for l in ledgers if l["id"] == ref["ledger"]), None
                    )
                    check(
                        ledger is not None, f"{context}: missing prior recipient ledger"
                    )
                    source_position = next(
                        (
                            i
                            for i, o in enumerate(episode["objectivePlan"])
                            if o["id"] == ref["objective"]
                        ),
                        len(objectives),
                    )
                    check(
                        source_position < position,
                        f"{context}: recipient ledger is not from a prior objective",
                    )
                    if ledger:
                        arrival_sets = [
                            set(r["entities"])
                            for r in source["predicate"]["requirements"]
                            if r["id"] in ledger["fromRequirements"]
                            and (r["kind"] == "transport-journey" or
                                 (r["kind"] == "entity-state" and r["state"] == "arrived"))
                        ]
                        common = (
                            set.intersection(*arrival_sets) if arrival_sets else set()
                        )
                        check(
                            len(arrival_sets) == len(ledger["fromRequirements"])
                            and set(req["entities"]) <= common
                            and ledger["minimumCount"] >= req["requiredCount"],
                            f"{context}: recipient identities escape supplied intersection",
                        )
                if req.get("arrivalAfterDeparture"):
                    ref = req["arrivalAfterDeparture"]
                    source = objectives.get(ref["objective"])
                    departure = (
                        next(
                            (
                                r
                                for r in source["predicate"]["requirements"]
                                if r["id"] == ref["requirement"]
                            ),
                            None,
                        )
                        if source
                        else None
                    )
                    source_index = next(
                        (
                            i
                            for i, o in enumerate(episode["objectivePlan"])
                            if o["id"] == ref["objective"]
                        ),
                        len(objectives),
                    )
                    check(
                        req["state"] == "arrived"
                        and source_index <= position
                        and departure is not None
                        and departure["kind"] == "ordered-departure"
                        and set(req["entities"]) <= set(departure["departingEntities"]),
                        f"{context}: arrival lacks exact prior departing identities",
                    )
            elif req["kind"] == "resource-transaction":
                check(
                    len(set(req["receivingZones"])) == len(req["receivingZones"])
                    and set(req["receivingZones"]) <= set(zones),
                    f"{context}: invalid payment receivers",
                )
                check(
                    req.get("atomic") is True
                    and req["once"] is True
                    and req["account"] == "spendable",
                    f"{context}: unsafe payment transaction",
                )
                check(
                    set(req["allocations"]) == set(req["receivingZones"]),
                    f"{context}: incomplete payment receivers",
                )
                for resource in ("food", "wood", "gold", "stone"):
                    check(
                        sum(v.get(resource, 0) for v in req["allocations"].values())
                        == req["amounts"].get(resource, 0),
                        f"{context}: payment allocations not conserved",
                    )
            elif req["kind"] == "derived-token":
                check(
                    set(req["inputEntities"]) <= set(entities)
                    and set(req["outputEntities"]) <= set(entities),
                    f"{context}: broken derived identity",
                )
                collected = {
                    eid
                    for earlier in episode["objectivePlan"][: position + 1]
                    for r in earlier["predicate"]["requirements"]
                    if r["kind"] == "entity-state" and r["state"] == "collected"
                    for eid in r["entities"]
                }
                check(
                    set(req["inputEntities"]) <= collected,
                    f"{context}: derivation without input collection",
                )
                for receipt in req.get("requiredPaymentReceipts", []):
                    producers = [
                        (index, source, payment)
                        for index, source in enumerate(episode["objectivePlan"])
                        for payment in source["predicate"]["requirements"]
                        if payment["kind"] == "resource-transaction"
                        and payment["paidFlag"] == receipt["flag"]
                    ]
                    check(
                        len(producers) == 1,
                        f"{context}: derived payment needs one producer",
                    )
                    if len(producers) != 1:
                        continue
                    source_index, source, payment = producers[0]
                    check(
                        source_index <= position,
                        f"{context}: derived payment comes from a future objective",
                    )
                    check(
                        source["id"] == receipt["fromObjective"]
                        and receipt.get("newDebit") is False
                        and all(
                            payment["amounts"].get(resource, 0)
                            == receipt["amounts"].get(resource, 0)
                            for resource in ("food", "wood", "gold", "stone")
                        ),
                        f"{context}: derived payment receipt amount or owner drift",
                    )
            elif req["kind"] == "transport-journey":
                transport["audit_requirement"](req, episode, position, check, context)
            elif req["kind"] == "ordered-departure":
                check(
                    len(req["departingEntities"]) == len(set(req["departingEntities"]))
                    and set(req["departingEntities"]) <= set(entities),
                    f"{context}: invalid departing identities",
                )
                source = objectives.get(req["receiptObjective"])
                source_index = next(
                    (
                        i
                        for i, o in enumerate(episode["objectivePlan"])
                        if o["id"] == req["receiptObjective"]
                    ),
                    len(objectives),
                )
                receipt = (
                    next(
                        (
                            r
                            for r in source["predicate"]["requirements"]
                            if r["id"] == req.get("receiptRequirement")
                        ),
                        None,
                    )
                    if source
                    else None
                )
                check(
                    source_index < position
                    and req["departureEnabledOnlyAfterReceipt"] is True,
                    f"{context}: departure is not gated by a prior receipt",
                )
                check(
                    receipt is not None
                    and receipt["kind"] == "entity-state"
                    and receipt["state"] == "arrived",
                    f"{context}: departure lacks an actual arrival receipt",
                )
            elif req["kind"] == "phase-deadline":
                limits = req.get("secondsByDifficulty", {})
                warning = req.get("warningSeconds")
                valid_limits = isinstance(limits, dict) and set(limits) == {"easy", "standard", "hard"} and all(
                    type(value) is int and value > 0 for value in limits.values()
                )
                check(
                    valid_limits and type(warning) is int and warning > 0
                    and warning < min(limits.values()),
                    f"{context}: invalid phase deadline limits or warning",
                )
                check(
                    req.get("phase") == objective["phase"]
                    and req.get("clock") == "relative-to-phase-entry"
                    and req.get("onExpiry") == "main-defeat"
                    and req.get("implementationStatus") == "unimplemented"
                    and req.get("proposalId") == "i00003",
                    f"{context}: phase deadline needs its matching phase and pending native gate",
                )
            elif req["kind"] == "area-state":
                check(
                    len(req["zones"]) == len(set(req["zones"]))
                    and set(req["zones"]) <= set(zones)
                    and 0 < req["requiredCount"] <= len(req["zones"]),
                    f"{context}: impossible route observation",
                )
                check(
                    req["state"] in ("visited-and-passable", "controlled-and-passable"),
                    f"{context}: unknown route observation state",
                )
                check(
                    set(req.get("blockingEnemies", [])) <= set(entities),
                    f"{context}: undefined route blocker",
                )
                until = req.get("mustRemainUntilObjective")
                if until:
                    future = next((i for i, row in enumerate(episode["objectivePlan"])
                                   if row["id"] == until), -1)
                    check(future > position and req["state"] == "controlled-and-passable",
                          f"{context}: invalid continuous control interval")
            else:
                check(False, f"{context}: unsupported dossier predicate {req['kind']}")
    presence = episode.get("presencePlan")
    if presence:
        check(
            presence.get("capabilityId") == "live-entity-presence"
            and presence.get("implementationStatus") == "unimplemented"
            and presence.get("proposalId") == "i00005"
            and presence.get("evaluation") == "current state before terminal latch, not historical arrivals",
            f"{label}: current presence plan needs its unimplemented capability gate",
        )
        bindings = presence.get("bindings", [])
        check(bool(bindings), f"{label}: current presence plan has no bindings")
        for binding in bindings:
            objective = objectives.get(binding.get("objective"))
            requirement = next(
                (r for r in objective["predicate"]["requirements"]
                 if r["id"] == binding.get("requirement")), None
            ) if objective else None
            check(
                requirement is not None
                and requirement["kind"] == "current-entity-presence",
                f"{label}: current presence replaced with delivery history",
            )
    checkpoint_bindings = [
        {"objective": objective["id"], "requirement": req["id"]}
        for objective in episode["objectivePlan"]
        for req in objective["predicate"]["requirements"]
        if req["kind"] == "checkpoint-entity-presence"
    ]
    checkpoint_plan = episode.get("checkpointPresencePlan")
    if checkpoint_bindings:
        checkpoint_capability = next(
            (c for c in episode["requiredCapabilities"]
             if c["id"] == "checkpoint-entity-presence"), None
        )
        check(
            checkpoint_plan is not None
            and checkpoint_plan.get("capabilityId") == "checkpoint-entity-presence"
            and checkpoint_plan.get("implementationStatus") == "unimplemented"
            and checkpoint_plan.get("proposalId") == "i00006"
            and checkpoint_plan.get("bindings") == checkpoint_bindings,
            f"{label}: checkpoint presence plan needs the exact i00006 pending gate and bindings",
        )
        check(
            checkpoint_capability is not None
            and checkpoint_capability.get("status")
            == "reference model implemented; native implementation pending",
            f"{label}: checkpoint presence capability must remain native pending",
        )
    else:
        check(
            checkpoint_plan is None,
            f"{label}: checkpoint presence plan has no matching requirement",
        )
    deadline_bindings = [
        {"objective": objective["id"], "requirement": req["id"]}
        for objective in episode["objectivePlan"]
        for req in objective["predicate"]["requirements"]
        if req["kind"] == "phase-deadline"
    ]
    deadline_plan = episode.get("deadlinePlan")
    if deadline_bindings:
        check(
            isinstance(deadline_plan, dict)
            and deadline_plan.get("capabilityId") == "phase-relative-deadline"
            and deadline_plan.get("proposalId") == "i00003"
            and deadline_plan.get("implementationStatus") == "unimplemented"
            and deadline_plan.get("bindings") == deadline_bindings,
            f"{label}: deadline plan needs exact bindings and pending native gate",
        )
        capability = next((c for c in episode["requiredCapabilities"]
                           if c["id"] == "phase-relative-deadline"), None)
        check(capability is not None and capability.get("status")
              == "reference model implemented; native implementation pending",
              f"{label}: phase deadline capability must remain native pending")
        for key in ("helpText", "warningText"):
            text = deadline_plan.get(key, {}) if isinstance(deadline_plan, dict) else {}
            check(isinstance(text, dict) and set(text) == {"en", "es-ES"} and all(text.values()),
                  f"{label}: missing bilingual deadline {key}")
    else:
        check(deadline_plan is None, f"{label}: deadline plan has no matching requirement")
    for group in episode["worldContract"]["survivorGroups"]:
        check(
            len(group["entities"]) == len(set(group["entities"])),
            f"{label}: duplicate survivor identity",
        )
        check(
            set(group["entities"]) <= set(entities)
            and group["minimumAliveOrAlreadySafe"] <= len(set(group["entities"])),
            f"{label}: impossible survival threshold",
        )
    playstyles = episode.get("playstyles", [])
    side_ids = {side["id"] for side in episode["secondaryObjectives"]}
    check(
        len(playstyles) >= 3
        and len({style["id"] for style in playstyles}) == len(playstyles),
        f"{label}: require three distinct authored playstyles",
    )
    portfolios = []
    for style in playstyles:
        portfolio = style.get("optionalObjectives", [])
        portfolios.append(frozenset(portfolio))
        check(
            bool(portfolio)
            and len(portfolio) == len(set(portfolio))
            and set(portfolio) <= side_ids
            and style.get("costOfOpportunity")
            and style.get("mainObjectivesUnchanged") is True
            and style.get("historicalOutcomeUnchanged") is True,
            f"{label}: invalid playstyle portfolio {style['id']}",
        )
    check(
        len(set(portfolios)) == len(portfolios),
        f"{label}: repeated playstyle portfolio",
    )
    screens = episode["screens"]
    keys = [s["key"] for s in screens]
    check(len(keys) == len(set(keys)), f"{label}: duplicate screen key")
    check(
        [s["id"] for s in screens[:4]]
        == ["title", "fact-intro", "handover", "persona-intro"],
        f"{label}: incorrect opening narrator sequence",
    )
    check(
        screens[1]["narrator"] == "collection-narrator"
        and screens[2]["narrator"] == "collection-narrator"
        and screens[3]["narrator"] == episode["knowledgeBasis"]["speaker"],
        f"{label}: incorrect opening narrator voice",
    )
    closing = {s["id"]: s for s in screens}
    check(
        closing["fact-outro"]["narrator"] == "collection-narrator"
        and closing["persona-outro"]["narrator"]
        == episode["knowledgeBasis"]["speaker"],
        f"{label}: incorrect closing narrator voice",
    )
    for s in screens:
        check(
            set(s["text"]) == {"en", "es-ES"} and all(s["text"].values()),
            f"{label}/{s['id']}: incomplete localization",
        )
        for locale, chunks in s.get("captionSegments", {}).items():
            check(
                " ".join(chunks) == " ".join(s["text"].get(locale, "").split())
                and all(len(chunk.split()) <= 32 for chunk in chunks),
                f"{label}/{s['id']}: caption content lost or too long",
            )
    hubs = episode["mapPlan"]["hubs"]
    hub_ids = {hub["id"] for hub in hubs}
    for corridor in episode["mapPlan"]["corridors"]:
        check(
            len(corridor["hubOrder"]) >= 2 and set(corridor["hubOrder"]) <= hub_ids,
            f"{label}: corridor has missing geographic district",
        )
    check(
        all(0 <= value < episode["mapSize"] for h in hubs for value in h["centre"]),
        f"{label}: district outside map",
    )
    check(
        all(math.dist(a["centre"], b["centre"]) > 6 for a, b in zip(hubs, hubs[1:])),
        f"{label}: main receiving districts overlap",
    )
    check(
        all(
            b["mainFeasibleSkippingAllOptionals"] and b["allOptionalCostsAffordable"]
            for b in episode["difficulty"].values()
        ),
        f"{label}: funding proof fails",
    )
    costs = {
        resource: sum(
            req.get("amounts", {}).get(resource, 0)
            for objective in episode["objectivePlan"]
            for req in objective["predicate"]["requirements"]
            if req["kind"] == "resource-transaction"
        )
        for resource in ("food", "wood", "gold", "stone")
    }
    for level, budget in episode["difficulty"].items():
        check(
            budget["mandatoryDeliveries"] == costs,
            f"{label}/{level}: main payment budget drift",
        )
    opposition = episode.get("oppositionPlan")
    if opposition:
        rosters = opposition.get("byDifficulty", {})
        check(
            set(rosters) == set(episode["difficulty"]),
            f"{label}: incomplete finite opposition profiles",
        )
        for level, roster in rosters.items():
            ids = roster["initialEntityIds"]
            check(
                len(ids) == len(set(ids)) and set(ids) <= set(entities),
                f"{label}/{level}: undefined or duplicate hostile identity",
            )
            check(
                all(
                    entities[e]["role"] == "fictional-hostile-patrol"
                    for e in ids
                    if e in entities
                ),
                f"{label}/{level}: civilian included in hostile roster",
            )
            check(
                len(ids) == episode["difficulty"][level]["enemyTotalCap"]
                and roster["productionEnabled"] is False
                and roster["mobilizations"] == [],
                f"{label}/{level}: finite opposition count or production drift",
            )
            blockers = {enemy for objective in episode["objectivePlan"]
                        for requirement in objective["predicate"]["requirements"]
                        for enemy in requirement.get("blockingEnemies", [])}
            check(blockers <= set(ids), f"{label}/{level}: mandatory blocker not instantiated")
    else:
        check(
            all(b["enemyTotalCap"] == 0 for b in episode["difficulty"].values()),
            f"{label}: enemies without explicit finite identity roster",
        )
    corridor_ids = {c["id"] for c in episode["mapPlan"]["corridors"]}
    for side in episode["secondaryObjectives"]:
        check(
            bool(side["reachability"]["corridorIds"])
            and set(side["reachability"]["corridorIds"]) <= corridor_ids,
            f"{label}/{side['id']}: undefined optional access corridor",
        )
        for effect in side["effects"]:
            if effect["kind"] == "mark-alternative-route":
                check(
                    effect.get("corridorId") in corridor_ids,
                    f"{label}/{side['id']}: undefined information corridor",
                )
            if effect["kind"] == "reveal-enemy-approach":
                check(
                    False, f"{label}/{side['id']}: undeclared enemy reserve information"
                )
    check_optional_objectives(episode, check, label)
    return failures


def audit_fulfillment_dossier(episode):
    """Audit composed v3 documentary views without treating them as runtime proof."""
    failures = []
    label = episode.get("id", "unknown-episode")

    def check(condition, message):
        if not condition:
            failures.append(f"{label}: {message}")

    profile = episode.get("referenceCapabilityProfile")
    check(isinstance(profile, dict) and profile.get("schemaVersion") == 3,
          "missing explicit v3 reference profile")
    if not isinstance(profile, dict):
        return failures
    for field in ("worldContract", "objectivePlan", "stateMachine", "secondaryObjectives", "secondaryBudget"):
        check(episode.get(field) == profile.get(field),
              f"derived {field} differs from referenceCapabilityProfile")
    check(episode.get("difficulty") == episode.get("selectionAnalysisByDifficulty"),
          "difficulty must be an exact view of selectionAnalysisByDifficulty")
    check(set(episode.get("selectionAnalysisByDifficulty", {})) == {"easy", "standard", "hard"},
          "selection analysis must cover exactly easy/standard/hard")
    check(set(episode.get("accountsByDifficulty", {})) == {"easy", "standard", "hard"},
          "authored accounts must cover exactly easy/standard/hard")
    qa = episode.get("qa") if isinstance(episode.get("qa"), dict) else {}
    check(qa.get("gameVerified") is False
          and qa.get("nativeStatus") == "pending",
          "v3 dossier cannot claim native or game verification")
    check(not any("receiptText" in row or "personaReaction" in row
                  for row in episode.get("objectivePlan", [])),
          "shared v3 objectives cannot acquire legacy receipt narration")
    check(not any(key in episode.get("difficulty", {}).get(level, {})
                  for key in ("gatherableBank", "mandatoryDeliveries", "enemyTotalCap", "roughDurationMinutes")
                  for level in ("easy", "standard", "hard")),
          "difficulty view contains legacy or unmeasured fields")
    map_plan = episode.get("mapPlan") if isinstance(episode.get("mapPlan"), dict) else {}
    map_bindings = episode.get("mapBindings") if isinstance(episode.get("mapBindings"), dict) else {}
    check(map_plan.get("terrainProfile") == episode.get("geographyId"),
          "mapPlan terrainProfile differs from selected geographyId")
    authored_hubs = map_plan.get("hubs", [])
    projected_hubs = map_bindings.get("hubs", [])
    if isinstance(authored_hubs, list) and isinstance(projected_hubs, list):
        check({row.get("id"): row.get("centre") for row in authored_hubs if isinstance(row, dict)}
              == {row.get("id"): row.get("centre") for row in projected_hubs if isinstance(row, dict)}
              and len([row for row in authored_hubs if isinstance(row, dict)]) == len(authored_hubs)
              and len([row for row in projected_hubs if isinstance(row, dict)]) == len(projected_hubs),
              "projected map hubs differ from authored mapPlan IDs/centres")
    authored_points = map_plan.get("points", [])
    projected_points = map_bindings.get("points", [])
    if isinstance(authored_points, list) and isinstance(projected_points, list):
        point_tiles = {row.get("id"): row.get("tile") for row in authored_points if isinstance(row, dict)}
        point_rows_valid = len([row for row in authored_points if isinstance(row, dict)]) == len(authored_points)
        check(point_rows_valid and len(point_tiles) == len(authored_points)
              and all(isinstance(row, dict) and row.get("pointId") in point_tiles
                      and row.get("tile") == point_tiles.get(row.get("pointId"))
                      for row in projected_points),
              "projected point-zone bindings differ from authored mapPlan point IDs/tiles")
    profile_services = profile.get("fulfillmentPlan", {}).get("services", [])
    service_rows = episode.get("fulfillmentServices", [])
    check([row.get("serviceId") for row in service_rows]
          == [row.get("id") for row in profile_services],
          "fulfillment services do not preserve authored order and identity")
    for source, projected in zip(profile_services, service_rows):
        source_recipes = [row.get("id") for row in source.get("recipes", [])]
        projected_recipes = [row.get("recipeId") for row in projected.get("recipes", [])]
        check(source_recipes == projected_recipes,
              f"service {source.get('id')} recipes differ from the authored plan")
    screens = episode.get("screens", [])
    screen_ids = [row.get("id") for row in screens if isinstance(row, dict)]
    check(len(screen_ids) == len(screens) and len(set(screen_ids)) == len(screen_ids),
          "screen identities must be unique")
    roles = episode.get("screenRoles", {})
    check(set(roles) == {"title", "factualIntro", "handover", "personalIntro", "factualOutro", "personalOutro", "defeat", "continuation"}
          and set(roles.values()) <= set(screen_ids)
          and len(set(roles.values())) == len(roles), "screen role bindings are incomplete, duplicate or unresolved")
    check([row.get("id") for row in screens[:4]] == [roles.get(key) for key in ("title", "factualIntro", "handover", "personalIntro")],
          "first four screens do not match the authored opening roles")
    screen_map = {row.get("id"): row for row in screens if isinstance(row, dict)}
    if set(roles) == {"title", "factualIntro", "handover", "personalIntro", "factualOutro", "personalOutro", "defeat", "continuation"}:
        if all(screen_id in screen_map for screen_id in roles.values()):
            check(screen_map[roles["factualIntro"]].get("text") == episode.get("event")
                  and screen_map[roles["factualOutro"]].get("text") == episode.get("historicalOutcome"),
                  "factual screen text differs from the episode frame")
            check(all(screen_map[roles[key]].get("narrator") == "collection-narrator"
                      for key in ("factualIntro", "factualOutro", "handover")),
                  "factual/hand-over narrator binding drift")
            selected_narrator = episode.get("knowledgeBasis", {}).get("speaker")
            check(all(screen_map[roles[key]].get("narrator") == selected_narrator
                      for key in ("personalIntro", "personalOutro")),
                  "personal narrator binding drift")
    expected_entities = {row.get("id") for row in profile.get("worldContract", {}).get("entities", [])}
    policies = episode.get("historicalMaterialPolicyByEntity", {})
    check(set(policies) == expected_entities and all(isinstance(v, str) and v.strip() for v in policies.values()),
          "documentary entity policies must exactly cover main-world identities")
    continuation = episode.get("continuation") if isinstance(episode.get("continuation"), dict) else {}
    check(continuation.get("campaignComplete") is False,
          "intermediate continuation cannot claim campaign completion")
    return failures
