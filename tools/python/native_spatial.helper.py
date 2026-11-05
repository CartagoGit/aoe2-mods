"""Render read-only XS predicates over original unit IDs.

These strings are native XS source, not an IR contract or proof of runtime behavior.
"""

import math
import re
from decimal import Decimal


_MAX_HANDLE = 2_147_483_647
_MAX_MAP_SIZE = 480
_FUNCTION_NAME = re.compile(r"cdf_[A-Za-z0-9_]*\Z", re.ASCII)


def _function_name(value):
    if not isinstance(value, str) or not value.isascii() or _FUNCTION_NAME.fullmatch(value) is None:
        raise ValueError("function_name must start with cdf_ and contain only ASCII letters, digits, or underscore")
    return value


def _exact_integer(value, name, minimum, maximum):
    if type(value) is not int:
        raise TypeError(f"{name} must be an exact integer")
    if value < minimum or value > maximum:
        raise ValueError(f"{name} must be in {minimum}..{maximum}")
    return value


def _finite_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a finite non-boolean number")
    try:
        result = float(value)
    except OverflowError as error:
        raise ValueError(f"{name} must be finite") from error
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


def _xs_float(value):
    literal = format(Decimal(format(value, ".17g")), "f")
    if "." in literal:
        literal = literal.rstrip("0").rstrip(".")
    if "." not in literal:
        literal += ".0"
    return literal


def _unit_identity_lines(handle_variable, player):
    lines = [
        f"    int cdf_unit_id = xsTriggerVariable({handle_variable});",
        "    if (cdf_unit_id < 0) {",
        "        return (false);",
        "    }",
        "    if (xsDoesUnitExist(cdf_unit_id) == false) {",
        "        return (false);",
        "    }",
        "    if (xsGetUnitHitpoints(cdf_unit_id) <= 0.0) {",
        "        return (false);",
        "    }",
    ]
    if player == 0:
        lines.extend([
            "    if (xsGetUnitOwner(cdf_unit_id) != 0) {",
            "        return (false);",
            "    }",
        ])
    else:
        lines.extend([
            f"    int cdf_expected_owner = xsGetWorldPlayerId({player});",
            "    if (xsGetUnitOwner(cdf_unit_id) != cdf_expected_owner) {",
            "        return (false);",
            "    }",
        ])
    return lines


def render_unit_alive_predicate(function_name, handle_variable, player):
    """Return a pure XS bool function for an alive original unit owned by a player."""
    name = _function_name(function_name)
    variable = _exact_integer(handle_variable, "handle_variable", 0, _MAX_HANDLE)
    owner = _exact_integer(player, "player", 0, 8)
    lines = [f"bool {name}() {{"]
    lines.extend(_unit_identity_lines(variable, owner))
    lines.extend(["    return (true);", "}"])
    return "\n".join(lines)


def render_unit_circle_predicate(function_name, handle_variable, player, x, y, radius, map_size):
    """Return a pure XS bool function for an alive, ungarrisoned unit in a true circle."""
    name = _function_name(function_name)
    variable = _exact_integer(handle_variable, "handle_variable", 0, _MAX_HANDLE)
    owner = _exact_integer(player, "player", 0, 8)
    size = _exact_integer(map_size, "map_size", 1, _MAX_MAP_SIZE)
    center_x = _finite_number(x, "x")
    center_y = _finite_number(y, "y")
    circle_radius = _finite_number(radius, "radius")
    if not 0.0 <= center_x < size or not 0.0 <= center_y < size:
        raise ValueError("circle center must be inside the map")
    if circle_radius <= 0.0 or circle_radius > size:
        raise ValueError("radius must be greater than zero and no larger than map_size")
    if (center_x - circle_radius < 0.0 or center_y - circle_radius < 0.0
            or center_x + circle_radius > size or center_y + circle_radius > size):
        raise ValueError("entire circle must fit inside the map")

    radius_squared = circle_radius * circle_radius
    lines = [f"bool {name}() {{"]
    lines.extend(_unit_identity_lines(variable, owner))
    lines.extend([
        "    if (xsGetGarrisonedInUnitId(cdf_unit_id) >= 0) {",
        "        return (false);",
        "    }",
        "    vector cdf_unit_position = xsGetUnitPosition(cdf_unit_id);",
        f"    float cdf_dx = xsVectorGetX(cdf_unit_position) - {_xs_float(center_x)};",
        f"    float cdf_dy = xsVectorGetY(cdf_unit_position) - {_xs_float(center_y)};",
        f"    return ((cdf_dx * cdf_dx + cdf_dy * cdf_dy) <= {_xs_float(radius_squared)});",
        "}",
    ])
    return "\n".join(lines)


__all__ = ["render_unit_alive_predicate", "render_unit_circle_predicate"]
