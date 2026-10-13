import { paymentReceiptMatches } from "../gameplay-validation/payment-receipt.helper";
import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";
import type { MainRequirement } from "./capability-action.model";
import {
  factKey,
  factsFor,
  hasArrival,
  hasRequirementArrival,
  objectiveRequirements,
} from "./capability-ledgers.helper";
import type { CapabilitySnapshot } from "./capability-snapshot.schema";
import { RESOURCES } from "./resource-accounts.helper";

export function secondaryRequirementsSatisfied(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  sideId: string,
) {
  const side = profile.secondaryObjectives.find((item) => item.id === sideId);
  if (!side) return false;
  return side.predicate.requirements.every((req, index) => {
    if (req.kind === "entity-arrival")
      return (
        [...new Set(req.entities)].filter((id) =>
          hasArrival(state, id, req.destinations[id] ?? ""),
        ).length >= req.requiredCount
      );
    if (req.kind === "atomic-payment")
      return state.paidReceipts.includes(req.receipt);
    if (req.kind === "visit-zones")
      return req.zones.every((id) => state.visitedZones.includes(id));
    return (
      factsFor(state, sideId, `requirement-${index}`).includes(req.entity) &&
      state.paidReceipts.includes(req.paymentReceipt)
    );
  });
}

export function mainRequirementSatisfied(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  objectiveId: string,
  requirement: CapabilityProfileV2["objectivePlan"][number]["predicate"]["requirements"][number],
): boolean {
  const facts = factsFor(state, objectiveId, requirement.id);
  switch (requirement.kind) {
    case "entity-state": {
      const eligible = requirement.eligibleEntitiesFromLedger
        ? new Set(
            state.exportedLedgers[
              factKey(
                requirement.eligibleEntitiesFromLedger.objective,
                requirement.eligibleEntitiesFromLedger.ledger,
              )
            ] ?? [],
          )
        : null;
      const candidates = [...new Set(requirement.entities)].filter(
        (id) =>
          (!eligible || eligible.has(id)) &&
          generationReady(profile, state, id),
      );
      if (requirement.state === "arrived") {
        const delivered = candidates.filter((id) =>
          hasRequirementArrival(state, objectiveId, requirement, id),
        );
        const assignedZones = new Set(
          Object.values(requirement.destinations ?? {}),
        );
        const counts = new Map<string, number>();
        for (const entityId of delivered) {
          const zoneId = requirement.destinations?.[entityId];
          if (zoneId) counts.set(zoneId, (counts.get(zoneId) ?? 0) + 1);
        }
        return (
          delivered.length >= requirement.requiredCount &&
          counts.size >= (requirement.distinctDestinationCount ?? 0) &&
          (requirement.minimumPerDestination === undefined ||
            [...assignedZones].every(
              (zoneId) =>
                (counts.get(zoneId) ?? 0) >=
                (requirement.minimumPerDestination ?? 0),
            ))
        );
      }
      if (requirement.state === "destroyed")
        return (
          candidates.filter((id) => state.entityStates[id] === "destroyed")
            .length >= requirement.requiredCount
        );
      if (requirement.state === "alive")
        return (
          candidates.filter(
            (id) =>
              state.entityStates[id] === "alive" ||
              state.entityStates[id] === "arrived",
          ).length >= requirement.requiredCount
        );
      return (
        candidates.filter(
          (id) =>
            facts.includes(id) &&
            (requirement.state !== "alive-and-held" ||
              state.entityStates[id] !== "destroyed") &&
            (!requirement.destinations ||
              hasArrival(state, id, requirement.destinations[id] ?? "")),
        ).length >= requirement.requiredCount
      );
    }
    case "resource-transaction":
      return state.paidReceipts.includes(requirement.paidFlag);
    case "minimum-stock": {
      if (
        requirement.atHub !== undefined ||
        requirement.accountEntityIds !== undefined ||
        requirement.maximumNavigableDistanceTiles !== undefined
      )
        return false;
      const account =
        requirement.account === "spendable"
          ? state.spendable
          : state.protectedRecovery;
      return RESOURCES.every(
        (resource) => account[resource] >= (requirement.amounts[resource] ?? 0),
      );
    }
    case "receipt-exists":
      return (
        paymentReceiptMatches(profile, requirement) &&
        state.paidReceipts.includes(requirement.flag)
      );
    case "paired-delivery":
      return facts.length >= requirement.requiredCount;
    case "route-choice":
      return (
        state.selectedRoutes[factKey(objectiveId, requirement.id)] !== undefined
      );
    case "finite-wave-resolution":
      return (
        [...new Set(requirement.waves)].filter((id) =>
          state.resolvedWaves.includes(id),
        ).length >= requirement.requiredCount
      );
    case "hold-area":
      return requirement.zones.every(
        (id) => (state.heldSeconds[id] ?? 0) >= requirement.continuousSeconds,
      );
    case "forbidden-entry":
      return !state.forbiddenEntries.some((id) =>
        id.startsWith(`${factKey(objectiveId, requirement.id)}:`),
      );
    case "ordered-departure":
      return (
        departureReceiptSatisfied(profile, state, requirement) &&
        requirement.departingEntities.every((id) =>
          state.departedEntities.includes(id),
        )
      );
    case "derived-token":
      return requirement.outputEntities.every((id) => facts.includes(id));
    case "phase-deadline":
      return (
        state.phase === requirement.phase &&
        state.phaseEnteredAtSeconds !== null &&
        state.phaseElapsedSeconds <
          requirement.secondsByDifficulty[state.difficulty]
      );
    case "area-state":
      return (
        [...new Set(requirement.zones)].filter((id) => {
          const zone = state.zoneConditions[id];
          return (
            zone?.passable &&
            (requirement.state === "visited-and-passable"
              ? state.visitedZones.includes(id)
              : zone.controlled)
          );
        }).length >= requirement.requiredCount &&
        (requirement.blockingEnemies ?? []).every(
          (id) => state.entityStates[id] === "destroyed",
        )
      );
    case "civilian-protection":
      return requirement.zones.every(
        (id) => state.zoneConditions[id]?.protected === true,
      );
  }
}

