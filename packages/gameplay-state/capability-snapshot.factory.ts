import { canonical, hash } from "../core/serialization.helper";
import type {
  CapabilityProfileV2,
  ResourceAmounts,
} from "../schemas/scenario-capability.schema";
import {
  asRecord,
  computeExportedLedgers,
  sortUnique,
} from "./capability-ledgers.helper";
import {
  type CapabilitySnapshot,
  capabilitySnapshotSchema,
} from "./capability-snapshot.schema";
import {
  EMPTY_RESOURCES,
  normalizeResources,
} from "./resource-accounts.helper";

export function createCapabilitySnapshot(
  profile: CapabilityProfileV2,
  accounts: {
    spendable: ResourceAmounts;
    protectedRecovery: ResourceAmounts;
    optionalReserve: ResourceAmounts;
  },
  phase = "briefing",
): CapabilitySnapshot {
  const entityStates: Record<string, "alive"> = {};
  for (const entity of profile.worldContract.entities)
    entityStates[entity.id] = "alive";
  for (const objective of profile.secondaryObjectives)
    for (const entity of objective.world.entities)
      entityStates[entity.id] = "alive";
  const snapshot: CapabilitySnapshot = {
    schemaVersion: 2,
    profile: "composed-world-ledger",
    contractFingerprint: capabilityFingerprint(profile),
    phase,
    phaseEnteredAtSeconds: null,
    phaseElapsedSeconds: 0,
    difficulty: "standard",
    terminal: null,
    objectiveLatches: [],
    requirementFacts: {},
    entityStates,
    arrivedEntities: {},
    arrivalLedger: [],
    exportedLedgers: {},
    observedEntityStates: {},
    zoneConditions: {},
    enteredPhases: [phase],
    visitedZones: [],
    forbiddenEntries: [],
    paidReceipts: [],
    spendable: {
      ...EMPTY_RESOURCES,
      ...normalizeResources(accounts.spendable),
    },
    protectedRecovery: {
      ...EMPTY_RESOURCES,
      ...normalizeResources(accounts.protectedRecovery),
    },
    optionalReserve: {
      ...EMPTY_RESOURCES,
      ...normalizeResources(accounts.optionalReserve),
    },
    secondaryStates: Object.fromEntries(
      profile.secondaryObjectives.map((o) => [o.id, "available"]),
    ),
    rewardFlags: [],
    releasedRosterIds: [],
    resolvedWaves: [],
    selectedRoutes: {},
    heldSeconds: {},
    deadlineWarnings: [],
    departedEntities: [],
  };
  return finalize(profile, snapshot);
}

export function closeAvailableSecondaries(
  state: CapabilitySnapshot,
): CapabilitySnapshot["secondaryStates"] {
  return Object.fromEntries(
    Object.entries(state.secondaryStates).map(([id, value]) => [
      id,
      value === "available" ? "closed-at-terminal" : value,
    ]),
  );
}

export function finalize(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
): CapabilitySnapshot {
  return capabilitySnapshotSchema.parse({
    ...state,
    objectiveLatches: sortUnique(state.objectiveLatches),
    arrivalLedger: sortUnique(state.arrivalLedger),
    exportedLedgers: computeExportedLedgers(profile, state),
    visitedZones: sortUnique(state.visitedZones),
    forbiddenEntries: sortUnique(state.forbiddenEntries),
    paidReceipts: sortUnique(state.paidReceipts),
    rewardFlags: sortUnique(state.rewardFlags),
    releasedRosterIds: sortUnique(state.releasedRosterIds),
    resolvedWaves: sortUnique(state.resolvedWaves),
    deadlineWarnings: sortUnique(state.deadlineWarnings),
    departedEntities: sortUnique(state.departedEntities),
    requirementFacts: asRecord(state.requirementFacts),
    observedEntityStates: asRecord(state.observedEntityStates),
    enteredPhases: sortUnique(state.enteredPhases),
    entityStates: Object.fromEntries(
      Object.entries(state.entityStates).sort(([a], [b]) => a.localeCompare(b)),
    ),
    arrivedEntities: Object.fromEntries(
      Object.entries(state.arrivedEntities).sort(([a], [b]) =>
        a.localeCompare(b),
      ),
    ),
    secondaryStates: Object.fromEntries(
      Object.entries(state.secondaryStates).sort(([a], [b]) =>
        a.localeCompare(b),
      ),
    ),
    selectedRoutes: Object.fromEntries(
      Object.entries(state.selectedRoutes).sort(([a], [b]) =>
        a.localeCompare(b),
      ),
    ),
    heldSeconds: Object.fromEntries(
      Object.entries(state.heldSeconds).sort(([a], [b]) => a.localeCompare(b)),
    ),
  });
}

export function finishTerminal(
  state: CapabilitySnapshot,
  terminal: "victory" | "defeat",
): CapabilitySnapshot {
  return {
    ...state,
    phase: terminal,
    terminal,
    secondaryStates: closeAvailableSecondaries(state),
  };
}

export function capabilityFingerprint(profile: CapabilityProfileV2) {
  return hash(
    canonical({
      profile: profile.profile,
      schemaVersion: profile.schemaVersion,
      districts: profile.districts,
      world: profile.worldContract,
      objectives: profile.objectivePlan.map((objective) => ({
        id: objective.id,
        after: objective.after,
        phase: objective.phase,
        predicate: objective.predicate,
      })),
      phases: profile.stateMachine,
      secondary: profile.secondaryObjectives.map((objective) => ({
        id: objective.id,
        world: objective.world,
        predicate: objective.predicate,
        effects: objective.effects,
        state: objective.stateContract,
      })),
      budget: profile.secondaryBudget,
      roster: profile.enemyRoster,
    }),
  );
}
