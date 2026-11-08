"""Render localized, nonblocking annotations for authored receiving zones.

These flags and revealers are auxiliary UI markers. They do not alter terrain,
original actors, receiving geometry, controller state or gameplay semantics.
"""

import math


LABEL_TRIGGER_PREFIX = "cdf-label-"
SUPPORTED_LOCALES = ("en", "es-ES")


def _prepare_zones(scenario, zones, locale):
    if locale not in SUPPORTED_LOCALES:
        raise ValueError("unsupported receiving-wayfinding locale")
    if not isinstance(zones, (list, tuple)) or not zones:
        raise ValueError("receiving wayfinding requires at least one authored zone")

    size = scenario.map_manager.map_size
    if type(size) is not int or size <= 0:
        raise ValueError("receiving wayfinding requires a valid square map frame")

    existing_names = {
        trigger.name for trigger in scenario.trigger_manager.triggers
    }
    prepared = []
    seen_ids = set()
    seen_trigger_names = set()
    for zone in zones:
        if not isinstance(zone, dict):
            raise ValueError("receiving zone must be an authored object")
        zone_id = zone.get("id")
        if not isinstance(zone_id, str) or not zone_id.strip():
            raise ValueError("receiving zone needs a nonempty semantic id")
        if zone_id in seen_ids:
            raise ValueError("duplicate receiving zone id")
        seen_ids.add(zone_id)

        trigger_name = LABEL_TRIGGER_PREFIX + zone_id
        if trigger_name in seen_trigger_names or trigger_name in existing_names:
            raise ValueError("duplicate receiving-zone label trigger name")
        seen_trigger_names.add(trigger_name)

        centre = zone.get("centre")
        if not isinstance(centre, (list, tuple)) or len(centre) != 2:
            raise ValueError("receiving zone needs a two-coordinate centre")
        x, y = centre
        if (
            type(x) not in (int, float)
            or type(y) not in (int, float)
            or not math.isfinite(x)
            or not math.isfinite(y)
            or x < 0
            or y < 0
            or x >= size
            or y >= size
        ):
            raise ValueError("receiving zone centre must be finite and inside the map")

        radius = zone.get("radius")
        if (
            type(radius) not in (int, float)
            or not math.isfinite(radius)
            or radius <= 0
            or x - radius < 0
            or y - radius < 0
            or x + radius >= size
            or y + radius >= size
        ):
            raise ValueError("receiving zone radius must be positive and fit inside the map")

        labels = zone.get("label")
        label = labels.get(locale) if isinstance(labels, dict) else None
        if not isinstance(label, str) or not label.strip():
            raise ValueError("receiving zone lacks a nonempty label for the requested locale")

        prepared.append(
            {
                "zoneId": zone_id,
                "centre": [x, y],
                "radius": radius,
                "label": label,
                "triggerName": trigger_name,
            }
        )
    return prepared


def render_receiving_wayfinding(scenario, zones, locale):
    """Add a FLAG_A, localized name trigger and MAP_REVEALER per zone.

    The complete input and all names are validated before the first native
    write. The returned provenance contains the exact object references that
    the parser assigned, without classifying those objects as source actors.
    """
    prepared = _prepare_zones(scenario, zones, locale)

    from AoE2ScenarioParser.datasets.other import OtherInfo

    flag_type = OtherInfo.FLAG_A.ID
    revealer_type = OtherInfo.MAP_REVEALER.ID
    if type(flag_type) is not int or type(revealer_type) is not int:
        raise ValueError("receiving wayfinding marker types are unavailable")

    provenance = []
    for zone in prepared:
        x, y = zone["centre"]
        flag = scenario.unit_manager.add_unit(
            player=1, unit_const=flag_type, x=x, y=y
        )
        label_trigger = scenario.trigger_manager.add_trigger(
            zone["triggerName"], enabled=True, looping=False
        )
        label_trigger.new_effect.change_object_name(
            selected_object_ids=flag.reference_id,
            message=zone["label"],
        )
        revealer = scenario.unit_manager.add_unit(
            player=1, unit_const=revealer_type, x=x, y=y
        )
        provenance.append(
            {
                "kind": "private-receiving-wayfinding-annotation",
                "zoneId": zone["zoneId"],
                "locale": locale,
                "centre": list(zone["centre"]),
                "radius": zone["radius"],
                "label": zone["label"],
                "labelTriggerName": zone["triggerName"],
                "flagReferenceId": flag.reference_id,
                "revealerReferenceId": revealer.reference_id,
            }
        )
    return provenance
