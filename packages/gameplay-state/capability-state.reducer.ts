import {
  paymentReceiptMatches,
  paymentReceiptPrecedesObjective,
} from "../gameplay-validation/payment-receipt.helper";
import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";
import type { CapabilityAction } from "./capability-action.model";
import {
  addFact,
  arrivalKey,
  asRecord,
  factKey,
  hasArrival,
  objectiveRequirements,
  sortUnique,
} from "./capability-ledgers.helper";
import {
  departureReceiptSatisfied,
  generationReady,
  hasIrrecoverableLoss,
  isActive,
  objectiveSatisfied,
  secondaryRequirementsSatisfied,
} from "./capability-predicates.validator";
import {
  capabilityFingerprint,
  closeAvailableSecondaries,
  finalize,
  finishTerminal,
} from "./capability-snapshot.factory";
import {
  type CapabilitySnapshot,
  capabilitySnapshotSchema,
} from "./capability-snapshot.schema";
import {
  credit,
  debit,
  EMPTY_RESOURCES,
  enough,
  RESOURCES,
} from "./resource-accounts.helper";

export function reduceCapabilityState(
  profile: CapabilityProfileV2,
  input: CapabilitySnapshot,
  action: CapabilityAction,
): CapabilitySnapshot {
  const state = capabilitySnapshotSchema.parse(input);
  if (state.contractFingerprint !== capabilityFingerprint(profile))
    throw new Error(
      "capability.snapshot-contract-mismatch: saved state belongs to a different objective contract",
    );
  if (state.terminal) return state;
  if (hasIrrecoverableLoss(profile, state))
    return finishTerminal(state, "defeat");
  let next = state;
  if (action.type === "observe-zone") {
    if (!profile.worldContract.zones.some((zone) => zone.id === action.zoneId))
      return state;
    next = {
      ...state,
      zoneConditions: {
        ...state.zoneConditions,
        [action.zoneId]: {
          controlled: action.controlled,
          passable: action.passable,
          protected: action.protected,
        },
      },
      heldSeconds:
        action.controlled && action.passable
          ? state.heldSeconds
          : { ...state.heldSeconds, [action.zoneId]: 0 },
    };
  } else if (action.type === "observe-entity-state") {
    const req = objectiveRequirements(profile, action.objectiveId)?.find(
      (item) => item.id === action.requirementId,
    );
    if (
      !req ||
      req.kind !== "entity-state" ||
      !req.entities.includes(action.entityId) ||
      !generationReady(profile, state, action.entityId) ||
      state.entityStates[action.entityId] === "destroyed" ||
      ["arrived", "alive", "destroyed"].includes(req.state)
    )
      return state;
    if (
      (req.inputRecords ?? []).some(
        (id) => !state.observedEntityStates[id]?.includes("collected"),
      )
    )
      return state;
    if (req.carriedRecords?.length) return state; // Inventory transport needs a typed ownership contract, not an arbitrary observation.
    if (
      req.state === "registered-after-arrival" ||
      req.state === "sealed-and-delivered"
    ) {
      if (
        !hasArrival(
          state,
          action.entityId,
          req.destinations?.[action.entityId] ?? "",
        )
      )
        return state;
    }
    next = {
      ...state,
      observedEntityStates: {
        ...state.observedEntityStates,
        [action.entityId]: sortUnique([
          ...(state.observedEntityStates[action.entityId] ?? []),
          req.state,
        ]),
      },
      requirementFacts: addFact(
        state,
        action.objectiveId,
        req.id,
        action.entityId,
      ),
    };
  } else if (action.type === "derive-token") {
    const req = objectiveRequirements(profile, action.objectiveId)?.find(
      (item) => item.id === action.requirementId,
    );
    if (
      !req ||
      req.kind !== "derived-token" ||
      !isActive(profile, state, action.objectiveId) ||
      req.inputEntities.some(
        (id) =>
          !state.observedEntityStates[id]?.includes("collected") ||
          state.entityStates[id] === "destroyed",
      ) ||
      (req.requiredPaymentReceipts ?? []).some(
        (receipt) =>
          !paymentReceiptMatches(profile, receipt) ||
          !paymentReceiptPrecedesObjective(
            profile,
            receipt.fromObjective,
            action.objectiveId,
          ) ||
          !state.paidReceipts.includes(receipt.flag),
      ) ||
      req.outputEntities.some((id) => state.entityStates[id] === "destroyed")
    )
      return state;
    let requirementFacts = state.requirementFacts;
    for (const output of req.outputEntities)
      requirementFacts = addFact(
        { ...state, requirementFacts },
        action.objectiveId,
        req.id,
        output,
      );
    next = { ...state, requirementFacts };
  } else if (action.type === "record-arrival") {
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
    const mainTargets = profile.objectivePlan.flatMap((objective) =>
      objective.predicate.requirements
        .filter(
          (req) =>
            (req.kind === "entity-state" &&
              req.destinations?.[action.entityId] === action.zoneId) ||
            (req.kind === "paired-delivery" &&
              req.destination === action.zoneId &&
              req.pairs.some(
                (pair) =>
                  pair.cargo === action.entityId ||
                  pair.receiver === action.entityId,
              )),
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
    if (!generationReady(profile, state, action.entityId)) return state;
    const arrivalLedger = sortUnique([
      ...state.arrivalLedger,
      arrivalKey(state.phase, action.entityId, action.zoneId),
    ]);
    const arrivals = state.arrivedEntities[action.entityId]
      ? state.arrivedEntities
      : { ...state.arrivedEntities, [action.entityId]: action.zoneId };
    let requirementFacts = state.requirementFacts;
    for (const target of [...mainTargets, ...sideTargets]) {
      const req = objectiveRequirements(profile, target.objectiveId)?.find(
        (item) => item.id === target.reqId,
      );
      if (req && (req.kind !== "entity-state" || req.state !== "arrived"))
        continue;
      requirementFacts = addFact(
        { ...state, requirementFacts },
        target.objectiveId,
        target.reqId,
        action.entityId,
      );
    }
    next = {
      ...state,
      entityStates: { ...state.entityStates, [action.entityId]: "arrived" },
      arrivedEntities: arrivals,
      arrivalLedger,
      requirementFacts,
    };
  } else if (action.type === "destroy-entity") {
    if (!state.entityStates[action.entityId]) return state;
    if (!generationReady(profile, state, action.entityId)) return state;
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
        "area-state",
        "civilian-protection",
        "entity-state",
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
      hasArrival(state, action.receiverId, req.destination) &&
      state.entityStates[action.receiverId] !== "destroyed";
    const cargoEntity = profile.worldContract.entities.find(
      (entity) => entity.id === action.cargoId,
    );
    if (
      !familyArrived ||
      !cargoEntity ||
      !hasArrival(state, action.cargoId, req.destination) ||
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
              [...new Set(arrival.entities)].filter((id) =>
                hasArrival(state, id, arrival.destinations[id] ?? ""),
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
      !Number.isFinite(action.healthFraction) ||
      action.healthFraction !== 1 ||
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
      wave.entityIds.some(
        (id) =>
          !state.releasedRosterIds.includes(id) ||
          state.entityStates[id] !== "destroyed",
      )
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
    if (
      !state.zoneConditions[action.zoneId]?.controlled ||
      !state.zoneConditions[action.zoneId]?.passable
    )
      return state;
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
    if (
      req.item.kind !== "forbidden-entry" ||
      !state.enteredPhases.includes(req.item.activeFrom)
    )
      return state;
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
      !departureReceiptSatisfied(profile, state, req) ||
      state.entityStates[action.entityId] === "destroyed"
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
      action.nowSeconds < 0 ||
      (state.phaseEnteredAtSeconds !== null &&
        action.nowSeconds <
          state.phaseEnteredAtSeconds + state.phaseElapsedSeconds)
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
      phaseElapsedSeconds: 0,
      enteredPhases: sortUnique([...state.enteredPhases, action.phase]),
      terminal:
        action.phase === "victory" || action.phase === "defeat"
          ? action.phase
          : null,
      secondaryStates:
        action.phase === "victory" || action.phase === "defeat"
          ? closeAvailableSecondaries(state)
          : state.secondaryStates,
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
      action.nowSeconds <
        state.phaseEnteredAtSeconds + state.phaseElapsedSeconds
    )
      return state;
    const elapsed = action.nowSeconds - state.phaseEnteredAtSeconds;
    next = {
      ...state,
      difficulty: action.difficulty,
      phaseElapsedSeconds: elapsed,
    };
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
      hasIrrecoverableLoss(profile, state);
    if (defeat) {
      next = finishTerminal(next, "defeat");
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
          difficulty: action.difficulty,
          phaseElapsedSeconds: elapsed,
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
  if (hasIrrecoverableLoss(profile, next))
    next = finishTerminal(next, "defeat");
  return finalize(profile, next);
}
