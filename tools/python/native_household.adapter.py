"""Bounded private native household controller for the civilian refuge episode.

This adapter implements only the closed household ledger semantics of
`02-civilian-refuge-jerusalem`: eight original civilian proxies, a cumulative
court ledger, one atomic 240-food court receipt and a single guarded terminal
commit. It does not enable the public composed exporter, does not own the map,
the historical interpretation or the physical binding, and does not approve the
whole slice. Source and XS inspection support compilation evidence only; they
do not execute the game engine.
"""

import json
import math
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
_NATIVE_MISSION = runpy.run_path(str(HERE / "native_mission.controller.py"))
NativeMissionController = _NATIVE_MISSION["NativeMissionController"]

EPISODE_ID = "02-civilian-refuge-jerusalem"
PREFIX = "faith-origins." + EPISODE_ID
HOUSEHOLD_COUNT = 8
SURVIVOR_MINIMUM = 6
REQUIRED_COUNT = 6
COURT_ZONE = PREFIX + ".destination-2"
REFUGE_ZONE = PREFIX + ".destination-3"
LEDGER = "received-households"
RECEIPT = PREFIX + ".o2.req-1.paid"
PAYMENT_COST = {"food": 240}
HOUSEHOLD_IDS = tuple(PREFIX + f".households-{index}" for index in range(1, 9))
DESTINATION_IDS = tuple(PREFIX + f".destination-{index}" for index in (1, 2, 3))
MAIN_SCREENS = (
    "o1-goal",
    "o1-receipt",
    "o1-reaction",
    "o2-goal",
    "o2-receipt",
    "o2-reaction",
    "o3-goal",
    "o3-receipt",
    "o3-reaction",
    "defeat",
    "recovery-help",
)
INTRO_ORDER = [
    "title",
    "fact-intro",
    "handover",
    "persona-intro",
    "historical-license",
    "route-help",
    "economy-help",
]
OUTRO_ORDER = ["fact-outro", "persona-outro", "next-episode"]
UNSUPPORTED_PROFILE_FIELDS = (
    "designProfile",
    "capability",
    "capabilityProfile",
    "referenceCapabilityProfile",
    "sharedCapabilityProfile",
    "fulfillment",
    "fulfillmentContract",
)
CIVILIAN_TYPES = ("villager-male", "villager-female")
LOCALES = ("en", "es-ES")


def _render_flag_total(function_name, variables, threshold):
    """Return true when at least `threshold` arrival facts are recorded.

    Arrival facts are historical and cumulative: leaving a receiving circle
    never erases them, so this count is not filtered by current life.
    """
    lines = [f"bool {function_name}() {{", "    int cdf_total = 0;"]
    for variable in variables:
        lines.append(f"    if (xsTriggerVariable({variable}) == 1) {{")
        lines.append("        cdf_total = cdf_total + 1;")
        lines.append("    }")
    lines.append(f"    return (cdf_total >= {threshold});")
    lines.append("}")
    return "\n".join(lines)


def _render_living_total(function_name, alive_functions, threshold):
    """Return true when at least `threshold` originals are alive right now."""
    lines = [f"bool {function_name}() {{", "    int cdf_total = 0;"]
    for alive in alive_functions:
        lines.append(f"    if ({alive}()) {{")
        lines.append("        cdf_total = cdf_total + 1;")
        lines.append("    }")
    lines.append(f"    return (cdf_total >= {threshold});")
    lines.append("}")
    return "\n".join(lines)


def _render_living_loss(function_name, alive_functions, minimum):
    """Return true when fewer than `minimum` originals are alive right now."""
    lines = [f"bool {function_name}() {{", "    int cdf_total = 0;"]
    for alive in alive_functions:
        lines.append(f"    if ({alive}()) {{")
        lines.append("        cdf_total = cdf_total + 1;")
        lines.append("    }")
    lines.append(f"    return (cdf_total < {minimum});")
    lines.append("}")
    return "\n".join(lines)


