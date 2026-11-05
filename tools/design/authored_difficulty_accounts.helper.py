"""Strict source and derived-account arithmetic for the legacy dossier opt-in."""

import runpy
from pathlib import Path

numbers = runpy.run_path(str(Path(__file__).with_name("design_numbers.helper.py")))
RESOURCES = numbers["RESOURCES"]
resource_amounts = numbers["resource_amounts"]
MAX_SAFE_INTEGER = 2**53 - 1
LEVELS = ("easy", "standard", "hard")
ACCOUNTS = ("spendable", "gatherableBank", "protectedRecovery", "optionalReserve")
PROFILE = "authored-finite-accounts-v1"


def vector(value, label):
    if not isinstance(value, dict) or set(value) != set(RESOURCES):
        raise ValueError(f"{label}: expected exactly food, wood, gold and stone")
    try:
        normalized = resource_amounts(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"{label}: {error}") from error
    for key, amount in normalized.items():
        if type(amount) is not int or amount < 0 or amount > MAX_SAFE_INTEGER:
            raise ValueError(f"{label}/{key}: expected nonnegative safe integer")
    return normalized


def observed_vector(value, label):
    """Normalize existing predicate/effect vectors, which may be sparse."""
    if not isinstance(value, dict):
        raise ValueError(f"{label}: expected a resource object")
    try:
        normalized = resource_amounts(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"{label}: {error}") from error
    for key, amount in normalized.items():
        if type(amount) is not int or amount < 0 or amount > MAX_SAFE_INTEGER:
            raise ValueError(f"{label}/{key}: expected nonnegative safe integer")
    return normalized


def add(*vectors):
    result = {key: 0 for key in RESOURCES}
    for source in vectors:
        for key in RESOURCES:
            result[key] += source[key]
            if result[key] > MAX_SAFE_INTEGER:
                raise ValueError(f"resource total overflows safe integer: {key}")
    return result


def read_source(source):
    if not isinstance(source, dict) or set(source) != set(LEVELS):
        raise ValueError("authoredDifficultyAccounts needs exactly easy, standard and hard")
    result = {}
    for level in LEVELS:
        row = source[level]
        if not isinstance(row, dict) or set(row) != set(ACCOUNTS):
            raise ValueError(f"{level}: expected exactly the four authored accounts")
        result[level] = {key: vector(row[key], f"{level}/{key}") for key in ACCOUNTS}
        add(*result[level].values())
    return result


def verify_episode(episode, optional_states, all_mask):
    """Rebuild all numeric witnesses from materialized predicates and effects."""
    source_mode = episode.get("economyProfile") == PROFILE
    profile_mode = any("economyProfile" in row for row in episode.get("difficulty", {}).values())
    if not source_mode and not profile_mode:
        return None
    if episode.get("economyProfile") != PROFILE:
        raise ValueError(f"{episode.get('id')}: malformed or unknown economyProfile")
    if profile_mode:
        raise ValueError(f"{episode.get('id')}: economyProfile marker is only valid on dossier")
    if set(episode["difficulty"]) != set(LEVELS):
        raise ValueError(f"{episode['id']}: incomplete difficulty profiles")
    if "authoredDifficultyAccounts" in episode:
        raise ValueError("derived economyProfile must not retain source input")
    if any(k in episode for k in ("startingResources", "discretionaryMargin")):
        raise ValueError("legacy startingResources/discretionaryMargin aliases are ambiguous")
    main = {key: 0 for key in RESOURCES}
    for obj in episode["objectivePlan"]:
        for req in obj["predicate"]["requirements"]:
            if req["kind"] == "resource-transaction":
                main = add(main, observed_vector(req.get("amounts"), "mandatory payment"))
    costs, rewards = ({key: 0 for key in RESOURCES} for _ in range(2))
    tasks = episode.get("secondaryObjectives")
    if not isinstance(tasks, list) or not 6 <= len(tasks) <= 8:
        raise ValueError("explicit accounts require 6–8 built optional task rows")
    if len({task["id"] for task in tasks}) != len(tasks):
        raise ValueError("duplicate optional task identity")
    options = []
    for task in tasks:
        if len(task.get("effects", [])) != 1:
            raise ValueError("each optional task needs its actual single reward effect")
        reward = observed_vector(task["effects"][0].get("resources"), "optional reward")
        if task["effects"][0].get("onceFlag") is None:
            raise ValueError("optional reward must have a once flag")
        task_cost = {key: 0 for key in RESOURCES}
        for req in task["predicate"]["requirements"]:
            if req["kind"] == "atomic-payment":
                task_cost = add(task_cost, observed_vector(req.get("resources"), "optional cost"))
        costs = add(costs, task_cost)
        rewards = add(rewards, reward)
        options.append({"id": task["id"], "cost": task_cost, "reward": reward})
    reserve = episode["secondaryBudget"]["reservedRewards"]
    if vector(reserve, "reservedRewards") != rewards:
        raise ValueError("optionalReserve must equal the exact actual once-only reward sum")
    if vector(episode["secondaryBudget"]["reallocatedCacheAllowance"], "reallocatedCacheAllowance") != rewards:
        raise ValueError("reallocatedCacheAllowance must describe the same reward reserve")
    for level, profile in episode["difficulty"].items():
        vectors = {key: vector(profile.get(key), f"{level}/{key}") for key in
                   ("startingResources", "gatherableBank", "protectedRecoveryStock", "replacementBudget", "mandatoryDeliveries", "supplyMargins", "accessibleWithoutOptionalRewards")}
        S, B, P, Z = (vectors[k] for k in ("startingResources", "gatherableBank", "protectedRecoveryStock", "replacementBudget"))
        accessible = add(S, B)
        need = add(vectors["mandatoryDeliveries"], Z)
        margin = {key: accessible[key] - need[key] for key in RESOURCES}
        if any(value < 0 for value in margin.values()):
            raise ValueError(f"{level}: finite spendable supply cannot fund mandatory costs and planning floor")
        if vectors["mandatoryDeliveries"] != main or vectors["accessibleWithoutOptionalRewards"] != accessible or vectors["supplyMargins"] != margin:
            raise ValueError(f"{level}: authored account derivation drift")
        after_main = {key: accessible[key] - main[key] - Z[key] for key in RESOURCES}
        states = optional_states(after_main, options)
        full = states.get(all_mask(len(options)))
        if full is None:
            raise ValueError(f"{level}: actual optional costs/rewards do not reach all-complete state")
        if profile.get("mainFeasibleSkippingAllOptionals") is not True or profile.get("allOptionalCostsAffordable") is not True:
            raise ValueError(f"{level}: stored feasibility flags are not true")
        if "economyProfile" in profile:
            raise ValueError(f"{level}: marker belongs on dossier only")
    return {"rewards": rewards, "costs": costs, "main": main}


