import { z } from "zod";

const contractId = z.string().regex(/^[a-z0-9][a-z0-9.-]*$/);
const nonEmpty = z.string().trim().min(1);
const resources = ["food", "wood", "gold", "stone"] as const;
const resourceAmounts = z.strictObject({
  food: z.number().int().nonnegative().optional(),
  wood: z.number().int().nonnegative().optional(),
  gold: z.number().int().nonnegative().optional(),
  stone: z.number().int().nonnegative().optional(),
});
const resourceAllocations = z.record(contractId, resourceAmounts);
const offset = z.tuple([z.number().finite(), z.number().finite()]);

export const worldEntitySchema = z.strictObject({
  id: contractId,
  role: nonEmpty,
  initialHub: contractId,
  offsetTiles: offset,
  identity: nonEmpty,
  finite: z.literal(true),
  replacement: nonEmpty,
  initiallyDelivered: z.literal(false),
  originRule: nonEmpty,
  rosterSource: nonEmpty.optional(),
  rosterMemberId: contractId.optional(),
  countedOnce: z.boolean().optional(),
  atHub: contractId.optional(),
  initialHealthFraction: z.number().min(0).max(1).optional(),
  damageSource: nonEmpty.optional(),
  playerControllable: z.boolean().optional(),
  historicalPerson: z.boolean().optional(),
});
export const worldZoneSchema = z.strictObject({
  id: contractId,
  hub: contractId,
  offsetTiles: offset,
  radiusTiles: z.number().positive(),
  placement: nonEmpty,
  protectedCivilian: z.boolean(),
});
export const survivorGroupSchema = z.strictObject({
  entities: z.array(contractId).min(1),
  minimumAliveOrAlreadySafe: z.number().int().positive(),
  loss: nonEmpty,
});
export const worldContractSchema = z.strictObject({
  version: z.literal(1),
  classification: z.literal("authoring specification, not implemented DSL"),
  entities: z.array(worldEntitySchema),
  zones: z.array(worldZoneSchema),
  ledgerPolicy: nonEmpty,
  resourcePolicy: nonEmpty,
  defeatPolicy: nonEmpty,
  earlyDelivery: nonEmpty,
  survivorGroups: z.array(survivorGroupSchema),
  enemyBinding: nonEmpty,
});

