"""Focused native evidence for the closed Jerusalem household controller.

No engine execution happens here. The binding used by these tests is an
explicitly synthetic, nonhistorical fixture that reuses the real dossier
identities; it is not the historical Jerusalem map, not the architect-owned
physical binding and not a game-played mission. Source and XS inspection
support compilation evidence only.
"""

import copy
import json
import math
import re
import runpy
import tempfile
import unittest
from pathlib import Path

from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

ROOT = Path(__file__).resolve().parents[3]
FACTORY = runpy.run_path(str(ROOT / "tools/python/native_scenario.factory.py"))
ADAPTER = runpy.run_path(str(ROOT / "tools/python/native_household.adapter.py"))
SIGNATURE = runpy.run_path(str(ROOT / "tools/python/native_signature.helper.py"))
DOSSIER = json.loads(
    (ROOT / "docs/design/odysseys/faith-origins.json").read_text(encoding="utf8")
)["episodes"][1]

PREFIX = "faith-origins.02-civilian-refuge-jerusalem"
HOUSEHOLDS = [f"{PREFIX}.households-{index}" for index in range(1, 9)]
COURT_ZONE = f"{PREFIX}.destination-2"
REFUGE_ZONE = f"{PREFIX}.destination-3"
MAP_SIZE = 64
HOUSEHOLD_POSITIONS = [
    (10.0, 30.0),
    (12.0, 30.0),
    (14.0, 30.0),
    (16.0, 30.0),
    (10.0, 32.0),
    (12.0, 32.0),
    (14.0, 32.0),
    (16.0, 32.0),
]
SIDE_BODIES = {
    "side-1.entity-1": ("villager-male", 1, (12.0, 12.0)),
    "side-1.entity-2": ("villager-female", 1, (14.0, 12.0)),
    "side-2.entity-1": ("villager-male", 1, (22.0, 22.0)),
    "side-2.entity-2": ("villager-female", 1, (24.0, 22.0)),
    "side-3.entity-1": ("house", 2, (22.0, 30.0)),
    "side-4.entity-1": ("villager-male", 1, (26.0, 30.0)),
    "side-5.entity-1": ("villager-male", 1, (16.0, 34.0)),
    "side-6.entity-1": ("villager-female", 1, (22.0, 44.0)),
    "side-6.entity-2": ("villager-male", 1, (24.0, 44.0)),
}
ZONE_CENTRES = {
    f"{PREFIX}.destination-1": (16.0, 12.0),
    COURT_ZONE: (40.0, 30.0),
    REFUGE_ZONE: (40.0, 50.0),
    "02-civilian-refuge-jerusalem.side-1.zone-1": (30.0, 30.0),
    "02-civilian-refuge-jerusalem.side-1.zone-2": (50.0, 30.0),
    "02-civilian-refuge-jerusalem.side-2.zone-1": (16.0, 20.0),
    "02-civilian-refuge-jerusalem.side-3.zone-1": (30.0, 38.0),
    "02-civilian-refuge-jerusalem.side-4.zone-1": (50.0, 38.0),
    "02-civilian-refuge-jerusalem.side-5.zone-1": (50.0, 50.0),
    "02-civilian-refuge-jerusalem.side-6.zone-1": (16.0, 44.0),
}
XS_FUNCTIONS = re.compile(r"(?:bool|void) (cdf_[A-Za-z0-9_]+)\(\) \{.*?\n\}", re.S)


def synthetic_binding():
    """An explicitly nonhistorical v1 fixture that reuses the real identities."""
    entities = []
    for index, entity in enumerate(HOUSEHOLDS):
        entities.append(
            {
                "id": entity,
                "unitType": "villager-male" if index % 2 == 0 else "villager-female",
                "player": 1,
                "position": list(HOUSEHOLD_POSITIONS[index]),
                "label": {
                    "en": f"Household {index + 1} — synthetic proxy",
                    "es-ES": f"Hogar {index + 1} — sustituto sintético",
                },
            }
        )
    for name, (unit_type, player, position) in SIDE_BODIES.items():
        entities.append(
            {
                "id": f"02-civilian-refuge-jerusalem.{name}",
                "unitType": unit_type,
                "player": player,
                "position": list(position),
                "label": {"en": f"{name} — synthetic body", "es-ES": f"{name} — cuerpo sintético"},
            }
        )
    zones = [
        {
            "id": zone,
            "centre": list(centre),
            "radius": 3,
            "label": {"en": f"{zone} — synthetic court", "es-ES": f"{zone} — patio sintético"},
        }
        for zone, centre in ZONE_CENTRES.items()
    ]
    return {
        "schemaVersion": 1,
        "kind": "private-historical-household-native-binding",
        "campaignId": "faith-origins",
        "episodeId": "02-civilian-refuge-jerusalem",
        "synthetic": True,
        "syntheticNotice": "explicitly nonhistorical test fixture; not the Jerusalem map",
        "map": {
            "size": MAP_SIZE,
            "corridors": [
                {
                    "id": "main",
                    "widthTiles": 4,
                    "points": [[12.0, 31.0], [40.0, 30.0]],
                },
                {
                    "id": "relief",
                    "widthTiles": 4,
                    "points": [[12.0, 31.0], [24.0, 44.0], [40.0, 50.0]],
                },
            ],
        },
        "entities": entities,
        "zones": zones,
        "households": {
            "entities": list(HOUSEHOLDS),
            "requiredCount": 6,
            "courtZone": COURT_ZONE,
            "refugeZone": REFUGE_ZONE,
            "payment": {"cost": {"food": 240}},
        },
        "optionalPayments": {
            "side-3": {
                "command": "select the original damaged store",
                "cost": {"wood": 50},
            },
            "side-4": {
                "command": "select the original trader",
                "cost": {"gold": 50},
            },
        },
        "narration": {
            "introOrder": [
                "title",
                "fact-intro",
                "handover",
                "persona-intro",
                "historical-license",
                "route-help",
                "economy-help",
            ],
            "outroOrder": ["fact-outro", "persona-outro", "next-episode"],
            "speakerLabels": {
                "collection-narrator": {"en": "Chronicle", "es-ES": "Crónica"},
                "miriam-archive": {
                    "en": "Miriam of Caesarea",
                    "es-ES": "Miriam de Cesarea",
                },
            },
        },
        "gameVerified": False,
    }


