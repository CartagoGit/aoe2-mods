"""Conservative continuous capsule audit for an authored corridor.

The existing transport fixture helper paints a square span of
(width-1)//2 tiles around rounded points, so an authored width of 10 covers
nine tiles and an authored width of 6 covers five. That helper is unchanged
and is not reused here.

This module computes the conservative envelope of the authored continuous
capsule. The author's points are used exactly as they were authored: they are
never rounded and the width is never reduced. A tile belongs to the envelope
when its own footprint could touch the capsule of radius width/2 around the
polyline, which is exactly

    distance(tile centre, polyline) <= width/2 + sqrt(0.5)

because sqrt(0.5) is the largest distance from the centre of a unit tile to
any point of that tile's own footprint. Extra included cells are deliberate
conservatism.

The audit never carves a path, never flattens or lowers terrain, never
infers water and never claims a native navigation result. It reports the
included cells, the level changes between adjacent included cells and every
cell that carries no data or lies on known water.

The candidate enumeration is deliberately not clipped to the frame. A tile the
capsule reaches outside the frame is enumerated and recorded, and its
presence refuses the corridor: a clipped enumeration would otherwise prove
nothing about the reach of the capsule.
"""

import math

# The largest distance from the centre of a unit tile to any point of its own
# footprint: half of the tile diagonal.
TILE_HALF_DIAGONAL = math.sqrt(0.5)

INCLUSION_RULE = (
    "distance(tile centre, polyline) <= width/2 + sqrt(0.5); the author's "
    "points are used as authored and are never rounded, and the width is "
    "never reduced"
)
AUDIT_STATUS = (
    "conservative geometric envelope of the authored capsule; not exact "
    "polygon rasterisation, not a carved path and not native navigation"
)


def _finite(value):
    return type(value) in (int, float) and math.isfinite(value)


def point_segment_distance(point, start, end):
    """The distance from a point to a closed segment, without rounding."""
    px, py = point
    ax, ay = start
    bx, by = end
    dx, dy = bx - ax, by - ay
    length = dx * dx + dy * dy
    if length == 0:
        return math.dist(point, start)
    ratio = ((px - ax) * dx + (py - ay) * dy) / length
    ratio = min(1.0, max(0.0, ratio))
    return math.dist(point, (ax + ratio * dx, ay + ratio * dy))


def polyline_distance(point, points):
    """The distance from a point to the polyline, endcaps included.

    The distance to a closed segment already covers the round cap at each
    endpoint, so the union of the segment capsules is the polyline capsule.
    """
    if len(points) < 2:
        raise ValueError("a corridor needs at least two points")
    return min(
        point_segment_distance(point, points[index], points[index + 1])
        for index in range(len(points) - 1)
    )


def envelope_radius(width_tiles):
    """The conservative inclusion radius of an authored width."""
    if isinstance(width_tiles, bool) or not _finite(width_tiles) or width_tiles <= 0:
        raise ValueError("a corridor width must be a positive finite number")
    return width_tiles / 2.0 + TILE_HALF_DIAGONAL


def _points_bounds(points):
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return min(xs), min(ys), max(xs), max(ys)


def capsule_cells(points, width_tiles):
    """Every tile candidate of the authored capsule, inside and outside a frame.

    The candidates are enumerated over a bounded window around the authored
    points and are not clipped to a frame: a tile that the capsule reaches
    outside the frame is recorded here, so a clipped enumeration can never
    hide an out-of-frame inclusion.
    """
    radius = envelope_radius(width_tiles)
    min_x, min_y, max_x, max_y = _points_bounds(points)
    first_x = math.floor(min_x - radius - 1)
    last_x = math.ceil(max_x + radius + 1)
    first_y = math.floor(min_y - radius - 1)
    last_y = math.ceil(max_y + radius + 1)
    cells = []
    for y in range(first_y, last_y + 1):
        for x in range(first_x, last_x + 1):
            if polyline_distance((x + 0.5, y + 0.5), points) <= radius:
                cells.append((x, y))
    return cells


def _in_frame(cell, size):
    return 0 <= cell[0] < size and 0 <= cell[1] < size


def envelope_cells(points, width_tiles, size):
    """The included tiles that fall inside the frame."""
    return [
        cell
        for cell in capsule_cells(points, width_tiles)
        if _in_frame(cell, size)
    ]


def outside_cells(points, width_tiles, size):
    """The included tiles that fall outside the frame.

    A corridor whose capsule reaches beyond the frame is refused: the
    conservative envelope would be incomplete inside the map.
    """
    return [
        cell
        for cell in capsule_cells(points, width_tiles)
        if not _in_frame(cell, size)
    ]