export function objectiveSatisfied(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  objectiveId: string,
) {
  const objective = profile.objectivePlan.find(
    (item) => item.id === objectiveId,
  );
  return (
    !!objective &&
    (objective.predicate.exportedLedgers ?? []).every(
      (ledger) =>
        (state.exportedLedgers[factKey(objectiveId, ledger.id)]?.length ?? 0) >=
        ledger.minimumCount,
    ) &&
    objective.predicate.requirements.every((req) =>
      mainRequirementSatisfied(profile, state, objectiveId, req),
    )
  );
}

export function isActive(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  objectiveId: string,
) {
  const objective = profile.objectivePlan.find(
    (item) => item.id === objectiveId,
  );
  return (
    !!objective &&
    state.phase === objective.phase &&
    objective.after.every((id) => state.objectiveLatches.includes(id))
  );
}

export function hasIrrecoverableLoss(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
) {
  return (
    state.forbiddenEntries.length > 0 ||
    profile.objectivePlan.some((objective) =>
      objective.predicate.requirements.some(
        (req) =>
          req.kind === "civilian-protection" &&
          state.enteredPhases.includes(req.activeFrom) &&
          !state.enteredPhases.includes(req.activeUntil) &&
          req.zones.some(
            (zoneId) => state.zoneConditions[zoneId]?.protected === false,
          ),
      ),
    ) ||
    profile.objectivePlan.some((objective) =>
      objective.predicate.requirements.some(
        (req) =>
          req.kind === "area-state" &&
          req.mustRemainUntilObjective &&
          state.objectiveLatches.includes(objective.id) &&
          !state.objectiveLatches.includes(req.mustRemainUntilObjective) &&
          !mainRequirementSatisfied(profile, state, objective.id, req),
      ),
    ) ||
    profile.worldContract.survivorGroups.some(
      (group) =>
        [...new Set(group.entities)].filter(
          (id) =>
            state.entityStates[id] === "alive" ||
            state.entityStates[id] === "arrived",
        ).length < group.minimumAliveOrAlreadySafe,
    )
  );
}

export function departureReceiptSatisfied(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  req: Extract<MainRequirement, { kind: "ordered-departure" }>,
) {
  if (!req.receiptRequirement)
    return state.objectiveLatches.includes(req.receiptObjective);
  const receipt = objectiveRequirements(profile, req.receiptObjective)?.find(
    (item) => item.id === req.receiptRequirement,
  );
  return (
    !!receipt &&
    receipt.kind !== "ordered-departure" &&
    mainRequirementSatisfied(profile, state, req.receiptObjective, receipt)
  );
}

export function generationReady(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  entityId: string,
) {
  for (const objective of profile.objectivePlan)
    for (const req of objective.predicate.requirements) {
      if (
        req.kind === "derived-token" &&
        req.outputEntities.includes(entityId) &&
        !factsFor(state, objective.id, req.id).includes(entityId)
      )
        return false;
      if (req.kind === "entity-state")
        for (const receipt of req.generatedByReceipts ?? []) {
          if (
            receipt.output === entityId &&
            !hasArrival(state, receipt.receivedEntity, receipt.destination)
          )
            return false;
        }
    }
  return true;
}