def build_scenario(binding, locale):
    units = []
    for index, entity in enumerate(binding["entities"]):
        x, y = map(math.floor, entity["position"])
        units.append(
            {
                "id": f"original-{index}",
                "faction": "player" if entity["player"] == 1 else "local",
                "type": entity["unitType"],
                "position": {"x": x, "y": y},
                "essential": False,
            }
        )
    base = {
        "schemaVersion": 1,
        "scenario": {
            "id": "02-civilian-refuge-jerusalem",
            "map": {
                "width": MAP_SIZE,
                "height": MAP_SIZE,
                "baseTerrain": "grass-1",
                "tiles": [],
                "blocked": [],
                "start": {"x": 10, "y": 30},
            },
            "factions": [
                {
                    "id": "player",
                    "player": 1,
                    "civilization": "byzantines",
                    "role": "human",
                    "economy": {
                        "model": "finite-reserve",
                        "initial": {
                            "food": 350,
                            "wood": 150,
                            "gold": 85,
                            "stone": 0,
                        },
                    },
                },
                {
                    "id": "local",
                    "player": 2,
                    "civilization": "byzantines",
                    "role": "ally",
                    "economy": {
                        "model": "finite-reserve",
                        "initial": {"food": 0, "wood": 0, "gold": 0, "stone": 0},
                    },
                },
            ],
            "units": units,
            "technologies": [],
        },
    }
    scenario, native_ids, _ = FACTORY["create_native_scenario_base"](base, "1.59")
    handles = {
        binding["entities"][index]["id"]: native_ids[f"original-{index}"]
        for index in range(len(units))
    }
    result = ADAPTER["compile_household_controller"](
        scenario, handles, DOSSIER, binding, locale
    )
    return scenario, handles, result


def xs_bodies(source):
    return [(match.group(1), match.group(0)) for match in XS_FUNCTIONS.finditer(source)]


def find_xs(source, predicate, label):
    for name, body in xs_bodies(source):
        if predicate(body):
            return name, body
    raise AssertionError("no native function matched " + label)



class NativeHouseholdControllerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.binding = synthetic_binding()
        cls.dossier = copy.deepcopy(DOSSIER)
        cls.inputs_before = copy.deepcopy((cls.dossier, cls.binding))
        cls.scenario, cls.handles, cls.receipt = build_scenario(cls.binding, "en")
        cls.triggers = {
            trigger.name: trigger for trigger in cls.scenario.trigger_manager.triggers
        }
        cls.order = list(cls.triggers)
        cls.variables = cls.receipt["variables"]
        cls.xs = cls.receipt["xsSource"]
        cls.spanish, _, cls.spanish_receipt = build_scenario(cls.binding, "es-ES")
        cls.spanish_xs = cls.spanish_receipt["xsSource"]
        cls.scratch = Path(ROOT / ".cache" / "scratch")
        cls.scratch.mkdir(parents=True, exist_ok=True)
        cls.temporary = tempfile.TemporaryDirectory(
            prefix="native-household-", dir=cls.scratch
        )

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def test_fixture_is_synthetic_and_every_original_starts_outside_its_circles(self):
        self.assertTrue(self.binding["synthetic"])
        self.assertIn("nonhistorical", self.binding["syntheticNotice"])
        self.assertEqual(17, len(self.binding["entities"]))
        self.assertEqual(10, len(self.binding["zones"]))
        zones = {zone["id"]: zone for zone in self.binding["zones"]}
        by_id = {entity["id"]: entity for entity in self.binding["entities"]}
        for entity in HOUSEHOLDS:
            for zone in (COURT_ZONE, REFUGE_ZONE):
                self.assertGreater(
                    math.dist(by_id[entity]["position"], zones[zone]["centre"]),
                    zones[zone]["radius"],
                )

    def test_contract_is_accepted_for_the_authored_source_and_binding(self):
        originals, ledger, receipt = ADAPTER["validate_household_contract"](
            self.dossier, self.binding
        )
        self.assertEqual(HOUSEHOLDS, originals)
        self.assertEqual("received-households", ledger)
        self.assertEqual(f"{PREFIX}.o2.req-1.paid", receipt)

    def test_source_and_binding_are_not_mutated_by_compilation(self):
        self.assertEqual(self.inputs_before, (self.dossier, self.binding))

    def test_native_handles_are_distinct_integers_and_uid_zero_is_valid(self):
        handles = self.receipt["nativeOriginalHandles"]
        self.assertEqual(17, len(handles))
        self.assertEqual(17, len(set(handles.values())))
        self.assertEqual(0, handles[HOUSEHOLDS[0]])
        for handle in handles.values():
            self.assertIs(type(handle), int)
            self.assertGreaterEqual(handle, 0)

    def test_trigger_and_variable_construction_follows_the_authored_graph(self):
        expected = (
            ["cdf-household-initialize", "cdf-household-loss", "cdf-household-final"]
            + [f"cdf-court-arrival-{index}" for index in range(8)]
            + [f"cdf-refuge-arrival-{index}" for index in range(8)]
            + [f"cdf-court-payment-{index}" for index in range(8)]
            + [
                "cdf-court-objective-reached",
                "cdf-court-payment-goal",
                "cdf-household-final-goal",
                "cdf-declare-win",
                "cdf-declare-loss",
            ]
        )
        for name in expected:
            self.assertIn(name, self.triggers)
        for index in range(8):
            self.assertIn(f"court-arrival-{index}", self.variables)
            self.assertIn(f"refuge-arrival-{index}", self.variables)
            self.assertIn(f"held-{index}", self.variables)
        self.assertIn("court-payment", self.variables)
        self.assertIn("objective-o3", self.variables)
        for name in ("ready", "phase", "terminal"):
            self.assertIs(type(self.variables[name]), int)
            self.assertGreaterEqual(self.variables[name], 0)
        self.assertEqual(
            {
                f"{PREFIX}.o2.req-1.paid": {"variable": self.variables["court-payment"], "trueValue": 1},
                "objective-latched:o3": {"variable": self.variables["objective-o3"], "trueValue": 1},
            },
            {
                key: value
                for key, value in self.receipt["semanticFlags"].items()
                if key.startswith(PREFIX) or key.startswith("objective-latched")
            },
        )

    def test_observations_use_the_shared_original_handle_circle_predicate(self):
        for index in range(8):
            for name in (f"cdf-court-arrival-{index}", f"cdf-refuge-arrival-{index}"):
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
        self.assertIn("xsDoesUnitExist", self.xs)

    def test_o1_counts_historical_arrival_flags_with_a_survivor_floor(self):
        _, court_total = find_xs(
            self.xs,
            lambda body: "xsTriggerVariable" in body
            and "return (cdf_total >= 6);" in body
            and "xsGetUnitHitpoints" not in body,
            "the historical court arrival total",
        )
        self.assertEqual(8, court_total.count("xsTriggerVariable("))
        _, living = find_xs(
            self.xs,
            lambda body: "xsGetUnitHitpoints" not in body
            and "xsTriggerVariable" not in body
            and "return (cdf_total >= 6);" in body
            and body.count("if (") == 8,
            "the living survivor total",
        )
        self.assertIn("return (cdf_total >= 6);", living)
        reached = self.triggers["cdf-court-objective-reached"]
        conditions = {
            (c.variable, c.quantity)
            for c in reached.conditions
            if c.condition_type == ConditionId.VARIABLE_VALUE
        }
        self.assertIn((self.variables["ready"], 1), conditions)
        self.assertIn((self.variables["terminal"], 0), conditions)
        self.assertIn((self.variables["phase"], 1), conditions)
        self.assertTrue(
            any(c.condition_type == ConditionId.SCRIPT_CALL for c in reached.conditions)
        )

    def test_final_objective_is_one_guarded_invocation_that_decides_loss_first(self):
        final = self.triggers["cdf-household-final"]
        actions = [
            e
            for e in final.effects
            if e.effect_type == EffectId.SCRIPT_CALL
        ]
        self.assertEqual(1, len(actions))
        _, body = find_xs(
            self.xs,
            lambda text: "int cdf_qualified = 0;" in text and "xsSetTriggerVariable" in text,
            "the guarded final action",
        )
        loss_at = body.index("if (cdf_alive < 6)")
        qualified_at = body.index("if (cdf_qualified >= 6)")
        latch_at = body.index(f"xsSetTriggerVariable({self.variables['objective-o3']}, 1)")
        terminal_at = body.index(f"xsSetTriggerVariable({self.variables['terminal']}, 1)")
        self.assertLess(loss_at, qualified_at)
        self.assertLess(qualified_at, latch_at)
        self.assertLess(latch_at, terminal_at)
        first_write = min(
            match.start() for match in re.finditer(r"xsSetTriggerVariable", body)
        )
        for variable, expected in (
            ("ready", 1),
            ("phase", 3),
            ("court-payment", 1),
            ("terminal", 0),
        ):
            guard = (
                f"if (xsTriggerVariable({self.variables[variable]}) != {expected})"
            )
            self.assertIn(guard, body)
            self.assertLess(body.index(guard), first_write)
            self.assertLess(body.index(guard), body.index("int cdf_alive = 0;"))
        queried = re.findall(r"if \((cdf_[A-Za-z0-9_]+)\(\)\) \{", body)
        self.assertEqual(8, len(queried))
        self.assertEqual(8, len(set(queried)))
        bodies = dict(xs_bodies(self.xs))
        for name in queried:
            self.assertIn("xsGetUnitHitpoints", bodies[name])
            self.assertIn("xsGetUnitOwner", bodies[name])
            self.assertNotIn("xsGetGarrisonedInUnitId", bodies[name])
        for variable in ("ready", "phase", "court-payment", "terminal"):
            self.assertIn(
                f"xsTriggerVariable({self.variables[variable]})", body
            )
        self.assertFalse(
            any(c.condition_type == ConditionId.TIMER for c in final.conditions)
        )

    def test_defeat_closes_the_optional_circuits_before_any_late_reward(self):
        self.assertLess(
            self.order.index("cdf-household-loss"),
            self.order.index("cdf-household-final"),
        )
        self.assertLess(
            self.order.index("cdf-household-final"),
            self.order.index("cdf-side-1-complete"),
        )
        for number in range(1, 7):
            key = f"side-{number}"
            reward = self.triggers[f"cdf-{key}-complete"]
            self.assertTrue(
                any(
                    c.variable == self.variables["terminal"] and c.quantity == 0
                    for c in reward.conditions
                    if c.condition_type == ConditionId.VARIABLE_VALUE
                )
            )
            self.assertIn(f"cdf-{key}-close-1", self.triggers)
            self.assertIn(f"cdf-{key}-close-2", self.triggers)
        self.assertFalse(
            any(
                e.effect_type == EffectId.STORE_KEY_VALUE
                for trigger in self.triggers.values()
                for e in trigger.effects
            )
        )

    def test_reserves_are_fixed_and_finite_and_the_payment_is_shared_and_once(self):
        initial = self.triggers["cdf-household-initialize"]
        writes = {
            effect.variable: effect.quantity
            for effect in initial.effects
            if effect.effect_type == EffectId.CHANGE_VARIABLE
        }
        self.assertEqual(
            [550, 200, 25, 0],
            [
                writes[self.variables["optional-reserve-" + resource]]
                for resource in ("food", "wood", "gold", "stone")
            ],
        )
        receipt = self.variables["court-payment"]
        payment_name, payment = find_xs(
            self.xs,
            lambda body: f"if (xsTriggerVariable({receipt}) != 0)" in body,
            "the guarded court payment",
        )
        self.assertIn("xsSetPlayerAttribute", payment)
        self.assertIn("return (true);", payment)
        self.assertEqual(1, len(
            [
                name
                for name, body in xs_bodies(self.xs)
                if f"if (xsTriggerVariable({receipt}) != 0)" in body
            ]
        ))
        for index in range(8):
            trigger = self.triggers[f"cdf-court-payment-{index}"]
            selection = [
                c
                for c in trigger.conditions
                if c.condition_type == ConditionId.OBJECT_SELECTED
            ]
            self.assertEqual(1, len(selection))
            self.assertEqual(self.handles[HOUSEHOLDS[index]], selection[0].unit_object)
            self.assertTrue(
                any(
                    c.condition_type == ConditionId.SCRIPT_CALL
                    for c in trigger.conditions
                )
            )
            action = next(
                e.message
                for e in trigger.effects
                if e.effect_type == EffectId.SCRIPT_CALL
            )
            _, action_body = find_xs(
                self.xs,
                lambda body, want=action: body.startswith("void " + want[:-2]),
                "the payment action " + action,
            )
            self.assertIn(payment_name + "()", action_body)
            self.assertIn("xsSetTriggerVariable", action_body)
            first_write = min(
                match.start()
                for match in re.finditer(r"xsSetTriggerVariable", action_body)
            )
            for variable, expected in (
                ("ready", 1),
                ("phase", 2),
                ("terminal", 0),
            ):
                guard = (
                    f"if (xsTriggerVariable({self.variables[variable]}) != {expected})"
                )
                self.assertIn(guard, action_body)
                self.assertLess(action_body.index(guard), first_write)

    def test_victory_never_depends_on_a_type_count_or_a_clock(self):
        for name in (
            "cdf-court-objective-reached",
            "cdf-household-final",
            "cdf-declare-win",
            "cdf-declare-loss",
        ):
            trigger = self.triggers[name]
            self.assertFalse(
                any(c.condition_type == ConditionId.TIMER for c in trigger.conditions)
            )
        self.assertNotIn("xsGetUnitType", self.xs)
        self.assertNotIn("xsGetUnitCount", self.xs)
        self.assertNotIn("xsGetUnitGroup", self.xs)
        timers = [
            name
            for name, trigger in self.triggers.items()
            if any(c.condition_type == ConditionId.TIMER for c in trigger.conditions)
        ]
        self.assertTrue(timers)
        self.assertTrue(all("release" in name for name in timers), timers)

    def test_native_write_and_reopen_preserve_the_original_identities(self):
        path = Path(self.temporary.name) / "household.aoe2scenario"
        self.scenario.write_to_file(str(path))
        reopened = AoE2DEScenario.from_file(str(path))
        reopened.xs_manager.xs_check.raise_on_error = True
        reopened.xs_manager.validate_scenario_xs()
        self.assertEqual(
            SIGNATURE["native_signature"](self.scenario),
            SIGNATURE["native_signature"](reopened),
        )
        units = {
            unit.reference_id: unit.unit_const
            for unit in reopened.unit_manager.get_all_units()
        }
        for handle in self.receipt["nativeOriginalHandles"].values():
            self.assertIn(handle, units)
        self.assertEqual(
            len(self.scenario.trigger_manager.variables),
            len(reopened.trigger_manager.variables),
        )

    def test_both_locales_embed_their_own_captions(self):
        english = [
            effect.message
            for trigger in self.triggers.values()
            for effect in trigger.effects
            if effect.effect_type == EffectId.DISPLAY_INSTRUCTIONS
        ]
        spanish = [
            effect.message
            for trigger in self.spanish.trigger_manager.triggers
            for effect in trigger.effects
            if effect.effect_type == EffectId.DISPLAY_INSTRUCTIONS
        ]
        self.assertTrue(any(message.startswith("Chronicle:") for message in english))
        self.assertTrue(any(message.startswith("Miriam of Caesarea:") for message in english))
        self.assertTrue(any(message.startswith("Crónica:") for message in spanish))
        self.assertTrue(any(message.startswith("Miriam de Cesarea:") for message in spanish))
        self.assertNotEqual(english, spanish)
        self.assertFalse(self.receipt["gameVerified"])
        self.assertFalse(self.spanish_receipt["gameVerified"])

    def test_embedded_xs_static_checking_is_live(self):
        scenario = AoE2DEScenario.from_default("1.59")
        scenario.xs_manager.xs_check.raise_on_error = True
        with self.assertRaises(Exception):
            scenario.xs_manager.validate(
                xs="bool cdf_household_broken() { return (undefined_symbol); }"
            )

    def test_numeric_booleans_and_float_counts_are_not_accepted(self):
        mutations = [
            lambda d, b: d["objectivePlan"][0]["predicate"]["requirements"][0].__setitem__(
                "oncePerEntity", 1
            ),
            lambda d, b: d["objectivePlan"][2]["predicate"]["requirements"][1].__setitem__(
                "oncePerEntity", 1
            ),
            lambda d, b: d["objectivePlan"][1]["predicate"]["requirements"][0].__setitem__(
                "once", 1
            ),
            lambda d, b: d["objectivePlan"][1]["predicate"]["requirements"][0].__setitem__(
                "atomic", 1
            ),
            lambda d, b: d["objectivePlan"][1]["predicate"]["requirements"][0].__setitem__(
                "amounts", {"food": 240.0}
            ),
            lambda d, b: d["objectivePlan"][0]["predicate"]["requirements"][0].__setitem__(
                "requiredCount", 6.0
            ),
            lambda d, b: d["worldContract"]["survivorGroups"][0].__setitem__(
                "minimumAliveOrAlreadySafe", 6.0
            ),
            lambda d, b: b["households"].__setitem__("requiredCount", 6.0),
            lambda d, b: b["households"]["payment"].__setitem__("cost", {"food": 240.0}),
            lambda d, b: b["optionalPayments"]["side-3"].__setitem__(
                "cost", {"wood": 50.0}
            ),
        ]
        for mutation in mutations:
            dossier = copy.deepcopy(self.dossier)
            binding = copy.deepcopy(self.binding)
            mutation(dossier, binding)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                ADAPTER["validate_household_contract"](dossier, binding)

    def test_snapped_native_starts_cannot_collide(self):
        binding = copy.deepcopy(self.binding)
        binding["entities"][0]["position"] = [10.1, 30.1]
        binding["entities"][1]["position"] = [10.9, 30.9]
        with self.assertRaises(ValueError):
            ADAPTER["validate_household_contract"](self.dossier, binding)
        binding = copy.deepcopy(self.binding)
        binding["entities"][0]["position"] = [10.4, 30.1]
        binding["entities"][1]["position"] = [10.6, 30.9]
        with self.assertRaises(ValueError):
            ADAPTER["validate_household_contract"](self.dossier, binding)

    def test_map_size_radius_and_snapped_household_placement_are_checked(self):
        for size in (0, -64, 64.0, "64", True):
            binding = copy.deepcopy(self.binding)
            binding["map"]["size"] = size
            with self.subTest(size=size), self.assertRaises(ValueError):
                ADAPTER["validate_household_contract"](self.dossier, binding)
        binding = copy.deepcopy(self.binding)
        binding["zones"][0]["centre"] = [1.0, 1.0]
        with self.assertRaises(ValueError):
            ADAPTER["validate_household_contract"](self.dossier, binding)
        binding = copy.deepcopy(self.binding)
        binding["zones"][0]["centre"] = [63.0, 12.0]
        with self.assertRaises(ValueError):
            ADAPTER["validate_household_contract"](self.dossier, binding)
        binding = copy.deepcopy(self.binding)
        binding["zones"][0]["radius"] = 0
        with self.assertRaises(ValueError):
            ADAPTER["validate_household_contract"](self.dossier, binding)
        binding = copy.deepcopy(self.binding)
        binding["zones"][0]["radius"] = float("inf")
        with self.assertRaises(ValueError):
            ADAPTER["validate_household_contract"](self.dossier, binding)
        binding = copy.deepcopy(self.binding)
        binding["entities"][0]["position"] = [39.6, 30.1]
        with self.assertRaises(ValueError):
            ADAPTER["validate_household_contract"](self.dossier, binding)

    def test_composed_profiles_and_contract_fields_are_refused(self):
        mutations = [
            lambda d, b: d.__setitem__("designProfile", "alternative-fulfillment-v3"),
            lambda d, b: d.__setitem__("designProfile", None),
            lambda d, b: d.__setitem__("capability", None),
            lambda d, b: d.__setitem__("capabilityProfile", None),
            lambda d, b: d.__setitem__("referenceCapabilityProfile", {}),
            lambda d, b: d.__setitem__("sharedCapabilityProfile", {}),
            lambda d, b: d.__setitem__("fulfillment", {}),
            lambda d, b: d.__setitem__("fulfillmentContract", {}),
            lambda d, b: b.__setitem__("designProfile", "alternative-fulfillment-v3"),
            lambda d, b: b.__setitem__("capability", None),
            lambda d, b: b.__setitem__("capabilityProfile", None),
            lambda d, b: b.__setitem__("referenceCapabilityProfile", {}),
            lambda d, b: b.__setitem__("sharedCapabilityProfile", {}),
            lambda d, b: b.__setitem__("fulfillment", {}),
            lambda d, b: b.__setitem__("fulfillmentContract", {}),
        ]
        for mutation in mutations:
            dossier = copy.deepcopy(self.dossier)
            binding = copy.deepcopy(self.binding)
            mutation(dossier, binding)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                ADAPTER["validate_household_contract"](dossier, binding)

    def test_only_player1_civilian_villagers_may_move_and_only_the_store_is_a_house(self):
        mutations = [
            lambda d, b: b["entities"][0].__setitem__("player", 2),
            lambda d, b: b["entities"][0].__setitem__("player", True),
            lambda d, b: b["entities"][0].__setitem__("unitType", "house"),
            lambda d, b: b["entities"][0].__setitem__("unitType", "villager"),
            lambda d, b: next(
                e
                for e in b["entities"]
                if e["id"] == "02-civilian-refuge-jerusalem.side-1.entity-1"
            ).__setitem__("player", 2),
            lambda d, b: next(
                e
                for e in b["entities"]
                if e["id"] == "02-civilian-refuge-jerusalem.side-4.entity-1"
            ).__setitem__("unitType", "house"),
            lambda d, b: next(
                e
                for e in b["entities"]
                if e["id"] == "02-civilian-refuge-jerusalem.side-6.entity-2"
            ).__setitem__("player", 2),
            lambda d, b: next(
                e
                for e in b["entities"]
                if e["id"] == "02-civilian-refuge-jerusalem.side-3.entity-1"
            ).__setitem__("player", 1),
            lambda d, b: next(
                e
                for e in b["entities"]
                if e["id"] == "02-civilian-refuge-jerusalem.side-3.entity-1"
            ).__setitem__("unitType", "villager-male"),
        ]
        for mutation in mutations:
            dossier = copy.deepcopy(self.dossier)
            binding = copy.deepcopy(self.binding)
            mutation(dossier, binding)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                ADAPTER["validate_household_contract"](dossier, binding)

    def test_labels_must_be_nonempty_localized_strings(self):
        mutations = [
            lambda d, b: b["entities"][0]["label"].__setitem__("en", ""),
            lambda d, b: b["entities"][0]["label"].__setitem__("en", "   "),
            lambda d, b: b["entities"][0]["label"].__setitem__("es-ES", None),
            lambda d, b: b["entities"][0]["label"].pop("es-ES"),
            lambda d, b: b["zones"][0]["label"].__setitem__("en", ""),
            lambda d, b: b["zones"][0]["label"].__setitem__("es-ES", None),
        ]
        for mutation in mutations:
            dossier = copy.deepcopy(self.dossier)
            binding = copy.deepcopy(self.binding)
            mutation(dossier, binding)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                ADAPTER["validate_household_contract"](dossier, binding)

    def test_intro_and_outro_orders_are_fixed_and_factual_before_persona(self):
        mutations = [
            lambda d, b: b["narration"].__setitem__(
                "introOrder", ["persona-intro", "fact-intro"]
            ),
            lambda d, b: b["narration"].__setitem__(
                "introOrder",
                [
                    "title",
                    "handover",
                    "fact-intro",
                    "persona-intro",
                    "historical-license",
                    "route-help",
                    "economy-help",
                ],
            ),
            lambda d, b: b["narration"]["introOrder"].pop(),
            lambda d, b: b["narration"].__setitem__(
                "outroOrder", ["persona-outro", "fact-outro", "next-episode"]
            ),
            lambda d, b: b["narration"]["outroOrder"].pop(),
        ]
        for mutation in mutations:
            dossier = copy.deepcopy(self.dossier)
            binding = copy.deepcopy(self.binding)
            mutation(dossier, binding)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                ADAPTER["validate_household_contract"](dossier, binding)

    def test_optional_placement_is_checked_at_the_native_snapped_start(self):
        binding = copy.deepcopy(self.binding)
        entity = next(
            item
            for item in binding["entities"]
            if item["id"] == "02-civilian-refuge-jerusalem.side-1.entity-1"
        )
        zone = next(
            item
            for item in binding["zones"]
            if item["id"] == "02-civilian-refuge-jerusalem.side-1.zone-1"
        )
        entity["position"] = [32.99, 30.99]
        zone["centre"] = [30.0, 30.0]
        self.assertGreater(
            math.dist(entity["position"], zone["centre"]), zone["radius"]
        )
        with self.assertRaises(ValueError):
            ADAPTER["validate_household_contract"](self.dossier, binding)
        self.assertEqual([32.99, 30.99], entity["position"])
        ADAPTER["validate_household_contract"](self.dossier, self.binding)

    def test_corridor_geometry_must_be_authored_and_usable(self):
        def corridor(binding, index=1):
            return binding["map"]["corridors"][index]

        mutations = [
            lambda d, b: corridor(b).__setitem__("points", []),
            lambda d, b: corridor(b).__setitem__("points", [[12.0, 31.0]]),
            lambda d, b: corridor(b).__setitem__(
                "points", [[12.0, 31.0], [12.0, 31.0], [12.0, 31.0]]
            ),
            lambda d, b: corridor(b).__setitem__(
                "points", [[12.0, 31.0], [float("nan"), 31.0]]
            ),
            lambda d, b: corridor(b).__setitem__(
                "points", [[12.0, 31.0], [float("inf"), 31.0]]
            ),
            lambda d, b: corridor(b).__setitem__(
                "points", [[12.0, 31.0], [200.0, 31.0]]
            ),
            lambda d, b: corridor(b).__setitem__(
                "points", [[12.0, 31.0], "north-road"]
            ),
            lambda d, b: corridor(b).__setitem__("points", [[12.0, 31.0], [12.0]]),
            lambda d, b: corridor(b).__setitem__("points", None),
            lambda d, b: corridor(b).__setitem__("widthTiles", 0),
            lambda d, b: corridor(b).__setitem__("widthTiles", -4),
            lambda d, b: corridor(b).__setitem__("widthTiles", "4"),
            lambda d, b: corridor(b).__setitem__("widthTiles", float("inf")),
            lambda d, b: b["map"]["corridors"].append(
                dict(corridor(b, 0), id="main")
            ),
            lambda d, b: b["map"]["corridors"].__setitem__(0, dict(corridor(b, 0), id="")),
        ]
        for mutation in mutations:
            dossier = copy.deepcopy(self.dossier)
            binding = copy.deepcopy(self.binding)
            mutation(dossier, binding)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                ADAPTER["validate_household_contract"](dossier, binding)
        ADAPTER["validate_household_contract"](self.dossier, self.binding)

    def test_unsupported_contracts_are_rejected_before_any_native_change(self):
        mutations = [
            lambda d, b: d["objectivePlan"][2]["predicate"]["requirements"].append(
                copy.deepcopy(d["objectivePlan"][2]["predicate"]["requirements"][1])
            ),
            lambda d, b: d["objectivePlan"][2]["predicate"]["requirements"][0][
                "eligibleEntitiesFromLedger"
            ].__setitem__("ledger", "other-ledger"),
            lambda d, b: d["objectivePlan"][1]["predicate"]["requirements"][0].__setitem__(
                "paidFlag", "other-receipt"
            ),
            lambda d, b: d["objectivePlan"][0]["predicate"]["requirements"][0].__setitem__(
                "requiredCount", 5
            ),
            lambda d, b: d["objectivePlan"][0]["predicate"].__setitem__("operator", "any"),
            lambda d, b: d["objectivePlan"][0].__setitem__("after", ["o2"]),
            lambda d, b: d["objectivePlan"][1].__setitem__("phase", "phase-3"),
            lambda d, b: d["objectivePlan"][0]["predicate"].__setitem__(
                "neverUseTimerInstead", False
            ),
            lambda d, b: d["stateMachine"].__setitem__("campaignProgressWrite", True),
            lambda d, b: d["stateMachine"]["phaseTransitions"].__setitem__(
                3, {"from": "phase-3", "to": "victory", "on": "objective-latched"}
            ),
            lambda d, b: d["stateMachine"].__setitem__("terminalPriority", "victory first"),
            lambda d, b: d["worldContract"]["survivorGroups"][0].__setitem__(
                "minimumAliveOrAlreadySafe", 5
            ),
            lambda d, b: d["worldContract"]["survivorGroups"].append(
                copy.deepcopy(d["worldContract"]["survivorGroups"][0])
            ),
            lambda d, b: d["worldContract"]["entities"].__setitem__(
                0, dict(d["worldContract"]["entities"][0], id="other-household")
            ),
            lambda d, b: b["households"].__setitem__("requiredCount", 7),
            lambda d, b: b["households"].__setitem__("courtZone", f"{PREFIX}.destination-1"),
            lambda d, b: b["households"].__setitem__("refugeZone", COURT_ZONE),
            lambda d, b: b["households"].__setitem__("entities", HOUSEHOLDS[:7]),
            lambda d, b: b["households"]["payment"].__setitem__("cost", {"food": 300}),
            lambda d, b: b.__setitem__("kind", "private-historical-episode-native-binding"),
            lambda d, b: b.__setitem__("schemaVersion", 2),
            lambda d, b: b["optionalPayments"]["side-3"].__setitem__(
                "cost", {"wood": 40}
            ),
            lambda d, b: b["map"].__setitem__("corridors", []),
            lambda d, b: b["narration"]["speakerLabels"].pop("miriam-archive"),
            lambda d, b: b["narration"].__setitem__("outroOrder", ["not-a-screen"]),
            lambda d, b: b["entities"].pop(),
            lambda d, b: b["entities"].__setitem__(
                1, dict(b["entities"][1], id=b["entities"][0]["id"])
            ),
            lambda d, b: b["entities"][0].__setitem__("position", [999.0, 30.0]),
            lambda d, b: b["entities"][0].__setitem__("position", [float("nan"), 30.0]),
            lambda d, b: b["entities"][0].__setitem__("position", [40.0, 30.0]),
            lambda d, b: b["entities"][0].__setitem__("player", 3),
            lambda d, b: b["zones"][0].__setitem__("radius", 0),
        ]
        for mutation in mutations:
            dossier = copy.deepcopy(self.dossier)
            binding = copy.deepcopy(self.binding)
            mutation(dossier, binding)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                ADAPTER["validate_household_contract"](dossier, binding)

    def test_native_handles_must_be_distinct_nonnegative_integers(self):
        duplicates = dict(self.handles)
        duplicates[HOUSEHOLDS[1]] = duplicates[HOUSEHOLDS[0]]
        with self.assertRaises(ValueError):
            ADAPTER["_validate_native_handles"](duplicates, self.binding)
        boolean = dict(self.handles)
        boolean[HOUSEHOLDS[0]] = True
        with self.assertRaises(ValueError):
            ADAPTER["_validate_native_handles"](boolean, self.binding)
        negative = dict(self.handles)
        negative[HOUSEHOLDS[0]] = -1
        with self.assertRaises(ValueError):
            ADAPTER["_validate_native_handles"](negative, self.binding)
        missing = dict(self.handles)
        missing.pop(HOUSEHOLDS[0])
        with self.assertRaises(ValueError):
            ADAPTER["_validate_native_handles"](missing, self.binding)
        extra = dict(self.handles)
        extra["not-an-original"] = 9999
        with self.assertRaises(ValueError):
            ADAPTER["_validate_native_handles"](extra, self.binding)
        with self.assertRaises(ValueError):
            ADAPTER["compile_household_controller"](
                self.scenario, self.handles, self.dossier, self.binding, "fr"
            )

    def test_payment_surface_accepts_only_living_originals_inside_the_court(self):
        selected = []
        for index in range(8):
            trigger = self.triggers[f"cdf-court-payment-{index}"]
            selection = next(
                c
                for c in trigger.conditions
                if c.condition_type == ConditionId.OBJECT_SELECTED
            )
            selected.append(selection.unit_object)
            circles = [
                c
                for c in trigger.conditions
                if c.condition_type == ConditionId.SCRIPT_CALL
                and "xsGetGarrisonedInUnitId"
                in dict(xs_bodies(self.xs)).get(c.xs_function, "")
            ]
            self.assertEqual(1, len(circles))
            circle = dict(xs_bodies(self.xs))[circles[0].xs_function]
            self.assertIn("xsGetUnitHitpoints", circle)
            self.assertIn("xsGetUnitOwner", circle)
            self.assertIn("xsGetGarrisonedInUnitId", circle)
            self.assertIn("cdf_dx * cdf_dx + cdf_dy * cdf_dy", circle)
        self.assertEqual(
            sorted(self.handles[entity] for entity in HOUSEHOLDS), sorted(selected)
        )
        optional = [
            handle
            for entity, handle in self.handles.items()
            if entity not in HOUSEHOLDS
        ]
        self.assertFalse(set(optional) & set(selected))
        receipt = self.variables["court-payment"]
        _, payment = find_xs(
            self.xs,
            lambda body: f"if (xsTriggerVariable({receipt}) != 0)" in body,
            "the guarded court payment",
        )
        self.assertLess(
            payment.index("xsPlayerAttribute"), payment.index("xsSetPlayerAttribute")
        )
        self.assertIn("xsSetTriggerVariable", payment)


if __name__ == "__main__":
    unittest.main()
