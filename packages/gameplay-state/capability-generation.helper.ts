import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";
import {
  factsFor,
  hasRequirementArrival,
  objectiveRequirements,
} from "./capability-ledgers.helper";
import type { CapabilitySnapshot } from "./capability-snapshot.schema";

/** A declared output is usable only after its exact producer has run. */
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
          if (receipt.output !== entityId) continue;
          const producer = objectiveRequirements(
            profile,
            receipt.fromObjective,
          )?.find((item) => item.id === receipt.fromRequirement);
          if (
            !producer ||
            producer.kind !== "entity-state" ||
            producer.state !== "arrived" ||
            producer.destinations?.[receipt.receivedEntity] !==
              receipt.destination ||
            !hasRequirementArrival(
              state,
              receipt.fromObjective,
              producer,
              receipt.receivedEntity,
            )
          )
            return false;
        }
    }
  return true;
}
