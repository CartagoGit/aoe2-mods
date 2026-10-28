"""Real native inspection of the bounded historical opening; no engine execution."""

import contextlib
import copy
import io
import json
import runpy
import tempfile
import unittest
from pathlib import Path

from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

ROOT = Path(__file__).resolve().parents[3]
BUILDER = runpy.run_path(str(ROOT / "tools/python/build_delivery_episode.script.py"))
ADAPTER = runpy.run_path(str(ROOT / "tools/python/native_delivery.adapter.py"))
SIGNATURE = runpy.run_path(str(ROOT / "tools/python/native_signature.helper.py"))
BINDING = (
    ROOT
    / "docs/wiki/faith-origins/episodes/01-administrative-records-caesarea/16-native-binding.json"
)


class NativeDeliveryControllerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.campaign, cls.dossier, cls.binding = BUILDER["load_delivery_source"](
            ROOT, BINDING
        )
        cls.temporary = tempfile.TemporaryDirectory(prefix="native-delivery-tests-")
        cls.output = Path(cls.temporary.name) / "variant"
        cls.inputs_before = copy.deepcopy((cls.dossier, cls.binding))
        coast = BUILDER["coast_intersections"](ROOT, cls.binding)
        with contextlib.redirect_stdout(io.StringIO()):
            cls.path, cls.receipt = BUILDER["build_variant"](
                ROOT,
                cls.dossier,
                cls.binding,
                coast,
                cls.output,
                "es-ES",
                "hard",
                "1.59",
            )
            cls.scenario = AoE2DEScenario.from_file(str(cls.path))
        cls.triggers = {t.name: t for t in cls.scenario.trigger_manager.triggers}
        cls.variables = cls.receipt["variables"]
        cls.xs = (cls.output / "native-controller.xs").read_text()

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def test_real_native_originals_stock_and_generation_are_bound_without_source_mutation(
        self,
    ):
        self.assertEqual(self.inputs_before, (self.dossier, self.binding))
        self.assertEqual(320, self.scenario.map_manager.map_size)
        ids = self.receipt["nativeOriginalHandles"]
        self.assertEqual(13, len(ids))
        self.assertEqual(13, len(set(ids.values())))
        self.assertEqual(0, ids[self.binding["collection"]["entities"][0]])
        self.assertEqual(
            (297, 127, 72, 0),
            tuple(
                getattr(self.scenario.player_manager.players[1], r)
                for r in ("food", "wood", "gold", "stone")
            ),
        )
        initial = self.triggers["cdf-delivery-initialize"]
        writes = {
            e.variable: e.quantity
            for e in initial.effects
            if e.effect_type == EffectId.CHANGE_VARIABLE
        }
        self.assertEqual(0, writes[self.variables["register-issued"]])
        self.assertEqual(0, writes[self.variables["copy-payment"]])
        self.assertEqual(
            [550, 200, 25, 0],
            [
                writes[self.variables["optional-reserve-" + r]]
                for r in ("food", "wood", "gold", "stone")
            ],
        )
        self.assertEqual(self.variables["ready"], initial.effects[-1].variable)
        self.assertEqual(1, initial.effects[-1].quantity)
        self.assertFalse(self.receipt["gameVerified"])

    def test_delivery_uses_original_spatial_observations_and_accumulated_court_arrivals(
        self,
    ):
        copying = self.triggers["cdf-copy-command"]
        court_flags = [self.variables["copy-court-arrival-" + str(i)] for i in range(3)]
        found = {
            c.variable
            for c in copying.conditions
            if c.condition_type == ConditionId.VARIABLE_VALUE and c.quantity == 1
        }
        self.assertTrue(set(court_flags) <= found)
        selection = next(
            c
            for c in copying.conditions
            if c.condition_type == ConditionId.OBJECT_SELECTED
        )
        self.assertEqual(
            self.receipt["nativeOriginalHandles"][
                self.binding["copying"]["outputEntity"]
            ],
            selection.unit_object,
        )
        for name in (
            ["cdf-collect-" + str(i) for i in range(3)]
            + ["cdf-copy-court-arrival-" + str(i) for i in range(3)]
            + ["cdf-original-register-delivered"]
        ):
            trigger = self.triggers[name]
            self.assertFalse(
                any(c.condition_type == ConditionId.TIMER for c in trigger.conditions)
            )
            self.assertTrue(
                any(
                    c.condition_type == ConditionId.SCRIPT_CALL
                    for c in trigger.conditions
                )
            )
        self.assertIn("xsGetGarrisonedInUnitId", self.xs)
        self.assertIn("xsGetUnitPosition", self.xs)
        self.assertIn("cdf_dx * cdf_dx + cdf_dy * cdf_dy", self.xs)

    def test_terminal_precedes_optional_rewards_and_every_action_is_guarded(self):
        order = list(self.triggers)
        self.assertLess(
            order.index("cdf-main-loss"), order.index("cdf-original-register-delivered")
        )
        for number in range(1, 7):
            key = f"side-{number}"
            reward = self.triggers[f"cdf-{key}-complete"]
            self.assertLess(
                order.index("cdf-original-register-delivered"), order.index(reward.name)
            )
            self.assertTrue(
                any(
                    c.variable == self.variables["terminal"] and c.quantity == 0
                    for c in reward.conditions
                    if c.condition_type == ConditionId.VARIABLE_VALUE
                )
            )
            self.assertIn(f"cdf-{key}-loss", self.triggers)
            self.assertIn(f"cdf-{key}-close-1", self.triggers)
            self.assertIn(f"cdf-{key}-close-2", self.triggers)
        final = self.triggers["cdf-original-register-delivered"]
        self.assertEqual(
            (self.variables["terminal"], 1),
            (final.effects[0].variable, final.effects[0].quantity),
        )
        self.assertFalse(
            any(
                e.effect_type == EffectId.STORE_KEY_VALUE
                for t in self.triggers.values()
                for e in t.effects
            )
        )

    def test_native_captions_goals_and_economic_isolation_survive_the_file(self):
        ui = [t for t in self.triggers.values() if t.display_as_objective]
        self.assertEqual(9, len(ui))
        self.assertTrue(all(t.description for t in ui))
        self.assertIn("registro", self.scenario.message_manager.instructions.lower())
        messages = [
            e.message
            for t in self.triggers.values()
            for e in t.effects
            if e.effect_type == EffectId.DISPLAY_INSTRUCTIONS
        ]
        self.assertTrue(any(x.startswith("Crónica:") for x in messages))
        self.assertTrue(any(x.startswith("Miriam de Cesarea:") for x in messages))
        self.assertTrue(any("no tienen que permanecer juntos" in x for x in messages))
        self.assertIn("xsEffectAmount(cSetAttribute,", self.xs)
        self.assertFalse(
            any(
                e.effect_type
                in (EffectId.MODIFY_ATTRIBUTE, EffectId.MODIFY_OBJECT_ATTRIBUTE)
                and e.quantity == 0
                for t in self.triggers.values()
                for e in t.effects
            )
        )
        for player in (1, 2):
            obj = self.scenario.player_manager.players[player]
            self.assertGreater(len(obj.disabled_buildings), 100)
            self.assertGreater(len(obj.disabled_units), 100)
            self.assertGreater(len(obj.disabled_techs), 100)
        self.assertFalse(
            any("effects" == name.rsplit("-", 1)[-1] for name in self.triggers)
        )
        self.assertIn("xsCreateUnit", self.xs)
        self.assertIn("0.0, 1);", self.xs)

    def test_reopened_native_signature_and_xs_are_stable(self):
        second = Path(self.temporary.name) / "second.aoe2scenario"
        with contextlib.redirect_stdout(io.StringIO()):
            self.scenario.write_to_file(str(second))
            again = AoE2DEScenario.from_file(str(second))
            again.xs_manager.xs_check.raise_on_error = True
            again.xs_manager.validate_scenario_xs()
        self.assertEqual(
            SIGNATURE["native_signature"](self.scenario),
            SIGNATURE["native_signature"](again),
        )
        self.assertEqual(87, len(self.scenario.trigger_manager.variables))

    def test_unsupported_semantics_are_rejected_before_build(self):
        mutations = [
            lambda d: d["objectivePlan"][1]["predicate"].__setitem__("operator", "any"),
            lambda d: d["secondaryObjectives"][2]["predicate"]["requirements"][
                0
            ].__setitem__("health", "half"),
            lambda d: d["secondaryObjectives"][3]["predicate"]["requirements"][
                1
            ].__setitem__("afterArrival", False),
            lambda d: d["objectivePlan"][1]["predicate"]["requirements"].__delitem__(2),
            lambda d: d["secondaryObjectives"][0]["predicate"]["requirements"][
                0
            ].__setitem__("noSubstitutes", False),
        ]
        for mutation in mutations:
            dossier = copy.deepcopy(self.dossier)
            mutation(dossier)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                ADAPTER["validate_delivery_contract"](dossier, self.binding)

    def test_duplicate_originals_early_optional_placement_and_changed_receipt_fail(
        self,
    ):
        binding = copy.deepcopy(self.binding)
        binding["entities"][1]["id"] = binding["entities"][0]["id"]
        with self.assertRaises(ValueError):
            ADAPTER["validate_delivery_contract"](self.dossier, binding)
        binding = copy.deepcopy(self.binding)
        first = self.dossier["secondaryObjectives"][0]["predicate"]["requirements"][0]
        entity = next(x for x in binding["entities"] if x["id"] == first["entities"][0])
        entity["position"] = next(
            z["centre"]
            for z in binding["zones"]
            if z["id"] == first["destinations"][entity["id"]]
        )
        with self.assertRaises(ValueError):
            ADAPTER["validate_delivery_contract"](self.dossier, binding)
        dossier = copy.deepcopy(self.dossier)
        dossier["objectivePlan"][1]["predicate"]["requirements"][1][
            "requiredPaymentReceipts"
        ][0]["newDebit"] = True
        with self.assertRaises(ValueError):
            ADAPTER["validate_delivery_contract"](dossier, self.binding)

    def test_changed_source_or_existing_output_is_not_overwritten(self):
        binding = copy.deepcopy(self.binding)
        binding["sourceSha256"] = "0" * 64
        path = Path(self.temporary.name) / "bad-binding.json"
        path.write_text(json.dumps(binding))
        target = Path(self.temporary.name) / "rejected"
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            BUILDER["build_preview"](ROOT, path, target, ["es-ES"], ["hard"])
        self.assertFalse(target.exists())
        target.mkdir()
        sentinel = target / "keep.txt"
        sentinel.write_text("original")
        with self.assertRaisesRegex(ValueError, "immutable"):
            BUILDER["build_preview"](ROOT, BINDING, target, ["es-ES"], ["hard"])
        self.assertEqual("original", sentinel.read_text())


if __name__ == "__main__":
    unittest.main()
