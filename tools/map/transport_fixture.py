"""Adversarial transport, crossing and impassability fixtures for i00003/S2.

Pure geometry and policy checks over an authored scenario IR. This module never
executes a native journey, never emulates an adapter operation that does not
exist, and never claims a game observation.

Three things live here, and they are deliberately independent:

* a **dated land/water layer**, decided by an explicit dated control and never
  by elevation. Height says nothing about where the water is;
* **footprint-aware reachability** with an explicit elevation-step rule, so a
  cliff is a height difference that cannot be walked and a graded ramp is one
  that can;
* a **crossing discipline** where a land route may only cross water through a
  documented bridge or ferry. The crossing is an object over the water, never
  land painted onto it.

The fixtures carry their journey, manifest and loss policy as data next to the
IR instead of inside it, so no public schema, contract or campaign identity
changes.
"""

import copy
import json
import math
import runpy
from collections import deque
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# The design contract this module's fixtures must satisfy. It is reused, never
# re-implemented: tools/design/transport_journey.helper.py is the authority for
# the journey event order and the proof flags.
JOURNEY = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / "design" / "transport_journey.helper.py")
)
EVENT_ORDER = list(JOURNEY["EVENT_ORDER"])
PROOF_FLAGS = list(JOURNEY["PROOF_FLAGS"])
CAPABILITY_ID = JOURNEY["CAPABILITY_ID"]

LOSS_POLICY = (
    "destroyed carrier loses every currently boarded passenger; "
    "disembarked passengers survive independently"
)
CARGO_POLICY = "identified loadable proxies; no resource inventory claim"

# A unit occupies a disc of radius one tile; a cell is only enterable when the
# whole footprint lands on passable ground.
UNIT_FOOTPRINT_RADIUS = 1
# A graded ramp never rises more than one native level between adjacent cells.
ELEVATION_MAX_STEP = 1

FIXTURE_KINDS = (
    "loading",
    "disembarking",
    "lost-boat",
    "alternative-route",
    "impassable-cliff",
)

# Geometry authored on the 400-tile frame and scaled to the requested size with
# the same rule the large-map diagnostic uses.
CHANNEL_400 = (180, 80, 220, 320)
# The cliff is a full-height column at this x; the graded pass is a y range.
CLIFF_400 = (247,)
RAMP_400 = (190, 200)
DIRECT_ROUTE_400 = ((160, 200), (240, 200))
ALTERNATIVE_ROUTE_400 = ((160, 200), (160, 60), (240, 60), (240, 200))
EMBARK_400 = (176, 200)
CARRIER_400 = (187, 200)
LANDING_400 = (224, 200)


def scale(value_400, size):
    """Scale a 400-frame coordinate to `size`, the diagnostic's own rule."""
    return math.floor(value_400 * size / 400 + 0.5)


def scale_point(point, size):
    return (scale(point[0], size), scale(point[1], size))


def scale_rectangle(rectangle, size):
    return tuple(scale(value, size) for value in rectangle)


# --------------------------------------------------------------------------
# the dated land/water layer
# --------------------------------------------------------------------------


def build_water_layer(cells, *, layer_id, date_basis, interpretation):
    """A dated water control.

    `date_basis` names the date the control describes and `interpretation` says
    what it is and is not. The layer is the only authority on where water is;
    elevation is never consulted to derive it.
    """
    if not layer_id or not date_basis or not interpretation:
        raise ValueError("a dated water layer needs an identity, a date basis and an interpretation")
    water = frozenset((int(x), int(y)) for x, y in cells)
    return {
        "layerId": layer_id,
        "dateBasis": date_basis,
        "interpretation": interpretation,
        "waterCells": water,
    }


def layer_terrain(layer, cell, edge_distance):
    """The terrain a dated water control demands for one cell.

    The outer column is the shore, the next three are shallow water and the
    interior is deep water. A cell outside the layer keeps the base terrain.
    """
    if cell not in layer["waterCells"]:
        return None
    if edge_distance == 0:
        return "beach"
    if edge_distance <= 3:
        return "water-shallow"
    return "water-deep"