def _expected_objectives():
    households = list(HOUSEHOLD_IDS)
    court = {entity: COURT_ZONE for entity in households}
    refuge = {entity: REFUGE_ZONE for entity in households}
    eligible = {"objective": "o1", "ledger": LEDGER}
    return [
        {
            "operator": "all",
            "requirements": [
                {
                    "kind": "entity-state",
                    "requiredCount": REQUIRED_COUNT,
                    "state": "arrived",
                    "id": "req-1",
                    "entities": households,
                    "destinations": court,
                    "oncePerEntity": True,
                }
            ],
            "neverUseTimerInstead": True,
            "exportedLedgers": [
                {
                    "id": LEDGER,
                    "operator": "intersection",
                    "fromRequirements": ["req-1"],
                    "minimumCount": REQUIRED_COUNT,
                }
            ],
        },
        {
            "operator": "all",
            "requirements": [
                {
                    "kind": "resource-transaction",
                    "amounts": dict(PAYMENT_COST),
                    "id": "req-1",
                    "receivingZones": [COURT_ZONE],
                    "allocations": {COURT_ZONE: dict(PAYMENT_COST)},
                    "account": "spendable",
                    "paidFlag": RECEIPT,
                    "once": True,
                    "atomic": True,
                }
            ],
            "neverUseTimerInstead": True,
        },
        {
            "operator": "all",
            "requirements": [
                {
                    "kind": "entity-state",
                    "requiredCount": REQUIRED_COUNT,
                    "state": "arrived",
                    "id": "req-1",
                    "entities": households,
                    "destinations": refuge,
                    "oncePerEntity": True,
                    "eligibleEntitiesFromLedger": eligible,
                },
                {
                    "kind": "entity-state",
                    "requiredCount": REQUIRED_COUNT,
                    "state": "alive-and-held",
                    "id": "req-2",
                    "entities": households,
                    "destinations": refuge,
                    "oncePerEntity": True,
                    "eligibleEntitiesFromLedger": eligible,
                },
            ],
            "neverUseTimerInstead": True,
        },
    ]


def _expected_transitions():
    return [
        {"from": "briefing", "to": "phase-1", "on": "intro-accepted"},
        *[
            {
                "from": f"phase-{index}",
                "to": f"phase-{index + 1}" if index < 3 else "victory",
                "on": "objective-latched",
                "objectiveId": f"o{index}",
            }
            for index in (1, 2, 3)
        ],
    ]


def _finite_number(value):
    return type(value) in (int, float) and math.isfinite(value)


def _canonical(value, label):
    """Return a type-strict canonical form; Python equality accepts 1 == True."""
    try:
        return json.dumps(
            value, sort_keys=True, allow_nan=False, separators=(",", ":")
        )
    except (TypeError, ValueError) as error:
        raise ValueError(f"{label} is not canonical JSON") from error


def _snapped(position):
    """Return the native start of a design position; the shared base snaps it."""
    return (math.floor(position[0]) + 0.5, math.floor(position[1]) + 0.5)


def _check_placement(binding):
    size = binding["map"]["size"]
    if type(size) is not int or size <= 0:
        raise ValueError("native map size must be a positive integer")
    positions = set()
    for entity in binding["entities"]:
        position = entity["position"]
        if len(position) != 2 or any(
            not _finite_number(value) or not 0 <= value < size for value in position
        ):
            raise ValueError("invalid native entity position")
        if (
            _snapped(position) in positions
            or type(entity["player"]) is not int
            or entity["player"] not in (1, 2)
        ):
            raise ValueError("overlapping native bodies or unsupported owner")
        positions.add(_snapped(position))
    for zone in binding["zones"]:
        centre = zone["centre"]
        radius = zone["radius"]
        if len(centre) != 2 or any(
            not _finite_number(value) or not 0 <= value < size for value in centre
        ):
            raise ValueError("invalid native zone centre")
        if not _finite_number(radius) or radius <= 0:
            raise ValueError("invalid native zone radius")
        if (
            centre[0] - radius < 0
            or centre[1] - radius < 0
            or centre[0] + radius > size
            or centre[1] + radius > size
        ):
            raise ValueError("receiving circle must fit inside the map")


