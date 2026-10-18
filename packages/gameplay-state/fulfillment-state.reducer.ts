import {
  type CapabilityProfileV3,
  sharedCapabilityProfile,
} from "../schemas/alternative-fulfillment.schema";
import type { CapabilityAction } from "./capability-action.model";
import { generationReady } from "./capability-generation.helper";
import { hasIrrecoverableLoss } from "./capability-predicates.validator";
import { finishTerminal } from "./capability-snapshot.factory";
import { reduceCapabilityState } from "./capability-state.reducer";
import {
  type FulfillmentInputContext,
  fulfillmentActionSchema,
} from "./fulfillment-action.model";
import {
  committedShares,
  recipeTotal,
  sameResources,
  selectedRecipes,
} from "./fulfillment-plan.helper";
import {
  fulfillmentPresent,
  sharedExpenditure,
  validateFulfillmentSnapshot,
} from "./fulfillment-snapshot.factory";
import type {
  FulfillmentSelection,
  FulfillmentSnapshot,
} from "./fulfillment-snapshot.schema";
import { applyLiveSpatialBatch } from "./live-entity-presence.helper";
import {
  credit,
  debit,
  EMPTY_RESOURCES,
  enough,
} from "./resource-accounts.helper";

function irrecoverablePlanLoss(
  profile: CapabilityProfileV3,
  state: FulfillmentSnapshot,
) {
  const dead = (id: string) => state.core.entityStates[id] === "destroyed";
  if (state.active?.status === "committed") {
    const active = state.active;
    return (
      selectedRecipes(profile, active.selection)?.some(
        (recipe) =>
          recipe.recipientIds.some(dead) ||
          (!Object.hasOwn(active.work, recipe.id) && dead(recipe.workerId)) ||
          (active.generated.includes(recipe.id) && dead(recipe.outputEntityId)),
      ) ?? true
    );
  }
  return profile.fulfillmentPlan.services.some((service) =>
    service.recipes.every(
      (recipe) => dead(recipe.workerId) || recipe.recipientIds.some(dead),
    ),
  );
}

const finalized = (
  profile: CapabilityProfileV3,
  state: FulfillmentSnapshot,
) => {
  const expense = sharedExpenditure(profile, state);
  return validateFulfillmentSnapshot(profile, {
    ...state,
    fixedMainExpenditure: expense.fixedMain,
    optionalExpenditure: expense.optional,
  });
};

/** Free immutable preview. It neither selects an attempt nor writes a receipt. */
export function previewFulfillment(
  profile: CapabilityProfileV3,
  input: FulfillmentSnapshot,
  selection: FulfillmentSelection,
) {
  const state = validateFulfillmentSnapshot(profile, input);
  const recipes = selectedRecipes(profile, selection);
  if (
    !recipes ||
    state.core.terminal ||
    state.core.phase !== profile.fulfillmentPlan.phase ||
    state.active
  )
    return null;
  const total = recipeTotal(recipes);
  return {
    selection,
    total,
    spendable: { ...state.core.spendable },
    affordable: enough(state.core.spendable, total),
    remainder: enough(state.core.spendable, total)
      ? debit(state.core.spendable, total)
      : null,
    recipes,
  };
}

