import { capabilityProfileV2Schema } from "../../packages/schemas/scenario-capability.schema";

export const actor = (id: string) => ({
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
export const zone = (id: string, x: number) => ({
  id,
  hub: "hub",
  offsetTiles: [x, 20] as [number, number],
  radiusTiles: 2,
  placement: "reference zone only",
  protectedCivilian: false,
});
export const originalIds = [
  "bundle-1",
  "bundle-2",
  "bundle-3",
  "custodian-1",
  "custodian-2",
  "custodian-3",
];
export const destinations = Object.fromEntries(
  originalIds.map((id, index) => [id, `store-${(index % 3) + 1}`]),
);

export function side(index: number) {
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

export function makeProfile() {
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
