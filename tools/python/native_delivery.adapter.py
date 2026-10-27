"""Bounded native civilian-delivery prototype, separate from the public IR exporter.

Only the explicit three-stage collection / paid copy / original delivery shape
is accepted. This does not enable composed v2/v3 export. Physical bindings and
historical source approval remain separate from native serialization evidence.
"""

import math
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
_NATIVE_MISSION = runpy.run_path(str(HERE / "native_mission.controller.py"))
NativeMissionController = _NATIVE_MISSION["NativeMissionController"]


def validate_delivery_contract(dossier, binding):
    """Reject unsupported contracts before constructing a native scenario."""
    if (
        binding.get("kind") != "private-historical-episode-native-binding"
        or type(binding.get("schemaVersion")) is not int
        or binding["schemaVersion"] != 1
    ):
        raise ValueError("unsupported native delivery binding")
    if dossier["id"] != binding["episodeId"]:
        raise ValueError("delivery binding episode mismatch")
    objectives = dossier["objectivePlan"]
    if [o["id"] for o in objectives] != ["o1", "o2", "o3"]:
        raise ValueError("unsupported delivery objective graph")
    if [o["after"] for o in objectives] != [[], ["o1"], ["o2"]]:
        raise ValueError("unsupported delivery prerequisites")
    if (
        dossier["worldContract"]["survivorGroups"]
        or dossier["stateMachine"].get("campaignProgressWrite") is not False
    ):
        raise ValueError("unsupported survivor/progress contract")
    if [o["phase"] for o in objectives] != ["phase-1", "phase-2", "phase-3"]:
        raise ValueError("unsupported delivery phases")
    if any(
        o["predicate"]["operator"] != "all"
        or o["predicate"].get("neverUseTimerInstead") is not True
        for o in objectives
    ):
        raise ValueError("native delivery supports only all predicates")
    expected_transitions = [
        {"from": "briefing", "to": "phase-1", "on": "intro-accepted"},
        *[
            {
                "from": f"phase-{i}",
                "to": f"phase-{i + 1}" if i < 3 else "victory",
                "on": "objective-latched",
                "objectiveId": f"o{i}",
            }
            for i in (1, 2, 3)
        ],
    ]
    if dossier["stateMachine"]["phaseTransitions"] != expected_transitions:
        raise ValueError("unsupported native phase transitions")
    if (
        dossier["stateMachine"]["terminalPriority"]
        != "defeat first; close side rewards; one terminal latch"
    ):
        raise ValueError("unsupported native terminal priority")
    requirements = [o["predicate"]["requirements"] for o in objectives]
    if [[r["kind"] for r in rows] for rows in requirements] != [
        ["entity-state"],
        ["resource-transaction", "derived-token", "entity-state"],
        ["entity-state"],
    ]:
        raise ValueError(
            "unsupported delivery operations; physical copying arrival must be authored"
        )
    collect, (payment, derive, court), deliver = (
        requirements[0][0],
        requirements[1],
        requirements[2][0],
    )
    originals = binding["collection"]["entities"]
    output = binding["copying"]["outputEntity"]
    if (
        binding["copying"]["inputEntities"] != originals
        or binding["delivery"]["entity"] != output
    ):
        raise ValueError("inconsistent native provenance binding")
    if (
        len(originals) != 3
        or len(set(originals)) != 3
        or collect.get("state") != "collected"
        or collect.get("entities") != originals
        or collect.get("requiredCount") != 3
        or court.get("state") != "arrived"
        or court.get("entities") != originals
        or court.get("requiredCount") != 3
        or court.get("destinations")
        != dict.fromkeys(originals, binding["copying"]["zone"])
        or payment.get("amounts") != binding["copying"]["cost"]
        or payment.get("account") != "spendable"
        or payment.get("receivingZones") != [binding["copying"]["zone"]]
        or derive.get("inputEntities") != originals
        or derive.get("outputEntities") != [output]
        or deliver.get("state") != "arrived"
        or deliver.get("entities") != [output]
        or deliver.get("requiredCount") != 1
        or deliver.get("destinations") != {output: binding["delivery"]["zone"]}
    ):
        raise ValueError("native delivery source/binding contract mismatch")
    if [[r.get("id") for r in rows] for rows in requirements] != [
        ["req-1"],
        ["req-1", "req-2", "req-3"],
        ["req-1"],
    ]:
        raise ValueError("unsupported delivery requirement identity")
    if (
        any(r.get("oncePerEntity") is not True for r in (collect, court, deliver))
        or payment.get("atomic") is not True
        or payment.get("once") is not True
    ):
        raise ValueError("unsupported repeatable main transaction")
    if payment.get("allocations") != {
        binding["copying"]["zone"]: binding["copying"]["cost"]
    }:
        raise ValueError("payment allocation mismatch")
    if any(type(r.get("requiredCount")) is not int for r in (collect, court, deliver)):
        raise ValueError("main counts must be exact integers")
    receipts = derive.get("requiredPaymentReceipts", [])
    if (
        len(receipts) != 1
        or receipts[0].get("newDebit") is not False
        or receipts[0]
        != {
            "flag": payment["paidFlag"],
            "fromObjective": "o2",
            "amounts": payment["amounts"],
            "newDebit": False,
        }
    ):
        raise ValueError("native derivation must reuse its exact payment receipt")
    expected_entities = dossier["worldContract"]["entities"] + [
        e for o in dossier["secondaryObjectives"] for e in o["world"]["entities"]
    ]
    expected_zones = dossier["worldContract"]["zones"] + [
        z for o in dossier["secondaryObjectives"] for z in o["world"]["zones"]
    ]
    for actual, expected, label in (
        (binding["entities"], expected_entities, "entity"),
        (binding["zones"], expected_zones, "zone"),
    ):
        ids = [item["id"] for item in actual]
        if len(set(ids)) != len(ids) or set(ids) != {item["id"] for item in expected}:
            raise ValueError(f"exact original {label} identity binding required")
    positions = set()
    for entity in binding["entities"]:
        pos = entity["position"]
        if len(pos) != 2 or any(
            type(x) not in (int, float)
            or not math.isfinite(x)
            or not 0 <= x < binding["map"]["size"]
            for x in pos
        ):
            raise ValueError("invalid native entity position")
        if (
            tuple(pos) in positions
            or type(entity["player"]) is not int
            or entity["player"] not in (1, 2)
        ):
            raise ValueError("overlapping native bodies or unsupported owner")
        positions.add(tuple(pos))
    by_id = {e["id"]: e for e in binding["entities"]}
    zones = {z["id"]: z for z in binding["zones"]}
    if [o["kind"] for o in dossier["secondaryObjectives"]] != [
        "aid",
        "copy",
        "repair",
        "trade",
        "guide",
        "extract",
    ]:
        raise ValueError("unsupported optional delivery set")
    if [o["id"] for o in dossier["secondaryObjectives"]] != [
        f"side-{i}" for i in range(1, 7)
    ]:
        raise ValueError("unsupported optional identity set")
    for side in dossier["secondaryObjectives"]:
        if (
            side["predicate"]["operator"] != "all"
            or side["predicate"].get("neverUseTimerInstead") is not True
            or side.get("mandatory") is not False
        ):
            raise ValueError("unsupported optional conjunction or mandatory goal")
        expected_shapes = {
            "repair": ["entity-health", "atomic-payment"],
            "trade": ["entity-arrival", "atomic-payment"],
        }
        if [
            r["kind"] for r in side["predicate"]["requirements"]
        ] != expected_shapes.get(side["kind"], ["entity-arrival"]):
            raise ValueError("unsupported optional requirement shape")
        if len(side["effects"]) != 1:
            raise ValueError("bounded delivery accepts exactly one optional effect")
        if (
            side["kind"] not in ("aid", "copy", "repair", "trade", "guide", "extract")
            or side["dependencies"]
        ):
            raise ValueError("unsupported optional delivery mechanic")
        for req in side["predicate"]["requirements"]:
            if req["kind"] not in ("entity-arrival", "atomic-payment", "entity-health"):
                raise ValueError("unsupported optional predicate")
            if req["kind"] == "atomic-payment":
                if req["resources"] != binding["optionalPayments"][side["id"]]["cost"]:
                    raise ValueError("optional payment cost/binding mismatch")
                if (
                    req.get("once") is not True
                    or req.get("protectedRecoveryCannotBeSpent") is not True
                    or req.get("afterArrival") is not (side["kind"] == "trade")
                ):
                    raise ValueError("unsupported optional payment ordering")
            if req["kind"] == "entity-health":
                payment_req = side["predicate"]["requirements"][1]
                if req.get("health") != "full" or req.get(
                    "paymentReceipt"
                ) != payment_req.get("receipt"):
                    raise ValueError("unsupported repair health or receipt")
            if req["kind"] == "entity-arrival":
                if any(
                    req.get(flag) is not True
                    for flag in (
                        "aliveAtDelivery",
                        "oncePerEntity",
                        "noSubstitutes",
                        "initialPlacementDoesNotCount",
                    )
                ):
                    raise ValueError("unsupported optional identity/arrival semantics")
                if (
                    type(req["requiredCount"]) is not int
                    or req["requiredCount"] != len(req["entities"])
                    or set(req["destinations"]) != set(req["entities"])
                ):
                    raise ValueError(
                        "bounded arrival requires every original and assigned destination"
                    )
                for entity, zone in req["destinations"].items():
                    if (
                        math.dist(by_id[entity]["position"], zones[zone]["centre"])
                        <= zones[zone]["radius"]
                    ):
                        raise ValueError(
                            "initial placement cannot count as optional delivery"
                        )
        for effect in side["effects"]:
            expected_effect = (
                "unlock-context-and-hint"
                if side["kind"] == "copy"
                else "mark-alternative-route"
                if side["kind"] == "guide"
                else "finite-supply-withdrawal"
            )
            if (
                effect["kind"] != expected_effect
                or effect.get("funding") != "reserved-optional-stock"
                or effect.get("changesHistoricalOutcome") is not False
            ):
                raise ValueError("unsupported optional effect/funding")
    return originals, output