const entityStatePredicate = z.strictObject({
  id: contractId,
  kind: z.literal("entity-state"),
  state: z.enum([
    "arrived",
    "alive",
    "alive-and-held",
    "collected",
    "destroyed",
    "prepared",
    "registered-after-arrival",
    "repaired-to-full-health",
    "sealed-and-delivered",
  ]),
  entities: z.array(contractId).min(1),
  requiredCount: z.number().int().positive(),
  oncePerEntity: z.literal(true),
  destinations: z.record(contractId, contractId).optional(),
  arrivalRule: nonEmpty.optional(),
  arrivalAfterDeparture: z
    .strictObject({
      objective: contractId,
      requirement: contractId,
    })
    .optional(),
  distinctDestinationCount: z.number().int().positive().optional(),
  minimumPerDestination: z.number().int().positive().optional(),
  eligibilityRule: nonEmpty.optional(),
  eligibleEntitiesFromLedger: z
    .strictObject({
      objective: contractId,
      ledger: contractId,
    })
    .optional(),
  generatedByReceipts: z
    .array(
      z.strictObject({
        fromObjective: contractId,
        fromRequirement: contractId,
        receivedEntity: contractId,
        destination: contractId,
        output: contractId,
      }),
    )
    .optional(),
  inputRecords: z.array(contractId).optional(),
  carriedRecords: z.array(contractId).optional(),
  transportModes: z.array(nonEmpty).optional(),
  originRule: nonEmpty.optional(),
  seaProof: nonEmpty.optional(),
});
const areaStatePredicate = z.strictObject({
  id: contractId,
  kind: z.literal("area-state"),
  state: z.enum(["controlled-and-passable", "visited-and-passable"]),
  zones: z.array(contractId).min(1),
  blockingEnemies: z.array(contractId).optional(),
  requiredCount: z.number().int().positive(),
  proof: nonEmpty.optional(),
  mustRemainUntilObjective: contractId.optional(),
});
const resourceTransactionPredicate = z.strictObject({
  id: contractId,
  kind: z.literal("resource-transaction"),
  amounts: resourceAmounts,
  receivingZones: z.array(contractId).min(1),
  allocations: resourceAllocations,
  paidFlag: contractId,
  account: z.enum(["spendable", "protected-recovery"]),
  atomic: z.literal(true),
  once: z.literal(true),
  commit: nonEmpty,
});
const minimumStockPredicate = z.strictObject({
  id: contractId,
  kind: z.literal("minimum-stock"),
  account: z.enum(["spendable", "protected-recovery"]),
  amounts: resourceAmounts,
  atHub: contractId.optional(),
  accountEntityIds: z.array(contractId).optional(),
  evaluate: nonEmpty,
  maximumNavigableDistanceTiles: z.number().positive().optional(),
});
const civilianProtectionPredicate = z.strictObject({
  id: contractId,
  kind: z.literal("civilian-protection"),
  zones: z.array(contractId).min(1),
  rule: nonEmpty,
  implementation: nonEmpty,
  activeFrom: contractId,
  activeUntil: contractId,
});
const pairedDeliveryPredicate = z.strictObject({
  id: contractId,
  kind: z.literal("paired-delivery"),
  pairs: z
    .array(z.strictObject({ cargo: contractId, receiver: contractId }))
    .min(1),
  receiverSet: nonEmpty,
  destination: contractId,
  requiredCount: z.number().int().positive(),
  oncePerPair: z.literal(true),
  cargoRecovery: nonEmpty,
});
const routeChoicePredicate = z.strictObject({
  id: contractId,
  kind: z.literal("route-choice"),
  allowedRoutes: z
    .array(
      z.strictObject({
        id: contractId,
        progressKey: z.string().min(1),
        value: z.number().int(),
        resetOtherKeys: z.literal(false),
      }),
    )
    .min(1),
  requiredCount: z.literal(1),
  selection: nonEmpty,
  preserveOtherKeys: z.literal(true),
});
const finiteWavePredicate = z.strictObject({
  id: contractId,
  kind: z.literal("finite-wave-resolution"),
  waves: z.array(contractId).min(1),
  state: nonEmpty,
  requiredCount: z.number().int().positive(),
  terminalSkip: z.boolean(),
});
const holdAreaPredicate = z.strictObject({
  id: contractId,
  kind: z.literal("hold-area"),
  zones: z.array(contractId).min(1),
  continuousSeconds: z.number().int().positive(),
  resetOnContest: z.literal(true),
  requires: nonEmpty,
});
const receiptExistsPredicate = z.strictObject({
  id: contractId,
  kind: z.literal("receipt-exists"),
  flag: contractId,
  fromObjective: contractId,
  amounts: resourceAmounts,
  newDebit: z.literal(false),
});
const derivedTokenPredicate = z.strictObject({
  id: contractId,
  kind: z.literal("derived-token"),
  inputEntities: z.array(contractId).min(1),
  outputEntities: z.array(contractId).min(1),
  once: z.literal(true),
  deriveWhen: nonEmpty,
  requiredPaymentReceipts: z
    .array(receiptExistsPredicate.omit({ id: true, kind: true }))
    .min(1)
    .optional(),
});
const orderedDeparturePredicate = z.strictObject({
  id: contractId,
  kind: z.literal("ordered-departure"),
  departingEntities: z.array(contractId).min(1),
  departureEnabledOnlyAfterReceipt: z.literal(true),
  receiptObjective: contractId,
  receiptRequirement: contractId.optional(),
});
const forbiddenEntryPredicate = z.strictObject({
  id: contractId,
  kind: z.literal("forbidden-entry"),
  entities: z.array(contractId),
  zones: z.array(contractId).min(1),
  activeFrom: contractId,
  onEntry: nonEmpty,
  actorSelector: z.literal("all-player-controlled-units"),
  rule: nonEmpty,
});
const phaseDeadlinePredicate = z.strictObject({
  id: contractId,
  kind: z.literal("phase-deadline"),
  phase: contractId,
  clock: z.literal("relative-to-phase-entry"),
  onExpiry: nonEmpty,
  secondsByDifficulty: z.strictObject({
    easy: z.number().int().positive(),
    standard: z.number().int().positive(),
    hard: z.number().int().positive(),
  }),
  warningSeconds: z.number().int().positive(),
});
const liveEntityPresencePredicate = z.strictObject({
  id: contractId,
  kind: z.literal("current-entity-presence"),
  entities: z.array(contractId).min(1),
  destinations: z.record(contractId, contractId),
  requiredCount: z.number().int().positive(),
});
const checkpointEntityPresencePredicate = z.strictObject({
  id: contractId,
  kind: z.literal("checkpoint-entity-presence"),
  entities: z.array(contractId).min(1),
  destinations: z.record(contractId, contractId),
  requiredCount: z.number().int().positive(),
});
export const worldPredicateSchema = z.discriminatedUnion("kind", [
  entityStatePredicate,
  areaStatePredicate,
  resourceTransactionPredicate,
  minimumStockPredicate,
  civilianProtectionPredicate,
  pairedDeliveryPredicate,
  routeChoicePredicate,
  finiteWavePredicate,
  holdAreaPredicate,
  receiptExistsPredicate,
  derivedTokenPredicate,
  orderedDeparturePredicate,
  forbiddenEntryPredicate,
  phaseDeadlinePredicate,
  liveEntityPresencePredicate,
  checkpointEntityPresencePredicate,
]);
const composedPredicateSchema = z.strictObject({
  operator: z.literal("all"),
  operation: contractId,
  requiredCount: z.number().int().positive(),
  destination: contractId.optional(),
  defeatBelowRemaining: z.number().int().nonnegative().nullable(),
  resourceAmounts: resourceAmounts,
  phaseGated: z.boolean(),
  neverUseTimerInstead: z.literal(true),
  foodPerHouse: z.number().int().positive().optional(),
  requirements: z.array(worldPredicateSchema).min(1),
  requiredLedgers: z.array(contractId).min(1),
  allRequired: z.literal(true),
  exportedLedgers: z
    .array(
      z.strictObject({
        id: contractId,
        operator: z.literal("intersection"),
        fromRequirements: z.array(contractId).min(1),
        minimumCount: z.number().int().positive(),
      }),
    )
    .optional(),
});
const objectiveEntitySchema = worldEntitySchema.extend({
  countedOnce: z.literal(true).optional(),
  atHub: contractId.optional(),
});
export const mainObjectiveSchema = z.strictObject({
  id: contractId,
  text: z.record(z.enum(["en", "es-ES"]), nonEmpty),
  after: z.array(contractId),
  targetHub: contractId,
  phase: contractId,
  completion: nonEmpty,
  countLedger: z.strictObject({
    id: contractId,
    oncePerEntity: z.literal(true),
    required: z.number().int().positive(),
  }),
  earlyCompletion: nonEmpty,
  effect: nonEmpty,
  capability: nonEmpty,
  operation: contractId,
  threshold: z.number().int().positive(),
  entities: z.array(objectiveEntitySchema),
  predicate: composedPredicateSchema,
});

