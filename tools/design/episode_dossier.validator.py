"""Check authored episode contracts without asserting native behavior or balance."""

import math
import runpy
from pathlib import Path
from secondary import check_optional_objectives

continuity = runpy.run_path(str(Path(__file__).with_name("odyssey_continuity.helper.py")))
transport = runpy.run_path(str(Path(__file__).with_name("transport_journey.helper.py")))
audit_finale = continuity["audit_finale"]
audit_entry = continuity["audit_entry"]


def audit_dossier(episode, campaign=None, baseline=None):
    failures = []

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
            if req["kind"] == "entity-state":
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
