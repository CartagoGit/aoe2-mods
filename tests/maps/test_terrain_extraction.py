"""Adversarial checks for the verified DSM extraction step.

The reference is `tests/maps/fixtures/edirne-dsm-sample-grid.json`, whose
twenty-five values were read by hand from the real Edirne crop. This module
must reproduce them exactly; a decoder that differs in the last bit, or that
resolves the sample anchor differently, fails here.
"""

import json
import runpy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CROP = ROOT / "docs/research/odyssey-research/geography/edirne-modern-dsm-regional-crop.tif"
FIXTURE = ROOT / "tests/maps/fixtures/edirne-dsm-sample-grid.json"
LICENCE = "docs/research/odyssey-research/geography/edirne-modern-dsm-license.md"

EXTRACTOR = runpy.run_path(str(ROOT / "tools/map/geographic_dsm_extractor.py"))
extract_window = EXTRACTOR["extract_window"]
verify_extraction = EXTRACTOR["verify_extraction"]
georeference = EXTRACTOR["georeference"]
sample_origin = EXTRACTOR["sample_origin"]
read_pixel = EXTRACTOR["read_pixel"]


def grid(**overrides):
    arguments = {
        "column_start": 576,
        "column_end": 580,
        "row_start": 826,
        "row_end": 830,
        "sample_anchor": "centre",
        "vertical_datum": "EGM2008 (product documentation)",
        "source_classification": "modern-dsm",
        "licence_notice_path": LICENCE,
    }
    arguments.update(overrides)
    return extract_window(str(CROP), **arguments)


def build_tiff(path, *, width=2, height=2, values=(1.0, 2.0, 3.0, 4.0),
               scale=(0.0002777777777777778, 0.0002777777777777778, 0.0),
               tiepoint=(0.0, 0.0, 0.0, 26.4, 41.9, 0.0),
               geographic_type=4326, transformation=None):
    """Write a minimal little-endian float32 TIFF, used for the refusal cases."""
    import struct

    samples = b"".join(struct.pack("<f", value) for value in values)
    entries = [
        (256, 4, 1, struct.pack("<I", width)),
        (257, 4, 1, struct.pack("<I", height)),
        (258, 3, 1, struct.pack("<H", 32)),
        (259, 3, 1, struct.pack("<H", 1)),
        (277, 3, 1, struct.pack("<H", 1)),
        (284, 3, 1, struct.pack("<H", 1)),
        (339, 3, 1, struct.pack("<H", 3)),
        (273, 4, 1, struct.pack("<I", 8)),
        (279, 4, 1, struct.pack("<I", len(samples))),
        (33550, 12, 3, struct.pack("<3d", *scale)),
        (33922, 12, 6, struct.pack("<6d", *tiepoint)),
        (34735, 3, 8, struct.pack("<8H", 1, 1, 0, 1, 2048, 0, 1, geographic_type)),
    ]
    if transformation is not None:
        entries.append((34264, 12, 16, struct.pack("<16d", *transformation)))

    data_offset = 8
    ifd_offset = data_offset + len(samples)
    ifd_size = 2 + 12 * len(entries) + 4
    ext_offset = ifd_offset + ifd_size
    external = bytearray()
    positions = {}
    for tag, field_type, count, payload in entries:
        if len(payload) > 4:
            positions[tag] = ext_offset + len(external)
            external += payload
            if len(external) % 2:
                external += b"\x00"
    out = bytearray(b"II" + struct.pack("<HI", 42, ifd_offset))
    out += samples
    out += struct.pack("<H", len(entries))
    for tag, field_type, count, payload in entries:
        if len(payload) > 4:
            value = struct.pack("<I", positions[tag])
        else:
            value = payload + b"\x00" * (4 - len(payload))
        out += struct.pack("<HHI", tag, field_type, count) + value
    out += struct.pack("<I", 0)
    out += external
    Path(path).write_bytes(bytes(out))
    return str(path)


