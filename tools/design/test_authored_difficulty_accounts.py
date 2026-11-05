"""Artificial factory and validator coverage for explicit finite accounts."""

import copy
import json
import runpy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/design"))
RESOURCES = ("food", "wood", "gold", "stone")


class AuthoredDifficultyAccountsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pipeline = runpy.run_path(str(ROOT / "tools/design/episode_dossiers.script.py"))
        cls.factory, cls.validator = cls.pipeline["factory"], cls.pipeline["validator"]
        cls.helper = runpy.run_path(str(ROOT / "tools/design/authored_difficulty_accounts.helper.py"))

    def fixture(self):
        campaign = json.loads((ROOT / "docs/design/odysseys/imperial-church.json").read_text())
        authored = copy.deepcopy(next(row for row in campaign["episodeBlueprints"] if row.get("order") == 1))
        selection = next(row for row in campaign["episodeSelection"] if row["id"] == authored["episodeId"])
        next_selection = next(row for row in campaign["episodeSelection"] if row["order"] == selection["order"] + 1)
        geography = json.loads((ROOT / "docs/design/geography.json").read_text())
        profile = next(row for row in geography["profiles"] if row["id"] == selection["geographyId"])
        baseline = json.loads((ROOT / "docs/design/catalog.json").read_text())["campaigns"]
        return campaign, authored, selection, profile, next_selection, baseline

    def make_accounts(self, rewards):
        return {
            level: {
                "spendable": {"food": stock, "wood": stock, "gold": stock, "stone": stock},
                "gatherableBank": {key: 0 for key in RESOURCES},
                "protectedRecovery": {"food": 7, "wood": 5, "gold": 3, "stone": 2},
                "optionalReserve": copy.deepcopy(rewards),
            }
            for level, stock in (("easy", 1000000), ("standard", 800000), ("hard", 600000))
        }

    def test_real_factory_validator_and_civic_accept_three_different_profiles(self):
        campaign, authored, selection, geography, successor, baseline = self.fixture()
        original = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        authored["authoredDifficultyAccounts"] = self.make_accounts(original["secondaryBudget"]["reservedRewards"])
        authored.pop("protectedRecoveryStock", None)
        authored.pop("startingResources", None)
        authored.pop("discretionaryMargin", None)
        draft = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        self.assertEqual(draft["economyProfile"], "authored-finite-accounts-v1")
        self.assertEqual(draft["secondaryBudget"]["reallocatedCacheAllowance"], draft["secondaryBudget"]["reservedRewards"])
        self.assertEqual([draft["difficulty"][x]["startingResources"]["food"] for x in ("easy", "standard", "hard")], [1000000, 800000, 600000])
        for level in ("easy", "standard", "hard"):
            row = draft["difficulty"][level]
            self.assertEqual(row["gatherableBank"], {key: 0 for key in RESOURCES})
            self.assertEqual(row["accessibleWithoutOptionalRewards"]["food"], row["startingResources"]["food"])
            self.assertEqual(row["protectedRecoveryStock"]["food"], 7)
            self.assertEqual(row["supplyMargins"]["food"], row["startingResources"]["food"] - row["mandatoryDeliveries"]["food"] - row["replacementBudget"]["food"])
            self.assertTrue(row["mainFeasibleSkippingAllOptionals"])
            self.assertTrue(row["allOptionalCostsAffordable"])
        self.assertEqual(self.validator.audit_dossier(draft, campaign, baseline), [])
        self.assertIn("Explicit finite difficulty accounts", self.pipeline["wiki"](campaign, draft))
        civic = runpy.run_path(str(ROOT / "tools/design/civic_difficulty_audit.script.py"))
        record = civic["episode_audit"](campaign["campaignId"], draft)
        self.assertEqual(record["economyModel"]["profile"], draft["economyProfile"])
        self.assertEqual(record["difficulty"]["hard"]["accessibleWithoutOptionalRewards"], draft["difficulty"]["hard"]["accessibleWithoutOptionalRewards"])

    def test_absent_opt_in_remains_legacy_and_is_byte_equal(self):
        campaign, authored, selection, geography, successor, baseline = self.fixture()
        expected = next(row for row in campaign["episodes"] if row["id"] == selection["id"])
        actual = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        self.assertNotIn("economyProfile", actual)
        self.assertEqual(json.dumps(actual, sort_keys=True, separators=(",", ":")), json.dumps(expected, sort_keys=True, separators=(",", ":")))
        wiki_path = ROOT / "docs/wiki" / campaign["campaignId"] / "episodes" / selection["id"] / "15-odyssey-dossier.md"
        self.assertEqual(self.pipeline["wiki"](campaign, actual), wiki_path.read_text())

    def test_source_shape_numeric_alias_and_feasibility_rejections(self):
        good = self.make_accounts({key: 0 for key in RESOURCES})
        mutations = []
        for level in ("easy", "standard", "hard"):
            bad = copy.deepcopy(good); bad[level]["spendable"]["food"] = True; mutations.append(bad)
            bad = copy.deepcopy(good); bad[level]["spendable"]["food"] = 1.5; mutations.append(bad)
            bad = copy.deepcopy(good); bad[level]["spendable"]["food"] = -1; mutations.append(bad)
            bad = copy.deepcopy(good); bad[level]["spendable"]["ore"] = 1; mutations.append(bad)
            bad = copy.deepcopy(good); del bad[level]["spendable"]["wood"]; mutations.append(bad)
            bad = copy.deepcopy(good); bad[level]["spendable"]["food"] = 2**53; mutations.append(bad)
            bad = copy.deepcopy(good); bad[level]["spendable"]["food"] = 2**53 - 1; bad[level]["gatherableBank"]["food"] = 1; mutations.append(bad)
        for malformed in ({}, {"easy": {}, "standard": {}, "hard": {}}, {**good, "extra": {}}, None):
            with self.subTest(malformed=malformed), self.assertRaises(ValueError):
                self.helper["read_source"](malformed)
        for accounts in mutations:
            with self.subTest(accounts=accounts):
                with self.assertRaises(ValueError): self.helper["read_source"](accounts)
        campaign, authored, selection, geography, successor, baseline = self.fixture()
        authored["authoredDifficultyAccounts"] = good
        authored["startingResources"] = {key: 1 for key in RESOURCES}
        with self.assertRaisesRegex(ValueError, "cannot be combined"):
            self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        authored.pop("startingResources")
        authored["economyProfile"] = "authored-finite-accounts-v1"
        with self.assertRaisesRegex(ValueError, "cannot be authored directly"):
            self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)

    def test_derived_marker_and_timing_audit_fail_closed(self):
        campaign, authored, selection, geography, successor, baseline = self.fixture()
        original = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        authored["authoredDifficultyAccounts"] = self.make_accounts(original["secondaryBudget"]["reservedRewards"])
        authored.pop("protectedRecoveryStock", None)
        authored.pop("startingResources", None)
        authored.pop("discretionaryMargin", None)
        draft = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        timing = runpy.run_path(str(ROOT / "tools/design/readiness_timing_audit.script.py"))
        with self.assertRaisesRegex(ValueError, "does not support economyProfile"):
            timing["build_report"]({"objectiveId": "missing"}, draft)
        malformed = copy.deepcopy(draft); malformed["economyProfile"] = "mystery"
        self.assertTrue(any("unsupported economyProfile" in error for error in self.validator.audit_dossier(malformed)))
        v3 = copy.deepcopy(draft); v3["designProfile"] = "alternative-fulfillment-v3"
        self.assertTrue(any("not supported with designProfile" in error for error in self.validator.audit_dossier(v3)))
        bad_margin = copy.deepcopy(draft); bad_margin["difficulty"]["easy"]["supplyMargins"]["food"] += 1
        self.assertTrue(any("authored finite account audit failed" in error for error in self.validator.audit_dossier(bad_margin)))

    def test_alias_infeasible_main_and_unaffordable_optional_rows_fail_in_real_factory(self):
        campaign, authored, selection, geography, successor, baseline = self.fixture()
        original = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        accounts = self.make_accounts(original["secondaryBudget"]["reservedRewards"])
        for level in accounts:
            accounts[level]["protectedRecovery"]["food"] = 7
        authored["authoredDifficultyAccounts"] = accounts
        authored["protectedRecoveryStock"] = {"food": 8, "wood": 5, "gold": 3, "stone": 2}
        authored.pop("startingResources", None); authored.pop("discretionaryMargin", None)
        with self.assertRaisesRegex(ValueError, "protectedRecoveryStock alias conflicts"):
            self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)

        authored.pop("protectedRecoveryStock")
        authored["authoredDifficultyAccounts"]["easy"]["spendable"] = {key: 0 for key in RESOURCES}
        with self.assertRaisesRegex(ValueError, "cannot fund mandatory payments"):
            self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)

        campaign, authored, selection, geography, successor, baseline = self.fixture()
        for task in authored["optionalTasks"]:
            if task["kind"] in ("aid", "extract", "repair", "trade"):
                task["resourceReward"] = {}
        authored.pop("startingResources", None); authored.pop("discretionaryMargin", None)
        authored.pop("protectedRecoveryStock", None)
        authored["authoredDifficultyAccounts"] = self.make_accounts({key: 0 for key in RESOURCES})
        authored["authoredDifficultyAccounts"]["hard"]["spendable"]["gold"] = 600
        with self.assertRaisesRegex(ValueError, "all optional payments are not affordable"):
            self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)


if __name__ == "__main__":
    unittest.main()
