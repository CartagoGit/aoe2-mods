import { describe, expect, test } from "bun:test";
import { createCapabilitySnapshot } from "../../packages/gameplay-state/capability-snapshot.factory";
import { reduceCapabilityState } from "../../packages/gameplay-state/capability-state.reducer";
import { validateScenarioCapability } from "../../packages/gameplay-validation/scenario-capability.validator";
import { compileCapabilityProfile } from "../../packages/scenario-compiler/capability.compiler";
import type { LiveSpatialBatch } from "../../packages/schemas/live-spatial-batch.schema";
import { capabilityProfileV2Schema } from "../../packages/schemas/scenario-capability.schema";

const actor = (id: string) => ({
  id,
  role: "civilian",
  initialHub: "hub",
  offsetTiles: [0, 0] as [number, number],
  identity: id,
  finite: true as const,
  replacement: "none",
  initiallyDelivered: false as const,
  originRule: "original actor",
});
const zone = (id: string, x: number) => ({
  id,
  hub: "hub",
  offsetTiles: [x, 20] as [number, number],
  radiusTiles: 2,
  placement: "reference zone only",
  protectedCivilian: false,
});
const originalIds = [
  "bundle-1",
  "bundle-2",
  "bundle-3",
  "custodian-1",
  "custodian-2",
  "custodian-3",
];
const destinations = Object.fromEntries(
  originalIds.map((id, index) => [id, `store-${(index % 3) + 1}`]),
);

function side(index: number) {
  const id = `side-${index}`;
  const sideZone = `${id}-zone`;
  return {
    id,
    kind: "scout",
    title: { en: "Scout", "es-ES": "Explorar" },
    subject: { en: "Route", "es-ES": "Ruta" },
    classification: "optional",
    rationale: { en: "Optional", "es-ES": "Opcional" },
    text: { en: "Visit", "es-ES": "Visitar" },
    mandatory: false,
    activation: "available",
    dependencies: [],
    predicate: {
      operator: "all",
      requirements: [
        {
          kind: "visit-zones",
          zones: [sideZone],
          actor: "any-player-controlled-unit",
          requiredCount: 1,
          observationsPersistent: true,
          countInitialVisibility: false,
        },
      ],
      neverUseTimerInstead: true,
    },
    world: { entities: [], zones: [zone(sideZone, 80 + index * 10)] },
    effects: [
      {
        kind: "unlock-context-and-hint",
        target: "hint",
        resources: {},
        onceFlag: `${id}-reward`,
        funding: "reserved-optional-stock",
        changesHistoricalOutcome: false,
      },
    ],
    completionFlag: `${id}-complete`,
    stateContract: {
      states: [
        "available",
        "completed",
        "failed-optional",
        "closed-at-terminal",
      ],
      requiresNonterminalScenario: true,
      persistentAcrossSave: true,
      completionAndEffectsAtomic: true,
      paymentBeforeReward: true,
      paymentIsNotCompletion: true,
      failedGoalCannotReward: true,
      latchAtFirstCompletion: true,
      noMainVictoryDependency: true,
      rewardTransaction: [
        "verify all predicate ledgers and nonterminal state",
        "verify reserved stock",
        "debit reserved stock",
        "credit spendable stock",
        "set reward onceFlag",
        "set completionFlag",
      ],
      transactionIsolation: "atomic",
      persistentLedgers: ["visits"],
      terminalPriority: "defeat first",
    },
    unavailablePolicy: "unavailable",
    terminalPolicy: "close",
    difficultyPolicy: "fixed",
    reachability: {
      originHub: "hub",
      receivingHub: "hub",
      corridorIds: [`${id}-corridor`],
      maxRequiredRoundTrips: 0,
      spawnOutsideReceivingZone: true,
      placementGate: "review",
    },
    qa: ["visit once"],
  };
}

