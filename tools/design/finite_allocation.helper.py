"""Enumerate finite alternative allocations and affordable optional prefixes.

Pure authoring analysis. No recipe selection, payment, native trigger or game
behavior is implemented by enumerating these candidate resource states.
"""

from collections import deque
from itertools import product
import hashlib
import json

from secondary import COSTS, RESOURCES, REWARDS

LEVELS = ("easy", "standard", "hard")
MAX_SERVICES = 8
MAX_COMBINATIONS = 4096
MAX_OPTIONALS = 12
MAX_ANALYSIS_STATES = 65536


def amounts(value):
    if not isinstance(value, dict) or set(value) - set(RESOURCES):
        raise ValueError("Unknown resource or invalid resource vector")
    if any(type(amount) is not int or amount < 0 for amount in value.values()):
        raise ValueError("Resource amounts must be nonnegative integers")
    return {key: value.get(key, 0) for key in RESOURCES}


def identifier(value):
    if not isinstance(value, str) or not value or not value.isascii() or any(
        char not in "abcdefghijklmnopqrstuvwxyz0123456789-" for char in value
    ):
        raise ValueError("Expected an explicit ASCII resource-plan identity")
    return value


def balance(stock, cost, reward=None):
    """Payment precedes reward: a later credit can never fund its own debit."""
    if any(stock[key] < cost[key] for key in RESOURCES):
        return None
    reward = reward or amounts({})
    return {key: stock[key] - cost[key] + reward[key] for key in RESOURCES}


def optional_states(stock, optionals):
    """One state per completed subset; final stock is order-independent.

    Reachability is not: a subset is visited only via an affordable payment
    prefix. Each optional identity completes at most once, with its reserved
    reward credited after payment. This assumes all spatial tasks succeed.
    """
    states = {0: (dict(stock), [])}
    pending = deque([0])
    while pending:
        mask = pending.popleft()
        current, order = states[mask]
        for index, item in enumerate(optionals):
            bit = 1 << index
            if mask & bit or (mask | bit) in states:
                continue
            after = balance(current, item["cost"], item["reward"])
            if after is not None:
                next_mask = mask | bit
                states[next_mask] = (after, [*order, item["id"]])
                pending.append(next_mask)
    return states


def resolved_inputs(plan):
    if type(plan.get("schemaVersion")) is not int or plan["schemaVersion"] != 1:
        raise ValueError("Unsupported internal analysis-plan version")
    if plan.get("classification") != "candidate economic analysis; not gameplay DSL":
        raise ValueError("Plan must explicitly declare its research-only status")
    profiles = plan.get("operatingStockByDifficulty")
    if not isinstance(profiles, dict) or set(profiles) != set(LEVELS):
        raise ValueError("All three operating-stock profiles are required")
    stocks = {level: amounts(profiles[level]) for level in LEVELS}
    services = plan.get("services")
    if not isinstance(services, list) or not 1 <= len(services) <= MAX_SERVICES:
        raise ValueError("Expected one to eight explicit services")
    service_ids, recipe_ids, resolved, combinations = set(), set(), [], 1
    for service in services:
        sid = identifier(service["id"])
        if sid in service_ids:
            raise ValueError("Duplicate service identity")
        service_ids.add(sid)
        recipes = service.get("recipes")
        if not isinstance(recipes, list) or not recipes:
            raise ValueError("Each service needs explicit alternatives")
        row = []
        for recipe in recipes:
            rid = identifier(recipe["id"])
            if rid in recipe_ids:
                raise ValueError("Duplicate recipe identity")
            recipe_ids.add(rid)
            row.append({"id": rid, "service": sid, "cost": amounts(recipe["cost"])})
        combinations *= len(row)
        if combinations > MAX_COMBINATIONS:
            raise ValueError("Authoring combination cap exceeded")
        resolved.append(row)
    optional_rows = plan.get("optionalTasks", [])
    if not isinstance(optional_rows, list) or len(optional_rows) > MAX_OPTIONALS:
        raise ValueError("Optional enumeration cap exceeded")
    if combinations * (1 << len(optional_rows)) * len(LEVELS) > MAX_ANALYSIS_STATES:
        raise ValueError("Combined allocation/optional analysis cap exceeded")
    optional_ids, optionals = set(), []
    for item in optional_rows:
        oid, kind = identifier(item["id"]), item["kind"]
        if oid in optional_ids or kind not in REWARDS:
            raise ValueError("Duplicate optional identity or unknown shared optional recipe")
        optional_ids.add(oid)
        optionals.append({"id": oid, "kind": kind, "cost": amounts(COSTS.get(kind, {})),
                          "reward": amounts(REWARDS[kind])})
    return stocks, resolved, optionals


def build_report(plan):
    stocks, services, optionals = resolved_inputs(plan)
    resolved = {"plan": plan, "optionalMechanics": optionals}
    fingerprint = hashlib.sha256(json.dumps(resolved, sort_keys=True,
                                           ensure_ascii=False).encode()).hexdigest()
    combinations = []
    for selected in product(*services):
        cost = {key: sum(recipe["cost"][key] for recipe in selected) for key in RESOURCES}
        combinations.append({"recipes": [recipe["id"] for recipe in selected], "cost": cost})
    all_mask = (1 << len(optionals)) - 1
    profiles = {}
    for level, stock in stocks.items():
        before = optional_states(stock, optionals)
        rows = []
        for combination in combinations:
            after = balance(stock, combination["cost"])
            reachable_after = optional_states(after, optionals) if after is not None else {}
            completion = reachable_after.get(all_mask)
            unlocking = None
            for available, order in before.values():
                remainder = balance(available, combination["cost"])
                if remainder is not None:
                    unlocking = order
                    break
            rows.append({**combination, "allSkipAffordable": after is not None,
                         "allSkipRemainder": after,
                         "reachableOptionalSubsetsAfterFunding": len(reachable_after),
                         "allOptionalsAfterFundingAffordable": completion is not None,
                         "allOptionalsExampleOrder": completion[1] if completion else None,
                         "allOptionalsRemainder": completion[0] if completion else None,
                         "affordableAfterSomeOptionals": unlocking is not None,
                         "examplePreFundingOptionals": unlocking})
        if not any(row["allSkipAffordable"] for row in rows):
            raise ValueError(f"{level}: main allocation depends on optional rewards")
        profiles[level] = {"operatingStock": stock,
                           "allSkipAffordableCount": sum(row["allSkipAffordable"] for row in rows),
                           "allOptionalsAfterFundingAffordableCount": sum(row["allOptionalsAfterFundingAffordable"] for row in rows),
                           "affordableAfterSomeOptionalsCount": sum(row["affordableAfterSomeOptionals"] for row in rows),
                           "combinations": rows}
    return {"schemaVersion": 1, "episodeId": plan["episodeId"],
            "status": "candidate finite accounting; not a dossier, runtime choice or game verification",
            "resolvedInputsSha256": fingerprint, "combinationCount": len(combinations),
            "optionalTasks": optionals,
            "reservedOptionalRewards": {key: sum(item["reward"][key] for item in optionals) for key in RESOURCES},
            "profiles": profiles, "nativeImplemented": False, "gameVerified": False,
            "limits": ["Resource accounting assumes all listed operating stock is actually accessible.",
                       "Optional prefix reachability assumes spatial/actor predicates succeed; not a movement schedule.",
                       "No recipe output, work site, terrain, time, challenge, history or native operation is certified.",
                       "Only supplied operating stock and once-only successful optional rewards are used; no recovery reserve or future income."]}
