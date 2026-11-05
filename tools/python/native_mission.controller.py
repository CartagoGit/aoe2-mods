"""Shared bounded runtime primitives for native civilian missions."""

import math
import runpy
from pathlib import Path

from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.trigger_lists import Comparison, ObjectAttribute, Operation

HERE = Path(__file__).resolve().parent


def _load(name):
    return runpy.run_path(str(HERE / name))


class NativeMissionController:
    """Own common native variables, XS names, spatial bindings and UI helpers."""

    def __init__(
        self,
        scenario,
        units,
        dossier,
        binding,
        locale,
        *,
        init_trigger_name="cdf-delivery-initialize",
        function_prefix="cdf_delivery",
        action_prefix="cdf_delivery_action",
    ):
        self.scenario, self.units, self.dossier, self.binding, self.locale = (
            scenario,
            units,
            dossier,
            binding,
            locale,
        )
        self.function_prefix = function_prefix
        self.action_prefix = action_prefix
        self.tm = scenario.trigger_manager
        self.spatial = _load("native_spatial.helper.py")
        self.transactions = _load("native_transactions.helper.py")
        self.variables, self.xs, self.names = {}, [], 0
        self.semantic_variables = {}
        self.init = self.tm.add_trigger(init_trigger_name, enabled=True, looping=False)
        self.ready = self.variable("ready")
        self.phase = self.variable("phase")
        self.terminal = self.variable("terminal")
        self.busy = self.variable("caption-busy")
        self.entities, self.zones = {}, {}
        self.handles, self.alive, self.reserve = {}, {}, {}
        self.screens = {}

    def load(self, name):
        return _load(name)

    def initialize_originals_and_reserves(self):
        self.entities = {e["id"]: e for e in self.binding["entities"]}
        self.zones = {z["id"]: z for z in self.binding["zones"]}
        for i, entity in enumerate(self.binding["entities"]):
            entity_id = entity["id"]
            self.handles[entity_id] = self.variable(f"handle-{i}", self.units[entity_id])
            self.alive[entity_id] = self.function(
                self.spatial["render_unit_alive_predicate"],
                self.handles[entity_id],
                entity["player"],
            )
            self.init.new_effect.change_object_name(
                selected_object_ids=self.units[entity_id], message=entity["label"][self.locale]
            )
        # Parser 0.9.6 loses zero float quantities when reopening MODIFY_ATTRIBUTE.
        # Use the documented native XS SetAttribute operation, with dataset IDs,
        # instead of changing the dependency or accepting a lossy round-trip.
        work_calls = [
            f"    xsEffectAmount(cSetAttribute, {unit.ID}, {int(ObjectAttribute.WORK_RATE)}, 0.0, 1);"
            for unit in UnitInfo
            if unit.name.startswith("VILLAGER_")
        ]
        self.call(self.init, "\n".join(work_calls))
        self.reserve = {
            r: self.variable("optional-reserve-" + r, q)
            for r, q in self.dossier["secondaryBudget"]["reservedRewards"].items()
        }
        self.screens = {screen["id"]: screen for screen in self.dossier["screens"]}

    def variable(self, name, value=0):
        if name in self.variables:
            raise ValueError("duplicate native variable role: " + name)
        variable = self.tm.add_variable("cdf-" + name).variable_id
        self.variables[name] = variable
        self.set(self.init, variable, value)
        return variable

    @staticmethod
    def set(trigger, variable, value):
        trigger.new_effect.change_variable(
            variable=variable, quantity=value, operation=Operation.SET
        )

    @staticmethod
    def equal(trigger, variable, value):
        trigger.new_condition.variable_value(
            variable=variable, quantity=value, comparison=Comparison.EQUAL
        )

    def trigger(self, name, terminal=0, phase=None, looping=False):
        result = self.tm.add_trigger("cdf-" + name, enabled=True, looping=looping)
        self.equal(result, self.ready, 1)
        self.equal(result, self.terminal, terminal)
        if phase is not None:
            self.equal(result, self.phase, phase)
        return result

    def function(self, renderer, *args):
        self.names += 1
        name = f"{self.function_prefix}_{self.names}"
        self.xs.append(renderer(name, *args))
        return name

    def expression(self, expression):
        return self.function(
            lambda name: f"bool {name}() {{\n    return ({expression});\n}}"
        )

    def in_zone(self, entity, zone):
        z = self.zones[zone]
        return self.function(
            self.spatial["render_unit_circle_predicate"],
            self.handles[entity],
            self.entities[entity]["player"],
            *z["centre"],
            z["radius"],
            self.binding["map"]["size"],
        )

    def condition(self, trigger, function):
        trigger.new_condition.script_call(xs_function=function)

    def call(self, trigger, source):
        self.names += 1
        name = f"{self.action_prefix}_{self.names}"
        self.xs.append("void " + name + "() {\n" + source + "\n}")
        trigger.new_effect.script_call(message=name + "();")

    def captions(self, name, keys, gate, expected, terminal=0, extra_text=()):
        """One global caption slot; release always clears it, even after terminal."""
        parts = []
        for key in keys:
            screen = self.screens[key]
            speaker = screen["narrator"]
            labels = self.binding["narration"]["speakerLabels"]
            if speaker != "none" and speaker not in labels:
                raise ValueError("native caption requires a localized speaker label")
            prefix = labels[speaker][self.locale] + ": " if speaker != "none" else ""
            for text in screen["captionSegments"][self.locale]:
                parts.append(prefix + text)
        parts.extend(extra_text)
        previous = None
        for i, text in enumerate(parts):
            done = self.variable(f"{name}-caption-{i}")
            show = self.trigger(f"{name}-caption-{i}", terminal=terminal)
            self.equal(show, gate, expected)
            self.equal(show, self.busy, 0)
            if terminal == 0 and name != "intro":
                show.new_condition.variable_value(
                    variable=self.phase, quantity=0, comparison=Comparison.LARGER
                )
            if previous is not None:
                self.equal(show, previous, 1)
            duration = max(3, math.ceil(len(text.split()) / 2.5))
            self.set(show, self.busy, 1)
            show.new_effect.display_instructions(
                source_player=1,
                message=text,
                display_time=duration,
                instruction_panel_position=0,
            )
            release = self.tm.add_trigger(
                f"cdf-{name}-release-{i}", enabled=False, looping=False
            )
            release.new_condition.timer(timer=duration)
            self.set(release, self.busy, 0)
            self.set(release, done, 1)
            show.new_effect.activate_trigger(trigger_id=release.trigger_id)
            previous = done
        return previous

    def advance_after(self, name, done, next_phase, terminal=0):
        advance = self.trigger(name, terminal=terminal)
        self.equal(advance, done, 1)
        self.set(advance, self.phase, next_phase)
        return advance

    @staticmethod
    def objective_ui(trigger, text, order, optional=False):
        trigger.display_as_objective = True
        trigger.description = text
        trigger.short_description = text
        trigger.description_order = order
        trigger.display_on_screen = not optional

    def finish(self):
        self.set(self.init, self.ready, 1)
        source = "\n\n".join(self.xs)
        self.scenario.xs_manager.add_script(xs_string=source)
        self.scenario.xs_manager.validate(xs=source)
        return {
            "variables": dict(self.variables),
            "semanticFlags": dict(self.semantic_variables),
            "nativeOriginalHandles": dict(self.units),
            "xsSource": source,
            "gameVerified": False,
        }