def terrain_index(tiles):
    return {(int(t["position"]["x"]), int(t["position"]["y"])): t for t in tiles}


def audit_layer_against_terrain(layer, tiles, channel):
    """The painted terrain must agree with the dated layer, and vice versa.

    A water cell painted as land is exactly the "route that crosses water
    turned into fictitious land" failure, so it is an error, not a warning.
    """
    painted = terrain_index(tiles)
    x0, y0, x1, y1 = channel
    violations = []
    for y in range(y0, y1):
        for x in range(x0, x1):
            edge = min(x - x0, x1 - 1 - x)
            required = layer_terrain(layer, (x, y), edge)
            tile = painted.get((x, y))
            actual = tile["terrain"] if tile else None
            if required != actual:
                violations.append(
                    {"cell": [x, y], "required": required, "painted": actual}
                )
    for cell in layer["waterCells"]:
        if not (x0 <= cell[0] < x1 and y0 <= cell[1] < y1):
            violations.append({"cell": list(cell), "required": None, "painted": "outside-channel"})
    return violations


# --------------------------------------------------------------------------
# footprint-aware reachability and the cliff rule
# --------------------------------------------------------------------------


@lru_cache(maxsize=None)
def footprint_cells(cell, radius=UNIT_FOOTPRINT_RADIUS):
    x, y = cell
    return frozenset(
        (x + dx, y + dy)
        for dx in range(-radius, radius + 1)
        for dy in range(-radius, radius + 1)
        if dx * dx + dy * dy <= radius * radius
    )


def elevation_of(elevation_by_cell, cell):
    return int(elevation_by_cell.get(cell, 0))


def step_allowed(elevation_by_cell, origin, target, max_step=ELEVATION_MAX_STEP):
    """A move is allowed only when the whole footprint climbs by one level."""
    origin_level = elevation_of(elevation_by_cell, origin)
    for cell in footprint_cells(target):
        if abs(elevation_of(elevation_by_cell, cell) - origin_level) > max_step:
            return False
    return True


def _blocked_by_water(water_cells):
    """Cells whose unit footprint would touch the water.

    The footprint is a disc of radius one, so a target cell is unusable when
    some water cell lies within Chebyshev distance two of it.
    """
    blocked = set()
    for x, y in water_cells:
        for dx in (-2, -1, 0, 1, 2):
            for dy in (-2, -1, 0, 1, 2):
                blocked.add((x + dx, y + dy))
    return blocked


def _footprint_levels(elevation_by_cell):
    """Kept for callers that need the levels under a footprint."""
    elevated = set()
    for (x, y), value in elevation_by_cell.items():
        if value:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    elevated.add((x + dx, y + dy))
    bounds = {}
    for cell in elevated:
        levels = [elevation_by_cell.get(f, 0) for f in footprint_cells(cell)]
        bounds[cell] = (min(levels), max(levels))
    return bounds