def _reject_unsupported_profiles(owner, label):
    for field in UNSUPPORTED_PROFILE_FIELDS:
        if field in owner:
            raise ValueError(f"{label} must not carry a composed {field} field")


def _is_player(body, player):
    return type(body["player"]) is int and body["player"] == player


def _check_bodies(dossier, binding):
    by_id = {entity["id"]: entity for entity in binding["entities"]}
    for entity in HOUSEHOLD_IDS:
        body = by_id[entity]
        if not _is_player(body, 1) or body["unitType"] not in CIVILIAN_TYPES:
            raise ValueError(
                "the eight household proxies must be player1 civilian villagers"
            )
    for side in dossier["secondaryObjectives"]:
        for entity in side["world"]["entities"]:
            body = by_id[entity["id"]]
            if side["kind"] == "repair":
                if not _is_player(body, 2) or body["unitType"] != "house":
                    raise ValueError(
                        "the optional repair store must be the original player2 house"
                    )
            elif not _is_player(body, 1) or body["unitType"] not in CIVILIAN_TYPES:
                raise ValueError(
                    "optional bearers must be player1 civilian villagers"
                )
    for entity in binding["entities"]:
        labels = entity.get("label")
        if not isinstance(labels, dict):
            raise ValueError("native entity labels must be localized strings")
        for locale in LOCALES:
            if not isinstance(labels.get(locale), str) or not labels[locale].strip():
                raise ValueError("native entity labels must be nonempty strings")
    for zone in binding["zones"]:
        labels = zone.get("label")
        if not isinstance(labels, dict):
            raise ValueError("native zone labels must be localized strings")
        for locale in LOCALES:
            if not isinstance(labels.get(locale), str) or not labels[locale].strip():
                raise ValueError("native zone labels must be nonempty strings")


def _check_narration(dossier, binding):
    narration = binding.get("narration")
    if not isinstance(narration, dict):
        raise ValueError("household binding requires narration")
    for key in ("introOrder", "outroOrder", "speakerLabels"):
        if not narration.get(key):
            raise ValueError("household binding narration is incomplete")
    if list(narration["introOrder"]) != INTRO_ORDER:
        raise ValueError("the household intro order is fixed and factual before persona")
    if list(narration["outroOrder"]) != OUTRO_ORDER:
        raise ValueError("the household outro order is fixed")
    screens = {screen["id"]: screen for screen in dossier["screens"]}
    for key in MAIN_SCREENS:
        if key not in screens:
            raise ValueError("household dossier is missing an authored screen")
    for key in list(narration["introOrder"]) + list(narration["outroOrder"]):
        if key not in screens:
            raise ValueError("household narration references an unknown screen")
    for key in list(narration["introOrder"]) + list(narration["outroOrder"]):
        speaker = screens[key]["narrator"]
        if speaker == "none":
            continue
        labels = narration["speakerLabels"].get(speaker)
        if not isinstance(labels, dict) or not labels.get("en") or not labels.get("es-ES"):
            raise ValueError("native caption requires a localized speaker label")


def _check_optional_payments(dossier, binding):
    payments = binding.get("optionalPayments")
    if not isinstance(payments, dict):
        raise ValueError("household binding requires optional payments")
    for side in dossier["secondaryObjectives"]:
        for requirement in side["predicate"]["requirements"]:
            if requirement["kind"] != "atomic-payment":
                continue
            declared = payments.get(side["id"])
            if not isinstance(declared, dict) or _canonical(
                declared.get("cost"), "optional payment cost"
            ) != _canonical(requirement["resources"], "optional payment requirement"):
                raise ValueError("optional payment cost/binding mismatch")


