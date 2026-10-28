/**
 * Test-only bridge between the design-source survivor projection and the
 * existing public loss evaluator.
 *
 * The Python design source emits a two-field survivor row; the public v2 row
 * additionally declares `loss`. This fixture adapts one artificial profile,
 * validates it with the public schema and validator, and then executes the
 * existing reducer so the observed terminal is real. It is not a production
 * mapper, an export path or a second survival rule.
 */

import { objectiveSatisfied } from "../../packages/gameplay-state/capability-predicates.validator";
import { createCapabilitySnapshot } from "../../packages/gameplay-state/capability-snapshot.factory";
import type { CapabilitySnapshot } from "../../packages/gameplay-state/capability-snapshot.schema";
import { reduceCapabilityState } from "../../packages/gameplay-state/capability-state.reducer";
import { livePresenceSatisfied } from "../../packages/gameplay-state/live-entity-presence.helper";
import { validateScenarioCapability } from "../../packages/gameplay-validation/scenario-capability.validator";
import type { LiveSpatialBatch } from "../../packages/schemas/live-spatial-batch.schema";
import {
  type CapabilityProfileV2,
  capabilityProfileV2Schema,
} from "../../packages/schemas/scenario-capability.schema";
import {
  actor,
  destinations,
  makeProfile,
  originalIds,
} from "./checkpoint-presence.fixture";

export type PooledBridgeEntity = {
  id: string;
  role: string;
  initialHub: string;
  offsetTiles: [number, number];
  identity: string;
};

export type PooledBridgeCourt = {
  group: string;
  originHub: string;
  entityIds: string[];
};

export type PooledBridgeSurvivorRow = {
  entities: string[];
  minimumAliveOrAlreadySafe: number;
};

export type PooledPublicSurvivorRow = PooledBridgeSurvivorRow & {
  loss: string;
};

export type PooledBridgeInput = {
  entities: PooledBridgeEntity[];
  survivorGroups: PooledBridgeSurvivorRow[];
  courts: PooledBridgeCourt[];
};

export type PooledTerminalObservation = {
  terminal: string | null;
  phase: string;
  alivePooled: number;
};

export type PooledBridgeObservation = {
  profile: {
    districts: string[];
    survivorGroups: PooledPublicSurvivorRow[];
    pooledEntities: {
      id: string;
      initialHub: string;
      offsetTiles: [number, number];
    }[];
    validatorIssues: string[];
  };
  lossScenarios: Record<
    string,
    {
      twoLosses: PooledTerminalObservation;
      thirdLoss: PooledTerminalObservation;
    }
  >;
  priority: {
    receiptOnly: {
      terminal: string | null;
      objectiveSatisfied: boolean;
      livePresenceSatisfied: boolean;
      objectiveLatches: string[];
    };
    latched: { terminal: string | null; objectiveLatches: string[] };
    controlTick: {
      terminal: string | null;
      phase: string;
      objectiveLatches: string[];
    };
    defeatTick: {
      terminal: string | null;
      phase: string;
      objectiveLatches: string[];
    };
  };
  negativeValidatorCases: Record<string, string[]>;
};

const accounts = {
  spendable: {},
  protectedRecovery: {},
  optionalReserve: {},
};

const OPTIONAL_IDENTITY_ID = "optional-helper-identity";

function presenceRequirement(profile: CapabilityProfileV2) {
  const requirement = profile.objectivePlan[0]?.predicate.requirements.find(
    (candidate) => candidate.kind === "current-entity-presence",
  );
  if (!requirement || requirement.kind !== "current-entity-presence")
    throw new Error(
      "Artificial profile has no current-entity-presence requirement",
    );
  return requirement;
}

function helperBatch(sequence: number): LiveSpatialBatch {
  return {
    sequence,
    entities: originalIds.map((entityId) => ({
      entityId,
      alive: true,
      zones: [destinations[entityId] ?? ""],
    })),
  };
}

function pooledBatch(
  sequence: number,
  aliveIds: string[],
  deadIds: string[],
): LiveSpatialBatch {
  return {
    sequence,
    entities: [
      ...helperBatch(sequence).entities,
      ...aliveIds.map((entityId) => ({ entityId, alive: true, zones: [] })),
      ...deadIds.map((entityId) => ({ entityId, alive: false, zones: [] })),
    ],
  };
}

