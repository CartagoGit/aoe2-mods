"""Artificial factory and validator coverage for explicit finite accounts."""

import copy
import datetime
import hashlib
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
        cls.finite = runpy.run_path(str(ROOT / "tools/design/finite_allocation.helper.py"))

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

    def test_review_regressions_reject_derived_overflow_and_raw_boolean_payment(self):
        campaign, authored, selection, geography, successor, baseline = self.fixture()
        original = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        authored["authoredDifficultyAccounts"] = self.make_accounts(original["secondaryBudget"]["reservedRewards"])
        for field in ("protectedRecoveryStock", "startingResources", "discretionaryMargin"):
            authored.pop(field, None)
        draft = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        limit = 2**53 - 1
        for row in draft["difficulty"].values():
            row["startingResources"]["food"] = limit
            row["accessibleWithoutOptionalRewards"]["food"] = limit
            row["supplyMargins"]["food"] = limit - row["mandatoryDeliveries"]["food"] - row["replacementBudget"]["food"]
        errors = self.validator.audit_dossier(draft, campaign, baseline)
        self.assertTrue(any("safe integer" in error for error in errors), errors)
        civic = runpy.run_path(str(ROOT / "tools/design/civic_difficulty_audit.script.py"))
        with self.assertRaisesRegex(ValueError, "safe integer"):
            civic["episode_audit"](campaign["campaignId"], draft)

        campaign, authored, selection, geography, successor, baseline = self.fixture()
        authored["authoredDifficultyAccounts"] = self.make_accounts({key: 0 for key in RESOURCES})
        for field in ("protectedRecoveryStock", "startingResources", "discretionaryMargin"):
            authored.pop(field, None)
        payment = next(req for obj in authored["mainObjectives"] for req in obj["requirements"]
                       if req["kind"] == "resource-transaction")
        payment["amounts"]["food"] = True
        with self.assertRaisesRegex(ValueError, "Resource amounts must be nonnegative integers"):
            self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)

    def test_all_31_architecture_cases_with_executable_results(self):
        case_file = ROOT / "docs/qa/campaign-design/authored-difficulty-accounts-cases.json"
        cases = json.loads(case_file.read_text())["prospectiveRejectionCases"]
        self.assertEqual(len(cases), 31)
        results = []

        def record(case_id, assertion):
            with self.subTest(case=case_id):
                assertion()
            results.append({"id": case_id, "result": "pass"})

        def source():
            return self.make_accounts({key: 0 for key in RESOURCES})

        def context():
            campaign, authored, selection, geography, successor, baseline = self.fixture()
            original = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
            authored["authoredDifficultyAccounts"] = self.make_accounts(original["secondaryBudget"]["reservedRewards"])
            for field in ("protectedRecoveryStock", "startingResources", "discretionaryMargin"):
                authored.pop(field, None)
            return campaign, authored, selection, geography, successor, baseline

        def rejects_source(case_id, mutation):
            value = source()
            mutation(value)
            with self.assertRaises(ValueError):
                self.helper["read_source"](value)

        record("missing-difficulty", lambda: rejects_source("missing-difficulty", lambda x: x.pop("hard")))
        record("unknown-difficulty", lambda: rejects_source("unknown-difficulty", lambda x: x.update(nightmare=copy.deepcopy(x["hard"]))))
        record("missing-account", lambda: rejects_source("missing-account", lambda x: x["hard"].pop("optionalReserve")))
        record("unknown-account", lambda: rejects_source("unknown-account", lambda x: x["hard"].update(cacheAllowance={key: 0 for key in RESOURCES})))
        record("missing-resource", lambda: rejects_source("missing-resource", lambda x: x["hard"]["spendable"].pop("stone")))
        record("unknown-resource", lambda: rejects_source("unknown-resource", lambda x: x["hard"]["spendable"].update(faith=1)))
        record("negative", lambda: rejects_source("negative", lambda x: x["hard"]["gatherableBank"].update(food=-1)))
        record("boolean", lambda: rejects_source("boolean", lambda x: x["hard"]["spendable"].update(food=True)))
        record("fraction", lambda: rejects_source("fraction", lambda x: x["hard"]["spendable"].update(food=1.5)))
        record("unsafe", lambda: rejects_source("unsafe", lambda x: x["hard"]["spendable"].update(food=2**53)))
        record("nonfinite", lambda: rejects_source("nonfinite", lambda x: x["hard"]["spendable"].update(food=float("inf"))))

        def alias(field):
            campaign, authored, selection, geography, successor, baseline = context()
            authored[field] = {key: 1 for key in RESOURCES}
            with self.assertRaises(ValueError): self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        record("conflicting-start-alias", lambda: alias("startingResources"))
        record("conflicting-margin-alias", lambda: alias("discretionaryMargin"))

        def recovery_alias():
            campaign, authored, selection, geography, successor, baseline = context()
            authored["protectedRecoveryStock"] = {"food": 0}
            with self.assertRaisesRegex(ValueError, "alias conflicts"):
                self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        record("recovery-alias", recovery_alias)

        def reward_account(delta):
            campaign, authored, selection, geography, successor, baseline = context()
            authored["authoredDifficultyAccounts"]["easy"]["optionalReserve"]["food"] += delta
            with self.assertRaisesRegex(ValueError, "optionalReserve must equal"):
                self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        record("reward-shortfall", lambda: reward_account(-1))
        record("reward-excess", lambda: reward_account(1))

        def main_cannot_borrow(source_account):
            campaign, authored, selection, geography, successor, baseline = context()
            row = authored["authoredDifficultyAccounts"]["easy"]
            row["spendable"]["food"] = 0
            if source_account == "protectedRecovery":
                row[source_account]["food"] = 1000000
            with self.assertRaisesRegex(ValueError, "cannot fund mandatory payments"):
                self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        record("protected-main", lambda: main_cannot_borrow("protectedRecovery"))
        record("reward-main", lambda: main_cannot_borrow("optionalReserve"))

        def self_funding():
            tasks = [{"id": "trade", "cost": {"food": 0, "wood": 0, "gold": 20, "stone": 0},
                      "reward": {"food": 0, "wood": 0, "gold": 20, "stone": 0}}]
            states = self.finite["optional_states"]({key: 0 for key in RESOURCES}, tasks)
            self.assertNotIn(1, states)
        record("self-funding", self_funding)

        def no_actual_rows():
            campaign, authored, selection, geography, successor, baseline = context()
            with self.assertRaisesRegex(ValueError, "materialized optional task rows"):
                self.factory.difficulty_profiles(authored, {}, {})
        record("missing-task-inputs", no_actual_rows)

        def duplicate_side_id():
            campaign, authored, selection, geography, successor, baseline = context()
            draft = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
            draft["secondaryObjectives"][1]["id"] = draft["secondaryObjectives"][0]["id"]
            self.assertTrue(any("duplicate optional task identity" in e for e in self.validator.audit_dossier(draft, campaign, baseline)))
        record("duplicate-once", duplicate_side_id)

        def unapproved_bank_is_explicit_only():
            campaign, authored, selection, geography, successor, baseline = context()
            authored["authoredDifficultyAccounts"]["easy"]["gatherableBank"]["food"] = 25
            draft = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
            self.assertEqual(draft["difficulty"]["easy"]["gatherableBank"]["food"], 25)
            self.assertEqual(draft["secondaryBudget"]["nativeStatus"], "design-only; requires certified reusable predicates and native QA")
        record("unapproved-bank", unapproved_bank_is_explicit_only)

        def aggregate_overflow():
            value = source()
            value["hard"]["spendable"]["food"] = 2**53 - 1
            with self.assertRaisesRegex(ValueError, "overflows safe integer"):
                self.helper["read_source"](value)
        record("aggregate-overflow", aggregate_overflow)

        def optional_count(count):
            campaign, authored, selection, geography, successor, baseline = context()
            base = authored["optionalTasks"]
            authored["optionalTasks"] = base[:count] if count < 6 else base + [copy.deepcopy(base[0]) for _ in range(count - len(base))]
            if count > len(base):
                for index, task in enumerate(authored["optionalTasks"][len(base):], len(base) + 1):
                    task["title"] = {"en": f"Extra task {index}", "es-ES": f"Tarea extra {index}"}
            with self.assertRaisesRegex(ValueError, "6–8"):
                self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        def count_bounds(): optional_count(5); optional_count(9)
        record("optional-count", count_bounds)

        def no_full_witness():
            campaign, authored, selection, geography, successor, baseline = self.fixture()
            for task in authored["optionalTasks"]:
                if task["kind"] in ("aid", "extract", "repair", "trade"):
                    task["resourceReward"] = {}
            next(row for row in authored["optionalTasks"] if row["kind"] == "aid")["resourceReward"] = {"gold": 10}
            trade = next(row for row in authored["optionalTasks"] if row["kind"] == "trade")
            trade["resourceCost"] = {"gold": 20}
            trade["instruction"] = {"en": "Pay twenty gold once.", "es-ES": "Paga veinte de oro una vez."}
            original = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
            authored["authoredDifficultyAccounts"] = self.make_accounts(original["secondaryBudget"]["reservedRewards"])
            for field in ("protectedRecoveryStock", "startingResources", "discretionaryMargin"):
                authored.pop(field, None)
            authored["authoredDifficultyAccounts"]["hard"]["spendable"]["gold"] = 600
            with self.assertRaisesRegex(ValueError, "all optional payments are not affordable"):
                self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        record("no-full-witness", no_full_witness)

        def marker_rejected(marker, v3=False):
            campaign, authored, selection, geography, successor, baseline = context()
            draft = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
            draft["economyProfile"] = marker
            if v3: draft["designProfile"] = "alternative-fulfillment-v3"
            self.assertTrue(self.validator.audit_dossier(draft, campaign, baseline))
            civic = runpy.run_path(str(ROOT / "tools/design/civic_difficulty_audit.script.py"))
            with self.assertRaises(ValueError): civic["episode_audit"](campaign["campaignId"], draft)
        record("unknown-economy-mode", lambda: marker_rejected("unknown"))
        record("v3-economy-marker", lambda: marker_rejected("authored-finite-accounts-v1", True))

        def wrong_margin():
            campaign, authored, selection, geography, successor, baseline = context()
            draft = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
            draft["difficulty"]["easy"]["supplyMargins"]["food"] += 1
            self.assertTrue(self.validator.audit_dossier(draft, campaign, baseline))
            civic = runpy.run_path(str(ROOT / "tools/design/civic_difficulty_audit.script.py"))
            with self.assertRaisesRegex(ValueError, "derivation drift"):
                civic["episode_audit"](campaign["campaignId"], draft)
        record("wrong-new-margin", wrong_margin)

        def direct_output_marker():
            campaign, authored, selection, geography, successor, baseline = context()
            authored["economyProfile"] = "authored-finite-accounts-v1"
            with self.assertRaisesRegex(ValueError, "cannot be authored directly"):
                self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
        record("direct-output-marker-input", direct_output_marker)

        def legacy_drift():
            campaign, authored, selection, geography, successor, baseline = self.fixture()
            draft = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
            draft["difficulty"]["easy"]["accessibleWithoutOptionalRewards"]["food"] += 1
            self.assertTrue(any("nonoptional stock drift" in e for e in self.validator.audit_dossier(draft, campaign, baseline)))
        record("legacy-default-checks", legacy_drift)

        def timing_unknown_and_known():
            campaign, authored, selection, geography, successor, baseline = context()
            draft = self.factory.build_dossier(campaign, selection, authored, geography, successor, baseline)
            timing = runpy.run_path(str(ROOT / "tools/design/readiness_timing_audit.script.py"))
            for marker in ("authored-finite-accounts-v1", "unknown"):
                target = copy.deepcopy(draft); target["economyProfile"] = marker
                with self.assertRaisesRegex(ValueError, "does not support economyProfile"):
                    timing["build_report"]({"objectiveId": "absent"}, target)
        record("timing-unsupported", timing_unknown_and_known)

        self.assertEqual({row["id"] for row in results}, {row["id"] for row in cases})
        evidence_dir = ROOT / ".cache/artifacts/i00013-S2"
        evidence_dir.mkdir(parents=True, exist_ok=True)
        evidence = {
            "schemaVersion": 1, "proposal": "i00013", "slice": "S2",
            "productCommit": "bef5374dd305966e0c56f4529d281f1ffc0b1fee",
            "test": "test_all_31_architecture_cases_with_executable_results",
            "command": "python3 -m unittest -v tools.design.test_authored_difficulty_accounts.AuthoredDifficultyAccountsTests.test_all_31_architecture_cases_with_executable_results",
            "sourceCaseFileSha256": hashlib.sha256(case_file.read_bytes()).hexdigest(),
            "sourceCaseFlagsChanged": False,
            "completedAtUtc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "count": 31, "result": "pass", "cases": results,
        }
        (evidence_dir / "acceptance-cases.json").write_text(json.dumps(evidence, indent=2) + "\n")


if __name__ == "__main__":
    unittest.main()
