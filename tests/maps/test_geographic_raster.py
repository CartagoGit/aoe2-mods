"""Synthetic geometry assertions and a real DSM sample smoke test, never AoE2 QA."""

import copy
import hashlib
import json
import runpy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COMPILER = runpy.run_path(str(ROOT / "tools/map/geographic_raster.compiler.py"))
EXTENT = runpy.run_path(str(ROOT / "tools/map/geographic_extent_audit.script.py"))
FRAME = runpy.run_path(str(ROOT / "tools/map/geographic_frame.helper.py"))
SCRIPT = ROOT / "tools/map/geographic_raster.script.py"
REAL_GRID = ROOT / "tests/maps/fixtures/edirne-dsm-sample-grid.json"
BBOX = [10.08, 50.82, 10.20, 50.94]
REAL_BBOX = [26.5603, 41.66975, 26.5608, 41.67025]


def plane():
    return {"schemaVersion": 1, "sourceClassification": "synthetic-test",
            "horizontalCrs": "EPSG:4326", "heightUnit": "metre", "verticalDatum": "synthetic metre datum",
            "sampleOriginLonLat": [10, 51], "stepDegrees": [0.1, -0.1],
            "rows": [[100 + row * 10 + column * 2 for column in range(4)] for row in range(4)]}


class GeographicRasterTests(unittest.TestCase):
    def test_existing_projection_inverse_and_outer_cell_bounds(self):
        for size in (300, 400):
            frame = FRAME["make_frame"](BBOX, size)
            for point in ((0, 0), (size - 1, size - 1), (size / 2, 80)):
                self.assertEqual(frame.tile_at(frame.lon_lat_at(*point)), list(point))
            centres, cells = frame.bounds_at(0, size - 1), frame.bounds_at(-0.5, size - 0.5)
            self.assertLess(cells[0], centres[0])
            self.assertGreater(cells[3], centres[3])
            self.assertGreater(frame.lon_lat_at(1, 0)[0], frame.lon_lat_at(0, 0)[0])
            self.assertLess(frame.lon_lat_at(0, 1)[1], frame.lon_lat_at(0, 0)[1])

    def test_bilinear_plane_and_orientation(self):
        candidate = COMPILER["compile_height_candidate"](plane(), BBOX, 300)
        frame = FRAME["make_frame"](BBOX, 300)
        for x, y in ((0, 0), (299, 299), (123, 78), (1, 299)):
            lon, lat = frame.lon_lat_at(x, y)
            expected = 100 + (51 - lat) * 100 + (lon - 10) * 20
            self.assertAlmostEqual(candidate["elevationRowsMetres"][y][x], expected, places=6)
        self.assertTrue(candidate["completeSampleCoverage"])
        self.assertFalse(candidate["nativeTerrainWritten"])
        self.assertFalse(candidate["gameVerified"])

    def test_missing_coverage_and_nodata_cannot_be_filled(self):
        source = plane()
        source["rows"][1][1] = None
        self.assertEqual(COMPILER["sample_bilinear"](source, [10, 51]), (100.0, None))
        self.assertEqual(COMPILER["sample_bilinear"](source, [10.05, 50.95])[1], "source-nodata")
        interior = plane()
        interior["rows"][0][1] = None
        self.assertEqual(COMPILER["sample_bilinear"](interior, [10.1, 50.9]), (112.0, None))
        with self.assertRaisesRegex(ValueError, "Incomplete sample coverage"):
            COMPILER["compile_height_candidate"](source, BBOX, 300)
        # Authored rectangle fits the source, but its square padding does not.
        padded = COMPILER["compile_height_candidate"](plane(), [10, 50.7, 10.3, 51], 300, True)
        self.assertFalse(padded["completeSampleCoverage"])
        self.assertGreater(padded["missingSamples"]["outside-source-sample-centers"], 0)
        self.assertIsNone(padded["elevationRowsMetres"][0][0])

    def test_invalid_frames_and_sample_grids_are_rejected(self):
        for size in (299, 401, True):
            with self.subTest(size=size), self.assertRaises(ValueError):
                FRAME["make_frame"](BBOX, size)
        for bounds in ([11, 50, 10, 51], [179, 80, -179, 81], [0, 89, 1, 90]):
            with self.subTest(bounds=bounds), self.assertRaises(ValueError):
                FRAME["make_frame"](bounds, 300)
        for key, value in (("horizontalCrs", "EPSG:3857"), ("schemaVersion", True),
                           ("stepDegrees", [0.1, 0.1]), ("verticalDatum", ""), ("heightUnit", "foot"),
                           ("rows", [[True, 1], [2, 3]]), ("rows", [[1, 2], [3]]),
                           ("rows", [[float("nan"), 1], [2, 3]])):
            with self.subTest(key=key, value=value):
                source = plane()
                source[key] = value
                with self.assertRaises(ValueError):
                    COMPILER["validate_source"](source)

    def cli(self, source, output, size=300):
        return subprocess.run([sys.executable, str(SCRIPT), "--source-grid", str(source),
                               "--bbox", *map(str, REAL_BBOX), "--size", str(size), "--output", str(output)],
                              cwd=ROOT, capture_output=True, text=True)

    def test_actual_dsm_fixture_cli_and_byte_provenance(self):
        fixture = json.loads(REAL_GRID.read_text())
        for size in (300, 400):
            with self.subTest(size=size), tempfile.TemporaryDirectory() as temporary:
                output = Path(temporary) / "candidate.json"
                result = self.cli(REAL_GRID, output, size)
                self.assertEqual(result.returncode, 0, result.stderr)
                candidate = json.loads(output.read_text())
                self.assertEqual(candidate["sourceGridBytesSha256"], hashlib.sha256(REAL_GRID.read_bytes()).hexdigest())
                self.assertTrue(candidate["localSourceHashVerified"])
                self.assertFalse(candidate["sourceSampleExtractionVerified"])
                self.assertEqual(len(candidate["elevationRowsMetres"]), size)
                self.assertTrue(candidate["completeSampleCoverage"])
                self.assertEqual(candidate["sourceClassification"], "modern-dsm")
                values = [value for row in fixture["rows"] for value in row]
                self.assertGreaterEqual(candidate["rangeMetres"][0], min(values))
                self.assertLessEqual(candidate["rangeMetres"][1], max(values))
                self.assertFalse(candidate["gameVerified"])

    def test_cli_hash_mismatch_and_source_overwrite_do_not_write(self):
        with tempfile.TemporaryDirectory() as temporary:
            source, output = Path(temporary) / "input.json", Path(temporary) / "candidate.json"
            data = json.loads(REAL_GRID.read_text())
            data["provenance"]["sourceSha256"] = "0" * 64
            source.write_text(json.dumps(data))
            self.assertNotEqual(self.cli(source, output).returncode, 0)
            self.assertFalse(output.exists())
            before = source.read_bytes()
            self.assertNotEqual(self.cli(source, source).returncode, 0)
            self.assertEqual(source.read_bytes(), before)

    def test_padded_reference_gap_and_half_cell_gap_are_separate(self):
        episode = {"id": "synthetic", "order": 1, "geographyId": "region", "mapSize": 300,
                   "mapPlan": {"bbox": [-0.1, -0.1, 0.1, 0.1]}}
        record = EXTENT["audit_episode"]("campaign", episode, {"bbox": [-0.1, -0.1, 0.1, 0.1]})
        self.assertTrue(record["requestedBBoxWithinReference"])
        self.assertFalse(record["paddedSampleCentersWithinReference"])
        self.assertTrue(record["coverageReviewNeeded"])
        frame = FRAME["make_frame"](episode["mapPlan"]["bbox"], 300)
        record = EXTENT["audit_episode"]("campaign", episode, {"bbox": frame.bounds_at(0, 299)})
        self.assertTrue(record["paddedSampleCentersWithinReference"])
        self.assertTrue(record["onlyOuterHalfCellExceedsReference"])
        record = EXTENT["audit_episode"]("campaign", episode, {"bbox": [-0.2, -0.2, 0.2, 0.2]})
        self.assertFalse(record["coverageReviewNeeded"])

    def test_extent_audit_preserves_zero_dossier_campaign_and_rejects_missing_source(self):
        policy = {"campaigns": [{"id": "a"}, {"id": "b"}]}
        episode = {"id": "synthetic", "order": 1, "geographyId": "region", "mapSize": 300,
                   "mapPlan": {"bbox": [-0.1, -0.1, 0.1, 0.1]}}
        campaigns = [{"campaignId": "a", "episodes": [episode], "episodeSelection": [episode]},
                     {"campaignId": "b", "episodes": [], "episodeSelection": [{"id": "pending"}]}]
        report = EXTENT["build_report"](policy, campaigns, {"region": {"bbox": [-0.2, -0.2, 0.2, 0.2]}}, {})
        self.assertEqual(report["authoredDossiers"], 1)
        self.assertEqual(report["selectedEpisodes"], 2)
        self.assertEqual(report["campaignCoverage"][1]["authoredDossiers"], 0)
        self.assertFalse(report["gameVerified"])
        with self.assertRaisesRegex(ValueError, "Missing geographic reference"):
            EXTENT["build_report"](policy, campaigns, {}, {})
        del campaigns[1]["episodes"]
        with self.assertRaisesRegex(ValueError, "explicitly declare"):
            EXTENT["build_report"](policy, campaigns, {"region": {"bbox": [-0.2, -0.2, 0.2, 0.2]}}, {})

    def test_actual_extent_cli_is_complete_without_granting_approval(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "extent.json"
            result = subprocess.run([sys.executable, str(ROOT / "tools/map/geographic_extent_audit.script.py"),
                                     "--output", str(output)], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(output.read_text())
            self.assertEqual(report["authoredDossiers"], len(report["records"]))
            self.assertEqual(report["extentQuestions"], sum(row["coverageReviewNeeded"] for row in report["records"]))
            self.assertEqual(len(report["campaignCoverage"]), len(json.loads((ROOT / "docs/design/odyssey-policy.json").read_text())["campaigns"]))
            self.assertTrue(report["sourceSemanticHashes"])
            self.assertFalse(report["gameVerified"])


if __name__ == "__main__":
    unittest.main()
