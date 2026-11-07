"""Compress verified modern relief into the native 0-7 height range.

This implements the architect's published candidate band table from
`docs/research/odyssey-research/adrianople378-relief-design.md` and nothing
more. It is a research candidate: it asserts no terrain, navigation, water or
game approval, and it decides no flattening and no relocation.

Four rules the architect set, kept literally:

* the bands are **absolute metre thresholds**, never a per-district quantile
  remapping, so two districts at the same height get the same native level and
  the regional orientation is not changed by the compression;
* **native height 0 does not mean water**. This module never emits a water
  claim; the water of a map comes from the dated layer, not from a height band;
* a cliff is **not applied wherever a threshold is crossed**. A level jump of
  two or more is detected and reported, and a graded transition is *proposed*
  for the architect to accept or reject, never applied silently;
* unknown ground stays unknown. A nodata sample is never filled, and a region
  the raster does not cover keeps its unknown cells instead of being flattened.

The input is the output of `tools/map/geographic_raster.compiler.py`, so the
metre-height resampling and this compression compose without a second
projection, a second resampling or a second coordinate system.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# The architect's candidate compression, verbatim:
#   below 70 m -> 0; 70-<100 -> 1; 100-<130 -> 2; 130-<160 -> 3;
#   160-<190 -> 4; 190-<220 -> 5; 220-<250 -> 6; 250 and above -> 7.
CANDIDATE_BANDS = (
    (70.0, 1),
    (100.0, 2),
    (130.0, 3),
    (160.0, 4),
    (190.0, 5),
    (220.0, 6),
    (250.0, 7),
)
NATIVE_MIN = 0
NATIVE_MAX = 7
# A graded transition never rises more than one native level between adjacent
# cells, so a level jump of two or more is a cliff candidate.
MAX_NATIVE_STEP = 1

BAND_STATUS = (
    "architect candidate band table; not implemented terrain, not a historic "
    "reconstruction, not approved for native use"
)


def band_for_height(metres, bands=CANDIDATE_BANDS):
    """The native level for an absolute modern height.

    The thresholds are absolute, so this is a pure function of the height and
    two places at the same height always get the same level. There is no
    quantile remapping and no per-district normalisation.
    """
    if metres is None:
        return None
    level = NATIVE_MIN
    for threshold, candidate in bands:
        if metres < threshold:
            break
        level = candidate
    return level


def _grid_shape(rows, size):
    if len(rows) != size:
        raise ValueError(f"expected {size} rows, got {len(rows)}")
    for index, row in enumerate(rows):
        if len(row) != size:
            raise ValueError(f"row {index} has {len(row)} samples, expected {size}")
    return True


def quantise_height_candidate(candidate, bands=CANDIDATE_BANDS):
    """Compress a metre-height raster candidate into native levels 0..7."""
    if candidate.get("kind") != "geographic-height-raster-candidate":
        raise ValueError("expected a geographic-height-raster-candidate")
    if candidate.get("heightUnit") != "metre":
        raise ValueError("the raster candidate must carry explicit metre units")
    size = candidate.get("mapSize")
    rows = candidate.get("elevationRowsMetres")
    if not isinstance(size, int) or not rows:
        raise ValueError("the raster candidate needs a map size and elevation rows")
    _grid_shape(rows, size)

    levels = []
    histogram = {str(level): 0 for level in range(NATIVE_MIN, NATIVE_MAX + 1)}
    nodata_cells = 0
    heights = []
    for row in rows:
        level_row = []
        for value in row:
            level = band_for_height(value, bands)
            if level is None:
                nodata_cells += 1
                level_row.append(None)
                continue
            heights.append(value)
            histogram[str(level)] += 1
            level_row.append(level)
        levels.append(level_row)

    edges = cliff_edges(levels, size)
    ramps = candidate_ramps(levels, size, edges)
    return {
        "schemaVersion": 1,
        "kind": "native-height-candidate",
        "status": "research candidate; no terrain, navigation, water or game approval",
        "bandStatus": BAND_STATUS,
        "bands": [{"fromMetres": threshold, "nativeLevel": level} for threshold, level in bands],
        "quantisationRule": (
            "absolute metre bands applied to the whole padded square; no per-district "
            "quantile remapping, no mirroring, no regional orientation change"
        ),
        "mapSize": size,
        "requestedBBox": candidate.get("requestedBBox"),
        "orientation": candidate.get("orientation"),
        "projection": candidate.get("projection"),
        "resampling": candidate.get("resampling"),
        "sourceClassification": candidate.get("sourceClassification"),
        "verticalDatum": candidate.get("verticalDatum"),
        "rangeMetres": candidate.get("rangeMetres"),
        "levelHistogram": histogram,
        "nodataCells": nodata_cells,
        "unknownCellsPreserved": nodata_cells > 0,
        "cliffEdges": edges,
        "cliffEdgeCount": len(edges),
        "rampCandidates": ramps,
        "rampCandidateCount": len(ramps),
        "waterStatus": (
            "native height 0 is not water; no water cell, shoreline or hydrology is "
            "asserted here and the water of a map comes from its dated layer"
        ),
        "passabilityStatus": (
            "unassessed; a level difference of one is not certified walkable and a "
            "level difference of two or more is a cliff candidate, not an obstacle"
        ),
        "historicalStatus": (
            "unassessed; a modern surface may carry vegetation, buildings and modern "
            "infrastructure, and no ancient surface is inferred"
        ),
        "flatteningApplied": False,
        "relocationApplied": False,
        "nativeTerrainWritten": False,
        "gameVerified": False,
        "levelRows": levels,
    }


def cliff_edges(levels, size):
    """Edges where the native level jumps by two or more.

    A threshold crossing is not a cliff on its own: only a jump the architect's
    own rule forbids, a rise of more than one native level between adjacent
    cells, is reported here.
    """
    edges = []
    for y in range(size):
        for x in range(size):
            here = levels[y][x]
            if here is None:
                continue
            for dx, dy in ((1, 0), (0, 1)):
                nx, ny = x + dx, y + dy
                if nx >= size or ny >= size:
                    continue
                there = levels[ny][nx]
                if there is None:
                    continue
                delta = int(there) - int(here)
                if abs(delta) >= MAX_NATIVE_STEP + 1:
                    edges.append(
                        {
                            "from": [x, y],
                            "to": [nx, ny],
                            "levelFrom": int(here),
                            "levelTo": int(there),
                            "delta": delta,
                            "reason": "native level jump above one",
                        }
                    )
    return edges


def candidate_ramps(levels, size, edges):
    """Propose a graded transition for each cliff edge.

    This is a proposal, never an edit. The architect decides whether a ridge
    needs a connected graded transition, and the exact flattening and any
    relocation of actors need architect review with evidence, so the candidate
    only reports the cells and the levels it would assign.
    """
    candidates = []
    for edge in edges:
        low, high = (edge["from"], edge["to"]) if edge["levelTo"] > edge["levelFrom"] else (edge["to"], edge["from"])
        low_level = min(edge["levelFrom"], edge["levelTo"])
        high_level = max(edge["levelFrom"], edge["levelTo"])
        steps = []
        current = high
        visited = {tuple(high)}
        while True:
            steps.append({"cell": list(current), "fromLevel": levels[current[1]][current[0]], "toLevel": None})
            if levels[current[1]][current[0]] is None or levels[current[1]][current[0]] <= low_level + MAX_NATIVE_STEP:
                break
            best = None
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = current[0] + dx, current[1] + dy
                if not (0 <= nx < size and 0 <= ny < size):
                    continue
                if (nx, ny) in visited:
                    continue
                value = levels[ny][nx]
                if value is None:
                    continue
                if best is None or value < levels[best[1]][best[0]]:
                    best = (nx, ny)
            if best is None:
                break
            visited.add(best)
            current = best
        # the staircase descends one level per cell from the high side
        for index, step in enumerate(steps):
            step["toLevel"] = max(low_level + MAX_NATIVE_STEP, high_level - index)
        candidates.append(
            {
                "cliffEdge": edge,
                "cells": steps,
                "fromLevel": high_level,
                "toLevel": low_level,
                "status": "candidate for architect review; not applied",
            }
        )
    return candidates


def write_candidate(candidate, path):
    """Write the candidate to an explicit path, as a research artifact."""
    target = Path(path)
    if target.parent and str(target.parent) not in ("", "."):
        target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return str(target)