function makeProfile() {
  return capabilityProfileV2Schema.parse({
    profile: "composed-world-ledger",
    schemaVersion: 2,
    districts: ["hub"],
    worldContract: {
      version: 1,
      classification: "authoring specification, not implemented DSL",
      entities: [...originalIds, "lookalike"].map(actor),
      zones: [zone("store-1", 20), zone("store-2", 40), zone("store-3", 60)],
      ledgerPolicy: "arrival history separate from current presence",
      resourcePolicy: "finite",
      defeatPolicy: "defeat first",
      earlyDelivery: "record original receipt",
      survivorGroups: [],
      enemyBinding: "none",
    },
    objectivePlan: [
      {
        id: "return",
        text: { en: "Return", "es-ES": "Volver" },
        after: [],
        targetHub: "hub",
        phase: "phase-1",
        completion: "six originals presently assigned",
        countLedger: { id: "actors", oncePerEntity: true, required: 6 },
        earlyCompletion: "only after fresh observation",
        effect: "complete",
        capability: "reference presence",
        operation: "return",
        threshold: 6,
        entities: originalIds.map(actor),
        predicate: {
          operator: "all",
          operation: "return",
          requiredCount: 6,
          defeatBelowRemaining: null,
          resourceAmounts: {},
          phaseGated: true,
          neverUseTimerInstead: true,
          requirements: [
            {
              id: "first-receipt",
              kind: "entity-state",
              state: "arrived",
              entities: ["bundle-1"],
              requiredCount: 1,
              oncePerEntity: true,
              destinations: { "bundle-1": "store-1" },
            },
            {
              id: "stores-current",
              kind: "current-entity-presence",
              entities: originalIds,
              destinations,
              requiredCount: 6,
            },
          ],
          requiredLedgers: ["first-receipt", "stores-current"],
          allRequired: true,
        },
      },
    ],
    stateMachine: {
      states: ["briefing", "phase-1", "victory", "defeat"],
      transitions: [
        "briefing → phase-1",
        "phase-1 → victory",
        "phase-1 → defeat",
      ],
      phaseTransitions: [
        { from: "briefing", to: "phase-1", on: "intro-accepted" },
        {
          from: "phase-1",
          to: "victory",
          on: "objective-latched",
          objectiveId: "return",
        },
      ],
      terminalPriority:
        "defeat evaluated first; one terminal latch, choice order documented",
      saveLoad: "snapshot v2",
      phaseClock: "relative",
    },
    secondaryObjectives: Array.from({ length: 6 }, (_, index) =>
      side(index + 1),
    ),
    secondaryBudget: {
      reservedRewards: {},
      maxOptionalCosts: {},
      reallocatedCacheAllowance: {},
      fundingPolicy: "finite",
      nativeStatus:
        "design-only; requires certified reusable predicates and native QA",
    },
    enemyRoster: {
      initialEntityIds: [],
      productionEnabled: false,
      mobilizations: [],
      unspentPolicy: "remain-in-reserve",
    },
  });
}

const completeBatch = (sequence: number): LiveSpatialBatch => ({
  sequence,
  entities: originalIds.map((entityId) => ({
    entityId,
    alive: true,
    zones: [destinations[entityId] ?? ""],
  })),
});
function firstEntity(batch: LiveSpatialBatch) {
  const first = batch.entities[0];
  if (!first) throw new Error("Test batch has no first entity");
  return first;
}
const base = makeProfile();
function presenceRequirement(profile: typeof base) {
  const requirement = profile.objectivePlan[0]?.predicate.requirements.find(
    (candidate) => candidate.kind === "current-entity-presence",
  );
  if (!requirement || requirement.kind !== "current-entity-presence")
    throw new Error("Test profile has no live presence requirement");
  return requirement;
}
const start = () => {
  const initial = createCapabilitySnapshot(base, {
    spendable: {},
    protectedRecovery: {},
    optionalReserve: {},
  });
  return reduceCapabilityState(base, initial, {
    type: "enter-phase",
    phase: "phase-1",
    nowSeconds: 0,
  });
};
const arrive = (state: ReturnType<typeof start>) =>
  reduceCapabilityState(base, state, {
    type: "record-arrival",
    entityId: "bundle-1",
    zoneId: "store-1",
  });
const latch = (state: ReturnType<typeof start>, batch?: LiveSpatialBatch) =>
  reduceCapabilityState(base, state, {
    type: "latch-objective",
    objectiveId: "return",
    ...(batch ? { liveSpatialBatch: batch } : {}),
  });