const secondaryRequirementSchema = z.discriminatedUnion("kind", [
  z.strictObject({
    kind: z.literal("entity-arrival"),
    entities: z.array(contractId).min(1),
    destinations: z.record(contractId, contractId),
    requiredCount: z.number().int().positive(),
    aliveAtDelivery: z.literal(true),
    oncePerEntity: z.literal(true),
    noSubstitutes: z.literal(true),
    initialPlacementDoesNotCount: z.literal(true),
  }),
  z.strictObject({
    kind: z.literal("atomic-payment"),
    resources: resourceAmounts,
    receipt: contractId,
    afterArrival: z.boolean(),
    once: z.literal(true),
    protectedRecoveryCannotBeSpent: z.literal(true),
  }),
  z.strictObject({
    kind: z.literal("visit-zones"),
    zones: z.array(contractId).min(1),
    actor: z.literal("any-player-controlled-unit"),
    requiredCount: z.number().int().positive(),
    observationsPersistent: z.literal(true),
    countInitialVisibility: z.literal(false),
  }),
  z.strictObject({
    kind: z.literal("entity-health"),
    entity: contractId,
    health: z.literal("full"),
    paymentReceipt: contractId,
    restoration: nonEmpty,
  }),
]);
const secondaryEffectSchema = z.strictObject({
  kind: z.enum([
    "reveal-enemy-approach",
    "finite-supply-withdrawal",
    "unlock-context-and-hint",
    "mark-alternative-route",
  ]),
  target: nonEmpty,
  resources: resourceAmounts,
  onceFlag: contractId,
  funding: z.literal("reserved-optional-stock"),
  changesHistoricalOutcome: z.literal(false),
  sourceIds: z.array(contractId).optional(),
  historicalNote: z.record(z.enum(["en", "es-ES"]), nonEmpty).optional(),
  hint: z.record(z.enum(["en", "es-ES"]), nonEmpty).optional(),
  rosterIds: z.array(contractId).optional(),
  alreadyReleasedPolicy: nonEmpty.optional(),
  corridorId: contractId.optional(),
});
export const secondaryObjectiveSchema = z.strictObject({
  id: contractId,
  kind: z.enum([
    "scout",
    "aid",
    "copy",
    "repair",
    "trade",
    "guide",
    "extract",
    "watch",
  ]),
  title: z.record(z.enum(["en", "es-ES"]), nonEmpty),
  subject: z.record(z.enum(["en", "es-ES"]), nonEmpty),
  classification: nonEmpty,
  rationale: z.record(z.enum(["en", "es-ES"]), nonEmpty),
  text: z.record(z.enum(["en", "es-ES"]), nonEmpty),
  mandatory: z.literal(false),
  activation: nonEmpty,
  dependencies: z.array(contractId),
  predicate: z.strictObject({
    operator: z.literal("all"),
    requirements: z.array(secondaryRequirementSchema).min(1),
    neverUseTimerInstead: z.literal(true),
  }),
  world: z.strictObject({
    entities: z.array(worldEntitySchema),
    zones: z.array(worldZoneSchema),
  }),
  effects: z.array(secondaryEffectSchema).min(1),
  completionFlag: contractId,
  stateContract: z.strictObject({
    states: z.tuple([
      z.literal("available"),
      z.literal("completed"),
      z.literal("failed-optional"),
      z.literal("closed-at-terminal"),
    ]),
    requiresNonterminalScenario: z.literal(true),
    persistentAcrossSave: z.literal(true),
    completionAndEffectsAtomic: z.literal(true),
    paymentBeforeReward: z.literal(true),
    paymentIsNotCompletion: z.literal(true),
    failedGoalCannotReward: z.literal(true),
    latchAtFirstCompletion: z.literal(true),
    noMainVictoryDependency: z.literal(true),
    rewardTransaction: z.tuple([
      z.literal("verify all predicate ledgers and nonterminal state"),
      z.literal("verify reserved stock"),
      z.literal("debit reserved stock"),
      z.literal("credit spendable stock"),
      z.literal("set reward onceFlag"),
      z.literal("set completionFlag"),
    ]),
    transactionIsolation: nonEmpty,
    persistentLedgers: z.array(nonEmpty).min(1),
    terminalPriority: nonEmpty,
  }),
  unavailablePolicy: nonEmpty,
  terminalPolicy: nonEmpty,
  difficultyPolicy: nonEmpty,
  reachability: z.strictObject({
    originHub: contractId,
    receivingHub: contractId,
    corridorIds: z.array(contractId).min(1),
    maxRequiredRoundTrips: z.number().int().nonnegative(),
    spawnOutsideReceivingZone: z.literal(true),
    placementGate: nonEmpty,
  }),
  qa: z.array(nonEmpty).min(1),
});