class DeliveryController(NativeMissionController):
    """Caesarea-specific provenance/commissioning layered on shared runtime."""

    def __init__(self, scenario, units, dossier, binding, locale):
        super().__init__(
            scenario,
            units,
            dossier,
            binding,
            locale,
            init_trigger_name="cdf-delivery-initialize",
            function_prefix="cdf_delivery",
            action_prefix="cdf_delivery_action",
        )
        self.issued = self.variable("register-issued")
        self.paid = self.variable("copy-payment")
        main_payment = dossier["objectivePlan"][1]["predicate"]["requirements"][0]
        self.semantic_variables = {
            main_payment["paidFlag"]: {"variable": self.paid, "trueValue": 1}
        }
        self.initialize_originals_and_reserves()

    def main(self, originals, output):
        input_alive = " && ".join(f"{self.alive[e]}()" for e in originals)
        main_valid = self.expression(
            f"{self.alive[output]}() && (xsTriggerVariable({self.issued}) == 1 || ({input_alive}))"
        )
        loss = self.trigger("main-loss")
        self.condition(loss, self.expression(f"{main_valid}() == false"))
        self.set(loss, self.terminal, 2)
        self.set(loss, self.phase, 14)
        defeat_done = self.captions(
            "defeat", ["defeat", "recovery-help"], self.terminal, 2, terminal=2
        )
        defeat = self.advance_after("declare-loss", defeat_done, 14, terminal=2)
        defeat.new_effect.declare_victory(source_player=1, enabled=0)
        help_text = {
            "en": "Move each original record bearer into the collection circle. Each original bearer must later arrive at the copying circle once and stay alive until issuance. Select the original copyist in that circle to authorize 40 wood and 20 gold; the bearers need not remain there together. Select the store to authorize its repair; select the arrived trader to authorize trade.",
            "es-ES": "Lleva cada portador original al círculo de recogida. Después, cada portador debe llegar una vez al círculo de copias y seguir vivo hasta la expedición. Selecciona allí al copista original para autorizar 40 de madera y 20 de oro; los portadores no tienen que permanecer juntos en el patio. Selecciona el almacén para autorizar su reparación y al comerciante que haya llegado para autorizar el comercio.",
        }[self.locale]
        intro = self.captions(
            "intro",
            self.binding["narration"]["introOrder"] + ["o1-goal"],
            self.phase,
            0,
            extra_text=[help_text],
        )
        self.advance_after("start-collection", intro, 1)
        collected = []
        for i, entity in enumerate(originals):
            flag = self.variable("collected-" + str(i))
            collected.append(flag)
            trigger = self.trigger("collect-" + str(i), phase=1)
            self.condition(trigger, main_valid)
            self.condition(
                trigger, self.in_zone(entity, self.binding["collection"]["zone"])
            )
            self.set(trigger, flag, 1)
        first = self.trigger("collection-complete", phase=1)
        self.objective_ui(
            first, self.dossier["objectivePlan"][0]["text"][self.locale], 0
        )
        self.condition(first, main_valid)
        for flag in collected:
            self.equal(first, flag, 1)
        self.set(first, self.phase, 11)
        first_text = self.captions(
            "collected", ["o1-receipt", "o1-reaction", "o2-goal"], self.phase, 11
        )
        self.advance_after("start-copying", first_text, 2)
        copying = self.trigger("copy-command", phase=2, looping=True)
        self.condition(copying, main_valid)
        for i, entity in enumerate(originals):
            arrived = self.variable("copy-court-arrival-" + str(i))
            observe = self.trigger("copy-court-arrival-" + str(i), phase=2)
            self.condition(observe, main_valid)
            self.condition(
                observe, self.in_zone(entity, self.binding["copying"]["zone"])
            )
            self.set(observe, arrived, 1)
            self.equal(copying, arrived, 1)
        self.condition(copying, self.in_zone(output, self.binding["copying"]["zone"]))
        copying.new_condition.object_selected(unit_object=self.units[output])
        pay = self.function(
            self.transactions["render_payment_function"],
            1,
            self.binding["copying"]["cost"],
            self.paid,
            {self.ready: 1, self.terminal: 0, self.phase: 2},
        )
        self.call(
            copying,
            f"    if ({main_valid}() && {pay}()) {{\n        xsSetTriggerVariable({self.issued}, 1);\n        xsSetTriggerVariable({self.phase}, 12);\n    }}",
        )
        issued = self.trigger("register-issued-name", phase=12)
        self.equal(issued, self.issued, 1)
        issued.new_effect.change_object_name(
            selected_object_ids=self.units[output],
            message=self.binding["copying"]["outputLabel"][self.locale],
        )
        copy_goal = self.trigger("copying-objective-ui")
        self.equal(copy_goal, self.issued, 1)
        self.objective_ui(
            copy_goal, self.dossier["objectivePlan"][1]["text"][self.locale], 1
        )
        copy_text = self.captions(
            "copied", ["o2-receipt", "o2-reaction", "o3-goal"], self.phase, 12
        )
        self.advance_after("start-final-delivery", copy_text, 3)
        final = self.trigger("original-register-delivered", phase=3)
        self.objective_ui(
            final, self.dossier["objectivePlan"][2]["text"][self.locale], 2
        )
        self.equal(final, self.issued, 1)
        self.equal(final, self.paid, 1)
        self.condition(final, main_valid)
        self.condition(final, self.in_zone(output, self.binding["delivery"]["zone"]))
        self.set(final, self.terminal, 1)
        self.set(final, self.phase, 13)
        won_text = self.captions(
            "outcome",
            ["o3-receipt", "o3-reaction"] + self.binding["narration"]["outroOrder"],
            self.terminal,
            1,
            terminal=1,
        )
        win = self.advance_after("declare-win", won_text, 13, terminal=1)
        win.new_effect.declare_victory(source_player=1, enabled=1)

    def compile(self):
        originals, output = validate_delivery_contract(self.dossier, self.binding)
        self.main(originals, output)
        secondary = runpy.run_path(str(HERE / "native_secondary.adapter.py"))
        for side in self.dossier["secondaryObjectives"]:
            secondary["compile_native_secondary"](self, side)
        return self.finish()


def compile_delivery_controller(scenario, units, dossier, binding, locale):
    if locale not in ("en", "es-ES"):
        raise ValueError("unsupported private delivery locale")
    validate_delivery_contract(dossier, binding)
    if set(units) != {e["id"] for e in binding["entities"]}:
        raise ValueError("native original handle binding mismatch")
    return DeliveryController(scenario, units, dossier, binding, locale).compile()