def _check_corridors(dossier, binding):
    corridors = {
        corridor.get("id") for corridor in binding["map"].get("corridors", []) or []
    }
    for side in dossier["secondaryObjectives"]:
        for effect in side["effects"]:
            if (
                effect["kind"] == "mark-alternative-route"
                and effect.get("corridorId") not in corridors
            ):
                raise ValueError(
                    "optional guide effect needs an authored corridor in the binding"
                )


def validate_household_contract(dossier, binding):
    """Reject unsupported or inconsistent household graphs before any native change."""
    if (
        binding.get("kind") != "private-historical-household-native-binding"
        or type(binding.get("schemaVersion")) is not int
        or binding["schemaVersion"] != 1
    ):
        raise ValueError("unsupported native household binding")
    if dossier["id"] != EPISODE_ID or binding["episodeId"] != EPISODE_ID:
        raise ValueError("household binding episode mismatch")
    _reject_unsupported_profiles(dossier, "the private dossier")
    _reject_unsupported_profiles(binding, "the private binding")
    objectives = dossier["objectivePlan"]
    if [objective["id"] for objective in objectives] != ["o1", "o2", "o3"]:
        raise ValueError("unsupported household objective graph")
    if [objective["after"] for objective in objectives] != [[], ["o1"], ["o2"]]:
        raise ValueError("unsupported household prerequisites")
    if [objective["phase"] for objective in objectives] != [
        "phase-1",
        "phase-2",
        "phase-3",
    ]:
        raise ValueError("unsupported household phases")
    state_machine = dossier["stateMachine"]
    if state_machine.get("campaignProgressWrite") is not False:
        raise ValueError("household controller writes no campaign progress")
    if state_machine["phaseTransitions"] != _expected_transitions():
        raise ValueError("unsupported household phase transitions")
    if (
        state_machine["terminalPriority"]
        != "defeat first; close side rewards; one terminal latch"
    ):
        raise ValueError("unsupported household terminal priority")
    expected = _expected_objectives()
    for index, predicate in enumerate(expected):
        if _canonical(
            objectives[index]["predicate"], "household source predicate"
        ) != _canonical(predicate, "expected household predicate"):
            raise ValueError(
                f"household o{index + 1} source requirement shape mismatch"
            )
    world = dossier["worldContract"]
    if [entity["id"] for entity in world["entities"]] != list(HOUSEHOLD_IDS):
        raise ValueError("household world entity identity mismatch")
    if [zone["id"] for zone in world["zones"]] != list(DESTINATION_IDS):
        raise ValueError("household world zone identity mismatch")
    if world.get("objectGroups") and world["objectGroups"].get(
        "households"
    ) != list(HOUSEHOLD_IDS):
        raise ValueError("household object group mismatch")
    survivors = world["survivorGroups"]
    if (
        len(survivors) != 1
        or _canonical(
            survivors[0].get("entities"), "survivor group entities"
        )
        != _canonical(list(HOUSEHOLD_IDS), "expected survivor entities")
        or _canonical(
            survivors[0].get("minimumAliveOrAlreadySafe"), "survivor minimum"
        )
        != _canonical(SURVIVOR_MINIMUM, "expected survivor minimum")
    ):
        raise ValueError("household survivor group mismatch")
    declared = binding.get("households")
    if not isinstance(declared, dict):
        raise ValueError("household binding requires a households block")
    if declared.get("entities") != list(HOUSEHOLD_IDS):
        raise ValueError("household binding entity identity mismatch")
    if (
        type(declared.get("requiredCount")) is not int
        or declared["requiredCount"] != REQUIRED_COUNT
    ):
        raise ValueError("household binding threshold mismatch")
    if declared.get("courtZone") != COURT_ZONE or declared.get("refugeZone") != REFUGE_ZONE:
        raise ValueError("household binding zone reference mismatch")
    payment = declared.get("payment")
    if not isinstance(payment, dict) or _canonical(
        payment.get("cost"), "household payment cost"
    ) != _canonical(PAYMENT_COST, "expected household payment cost"):
        raise ValueError("household binding payment mismatch")
    expected_entities = list(HOUSEHOLD_IDS) + [
        entity["id"]
        for side in dossier["secondaryObjectives"]
        for entity in side["world"]["entities"]
    ]
    expected_zones = list(DESTINATION_IDS) + [
        zone["id"]
        for side in dossier["secondaryObjectives"]
        for zone in side["world"]["zones"]
    ]
    for actual, wanted, label in (
        (binding["entities"], expected_entities, "entity"),
        (binding["zones"], expected_zones, "zone"),
    ):
        ids = [item["id"] for item in actual]
        if len(ids) != len(wanted) or set(ids) != set(wanted):
            raise ValueError(f"exact original {label} identity binding required")
    _check_placement(binding)
    by_id = {entity["id"]: entity for entity in binding["entities"]}
    zones = {zone["id"]: zone for zone in binding["zones"]}
    for entity in HOUSEHOLD_IDS:
        start = _snapped(by_id[entity]["position"])
        for zone in (COURT_ZONE, REFUGE_ZONE):
            if math.dist(start, zones[zone]["centre"]) <= zones[zone]["radius"]:
                raise ValueError("original placement cannot count as a household arrival")
    _check_narration(dossier, binding)
    _check_bodies(dossier, binding)
    _check_optional_payments(dossier, binding)
    _check_corridors(dossier, binding)
    secondary = runpy.run_path(str(HERE / "native_secondary.adapter.py"))
    validator = secondary.get("validate_native_secondary_contracts")
    if validator is None:
        raise ValueError("shared native secondary contract validator is unavailable")
    validator(dossier, binding)
    ledger = objectives[0]["predicate"]["exportedLedgers"][0]["id"]
    receipt = objectives[1]["predicate"]["requirements"][0]["paidFlag"]
    return list(HOUSEHOLD_IDS), ledger, receipt


