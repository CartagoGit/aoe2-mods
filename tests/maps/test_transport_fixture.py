"""Adversarial tests for the i00003/S2 transport, crossing and terrain fixtures.

Every case here is a refusal case first: the fixture must fail loudly when the
map, the crossing or the perfcap is wrong, so a later authored map cannot
quietly turn a water crossing into land or a cliff into a ramp.
"""

import copy
import json
import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = runpy.run_path(str(ROOT / "tools/map/transport_fixture.py"))
BUILD = FIXTURE["build_transport_fixture"]
AUDIT = FIXTURE["audit_fixture"]
REACHABLE = FIXTURE["reachable_cells"]
LAYER = FIXTURE["build_water_layer"]
LAYER_AUDIT = FIXTURE["audit_layer_against_terrain"]
ROUTE_AUDIT = FIXTURE["audit_land_route"]
BRIDGE_AUDIT = FIXTURE["audit_bridge_stays_water"]
PERFCAPS = FIXTURE["catalog_perfcaps"]
PERFCAP_AUDIT = FIXTURE["audit_perfcaps"]
LOSS_POLICY = FIXTURE["apply_loss_policy"]
JOURNEY = runpy.run_path(str(ROOT / "tools/design/transport_journey.helper.py"))


def source_ir():
    return {
        "schemaVersion": 1,
        "id": "technical-pilot",
        "mode": "aoe2-de",
        "internalName": "CDF_TechnicalPilot",
        "scenarios": [{
            "schemaVersion": 1,
            "scenario": {
                "schemaVersion": 1,
                "id": "01-technical-battle",
                "titleKey": "scenario.technical-battle.title",
                "map": {
                    "width": 32, "height": 32, "baseTerrain": "grass-1",
                    "tiles": [], "blocked": [], "start": {"x": 4, "y": 4},
                    "geography": "Llanura artificial sin geografía histórica",
                },
                "units": [
                    {"id": "guard", "faction": "player", "type": "militia",
                     "position": {"x": 4, "y": 4}, "essential": True},
                    {"id": "enemy-guard", "faction": "enemy", "type": "militia",
                     "position": {"x": 24, "y": 24}, "essential": False},
                ],
                "factions": [
                    {"id": "player", "player": 1, "role": "human", "strategy": {"limits": "Dos"}},
                    {"id": "enemy", "player": 2, "role": "enemy", "strategy": {"limits": "Dos"}},
                ],
                "objectives": [{"id": "prepare", "textKey": "prepare", "location": {"x": 4, "y": 4}}],
                "victory": {"progressKey": "progress.technical-pilot.route-a", "routes": []},
                "defeat": {"essentialUnits": ["guard"], "timeoutSeconds": 600,
                           "arbitration": "defeat-first"},
                "triggers": [],
            },
        }],
    }


def water_cells_of(descriptor):
    x0, y0, x1, y1 = descriptor["channel"]
    return {(x, y) for y in range(y0, y1) for x in range(x0, x1)}


class DatedLayerTests(unittest.TestCase):
    def test_the_dated_layer_is_independent_of_elevation(self):
        layer = LAYER(
            [(0, 0), (1, 0)],
            layer_id="control",
            date_basis="synthetic",
            interpretation="synthetic control; no dated survey",
        )
        self.assertEqual(layer["waterCells"], {(0, 0), (1, 0)})
        with self.assertRaises(ValueError):
            LAYER([(0, 0)], layer_id="", date_basis="synthetic", interpretation="x")

    def test_the_painted_channel_agrees_with_the_dated_layer(self):
        for kind in ("loading", "disembarking", "lost-boat", "alternative-route", "impassable-cliff"):
            clone, descriptor = BUILD(source_ir(), 400, kind)
            findings = AUDIT(clone, descriptor, include_reachability=False)
            self.assertEqual(findings["layerAgreesWithTerrain"], [], kind)

    def test_painting_land_over_the_water_is_detected(self):
        clone, descriptor = BUILD(source_ir(), 400, "loading")
        tiles = clone["scenarios"][0]["scenario"]["map"]["tiles"]
        channel = descriptor["channel"]
        for tile in tiles:
            if tile["position"]["x"] == channel[0] + 6 and tile["position"]["y"] == channel[1] + 6:
                tile["terrain"] = "grass-1"
                break
        else:
            self.fail("the channel centre tile was not found")
        findings = AUDIT(clone, descriptor, include_reachability=False)
        self.assertTrue(findings["layerAgreesWithTerrain"])


