"""Adversarial tests for the native height quantiser.

The quantiser implements the architect's candidate band table and nothing more,
so every case here checks that it stays a candidate: absolute bands, no
quantile remapping, no water claim, no cliff applied silently, no unknown
ground flattened and no relocation decided.
"""

import json
import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
QUANTISER = runpy.run_path(str(ROOT / "tools/map/terrain_quantiser.py"))
BAND = QUANTISER["band_for_height"]
QUANTISE = QUANTISER["quantise_height_candidate"]
CLIFFS = QUANTISER["cliff_edges"]
RAMPS = QUANTISER["candidate_ramps"]


def candidate(rows, **extra):
    size = len(rows)
    payload = {
        "schemaVersion": 1,
        "kind": "geographic-height-raster-candidate",
        "heightUnit": "metre",
        "mapSize": size,
        "requestedBBox": [0.0, 0.0, 1.0, 1.0],
        "orientation": "north-up, x eastward, y southward",
        "projection": "cosine-corrected design projection",
        "resampling": "bilinear on source sample centers",
        "sourceClassification": "modern-dsm",
        "verticalDatum": "EGM 2008",
        "rangeMetres": [min(v for row in rows for v in row if v is not None),
                        max(v for row in rows for v in row if v is not None)],
        "elevationRowsMetres": rows,
    }
    payload.update(extra)
    return payload


class BandTests(unittest.TestCase):
    def test_the_architect_candidate_bands_are_applied_verbatim(self):
        self.assertEqual(BAND(0), 0)
        self.assertEqual(BAND(69.999), 0)
        self.assertEqual(BAND(70), 1)
        self.assertEqual(BAND(99.999), 1)
        self.assertEqual(BAND(100), 2)
        self.assertEqual(BAND(129.999), 2)
        self.assertEqual(BAND(130), 3)
        self.assertEqual(BAND(159.999), 3)
        self.assertEqual(BAND(160), 4)
        self.assertEqual(BAND(189.999), 4)
        self.assertEqual(BAND(190), 5)
        self.assertEqual(BAND(219.999), 5)
        self.assertEqual(BAND(220), 6)
        self.assertEqual(BAND(249.999), 6)
        self.assertEqual(BAND(250), 7)
        self.assertEqual(BAND(9000), 7)

    def test_an_unknown_sample_stays_unknown(self):
        self.assertIsNone(BAND(None))

    def test_the_bands_are_absolute_not_quantiles(self):
        # Two districts with the same height get the same level, and a low
        # district is never stretched to fill the range.
        low = candidate([[10.0, 20.0], [30.0, 40.0]])
        high = candidate([[200.0, 210.0], [220.0, 230.0]])
        low_levels = QUANTISE(low)["levelRows"]
        high_levels = QUANTISE(high)["levelRows"]
        self.assertEqual(low_levels[0][0], 0)
        self.assertEqual(high_levels[0][0], 5)
        # 10-40 m all sit in the lowest band; 200-230 m split across two bands
        # exactly as the absolute thresholds say, never stretched to 0..7.
        self.assertEqual(QUANTISE(low)["levelHistogram"]["0"], 4)
        self.assertEqual(QUANTISE(high)["levelHistogram"]["5"], 2)
        self.assertEqual(QUANTISE(high)["levelHistogram"]["6"], 2)
        self.assertEqual(QUANTISE(high)["levelHistogram"]["0"], 0)


class CandidateTests(unittest.TestCase):
    def test_the_result_is_a_candidate_and_not_terrain(self):
        result = QUANTISE(candidate([[10.0, 20.0], [30.0, 40.0]]))
        self.assertFalse(result["nativeTerrainWritten"])
        self.assertFalse(result["gameVerified"])
        self.assertFalse(result["flatteningApplied"])
        self.assertFalse(result["relocationApplied"])
        self.assertIn("architect candidate", result["bandStatus"])

    def test_level_zero_is_never_claimed_to_be_water(self):
        result = QUANTISE(candidate([[10.0, 20.0], [30.0, 40.0]]))
        # The only water word in the whole result is the status that says the
        # quantiser makes no water claim at all.
        water_keys = [key for key in result if "water" in key.lower()]
        self.assertEqual(water_keys, ["waterStatus"])
        self.assertIn("native height 0 is not water", result["waterStatus"].lower())

    def test_nodata_is_preserved_and_never_flattened(self):
        result = QUANTISE(candidate([[10.0, None], [30.0, 40.0]]))
        self.assertEqual(result["nodataCells"], 1)
        self.assertTrue(result["unknownCellsPreserved"])
        self.assertIsNone(result["levelRows"][0][1])

    def test_a_ragged_or_wrong_sized_raster_is_refused(self):
        with self.assertRaises(ValueError):
            QUANTISE(candidate([[10.0, 20.0], [30.0]]))
        with self.assertRaises(ValueError):
            QUANTISE(candidate([[10.0, 20.0]]))
        with self.assertRaises(ValueError):
            QUANTISE({"kind": "something-else"})

    def test_a_candidate_without_explicit_metre_units_is_refused(self):
        payload = candidate([[10.0, 20.0], [30.0, 40.0]])
        payload["heightUnit"] = "feet"
        with self.assertRaises(ValueError):
            QUANTISE(payload)


class CliffTests(unittest.TestCase):
    def test_a_one_level_step_is_not_a_cliff(self):
        levels = [[0, 1], [0, 0]]
        self.assertEqual(CLIFFS(levels, 2), [])

    def test_a_two_level_jump_is_reported_as_a_cliff_candidate(self):
        levels = [[0, 2], [0, 0]]
        edges = CLIFFS(levels, 2)
        # The jump is reported on both of its sides, so the report never hides
        # a cliff behind a single boundary.
        self.assertEqual(len(edges), 2)
        self.assertEqual(sorted(edge["delta"] for edge in edges), [-2, 2])
        self.assertEqual(
            sorted((edge["levelFrom"], edge["levelTo"]) for edge in edges),
            [(0, 2), (2, 0)],
        )

    def test_a_cliff_is_not_applied_but_only_proposed(self):
        rows = [[10.0, 10.0, 10.0], [10.0, 10.0, 260.0], [10.0, 10.0, 10.0]]
        result = QUANTISE(candidate(rows))
        self.assertGreaterEqual(result["cliffEdgeCount"], 1)
        self.assertGreaterEqual(result["rampCandidateCount"], 1)
        # The published levels keep the honest band; the ramp is a candidate.
        self.assertEqual(result["levelRows"][1][2], 7)
        for ramp in result["rampCandidates"]:
            self.assertIn("not applied", ramp["status"])
            for step in ramp["cells"]:
                self.assertIsNotNone(step["toLevel"])

    def test_the_ramp_candidate_descends_one_level_at_a_time(self):
        levels = [[7, 7, 7], [0, 0, 0], [0, 0, 0]]
        edges = CLIFFS(levels, 3)
        ramps = RAMPS(levels, 3, edges)
        self.assertTrue(ramps)
        for ramp in ramps:
            levels_seen = [step["toLevel"] for step in ramp["cells"]]
            for before, after in zip(levels_seen, levels_seen[1:]):
                self.assertLessEqual(abs(before - after), 1)

    def test_a_flat_raster_has_no_cliff_and_no_ramp(self):
        result = QUANTISE(candidate([[10.0, 10.0, 10.0], [10.0, 10.0, 10.0], [10.0, 10.0, 10.0]]))
        self.assertEqual(result["cliffEdgeCount"], 0)
        self.assertEqual(result["rampCandidateCount"], 0)


if __name__ == "__main__":
    unittest.main()
