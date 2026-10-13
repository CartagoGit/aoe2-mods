import { type Issue, issue } from "../core/diagnostics.helper";
import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";

/** Detect receipt/departure/arrival cycles before a profile can be played. */
export function validateRequirementCausality(
  profile: CapabilityProfileV2,
): Issue[] {
  const key = (objective: string, requirement: string) =>
    JSON.stringify([objective, requirement]);
  const graph = new Map<string, string[]>();
  for (const objective of profile.objectivePlan) {
    for (const requirement of objective.predicate.requirements) {
      const dependencies: string[] = [];
      if (
        requirement.kind === "entity-state" &&
        requirement.arrivalAfterDeparture
      ) {
        const ref = requirement.arrivalAfterDeparture;
        dependencies.push(key(ref.objective, ref.requirement));
      }
      if (requirement.kind === "ordered-departure") {
        const source = profile.objectivePlan.find(
          (o) => o.id === requirement.receiptObjective,
        );
        if (requirement.receiptRequirement)
          dependencies.push(
            key(requirement.receiptObjective, requirement.receiptRequirement),
          );
        else
          dependencies.push(
            ...(source?.predicate.requirements ?? []).map((r) =>
              key(requirement.receiptObjective, r.id),
            ),
          );
      }
      graph.set(key(objective.id, requirement.id), dependencies);
    }
  }
  const active = new Set<string>();
  const complete = new Set<string>();
  const out: Issue[] = [];
  function visit(node: string): void {
    if (complete.has(node)) return;
    if (active.has(node)) {
      out.push(
        issue(
          "capability.requirement-cycle",
          node,
          "Recibo, salida y llegada forman una dependencia circular",
        ),
      );
      return;
    }
    active.add(node);
    for (const dependency of graph.get(node) ?? []) visit(dependency);
    active.delete(node);
    complete.add(node);
  }
  for (const node of graph.keys()) visit(node);
  return out;
}