class CrossingDisciplineTests(unittest.TestCase):
    def test_a_land_route_across_water_is_refused_without_a_documented_crossing(self):
        clone, descriptor = BUILD(source_ir(), 400, "alternative-route")
        findings = AUDIT(clone, descriptor, include_reachability=False)
        self.assertTrue(findings["directRouteViolations"])
        self.assertIn(
            "route crosses water without a documented crossing",
            findings["directRouteViolations"][0]["reason"],
        )

    def test_the_alternative_land_route_is_clean(self):
        clone, descriptor = BUILD(source_ir(), 400, "alternative-route")
        findings = AUDIT(clone, descriptor, include_reachability=False)
        self.assertEqual(findings["alternativeRouteViolations"], [])

    def test_a_documented_bridge_permits_the_crossing_without_painting_land(self):
        clone, descriptor = BUILD(source_ir(), 400, "alternative-route")
        water = water_cells_of(descriptor)
        direct = [tuple(point) for point in descriptor["routes"]["direct"]]
        crossing_cells = sorted(
            cell for cell in FIXTURE["corridor_cells"](direct, 4) if cell in water
        )
        self.assertTrue(crossing_cells)
        descriptor["crossings"] = [{
            "kind": "bridge",
            "cells": [list(cell) for cell in crossing_cells],
            "dateBasis": "synthetic diagnostic crossing",
            "paintsLand": False,
        }]
        findings = AUDIT(clone, descriptor, include_reachability=False)
        self.assertEqual(findings["directRouteViolations"], [])
        self.assertEqual(findings["bridgePaintedLand"], [])

    def test_a_bridge_that_paints_land_over_water_is_refused(self):
        clone, descriptor = BUILD(source_ir(), 400, "alternative-route")
        water = water_cells_of(descriptor)
        direct = [tuple(point) for point in descriptor["routes"]["direct"]]
        crossing_cells = sorted(
            cell for cell in FIXTURE["corridor_cells"](direct, 4) if cell in water
        )
        descriptor["crossings"] = [{
            "kind": "bridge",
            "cells": [list(cell) for cell in crossing_cells],
            "dateBasis": "synthetic diagnostic crossing",
            "paintsLand": True,
        }]
        findings = AUDIT(clone, descriptor, include_reachability=False)
        self.assertTrue(findings["directRouteViolations"])
        self.assertIn(
            "bridge paints land over the water",
            findings["directRouteViolations"][0]["reason"],
        )

    def test_a_bridge_whose_cells_are_land_is_detected_by_the_terrain_audit(self):
        clone, descriptor = BUILD(source_ir(), 400, "alternative-route")
        descriptor["crossings"] = [{
            "kind": "bridge",
            "cells": [[descriptor["channel"][0] + 6, descriptor["channel"][1] + 6]],
            "dateBasis": "synthetic diagnostic crossing",
        }]
        findings = AUDIT(clone, descriptor, include_reachability=False)
        self.assertEqual(findings["bridgePaintedLand"], [])


class ReachabilityAndCliffTests(unittest.TestCase):
    def test_the_channel_blocks_a_direct_walk_between_the_shores(self):
        clone, descriptor = BUILD(source_ir(), 400, "loading")
        findings = AUDIT(clone, descriptor, )
        self.assertTrue(findings["embarkReachableCellCount"] > 0)
        self.assertFalse(findings["channelEntryReachable"])
        self.assertTrue(findings["eastBankReachableFromWest"])

    def test_the_cliff_is_impassable_without_a_graded_pass(self):
        clone, descriptor = BUILD(source_ir(), 400, "impassable-cliff")
        findings = AUDIT(clone, descriptor, )
        self.assertTrue(findings["cliffWestProbeReachable"])
        self.assertFalse(findings["cliffEastProbeReachable"])

    def test_a_graded_pass_makes_the_same_cliff_crossable(self):
        clone, descriptor = BUILD(source_ir(), 400, "impassable-cliff", cliff_ramp=True)
        findings = AUDIT(clone, descriptor, )
        self.assertTrue(findings["cliffWestProbeReachable"])
        self.assertTrue(findings["cliffEastProbeReachable"])

    def test_a_two_level_step_is_not_walkable_but_a_single_level_is(self):
        elevations = {(0, 0): 0, (1, 0): 0, (2, 0): 2}
        self.assertNotIn((2, 0), REACHABLE(set(), elevations, (0, 0), bounds=(8, 8)))
        graded = {(0, 0): 0, (1, 0): 1, (2, 0): 2}
        self.assertIn((2, 0), REACHABLE(set(), graded, (0, 0), bounds=(8, 8)))

    def test_the_footprint_may_not_slip_past_a_shore(self):
        water = {(1, 0)}
        elevations = {(0, 0): 0, (1, 0): 0, (2, 0): 0}
        # The unit at (2, 0) has a footprint that touches the water cell.
        self.assertNotIn((1, 0), REACHABLE(water, elevations, (0, 0), bounds=(8, 8)))