function alivePooledCount(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
): number {
  const pool = profile.worldContract.survivorGroups.at(-1);
  if (!pool) throw new Error("Artificial profile has no survivor pool");
  return [...new Set(pool.entities)].filter(
    (id) =>
      state.entityStates[id] === "alive" ||
      state.entityStates[id] === "arrived",
  ).length;
}

function terminalObservation(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
): PooledTerminalObservation {
  return {
    terminal: state.terminal,
    phase: state.phase,
    alivePooled: alivePooledCount(profile, state),
  };
}

export function buildPooledProfile(
  input: PooledBridgeInput,
): CapabilityProfileV2 {
  const base = makeProfile();
  const pooledEntities = input.entities.map((entity) => ({
    ...actor(entity.id),
    role: entity.role,
    initialHub: entity.initialHub,
    offsetTiles: entity.offsetTiles,
    identity: entity.identity,
  }));
  const districts = [
    ...new Set([
      ...base.districts,
      ...pooledEntities.map((entity) => entity.initialHub),
    ]),
  ];
  const survivorGroups = [
    ...base.worldContract.survivorGroups,
    ...input.survivorGroups.map((row) => ({
      entities: [...row.entities],
      minimumAliveOrAlreadySafe: row.minimumAliveOrAlreadySafe,
      loss: "defeat",
    })),
  ];
  const secondaryObjectives = base.secondaryObjectives.map((side, index) =>
    index === 0
      ? {
          ...side,
          world: {
            ...side.world,
            entities: [
              ...side.world.entities,
              {
                ...actor(OPTIONAL_IDENTITY_ID),
                initialHub: side.reachability.originHub,
              },
            ],
          },
        }
      : side,
  );
  return capabilityProfileV2Schema.parse({
    ...base,
    districts,
    worldContract: {
      ...base.worldContract,
      entities: [...base.worldContract.entities, ...pooledEntities],
      survivorGroups,
    },
    secondaryObjectives,
  });
}

function startPhase(profile: CapabilityProfileV2): CapabilitySnapshot {
  const initial = createCapabilitySnapshot(profile, accounts);
  return reduceCapabilityState(profile, initial, {
    type: "enter-phase",
    phase: "phase-1",
    nowSeconds: 0,
  });
}

function destroyEntity(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  entityId: string,
): CapabilitySnapshot {
  return reduceCapabilityState(profile, state, {
    type: "destroy-entity",
    entityId,
  });
}

function lossScenario(
  profile: CapabilityProfileV2,
  toleratedIds: string[],
  thirdId: string,
) {
  let state = startPhase(profile);
  for (const entityId of toleratedIds)
    state = destroyEntity(profile, state, entityId);
  const twoLosses = terminalObservation(profile, state);
  state = destroyEntity(profile, state, thirdId);
  const thirdLoss = terminalObservation(profile, state);
  return { twoLosses, thirdLoss };
}

function priorityScenario(
  profile: CapabilityProfileV2,
  destroyedIds: string[],
  aliveIds: string[],
  thirdId: string,
) {
  let state = startPhase(profile);
  for (const entityId of destroyedIds)
    state = destroyEntity(profile, state, entityId);
  state = reduceCapabilityState(profile, state, {
    type: "record-arrival",
    entityId: "bundle-1",
    zoneId: "store-1",
  });
  const requirement = presenceRequirement(profile);
  const receiptOnly = {
    terminal: state.terminal,
    objectiveSatisfied: objectiveSatisfied(profile, state, "return"),
    livePresenceSatisfied: livePresenceSatisfied(profile, state, requirement),
    objectiveLatches: [...state.objectiveLatches],
  };
  state = reduceCapabilityState(profile, state, {
    type: "latch-objective",
    objectiveId: "return",
    liveSpatialBatch: helperBatch(1),
  });
  const latched = {
    terminal: state.terminal,
    objectiveLatches: [...state.objectiveLatches],
  };
  const prior = structuredClone(state);
  const control = reduceCapabilityState(profile, prior, {
    type: "tick",
    nowSeconds: 1,
    difficulty: "standard",
    defeatConditions: [],
    victoryConditions: ["return"],
    liveSpatialBatch: pooledBatch(2, aliveIds, []),
  });
  const defeat = reduceCapabilityState(profile, prior, {
    type: "tick",
    nowSeconds: 1,
    difficulty: "standard",
    defeatConditions: [],
    victoryConditions: ["return"],
    liveSpatialBatch: pooledBatch(2, aliveIds, [thirdId]),
  });
  return {
    receiptOnly,
    latched,
    controlTick: {
      terminal: control.terminal,
      phase: control.phase,
      objectiveLatches: [...control.objectiveLatches],
    },
    defeatTick: {
      terminal: defeat.terminal,
      phase: defeat.phase,
      objectiveLatches: [...defeat.objectiveLatches],
    },
  };
}

