import { assertValid } from "../core/diagnostics.helper";
import { validateScenarioCapability } from "../gameplay-validation/scenario-capability.validator";
import {
  type CapabilityProfileV2,
  capabilityProfileV2Schema,
} from "../schemas/scenario-capability.schema";

/** Deterministic reference IR; IDs are preserved and no legacy approximation is emitted. */
export function compileCapabilityProfile(input: CapabilityProfileV2) {
  const profile = capabilityProfileV2Schema.parse(input);
  assertValid(validateScenarioCapability(profile));
  return {
    schemaVersion: 2 as const,
    profile: "composed-world-ledger" as const,
    districts: [...profile.districts].sort((a, b) => a.localeCompare(b)),
    worldContract: profile.worldContract,
    objectivePlan: profile.objectivePlan,
    stateMachine: profile.stateMachine,
    secondaryObjectives: profile.secondaryObjectives,
    secondaryBudget: profile.secondaryBudget,
    enemyRoster: profile.enemyRoster,
  };
}