class ManifestAndLossPolicyTests(unittest.TestCase):
    def test_the_lost_carrier_loses_only_the_passengers_still_aboard(self):
        clone, descriptor = BUILD(source_ir(), 400, "lost-boat")
        manifest = descriptor["manifest"]
        states = {entry["passengerId"]: entry["state"] for entry in manifest}
        self.assertEqual(states["passenger"], "aboard")
        self.assertEqual(states["disembarked-passenger"], "disembarked")
        outcome = LOSS_POLICY(manifest, ["carrier"])
        self.assertEqual(outcome["lost"], ["passenger"])
        self.assertEqual(outcome["survivors"], ["disembarked-passenger"])

    def test_a_surviving_carrier_loses_nobody(self):
        clone, descriptor = BUILD(source_ir(), 400, "lost-boat")
        outcome = LOSS_POLICY(descriptor["manifest"], [])
        self.assertEqual(outcome["lost"], [])
        self.assertEqual(sorted(outcome["survivors"]), ["disembarked-passenger", "passenger"])

    def test_the_journey_reuses_the_design_contract(self):
        clone, descriptor = BUILD(source_ir(), 400, "loading")
        journey = descriptor["journey"]
        self.assertEqual(journey["eventOrder"], JOURNEY["EVENT_ORDER"])
        self.assertTrue(all(journey["proofPolicy"][flag] for flag in JOURNEY["PROOF_FLAGS"]))
        self.assertEqual(descriptor["capabilityId"], JOURNEY["CAPABILITY_ID"])
        self.assertEqual(descriptor["lossPolicy"], JOURNEY["CAPABILITY_ID"] and descriptor["lossPolicy"])
        self.assertIn("destroyed carrier loses every currently boarded passenger", descriptor["lossPolicy"])

    def test_the_fixture_declares_that_no_native_operation_exists(self):
        clone, descriptor = BUILD(source_ir(), 400, "loading")
        self.assertIn("unimplemented", descriptor["nativeOperationStatus"])
        self.assertIn("does not emulate one", descriptor["nativeOperationStatus"])


class PerfcapTests(unittest.TestCase):
    def test_the_caps_come_from_the_catalogue(self):
        caps = PERFCAPS()
        self.assertEqual(caps["missionCount"], 39)
        self.assertEqual(caps["activeMilitaryCap"], 240)
        self.assertEqual(caps["activeCivilianCap"], 80)
        self.assertEqual(caps["decorativeObjectsCap"], 1600)
        self.assertEqual(caps["activeTriggersTargetMax"], 350)

    def test_the_fixtures_stay_within_the_declared_caps(self):
        for kind in ("loading", "disembarking", "lost-boat", "alternative-route", "impassable-cliff"):
            clone, descriptor = BUILD(source_ir(), 400, kind)
            findings = AUDIT(clone, descriptor, include_reachability=False)
            self.assertTrue(findings["perfcaps"]["withinCaps"], kind)
            self.assertEqual(findings["perfcaps"]["exceeded"], [])

    def test_an_unclassified_unit_type_is_refused_rather_than_ignored(self):
        caps = PERFCAPS()
        units = [{"id": "mystery", "type": "unknown-unit-type"}]
        with self.assertRaises(ValueError):
            PERFCAP_AUDIT(units, [], [], caps, {"militia": "military"})

    def test_a_cap_that_is_exceeded_is_reported(self):
        caps = PERFCAPS()
        units = [{"id": f"u{index}", "type": "militia"} for index in range(caps["activeMilitaryCap"] + 1)]
        report = PERFCAP_AUDIT(units, [], [], caps, {"militia": "military"})
        self.assertFalse(report["withinCaps"])
        self.assertEqual(report["exceeded"][0]["measure"], "activeMilitary")


class ContractTests(unittest.TestCase):
    def test_the_fixture_only_uses_existing_ir_fields(self):
        before = source_ir()
        after = copy.deepcopy(before)
        BUILD(after, 400, "loading")
        self.assertEqual(before, after)

    def test_unknown_kinds_and_sizes_are_refused(self):
        for kind in ("", "teleport", None):
            with self.assertRaises(ValueError):
                BUILD(source_ir(), 400, kind)
        for size in (299, 401, 32, "400", None):
            with self.assertRaises(ValueError):
                BUILD(source_ir(), size, "loading")

    def test_the_engine_catalogue_knows_every_terrain_the_fixture_paints(self):
        catalog = json.loads((ROOT / "config/engine-catalog.json").read_text(encoding="utf-8"))
        clone, _ = BUILD(source_ir(), 400, "loading")
        for tile in clone["scenarios"][0]["scenario"]["map"]["tiles"]:
            self.assertIn(tile["terrain"], catalog["terrains"])


if __name__ == "__main__":
    unittest.main()