const tick = (state: ReturnType<typeof start>, batch?: LiveSpatialBatch) =>
  reduceCapabilityState(base, state, {
    type: "tick",
    nowSeconds: 1,
    difficulty: "standard",
    defeatConditions: [],
    victoryConditions: ["return"],
    ...(batch ? { liveSpatialBatch: batch } : {}),
  });

describe("live entity presence reference", () => {
  test("schema and compiler accept current presence while preserving source profile version", () => {
    expect(validateScenarioCapability(base)).toEqual([]);
    expect(compileCapabilityProfile(base).schemaVersion).toBe(2);
    expect(base.schemaVersion).toBe(2);
    const wrongKind = structuredClone(base);
    Object.assign(presenceRequirement(wrongKind), {
      kind: "live-entity-presence",
    });
    expect(capabilityProfileV2Schema.safeParse(wrongKind).success).toBe(false);
  });

  test("arrival remains historical after departure; return of the same six originals restores current presence", () => {
    const delivered = arrive(start());
    const elsewhere = completeBatch(1);
    firstEntity(elsewhere).zones = ["store-2"];
    const left = latch(delivered, elsewhere);
    expect(left.objectiveLatches).toEqual([]);
    expect(left.arrivalLedger).toEqual(delivered.arrivalLedger);
    expect(left.arrivedEntities).toEqual(delivered.arrivedEntities);
    expect(latch(left).objectiveLatches).toEqual([]);
    expect(latch(left, completeBatch(2)).objectiveLatches).toEqual(["return"]);
  });

  test("one actor per assigned store; substitutes, empty membership and unobserved originals cannot fill the count", () => {
    const delivered = arrive(start());
    const sameStore = completeBatch(1);
    sameStore.entities.forEach((item) => {
      item.zones = ["store-1"];
    });
    expect(latch(delivered, sameStore).objectiveLatches).toEqual([]);
    const substitute = completeBatch(2);
    substitute.entities.shift();
    substitute.entities.push({
      entityId: "lookalike",
      alive: true,
      zones: ["store-1"],
    });
    expect(latch(delivered, substitute).objectiveLatches).toEqual([]);
    const outside = completeBatch(3);
    firstEntity(outside).zones = [];
    expect(latch(delivered, outside).objectiveLatches).toEqual([]);
  });

  test("a declared derived identity counts only after its collected input is derived", () => {
    const profile = structuredClone(base);
    const producer = structuredClone(profile.objectivePlan[0]);
    if (!producer) throw new Error("Missing producer objective");
    producer.id = "producer";
    producer.after = [];
    producer.predicate.requirements = [
      {
        id: "collect-input",
        kind: "entity-state",
        state: "collected",
        entities: ["lookalike"],
        requiredCount: 1,
        oncePerEntity: true,
      },
      {
        id: "derive-custodian",
        kind: "derived-token",
        inputEntities: ["lookalike"],
        outputEntities: ["custodian-1"],
        once: true,
        deriveWhen: "after the named input is collected",
      },
    ];
    producer.predicate.requiredLedgers = ["collect-input", "derive-custodian"];
    profile.objectivePlan.push(producer);
    expect(validateScenarioCapability(profile)).toEqual([]);
    let state = createCapabilitySnapshot(profile, {
      spendable: {},
      protectedRecovery: {},
      optionalReserve: {},
    });
    state = reduceCapabilityState(profile, state, {
      type: "enter-phase",
      phase: "phase-1",
      nowSeconds: 0,
    });
    state = reduceCapabilityState(profile, state, {
      type: "record-arrival",
      entityId: "bundle-1",
      zoneId: "store-1",
    });
    const attempt = (sequence: number) =>
      ({
        type: "latch-objective",
        objectiveId: "return",
        liveSpatialBatch: completeBatch(sequence),
      }) as const;
    state = reduceCapabilityState(profile, state, attempt(1));
    expect(state.objectiveLatches).toEqual([]);
    state = reduceCapabilityState(profile, state, {
      type: "observe-entity-state",
      objectiveId: "producer",
      requirementId: "collect-input",
      entityId: "lookalike",
    });
    state = reduceCapabilityState(profile, state, attempt(2));
    expect(state.objectiveLatches).toEqual([]);
    state = reduceCapabilityState(profile, state, {
      type: "derive-token",
      objectiveId: "producer",
      requirementId: "derive-custodian",
    });
    expect(state.requirementFacts["producer.derive-custodian"]).toEqual([
      "custodian-1",
    ]);
    const saved = JSON.parse(JSON.stringify(state));
    expect(
      reduceCapabilityState(profile, saved, attempt(3)).objectiveLatches,
    ).toEqual(["return"]);
  });

  test("a generated receipt needs its exact originating arrival before presence can count", () => {
    const profile = structuredClone(base);
    const producer = structuredClone(profile.objectivePlan[0]);
    if (!producer) throw new Error("Missing producer objective");
    producer.id = "producer";
    producer.after = [];
    producer.predicate.requirements = [
      {
        id: "wagon",
        kind: "entity-state",
        state: "arrived",
        entities: ["lookalike"],
        requiredCount: 1,
        oncePerEntity: true,
        destinations: { lookalike: "store-1" },
      },
      {
        id: "generated-custodian",
        kind: "entity-state",
        state: "arrived",
        entities: ["custodian-1"],
        requiredCount: 1,
        oncePerEntity: true,
        destinations: { "custodian-1": "store-1" },
        generatedByReceipts: [
          {
            fromObjective: "producer",
            fromRequirement: "wagon",
            receivedEntity: "lookalike",
            destination: "store-1",
            output: "custodian-1",
          },
        ],
      },
    ];
    producer.predicate.requiredLedgers = ["wagon", "generated-custodian"];
    profile.objectivePlan.push(producer);
    expect(validateScenarioCapability(profile)).toEqual([]);
    let state = createCapabilitySnapshot(profile, {
      spendable: {},
      protectedRecovery: {},
      optionalReserve: {},
    });
    state = reduceCapabilityState(profile, state, {
      type: "enter-phase",
      phase: "phase-1",
      nowSeconds: 0,
    });
    state = reduceCapabilityState(profile, state, {
      type: "record-arrival",
      entityId: "bundle-1",
      zoneId: "store-1",
    });
    const attempt = (sequence: number) =>
      reduceCapabilityState(profile, state, {
        type: "latch-objective",
        objectiveId: "return",
        liveSpatialBatch: completeBatch(sequence),
      });
    expect(attempt(1).objectiveLatches).toEqual([]);
    state = reduceCapabilityState(profile, state, {
      type: "record-arrival",
      entityId: "lookalike",
      zoneId: "store-2",
    });
    expect(attempt(2).objectiveLatches).toEqual([]);
    state = reduceCapabilityState(profile, state, {
      type: "record-arrival",
      entityId: "lookalike",
      zoneId: "store-1",
    });
    expect(state.requirementFacts["producer.wagon"]).toEqual(["lookalike"]);
    expect(attempt(3).objectiveLatches).toEqual(["return"]);
  });

  test("a six-of-eight quorum accepts six live originals without observing the other two", () => {
    const profile = structuredClone(base);
    const extras = ["custodian-4", "custodian-5"];
    profile.worldContract.entities.push(...extras.map(actor));
    const requirement = presenceRequirement(profile);
    requirement.entities.push(...extras);
    requirement.destinations["custodian-4"] = "store-1";
    requirement.destinations["custodian-5"] = "store-2";
    expect(validateScenarioCapability(profile)).toEqual([]);
    let state = createCapabilitySnapshot(profile, {
      spendable: {},
      protectedRecovery: {},
      optionalReserve: {},
    });
    state = reduceCapabilityState(profile, state, {
      type: "enter-phase",
      phase: "phase-1",
      nowSeconds: 0,
    });
    state = reduceCapabilityState(profile, state, {
      type: "record-arrival",
      entityId: "bundle-1",
      zoneId: "store-1",
    });
    state = reduceCapabilityState(profile, state, {
      type: "latch-objective",
      objectiveId: "return",
      liveSpatialBatch: completeBatch(1),
    });
    expect(state.objectiveLatches).toEqual(["return"]);
    expect(
      Object.keys(state.liveSpatialObservation?.entities ?? {}),
    ).toHaveLength(6);
  });

  test("partial batch replaces old positive positions; stale, duplicate and unknown input fail closed", () => {
    const delivered = arrive(start());
    const observed = reduceCapabilityState(base, delivered, {
      type: "observe-live-spatial-batch",
      liveSpatialBatch: completeBatch(5),
    });
    expect(observed.liveSpatialObservation?.sequence).toBe(5);
    expect(latch(observed).objectiveLatches).toEqual([]);
    const partial = reduceCapabilityState(base, observed, {
      type: "observe-live-spatial-batch",
      liveSpatialBatch: {
        sequence: 6,
        entities: completeBatch(6).entities.slice(0, 2),
      },
    });
    expect(
      Object.keys(partial.liveSpatialObservation?.entities ?? {}),
    ).toHaveLength(2);
    expect(
      latch(partial, {
        sequence: 7,
        entities: completeBatch(7).entities.slice(0, 2),
      }).objectiveLatches,
    ).toEqual([]);
    const stale = latch(partial, completeBatch(6));
    expect(stale).toEqual(partial);
    const duplicate = completeBatch(7);
    duplicate.entities.push({ ...firstEntity(duplicate) });
    expect(latch(partial, duplicate)).toEqual(partial);
    const unknown = completeBatch(7);
    unknown.entities.push({ entityId: "intruder", alive: true, zones: [] });
    expect(latch(partial, unknown)).toEqual(partial);
    const badZone = completeBatch(7);
    firstEntity(badZone).zones = ["unknown-zone"];
    expect(latch(partial, badZone)).toEqual(partial);
    const repeatedZone = completeBatch(7);
    firstEntity(repeatedZone).zones = ["store-1", "store-1"];
    expect(latch(partial, repeatedZone)).toEqual(partial);
    const inconsistentDeath = completeBatch(7);
    firstEntity(inconsistentDeath).alive = false;
    expect(latch(partial, inconsistentDeath)).toEqual(partial);
    expect(
      latch(partial, {
        ...completeBatch(7),
        sequence: Number.MAX_SAFE_INTEGER + 1,
      }),
    ).toEqual(partial);
    const malformedStatus = completeBatch(7) as unknown as {
      sequence: number;
      entities: unknown[];
    };
    malformedStatus.entities[0] = {
      entityId: "bundle-1",
      alive: "yes",
      zones: ["store-1"],
    };
    expect(latch(partial, malformedStatus as LiveSpatialBatch)).toEqual(
      partial,
    );
  });

  test("saved positive membership cannot latch or win without a new sequence; moving after latch blocks terminal", () => {
    const delivered = arrive(start());
    const latched = latch(delivered, completeBatch(1));
    expect(latched.objectiveLatches).toEqual(["return"]);
    const saved = JSON.parse(JSON.stringify(latched));
    expect(tick(saved).terminal).toBeNull();
    expect(
      tick(saved, {
        sequence: 2,
        entities: completeBatch(2).entities.slice(0, 2),
      }).terminal,
    ).toBeNull();
    const moved = completeBatch(2);
    firstEntity(moved).zones = ["store-2"];
    const continued = tick(saved, moved);
    expect(continued.terminal).toBeNull();
    expect(continued.arrivalLedger).toEqual(latched.arrivalLedger);
    const staleTick = tick(saved, completeBatch(1));
    expect(staleTick.terminal).toBeNull();
    expect(staleTick.phaseElapsedSeconds).toBe(1);
    expect(staleTick.liveSpatialObservation).toEqual(
      saved.liveSpatialObservation,
    );
    expect(tick(saved, completeBatch(2)).terminal).toBe("victory");
    expect(
      reduceCapabilityState(base, saved, {
        type: "enter-phase",
        phase: "victory",
        nowSeconds: 1,
      }).terminal,
    ).toBeNull();
    expect(
      reduceCapabilityState(base, saved, {
        type: "enter-phase",
        phase: "victory",
        nowSeconds: 1,
        liveSpatialBatch: moved,
      }).terminal,
    ).toBeNull();
  });

  test("batch application leaves the caller snapshot and input observations unchanged", () => {
    const delivered = arrive(start());
    const prior = structuredClone(delivered);
    const batch = completeBatch(1);
    const priorBatch = structuredClone(batch);
    latch(delivered, batch);
    expect(delivered).toEqual(prior);
    expect(batch).toEqual(priorBatch);
  });

  test("observed death is irreversible and wins no same-tick victory", () => {
    const delivered = arrive(start());
    const dead = completeBatch(1);
    firstEntity(dead).alive = false;
    firstEntity(dead).zones = [];
    const state = latch(delivered, dead);
    expect(state.entityStates["bundle-1"]).toBe("destroyed");
    expect(state.objectiveLatches).toEqual([]);
    expect(latch(state, completeBatch(2))).toEqual(state);
    const protectedProfile = structuredClone(base);
    protectedProfile.worldContract.survivorGroups.push({
      entities: originalIds,
      minimumAliveOrAlreadySafe: 6,
      loss: "defeat",
    });
    const protectedStart = createCapabilitySnapshot(protectedProfile, {
      spendable: {},
      protectedRecovery: {},
      optionalReserve: {},
    });
    const protectedEntered = reduceCapabilityState(
      protectedProfile,
      protectedStart,
      {
        type: "enter-phase",
        phase: "phase-1",
        nowSeconds: 0,
      },
    );
    const sameTick = reduceCapabilityState(protectedProfile, protectedEntered, {
      type: "tick",
      nowSeconds: 1,
      difficulty: "standard",
      defeatConditions: [],
      victoryConditions: ["return"],
      liveSpatialBatch: dead,
    });
    expect(sameTick.terminal).toBe("defeat");
    const malformed = completeBatch(1);
    malformed.entities.push({ ...firstEntity(malformed) });
    const explicitDefeat = reduceCapabilityState(base, delivered, {
      type: "tick",
      nowSeconds: 1,
      difficulty: "standard",
      defeatConditions: ["loss"],
      victoryConditions: ["return"],
      liveSpatialBatch: malformed,
    });
    expect(explicitDefeat.terminal).toBe("defeat");
  });

  test("invalid or stale presence batches cannot suppress an expired deadline or certify victory", () => {
    const profile = structuredClone(base);
    const watch = structuredClone(profile.objectivePlan[0]);
    if (!watch) throw new Error("Missing deadline objective");
    watch.id = "deadline-watch";
    watch.after = [];
    watch.predicate.requirements = [
      {
        id: "deadline",
        kind: "phase-deadline",
        phase: "phase-1",
        clock: "relative-to-phase-entry",
        onExpiry: "defeat",
        secondsByDifficulty: { easy: 10, standard: 10, hard: 10 },
        warningSeconds: 2,
      },
    ];
    watch.predicate.requiredLedgers = ["deadline"];
    profile.objectivePlan.push(watch);
    expect(validateScenarioCapability(profile)).toEqual([]);
    let state = createCapabilitySnapshot(profile, {
      spendable: {},
      protectedRecovery: {},
      optionalReserve: {},
    });
    state = reduceCapabilityState(profile, state, {
      type: "enter-phase",
      phase: "phase-1",
      nowSeconds: 0,
    });
    state = reduceCapabilityState(profile, state, {
      type: "record-arrival",
      entityId: "bundle-1",
      zoneId: "store-1",
    });
    const latched = reduceCapabilityState(profile, state, {
      type: "latch-objective",
      objectiveId: "return",
      liveSpatialBatch: completeBatch(1),
    });
    expect(latched.objectiveLatches).toEqual(["return"]);
    const duplicate = completeBatch(2);
    duplicate.entities.push({ ...firstEntity(duplicate) });
    for (const prior of [state, latched, JSON.parse(JSON.stringify(latched))])
      for (const batch of prior === state
        ? [duplicate]
        : [duplicate, completeBatch(1)]) {
        const result = reduceCapabilityState(profile, prior, {
          type: "tick",
          nowSeconds: 11,
          difficulty: "standard",
          defeatConditions: [],
          victoryConditions: ["return"],
          liveSpatialBatch: batch,
        });
        expect(result.terminal).toBe("defeat");
        expect(result.liveSpatialObservation).toEqual(
          prior.liveSpatialObservation,
        );
      }
    const beforeDeadline = reduceCapabilityState(profile, latched, {
      type: "tick",
      nowSeconds: 5,
      difficulty: "standard",
      defeatConditions: [],
      victoryConditions: ["return"],
      liveSpatialBatch: duplicate,
    });
    expect(beforeDeadline.terminal).toBeNull();
    expect(beforeDeadline.phaseElapsedSeconds).toBe(5);
    const dead = completeBatch(2);
    firstEntity(dead).alive = false;
    firstEntity(dead).zones = [];
    const movedAndDead = reduceCapabilityState(profile, latched, {
      type: "tick",
      nowSeconds: 5,
      difficulty: "standard",
      defeatConditions: [],
      victoryConditions: ["return"],
      liveSpatialBatch: dead,
    });
    expect(movedAndDead.terminal).toBeNull();
    expect(movedAndDead.entityStates["bundle-1"]).toBe("destroyed");
    expect(
      reduceCapabilityState(profile, movedAndDead, {
        type: "tick",
        nowSeconds: 11,
        difficulty: "standard",
        defeatConditions: [],
        victoryConditions: ["return"],
        liveSpatialBatch: duplicate,
      }).terminal,
    ).toBe("defeat");

    const withoutPresence = structuredClone(profile);
    const returnObjective = withoutPresence.objectivePlan[0];
    if (!returnObjective) throw new Error("Missing return objective");
    returnObjective.predicate.requirements =
      returnObjective.predicate.requirements.filter(
        (requirement) => requirement.kind !== "current-entity-presence",
      );
    returnObjective.predicate.requiredLedgers = ["first-receipt"];
    expect(validateScenarioCapability(withoutPresence)).toEqual([]);
    let oldState = createCapabilitySnapshot(withoutPresence, {
      spendable: {},
      protectedRecovery: {},
      optionalReserve: {},
    });
    oldState = reduceCapabilityState(withoutPresence, oldState, {
      type: "enter-phase",
      phase: "phase-1",
      nowSeconds: 0,
    });
    const oldExpired = reduceCapabilityState(withoutPresence, oldState, {
      type: "tick",
      nowSeconds: 11,
      difficulty: "standard",
      defeatConditions: [],
      victoryConditions: [],
      liveSpatialBatch: duplicate,
    });
    expect(oldExpired.terminal).toBe("defeat");
    expect(oldExpired.liveSpatialObservation).toBeUndefined();
  });

  test("invalid contracts reject duplicates, unknown zones, missing destinations and impossible thresholds", () => {
    const cases = [
      (p: typeof base) => {
        presenceRequirement(p).entities.push("bundle-1");
      },
      (p: typeof base) => {
        presenceRequirement(p).destinations["bundle-1"] = "unknown-zone";
      },
      (p: typeof base) => {
        delete presenceRequirement(p).destinations["bundle-1"];
      },
      (p: typeof base) => {
        presenceRequirement(p).requiredCount = 7;
      },
    ];
    for (const mutate of cases) {
      const candidate = structuredClone(base);
      mutate(candidate);
      expect(validateScenarioCapability(candidate).length).toBeGreaterThan(0);
      expect(() => compileCapabilityProfile(candidate)).toThrow();
    }
  });

  test("old profiles keep their snapshot shape, fingerprint and receipt behavior", () => {
    const old = structuredClone(base);
    const objective = old.objectivePlan[0];
    if (!objective) throw new Error("Test profile has no objective");
    objective.predicate.requirements.pop();
    objective.predicate.requiredLedgers.pop();
    expect(validateScenarioCapability(old)).toEqual([]);
    const oldState = createCapabilitySnapshot(old, {
      spendable: {},
      protectedRecovery: {},
      optionalReserve: {},
    });
    expect(oldState.liveSpatialObservation).toBeUndefined();
    const oldEntered = reduceCapabilityState(old, oldState, {
      type: "enter-phase",
      phase: "phase-1",
      nowSeconds: 0,
    });
    const oldDelivered = reduceCapabilityState(old, oldEntered, {
      type: "record-arrival",
      entityId: "bundle-1",
      zoneId: "store-1",
    });
    expect(
      reduceCapabilityState(old, oldDelivered, {
        type: "latch-objective",
        objectiveId: "return",
      }).objectiveLatches,
    ).toEqual(["return"]);
    expect(() =>
      reduceCapabilityState(base, oldDelivered, {
        type: "latch-objective",
        objectiveId: "return",
      }),
    ).toThrow("capability.snapshot-contract-mismatch");
    const initial = createCapabilitySnapshot(base, {
      spendable: {},
      protectedRecovery: {},
      optionalReserve: {},
    });
    expect(initial).toEqual(JSON.parse(JSON.stringify(initial)));
  });
});