function negativeValidatorCases(profile: CapabilityProfileV2) {
  const cases: Record<string, (group: PooledBridgeSurvivorRow) => void> = {
    duplicateIdentity: (group) => {
      const first = group.entities[0];
      if (first === undefined) throw new Error("Pool has no first identity");
      group.entities = [...group.entities, first];
    },
    unknownIdentity: (group) => {
      group.entities = [
        ...group.entities,
        "artificial.pooled-originals.absent-1",
      ];
    },
    oversizedMinimum: (group) => {
      group.minimumAliveOrAlreadySafe = group.entities.length + 1;
    },
    optionalIdentity: (group) => {
      group.entities = [...group.entities, OPTIONAL_IDENTITY_ID];
    },
  };
  const observed: Record<string, string[]> = {};
  for (const [name, mutate] of Object.entries(cases)) {
    const candidate = structuredClone(profile);
    const group = candidate.worldContract.survivorGroups.at(-1);
    if (!group) throw new Error("Artificial profile has no survivor pool");
    mutate(group);
    observed[name] = validateScenarioCapability(candidate).map(
      (item) => item.code,
    );
  }
  return observed;
}

export function observePooledSurvivorProjection(
  input: PooledBridgeInput,
): PooledBridgeObservation {
  const profile = buildPooledProfile(input);
  const validatorIssues = validateScenarioCapability(profile).map(
    (item) => item.code,
  );
  const courts = input.courts;
  const first = courts[0];
  const second = courts[1];
  const third = courts[2];
  if (!first || !second || !third)
    throw new Error("Artificial fixture needs four courts");
  const westOne = first.entityIds[0];
  const westTwo = first.entityIds[1];
  const eastOne = second.entityIds[0];
  const southOne = third.entityIds[0];
  if (!westOne || !westTwo || !eastOne || !southOne)
    throw new Error("Artificial fixture needs two identities per court");
  const pool = profile.worldContract.survivorGroups.at(-1);
  if (!pool) throw new Error("Artificial profile has no survivor pool");
  const crossCourt = [westOne, eastOne];
  const sameCourt = [westOne, westTwo];
  const destroyed = [...crossCourt];
  const remaining = pool.entities.filter((id) => !destroyed.includes(id));
  const controlThird = remaining[0];
  if (!controlThird)
    throw new Error("Artificial fixture needs a remaining pooled identity");
  const controlAlive = remaining.filter((id) => id !== controlThird);
  return {
    profile: {
      districts: [...profile.districts],
      survivorGroups: profile.worldContract.survivorGroups.map((group) => ({
        entities: [...group.entities],
        minimumAliveOrAlreadySafe: group.minimumAliveOrAlreadySafe,
        loss: group.loss,
      })),
      pooledEntities: input.entities.map((entity) => ({
        id: entity.id,
        initialHub: entity.initialHub,
        offsetTiles: entity.offsetTiles,
      })),
      validatorIssues,
    },
    lossScenarios: {
      crossCourt: lossScenario(profile, crossCourt, southOne),
      sameCourt: lossScenario(profile, sameCourt, eastOne),
    },
    priority: priorityScenario(profile, destroyed, controlAlive, controlThird),
    negativeValidatorCases: negativeValidatorCases(profile),
  };
}

async function readStdin(): Promise<string> {
  const chunks: Uint8Array[] = [];
  for await (const chunk of process.stdin) {
    chunks.push(typeof chunk === "string" ? Buffer.from(chunk) : chunk);
  }
  return Buffer.concat(chunks).toString("utf8");
}

if (import.meta.main) {
  try {
    const input = JSON.parse(await readStdin()) as PooledBridgeInput;
    process.stdout.write(
      `${JSON.stringify(observePooledSurvivorProjection(input))}\n`,
    );
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    process.stderr.write(
      `pooled survivor reference bridge failed: ${message}\n`,
    );
    process.exitCode = 1;
  }
}