def _level_at(levels, cell):
    if levels is None:
        return None
    x, y = cell
    if y >= len(levels) or x >= len(levels[y]):
        return None
    return levels[y][x]


def audit_corridor(
    points,
    width_tiles,
    size,
    *,
    levels=None,
    known_water_cells=None,
    corridor_id=None,
):
    """Audit one authored corridor against the derived frame.

    `levels` is the derived native level grid, with None for a cell that
    carries no data. `known_water_cells` is the dated water control; it is
    only used to report a violation, never to paint or remove anything.
    """
    if type(size) is not int or size <= 0:
        raise ValueError("the frame size must be a positive integer")
    radius = envelope_radius(width_tiles)
    min_x, min_y, max_x, max_y = _points_bounds(points)
    candidates = capsule_cells(points, width_tiles)
    cells = [cell for cell in candidates if _in_frame(cell, size)]
    outside = [cell for cell in candidates if not _in_frame(cell, size)]
    clipped = bool(outside)
    water = set(tuple(cell) for cell in (known_water_cells or []))
    nodata_cells = []
    water_cells = []
    histogram = {}
    levels_seen = []
    for cell in cells:
        level = _level_at(levels, cell)
        if level is None:
            if levels is not None:
                nodata_cells.append(list(cell))
        else:
            key = str(int(level))
            histogram[key] = histogram.get(key, 0) + 1
            levels_seen.append(int(level))
        if cell in water:
            water_cells.append(list(cell))
    adjacent_changes = 0
    adjacent_jumps = []
    included = set(cells)
    for x, y in cells:
        for neighbour in ((x + 1, y), (x, y + 1)):
            if neighbour not in included:
                continue
            here = _level_at(levels, (x, y))
            there = _level_at(levels, neighbour)
            if here is None or there is None:
                continue
            delta = int(there) - int(here)
            if delta == 0:
                continue
            adjacent_changes += 1
            if abs(delta) >= 2:
                adjacent_jumps.append(
                    {
                        "from": [x, y],
                        "to": list(neighbour),
                        "levelFrom": int(here),
                        "levelTo": int(there),
                        "delta": delta,
                    }
                )
    violations = []
    if clipped:
        violations.append(
            {
                "reason": "the conservative envelope leaves the frame",
                "inclusionRadiusTiles": radius,
                "outsideCellCount": len(outside),
                "outsideCells": [list(cell) for cell in outside[:32]],
                "authoredBounds": [min_x, min_y, max_x, max_y],
            }
        )
    if nodata_cells:
        violations.append(
            {
                "reason": "the corridor covers cells that carry no data",
                "cellCount": len(nodata_cells),
                "cells": nodata_cells[:32],
            }
        )
    if water_cells:
        violations.append(
            {
                "reason": "the corridor covers known water",
                "cellCount": len(water_cells),
                "cells": water_cells[:32],
            }
        )
    return {
        "corridorId": corridor_id,
        "widthTiles": width_tiles,
        "inclusionRadiusTiles": radius,
        "inclusionRule": INCLUSION_RULE,
        "status": AUDIT_STATUS,
        "authoredPointCount": len(points),
        "authoredPoints": [list(point) for point in points],
        "includedCellCount": len(cells),
        "includedCells": [list(cell) for cell in cells],
        "levelHistogram": histogram,
        "minimumLevel": min(levels_seen) if levels_seen else None,
        "maximumLevel": max(levels_seen) if levels_seen else None,
        "adjacentLevelChangeCount": adjacent_changes,
        "adjacentLevelJumpAtLeast2Count": len(adjacent_jumps),
        "adjacentLevelJumpsAtLeast2": adjacent_jumps[:32],
        "nodataCellCount": len(nodata_cells),
        "knownWaterCellCount": len(water_cells),
        "envelopeLeavesFrame": clipped,
        "outsideCellCount": len(outside),
        "violations": violations,
        "accepted": not violations,
    }


def audit_corridors(
    corridors,
    size,
    *,
    levels=None,
    known_water_cells=None,
):
    """Audit every authored corridor of one plan."""
    reports = []
    for corridor in corridors:
        reports.append(
            audit_corridor(
                [tuple(point) for point in corridor["points"]],
                corridor["widthTiles"],
                size,
                levels=levels,
                known_water_cells=known_water_cells,
                corridor_id=corridor.get("id"),
            )
        )
    return {
        "corridors": reports,
        "accepted": all(report["accepted"] for report in reports),
        "status": AUDIT_STATUS,
    }