export const capabilityProfileV2Schema = z.strictObject({
  profile: z.literal("composed-world-ledger"),
  schemaVersion: z.literal(2),
  districts: z.array(contractId).min(1),
  worldContract: worldContractSchema,
  objectivePlan: z.array(mainObjectiveSchema).min(1),
  stateMachine: z.strictObject({
    states: z.array(contractId).min(3),
    transitions: z.array(nonEmpty).min(1),
    phaseTransitions: z
      .array(
        z.strictObject({
          from: contractId,
          to: contractId,
          on: z.enum(["intro-accepted", "objective-latched"]),
          objectiveId: contractId.optional(),
        }),
      )
      .min(1),
    terminalPriority: z.literal(
      "defeat evaluated first; one terminal latch, choice order documented",
    ),
    saveLoad: nonEmpty,
    phaseClock: nonEmpty,
  }),
  secondaryObjectives: z.array(secondaryObjectiveSchema),
  secondaryBudget: z.strictObject({
    reservedRewards: resourceAmounts,
    maxOptionalCosts: resourceAmounts,
    reallocatedCacheAllowance: resourceAmounts,
    fundingPolicy: nonEmpty,
    nativeStatus: z.literal(
      "design-only; requires certified reusable predicates and native QA",
    ),
  }),
  enemyRoster: z.strictObject({
    initialEntityIds: z.array(contractId),
    productionEnabled: z.literal(false),
    mobilizations: z.array(
      z.strictObject({
        id: contractId,
        entityIds: z.array(contractId).min(1),
        releasedOnce: z.literal(true),
      }),
    ),
    unspentPolicy: z.literal("remain-in-reserve"),
  }),
});
export type CapabilityProfileV2 = z.infer<typeof capabilityProfileV2Schema>;
export type WorldPredicate = z.infer<typeof worldPredicateSchema>;
export type MainObjective = z.infer<typeof mainObjectiveSchema>;
export type SecondaryObjective = z.infer<typeof secondaryObjectiveSchema>;
export type ResourceAmounts = z.infer<typeof resourceAmounts>;
export const capabilityResources = resources;
