"""Adversarial tests for the pooled original survivor projection.

The design source projects one survivor row per authored selector. A row
selects exactly one generated object group or a nonempty list of distinct
generated object groups; the pooled row keeps the already generated
identities, origins and order. These tests drive the real factory, the real
dossier validation and the existing public loss evaluator.
"""

import copy
import json
import runpy
import shutil
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BRIDGE = ROOT / "tests/unit/pooled-survivor-projection.fixture.ts"
COURTS = ("west", "east", "south", "central")
COURT_HUBS = {court: f"hub-{index}" for index, court in enumerate(COURTS, 1)}


def _load_design_module(name):
    design = str(ROOT / "tools/design")
    if design not in sys.path:
        sys.path.insert(0, design)
    return runpy.run_path(str(ROOT / f"tools/design/{name}"))


class PooledSurvivorProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pipeline = _load_design_module("episode_dossiers.script.py")
        cls.factory = cls.pipeline["factory"]
        cls.numbers = _load_design_module("design_numbers.helper.py")

    def authored(self, survivor_rows, counts=None):
        return {
            "objectGroups": [
                {
                    "key": court,
                    "count": 2 if counts is None else counts[court],
                    "role": "artificial originals",
                    "originHub": COURT_HUBS[court],
                    "historicalMaterialPolicy": "Artificial reference, not history",
                }
                for court in COURTS
            ],
            "mainObjectives": [],
            "survivorGroups": survivor_rows,
        }

    def hubs(self):
        return [{"id": COURT_HUBS[court]} for court in COURTS]

    def project(self, survivor_rows, counts=None):
        world, _ = self.factory.world_and_objectives(
            "artificial",
            {"id": "pooled-originals"},
            self.authored(survivor_rows, counts),
            self.hubs(),
        )
        return world

    def expected_ids(self, court):
        return [
            f"artificial.pooled-originals.{court}-{index}" for index in (1, 2)
        ]

    def test_pooled_groups_project_one_row_over_the_generated_originals(self):
        world = self.project(
            [{"groups": list(COURTS), "minimumAliveOrAlreadySafe": 6}]
        )
        self.assertEqual(len(world["survivorGroups"]), 1)
        row = world["survivorGroups"][0]
        self.assertEqual(set(row), {"entities", "minimumAliveOrAlreadySafe"})
        self.assertEqual(
            row["entities"],
            [identity for court in COURTS for identity in self.expected_ids(court)],
        )
        self.assertEqual(row["minimumAliveOrAlreadySafe"], 6)

    def test_pooled_projection_keeps_the_same_entities_origins_and_identity_set(self):
        pooled = self.project(
            [{"groups": list(COURTS), "minimumAliveOrAlreadySafe": 6}]
        )
        bare = self.project([])
        self.assertEqual(pooled["entities"], bare["entities"])
        self.assertEqual(pooled["objectGroups"], bare["objectGroups"])
        self.assertEqual(len(pooled["entities"]), 8)
        self.assertEqual(len({entity["id"] for entity in pooled["entities"]}), 8)
        origins = {
            entity["id"]: (entity["initialHub"], entity["offsetTiles"])
            for entity in pooled["entities"]
        }
        self.assertEqual(
            sorted({hub for hub, _ in origins.values()}),
            sorted(COURT_HUBS.values()),
        )
        self.assertEqual(
            [origins[identity][0] for identity in self.expected_ids("west")],
            [COURT_HUBS["west"], COURT_HUBS["west"]],
        )

    def test_single_group_rows_keep_the_exact_legacy_projection(self):
        world = self.project([{"group": "west", "minimumAliveOrAlreadySafe": 2}])
        self.assertEqual(
            world["survivorGroups"],
            [
                {
                    "entities": world["objectGroups"]["west"],
                    "minimumAliveOrAlreadySafe": 2,
                }
            ],
        )
        self.assertEqual(
            world["survivorGroups"][0]["entities"], self.expected_ids("west")
        )

    def test_malformed_selectors_and_minima_are_rejected_by_the_factory(self):
        cases = {
            "both selectors": [
                {"group": "west", "groups": ["west"], "minimumAliveOrAlreadySafe": 2}
            ],
            "no selector": [{"minimumAliveOrAlreadySafe": 2}],
            "null group": [{"group": None, "minimumAliveOrAlreadySafe": 2}],
            "empty group": [{"group": "", "minimumAliveOrAlreadySafe": 2}],
            "blank group": [{"group": "   ", "minimumAliveOrAlreadySafe": 2}],
            "scalar groups": [{"groups": "west", "minimumAliveOrAlreadySafe": 2}],
            "empty groups": [{"groups": [], "minimumAliveOrAlreadySafe": 2}],
            "duplicate names": [
                {"groups": ["west", "west"], "minimumAliveOrAlreadySafe": 2}
            ],
            "blank name": [
                {"groups": ["west", " "], "minimumAliveOrAlreadySafe": 2}
            ],
            "unknown pooled name": [
                {"groups": ["north"], "minimumAliveOrAlreadySafe": 2}
            ],
            "unknown group": [{"group": "north", "minimumAliveOrAlreadySafe": 2}],
            "missing minimum": [{"group": "west"}],
            "zero minimum": [{"group": "west", "minimumAliveOrAlreadySafe": 0}],
            "negative minimum": [{"group": "west", "minimumAliveOrAlreadySafe": -1}],
            "boolean minimum": [
                {"group": "west", "minimumAliveOrAlreadySafe": True}
            ],
            "float minimum": [{"group": "west", "minimumAliveOrAlreadySafe": 2.0}],
            "string minimum": [{"group": "west", "minimumAliveOrAlreadySafe": "2"}],
            "oversized minimum": [
                {"groups": list(COURTS), "minimumAliveOrAlreadySafe": 9}
            ],
        }
        for name, rows in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(ValueError):
                    self.project(rows)

    def test_a_group_without_originals_is_rejected(self):
        with self.assertRaises(ValueError):
            self.project(
                [{"groups": ["west"], "minimumAliveOrAlreadySafe": 1}],
                counts={court: 0 for court in COURTS},
            )

    def test_repeated_identity_membership_is_rejected(self):
        pool = self.factory._survivor_pool
        forged = {"west": ["a-1", "a-2"], "east": ["a-2", "e-1"]}
        with self.assertRaises(ValueError):
            pool({"groups": ["west", "east"], "minimumAliveOrAlreadySafe": 2}, forged)

    def test_current_sources_keep_their_single_group_projection(self):
        checked = 0
        for path in sorted((ROOT / "docs/design/odysseys").glob("*.json")):
            campaign = json.loads(path.read_text(encoding="utf-8"))
            episodes = {
                episode["id"]: episode for episode in campaign.get("episodes", [])
            }
            for blueprint in campaign.get("episodeBlueprints", []):
                if "designProfile" in blueprint or not blueprint.get("survivorGroups"):
                    continue
                episode = episodes.get(blueprint["episodeId"])
                if episode is None:
                    continue
                world, _ = self.factory.world_and_objectives(
                    campaign["campaignId"],
                    {"id": episode["id"]},
                    copy.deepcopy(blueprint),
                    episode["mapPlan"]["hubs"],
                )
                self.assertEqual(
                    world["survivorGroups"],
                    episode["worldContract"]["survivorGroups"],
                )
                self.assertEqual(
                    world["entities"], episode["worldContract"]["entities"]
                )
                checked += 1
        self.assertEqual(checked, 49)

    def test_current_sources_still_author_only_single_group_rows(self):
        rows = 0
        for path in sorted((ROOT / "docs/design/odysseys").glob("*.json")):
            campaign = json.loads(path.read_text(encoding="utf-8"))
            for blueprint in campaign.get("episodeBlueprints", []):
                for row in blueprint.get("survivorGroups", []):
                    self.assertEqual(set(row), {"group", "minimumAliveOrAlreadySafe"})
                    rows += 1
        self.assertEqual(rows, 138)

    def test_generated_dossiers_keep_their_counts_and_numeric_audit(self):
        episodes = []
        for path in sorted((ROOT / "docs/design/odysseys").glob("*.json")):
            campaign = json.loads(path.read_text(encoding="utf-8"))
            episodes.extend(campaign.get("episodes", []))
        self.assertEqual(len(episodes), 64)
        self.assertEqual(
            sum(len(episode.get("screens", [])) for episode in episodes), 2645
        )
        self.assertEqual(
            sum(len(episode.get("secondaryObjectives", [])) for episode in episodes),
            398,
        )
        for episode in episodes:
            self.assertEqual(self.numbers["audit_count_thresholds"](episode), [])

    def test_artificial_factory_output_passes_the_existing_dossier_validation(self):
        world = self.project(
            [{"groups": list(COURTS), "minimumAliveOrAlreadySafe": 6}]
        )
        episode = {
            "id": "pooled-originals",
            "objectivePlan": [],
            "worldContract": world,
        }
        self.assertEqual(self.numbers["audit_count_thresholds"](episode), [])

    def bridge_payload(self):
        world = self.project(
            [{"groups": list(COURTS), "minimumAliveOrAlreadySafe": 6}]
        )
        row = world["survivorGroups"][0]
        return {
            "entities": [
                {
                    "id": entity["id"],
                    "role": entity["role"],
                    "initialHub": entity["initialHub"],
                    "offsetTiles": entity["offsetTiles"],
                    "identity": entity["identity"],
                }
                for entity in world["entities"]
            ],
            "survivorGroups": [
                {
                    "entities": list(row["entities"]),
                    "minimumAliveOrAlreadySafe": row["minimumAliveOrAlreadySafe"],
                }
            ],
            "courts": [
                {
                    "group": court,
                    "originHub": COURT_HUBS[court],
                    "entityIds": list(world["objectGroups"][court]),
                }
                for court in COURTS
            ],
        }

    def observe(self):
        bun = shutil.which("bun")
        if not bun:
            self.fail("Bun is required to execute the existing reference reducer")
        result = subprocess.run(
            [bun, "run", str(BRIDGE)],
            input=json.dumps(self.bridge_payload()),
            text=True,
            capture_output=True,
            check=False,
            cwd=ROOT,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_the_existing_loss_evaluator_tolerates_two_losses_and_defeats_on_the_third(self):
        observation = self.observe()
        self.assertEqual(observation["profile"]["validatorIssues"], [])
        for case in ("crossCourt", "sameCourt"):
            with self.subTest(case=case):
                scenario = observation["lossScenarios"][case]
                self.assertIsNone(scenario["twoLosses"]["terminal"])
                self.assertEqual(scenario["thirdLoss"]["terminal"], "defeat")
                self.assertEqual(scenario["twoLosses"]["alivePooled"], 6)
                self.assertEqual(scenario["thirdLoss"]["alivePooled"], 5)

    def test_the_bridge_keeps_the_factory_pool_origins_and_adds_only_the_loss_row(self):
        payload = self.bridge_payload()
        observation = self.observe()
        self.assertEqual(
            observation["profile"]["survivorGroups"],
            [
                {
                    "entities": payload["survivorGroups"][0]["entities"],
                    "minimumAliveOrAlreadySafe": 6,
                    "loss": "defeat",
                }
            ],
        )
        self.assertEqual(
            observation["profile"]["pooledEntities"],
            [
                {
                    "id": entity["id"],
                    "initialHub": entity["initialHub"],
                    "offsetTiles": entity["offsetTiles"],
                }
                for entity in payload["entities"]
            ],
        )
        self.assertEqual(
            sorted(observation["profile"]["districts"]),
            sorted(["hub", *COURT_HUBS.values()]),
        )

    def test_a_real_winning_control_defeats_instead_on_the_same_prior_state(self):
        observation = self.observe()
        priority = observation["priority"]
        self.assertFalse(priority["receiptOnly"]["objectiveSatisfied"])
        self.assertFalse(priority["receiptOnly"]["livePresenceSatisfied"])
        self.assertEqual(priority["receiptOnly"]["objectiveLatches"], [])
        self.assertEqual(priority["latched"]["objectiveLatches"], ["return"])
        self.assertIsNone(priority["latched"]["terminal"])
        self.assertEqual(priority["controlTick"]["terminal"], "victory")
        self.assertEqual(priority["controlTick"]["phase"], "victory")
        self.assertEqual(priority["defeatTick"]["terminal"], "defeat")
        self.assertEqual(priority["defeatTick"]["phase"], "defeat")

    def test_the_public_validator_still_rejects_duplicate_unknown_and_oversized_pools(self):
        observation = self.observe()
        cases = observation["negativeValidatorCases"]
        self.assertIn("capability.survivor-identity", cases["duplicateIdentity"])
        self.assertIn("capability.survivor-entity", cases["unknownIdentity"])
        self.assertIn("capability.survivor-threshold", cases["oversizedMinimum"])
        self.assertIn("capability.survivor-entity", cases["optionalIdentity"])


if __name__ == "__main__":
    unittest.main()
