"""Shared private household base envelope factory.

The labelled synthetic fixture and the private geographic preview need the
same native v1 envelope: one square map, the two factions with their finite
reserves, the original bodies on the floor(design)+0.5 native centres and the
player's start. Only the artifact identifier, the frame and the terrain change
between them, so the construction lives here once and the second caller
cannot copy the first.

This module owns no household semantics: the ledger, the payment circuit, the
narration, the terrain and the exporter stay where they are. The caller
supplies the binding, the dossier, the difficulty level and the explicit
artifact scenario identifier, and receives the same envelope shape the shared
native base factory already accepts.

The native height convention is the existing one: the frame's integer sample
index[i,j] is the native tile[i,j], and a body design position snaps to
floor(design)+0.5. The zone centres stay continuous.
"""

import math

BASE_TERRAIN = "grass-1"
FACTIONS = (("player", 1, "human"), ("local", 2, "ally"))
NATIVE_LEVEL_MIN = 0
NATIVE_LEVEL_MAX = 7


def build_factions(stocks):
    """The two private factions with their finite reserves.

    Only the human player holds the authored stock; the ally starts empty.
    The reserve model is the existing finite-reserve contract and is not
    widened here.
    """
    return [
        {
            "id": name,
            "player": player,
            "civilization": "byzantines",
            "role": role,
            "economy": {
                "model": "finite-reserve",
                "initial": stocks if player == 1 else dict.fromkeys(stocks, 0),
            },
        }
        for name, player, role in FACTIONS
    ]


def build_native_units(binding):
    """The original bodies and the design-identifier to native-identifier map.

    The native centre of a body is floor(design)+0.5, the convention the
    shared base factory already applies, so the design position and the
    native centre are recorded separately by the caller.
    """
    native_units = []
    mapping = {}
    for index, entity in enumerate(binding["entities"]):
        key = f"original-{index}"
        mapping[entity["id"]] = key
        x, y = map(math.floor, entity["position"])
        native_units.append(
            {
                "id": key,
                "faction": "player" if entity["player"] == 1 else "local",
                "type": entity["unitType"],
                "position": {"x": x, "y": y},
                "essential": False,
            }
        )
    return native_units, mapping


def build_private_household_base(
    binding,
    dossier,
    level,
    *,
    scenario_id,
    size=None,
    base_terrain=BASE_TERRAIN,
    tiles=None,
):
    """Construct the explicit v1 base envelope of one private artifact.

    `scenario_id` is mandatory: an artifact without an explicit identifier
    cannot be told apart from another one in a receipt or on disk.
    """
    if not isinstance(scenario_id, str) or not scenario_id.strip():
        raise ValueError("a private artifact needs an explicit scenario identifier")
    map_size = binding["map"]["size"] if size is None else size
    if type(map_size) is not int or map_size <= 0:
        raise ValueError("the native map size must be a positive integer")
    stocks = dossier["difficulty"][level]["startingResources"]
    factions = build_factions(stocks)
    native_units, mapping = build_native_units(binding)
    start = next(
        unit["position"]
        for unit in native_units
        if unit["id"] == mapping[binding["households"]["entities"][0]]
    )
    base = {
        "schemaVersion": 1,
        "scenario": {
            "id": scenario_id,
            "map": {
                "width": map_size,
                "height": map_size,
                "baseTerrain": base_terrain,
                "tiles": list(tiles or []),
                "blocked": [],
                "start": start,
            },
            "factions": factions,
            "units": native_units,
            "technologies": [],
        },
    }
    return base, mapping


def native_centre(position):
    """The native centre of a design position: floor(design)+0.5."""
    return (math.floor(position[0]) + 0.5, math.floor(position[1]) + 0.5)


def native_tile(centre):
    """The native tile that holds a native centre.

    The frame's integer sample index[i,j] is the native tile[i,j], so the
    tile of a native centre is floor(centre). Rounding the design position
    instead of flooring the native centre can select another row.
    """
    return (math.floor(centre[0]), math.floor(centre[1]))
