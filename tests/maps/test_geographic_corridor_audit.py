"""Tests for the conservative continuous capsule audit of an authored corridor.

The audit must be conservative: every tile whose own footprint could touch the
authored capsule belongs to the envelope. It must not reproduce the older
fixture helper's even-width shortcut, must not round the author's points and
must not carve or flatten anything.

The expected sets here are computed independently of the helper: the segment,
the endcaps and the even widths are worked out from the radius and the tile
geometry, not by calling the helper back on itself. These are pure geometry
tests; they touch no native file and execute no game.
"""

import math
import runpy
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = runpy.run_path(str(ROOT / "tools/map/geographic_corridor_audit.helper.py"))
FIXTURE = runpy.run_path(str(ROOT / "tools/map/transport_fixture.py"))

AUDIT_CORRIDOR = AUDIT["audit_corridor"]
CAPSULE_CELLS = AUDIT["capsule_cells"]
ENVELOPE_CELLS = AUDIT["envelope_cells"]
OUTSIDE_CELLS = AUDIT["outside_cells"]
ENVELOPE_RADIUS = AUDIT["envelope_radius"]
POLYLINE_DISTANCE = AUDIT["polyline_distance"]
TILE_HALF_DIAGONAL = math.sqrt(0.5)


def expected_cells_for_segment(start, end, width_tiles, size):
    """The expected inclusion set of one straight segment, worked out here.

    A tile belongs to the envelope when the distance from its centre to the
    segment is at most width/2 + sqrt(0.5). The distance to a straight
    segment is the distance to the line for a projection inside the segment
    and the distance to the nearest endpoint otherwise.
    """
    radius = width_tiles / 2.0 + math.sqrt(0.5)
    cells = set()
    for y in range(size):
        for x in range(size):
            centre = (x + 0.5, y + 0.5)
            ax, ay = start
            bx, by = end
            dx, dy = bx - ax, by - ay
            length = dx * dx + dy * dy
            if length == 0:
                distance = math.dist(centre, start)
            else:
                ratio = ((centre[0] - ax) * dx + (centre[1] - ay) * dy) / length
                ratio = min(1.0, max(0.0, ratio))
                distance = math.dist(centre, (ax + ratio * dx, ay + ratio * dy))
            if distance <= radius:
                cells.add((x, y))
    return cells


