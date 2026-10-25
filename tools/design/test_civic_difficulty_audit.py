"""Regressions for static-audit false pressure signals and missing inputs."""

import copy
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch

audit = runpy.run_path(str(Path(__file__).with_name("civic_difficulty_audit.script.py")))


def v3_episode():
    resources = {key: 100 for key in audit["RESOURCES"]}
    accounts = {}
    selection_analysis = {}
    for index, level in enumerate(audit["LEVELS"]):
        accounts[level] = {
            "spendable": dict(resources),
            "protectedRecovery": {key: 10 + index for key in resources},
            "optionalReserve": {key: 20 + index for key in resources},
        }
        selection_analysis[level] = {
            "spendable": dict(accounts[level]["spendable"]),
            "protectedRecovery": dict(accounts[level]["protectedRecovery"]),
            "optionalReserve": dict(accounts[level]["optionalReserve"]),
            "selections": [{"recipeIds": ["fixture.recipe"], "affordable": True}],
            "affordableSelections": [["fixture.recipe"]] if index != 1 else [],
        }
    profile = {
        "schemaVersion": 3,
        "worldContract": {"entities": []},
        "objectivePlan": [],
        "secondaryObjectives": [],
        "enemyRoster": {
            "initialEntityIds": [],
            "productionEnabled": False,
            "mobilizations": [],
            "unspentPolicy": "remain-in-reserve",
        },
    }
    return {
        "id": "fixture.v3",
        "order": 1,
        "screens": [],
        "designProfile": "alternative-fulfillment-v3",
        "coreMechanic": "synthetic civic audit fixture",
        "referenceCapabilityProfile": profile,
        "accountsByDifficulty": accounts,
        "selectionAnalysisByDifficulty": selection_analysis,
        "difficulty": copy.deepcopy(selection_analysis),
    }


