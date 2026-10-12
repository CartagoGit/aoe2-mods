import { z } from "zod";
import type {
  CapabilityProfileV2,
  ResourceAmounts,
} from "../schemas/scenario-capability.schema";

const stringList = z
  .array(z.string())
  .refine((items) => new Set(items).size === items.length);
const accountSchema = z.strictObject({
  food: z.number().int().nonnegative(),
  wood: z.number().int().nonnegative(),
  gold: z.number().int().nonnegative(),
  stone: z.number().int().nonnegative(),
});
export const capabilitySnapshotSchema = z.strictObject({
  schemaVersion: z.literal(2),
  profile: z.literal("composed-world-ledger"),
  phase: z.string().min(1),
  phaseEnteredAtSeconds: z.number().nonnegative().nullable(),
  terminal: z.enum(["victory", "defeat"]).nullable(),
  objectiveLatches: stringList,
  requirementFacts: z.record(z.string(), stringList),
  entityStates: z.record(z.string(), z.enum(["alive", "arrived", "destroyed"])),
  arrivedEntities: z.record(z.string(), z.string()),
  visitedZones: stringList,
  forbiddenEntries: stringList,
  paidReceipts: stringList,
  spendable: accountSchema,
  protectedRecovery: accountSchema,
  optionalReserve: accountSchema,
  secondaryStates: z.record(
    z.string(),
    z.enum(["available", "completed", "failed-optional", "closed-at-terminal"]),
  ),
  rewardFlags: stringList,
  recoveredEntities: stringList,
  releasedRosterIds: stringList,
  resolvedWaves: stringList,
  selectedRoutes: z.record(z.string(), z.string()),
  heldSeconds: z.record(z.string(), z.number().int().nonnegative()),
  deadlineWarnings: stringList,
  departedEntities: stringList,
});
export type CapabilitySnapshot = z.infer<typeof capabilitySnapshotSchema>;

export type CapabilityAction =
  | { type: "record-arrival"; entityId: string; zoneId: string }
  | { type: "destroy-entity"; entityId: string }
  | { type: "recover-entity"; entityId: string }
  | { type: "visit-zone"; zoneId: string }
  | { type: "record-predicate"; objectiveId: string; requirementId: string }
  | {
      type: "record-pair";
      objectiveId: string;
      requirementId: string;
      cargoId: string;
      receiverId: string;
    }
  | {
      type: "choose-route";
      objectiveId: string;
      requirementId: string;
      routeId: string;
    }
  | { type: "pay-main"; objectiveId: string; requirementId: string }
  | { type: "pay-secondary"; objectiveId: string; receipt: string }
  | {
      type: "record-secondary-predicate";
      objectiveId: string;
      requirementIndex: number;
    }
  | { type: "award-secondary"; objectiveId: string }
  | { type: "record-wave-resolved"; waveId: string }
  | { type: "release-wave"; waveId: string }
  | { type: "record-hold"; zoneId: string; elapsedSeconds: number }
  | { type: "record-forbidden-entry"; requirementId: string; actorId: string }
  | {
      type: "record-departure";
      objectiveId: string;
      requirementId: string;
      entityId: string;
    }
  | { type: "enter-phase"; phase: string; nowSeconds: number }
  | { type: "latch-objective"; objectiveId: string }
  | {
      type: "tick";
      nowSeconds: number;
      difficulty: "easy" | "standard" | "hard";
      defeatConditions: string[];
      victoryConditions: string[];
    };

const RESOURCES = ["food", "wood", "gold", "stone"] as const;
const EMPTY_RESOURCES = { food: 0, wood: 0, gold: 0, stone: 0 };
const sortUnique = (values: readonly string[]) => [...new Set(values)].sort();
const asRecord = (record: Record<string, string[]>) =>
  Object.fromEntries(
    Object.entries(record).sort(([a], [b]) => a.localeCompare(b)),
  );
