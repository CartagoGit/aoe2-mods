"""Specify and audit future transport proofs; never execute native journeys."""

EVENT_ORDER = [
    "ready-receipt", "board", "depart-origin", "water-transit",
    "arrive-destination", "disembark",
]
PROOF_FLAGS = [
    "samePassengerIdentity", "sameCarrierWithinJourney", "observedPositions", "sourceObjectiveLatched",
    "sharedCapacityReservation", "persistentScopedReceipts", "arrivalAloneInsufficient",
    "noTimerSubstitution", "idempotentCompletion",
]
CAPABILITY_ID = "manifest-backed-water-journeys"


def materialize_requirement(requirement, groups, destinations):
    requirement["carriers"] = groups[requirement.pop("carrierGroup")]
    requirement["originZone"] = destinations[requirement.pop("originHub")]
    requirement["destinationZone"] = destinations[requirement.pop("disembarkHub")]


def audit_requirement(requirement, episode, position, check, context):
    entities = {e["id"]: e for e in episode["worldContract"]["entities"]}
    zones = {z["id"]: z for z in episode["worldContract"]["zones"]}
    passengers = requirement.get("entities", [])
    carriers = requirement.get("carriers", [])
    check(bool(passengers) and len(set(passengers)) == len(passengers)
          and set(passengers) <= set(entities)
          and 0 < requirement.get("requiredCount", 0) <= len(passengers),
          f"{context}: invalid journey passenger identities/count")
    check(bool(carriers) and len(set(carriers)) == len(carriers)
          and set(carriers) <= set(entities) and not set(carriers).intersection(passengers)
          and all(entities[c]["role"] == "fictional-original-water-carrier" for c in carriers if c in entities),
          f"{context}: invalid journey carriers")
    origin = zones.get(requirement.get("originZone"))
    destination = zones.get(requirement.get("destinationZone"))
    check(origin is not None and destination is not None and origin != destination,
          f"{context}: invalid journey endpoints")
    corridors = {c["id"]: c for c in episode["mapPlan"]["corridors"]}
    routes = requirement.get("allowedCorridorIds", [])
    check(bool(routes) and len(set(routes)) == len(routes),
          f"{context}: missing or duplicate water route")
    for route in routes:
        corridor = corridors.get(route)
        check(corridor is not None and corridor["mode"] == "water"
              and origin is not None and destination is not None
              and corridor["hubOrder"][0] == origin["hub"]
              and corridor["hubOrder"][-1] == destination["hub"],
              f"{context}: journey route must join its own shores by water")
    ready = requirement.get("readyReceipt", {})
    source = next((o for i, o in enumerate(episode["objectivePlan"])
                   if i < position and o["id"] == ready.get("objective")), None)
    receipt = next((r for r in source["predicate"]["requirements"]
                    if r["id"] == ready.get("requirement")), None) if source else None
    check(receipt is not None and receipt["kind"] == "entity-state"
          and receipt["state"] == "arrived"
          and set(receipt["entities"]) == set(passengers)
          and receipt["requiredCount"] >= requirement.get("requiredCount", 0)
          and set(receipt.get("destinations", {}).values()) == {requirement.get("originZone")},
          f"{context}: journey lacks its own prior shore readiness receipt")
    check(requirement.get("eventOrder") == EVENT_ORDER
          and all(requirement.get("proofPolicy", {}).get(flag) is True for flag in PROOF_FLAGS)
          and requirement.get("passengerSlotsEach") == 1,
          f"{context}: incomplete manifest journey proof")
    plan = episode.get("transportPlan", {})
    capacities = plan.get("capacityByCarrier", {})
    check(set(carriers) == set(capacities)
          and all(isinstance(capacities.get(c), int) and not isinstance(capacities[c], bool)
                  and capacities[c] > 0 for c in carriers),
          f"{context}: missing finite carrier capacity")
    check(plan.get("implementationStatus") == "design-only-unimplemented"
          and plan.get("sharedManifestAuthority") is True
          and plan.get("cargoPolicy") == "identified loadable proxies; no resource inventory claim"
          and plan.get("lossPolicy") == "destroyed carrier loses every currently boarded passenger; disembarked passengers survive independently"
          and any(c["id"] == CAPABILITY_ID for c in episode["requiredCapabilities"]),
          f"{context}: transport must retain its unimplemented capability gate")