class CivicDifficultyAuditTests(unittest.TestCase):
    def test_v3_uses_initial_spendable_accounts_and_keeps_other_accounts_separate(self):
        episode = v3_episode()
        record = audit["episode_audit"]("fixture", episode)
        self.assertTrue(record["accessibleBudgetSameAcrossDifficulties"])
        self.assertTrue(record["staticRiskCandidate"])  # no hostiles, deadline or budget difference
        self.assertEqual(record["budgetBasis"],
                         "v3 initial spendable operating account; excludes protected recovery and unearned optional rewards")
        self.assertEqual(record["accountsByDifficulty"], episode["accountsByDifficulty"])
        self.assertEqual(record["affordableSelectionCountByDifficulty"], {
            "easy": 1, "standard": 0, "hard": 1,
        })
        self.assertNotIn("enemyTotalCapByDifficulty", record)
        self.assertNotIn("enemyScheduledReleaseCounts", record)

        episode["accountsByDifficulty"]["standard"]["spendable"]["wood"] += 1
        episode["selectionAnalysisByDifficulty"]["standard"]["spendable"]["wood"] += 1
        episode["difficulty"] = copy.deepcopy(episode["selectionAnalysisByDifficulty"])
        changed = audit["episode_audit"]("fixture", episode)
        self.assertFalse(changed["accessibleBudgetSameAcrossDifficulties"])
        self.assertFalse(changed["staticRiskCandidate"])

    def test_v3_rejects_unknown_discriminator_and_missing_or_drifted_views(self):
        episode = v3_episode()
        unknown = copy.deepcopy(episode)
        unknown["designProfile"] = "alternative-fulfillment-v4"
        with self.assertRaisesRegex(ValueError, "unsupported designProfile"):
            audit["episode_audit"]("fixture", unknown)

        for mutate in (
            lambda row: row.pop("accountsByDifficulty"),
            lambda row: row["selectionAnalysisByDifficulty"].pop("hard"),
            lambda row: row["accountsByDifficulty"]["easy"].pop("spendable"),
            lambda row: row["selectionAnalysisByDifficulty"]["easy"]["spendable"].__setitem__("wood", 99),
        ):
            malformed = copy.deepcopy(episode)
            mutate(malformed)
            with self.subTest(malformed=malformed), self.assertRaises(ValueError):
                audit["episode_audit"]("fixture", malformed)

    def test_v3_consumed_resource_amounts_must_be_non_boolean_nonnegative_safe_integers(self):
        for amount in (True, False, -1, 1.5, 2**53, None):
            episode = v3_episode()
            episode["accountsByDifficulty"]["hard"]["spendable"]["wood"] = amount
            episode["selectionAnalysisByDifficulty"]["hard"]["spendable"]["wood"] = amount
            episode["difficulty"] = copy.deepcopy(episode["selectionAnalysisByDifficulty"])
            with self.subTest(amount=amount), self.assertRaisesRegex(ValueError, "safe integer"):
                audit["episode_audit"]("fixture", episode)

    def test_v3_roster_sets_finite_pressure_without_relabeling_roles(self):
        episode = v3_episode()
        episode["referenceCapabilityProfile"]["enemyRoster"]["initialEntityIds"] = ["fixture.rostered-enemy"]
        episode["referenceCapabilityProfile"]["worldContract"]["entities"] = [
            {"id": "fixture.rostered-enemy", "role": "enemy defender"},
            {"id": "fixture.person", "role": "historical person"},
        ]
        record = audit["episode_audit"]("fixture", episode)
        self.assertTrue(record["pressureMechanism"]["finiteHostilesPresent"])
        self.assertEqual(record["hostileRoleEntityCount"], 1)
        self.assertEqual(record["authoredEnemyRoster"], episode["referenceCapabilityProfile"]["enemyRoster"])

        episode["referenceCapabilityProfile"]["enemyRoster"]["initialEntityIds"] = []
        episode["referenceCapabilityProfile"]["worldContract"]["entities"] = [
            {"id": "fixture.person", "role": "historical person"},
        ]
        record = audit["episode_audit"]("fixture", episode)
        self.assertFalse(record["pressureMechanism"]["finiteHostilesPresent"])
        self.assertEqual(record["hostileRoleEntityCount"], 0)

        episode["referenceCapabilityProfile"].pop("enemyRoster")
        with self.assertRaisesRegex(ValueError, "malformed roster"):
            audit["episode_audit"]("fixture", episode)

    def test_v3_deadline_heuristic_ignores_prose_and_zero_but_accepts_positive_predicate(self):
        episode = v3_episode()
        episode["referenceCapabilityProfile"]["objectivePlan"] = [
            {"editorialReviewNotes": {"deadline": "do not add a timer"},
             "deadlineSecondsByDifficulty": {"easy": 0, "standard": 0, "hard": 0}}
        ]
        record = audit["episode_audit"]("fixture", episode)
        self.assertFalse(record["pressureMechanism"]["explicitStructuredDeadlinePresent"])
        self.assertEqual(record["pressureMechanism"]["deadlineFields"], [])

        episode["referenceCapabilityProfile"]["objectivePlan"] = [
            {"predicate": {"requirements": [{
                "kind": "phase-deadline",
                "secondsByDifficulty": {"easy": 90, "standard": 60, "hard": 30},
            }]}}
        ]
        record = audit["episode_audit"]("fixture", episode)
        self.assertTrue(record["pressureMechanism"]["explicitStructuredDeadlinePresent"])

    def test_legacy_audit_data_still_matches_the_63_dossier_report_exactly(self):
        report = audit["read"](audit["REPORT"])
        current = audit["build_audit"]()
        audit["check_report"](report, current)
        self.assertEqual(current, {key: report[key] for key in current})
        self.assertEqual(current["counts"]["dossierCount"], 63)
        self.assertEqual(current["counts"]["staticRiskCandidates"], 54)

    def test_v3_limit_is_added_only_when_v3_records_exist(self):
        episode = v3_episode()
        expected_limit = "Finite v3 financial alternatives are not gathering, timing or game evidence."
        policy = {"campaigns": [{"id": "fixture"}]}
        campaign = {"campaignId": "fixture", "episodes": [episode]}

        def fake_read(path, root=None):
            return policy if path == audit["POLICY"] else campaign

        with patch.dict(audit["build_audit"].__globals__, {
            "read": fake_read,
            "fingerprints": lambda paths, root=None: {path: "synthetic" for path in paths},
        }):
            report = audit["build_audit"]()
        self.assertIn(expected_limit, report["limits"])
        self.assertEqual(report["episodes"][0]["designProfile"], "alternative-fulfillment-v3")
        self.assertNotIn("enemyTotalCapByDifficulty", report["episodes"][0])

    def test_metadata_prose_clock_and_zero_container_are_not_deadlines(self):
        for episode in (
            {"stateMachine": {"phaseClock": "relative-to-phase-entry"}},
            {"deadlineSecondsByDifficulty": {"easy": 0, "standard": 0, "hard": 0}},
            {"editorialReviewNotes": {"deadline": "Do not introduce any deadline"}},
            {"deadlineEnabled": True, "deadline": {"revision": 2}},
            {"roughDurationMinutes": [40, 75], "neverUseTimerInstead": True},
        ):
            with self.subTest(episode=episode):
                self.assertEqual(audit["deadline_fields"](episode), [])

    def test_positive_limits_and_real_phase_predicate_are_visible(self):
        self.assertEqual(audit["deadline_fields"]({"deadlineSeconds": 90}), ["/deadlineSeconds"])
        self.assertEqual(audit["deadline_fields"]({"deadline": {"seconds": 90}}), ["/deadline"])
        predicate = {"kind": "phase-deadline", "clock": "relative-to-phase-entry",
                     "secondsByDifficulty": {"easy": 90, "standard": 60, "hard": 30}}
        self.assertEqual(audit["deadline_fields"]({"requirements": [predicate]}),
                         ["/requirements/0/secondsByDifficulty"])

    def test_invalid_actual_phase_deadline_fails_instead_of_masking_bad_input(self):
        for limits in ({"easy": 90}, {"easy": 90, "standard": 60, "hard": 0},
                       {"easy": 90, "standard": 60, "hard": True},
                       {"easy": 90, "standard": 60, "hard": {"seconds": 30}}):
            with self.subTest(limits=limits), self.assertRaises(ValueError):
                audit["deadline_fields"]({"kind": "phase-deadline", "secondsByDifficulty": limits})

    def test_missing_profile_or_budget_cannot_look_like_equal_envelopes(self):
        episode = {"id": "example", "difficulty": {level: {
            "accessibleWithoutOptionalRewards": dict.fromkeys(audit["RESOURCES"], 100),
            "enemyTotalCap": 0,
        } for level in audit["LEVELS"]}}
        missing_profile = copy.deepcopy(episode)
        del missing_profile["difficulty"]["hard"]
        with self.assertRaises(ValueError):
            audit["episode_audit"]("example", missing_profile)
        missing_budget = copy.deepcopy(episode)
        del missing_budget["difficulty"]["hard"]["accessibleWithoutOptionalRewards"]
        with self.assertRaises(KeyError):
            audit["episode_audit"]("example", missing_budget)

    def test_changed_source_hash_or_metric_requires_report_regeneration(self):
        expected = {"sourceSha256": {"example.json": "new"}, "counts": {"dossierCount": 2}}
        for changed in ("sourceSha256", "counts"):
            report = {"schemaVersion": 2, **copy.deepcopy(expected)}
            report[changed] = {}
            with self.subTest(changed=changed), self.assertRaisesRegex(ValueError, "Stale mechanical audit"):
                audit["check_report"](report, expected)


if __name__ == "__main__":
    unittest.main()