const normalizeResources = (amounts: ResourceAmounts) => ({
  food: amounts.food ?? 0,
  wood: amounts.wood ?? 0,
  gold: amounts.gold ?? 0,
  stone: amounts.stone ?? 0,
});
const enough = (
  balance: Record<(typeof RESOURCES)[number], number>,
  cost: ResourceAmounts,
) => RESOURCES.every((resource) => balance[resource] >= (cost[resource] ?? 0));
const debit = (
  balance: Record<(typeof RESOURCES)[number], number>,
  cost: ResourceAmounts,
) => {
  const normalized = normalizeResources(cost);
  return Object.fromEntries(
    RESOURCES.map((resource) => [
      resource,
      balance[resource] - normalized[resource],
    ]),
  ) as typeof EMPTY_RESOURCES;
};
const credit = (
  balance: Record<(typeof RESOURCES)[number], number>,
  amount: ResourceAmounts,
) => {
  const normalized = normalizeResources(amount);
  return Object.fromEntries(
    RESOURCES.map((resource) => [
      resource,
      balance[resource] + normalized[resource],
    ]),
  ) as typeof EMPTY_RESOURCES;
};

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
    phase,
    phaseEnteredAtSeconds: null,
    terminal: null,
    objectiveLatches: [],
    requirementFacts: {},
    entityStates,
    arrivedEntities: {},
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
    recoveredEntities: [],
    releasedRosterIds: [],
    resolvedWaves: [],
    selectedRoutes: {},
    heldSeconds: {},
    deadlineWarnings: [],
    departedEntities: [],
  };
  return capabilitySnapshotSchema.parse(snapshot);
}

