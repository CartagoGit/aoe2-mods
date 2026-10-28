"""Recompute static difficulty signals; never certify playability or game tests.

The policy supplies campaign coverage. Only materialized episodes[] are audited;
episodeSelection[] and episodeBlueprints[] never count as finished dossiers.
"""

import argparse
import datetime
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = "docs/research/odyssey-research/civic-difficulty-mechanical-audit.json"
POLICY = "docs/design/odyssey-policy.json"
LEVELS = ("easy", "standard", "hard")
RESOURCES = {"food", "wood", "gold", "stone"}
V3_DESIGN_PROFILE = "alternative-fulfillment-v3"
MAX_SAFE_INTEGER = 2**53 - 1


def read(path, root=ROOT):
    return json.loads((root / path).read_text(encoding="utf-8"))


def fingerprints(paths, root=ROOT):
    return {path: hashlib.sha256((root / path).read_bytes()).hexdigest()
            for path in paths}


def predicate_kinds(objectives):
    kinds = set()

    def walk(value, inside=False):
        if isinstance(value, dict):
            if inside and isinstance(value.get("kind"), str):
                kinds.add(value["kind"])
            for key, item in value.items():
                walk(item, inside or key == "predicate")
        elif isinstance(value, list):
            for item in value:
                walk(item, inside)

    walk(objectives)
    return sorted(kinds)


def deadline_fields(episode):
    """Report positive structured deadline keys, never matching prose values.

    This is a heuristic, not a semantic classifier. Rough duration, warnings,
    release offsets and neverUseTimerInstead do not constitute mission deadlines.
    """
    found = []

    def normalized(value):
        return "".join(char.lower() for char in value if char.isalnum())

    def positive_limit(value):
        if type(value) is int:
            return value > 0
        if type(value) is float:
            return math.isfinite(value) and value > 0
        if isinstance(value, dict):
            return any(positive_limit(item) for key, item in value.items()
                       if key in (*LEVELS, "seconds", "secondsByDifficulty"))
        return False

    def walk(value, path=""):
        if isinstance(value, dict):
            if value.get("kind") == "phase-deadline":
                limits = value.get("secondsByDifficulty")
                if not isinstance(limits, dict) or set(limits) != set(LEVELS) or not all(
                    type(item) is int and item > 0 for item in limits.values()
                ):
                    raise ValueError(f"{path}: invalid phase deadline limits")
                found.append(f"{path}/secondsByDifficulty")
            for key, item in value.items():
                child = f"{path}/{key}"
                name = normalized(key)
                excluded = any(term in name for term in (
                    "neverusetimerinstead", "roughdurationminutes",
                    "warningseconds", "offsetseconds",
                ))
                if not excluded and any(term in name for term in (
                    "deadline", "timelimit", "countdown", "expires",
                )) and positive_limit(item):
                    found.append(child)
                walk(item, child)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                walk(item, f"{path}/{index}")

    walk(episode)
    return sorted(found)


