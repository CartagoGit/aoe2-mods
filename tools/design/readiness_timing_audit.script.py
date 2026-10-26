"""Parametric all-skip readiness estimates, never native or game certification.

The author supplies routes and assumptions. This diagnostic reads the existing
phase/debit contract; it neither chooses gameplay values nor changes a dossier.
"""

import argparse
import hashlib
import heapq
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PLAN = "docs/research/odyssey-research/imperial33-readiness-timing-plan.json"
DEFAULT_REPORT = "docs/research/odyssey-research/imperial33-readiness-timing-audit.json"


def positive(value):
    return type(value) in (int, float) and math.isfinite(value) and value > 0


def shortest_distance(graph, start, end):
    if start not in graph or end not in graph:
        raise ValueError("Unknown route endpoint")
    pending, best = [(0.0, start)], {start: 0.0}
    while pending:
        distance, hub = heapq.heappop(pending)
        if distance != best[hub]:
            continue
        if hub == end:
            return distance
        for neighbor, length in graph[hub].items():
            candidate = distance + length
            if candidate < best.get(neighbor, math.inf):
                best[neighbor] = candidate
                heapq.heappush(pending, (candidate, neighbor))
    raise ValueError(f"No authored land route from {start} to {end}")


def worker_split(deficits, worker_count, rate):
    """Best fixed integer allocation; no reassignment or measured gather rates."""
    resources = [key for key, value in deficits.items() if value > 0]
    if not resources:
        return {"workers": {}, "harvestSeconds": 0.0}
    if type(worker_count) is not int or worker_count < len(resources) or not positive(rate):
        raise ValueError("Insufficient workers or invalid assumed gather rate")
    best = None
    # Enumerate integer compositions, rather than a Cartesian power of workers.
    for cuts in itertools.combinations(range(1, worker_count), len(resources) - 1):
        points = (0, *cuts, worker_count)
        counts = [end - start for start, end in zip(points, points[1:])]
        duration = max(deficits[key] / (count * rate) for key, count in zip(resources, counts))
        if best is None or duration < best[0]:
            best = duration, dict(zip(resources, counts))
    return {"workers": best[1], "harvestSeconds": best[0]}


