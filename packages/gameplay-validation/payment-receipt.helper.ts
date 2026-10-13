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