def _legacy_episode_audit(campaign, episode):
    difficulty = episode["difficulty"]
    if set(difficulty) != set(LEVELS):
        raise ValueError(f"{campaign}/{episode['id']}: missing difficulty profile")
    budgets, caps, profiles = {}, {}, {}
    for level in LEVELS:
        profile = difficulty[level]
        budget = profile["accessibleWithoutOptionalRewards"]
        if set(budget) != RESOURCES or any(
            type(amount) is not int or amount < 0 for amount in budget.values()
        ):
            raise ValueError(f"{campaign}/{episode['id']}/{level}: invalid budget")
        cap = profile["enemyTotalCap"]
        if type(cap) is not int or cap < 0:
            raise ValueError(f"{campaign}/{episode['id']}/{level}: invalid enemy cap")
        budgets[level], caps[level] = budget, cap
        profiles[level] = {
            "enemyTotalCap": cap,
            "initialEnemy": profile.get("initialEnemy"),
            "scheduledWaveCount": sum(len(profile.get(key, [])) for key in (
                "waves", "scheduledWaves", "enemyWaves", "scheduledEnemyWaves",
            )),
            "maxVillagers": profile.get("maxVillagers"),
            "accessibleWithoutOptionalRewards": budget,
        }
    hostile = sum(any(word in entity["role"].lower() for word in ("hostile", "enemy"))
                  for entity in episode["worldContract"]["entities"])
    deadlines = deadline_fields(episode)
    has_hostiles = any(caps.values()) or hostile > 0
    same_budget = budgets["easy"] == budgets["standard"] == budgets["hard"]
    return {
        "campaign": campaign, "order": episode["order"], "episodeId": episode["id"],
        "coreMechanic": episode["coreMechanic"],
        "enemyTotalCapByDifficulty": caps,
        "enemyScheduledReleaseCounts": {
            level: profiles[level]["scheduledWaveCount"] for level in LEVELS
        },
        "hostileRoleEntityCount": hostile,
        "pressureMechanism": {
            "finiteHostilesPresent": has_hostiles,
            "explicitStructuredDeadlinePresent": bool(deadlines),
            "deadlineFields": deadlines,
            "otherMainPredicateKinds": predicate_kinds(episode["objectivePlan"]),
            "otherSecondaryPredicateKinds": predicate_kinds(episode["secondaryObjectives"]),
        },
        "mainObjectiveCount": len(episode["objectivePlan"]),
        "secondaryObjectiveCount": len(episode["secondaryObjectives"]),
        "difficulty": profiles,
        "accessibleBudgetSameAcrossDifficulties": same_budget,
        "staticRiskCandidate": not has_hostiles and not deadlines and same_budget,
    }


def _require_resource_vector(value, label):
    if not isinstance(value, dict) or set(value) != RESOURCES:
        raise ValueError(f"{label}: expected complete resource vector")
    for resource, amount in value.items():
        if type(amount) is not int or amount < 0 or amount > MAX_SAFE_INTEGER:
            raise ValueError(f"{label}/{resource}: expected nonnegative safe integer")
    return value


def _v3_enemy_roster(profile, campaign, episode_id):
    roster = profile.get("enemyRoster")
    expected = {"initialEntityIds", "productionEnabled", "mobilizations", "unspentPolicy"}
    label = f"{campaign}/{episode_id}/referenceCapabilityProfile/enemyRoster"
    if not isinstance(roster, dict) or set(roster) != expected:
        raise ValueError(f"{label}: missing or malformed roster")
    if (
        not isinstance(roster["initialEntityIds"], list)
        or any(not isinstance(item, str) or not item for item in roster["initialEntityIds"])
        or roster["productionEnabled"] is not False
        or not isinstance(roster["mobilizations"], list)
        or roster["unspentPolicy"] != "remain-in-reserve"
    ):
        raise ValueError(f"{label}: missing or malformed roster")
    for index, mobilization in enumerate(roster["mobilizations"]):
        if (
            not isinstance(mobilization, dict)
            or set(mobilization) != {"id", "entityIds", "releasedOnce"}
            or not isinstance(mobilization["id"], str)
            or not mobilization["id"]
            or not isinstance(mobilization["entityIds"], list)
            or not mobilization["entityIds"]
            or any(not isinstance(item, str) or not item for item in mobilization["entityIds"])
            or mobilization["releasedOnce"] is not True
        ):
            raise ValueError(f"{label}/mobilizations/{index}: malformed entry")
    return roster