/** Versioned composition, reusing the v2 reducer and its actual observation helpers. */
export function reduceFulfillmentState(
  profile: CapabilityProfileV3,
  input: FulfillmentSnapshot,
  command: unknown,
  inputContext: FulfillmentInputContext,
): FulfillmentSnapshot {
  const state = validateFulfillmentSnapshot(profile, input);
  if (state.core.terminal) return state;
  const parsed = fulfillmentActionSchema.safeParse(command);
  if (!parsed.success) return state;
  const action = parsed.data;
  if (
    action.epoch !== inputContext.epoch ||
    action.contractFingerprint !== state.contractFingerprint
  )
    return state;
  const base = sharedCapabilityProfile(profile);
  if (
    state.core.phaseEnteredAtSeconds !== null &&
    action.nowSeconds <
      state.core.phaseEnteredAtSeconds + state.core.phaseElapsedSeconds
  )
    return state;
  // Time/known defeat precedes every debit or reward, including non-tick commands.
  const clock = reduceCapabilityState(base, state.core, {
    type: "tick",
    nowSeconds: action.nowSeconds,
    difficulty: state.core.difficulty,
    defeatConditions:
      action.type === "shared" &&
      action.action.type === "tick" &&
      action.action.nowSeconds === action.nowSeconds &&
      action.action.difficulty === state.core.difficulty
        ? action.action.defeatConditions
        : [],
    victoryConditions: [],
  });
  if (clock.terminal) return finalized(profile, { ...state, core: clock });
  // Deliberately bounded reference observation: at most one zone per identity.
  if (
    action.liveSpatialBatch.entities.some((entity) => entity.zones.length > 1)
  )
    return state;
  const allRecipes = profile.fulfillmentPlan.services.flatMap(
    (service) => service.recipes,
  );
  const unavailable = new Set(
    allRecipes
      .filter((recipe) => !state.active?.generated.includes(recipe.id))
      .map((recipe) => recipe.outputEntityId),
  );
  if (
    action.liveSpatialBatch.entities.some((entity) =>
      unavailable.has(entity.entityId),
    )
  )
    return state;
  const observed = applyLiveSpatialBatch(base, clock, action.liveSpatialBatch);
  if (!observed) return state;
  const current = { ...state, core: observed };
  if (
    hasIrrecoverableLoss(base, observed) ||
    irrecoverablePlanLoss(profile, current)
  )
    return finalized(profile, {
      ...current,
      core: finishTerminal(observed, "defeat"),
    });
  const living = (id: string) =>
    generationReady(base, observed, id) &&
    observed.entityStates[id] !== "destroyed" &&
    observed.liveSpatialObservation?.entities[id]?.alive === true;
  const at = (id: string, zone: string) =>
    living(id) &&
    observed.liveSpatialObservation?.entities[id]?.zones.includes(zone) ===
      true;

  if (action.type === "observe") return finalized(profile, current);
  if (action.type === "shared") {
    let shared: CapabilityAction = action.action;
    if (
      shared.type === "enter-phase" &&
      shared.nowSeconds !== action.nowSeconds
    )
      return finalized(profile, current);
    if ("entityId" in shared && unavailable.has(shared.entityId))
      return finalized(profile, current);
    const ready =
      current.active?.status === "committed" &&
      current.active.completedServices.length ===
        profile.fulfillmentPlan.services.length &&
      fulfillmentPresent(profile, current);
    if (shared.type === "enter-phase" && shared.phase === "victory" && !ready)
      return finalized(profile, current);
    if (shared.type === "tick") {
      if (
        shared.nowSeconds !== action.nowSeconds ||
        shared.difficulty !== state.core.difficulty
      )
        return finalized(profile, current);
      shared = {
        ...shared,
        victoryConditions: ready ? shared.victoryConditions : [],
      };
    }
    // Apply the genuine batch once to the persisted core. The preview above is
    // only a loss check; no cached batch is renumbered or asserted fresh.
    const coreAction = { ...shared, liveSpatialBatch: action.liveSpatialBatch };
    const core = reduceCapabilityState(base, clock, coreAction);
    const next = { ...current, core };
    if (!core.terminal && irrecoverablePlanLoss(profile, next))
      next.core = finishTerminal(core, "defeat");
    return finalized(profile, next);
  }
  if (observed.phase !== profile.fulfillmentPlan.phase)
    return finalized(profile, current);
  if (action.type === "reserve") {
    const recipes = selectedRecipes(profile, action.selection);
    if (
      state.active ||
      !recipes ||
      action.revision !== state.revision ||
      action.attempt !== state.attemptCounter + 1 ||
      action.attempt > Math.floor(Number.MAX_SAFE_INTEGER / 2) ||
      !sameResources(action.expectedSpendable, observed.spendable)
    )
      return finalized(profile, current);
    const total = recipeTotal(recipes);
    if (!enough(observed.spendable, total)) return finalized(profile, current);
    const selection = profile.fulfillmentPlan.services.map(
      (service, index) => ({
        serviceId: service.id,
        recipeId: recipes[index]?.id ?? "",
      }),
    );
    return finalized(profile, {
      ...current,
      core: { ...observed, spendable: debit(observed.spendable, total) },
      escrow: total,
      attemptCounter: action.attempt,
      revision: state.revision + 1,
      active: {
        attempt: action.attempt,
        selection,
        status: "reserved",
        committedAtSequence: null,
        committedShares: [],
        departures: {},
        work: {},
        generated: [],
        completedServices: [],
      },
    });
  }
  const active = state.active;
  if (
    !active ||
    action.attempt !== active.attempt ||
    action.revision !== state.revision
  )
    return finalized(profile, current);
  if (action.type === "cancel") {
    if (active.status !== "reserved") return finalized(profile, current);
    return finalized(profile, {
      ...current,
      core: {
        ...observed,
        spendable: credit(observed.spendable, state.escrow),
      },
      escrow: { ...EMPTY_RESOURCES },
      revision: state.revision + 1,
      active: null,
    });
  }
  if (action.type === "commit") {
    const recipes = selectedRecipes(profile, active.selection);
    if (
      active.status !== "reserved" ||
      !recipes ||
      recipes.some(
        (recipe) => ![recipe.workerId, ...recipe.recipientIds].every(living),
      )
    )
      return finalized(profile, current);
    return finalized(profile, {
      ...current,
      escrow: { ...EMPTY_RESOURCES },
      committedExpenditure: { ...state.escrow },
      revision: state.revision + 1,
      active: {
        ...active,
        status: "committed",
        committedAtSequence: action.liveSpatialBatch.sequence,
        committedShares: committedShares(profile, active.selection),
      },
    });
  }
  if (active.status !== "committed") return finalized(profile, current);
  const selected = active.selection.find(
    (item) =>
      item.serviceId === action.serviceId && item.recipeId === action.recipeId,
  );
  const recipe = allRecipes.find((item) => item.id === selected?.recipeId);
  if (!recipe) return finalized(profile, current);
  const sequence = action.liveSpatialBatch.sequence;
  if (action.type === "depart-for-work") {
    if (
      active.departures[recipe.id] !== undefined ||
      sequence <= (active.committedAtSequence ?? Infinity) ||
      !living(recipe.workerId) ||
      at(recipe.workerId, recipe.workZoneId)
    )
      return finalized(profile, current);
    return finalized(profile, {
      ...current,
      active: {
        ...active,
        departures: { ...active.departures, [recipe.id]: sequence },
      },
    });
  }
  if (action.type === "record-work") {
    if (
      active.work[recipe.id] !== undefined ||
      sequence <= (active.departures[recipe.id] ?? Infinity) ||
      !at(recipe.workerId, recipe.workZoneId)
    )
      return finalized(profile, current);
    return finalized(profile, {
      ...current,
      active: { ...active, work: { ...active.work, [recipe.id]: sequence } },
    });
  }
  if (action.type === "generate-output") {
    if (
      active.work[recipe.id] === undefined ||
      active.generated.includes(recipe.id)
    )
      return finalized(profile, current);
    return finalized(profile, {
      ...current,
      active: { ...active, generated: [...active.generated, recipe.id] },
    });
  }
  if (action.type === "complete-service") {
    if (
      !active.generated.includes(recipe.id) ||
      active.completedServices.includes(action.serviceId) ||
      ![recipe.outputEntityId, ...recipe.recipientIds].every((id) =>
        at(id, recipe.receptionZoneId),
      )
    )
      return finalized(profile, current);
    return finalized(profile, {
      ...current,
      active: {
        ...active,
        completedServices: [...active.completedServices, action.serviceId],
      },
    });
  }
  return finalized(profile, current);
}