def reachable_cells(water_cells, elevation_by_cell, start, *, bounds, max_step=ELEVATION_MAX_STEP):
    """Cells a unit can actually walk to, honouring footprint and cliff rule.

    The footprint is a disc of radius one tile: a cell is unusable when any
    water cell lies within Chebyshev distance two of it, because the unit would
    be standing in the water. The height rule is a step rule: a move is allowed
    only when the target cell is at most one native level above or below the
    cell the unit stands on, so a cliff is a height difference that cannot be
    walked and a graded pass is one that can.

    `bounds` is the `(width, height)` of the frame. It is required, because an
    unbounded search would wander the infinite plane.
    """
    start = (int(start[0]), int(start[1]))
    if start in water_cells:
        return set()
    width, height = int(bounds[0]), int(bounds[1])
    blocked = _blocked_by_water(water_cells)
    seen = {start}
    pending = deque((start,))
    while pending:
        current = pending.popleft()
        x, y = current
        level = elevation_by_cell.get(current, 0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbour = (x + dx, y + dy)
            if not (0 <= neighbour[0] < width and 0 <= neighbour[1] < height):
                continue
            if neighbour in seen or neighbour in blocked:
                continue
            if abs(elevation_by_cell.get(neighbour, 0) - level) > max_step:
                continue
            seen.add(neighbour)
            pending.append(neighbour)
    return seen


# --------------------------------------------------------------------------
# the crossing discipline
# --------------------------------------------------------------------------


def corridor_cells(points, width_tiles):
    """The cells a corridor of the given width covers."""
    cells = set()
    for start, end in zip(points, points[1:]):
        steps = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
        for step in range(steps + 1):
            ratio = step / steps if steps else 0.0
            cx = round(start[0] + (end[0] - start[0]) * ratio)
            cy = round(start[1] + (end[1] - start[1]) * ratio)
            radius = max(0, (width_tiles - 1) // 2)
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    cells.add((cx + dx, cy + dy))
    return cells


def audit_land_route(points, width_tiles, water_cells, crossings):
    """A land route may only cross water through a documented crossing.

    A bridge is a structure over water: its cells stay water. A ferry is a
    transport segment between two shores. Anything else that puts a land route
    on a water cell is the forbidden "painted land across water".
    """
    covered = {}
    for crossing in crossings or []:
        for cell in crossing.get("cells") or []:
            covered[(int(cell[0]), int(cell[1]))] = crossing
    violations = []
    for cell in sorted(corridor_cells(points, width_tiles)):
        if cell not in water_cells:
            continue
        crossing = covered.get(cell)
        if crossing is None:
            violations.append({"cell": list(cell), "reason": "route crosses water without a documented crossing"})
        elif crossing.get("kind") == "bridge" and crossing.get("paintsLand"):
            violations.append({"cell": list(cell), "reason": "bridge paints land over the water"})
    return violations


def audit_bridge_stays_water(crossings, tiles, required_terrain=None):
    """A bridge is an object over the water; its cells keep the dated terrain.

    The dated layer decides what a cell must look like, so the check compares
    the painted terrain with the terrain the layer demands. A bridge may span
    the shore band, but it may not turn a water cell into land.
    """
    painted = terrain_index(tiles)
    violations = []
    for crossing in crossings or []:
        if crossing.get("kind") != "bridge":
            continue
        for cell in crossing.get("cells") or []:
            key = (int(cell[0]), int(cell[1]))
            tile = painted.get(key)
            terrain = tile["terrain"] if tile else None
            if required_terrain is not None:
                expected = required_terrain.get(key)
                if terrain != expected:
                    violations.append({"cell": list(cell), "required": expected, "painted": terrain})
            elif terrain not in ("water-deep", "water-shallow", "beach"):
                violations.append({"cell": list(cell), "painted": terrain})
    return violations


# --------------------------------------------------------------------------
# the performance caps the catalogue declares
# --------------------------------------------------------------------------


def catalog_perfcaps(root=ROOT):
    """The performance budget every historical mission declares.

    The 39 missions carry the same budget, so it is a project-wide cap rather
    than a per-mission measurement target.
    """
    catalog = json.loads((Path(root) / "docs/design/catalog.json").read_text(encoding="utf-8"))
    budgets = []
    for campaign in catalog["campaigns"]:
        for scenario in campaign.get("scenarios") or []:
            budget = (scenario.get("mapPlan") or {}).get("performanceBudget")
            if budget is not None:
                budgets.append(budget)
    if not budgets:
        raise ValueError("no mission declares a performance budget")
    first = budgets[0]
    for budget in budgets[1:]:
        if budget != first:
            raise ValueError("missions declare different performance budgets; the cap is ambiguous")
    return {
        "missionCount": len(budgets),
        "activeMilitaryCap": first["activeMilitaryCap"],
        "activeCivilianCap": first["activeCivilianCap"],
        "decorativeObjectsCap": first["decorativeObjectsCap"],
        "activeTriggersTargetMax": first["activeTriggersTargetMax"],
        "benchmark": first.get("benchmark") or first.get("benchmarkStatus"),
    }


def audit_perfcaps(units, triggers, decorative_objects, caps, classification):
    """Compare the authored counts with the declared caps.

    `classification` must name every unit type that appears. An unclassified
    type is refused instead of silently counted as nothing, so a cap can never
    be met by omission.
    """
    counts = {"military": 0, "civilian": 0, "other": 0}
    for unit in units:
        kind = classification.get(unit["type"])
        if kind is None:
            raise ValueError(f"unit type {unit['type']!r} has no declared perfcap class")
        if kind not in counts:
            raise ValueError(f"unknown perfcap class {kind!r}")
        counts[kind] += 1
    trigger_count = len(triggers or [])
    report = {
        "counts": {
            "activeMilitary": counts["military"],
            "activeCivilian": counts["civilian"],
            "otherUnits": counts["other"],
            "decorativeObjects": len(decorative_objects or []),
            "activeTriggers": trigger_count,
        },
        "caps": {
            "activeMilitaryCap": caps["activeMilitaryCap"],
            "activeCivilianCap": caps["activeCivilianCap"],
            "decorativeObjectsCap": caps["decorativeObjectsCap"],
            "activeTriggersTargetMax": caps["activeTriggersTargetMax"],
        },
        "benchmark": caps.get("benchmark"),
        "exceeded": [],
    }
    for key, cap_key in (
        ("activeMilitary", "activeMilitaryCap"),
        ("activeCivilian", "activeCivilianCap"),
        ("decorativeObjects", "decorativeObjectsCap"),
        ("activeTriggers", "activeTriggersTargetMax"),
    ):
        if report["counts"][key] > report["caps"][cap_key]:
            report["exceeded"].append(
                {"measure": key, "count": report["counts"][key], "cap": report["caps"][cap_key]}
            )
    report["withinCaps"] = not report["exceeded"]
    return report


# --------------------------------------------------------------------------
# the fixtures
# --------------------------------------------------------------------------


def _channel_cells(channel):
    x0, y0, x1, y1 = channel
    return [
        (x, y)
        for y in range(y0, y1)
        for x in range(x0, x1)
    ]


def _paint_channel(tiles, channel):
    """Paint the dated channel: shore, shallow water, deep water."""
    x0, y0, x1, y1 = channel
    for y in range(y0, y1):
        for x in range(x0, x1):
            edge = min(x - x0, x1 - 1 - x)
            terrain = "beach" if edge == 0 else ("water-shallow" if edge <= 3 else "water-deep")
            tiles.append({"position": {"x": x, "y": y}, "terrain": terrain, "elevation": 0})


def _paint_cliff(tiles, column_x, size, ramp=None):
    """A full-height cliff column of native level 7.

    The column spans the whole frame, so it is a barrier rather than a hill: the
    only way past it is a graded pass, where the cliff cells drop to level 1 and
    the unit can step across one level at a time.
    """
    for y in range(size):
        tiles.append({"position": {"x": column_x, "y": y}, "terrain": "grass-1", "elevation": 7})
    if ramp is not None:
        ramp_y0, ramp_y1 = ramp
        if ramp_y1 - ramp_y0 < 5:
            raise ValueError("a graded pass needs room for the unit footprint")
        tiles[:] = [
            tile
            for tile in tiles
            if not (
                tile["position"]["x"] == column_x
                and ramp_y0 <= tile["position"]["y"] <= ramp_y1
            )
        ]
        for y in range(ramp_y0, ramp_y1 + 1):
            tiles.append({"position": {"x": column_x, "y": y}, "terrain": "grass-1", "elevation": 1})


def apply_loss_policy(manifest, lost_carriers):
    """Apply the declared loss policy to a manifest.

    A destroyed carrier loses every passenger currently aboard it. A passenger
    who already disembarked survives independently.
    """
    lost = set(lost_carriers)
    survivors = []
    lost_passengers = []
    for entry in manifest:
        if entry["carrierId"] in lost and entry["state"] == "aboard":
            lost_passengers.append(entry["passengerId"])
        else:
            survivors.append(entry["passengerId"])
    return {"survivors": survivors, "lost": lost_passengers}


def build_transport_fixture(source_ir, size, kind, *, cliff_ramp=False, root=ROOT):
    """Build one adversarial transport or terrain fixture.

    Returns `(clone_ir, descriptor)`. The clone only uses the existing IR
    fields — `map.tiles`, `map.blocked`, `map.start`, `units` — so no contract
    changes. The descriptor carries the dated layer, the crossings, the journey
    and the manifest next to the IR.
    """
    if kind not in FIXTURE_KINDS:
        raise ValueError(f"unknown fixture kind {kind!r}")
    if size not in (300, 400):
        raise ValueError("only the 300 and 400 tile frames are declared")

    clone = copy.deepcopy(source_ir)
    scenario = clone["scenarios"][0]["scenario"]
    map_spec = scenario["map"]

    channel = scale_rectangle(CHANNEL_400, size)
    layer = build_water_layer(
        _channel_cells(channel),
        layer_id="synthetic-adversarial-channel",
        date_basis="synthetic diagnostic control; not a dated historical survey",
        interpretation=(
            "synthetic water control authored for an adversarial fixture; it carries "
            "no historical date, no surveyed hydrology and no ancient water claim"
        ),
    )

    tiles = []
    _paint_channel(tiles, channel)
    elevation_by_cell = {}
    cliff_column = scale(CLIFF_400[0], size)
    ramp = None
    if kind == "impassable-cliff":
        if cliff_ramp:
            ramp = (scale(RAMP_400[0], size), scale(RAMP_400[1], size))
        _paint_cliff(tiles, cliff_column, size, ramp)
        for tile in tiles:
            elevation_by_cell[(tile["position"]["x"], tile["position"]["y"])] = tile["elevation"]

    map_spec["tiles"] = tiles
    map_spec["width"] = size
    map_spec["height"] = size

    embark = scale_point(EMBARK_400, size)
    carrier = scale_point(CARRIER_400, size)
    landing = scale_point(LANDING_400, size)
    direct = [scale_point(point, size) for point in DIRECT_ROUTE_400]
    alternative = [scale_point(point, size) for point in ALTERNATIVE_ROUTE_400]

    units = []
    manifest = []
    journey = None
    crossings = []

    if kind in ("loading", "disembarking", "lost-boat"):
        units.append(
            {"id": "carrier", "faction": "player", "type": "transport-ship", "position": {"x": carrier[0], "y": carrier[1]}, "essential": False}
        )
        units.append(
            {"id": "passenger", "faction": "player", "type": "villager-male", "position": {"x": embark[0], "y": embark[1]}, "essential": False}
        )
        manifest = [
            {
                "passengerId": "passenger",
                "carrierId": "carrier",
                "state": "aboard" if kind in ("disembarking", "lost-boat") else "ashore",
            }
        ]
        if kind == "lost-boat":
            units.append(
                {"id": "disembarked-passenger", "faction": "player", "type": "villager-male", "position": {"x": landing[0], "y": landing[1]}, "essential": False}
            )
            manifest.append(
                {
                    "passengerId": "disembarked-passenger",
                    "carrierId": "carrier",
                    "state": "disembarked",
                }
            )
        journey = {
            "eventOrder": list(EVENT_ORDER),
            "proofPolicy": {flag: True for flag in PROOF_FLAGS},
            "passengerSlotsEach": 1,
            "originZone": "embark-shore",
            "destinationZone": "landing-shore",
            "capabilityId": CAPABILITY_ID,
        }
    elif kind == "alternative-route":
        crossings = []
    elif kind == "impassable-cliff":
        crossings = []

    scenario["units"] = scenario["units"] + units

    descriptor = {
        "kind": kind,
        "size": size,
        "waterLayer": {
            "layerId": layer["layerId"],
            "dateBasis": layer["dateBasis"],
            "interpretation": layer["interpretation"],
            "cellCount": len(layer["waterCells"]),
        },
        "channel": list(channel),
        "crossings": crossings,
        "manifest": manifest,
        "journey": journey,
        "lossPolicy": LOSS_POLICY,
        "cargoPolicy": CARGO_POLICY,
        "capabilityId": CAPABILITY_ID,
        "routes": {
            "direct": [list(point) for point in direct],
            "alternative": [list(point) for point in alternative],
        },
        "endpoints": {
            "embark": list(embark),
            "carrier": list(carrier),
            "landing": list(landing),
        },
        "elevationByCell": {f"{x},{y}": value for (x, y), value in elevation_by_cell.items()},
        "cliff": {
            "column": cliff_column,
            "ramp": list(ramp) if ramp else None,
            "westProbe": [cliff_column - 1, scale(200, size)],
            "eastProbe": [cliff_column + 1, scale(200, size)],
        },
        "nativeOperationStatus": "unimplemented; the adapter exposes no boarding, "
        "disembarkation or carrier-loss operation, and this fixture does not emulate one",
    }
    return clone, descriptor


def audit_fixture(clone_ir, descriptor, *, root=ROOT, include_reachability=True):
    """Run every adversarial check the fixture claims to satisfy."""
    scenario = clone_ir["scenarios"][0]["scenario"]
    tiles = scenario["map"]["tiles"]
    channel = tuple(descriptor["channel"])
    water_cells = {
        (x, y)
        for y in range(channel[1], channel[3])
        for x in range(channel[0], channel[2])
    }
    elevation_by_cell = {
        (int(key.split(",")[0]), int(key.split(",")[1])): value
        for key, value in descriptor.get("elevationByCell", {}).items()
    }

    findings = {}
    layer = build_water_layer(
        water_cells,
        layer_id=descriptor["waterLayer"]["layerId"],
        date_basis=descriptor["waterLayer"]["dateBasis"],
        interpretation=descriptor["waterLayer"]["interpretation"],
    )
    findings["layerAgreesWithTerrain"] = audit_layer_against_terrain(layer, tiles, channel)
    required_terrain = {
        cell: layer_terrain(layer, cell, min(cell[0] - channel[0], channel[2] - 1 - cell[0]))
        for cell in water_cells
    }
    findings["directRouteViolations"] = audit_land_route(
        [tuple(point) for point in descriptor["routes"]["direct"]],
        4,
        water_cells,
        descriptor["crossings"],
    )
    findings["alternativeRouteViolations"] = audit_land_route(
        [tuple(point) for point in descriptor["routes"]["alternative"]],
        4,
        water_cells,
        descriptor["crossings"],
    )
    findings["bridgePaintedLand"] = audit_bridge_stays_water(
        descriptor["crossings"], tiles, required_terrain
    )

    if include_reachability:
        frame = (scenario["map"]["width"], scenario["map"]["height"])
        reachable = reachable_cells(
            water_cells, elevation_by_cell, descriptor["endpoints"]["embark"], bounds=frame
        )
        findings["embarkReachableCellCount"] = len(reachable)
        findings["landingReachableFromWest"] = tuple(descriptor["endpoints"]["landing"]) in reachable
        # The unit may not step into the channel at all: the direct crossing is
        # impossible, and only the land detour around it reaches the far bank.
        shore_band = {
            (channel[0], y) for y in range(channel[1], channel[3])
        }
        findings["channelEntryReachable"] = bool(reachable & shore_band)
        findings["eastBankReachableFromWest"] = bool(
            reachable & {(x, y) for x in range(channel[2], channel[2] + 8) for y in range(channel[1], channel[3])}
        )
        cliff = descriptor.get("cliff") or {}
        if cliff:
            findings["cliffWestProbeReachable"] = tuple(cliff["westProbe"]) in reachable
            findings["cliffEastProbeReachable"] = tuple(cliff["eastProbe"]) in reachable

    caps = catalog_perfcaps(root)
    classification = {
        "militia": "military",
        "villager-male": "civilian",
        "villager-female": "civilian",
        "transport-ship": "other",
    }
    findings["perfcaps"] = audit_perfcaps(
        scenario["units"],
        scenario.get("triggers") or [],
        scenario["map"].get("blocked") or [],
        caps,
        classification,
    )
    return findings