def _v3_episode_audit(campaign, episode):
    episode_id = episode.get("id")
    label = f"{campaign}/{episode_id}"
    profile = episode.get("referenceCapabilityProfile")
    if (
        not isinstance(profile, dict)
        or profile.get("profile") != "composed-world-ledger"
        or type(profile.get("schemaVersion")) is not int
        or profile["schemaVersion"] != 3
    ):
        raise ValueError(f"{label}: expected composed-world-ledger schemaVersion 3 reference profile")

    difficulty = episode.get("difficulty")
    selection_analysis = episode.get("selectionAnalysisByDifficulty")
    if not isinstance(selection_analysis, dict) or set(selection_analysis) != set(LEVELS):
        raise ValueError(f"{label}: missing selection analysis for all difficulties")
    try:
        difficulty_json = json.dumps(difficulty, sort_keys=True, allow_nan=False)
        selection_analysis_json = json.dumps(selection_analysis, sort_keys=True, allow_nan=False)
    except (TypeError, ValueError, OverflowError, RecursionError) as error:
        raise ValueError(
            f"{label}: difficulty and selectionAnalysisByDifficulty must be JSON-serializable "
            f"for exact comparison: {error}"
        ) from error
    if difficulty_json != selection_analysis_json:
        raise ValueError(f"{label}: difficulty must exactly match selectionAnalysisByDifficulty as JSON")

    accounts = episode.get("accountsByDifficulty")
    if not isinstance(accounts, dict) or set(accounts) != set(LEVELS):
        raise ValueError(f"{label}: missing complete accountsByDifficulty")
    affordable_counts = {}
    budgets = {}
    for level in LEVELS:
        account = accounts[level]
        if not isinstance(account, dict) or set(account) != {"spendable", "protectedRecovery", "optionalReserve"}:
            raise ValueError(f"{label}/{level}: malformed account")
        spendable = _require_resource_vector(account["spendable"], f"{label}/{level}/spendable")
        protected = _require_resource_vector(account["protectedRecovery"], f"{label}/{level}/protectedRecovery")
        _require_resource_vector(account["optionalReserve"], f"{label}/{level}/optionalReserve")
        budgets[level] = spendable

        view = selection_analysis[level]
        if not isinstance(view, dict):
            raise ValueError(f"{label}/{level}: malformed selection analysis")
        view_spendable = _require_resource_vector(
            view.get("spendable"), f"{label}/{level}/selectionAnalysis/spendable"
        )
        view_protected = _require_resource_vector(
            view.get("protectedRecovery"), f"{label}/{level}/selectionAnalysis/protectedRecovery"
        )
        if view_spendable != spendable or view_protected != protected:
            raise ValueError(f"{label}/{level}: selection analysis account views differ from authored accounts")
        if not isinstance(view.get("selections"), list) or not isinstance(view.get("affordableSelections"), list):
            raise ValueError(f"{label}/{level}: malformed selection rows")
        affordable_counts[level] = len(view["affordableSelections"])

    roster = _v3_enemy_roster(profile, campaign, episode_id)
    world = profile.get("worldContract")
    if not isinstance(world, dict) or not isinstance(world.get("entities"), list):
        raise ValueError(f"{label}: malformed reference profile worldContract")
    entities = world["entities"]
    if any(not isinstance(entity, dict) or not isinstance(entity.get("role"), str) for entity in entities):
        raise ValueError(f"{label}: malformed main-world entity role")
    hostile_roles = sum(
        any(word in entity["role"].lower() for word in ("hostile", "enemy"))
        for entity in entities
    )
    roster_hostiles = bool(roster["initialEntityIds"]) or any(
        mobilization["entityIds"] for mobilization in roster["mobilizations"]
    )
    has_hostiles = roster_hostiles or hostile_roles > 0

    objective_plan = profile.get("objectivePlan")
    secondary_objectives = profile.get("secondaryObjectives")
    if not isinstance(objective_plan, list) or not isinstance(secondary_objectives, list):
        raise ValueError(f"{label}: malformed objective views in reference profile")
    deadlines = deadline_fields({
        "objectivePlan": objective_plan,
        "secondaryObjectives": secondary_objectives,
    })
    same_budget = budgets["easy"] == budgets["standard"] == budgets["hard"]
    return {
        "campaign": campaign,
        "order": episode.get("order"),
        "episodeId": episode_id,
        "designProfile": V3_DESIGN_PROFILE,
        "coreMechanic": episode.get("coreMechanic"),
        "pressureMechanism": {
            "finiteHostilesPresent": has_hostiles,
            "explicitStructuredDeadlinePresent": bool(deadlines),
            "deadlineFields": deadlines,
            "otherMainPredicateKinds": predicate_kinds(objective_plan),
            "otherSecondaryPredicateKinds": predicate_kinds(secondary_objectives),
        },
        "mainObjectiveCount": len(objective_plan),
        "secondaryObjectiveCount": len(secondary_objectives),
        "hostileRoleEntityCount": hostile_roles,
        "authoredEnemyRoster": roster,
        "budgetBasis": "v3 initial spendable operating account; excludes protected recovery and unearned optional rewards",
        "accountsByDifficulty": accounts,
        "selectionAnalysisByDifficulty": selection_analysis,
        "affordableSelectionCountByDifficulty": affordable_counts,
        "accessibleBudgetSameAcrossDifficulties": same_budget,
        "staticRiskCandidate": not has_hostiles and not deadlines and same_budget,
    }


