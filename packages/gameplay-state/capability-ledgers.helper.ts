import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";
import type { CapabilitySnapshot } from "./capability-snapshot.schema";

export const sortUnique = (values: readonly string[]) =>
  [...new Set(values)].sort();

export const asRecord = (record: Record<string, string[]>) =>
  Object.fromEntries(
    Object.entries(record).sort(([a], [b]) => a.localeCompare(b)),
  );

export function objectiveRequirements(
  profile: CapabilityProfileV2,
  objectiveId: string,
) {
  return profile.objectivePlan.find((o) => o.id === objectiveId)?.predicate
    .requirements;
}

export function factKey(objectiveId: string, requirementId: string) {
  return `${objectiveId}.${requirementId}`;
}

export function arrivalKey(phase: string, entityId: string, zoneId: string) {
  return `${phase}|${entityId}|${zoneId}`;
}

export function hasArrival(
  state: CapabilitySnapshot,
  entityId: string,
  zoneId: string,
) {
  return state.arrivalLedger.some((entry) =>
    entry.endsWith(`|${entityId}|${zoneId}`),
  );
}

export function factsFor(
  state: CapabilitySnapshot,
  objectiveId: string,
  requirementId: string,
) {
  return state.requirementFacts[factKey(objectiveId, requirementId)] ?? [];
}

export function addFact(
  state: CapabilitySnapshot,
  objectiveId: string,
  requirementId: string,
  value: string,
) {
  const key = factKey(objectiveId, requirementId);
  return asRecord({
    ...state.requirementFacts,
    [key]: sortUnique([...(state.requirementFacts[key] ?? []), value]),
  });
}

export function computeExportedLedgers(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
) {
  const ledgers: Record<string, string[]> = {};
  for (const objective of profile.objectivePlan)
    for (const ledger of objective.predicate.exportedLedgers ?? []) {
      const sets = ledger.fromRequirements.map((requirementId) => {
        const requirement = objective.predicate.requirements.find(
          (item) => item.id === requirementId,
        );
        if (requirement?.kind === "paired-delivery")
          return new Set(
            requirement.pairs
              .filter((pair) =>
                factsFor(state, objective.id, requirement.id).includes(
                  `${pair.cargo}:${pair.receiver}`,
                ),
              )
              .map((pair) => pair.receiver),
          );
        if (
          requirement?.kind !== "entity-state" ||
          requirement.state !== "arrived"
        )
          return new Set<string>();
        return new Set(
          requirement.entities.filter((id) =>
            hasArrival(state, id, requirement.destinations?.[id] ?? ""),
          ),
        );
      });
      const members = [...(sets[0] ?? [])].filter((id) =>
        sets.every((set) => set.has(id)),
      );
      ledgers[factKey(objective.id, ledger.id)] = members.sort();
    }
  return Object.fromEntries(
    Object.entries(ledgers).sort(([a], [b]) => a.localeCompare(b)),
  );
}
