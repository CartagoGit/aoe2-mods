import { describe, expect, test } from "bun:test";
import { renderNativeCampaign } from "../../packages/aoe2-adapter/native-campaign.renderer";
import {
  createCapabilitySnapshot,
  reduceCapabilityState,
} from "../../packages/gameplay-validation/capability-state.reducer";
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
    expect(state.resolvedWaves).toEqual(["wave-a"]);
  });
});
