import { describe, expect, test } from "bun:test";
import { renderNativeCampaign } from "../../packages/aoe2-adapter/native-campaign.renderer";
import { createCapabilitySnapshot } from "../../packages/gameplay-state/capability-snapshot.factory";
import { reduceCapabilityState } from "../../packages/gameplay-state/capability-state.reducer";
import { validateScenarioCapability } from "../../packages/gameplay-validation/scenario-capability.validator";
import type { StringLock } from "../../packages/localization/localization.catalog";
import { compileCapabilityProfile } from "../../packages/scenario-compiler/capability.compiler";
import type { Campaign } from "../../packages/schemas/campaign.schema";
import { capabilityProfileV2Schema } from "../../packages/schemas/scenario-capability.schema";

const entity = (id: string, initialHub = "hub-a") => ({
  id,
  role: "civilian",
  initialHub,
  offsetTiles: [0, 0] as [number, number],
  identity: id,
  finite: true as const,
  replacement: "none",
  initiallyDelivered: false as const,
  originRule: "preplaced outside destination",
});
const profile = capabilityProfileV2Schema.parse({
  profile: "composed-world-ledger",
  schemaVersion: 2,
  districts: ["hub-a"],
  worldContract: {
    version: 1,
    classification: "authoring specification, not implemented DSL",
    entities: [
      entity("unit-a"),
      entity("cargo-a"),
      entity("receiver-a"),
      entity("guard-a"),
    ],
    zones: [
      {
        id: "zone-dest",
        hub: "hub-a",
        offsetTiles: [20, 20],
        radiusTiles: 2,
        placement: "outside start",
        protectedCivilian: false,
      },
      {
        id: "zone-other",
        hub: "hub-a",
        offsetTiles: [40, 40],
        radiusTiles: 2,
        placement: "separate",
        protectedCivilian: false,
      },
    ],
    ledgerPolicy: "once per entity",
    resourcePolicy: "atomic accounts",
    defeatPolicy: "defeat first",
    earlyDelivery: "persistent positive facts",
    survivorGroups: [],
    enemyBinding: "finite roster",
  },
  objectivePlan: [
    {
      id: "objective-a",
      text: { en: "Arrive", "es-ES": "Llegar" },
      after: [],
      targetHub: "hub-a",
      phase: "phase-1",
      completion: "arrival and payment",
      countLedger: { id: "ledger-a", oncePerEntity: true, required: 1 },
      earlyCompletion: "latch once true",
      effect: "register",
      capability: "all required",
      operation: "arrivals",
      threshold: 1,
      entities: [entity("unit-a")],
      predicate: {
        operator: "all",
        operation: "complete",
        requiredCount: 1,
        defeatBelowRemaining: null,
        resourceAmounts: {},
        phaseGated: true,
        neverUseTimerInstead: true,
        requirements: [
          {
            id: "arrive",
            kind: "entity-state",
            state: "arrived",
            entities: ["unit-a"],
            requiredCount: 1,
            oncePerEntity: true,
            destinations: { "unit-a": "zone-dest" },
          },
          {
            id: "payment",
            kind: "resource-transaction",
            amounts: { food: 1, gold: 1 },
            receivingZones: ["zone-dest", "zone-other"],
            allocations: {
              "zone-dest": { food: 1 },
              "zone-other": { gold: 1 },
            },
            paidFlag: "receipt-a",
            account: "spendable",
            atomic: true,
            once: true,
            commit: "all at once",
          },
          {
            id: "deadline",
            kind: "phase-deadline",
            phase: "phase-1",
            clock: "relative-to-phase-entry",
            onExpiry: "defeat",
            secondsByDifficulty: { easy: 60, standard: 40, hard: 20 },
            warningSeconds: 10,
          },
        ],
        requiredLedgers: ["arrive", "payment", "deadline"],
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
        objectiveId: "objective-a",
      },
      {
        from: "phase-1",
        to: "defeat",
        on: "objective-latched",
        objectiveId: "objective-a",
      },
    ],
    terminalPriority:
      "defeat evaluated first; one terminal latch, choice order documented",
    saveLoad: "snapshot schema v2",
    phaseClock: "relative to explicit phase entry",
  },
  secondaryObjectives: Array.from({ length: 6 }, (_, index) => ({
    id: `side-${index + 1}`,
    kind: "scout",
    title: { en: "Scout", "es-ES": "Explorar" },
    subject: { en: "Route", "es-ES": "Ruta" },
    classification: "optional",
    rationale: { en: "Optional", "es-ES": "Opcional" },
    text: { en: "Visit", "es-ES": "Visitar" },
    mandatory: false,
    activation: "available during phase one",
    dependencies: [],
    predicate: {
      operator: "all",
      requirements: [
        {
          kind: "visit-zones",
          zones: [`side-${index + 1}-zone`],
          actor: "any-player-controlled-unit",
          requiredCount: 1,
          observationsPersistent: true,
          countInitialVisibility: false,
        },
      ],
      neverUseTimerInstead: true,
    },
    world: {
      entities: [],
      zones: [
        {
          id: `side-${index + 1}-zone`,
          hub: "hub-a",
          offsetTiles: [60 + index * 10, 60],
          radiusTiles: 2,
          placement: "optional route",
          protectedCivilian: false,
        },
      ],
    },
    effects: [
      {
        kind: "unlock-context-and-hint",
        target: "hint",
        resources: {},
        onceFlag: `reward-${index + 1}`,
        funding: "reserved-optional-stock",
        changesHistoricalOutcome: false,
        hint: { en: "A clue", "es-ES": "Una pista" },
      },
    ],
    completionFlag: `complete-${index + 1}`,
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
      persistentLedgers: ["visits", "receipts", "stock", "flags"],
      terminalPriority: "terminal closes uncompleted goals",
    },
    unavailablePolicy: "unavailable",
    terminalPolicy: "close",
    difficultyPolicy: "fixed",
    reachability: {
      originHub: "hub-a",
      receivingHub: "hub-a",
      corridorIds: [`corridor-${index + 1}`],
      maxRequiredRoundTrips: 0,
      spawnOutsideReceivingZone: true,
      placementGate: "validate placement",
    },
    qa: ["replay visit"],
  })),
  secondaryBudget: {
    reservedRewards: {},
    maxOptionalCosts: {},
    reallocatedCacheAllowance: {},
    fundingPolicy: "fixed reserve",
    nativeStatus:
      "design-only; requires certified reusable predicates and native QA",
  },
  enemyRoster: {
    initialEntityIds: ["guard-a"],
    productionEnabled: false,
    mobilizations: [
      { id: "wave-a", entityIds: ["guard-a"], releasedOnce: true },
    ],
    unspentPolicy: "remain-in-reserve",
  },
});