def build_report(plan, episode):
    objective = next((row for row in episode["objectivePlan"] if row["id"] == plan["objectiveId"]), None)
    if not objective:
        raise ValueError("Unknown authored objective")
    requirements = objective["predicate"]["requirements"]
    deadlines = [row for row in requirements if row["kind"] == "phase-deadline"]
    if len(deadlines) != 1 or deadlines[0]["phase"] != objective["phase"]:
        raise ValueError("Diagnostic requires one matching authored phase deadline")
    if objective["after"]:
        raise ValueError("Later phases require an explicitly modelled incoming budget; unsupported here")
    hubs = {row["id"]: row["centre"] for row in episode["mapPlan"]["hubs"]}
    graph = {key: {} for key in hubs}
    for corridor in episode["mapPlan"]["corridors"]:
        if corridor["mode"] != "land":
            continue
        for start, end in zip(corridor["hubOrder"], corridor["hubOrder"][1:]):
            distance = math.dist(hubs[start], hubs[end])
            graph[start][end] = graph[end][start] = distance
    entities = {row["id"]: row for row in episode["worldContract"]["entities"]}
    zones = {row["id"]: row for row in episode["worldContract"]["zones"]}
    assignments, movements = {}, []
    for assignment in plan["stagingAssignments"]:
        entity_id, zone_id = assignment["entityId"], assignment["zoneId"]
        if entity_id in assignments or entity_id not in entities or zone_id not in zones:
            raise ValueError("Duplicate or unknown staging identity/destination")
        entity, zone = entities[entity_id], zones[zone_id]
        if entity.get("generationPolicy") != "preplaced and available":
            raise ValueError("Generated or phase-gated actors need an explicit availability schedule")
        assignments[entity_id] = zone_id
        # Full center-to-center path plus both offset connectors; not a native path.
        length = math.hypot(*entity["offsetTiles"]) + shortest_distance(
            graph, entity["initialHub"], zone["hub"]
        ) + math.hypot(*zone["offsetTiles"])
        movements.append({"entityId": entity_id, "zoneId": zone_id, "routeTiles": round(length, 6)})
    for req in requirements:
        if req["kind"] == "checkpoint-entity-presence" or (
            req["kind"] == "entity-state" and req["state"] == "arrived"
        ):
            matching = sum(assignments.get(entity_id) == zone for entity_id, zone in req["destinations"].items())
            if matching < req["requiredCount"]:
                raise ValueError(f"Staging assignments fail {req['id']}")
    assumptions = plan["assumptions"]
    for key in ("movementTilesPerGameSecond", "netResourcePerWorkerGameSecond", "pathLengthFactors"):
        if not assumptions[key] or not all(positive(value) for value in assumptions[key]):
            raise ValueError("Assumed rates/factors must be finite and positive")
    if min(assumptions["pathLengthFactors"]) < 1:
        raise ValueError("A detour factor cannot shorten authored routes")
    for key in ("collectionSeconds", "economicSetupSeconds", "finalCoordinationSeconds"):
        if type(assumptions[key]) not in (int, float) or not math.isfinite(assumptions[key]) or assumptions[key] < 0:
            raise ValueError("Assumed overhead must be finite and nonnegative")
    costs = {resource: sum(req.get("amounts", {}).get(resource, 0) for req in requirements
                           if req["kind"] == "resource-transaction")
             for resource in ("food", "wood", "gold", "stone")}
    if not movements:
        raise ValueError("No authored movement assignment")
    longest = max(row["routeTiles"] for row in movements)
    profiles = {}
    for level, profile in episode["difficulty"].items():
        deficits = {key: max(0, amount - profile["startingResources"][key]) for key, amount in costs.items()}
        if any(profile["accessibleWithoutOptionalRewards"][key] < amount for key, amount in costs.items()):
            raise ValueError("All-skip accessible stock cannot fund this objective")
        deadline = deadlines[0]["secondsByDifficulty"][level]
        samples = []
        for speed, rate, factor in itertools.product(
            assumptions["movementTilesPerGameSecond"],
            assumptions["netResourcePerWorkerGameSecond"], assumptions["pathLengthFactors"],
        ):
            economy = worker_split(deficits, profile["maxVillagers"], rate)
            movement_seconds = longest * factor / speed + assumptions["collectionSeconds"]
            economic_seconds = economy["harvestSeconds"] + assumptions["economicSetupSeconds"]
            estimate = max(movement_seconds, economic_seconds) + assumptions["finalCoordinationSeconds"]
            samples.append({
                "movementTilesPerGameSecond": speed, "netResourcePerWorkerGameSecond": rate,
                "pathLengthFactor": factor, "fixedWorkerAllocation": economy["workers"],
                "movementSeconds": round(movement_seconds, 3), "economicSeconds": round(economic_seconds, 3),
                "estimatedReadinessSeconds": round(estimate, 3),
                "deadlineMinusEstimateSeconds": round(deadline - estimate, 3),
                "strictlyInsideAssumedWindow": estimate < deadline,
            })
        profiles[level] = {"deadlineGameSeconds": deadline, "stagingDebit": costs,
                           "initialShortfall": deficits, "assumedSeparateGatherers": profile["maxVillagers"],
                           "samples": samples}
    return {"schemaVersion": 1, "episodeId": episode["id"], "objectiveId": objective["id"],
            "author": plan["author"], "date": plan["date"],
            "status": "conditional scheduling hypotheses; no native, historical, terrain or playability approval",
            "episodeSha256": hashlib.sha256(json.dumps(episode, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
            "planSha256": hashlib.sha256(json.dumps(plan, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
            "assumptions": assumptions, "movements": movements, "longestAuthoredRouteTiles": longest,
            "profiles": profiles, "limits": plan["limits"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", default=DEFAULT_PLAN)
    parser.add_argument("--output", default=DEFAULT_REPORT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    plan = json.loads((ROOT / args.plan).read_text())
    campaign = json.loads((ROOT / plan["campaignSource"]).read_text())
    episode = next(row for row in campaign["episodes"] if row["id"] == plan["episodeId"])
    report = build_report(plan, episode)
    serialized = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    output = ROOT / args.output
    if args.write:
        output.write_text(serialized)
    elif not output.exists() or output.read_text() != serialized:
        raise ValueError("Stale conditional timing audit; inspect assumptions before regenerating")
    print(f"Conditional timing audit: {report['episodeId']}, {sum(len(row['samples']) for row in report['profiles'].values())} hypotheses; gameVerified=false")


if __name__ == "__main__":
    main()