def build_profiles(authored, objectives, main, rewards):
    """Build explicit profiles using the actual materialized optional rows."""
    source = read_source(authored["authoredDifficultyAccounts"])
    if "startingResources" in authored or "discretionaryMargin" in authored:
        raise ValueError("Opt-in cannot be combined with legacy startingResources/discretionaryMargin")
    if "protectedRecoveryStock" in authored:
        alias = observed_vector(authored["protectedRecoveryStock"], "protectedRecoveryStock")
        if any(row["protectedRecovery"] != alias for row in source.values()):
            raise ValueError("protectedRecoveryStock alias conflicts with authored accounts")
    if "replacementBudget" not in authored:
        raise ValueError("Opt-in requires the existing replacementBudget planning floor")
    replacement = vector(authored["replacementBudget"], "replacementBudget")
    reward_sum = {key: 0 for key in RESOURCES}
    optionals = []
    if not isinstance(objectives, list) or not 6 <= len(objectives) <= 8:
        raise ValueError("Opt-in requires 6–8 built optional task rows")
    if len({row["id"] for row in objectives}) != len(objectives):
        raise ValueError("Opt-in requires distinct optional task identities")
    for task in objectives:
        effect_rows = task.get("effects", [])
        if len(effect_rows) != 1 or not effect_rows[0].get("onceFlag"):
            raise ValueError("Opt-in requires each actual task to have one once-only reward effect")
        reward = observed_vector(effect_rows[0].get("resources"), f"{task['id']}/reward")
        cost = {key: 0 for key in RESOURCES}
        for req in task["predicate"]["requirements"]:
            if req["kind"] == "atomic-payment":
                cost = add(cost, observed_vector(req.get("resources"), f"{task['id']}/cost"))
        reward_sum = add(reward_sum, reward)
        optionals.append({"id": task["id"], "cost": cost, "reward": reward})
    if reward_sum != vector(rewards, "actual optional reward total"):
        raise ValueError("Built reward effects do not equal the exact optional reserve")
    finite = runpy.run_path(str(Path(__file__).with_name("finite_allocation.helper.py")))
    states_fn = finite["optional_states"]
    result = {}
    for level in LEVELS:
        row = source[level]
        S, B, P, R = (row[key] for key in ACCOUNTS)
        if R != reward_sum:
            raise ValueError(f"{level}: optionalReserve must equal actual once-only rewards")
        accessible = add(S, B)
        need = add(main, replacement)
        margin = {key: accessible[key] - need[key] for key in RESOURCES}
        if any(value < 0 for value in margin.values()):
            raise ValueError(f"{level}: explicit spendable resources cannot fund mandatory payments and replacement floor")
        final = states_fn({key: accessible[key] - main[key] - replacement[key] for key in RESOURCES}, optionals)
        full = final.get((1 << len(optionals)) - 1)
        if full is None:
            raise ValueError(f"{level}: all optional payments are not affordable before their rewards")
        result[level] = {
            "basis": "authored finite accounts: spendable plus explicitly collectible finite bank; protected recovery and once-only rewards excluded from main-accessible stock. Financial witness assumes authored finite supply can be collected and all optional spatial tasks succeed; no native calibration or playability is implied.",
            "startingResources": S, "gatherableBank": B, "mandatoryDeliveries": main,
            "protectedRecoveryStock": P, "replacementBudget": replacement,
            "supplyMargins": margin, "accessibleWithoutOptionalRewards": accessible,
            "maxVillagers": {"easy": 12, "standard": 9, "hard": 6}[level],
            "enemyTotalCap": authored["enemyCounts"][level], "enemyProduction": False,
            "regeneratingResources": False,
            "roughDurationMinutes": authored.get("durationMinutesByDifficulty", {}).get(level, {"easy": [30, 55], "standard": [35, 65], "hard": [40, 75]}[level]),
            "difficultyLevers": authored["difficultyLevers"][level],
            "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
            "mainFeasibleSkippingAllOptionals": True, "allOptionalCostsAffordable": True,
        }
    return result