def episode_audit(campaign, episode):
    if not isinstance(episode, dict):
        raise ValueError(f"{campaign}: episode must be an object")
    if "designProfile" not in episode:
        return _legacy_episode_audit(campaign, episode)
    if episode["designProfile"] != V3_DESIGN_PROFILE:
        raise ValueError(f"{campaign}/{episode.get('id')}: unsupported designProfile {episode['designProfile']!r}")
    return _v3_episode_audit(campaign, episode)


def build_audit(root=ROOT):
    policy = read(POLICY, root)
    paths = [f"docs/design/odysseys/{item['id']}.json" for item in policy["campaigns"]]
    before = fingerprints([POLICY, *paths], root)
    campaigns = [read(path, root) for path in paths]
    records = [episode_audit(campaign["campaignId"], episode)
               for campaign in campaigns for episode in campaign["episodes"]]
    after = fingerprints([POLICY, *paths], root)
    if before != after:
        raise ValueError("Sources changed during audit; rerun on a stable snapshot")
    risks = [record for record in records if record["staticRiskCandidate"]]
    limits = [
        "Static inspection only: no historical, architectural, native or playability approval.",
        "Role names and deadline keys are heuristic signals, not evidence of working AoE2 opposition.",
        "Logistics, terrain, allocation and optional opportunity costs require separate design/playtest assessment.",
        "A dossier without a risk flag does not thereby pass difficulty, balance or engagement QA.",
    ]
    if any(record.get("designProfile") == V3_DESIGN_PROFILE for record in records):
        limits.append("Finite v3 financial alternatives are not gathering, timing or game evidence.")
    return {
        "sourceSha256": before,
        "scope": "All policy campaigns; only authored episodes[] dossiers counted",
        "riskRule": "No structured hostile cap/entity, no positive structured deadline key, identical accessible budgets across all three difficulties",
        "limits": limits,
        "counts": {
            "dossierCount": len(records),
            "byCampaign": {c["campaignId"]: len(c["episodes"]) for c in campaigns},
            "staticRiskCandidates": len(risks),
            "staticRiskCandidatesByCampaign": {
                c["campaignId"]: sum(r["campaign"] == c["campaignId"] for r in risks)
                for c in campaigns
            },
            "withFiniteHostiles": sum(r["pressureMechanism"]["finiteHostilesPresent"] for r in records),
            "withExplicitStructuredDeadlines": sum(r["pressureMechanism"]["explicitStructuredDeadlinePresent"] for r in records),
            "sameAccessibleBudgetsAcrossDifficulties": sum(r["accessibleBudgetSameAcrossDifficulties"] for r in records),
            "totalMainObjectives": sum(r["mainObjectiveCount"] for r in records),
            "totalSecondaryObjectives": sum(r["secondaryObjectiveCount"] for r in records),
            "totalScreens": sum(len(e["screens"]) for c in campaigns for e in c["episodes"]),
        },
        "staticRiskEpisodes": [{key: r[key] for key in ("campaign", "order", "episodeId")} for r in risks],
        "episodes": records,
    }


def check_report(report, audit):
    if report.get("schemaVersion") != 2 or any(report.get(key) != value for key, value in audit.items()):
        raise ValueError("Stale mechanical audit; regenerate with --write --author REAL_ID --date YYYY-MM-DD")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Replace the current report; default checks only")
    parser.add_argument("--author", help="Real model/person identity for a new snapshot")
    parser.add_argument("--date", type=datetime.date.fromisoformat, help="Actual audit date (YYYY-MM-DD)")
    args = parser.parse_args()
    audit = build_audit()
    if args.write:
        if not args.author or not args.date:
            parser.error("--write requires --author and --date; provenance is never inferred")
        report = {"schemaVersion": 2, "snapshot": {
            "date": args.date.isoformat(), "realIdentity": args.author,
            "method": "tools/design/civic_difficulty_audit.script.py",
        }, **audit}
        (ROOT / REPORT).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    else:
        report = read(REPORT)
        check_report(report, audit)
    print(json.dumps(audit["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
