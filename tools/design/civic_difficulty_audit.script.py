"""Recompute static difficulty signals; never certify playability or game tests.

The policy supplies campaign coverage. Only materialized episodes[] are audited;
episodeSelection[] and episodeBlueprints[] never count as finished dossiers.
"""

import argparse
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = "docs/research/odyssey-research/civic-difficulty-mechanical-audit.json"
POLICY = "docs/design/odyssey-policy.json"
LEVELS = ("easy", "standard", "hard")
RESOURCES = {"food", "wood", "gold", "stone"}


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def fingerprints(paths):
    return {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
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

    def walk(value, path=""):
        if isinstance(value, dict):
            for key, item in value.items():
                child = f"{path}/{key}"
                name = normalized(key)
                excluded = any(term in name for term in (
                    "neverusetimerinstead", "roughdurationminutes",
                    "warningseconds", "offsetseconds",
                ))
                if not excluded and any(term in name for term in (
                    "deadline", "timelimit", "countdown", "expires", "clock",
                )) and bool(item):
                    if not isinstance(item, (int, float)) or item > 0:
                        found.append(child)
                walk(item, child)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                walk(item, f"{path}/{index}")

    walk(episode)
    return sorted(found)


def episode_audit(campaign, episode):
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


def build_audit():
    policy = read(POLICY)
    paths = [f"docs/design/odysseys/{item['id']}.json" for item in policy["campaigns"]]
    before = fingerprints([POLICY, *paths])
    campaigns = [read(path) for path in paths]
    records = [episode_audit(campaign["campaignId"], episode)
               for campaign in campaigns for episode in campaign["episodes"]]
    after = fingerprints([POLICY, *paths])
    if before != after:
        raise ValueError("Sources changed during audit; rerun on a stable snapshot")
    risks = [record for record in records if record["staticRiskCandidate"]]
    return {
        "sourceSha256": before,
        "scope": "All policy campaigns; only authored episodes[] dossiers counted",
        "riskRule": "No structured hostile cap/entity, no positive structured deadline key, identical accessible budgets across all three difficulties",
        "limits": [
            "Static inspection only: no historical, architectural, native or playability approval.",
            "Role names and deadline keys are heuristic signals, not evidence of working AoE2 opposition.",
            "Logistics, terrain, allocation and optional opportunity costs require separate design/playtest assessment.",
            "A dossier without a risk flag does not thereby pass difficulty, balance or engagement QA.",
        ],
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
        if report.get("schemaVersion") != 2 or any(report.get(key) != value for key, value in audit.items()):
            raise ValueError("Stale mechanical audit; regenerate with --write --author REAL_ID --date YYYY-MM-DD")
    print(json.dumps(audit["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
