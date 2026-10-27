"""Compare native scenarios through the shared serialization signature.

The signature covers the fields this prototype's scenarios actually carry:
declared terrain, native object identity and type, IEEE float32 positions,
variables, player economy and diplomacy, options, message and text IDs,
embedded XS and the existing trigger, condition and effect fields. It is not
a signature of every possible AoE2 field, and it never proves game execution.
"""

import struct


def native_signature(scenario):
    """Fields that carry this prototype's actual world, conditions and effects."""
    condition_fields = (
        "condition_type",
        "quantity",
        "variable",
        "comparison",
        "unit_object",
        "timer",
        "xs_function",
        "source_player",
        "attribute",
    )
    effect_fields = (
        "effect_type",
        "quantity",
        "variable",
        "operation",
        "source_player",
        "enabled",
        "trigger_id",
        "message",
        "display_time",
        "selected_object_ids",
        "object_attributes",
        "object_list_unit_id",
        "location_x",
        "location_y",
    )
    return {
        "terrain": [(t.terrain_id, t.elevation) for t in scenario.map_manager.terrain],
        "units": [
            (
                u.reference_id,
                u.unit_const,
                u.player,
                struct.unpack("<f", struct.pack("<f", u.x))[0],
                struct.unpack("<f", struct.pack("<f", u.y))[0],
            )
            for u in scenario.unit_manager.get_all_units()
        ],
        "variables": [
            (v.variable_id, v.name) for v in scenario.trigger_manager.variables
        ],
        "players": [
            (
                i,
                p.human,
                p.civilization,
                p.food,
                p.wood,
                p.gold,
                p.stone,
                p.disabled_buildings,
                p.disabled_units,
                p.disabled_techs,
                list(p.diplomacy),
            )
            for i, p in enumerate(scenario.player_manager.players)
            if i in (1, 2)
        ],
        "options": (
            scenario.option_manager.victory_condition,
            scenario.option_manager.victory_custom_conditions_required,
            scenario.option_manager.lock_teams,
            scenario.option_manager.allow_players_choose_teams,
        ),
        "messages": [
            (
                f,
                getattr(scenario.message_manager, f),
                getattr(scenario.message_manager, f + "_string_table_id"),
            )
            for f in ("instructions", "hints", "history", "victory", "loss")
        ],
        "xs": scenario.xs_manager._get_scenario_xs(),
        "triggers": [
            (
                t.name,
                t.enabled,
                t.looping,
                t.description,
                t.short_description,
                t.display_as_objective,
                t.display_on_screen,
                t.description_order,
                [[getattr(c, f, None) for f in condition_fields] for c in t.conditions],
                [[getattr(e, f, None) for f in effect_fields] for e in t.effects],
            )
            for t in scenario.trigger_manager.triggers
        ],
    }