class ExtractionTest(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_fixture_is_present_and_declares_its_own_provenance(self):
        self.assertEqual(self.fixture["provenance"]["columnOffset"], 576)
        self.assertEqual(self.fixture["provenance"]["rowOffset"], 826)
        self.assertEqual(self.fixture["provenance"]["width"], 5)
        self.assertEqual(self.fixture["provenance"]["height"], 5)
        self.assertTrue(self.fixture["provenance"]["licenseNoticePath"].endswith(
            "edirne-modern-dsm-license.md"))

    def test_extracted_values_reproduce_the_hand_verified_fixture_exactly(self):
        extracted = grid()
        self.assertEqual(extracted["rows"], self.fixture["rows"])

    def test_sample_origin_reproduces_the_hand_verified_origin(self):
        extracted = grid()
        self.assertEqual(extracted["sampleOriginLonLat"], self.fixture["sampleOriginLonLat"])
        self.assertEqual(extracted["stepDegrees"], self.fixture["stepDegrees"])

    def test_source_digest_matches_the_recorded_one(self):
        extracted = grid()
        self.assertEqual(extracted["provenance"]["sourceSha256"],
                         self.fixture["provenance"]["sourceSha256"])

    def test_georeference_records_the_declared_anchor_and_the_geokey(self):
        reference = georeference(str(CROP))
        self.assertEqual(reference["rasterTypeGeoKey"], 2)
        self.assertEqual(reference["geographicTypeGeoKey"], 4326)
        self.assertEqual(reference["imageWidth"], 1441)
        self.assertEqual(reference["imageLength"], 1081)
        self.assertEqual(reference["bitsPerSample"], 32)
        self.assertEqual(reference["sampleFormat"], 3)
        self.assertEqual(reference["predictor"], 3)
        extracted = grid()
        self.assertIn("declared anchor 'centre'",
                      extracted["georeference"]["rasterInterpretation"])
        self.assertIn("GeoKey 1025 = 2", extracted["georeference"]["rasterInterpretation"])

    def test_a_corner_anchor_shifts_the_origin_by_half_a_pixel(self):
        centre = sample_origin(georeference(str(CROP)), 576, 826, "centre")
        corner = sample_origin(georeference(str(CROP)), 576, 826, "corner")
        self.assertAlmostEqual(corner[0] - centre[0], 0.0002777777777777778 / 2, places=12)
        self.assertAlmostEqual(corner[1] - centre[1], -0.0002777777777777778 / 2, places=12)

    def test_an_undeclared_anchor_is_refused(self):
        with self.assertRaises(ValueError):
            sample_origin(georeference(str(CROP)), 576, 826, "guessed")

    def test_a_rotated_raster_is_refused(self):
        import tempfile

        with tempfile.TemporaryDirectory() as folder:
            transformation = [1.0, 0.0, 0.0, 0.0,
                              0.0, 1.0, 0.0, 0.0,
                              0.0, 0.0, 1.0, 0.0,
                              0.0, 0.0, 0.0, 1.0]
            path = build_tiff(Path(folder) / "rotated.tif", transformation=transformation)
            with self.assertRaises(ValueError):
                georeference(path)

    def test_a_non_wgs84_raster_is_refused(self):
        import tempfile

        with tempfile.TemporaryDirectory() as folder:
            path = build_tiff(Path(folder) / "utm.tif", geographic_type=32632)
            with self.assertRaises(ValueError):
                extract_window(path, column_start=0, column_end=1, row_start=0, row_end=1,
                               sample_anchor="centre", vertical_datum="none",
                               source_classification="modern-dsm", licence_notice_path=LICENCE)

    def test_a_minimal_unrotated_raster_is_accepted_and_read(self):
        import tempfile

        with tempfile.TemporaryDirectory() as folder:
            path = build_tiff(Path(folder) / "plain.tif")
            reference = georeference(path)
            self.assertEqual(reference["geographicTypeGeoKey"], 4326)
            self.assertEqual(reference["imageWidth"], 2)
            self.assertEqual(read_pixel(path, 1, 1), 4.0)
            self.assertEqual(sample_origin(reference, 0, 0, "centre"), [26.4, 41.9])

    def test_verify_extraction_reports_no_mismatch(self):
        extracted = grid()
        receipt = verify_extraction(extracted, str(CROP), column_start=576, row_start=826)
        self.assertTrue(receipt["verified"])
        self.assertEqual(receipt["sampleCount"], 25)
        self.assertEqual(receipt["mismatches"], [])
        self.assertEqual(receipt["sourceSha256"], self.fixture["provenance"]["sourceSha256"])

    def test_verify_extraction_detects_a_tampered_value(self):
        extracted = grid()
        extracted["rows"][2][3] = extracted["rows"][2][3] + 1.0
        receipt = verify_extraction(extracted, str(CROP), column_start=576, row_start=826)
        self.assertFalse(receipt["verified"])
        self.assertEqual(len(receipt["mismatches"]), 1)
        self.assertEqual(receipt["mismatches"][0]["cell"], [579, 828])

    def test_a_sample_outside_the_raster_is_refused(self):
        with self.assertRaises(ValueError):
            read_pixel(str(CROP), 2000, 826)
        with self.assertRaises(ValueError):
            read_pixel(str(CROP), 576, 5000)

    def test_the_receipt_keeps_the_datum_the_licence_and_the_limits(self):
        extracted = grid(limits=["a modern DSM is a surface model, not a bare earth model"])
        self.assertEqual(extracted["verticalDatum"], "EGM2008 (product documentation)")
        self.assertEqual(extracted["sourceClassification"], "modern-dsm")
        self.assertEqual(extracted["provenance"]["licenseNoticePath"], LICENCE)
        self.assertEqual(len(extracted["limits"]), 1)
        self.assertEqual(extracted["horizontalCrs"], "EPSG:4326")
        self.assertEqual(extracted["heightUnit"], "metre")

    def test_the_module_has_no_third_party_import(self):
        source = (ROOT / "tools/map/geographic_dsm_extractor.py").read_text(encoding="utf-8")
        for forbidden in ("import numpy", "from numpy", "import PIL", "from PIL",
                          "import rasterio", "from osgeo", "import tifffile"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