const initial = () =>
  createCapabilitySnapshot(profile, {
    spendable: { food: 1, gold: 0 },
    protectedRecovery: { food: 3 },
    optionalReserve: { food: 1 },
  });
const reduce = (
  state: ReturnType<typeof initial>,
  action: Parameters<typeof reduceCapabilityState>[2],
) => reduceCapabilityState(profile, state, action);

describe("phase and ledger reference model", () => {
  test("profile contracts satisfy the structural compiler gate", () => {
    expect(validateScenarioCapability(profile)).toEqual([]);
    expect(compileCapabilityProfile(profile)).toMatchObject({
      schemaVersion: 2,
      profile: "composed-world-ledger",
    });
  });

  test("native renderer rejects v2 before reading templates", async () => {
    const campaign = {
      id: "test-campaign",
      scenarios: [{ capabilityProfile: profile }],
    } as Campaign;
    await expect(
      renderNativeCampaign(
        "/missing",
        campaign,
        { ids: {} } as StringLock,
        "/unused",
      ),
    ).rejects.toThrow("capability-not-implemented");
  });

  test("paired delivery cannot satisfy its family threshold with unrelated receivers", () => {
    const candidate = structuredClone(profile);
    candidate.objectivePlan[0]?.predicate.requirements.push({
      id: "family-pair",
      kind: "paired-delivery",
      pairs: [
        { cargo: "cargo-a", receiver: "receiver-a" },
        { cargo: "unit-a", receiver: "guard-a" },
      ],
      receiverSet: "one documented family",
      destination: "zone-dest",
      requiredCount: 2,
      oncePerPair: true,
      cargoRecovery: "receipt-backed only",
    });
    candidate.objectivePlan[0]?.predicate.requiredLedgers.push("family-pair");
    const issues = validateScenarioCapability(candidate);
    expect(
      issues.some((item) => item.code === "capability.paired-survivors"),
    ).toBe(true);
  });

  test("arrival is persistent, unique, and cannot be reassigned after re-entry", () => {
    let state = reduce(initial(), {
      type: "enter-phase",
      phase: "phase-1",
      nowSeconds: 100,
    });
    state = reduce(state, {
      type: "record-arrival",
      entityId: "unit-a",
      zoneId: "zone-dest",
    });
    const once = state;
    state = reduce(state, {
      type: "record-arrival",
      entityId: "unit-a",
      zoneId: "zone-dest",
    });
    expect(state.arrivedEntities).toEqual(once.arrivedEntities);
    expect(
      reduce(state, {
        type: "record-arrival",
        entityId: "unit-a",
        zoneId: "zone-other",
      }).arrivedEntities["unit-a"],
    ).toBe("zone-dest");
    state = reduce(state, { type: "destroy-entity", entityId: "unit-a" });
    expect(state.requirementFacts["objective-a.arrive"]).toContain("unit-a");
  });

  test("multi-resource payment is atomic and receipt prevents a second debit", () => {
    let state = initial();
    state = { ...state, spendable: { ...state.spendable, gold: 0 } };
    const insufficient = reduce(state, {
      type: "pay-main",
      objectiveId: "objective-a",
      requirementId: "payment",
    });
    expect(insufficient.spendable).toEqual(state.spendable);
    state = { ...state, spendable: { ...state.spendable, gold: 1 } };
    const paid = reduce(state, {
      type: "pay-main",
      objectiveId: "objective-a",
      requirementId: "payment",
    });
    expect(paid.spendable).toMatchObject({ food: 0, gold: 0 });
    expect(
      reduce(paid, {
        type: "pay-main",
        objectiveId: "objective-a",
        requirementId: "payment",
      }).spendable,
    ).toEqual(paid.spendable);
  });

  test("relative phase deadline resets on entry and defeat wins a same-tick race", () => {
    let state = reduce(initial(), {
      type: "enter-phase",
      phase: "phase-1",
      nowSeconds: 100,
    });
    state = reduce(state, {
      type: "tick",
      nowSeconds: 130,
      difficulty: "standard",
      defeatConditions: [],
      victoryConditions: [],
    });
    expect(state.deadlineWarnings).toContain("objective-a.deadline");
    state = reduce(state, {
      type: "record-arrival",
      entityId: "unit-a",
      zoneId: "zone-dest",
    });
    state = reduce(state, {
      type: "pay-main",
      objectiveId: "objective-a",
      requirementId: "payment",
    });
    state = reduce(state, {
      type: "record-predicate",
      objectiveId: "objective-a",
      requirementId: "deadline",
    });
    state = reduce(state, {
      type: "latch-objective",
      objectiveId: "objective-a",
    });
    state = reduce(state, {
      type: "tick",
      nowSeconds: 140,
      difficulty: "standard",
      defeatConditions: ["loss"],
      victoryConditions: ["objective-a"],
    });
    expect(state.terminal).toBe("defeat");
    expect(state.secondaryStates["side-1"]).toBe("closed-at-terminal");
  });

  test("snapshot parsing and repeated optional visit remain idempotent; optional goals do not gate main objective", () => {
    const state = reduce(initial(), {
      type: "visit-zone",
      zoneId: "side-1-zone",
    });
    const repeated = reduce(state, {
      type: "visit-zone",
      zoneId: "side-1-zone",
    });
    expect(repeated.visitedZones).toEqual(["side-1-zone"]);
    expect(JSON.parse(JSON.stringify(repeated))).toEqual(repeated);
    expect(repeated.objectiveLatches).toEqual([]);
    expect(repeated.secondaryStates["side-1"]).toBe("available");
    const completed = reduce(repeated, {
      type: "award-secondary",
      objectiveId: "side-1",
    });
    expect(completed.secondaryStates["side-1"]).toBe("completed");
    expect(
      reduce(completed, { type: "award-secondary", objectiveId: "side-1" }),
    ).toEqual(completed);
  });

  test("finite reserve mobilizes only once and only released units count as resolved", () => {
    let state = initial();
    state = reduce(state, { type: "record-wave-resolved", waveId: "wave-a" });
    expect(state.resolvedWaves).toEqual([]);
    state = reduce(state, { type: "release-wave", waveId: "wave-a" });
    const released = state;
    state = reduce(state, { type: "release-wave", waveId: "wave-a" });
    expect(state.releasedRosterIds).toEqual(["guard-a"]);
    expect(state).toEqual(released);
    state = reduce(state, { type: "record-wave-resolved", waveId: "wave-a" });
    expect(state.resolvedWaves).toEqual([]);
    state = reduce(state, { type: "destroy-entity", entityId: "guard-a" });
    state = reduce(state, { type: "record-wave-resolved", waveId: "wave-a" });
    expect(state.resolvedWaves).toEqual(["wave-a"]);
  });
});

