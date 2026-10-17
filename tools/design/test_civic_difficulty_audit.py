"""Regressions for static-audit false pressure signals and missing inputs."""

import copy
import runpy
import unittest
from pathlib import Path

audit = runpy.run_path(str(Path(__file__).with_name("civic_difficulty_audit.script.py")))


class CivicDifficultyAuditTests(unittest.TestCase):
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