def _validate_native_handles(units, binding):
    expected = {entity["id"] for entity in binding["entities"]}
    if set(units) != expected:
        raise ValueError("native original handle binding mismatch")
    seen = set()
    for handle in units.values():
        if type(handle) is not int or handle < 0:
            raise ValueError("native handle must be a distinct nonnegative integer")
        if handle in seen:
            raise ValueError("duplicate native original handle")
        seen.add(handle)


class HouseholdController(NativeMissionController):
    """Household ledger orchestration layered on the shared native runtime."""

    def __init__(self, scenario, units, dossier, binding, locale):
        super().__init__(
            scenario,
            units,
            dossier,
            binding,
            locale,
            init_trigger_name="cdf-household-initialize",
            function_prefix="cdf_household",
            action_prefix="cdf_household_action",
        )
        self.originals = list(binding["households"]["entities"])
        self.court_zone = binding["households"]["courtZone"]
        self.refuge_zone = binding["households"]["refugeZone"]
        self.required_count = binding["households"]["requiredCount"]
        self.survivor_minimum = dossier["worldContract"]["survivorGroups"][0][
            "minimumAliveOrAlreadySafe"
        ]
        payment_requirement = dossier["objectivePlan"][1]["predicate"]["requirements"][0]
        self.payment_cost = dict(payment_requirement["amounts"])
        self.receipt = payment_requirement["paidFlag"]
        self.ledger = dossier["objectivePlan"][0]["predicate"]["exportedLedgers"][0]["id"]
        self.court_arrival = [
            self.variable("court-arrival-" + str(index))
            for index in range(len(self.originals))
        ]
        self.refuge_arrival = [
            self.variable("refuge-arrival-" + str(index))
            for index in range(len(self.originals))
        ]
        self.held = [
            self.variable("held-" + str(index))
            for index in range(len(self.originals))
        ]
        self.payment = self.variable("court-payment")
        self.latch = self.variable("objective-o3")
        transition = next(
            item
            for item in dossier["stateMachine"]["phaseTransitions"]
            if item["to"] == "victory"
        )
        self.semantic_variables = {
            self.receipt: {"variable": self.payment, "trueValue": 1},
            f"{transition['on']}:{transition['objectiveId']}": {
                "variable": self.latch,
                "trueValue": 1,
            },
        }
        self.initialize_originals_and_reserves()

    def alive_functions(self):
        return [self.alive[entity] for entity in self.originals]

    def final_action_source(self):
        """One guarded invocation: activation guards, then loss, then the terminal write.

        The activation guards run before any mutation, so an inactive, wrong
        phase, unpaid or already terminal action does nothing. The fresh census
        then evaluates irreversible loss before the qualified success.
        """
        lines = [
            f"    if (xsTriggerVariable({self.ready}) != 1) {{ return; }}",
            f"    if (xsTriggerVariable({self.phase}) != 3) {{ return; }}",
            f"    if (xsTriggerVariable({self.payment}) != 1) {{ return; }}",
            f"    if (xsTriggerVariable({self.terminal}) != 0) {{ return; }}",
            "    int cdf_alive = 0;",
            "    int cdf_qualified = 0;",
        ]
        for index, entity in enumerate(self.originals):
            lines.append(f"    if ({self.alive[entity]}()) {{")
            lines.append("        cdf_alive = cdf_alive + 1;")
            lines.append(
                "        if (xsTriggerVariable("
                f"{self.court_arrival[index]}) == 1 && xsTriggerVariable("
                f"{self.refuge_arrival[index]}) == 1 && xsTriggerVariable("
                f"{self.held[index]}) == 1) {{"
            )
            lines.append("            cdf_qualified = cdf_qualified + 1;")
            lines.append("        }")
            lines.append("    }")
        lines.extend(
            [
                "    if (cdf_alive < " + str(self.survivor_minimum) + ") {",
                f"        xsSetTriggerVariable({self.terminal}, 2);",
                f"        xsSetTriggerVariable({self.phase}, 14);",
                "        return;",
                "    }",
                "    if (cdf_qualified >= " + str(self.required_count) + ") {",
                f"        xsSetTriggerVariable({self.latch}, 1);",
                f"        xsSetTriggerVariable({self.terminal}, 1);",
                f"        xsSetTriggerVariable({self.phase}, 13);",
                "    }",
            ]
        )
        return "\n".join(lines)

    def main(self):
        court = self.court_zone
        refuge = self.refuge_zone
        living = self.function(
            _render_living_total, self.alive_functions(), self.survivor_minimum
        )
        loss = self.function(
            _render_living_loss, self.alive_functions(), self.survivor_minimum
        )
        loss_trigger = self.trigger("household-loss")
        self.condition(loss_trigger, loss)
        self.set(loss_trigger, self.terminal, 2)
        self.set(loss_trigger, self.phase, 14)
        defeat_done = self.captions(
            "defeat", ["defeat", "recovery-help"], self.terminal, 2, terminal=2
        )
        defeat = self.advance_after("declare-loss", defeat_done, 14, terminal=2)
        defeat.new_effect.declare_victory(source_player=1, enabled=0)
        help_text = {
            "en": "Move each original household representative into the southern receiving court; a visit is recorded once and stays a fact. At least six of the eight must be alive. Then select any one living original representative that is currently inside the court to authorize 240 food, once. Afterwards bring at least six of the same eight, alive, to the southern-road refuge. Leaving a circle never erases an arrival, but a lost household never comes back, and three lost households defeat the mission.",
            "es-ES": "Lleva cada representante original de hogar al patio receptor meridional; cada visita se registra una sola vez y permanece. Al menos seis de los ocho deben estar vivos. Después selecciona a cualquier representante original vivo que esté dentro del patio para autorizar 240 de alimento, una sola vez. Lleva luego al refugio del camino sur al menos seis de los mismos ocho, con vida. Salir de un círculo nunca borra una llegada, pero un hogar perdido no vuelve, y tres hogares perdidos derrotan a la misión.",
        }[self.locale]
        intro = self.captions(
            "intro",
            self.binding["narration"]["introOrder"] + ["o1-goal"],
            self.phase,
            0,
            extra_text=[help_text],
        )
        self.advance_after("start-court-phase", intro, 1)
        for index, entity in enumerate(self.originals):
            court_observe = self.trigger(f"court-arrival-{index}")
            self.condition(court_observe, self.in_zone(entity, court))
            self.set(court_observe, self.court_arrival[index], 1)
            refuge_observe = self.trigger(f"refuge-arrival-{index}")
            self.condition(refuge_observe, self.in_zone(entity, refuge))
            self.set(refuge_observe, self.refuge_arrival[index], 1)
            self.set(refuge_observe, self.held[index], 1)
        court_total = self.function(
            _render_flag_total, self.court_arrival, self.required_count
        )
        first = self.trigger("court-objective-reached", phase=1)
        self.objective_ui(
            first, self.dossier["objectivePlan"][0]["text"][self.locale], 0
        )
        self.condition(first, self.expression(f"{court_total}() && {living}()"))
        self.set(first, self.phase, 11)
        first_text = self.captions(
            "court-received", ["o1-receipt", "o1-reaction", "o2-goal"], self.phase, 11
        )
        self.advance_after("start-payment-phase", first_text, 2)
        pay = self.function(
            self.transactions["render_payment_function"],
            1,
            dict(self.payment_cost),
            self.payment,
            {self.ready: 1, self.terminal: 0, self.phase: 2},
        )
        for index, entity in enumerate(self.originals):
            action = self.trigger(f"court-payment-{index}", phase=2, looping=True)
            action.new_condition.object_selected(unit_object=self.units[entity])
            self.condition(action, self.alive[entity])
            self.condition(action, self.in_zone(entity, court))
            self.call(
                action,
                "    if (xsTriggerVariable("
                + str(self.ready)
                + ") != 1) { return; }\n"
                + "    if (xsTriggerVariable("
                + str(self.phase)
                + ") != 2) { return; }\n"
                + "    if (xsTriggerVariable("
                + str(self.terminal)
                + ") != 0) { return; }\n"
                + "    if ("
                + loss
                + "()) {\n"
                + f"        xsSetTriggerVariable({self.terminal}, 2);\n"
                + f"        xsSetTriggerVariable({self.phase}, 14);\n"
                + "    } else if ("
                + pay
                + "()) {\n"
                + f"        xsSetTriggerVariable({self.phase}, 12);\n"
                + "    }",
            )
        payment_goal = self.trigger("court-payment-goal")
        self.equal(payment_goal, self.payment, 1)
        self.objective_ui(
            payment_goal, self.dossier["objectivePlan"][1]["text"][self.locale], 1
        )
        paid_text = self.captions(
            "court-paid", ["o2-receipt", "o2-reaction", "o3-goal"], self.phase, 12
        )
        self.advance_after("start-refuge-phase", paid_text, 3)
        final_goal = self.trigger("household-final-goal", phase=3)
        self.objective_ui(
            final_goal, self.dossier["objectivePlan"][2]["text"][self.locale], 2
        )
        final = self.trigger("household-final", phase=3, looping=True)
        self.equal(final, self.payment, 1)
        self.call(final, self.final_action_source())
        won_text = self.captions(
            "outcome",
            ["o3-receipt", "o3-reaction"] + self.binding["narration"]["outroOrder"],
            self.latch,
            1,
            terminal=1,
        )
        win = self.advance_after("declare-win", won_text, 13, terminal=1)
        win.new_effect.declare_victory(source_player=1, enabled=1)

    def compile(self):
        validate_household_contract(self.dossier, self.binding)
        self.main()
        secondary = runpy.run_path(str(HERE / "native_secondary.adapter.py"))
        for side in self.dossier["secondaryObjectives"]:
            secondary["compile_native_secondary"](self, side)
        return self.finish()


def compile_household_controller(scenario, units, dossier, binding, locale):
    if locale not in ("en", "es-ES"):
        raise ValueError("unsupported private household locale")
    validate_household_contract(dossier, binding)
    _validate_native_handles(units, binding)
    return HouseholdController(scenario, units, dossier, binding, locale).compile()