type Requirement =
  (typeof profile.objectivePlan)[number]["predicate"]["requirements"][number];
function referenceFixture(
  requirements: Requirement[],
  configure: (candidate: typeof profile) => void = () => {},
) {
  const candidate = structuredClone(profile);
  const objective = candidate.objectivePlan[0];
  if (!objective) throw new Error("Missing reference objective");
  objective.predicate.requirements = requirements;
  objective.predicate.requiredLedgers = requirements.map((req) => req.id);
  configure(candidate);
  const initial = createCapabilitySnapshot(candidate, {
    spendable: { food: 1, gold: 1 },
    protectedRecovery: {},
    optionalReserve: {},
  });
  const step = (
    state: typeof initial,
    action: Parameters<typeof reduceCapabilityState>[2],
  ) => reduceCapabilityState(candidate, state, action);
  return {
    candidate,
    step,
    entered: step(initial, {
      type: "enter-phase",
      phase: "phase-1",
      nowSeconds: 100,
    }),
  };
}
const arrivalRequirement = (
  id: string,
  entityId: string,
  zoneId: string,
): Requirement => ({
  id,
  kind: "entity-state",
  state: "arrived",
  entities: [entityId],
  requiredCount: 1,
  oncePerEntity: true,
  destinations: { [entityId]: zoneId },
});
const latch = { type: "latch-objective", objectiveId: "objective-a" } as const;