class GeographicCorridorAuditTests(unittest.TestCase):
    def test_a_straight_segment_matches_the_independently_expected_set(self):
        points = [(40.0, 30.25), (90.5, 70.75)]
        expected = expected_cells_for_segment(
            points[0], points[1], 6, 140
        )
        cells = set(ENVELOPE_CELLS(points, 6, 140))
        self.assertEqual(cells, expected)
        self.assertTrue(cells)

    def test_the_radius_is_the_width_half_plus_the_tile_half_diagonal(self):
        self.assertAlmostEqual(ENVELOPE_RADIUS(10), 5.0 + TILE_HALF_DIAGONAL)
        self.assertAlmostEqual(ENVELOPE_RADIUS(6), 3.0 + TILE_HALF_DIAGONAL)
        self.assertAlmostEqual(ENVELOPE_RADIUS(1), 0.5 + TILE_HALF_DIAGONAL)

    def test_an_even_width_keeps_the_half_width_the_older_helper_dropped(self):
        # A width of ten is a capsule of radius five: eleven tile centres
        # straddle the axis when the axis runs through a tile centre and ten
        # when it runs on a tile edge. The older helper's (width-1)//2 radius
        # covers nine tiles in both cases.
        points = [(60, 60), (100, 60)]
        wide = set(ENVELOPE_CELLS(points, 10, 140))
        narrow = set(ENVELOPE_CELLS(points, 6, 140))
        square_ten = FIXTURE["corridor_cells"](points, 10)
        square_six = FIXTURE["corridor_cells"](points, 6)
        self.assertEqual(9, len({row for _, row in square_ten}))
        self.assertEqual(5, len({row for _, row in square_six}))

        def rows(cells, axis, radius):
            return {
                cell[1]
                for cell in cells
                if abs((cell[1] + 0.5) - axis) <= radius and 60 <= cell[0] <= 99
            }

        self.assertEqual(11, len(rows(wide, 60.5, 5.0)))
        self.assertEqual(10, len(rows(wide, 60.0, 5.0)))
        self.assertEqual(7, len(rows(narrow, 60.5, 3.0)))
        self.assertEqual(6, len(rows(narrow, 60.0, 3.0)))
        self.assertGreater(len({row for _, row in wide}), 9)
        self.assertGreater(len({row for _, row in narrow}), 5)

    def test_the_authored_points_are_not_rounded(self):
        points = [(60.4, 60.6), (100.4, 60.6)]
        rounded = [(60.0, 61.0), (100.0, 61.0)]
        cells = set(ENVELOPE_CELLS(points, 4, 140))
        rounded_cells = set(ENVELOPE_CELLS(rounded, 4, 140))
        self.assertNotEqual(cells, rounded_cells)

    def test_the_endcaps_reach_the_authored_endpoint_plus_the_radius(self):
        points = [(60.0, 60.0), (100.0, 60.0)]
        radius = 8 / 2.0 + math.sqrt(0.5)
        cells = set(ENVELOPE_CELLS(points, 8, 140))
        beyond = [cell for cell in cells if cell[0] > 100]
        self.assertTrue(beyond)
        self.assertEqual(104, max(x for x, _ in beyond))
        # The last included tile is the one whose centre is still inside the
        # cap: 104.5 is 4.5 tiles from the endpoint, 105.5 is 5.5 tiles away.
        self.assertLessEqual(100 + 8 / 2.0 + math.sqrt(0.5), 104 + 1)
        self.assertGreater(100 + 8 / 2.0 + math.sqrt(0.5), 104)
        self.assertGreater(radius, 4.0)

    def test_a_capsule_that_fits_the_frame_is_accepted(self):
        # The capsule of a width of ten reaches 5.5 - 5 = 0.5 tiles from the
        # frame edge, so it stays inside the map; the tile whose centre would
        # be at x = -0.5 is six tiles away and outside the radius.
        report = AUDIT_CORRIDOR([(5.5, 50.0), (15.5, 50.0)], 10, 140)
        self.assertTrue(report["accepted"])
        self.assertFalse(report["envelopeLeavesFrame"])
        self.assertEqual(0, report["outsideCellCount"])
        self.assertNotIn((-1, 50), [tuple(cell) for cell in report["includedCells"]])
        self.assertGreater(
            POLYLINE_DISTANCE((-0.5, 50.0), [(5.5, 50.0), (15.5, 50.0)]), 5.707
        )

    def test_a_capsule_that_reaches_outside_the_frame_is_refused(self):
        report = AUDIT_CORRIDOR([(4.5, 50.0), (14.5, 50.0)], 10, 140)
        self.assertFalse(report["accepted"])
        self.assertTrue(report["envelopeLeavesFrame"])
        self.assertGreater(report["outsideCellCount"], 0)
        self.assertTrue(
            any(
                "leaves the frame" in violation["reason"]
                for violation in report["violations"]
            )
        )

    def test_the_outside_cells_are_enumerated_and_not_clipped_away(self):
        outside = OUTSIDE_CELLS([(4.5, 50.0), (14.5, 50.0)], 10, 140)
        self.assertTrue(outside)
        self.assertTrue(all(not (0 <= x < 140 and 0 <= y < 140) for x, y in outside))
        candidates = CAPSULE_CELLS([(4.5, 50.0), (14.5, 50.0)], 10)
        self.assertEqual(len(candidates), len(outside) + len(ENVELOPE_CELLS(
            [(4.5, 50.0), (14.5, 50.0)], 10, 140
        )))

    def test_known_water_inside_the_corridor_is_reported(self):
        report = AUDIT_CORRIDOR(
            [(60.0, 60.0), (100.0, 60.0)],
            6,
            140,
            levels=[[3] * 140 for _ in range(140)],
            known_water_cells=[[70, 60]],
        )
        self.assertFalse(report["accepted"])
        self.assertEqual(1, report["knownWaterCellCount"])
        self.assertTrue(
            any("known water" in violation["reason"] for violation in report["violations"])
        )

    def test_a_cell_without_data_inside_the_corridor_is_reported(self):
        levels = [[3] * 140 for _ in range(140)]
        levels[60][70] = None
        report = AUDIT_CORRIDOR(
            [(60.0, 60.0), (100.0, 60.0)], 6, 140, levels=levels
        )
        self.assertFalse(report["accepted"])
        self.assertEqual(1, report["nodataCellCount"])
        self.assertTrue(
            any(
                "no data" in violation["reason"] for violation in report["violations"]
            )
        )

    def test_adjacent_level_changes_are_reported(self):
        levels = [[3] * 140 for _ in range(140)]
        for x in range(60, 101):
            levels[60][x] = 4
        report = AUDIT_CORRIDOR(
            [(60.0, 60.0), (100.0, 60.0)], 6, 140, levels=levels
        )
        self.assertTrue(report["accepted"])
        self.assertGreater(report["adjacentLevelChangeCount"], 0)
        self.assertEqual(0, report["adjacentLevelJumpAtLeast2Count"])

    def test_a_cliff_inside_the_corridor_is_reported_as_a_jump(self):
        levels = [[3] * 140 for _ in range(140)]
        for x in range(60, 101):
            levels[60][x] = 3
        for x in range(80, 101):
            levels[60][x] = 5
        report = AUDIT_CORRIDOR(
            [(60.0, 60.0), (100.0, 60.0)], 6, 140, levels=levels
        )
        self.assertGreater(report["adjacentLevelJumpAtLeast2Count"], 0)
        jump = report["adjacentLevelJumpsAtLeast2"][0]
        self.assertEqual(2, abs(jump["delta"]))

    def test_the_distance_to_the_polyline_covers_the_endcaps(self):
        self.assertAlmostEqual(
            POLYLINE_DISTANCE((100.0, 60.0), [(60.0, 60.0), (100.0, 60.0)]), 0.0
        )
        self.assertAlmostEqual(
            POLYLINE_DISTANCE((104.0, 60.0), [(60.0, 60.0), (100.0, 60.0)]), 4.0
        )
        self.assertAlmostEqual(
            POLYLINE_DISTANCE((80.0, 64.0), [(60.0, 60.0), (100.0, 60.0)]), 4.0
        )

    def test_a_degenerate_width_is_refused(self):
        with self.assertRaises(ValueError):
            ENVELOPE_RADIUS(0)
        with self.assertRaises(ValueError):
            ENVELOPE_RADIUS(True)

    def test_the_architect_corridors_keep_their_reviewed_cell_counts(self):
        plan = __import__("json").loads(
            (ROOT / "docs/wiki/faith-origins/episodes/02-civilian-refuge-jerusalem/25-private-geographic-preview-plan.json").read_text(
                encoding="utf8"
            )
        )
        expected = {"main": 1225, "relief": 1014}
        for corridor in plan["corridors"]:
            cells = ENVELOPE_CELLS(
                [tuple(point) for point in corridor["tilePoints"]],
                corridor["widthTiles"],
                plan["frame"]["mapSize"],
            )
            self.assertEqual(expected[corridor["id"]], len(cells), corridor["id"])
            self.assertEqual(
                [], OUTSIDE_CELLS(
                    [tuple(point) for point in corridor["tilePoints"]],
                    corridor["widthTiles"],
                    plan["frame"]["mapSize"],
                )
            )


if __name__ == "__main__":
    unittest.main()
