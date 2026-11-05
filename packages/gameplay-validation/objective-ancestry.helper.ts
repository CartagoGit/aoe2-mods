import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";

/** True for the same objective or a transitive mandatory predecessor. */
export function isSameOrRequiredPredecessor(
  profile: CapabilityProfileV2,
  fromObjective: string,
  objectiveId: string,
): boolean {
  if (fromObjective === objectiveId) return true;
  const objectives = new Map(
    profile.objectivePlan.map((item) => [item.id, item]),
  );
  const pending = [...(objectives.get(objectiveId)?.after ?? [])];
  const visited = new Set<string>();
  while (pending.length) {
    const id = pending.pop();
    if (!id || visited.has(id)) continue;
    if (id === fromObjective) return true;
    visited.add(id);
    pending.push(...(objectives.get(id)?.after ?? []));
  }
  return false;
}