describe("independent-review regressions", () => {
  test("one family can receive supplies and subsequently reach a second destination", () => {
    const f = referenceFixture([
      arrivalRequirement("receive", "unit-a", "zone-dest"),
      arrivalRequirement("withdraw", "unit-a", "zone-other"),
    ]);
    let state = f.step(f.entered, {
      type: "record-arrival",
      entityId: "unit-a",
      zoneId: "zone-dest",
    });
    expect(f.step(state, latch).objectiveLatches).toEqual([]);
    state = f.step(state, {
      type: "record-arrival",
      entityId: "unit-a",
      zoneId: "zone-other",
    });
    expect(state.arrivalLedger).toHaveLength(2);
    expect(
      f.step(state, {
        type: "record-arrival",
        entityId: "unit-a",
        zoneId: "zone-other",
      }),
    ).toEqual(state);
    expect(
      f.step(JSON.parse(JSON.stringify(state)), latch).objectiveLatches,
    ).toEqual(["objective-a"]);
  });

  test("death cannot be overridden by an alive observation or generic predicate", () => {
    const f = referenceFixture([
      {
        id: "alive",
        kind: "entity-state",
        state: "alive",
        entities: ["unit-a"],
        requiredCount: 1,
        oncePerEntity: true,
      },
    ]);
    const dead = f.step(f.entered, {
      type: "destroy-entity",
      entityId: "unit-a",
    });
    const asserted = f.step(dead, {
      type: "record-predicate",
      objectiveId: "objective-a",
      requirementId: "alive",
    });
    expect(f.step(asserted, latch).objectiveLatches).toEqual([]);
  });

  test("two collected identities and a causal derived petition are required", () => {
    const f = referenceFixture([
      {
        id: "collect",
        kind: "entity-state",
        state: "collected",
        entities: ["unit-a", "cargo-a"],
        requiredCount: 2,
        oncePerEntity: true,
      },
      {
        id: "derive",
        kind: "derived-token",
        inputEntities: ["unit-a", "cargo-a"],
        outputEntities: ["receiver-a"],
        once: true,
        deriveWhen: "both records collected",
      },
      arrivalRequirement("deliver", "receiver-a", "zone-dest"),
    ]);
    let state = f.step(f.entered, {
      type: "record-arrival",
      entityId: "receiver-a",
      zoneId: "zone-dest",
    });
    expect(state.arrivalLedger).toEqual([]);
    state = f.step(state, {
      type: "observe-entity-state",
      objectiveId: "objective-a",
      requirementId: "collect",
      entityId: "unit-a",
    });
    expect(
      f.step(state, {
        type: "derive-token",
        objectiveId: "objective-a",
        requirementId: "derive",
      }),
    ).toEqual(state);
    state = f.step(state, {
      type: "observe-entity-state",
      objectiveId: "objective-a",
      requirementId: "collect",
      entityId: "cargo-a",
    });
    expect(state.requirementFacts["objective-a.collect"]).toEqual([
      "cargo-a",
      "unit-a",
    ]);
    state = f.step(state, {
      type: "derive-token",
      objectiveId: "objective-a",
      requirementId: "derive",
    });
    state = f.step(state, {
      type: "record-arrival",
      entityId: "receiver-a",
      zoneId: "zone-dest",
    });
    expect(f.step(state, latch).objectiveLatches).toEqual(["objective-a"]);
  });

  test("a zone visit cannot substitute for control, passability and eliminated blockers", () => {
    const f = referenceFixture([
      {
        id: "control",
        kind: "area-state",
        state: "controlled-and-passable",
        zones: ["zone-dest"],
        blockingEnemies: ["guard-a"],
        requiredCount: 1,
      },
    ]);
    let state = f.step(f.entered, { type: "visit-zone", zoneId: "zone-dest" });
    state = f.step(state, {
      type: "observe-zone",
      zoneId: "zone-dest",
      controlled: true,
      passable: true,
      protected: false,
    });
    expect(f.step(state, latch).objectiveLatches).toEqual([]);
    state = f.step(state, { type: "destroy-entity", entityId: "guard-a" });
    expect(f.step(state, latch).objectiveLatches).toEqual(["objective-a"]);
  });

  test("relative deadlines admit completion before expiry and reject time reversal", () => {
    const req = profile.objectivePlan[0]?.predicate.requirements.find(
      (req) => req.kind === "phase-deadline",
    );
    if (!req) throw new Error("Missing deadline");
    const f = referenceFixture([req]);
    const state = f.step(f.entered, {
      type: "tick",
      nowSeconds: 110,
      difficulty: "standard",
      defeatConditions: [],
      victoryConditions: [],
    });
    expect(state.phaseElapsedSeconds).toBe(10);
    expect(
      f.step(state, {
        type: "tick",
        nowSeconds: 105,
        difficulty: "standard",
        defeatConditions: [],
        victoryConditions: [],
      }),
    ).toEqual(state);
    const complete = f.step(state, latch);
    expect(complete.objectiveLatches).toEqual(["objective-a"]);
    const won = f.step(complete, {
      type: "enter-phase",
      phase: "victory",
      nowSeconds: 110,
    });
    expect(won.terminal).toBe("victory");
    expect(won.secondaryStates["side-1"]).toBe("closed-at-terminal");
    expect(
      f.step(won, { type: "award-secondary", objectiveId: "side-1" }),
    ).toEqual(won);
    expect(
      f.step(f.entered, {
        type: "tick",
        nowSeconds: 140,
        difficulty: "standard",
        defeatConditions: [],
        victoryConditions: [],
      }).terminal,
    ).toBe("defeat");
  });

  test("same-objective departure uses an explicit delivery receipt and cannot wait for itself", () => {
    const f = referenceFixture([
      arrivalRequirement("copies", "unit-a", "zone-dest"),
      {
        id: "leave",
        kind: "ordered-departure",
        departingEntities: ["receiver-a"],
        departureEnabledOnlyAfterReceipt: true,
        receiptObjective: "objective-a",
        receiptRequirement: "copies",
      },
    ]);
    expect(validateScenarioCapability(f.candidate)).toEqual([]);
    let state = f.step(f.entered, {
      type: "record-departure",
      objectiveId: "objective-a",
      requirementId: "leave",
      entityId: "receiver-a",
    });
    expect(state.departedEntities).toEqual([]);
    state = f.step(state, {
      type: "record-arrival",
      entityId: "unit-a",
      zoneId: "zone-dest",
    });
    state = f.step(state, {
      type: "record-departure",
      objectiveId: "objective-a",
      requirementId: "leave",
      entityId: "receiver-a",
    });
    expect(f.step(state, latch).objectiveLatches).toEqual(["objective-a"]);
    const cyclic = structuredClone(f.candidate);
    const leave = cyclic.objectivePlan[0]?.predicate.requirements.find(
      (req) => req.kind === "ordered-departure",
    );
    if (leave?.kind === "ordered-departure") delete leave.receiptRequirement;
    expect(
      validateScenarioCapability(cyclic).some(
        (issue) => issue.code === "capability.departure-cycle",
      ),
    ).toBe(true);
  });

  test("finite initial rosters reject duplicate identities", () => {
    const duplicate = structuredClone(profile);
    duplicate.enemyRoster.initialEntityIds.push("guard-a");
    expect(
      validateScenarioCapability(duplicate).some(
        (issue) => issue.code === "capability.enemy-roster",
      ),
    ).toBe(true);
  });

  test("water and rations must intersect on the same receivers, rather than equal counts", () => {
    const paired = (id: string, prefix: string): Requirement => ({
      id,
      kind: "paired-delivery",
      pairs: [1, 2, 3].map((index) => ({
        cargo: `${prefix}-${index}`,
        receiver: `family-${index}`,
      })),
      receiverSet: "same families",
      destination: "zone-dest",
      requiredCount: 2,
      oncePerPair: true,
      cargoRecovery: "none",
    });
    const f = referenceFixture(
      [paired("water", "water"), paired("rations", "ration")],
      (candidate) => {
        candidate.worldContract.entities.push(
          ...[1, 2, 3].flatMap((index) => [
            entity(`family-${index}`),
            entity(`water-${index}`),
            entity(`ration-${index}`),
          ]),
        );
        candidate.worldContract.survivorGroups.push({
          entities: ["family-1", "family-2", "family-3"],
          minimumAliveOrAlreadySafe: 2,
          loss: "defeat",
        });
        const objective = candidate.objectivePlan[0];
        if (objective)
          objective.predicate.exportedLedgers = [
            {
              id: "served-families",
              operator: "intersection",
              fromRequirements: ["water", "rations"],
              minimumCount: 2,
            },
          ];
      },
    );
    expect(validateScenarioCapability(f.candidate)).toEqual([]);
    let state = f.entered;
    for (const id of [
      "family-1",
      "family-2",
      "family-3",
      "water-1",
      "water-2",
      "ration-2",
      "ration-3",
    ])
      state = f.step(state, {
        type: "record-arrival",
        entityId: id,
        zoneId: "zone-dest",
      });
    for (const [requirementId, cargoId, receiverId] of [
      ["water", "water-1", "family-1"],
      ["water", "water-2", "family-2"],
      ["rations", "ration-2", "family-2"],
      ["rations", "ration-3", "family-3"],
    ])
      state = f.step(state, {
        type: "record-pair",
        objectiveId: "objective-a",
        requirementId: requirementId ?? "",
        cargoId: cargoId ?? "",
        receiverId: receiverId ?? "",
      });
    expect(state.exportedLedgers["objective-a.served-families"]).toEqual([
      "family-2",
    ]);
    expect(f.step(state, latch).objectiveLatches).toEqual([]);
    state = f.step(state, {
      type: "record-arrival",
      entityId: "ration-1",
      zoneId: "zone-dest",
    });
    state = f.step(state, {
      type: "record-pair",
      objectiveId: "objective-a",
      requirementId: "rations",
      cargoId: "ration-1",
      receiverId: "family-1",
    });
    expect(state.exportedLedgers["objective-a.served-families"]).toEqual([
      "family-1",
      "family-2",
    ]);
    expect(
      f.step(JSON.parse(JSON.stringify(state)), latch).objectiveLatches,
    ).toEqual(["objective-a"]);
  });

  test("an arrival-generated receipt cannot return before its originating wagon delivers", () => {
    const issued = arrivalRequirement(
      "returned-copy",
      "receiver-a",
      "zone-other",
    );
    if (issued.kind !== "entity-state")
      throw new Error("Missing entity requirement");
    issued.generatedByReceipts = [
      {
        fromObjective: "objective-a",
        fromRequirement: "wagon",
        receivedEntity: "unit-a",
        destination: "zone-dest",
        output: "receiver-a",
      },
    ];
    const f = referenceFixture([
      arrivalRequirement("wagon", "unit-a", "zone-dest"),
      issued,
    ]);
    let state = f.step(f.entered, {
      type: "record-arrival",
      entityId: "receiver-a",
      zoneId: "zone-other",
    });
    expect(state.arrivalLedger).toEqual([]);
    state = f.step(state, {
      type: "record-arrival",
      entityId: "unit-a",
      zoneId: "zone-dest",
    });
    state = f.step(state, {
      type: "record-arrival",
      entityId: "receiver-a",
      zoneId: "zone-other",
    });
    expect(f.step(state, latch).objectiveLatches).toEqual(["objective-a"]);
  });

  test("a snapshot from another objective contract cannot be loaded silently", () => {
    const f = referenceFixture([
      arrivalRequirement("one", "unit-a", "zone-dest"),
    ]);
    const other = referenceFixture([
      arrivalRequirement("another", "unit-a", "zone-other"),
    ]);
    expect(() => other.step(f.entered, latch)).toThrow(
      "capability.snapshot-contract-mismatch",
    );
  });

  test("control that must remain until a later objective is continuously enforced", () => {
    const f = referenceFixture(
      [
        {
          id: "control",
          kind: "area-state",
          state: "controlled-and-passable",
          zones: ["zone-dest"],
          requiredCount: 1,
          mustRemainUntilObjective: "objective-b",
        },
      ],
      (candidate) => {
        const source = candidate.objectivePlan[0];
        if (!source) throw new Error("Missing objective");
        candidate.objectivePlan.push({
          ...structuredClone(source),
          id: "objective-b",
          after: ["objective-a"],
          predicate: {
            ...source.predicate,
            requirements: [
              arrivalRequirement("return", "unit-a", "zone-other"),
            ],
            requiredLedgers: ["return"],
          },
        });
      },
    );
    let state = f.step(f.entered, {
      type: "observe-zone",
      zoneId: "zone-dest",
      controlled: true,
      passable: true,
      protected: false,
    });
    state = f.step(state, latch);
    expect(state.objectiveLatches).toEqual(["objective-a"]);
    state = f.step(state, {
      type: "observe-zone",
      zoneId: "zone-dest",
      controlled: false,
      passable: true,
      protected: false,
    });
    expect(state.terminal).toBe("defeat");
    expect(state.secondaryStates["side-1"]).toBe("closed-at-terminal");
  });
});
