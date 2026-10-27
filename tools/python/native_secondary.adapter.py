"""Existing bounded native secondary circuits and contract validation."""

import math

from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute, Operation


def validate_native_secondary_contracts(dossier, binding):
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


def compile_native_secondary(controller, side):
    key = side["id"]
    state = controller.variable(key + "-state")
    controller.semantic_variables[side["completionFlag"]] = {
        "variable": state,
        "trueValue": 1,
    }
    for effect in side["effects"]:
        controller.semantic_variables[effect["onceFlag"]] = {
            "variable": state,
            "trueValue": 1,
        }
    paid = controller.variable(key + "-paid")
    goal = controller.trigger(key + "-objective-ui")
    controller.equal(goal, state, 1)
    controller.objective_ui(
        goal, side["text"][controller.locale], 2 + int(key.split("-")[1]), optional=True
    )
    living = controller.expression(
        " && ".join(controller.alive[e["id"]] + "()" for e in side["world"]["entities"])
    )
    failure = controller.trigger(key + "-loss")
    controller.equal(failure, state, 0)
    controller.condition(failure, controller.expression(living + "() == false"))
    controller.set(failure, state, 2)
    controller.captions(key + "-lost", [key + "-lost"], state, 2)
    flags = {controller.ready: 1, controller.terminal: 0}
    for i, req in enumerate(side["predicate"]["requirements"]):
        if req["kind"] == "entity-arrival":
            for j, entity in enumerate(req["entities"]):
                arrived = controller.variable(f"{key}-arrival-{i}-{j}")
                observe = controller.trigger(f"{key}-arrival-{i}-{j}")
                controller.equal(observe, state, 0)
                controller.condition(observe, living)
                controller.condition(
                    observe, controller.in_zone(entity, req["destinations"][entity])
                )
                controller.set(observe, arrived, 1)
                flags[arrived] = 1
    payment = next(
        (
            r
            for r in side["predicate"]["requirements"]
            if r["kind"] == "atomic-payment"
        ),
        None,
    )
    health = next(
        (
            r
            for r in side["predicate"]["requirements"]
            if r["kind"] == "entity-health"
        ),
        None,
    )
    if payment:
        controller.semantic_variables[payment["receipt"]] = {
            "variable": paid,
            "trueValue": 1,
        }
        action = controller.trigger(key + "-payment", looping=True)
        controller.equal(action, state, 0)
        controller.condition(action, living)
        for variable, value in flags.items():
            controller.equal(action, variable, value)
        body = side["world"]["entities"][0]["id"]
        action.new_condition.object_selected(unit_object=controller.units[body])
        pay = controller.function(
            controller.transactions["render_payment_function"],
            1,
            payment["resources"],
            paid,
            {**flags, state: 0},
        )
        if health:
            full_hp = controller.variable(key + "-original-full-hp")
            handle = controller.handles[body]
            original = controller.entities[body]
            native_type = controller.load("native_scenario.factory.py")["unit_id"](
                original["unitType"]
            )
            controller.init.new_effect.modify_variable_by_attribute(
                source_player=original["player"],
                object_list_unit_id=native_type,
                object_attributes=ObjectAttribute.HIT_POINTS,
                operation=Operation.SET,
                variable=full_hp,
            )
            controller.call(
                controller.init,
                f"    xsSetUnitHitpoints(xsTriggerVariable({handle}), 0.5 * xsTriggerVariable({full_hp}));",
            )
            controller.call(
                action,
                f"    if ({living}() && {pay}()) {{\n        xsSetUnitHitpoints(xsTriggerVariable({handle}), xsTriggerVariable({full_hp}));\n    }}",
            )
            healthy = controller.expression(
                f"xsGetUnitHitpoints(xsTriggerVariable({handle})) >= xsTriggerVariable({full_hp})"
            )
        else:
            controller.call(action, f"    bool cdf_paid = {pay}();")
        flags[paid] = 1
    reward = {}
    for effect in side["effects"]:
        for resource, quantity in effect["resources"].items():
            reward[resource] = reward.get(resource, 0) + quantity
    grant = controller.function(
        controller.transactions["render_reward_function"],
        1,
        reward,
        {r: controller.reserve[r] for r in reward},
        state,
        flags,
    )
    complete = controller.trigger(key + "-complete", looping=True)
    controller.equal(complete, state, 0)
    controller.condition(complete, living)
    for variable, value in flags.items():
        controller.equal(complete, variable, value)
    if health:
        controller.condition(complete, healthy)
    extras, native_actions = [], []
    for effect in side["effects"]:
        if effect["kind"] == "unlock-context-and-hint":
            extras.extend(
                [effect["historicalNote"][controller.locale], effect["hint"][controller.locale]]
            )
        if effect["kind"] == "mark-alternative-route":
            corridor = next(
                c
                for c in controller.binding["map"]["corridors"]
                if c["id"] == effect["corridorId"]
            )
            for x, y in corridor["points"]:
                # Auxiliary markers are part of the same guarded invocation,
                # never a later trigger that terminal arbitration could skip.
                position = f"vector({float(x)}, {float(y)}, -1.0)"
                for marker_type in (OtherInfo.MAP_REVEALER.ID, OtherInfo.FLAG_B.ID):
                    native_actions.append(
                        f"        xsCreateUnit({marker_type}, 1, {position}, false, false, false);"
                    )
    action_source = "\n".join(native_actions)
    controller.call(complete, f"    if ({grant}()) {{\n{action_source}\n    }}")
    controller.captions(
        key + "-complete", [key + "-complete"], state, 1, extra_text=extras
    )
    for value in (1, 2):
        close = controller.trigger(key + "-close-" + str(value), terminal=value)
        controller.equal(close, state, 0)
        controller.set(close, state, 3)
