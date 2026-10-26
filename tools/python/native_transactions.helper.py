"""Render guarded, single-invocation XS resource transactions.

This module emits native XS source. Parsing it does not establish runtime
atomicity or prove behavior in AoE2; these functions contain no yield points.
"""

import re

from AoE2ScenarioParser.datasets.trigger_lists import Attribute


_FUNCTION_NAME = re.compile(r"cdf_[A-Za-z0-9_]*\Z", re.ASCII)
_MAX_VARIABLE_ID = 65_535
_MAX_AMOUNT = 1_000_000_000
_RESOURCE_ORDER = ("food", "wood", "gold", "stone")
_RESOURCE_ATTRIBUTES = {
    "food": Attribute.FOOD_STORAGE,
    "wood": Attribute.WOOD_STORAGE,
    "gold": Attribute.GOLD_STORAGE,
    "stone": Attribute.STONE_STORAGE,
}


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


def _variable_id(value, name):
    return _exact_integer(value, name, 0, _MAX_VARIABLE_ID)


def _player(value):
    return _exact_integer(value, "player", 1, 8)


def _amounts(value):
    if type(value) is not dict:
        raise TypeError("amounts must be a dict keyed by native resource name")
    result = {}
    for resource, amount in value.items():
        if type(resource) is not str or resource not in _RESOURCE_ATTRIBUTES:
            raise ValueError(f"unsupported resource: {resource!r}")
        result[resource] = _exact_integer(amount, f"amounts[{resource!r}]", 0, _MAX_AMOUNT)
    return result


def _required_flags(value):
    if value is None:
        return {}
    if type(value) is not dict:
        raise TypeError("required_flags must map trigger-variable IDs to exact integer values")
    flags = {}
    for variable, expected in value.items():
        expected = _exact_integer(expected, f"required_flags[{variable!r}]", -(2**31), 2**31 - 1)
        flags[_variable_id(variable, "required flag variable")] = expected
    return flags


def _distinct_roles(*roles):
    seen = {}
    for label, variable in roles:
        if variable in seen:
            raise ValueError(f"trigger-variable alias: {label} and {seen[variable]} both use {variable}")
        seen[variable] = label


def _resource_attribute(resource):
    # Resolve each ID through the pinned parser enum rather than repeating
    # engine numbers in this renderer.
    return int(_RESOURCE_ATTRIBUTES[resource].value)


def _stock_local(resource):
    return f"cdf_stock_{resource}"


def _reserve_local(resource):
    return f"cdf_reserve_{resource}"


def _header(name):
    return [f"bool {name}() {{"]


def _flag_guards(flags):
    return [
        [
            f"    if (xsTriggerVariable({variable}) != {expected}) {{",
            "        return (false);",
            "    }",
        ]
        for variable, expected in sorted(flags.items())
    ]


def render_payment_function(function_name, player, amounts, receipt_variable, required_flags=None):
    """Return XS that validates all inputs and stock before a one-time debit."""
    name = _function_name(function_name)
    owner = _player(player)
    costs = _amounts(amounts)
    receipt = _variable_id(receipt_variable, "receipt_variable")
    flags = _required_flags(required_flags)
    _distinct_roles(("receipt", receipt), *((f"flag {key}", key) for key in flags))

    lines = _header(name)
    lines.extend([
        f"    if (xsTriggerVariable({receipt}) != 0) {{",
        "        return (false);",
        "    }",
    ])
    for guard in _flag_guards(flags):
        lines.extend(guard)

    resources = [(resource, costs[resource]) for resource in _RESOURCE_ORDER if resource in costs]
    for resource, amount in resources:
        if amount == 0:
            continue
        lines.append(
            f"    float {_stock_local(resource)} = xsPlayerAttribute({owner}, {_resource_attribute(resource)});"
        )
        lines.extend([
            f"    if ({_stock_local(resource)} < {amount}) {{",
            "        return (false);",
            "    }",
        ])

    # All guards and stock checks precede the first mutation.
    for resource, amount in resources:
        if amount == 0:
            continue
        lines.append(
            f"    xsSetPlayerAttribute({owner}, {_resource_attribute(resource)}, {_stock_local(resource)} - {amount});"
        )
    lines.extend([
        f"    xsSetTriggerVariable({receipt}, 1);",
        "    return (true);",
        "}",
    ])
    return "\n".join(lines)


def render_reward_function(function_name, player, amounts, reserve_variables,
                           completion_variable, required_flags=None):
    """Return XS that atomically consumes named reserves and grants resources once."""
    name = _function_name(function_name)
    owner = _player(player)
    rewards = _amounts(amounts)
    if type(reserve_variables) is not dict:
        raise TypeError("reserve_variables must map native resource names to trigger-variable IDs")
    reserves = {}
    for resource, variable in reserve_variables.items():
        if type(resource) is not str or resource not in _RESOURCE_ATTRIBUTES:
            raise ValueError(f"unsupported reserve resource: {resource!r}")
        reserves[resource] = _variable_id(variable, f"reserve_variables[{resource!r}]")
    if set(reserves) != set(rewards):
        raise ValueError("reserve_variables must have exactly the same resource keys as amounts")

    completion = _variable_id(completion_variable, "completion_variable")
    flags = _required_flags(required_flags)
    roles = [("completion", completion)]
    roles.extend((f"reserve {resource}", variable) for resource, variable in reserves.items())
    roles.extend((f"flag {key}", key) for key in flags)
    _distinct_roles(*roles)

    lines = _header(name)
    lines.extend([
        f"    if (xsTriggerVariable({completion}) != 0) {{",
        "        return (false);",
        "    }",
    ])
    for guard in _flag_guards(flags):
        lines.extend(guard)

    resources = [(resource, rewards[resource], reserves[resource])
                 for resource in _RESOURCE_ORDER if resource in rewards]
    for resource, amount, variable in resources:
        if amount == 0:
            continue
        lines.append(f"    int {_reserve_local(resource)} = xsTriggerVariable({variable});")
        lines.extend([
            f"    if ({_reserve_local(resource)} < {amount}) {{",
            "        return (false);",
            "    }",
        ])

    # Snapshot the destination balances before the first mutation. All reserve
    # checks and snapshots complete before reserves or native stock are changed.
    for resource, amount, _variable in resources:
        if amount == 0:
            continue
        lines.append(
            f"    float {_stock_local(resource)} = xsPlayerAttribute({owner}, {_resource_attribute(resource)});"
        )

    for resource, amount, variable in resources:
        if amount == 0:
            continue
        lines.append(
            f"    xsSetTriggerVariable({variable}, {_reserve_local(resource)} - {amount});"
        )
    for resource, amount, _variable in resources:
        if amount == 0:
            continue
        lines.append(
            f"    xsSetPlayerAttribute({owner}, {_resource_attribute(resource)}, {_stock_local(resource)} + {amount});"
        )
    lines.extend([
        f"    xsSetTriggerVariable({completion}, 1);",
        "    return (true);",
        "}",
    ])
    return "\n".join(lines)


__all__ = ["render_payment_function", "render_reward_function"]