function objectiveRequirements(
  profile: CapabilityProfileV2,
  objectiveId: string,
) {
  return profile.objectivePlan.find((o) => o.id === objectiveId)?.predicate
    .requirements;
}
function factKey(objectiveId: string, requirementId: string) {
  return `${objectiveId}.${requirementId}`;
}
function factsFor(
  state: CapabilitySnapshot,
  objectiveId: string,
  requirementId: string,
) {
  return state.requirementFacts[factKey(objectiveId, requirementId)] ?? [];
}
function addFact(
  state: CapabilitySnapshot,
  objectiveId: string,
  requirementId: string,
  value: string,
) {
  const key = factKey(objectiveId, requirementId);
  return asRecord({
    ...state.requirementFacts,
    [key]: sortUnique([...(state.requirementFacts[key] ?? []), value]),
  });
}
function secondaryRequirementsSatisfied(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  sideId: string,
) {
  const side = profile.secondaryObjectives.find((item) => item.id === sideId);
  if (!side) return false;
  return side.predicate.requirements.every((req, index) => {
    if (req.kind === "entity-arrival")
      return (
        req.entities.filter(
          (id) => state.arrivedEntities[id] === req.destinations[id],
        ).length >= req.requiredCount
      );
    if (req.kind === "atomic-payment")
      return state.paidReceipts.includes(req.receipt);
    if (req.kind === "visit-zones")
      return req.zones.every((id) => state.visitedZones.includes(id));
    return (
      factsFor(state, sideId, `requirement-${index}`).includes(req.entity) &&
      state.paidReceipts.includes(req.paymentReceipt)
    );
  });
}
function mainRequirementSatisfied(
  state: CapabilitySnapshot,
  objectiveId: string,
  requirement: CapabilityProfileV2["objectivePlan"][number]["predicate"]["requirements"][number],
) {
  const facts = factsFor(state, objectiveId, requirement.id);
  switch (requirement.kind) {
    case "entity-state":
      if (requirement.state === "arrived")
        return (
          requirement.entities.filter(
            (id) =>
              state.arrivedEntities[id] === requirement.destinations?.[id],
          ).length >= requirement.requiredCount
        );
      if (requirement.state === "destroyed")
        return (
          requirement.entities.filter(
            (id) => state.entityStates[id] === "destroyed",
          ).length >= requirement.requiredCount
        );
      return facts.length >= requirement.requiredCount;
    case "resource-transaction":
      return state.paidReceipts.includes(requirement.paidFlag);
    case "minimum-stock": {
      const account =
        requirement.account === "spendable"
          ? state.spendable
          : state.protectedRecovery;
      return RESOURCES.every(
        (resource) => account[resource] >= (requirement.amounts[resource] ?? 0),
      );
    }
    case "receipt-exists":
      return state.paidReceipts.includes(requirement.flag);
    case "paired-delivery":
      return facts.length >= requirement.requiredCount;
    case "route-choice":
      return (
        state.selectedRoutes[factKey(objectiveId, requirement.id)] !== undefined
      );
    case "finite-wave-resolution":
      return (
        requirement.waves.filter((id) => state.resolvedWaves.includes(id))
          .length >= requirement.requiredCount
      );
    case "hold-area":
      return requirement.zones.every(
        (id) => (state.heldSeconds[id] ?? 0) >= requirement.continuousSeconds,
      );
    case "forbidden-entry":
      return !state.forbiddenEntries.some((id) =>
        id.startsWith(`${factKey(objectiveId, requirement.id)}:`),
      );
    case "ordered-departure":
      return (
        state.objectiveLatches.includes(requirement.receiptObjective) &&
        requirement.departingEntities.every((id) =>
          state.departedEntities.includes(id),
        )
      );
    case "derived-token":
      return requirement.outputEntities.every((id) => facts.includes(id));
    case "phase-deadline":
      return facts.length > 0;
    case "area-state":
      return (
        facts.length >= requirement.requiredCount || facts.includes("satisfied")
      );
    case "civilian-protection":
      return facts.includes("satisfied");
  }
}
function objectiveSatisfied(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  objectiveId: string,
) {
  const objective = profile.objectivePlan.find(
    (item) => item.id === objectiveId,
  );
  return (
    !!objective &&
    objective.predicate.requirements.every((req) =>
      mainRequirementSatisfied(state, objectiveId, req),
    )
  );
}
function isActive(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  objectiveId: string,
) {
  const objective = profile.objectivePlan.find(
    (item) => item.id === objectiveId,
  );
  return (
    !!objective &&
    state.phase === objective.phase &&
    objective.after.every((id) => state.objectiveLatches.includes(id))
  );
}
function closeAvailableSecondaries(
  state: CapabilitySnapshot,
): CapabilitySnapshot["secondaryStates"] {
  return Object.fromEntries(
    Object.entries(state.secondaryStates).map(([id, value]) => [
      id,
      value === "available" ? "closed-at-terminal" : value,
    ]),
  );
}
function finalize(state: CapabilitySnapshot): CapabilitySnapshot {
  return capabilitySnapshotSchema.parse({
    ...state,
    objectiveLatches: sortUnique(state.objectiveLatches),
    visitedZones: sortUnique(state.visitedZones),
    forbiddenEntries: sortUnique(state.forbiddenEntries),
    paidReceipts: sortUnique(state.paidReceipts),
    rewardFlags: sortUnique(state.rewardFlags),
    recoveredEntities: sortUnique(state.recoveredEntities),
    releasedRosterIds: sortUnique(state.releasedRosterIds),
    resolvedWaves: sortUnique(state.resolvedWaves),
    deadlineWarnings: sortUnique(state.deadlineWarnings),
    departedEntities: sortUnique(state.departedEntities),
    requirementFacts: asRecord(state.requirementFacts),
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

export function reduceCapabilityState(
  profile: CapabilityProfileV2,
  input: CapabilitySnapshot,
  action: CapabilityAction,
): CapabilitySnapshot {
  const state = capabilitySnapshotSchema.parse(input);
  if (state.terminal) return state;
  let next = state;
  if (action.type === "record-arrival") {
    const entity =
      profile.worldContract.entities.find(
        (item) => item.id === action.entityId,
      ) ??
      profile.secondaryObjectives
        .flatMap((side) => side.world.entities)
        .find((item) => item.id === action.entityId);
    const zone =
      profile.worldContract.zones.find((item) => item.id === action.zoneId) ??
      profile.secondaryObjectives
        .flatMap((side) => side.world.zones)
        .find((item) => item.id === action.zoneId);
    if (!entity || !zone || state.entityStates[action.entityId] === "destroyed")
      return state;
    if (
      state.arrivedEntities[action.entityId] &&
      state.arrivedEntities[action.entityId] !== action.zoneId
    )
      return state;
    const mainTargets = profile.objectivePlan.flatMap((objective) =>
      objective.predicate.requirements
        .filter(
          (req) =>
            req.kind === "entity-state" &&
            req.state === "arrived" &&
            req.destinations?.[action.entityId] === action.zoneId,
        )
        .map((req) => ({ objectiveId: objective.id, reqId: req.id })),
    );
    const sideTargets = profile.secondaryObjectives.flatMap((side) =>
      side.predicate.requirements
        .filter(
          (req) =>
            req.kind === "entity-arrival" &&
            req.destinations[action.entityId] === action.zoneId,
        )
        .map((_req, index) => ({
          objectiveId: side.id,
          reqId: `requirement-${index}`,
        })),
    );
    if (mainTargets.length === 0 && sideTargets.length === 0) return state;
    const arrivals = state.arrivedEntities[action.entityId]
      ? state.arrivedEntities
      : { ...state.arrivedEntities, [action.entityId]: action.zoneId };
    let requirementFacts = state.requirementFacts;
    for (const target of [...mainTargets, ...sideTargets])
      requirementFacts = addFact(
        { ...state, requirementFacts },
        target.objectiveId,
        target.reqId,
        action.entityId,
      );
    next = {
      ...state,
      entityStates: { ...state.entityStates, [action.entityId]: "arrived" },
      arrivedEntities: arrivals,
      requirementFacts,
    };
    for (const side of profile.secondaryObjectives) {
      if (
        side.world.entities.some((item) => item.id === action.entityId) &&
        state.secondaryStates[side.id] === "failed-optional"
      )
        continue;
    }
  } else if (action.type === "destroy-entity") {
    if (!state.entityStates[action.entityId]) return state;
    const side = profile.secondaryObjectives.find((item) =>
      item.predicate.requirements.some(
        (req) =>
          (req.kind === "entity-arrival" &&
            req.entities.includes(action.entityId)) ||
          (req.kind === "entity-health" && req.entity === action.entityId),
      ),
    );
    const secondaryStates =
      side && state.secondaryStates[side.id] === "available"
        ? { ...state.secondaryStates, [side.id]: "failed-optional" as const }
        : state.secondaryStates;
    next = {
      ...state,
      entityStates: { ...state.entityStates, [action.entityId]: "destroyed" },
      secondaryStates,
    };
  } else if (action.type === "recover-entity") {
    const entity = profile.worldContract.entities.find(
      (item) => item.id === action.entityId,
    );
    if (
      !entity ||
      state.entityStates[action.entityId] !== "destroyed" ||
      state.recoveredEntities.includes(action.entityId)
    )
      return state;
    next = {
      ...state,
      entityStates: { ...state.entityStates, [action.entityId]: "alive" },
      recoveredEntities: [...state.recoveredEntities, action.entityId],
    };
  } else if (action.type === "visit-zone") {
    const exists =
      profile.worldContract.zones.some((zone) => zone.id === action.zoneId) ||
      profile.secondaryObjectives.some((side) =>
        side.world.zones.some((zone) => zone.id === action.zoneId),
      );
    if (!exists) return state;
    let requirementFacts = state.requirementFacts;
    for (const objective of profile.objectivePlan)
      for (const req of objective.predicate.requirements)
        if (req.kind === "area-state" && req.zones.includes(action.zoneId))
          requirementFacts = addFact(
            { ...state, requirementFacts },
            objective.id,
            req.id,
            action.zoneId,
          );
    for (const side of profile.secondaryObjectives)
      side.predicate.requirements.forEach((req, index) => {
        if (req.kind === "visit-zones" && req.zones.includes(action.zoneId))
          requirementFacts = addFact(
            { ...state, requirementFacts },
            side.id,
            `requirement-${index}`,
            action.zoneId,
          );
      });
    next = {
      ...state,
      visitedZones: sortUnique([...state.visitedZones, action.zoneId]),
      requirementFacts,
    };
  } else if (action.type === "record-predicate") {
    const req = objectiveRequirements(profile, action.objectiveId)?.find(
      (item) => item.id === action.requirementId,
    );
    if (
      !req ||
      [
        "resource-transaction",
        "minimum-stock",
        "receipt-exists",
        "paired-delivery",
        "route-choice",
        "finite-wave-resolution",
        "hold-area",
        "forbidden-entry",
        "ordered-departure",
        "phase-deadline",
        "derived-token",
      ].includes(req.kind)
    )
      return state;
    next = {
      ...state,
      requirementFacts: addFact(
        state,
        action.objectiveId,
        action.requirementId,
        "satisfied",
      ),
    };
  } else if (action.type === "record-pair") {
    const objective = profile.objectivePlan.find(
      (item) => item.id === action.objectiveId,
    );
    const req = objective?.predicate.requirements.find(
      (item) => item.id === action.requirementId,
    );
    if (
      !req ||
      req.kind !== "paired-delivery" ||
      !req.pairs.some(
        (pair) =>
          pair.cargo === action.cargoId && pair.receiver === action.receiverId,
      )
    )
      return state;
    const familyArrived =
      state.arrivedEntities[action.receiverId] === req.destination;
    const cargoEntity = profile.worldContract.entities.find(
      (entity) => entity.id === action.cargoId,
    );
    if (
      !familyArrived ||
      !cargoEntity ||
      state.entityStates[action.cargoId] === "destroyed"
    )
      return state;
    next = {
      ...state,
      requirementFacts: addFact(
        state,
        action.objectiveId,
        action.requirementId,
        `${action.cargoId}:${action.receiverId}`,
      ),
    };
  } else if (action.type === "choose-route") {
    const req = objectiveRequirements(profile, action.objectiveId)?.find(
      (item) => item.id === action.requirementId,
    );
    if (
      !req ||
      req.kind !== "route-choice" ||
      !req.allowedRoutes.some((route) => route.id === action.routeId)
    )
      return state;
    const key = factKey(action.objectiveId, action.requirementId);
    next = {
      ...state,
      selectedRoutes: state.selectedRoutes[key]
        ? state.selectedRoutes
        : { ...state.selectedRoutes, [key]: action.routeId },
    };
  } else if (action.type === "pay-main") {
    const req = objectiveRequirements(profile, action.objectiveId)?.find(
      (item) => item.id === action.requirementId,
    );
    if (
      !req ||
      req.kind !== "resource-transaction" ||
      state.paidReceipts.includes(req.paidFlag) ||
      !enough(
        req.account === "spendable" ? state.spendable : state.protectedRecovery,
        req.amounts,
      )
    )
      return state;
    next = {
      ...state,
      spendable:
        req.account === "spendable"
          ? debit(state.spendable, req.amounts)
          : state.spendable,
      protectedRecovery:
        req.account === "protected-recovery"
          ? debit(state.protectedRecovery, req.amounts)
          : state.protectedRecovery,
      paidReceipts: [...state.paidReceipts, req.paidFlag],
      requirementFacts: addFact(
        state,
        action.objectiveId,
        action.requirementId,
        req.paidFlag,
      ),
    };
  } else if (action.type === "pay-secondary") {
    const side = profile.secondaryObjectives.find(
      (item) => item.id === action.objectiveId,
    );
    const req = side?.predicate.requirements.find(
      (item) => item.kind === "atomic-payment",
    );
    if (!req || req.receipt !== action.receipt) return state;
    if (
      !side ||
      state.secondaryStates[side.id] !== "available" ||
      state.paidReceipts.includes(req.receipt) ||
      (req.afterArrival &&
        !side.predicate.requirements
          .filter((item) => item.kind === "entity-arrival")
          .every(
            (arrival) =>
              arrival.entities.filter(
                (id) => state.arrivedEntities[id] === arrival.destinations[id],
              ).length >= arrival.requiredCount,
          )) ||
      !enough(state.spendable, req.resources)
    )
      return state;
    next = {
      ...state,
      spendable: debit(state.spendable, req.resources),
      paidReceipts: [...state.paidReceipts, req.receipt],
    };
  } else if (action.type === "record-secondary-predicate") {
    const side = profile.secondaryObjectives.find(
      (item) => item.id === action.objectiveId,
    );
    const req = side?.predicate.requirements[action.requirementIndex];
    if (
      !side ||
      req?.kind !== "entity-health" ||
      state.entityStates[req.entity] === "destroyed" ||
      !state.paidReceipts.includes(req.paymentReceipt)
    )
      return state;
    next = {
      ...state,
      requirementFacts: addFact(
        state,
        side.id,
        `requirement-${action.requirementIndex}`,
        req.entity,
      ),
    };
  } else if (action.type === "award-secondary") {
    const side = profile.secondaryObjectives.find(
      (item) => item.id === action.objectiveId,
    );
    if (
      !side ||
      state.secondaryStates[side.id] !== "available" ||
      !secondaryRequirementsSatisfied(profile, state, side.id)
    )
      return state;
    const reward = side.effects.reduce(
      (all, effect) => {
        for (const resource of RESOURCES)
          all[resource] += effect.resources[resource] ?? 0;
        return all;
      },
      { ...EMPTY_RESOURCES },
    );
    if (!enough(state.optionalReserve, reward)) return state;
    const rewardFlags = side.effects.map((effect) => effect.onceFlag);
    if (rewardFlags.some((flag) => state.rewardFlags.includes(flag)))
      return state;
    const requirementFacts = asRecord({
      ...state.requirementFacts,
      [factKey(side.id, "completed")]: [side.completionFlag],
    });
    next = {
      ...state,
      optionalReserve: debit(state.optionalReserve, reward),
      spendable: credit(state.spendable, reward),
      rewardFlags: [...state.rewardFlags, ...rewardFlags],
      secondaryStates: { ...state.secondaryStates, [side.id]: "completed" },
      requirementFacts,
    };
  } else if (action.type === "release-wave") {
    const wave = profile.enemyRoster.mobilizations.find(
      (item) => item.id === action.waveId,
    );
    if (
      !wave ||
      state.releasedRosterIds.some((id) => wave.entityIds.includes(id))
    )
      return state;
    next = {
      ...state,
      releasedRosterIds: [...state.releasedRosterIds, ...wave.entityIds],
    };
  } else if (action.type === "record-wave-resolved") {
    const wave = profile.enemyRoster.mobilizations.find(
      (item) => item.id === action.waveId,
    );
    if (
      !wave ||
      wave.entityIds.some((id) => !state.releasedRosterIds.includes(id))
    )
      return state;
    next = { ...state, resolvedWaves: [...state.resolvedWaves, action.waveId] };
  } else if (action.type === "record-hold") {
    if (
      !Number.isSafeInteger(action.elapsedSeconds) ||
      action.elapsedSeconds < 0
    )
      return state;
    const exists = profile.objectivePlan.some((objective) =>
      objective.predicate.requirements.some(
        (req) => req.kind === "hold-area" && req.zones.includes(action.zoneId),
      ),
    );
    if (!exists) return state;
    next = {
      ...state,
      heldSeconds: {
        ...state.heldSeconds,
        [action.zoneId]: action.elapsedSeconds,
      },
    };
  } else if (action.type === "record-forbidden-entry") {
    const req = profile.objectivePlan
      .flatMap((objective) =>
        objective.predicate.requirements.map((item) => ({ objective, item })),
      )
      .find(
        ({ item }) =>
          item.id === action.requirementId && item.kind === "forbidden-entry",
      );
    if (!req) return state;
    next = {
      ...state,
      forbiddenEntries: [
        ...state.forbiddenEntries,
        `${factKey(req.objective.id, req.item.id)}:${action.actorId}`,
      ],
    };
  } else if (action.type === "record-departure") {
    const req = objectiveRequirements(profile, action.objectiveId)?.find(
      (item) => item.id === action.requirementId,
    );
    if (
      !req ||
      req.kind !== "ordered-departure" ||
      !req.departingEntities.includes(action.entityId) ||
      !state.objectiveLatches.includes(req.receiptObjective)
    )
      return state;
    next = {
      ...state,
      departedEntities: [...state.departedEntities, action.entityId],
    };
  } else if (action.type === "enter-phase") {
    const transition = profile.stateMachine.phaseTransitions.find(
      (item) => item.from === state.phase && item.to === action.phase,
    );
    if (
      !transition ||
      !profile.stateMachine.states.includes(action.phase) ||
      !Number.isFinite(action.nowSeconds) ||
      action.nowSeconds < 0
    )
      return state;
    if (
      transition.on === "objective-latched" &&
      (!transition.objectiveId ||
        !state.objectiveLatches.includes(transition.objectiveId))
    )
      return state;
    next = {
      ...state,
      phase: action.phase,
      phaseEnteredAtSeconds: action.nowSeconds,
    };
  } else if (action.type === "latch-objective") {
    const objective = profile.objectivePlan.find(
      (item) => item.id === action.objectiveId,
    );
    if (
      !objective ||
      !isActive(profile, state, objective.id) ||
      !objectiveSatisfied(profile, state, objective.id)
    )
      return state;
    next = {
      ...state,
      objectiveLatches: [...state.objectiveLatches, objective.id],
    };
  } else if (action.type === "tick") {
    if (
      !Number.isFinite(action.nowSeconds) ||
      action.nowSeconds < 0 ||
      state.phaseEnteredAtSeconds === null ||
      action.nowSeconds < state.phaseEnteredAtSeconds
    )
      return state;
    const elapsed = action.nowSeconds - state.phaseEnteredAtSeconds;
    const activeDeadlines = profile.objectivePlan.flatMap((objective) =>
      objective.predicate.requirements.flatMap((req) =>
        req.kind === "phase-deadline" && req.phase === state.phase
          ? [{ objective, req }]
          : [],
      ),
    );
    const expired = activeDeadlines.some(({ objective, req }) => {
      const limit = req.secondsByDifficulty[action.difficulty];
      return elapsed >= limit && !state.objectiveLatches.includes(objective.id);
    });
    const defeat =
      action.defeatConditions.length > 0 ||
      expired ||
      profile.worldContract.survivorGroups.some((group) => {
        const possible = group.entities.filter(
          (id) =>
            state.entityStates[id] !== "destroyed" ||
            state.recoveredEntities.includes(id) ||
            !!state.arrivedEntities[id],
        ).length;
        return possible < group.minimumAliveOrAlreadySafe;
      });
    if (defeat) {
      next = {
        ...state,
        terminal: "defeat",
        secondaryStates: closeAvailableSecondaries(state),
      };
    } else {
      const won = action.victoryConditions.some((objectiveId) => {
        const transition = profile.stateMachine.phaseTransitions.find(
          (item) =>
            item.from === state.phase &&
            item.to === "victory" &&
            item.objectiveId === objectiveId,
        );
        return !!transition && state.objectiveLatches.includes(objectiveId);
      });
      if (won)
        next = {
          ...state,
          terminal: "victory",
          phase: "victory",
          secondaryStates: closeAvailableSecondaries(state),
        };
      const warnings = activeDeadlines.flatMap(({ objective, req }) => {
        const key = `${objective.id}.${req.id}`;
        const remaining = req.secondsByDifficulty[action.difficulty] - elapsed;
        return remaining <= req.warningSeconds &&
          remaining > 0 &&
          !state.deadlineWarnings.includes(key)
          ? [key]
          : [];
      });
      if (warnings.length && !next.terminal)
        next = {
          ...next,
          deadlineWarnings: [...next.deadlineWarnings, ...warnings],
        };
    }
  }
  return finalize(next);
}
