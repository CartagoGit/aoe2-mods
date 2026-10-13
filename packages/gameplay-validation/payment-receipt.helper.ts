import type {
  CapabilityProfileV2,
  WorldPredicate,
} from "../schemas/scenario-capability.schema";

/** Bind a receipt query to its unique producer and exact resource vector. */
export function paymentReceiptMatches(
  profile: CapabilityProfileV2,
  query: Pick<
    Extract<WorldPredicate, { kind: "receipt-exists" }>,
    "flag" | "fromObjective" | "amounts"
  >,
): boolean {
  const producers = profile.objectivePlan.flatMap((objective) =>
    objective.predicate.requirements.flatMap((requirement) =>
      requirement.kind === "resource-transaction" &&
      requirement.paidFlag === query.flag
        ? [{ objectiveId: objective.id, requirement }]
        : [],
    ),
  );
  const producer = producers[0];
  return (
    producers.length === 1 &&
    !!producer &&
    producer.objectiveId === query.fromObjective &&
    (["food", "wood", "gold", "stone"] as const).every(
      (resource) =>
        (producer.requirement.amounts[resource] ?? 0) ===
        (query.amounts[resource] ?? 0),
    )
  );
}

/** A production payment cannot depend on a later or unrelated objective. */
export function paymentReceiptPrecedesObjective(
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
