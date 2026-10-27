import { assertValid } from "../core/diagnostics.helper";
import { canonical, hash } from "../core/serialization.helper";
import { validateScenarioCapability } from "../gameplay-validation/scenario-capability.validator";
import {
  type CapabilityProfileV3,
  capabilityProfileV3Schema,
  sharedCapabilityProfile,
} from "../schemas/alternative-fulfillment.schema";
import { generationReady } from "./capability-generation.helper";
import {
  capabilityFingerprint,
  createCapabilitySnapshot,
} from "./capability-snapshot.factory";
import { validateFulfillmentCore } from "./fulfillment-core-snapshot.validator";
import {
  committedShares,
  recipeTotal,
  sameResources,
  sameValue,
  selectedRecipes,
} from "./fulfillment-plan.helper";
import {
  type FulfillmentSnapshot,
  fulfillmentSnapshotSchema,
} from "./fulfillment-snapshot.schema";
import { credit, EMPTY_RESOURCES, RESOURCES } from "./resource-accounts.helper";

export const fulfillmentFingerprint = (profile: CapabilityProfileV3) =>
  hash(canonical(capabilityProfileV3Schema.parse(profile)));

export function createFulfillmentSnapshot(
  profile: CapabilityProfileV3,
  accounts: Parameters<typeof createCapabilitySnapshot>[1],
  difficulty: "easy" | "standard" | "hard" = "standard",
): FulfillmentSnapshot {
  assertValid(validateScenarioCapability(profile));
  const core = {
    ...createCapabilitySnapshot(sharedCapabilityProfile(profile), accounts),
    difficulty,
  };
  return validateFulfillmentSnapshot(profile, {
    schemaVersion: 3,
    profile: "composed-world-ledger",
    contractFingerprint: fulfillmentFingerprint(profile),
    planId: profile.fulfillmentPlan.id,
    initialTotal: credit(
      credit(core.spendable, core.protectedRecovery),
      core.optionalReserve,
    ),
    core,
    escrow: { ...EMPTY_RESOURCES },
    committedExpenditure: { ...EMPTY_RESOURCES },
    fixedMainExpenditure: { ...EMPTY_RESOURCES },
    optionalExpenditure: { ...EMPTY_RESOURCES },
    attemptCounter: 0,
    revision: 0,
    active: null,
  });
}

/** Shared fixed/optional transactions remain owned by the existing reducer. */
export function sharedExpenditure(
  profile: CapabilityProfileV3,
  state: FulfillmentSnapshot,
) {
  let fixedMain = { ...EMPTY_RESOURCES };
  let optional = { ...EMPTY_RESOURCES };
  const known = new Set<string>();
  for (const objective of profile.objectivePlan)
    for (const req of objective.predicate.requirements)
      if (req.kind === "resource-transaction") {
        known.add(req.paidFlag);
        if (state.core.paidReceipts.includes(req.paidFlag))
          fixedMain = credit(fixedMain, req.amounts);
      }
  for (const side of profile.secondaryObjectives)
    for (const req of side.predicate.requirements)
      if (req.kind === "atomic-payment") {
        known.add(req.receipt);
        if (state.core.paidReceipts.includes(req.receipt))
          optional = credit(optional, req.resources);
      }
  return { fixedMain, optional, known };
}

export function validateFulfillmentSnapshot(
  profile: CapabilityProfileV3,
  input: unknown,
): FulfillmentSnapshot {
  const state = fulfillmentSnapshotSchema.parse(input);
  const sharedProfile = sharedCapabilityProfile(profile);
  validateFulfillmentCore(sharedProfile, state.core);
  const fail = (detail: string): never => {
    throw new Error(`fulfillment.snapshot-invalid: ${detail}`);
  };
  if (
    state.contractFingerprint !== fulfillmentFingerprint(profile) ||
    state.planId !== profile.fulfillmentPlan.id ||
    state.core.contractFingerprint !==
      capabilityFingerprint(sharedProfile)
  )
    fail("contract mismatch");
  const expense = sharedExpenditure(profile, state);
  if (
    !sameResources(expense.fixedMain, state.fixedMainExpenditure) ||
    !sameResources(expense.optional, state.optionalExpenditure) ||
    state.core.paidReceipts.some((id) => !expense.known.has(id))
  )
    fail("shared expenditure receipts");
  for (const resource of RESOURCES) {
    const total =
      state.core.spendable[resource] +
      state.core.protectedRecovery[resource] +
      state.core.optionalReserve[resource] +
      state.escrow[resource] +
      state.committedExpenditure[resource] +
      state.fixedMainExpenditure[resource] +
      state.optionalExpenditure[resource];
    if (!Number.isSafeInteger(total) || total !== state.initialTotal[resource])
      fail("resource conservation");
  }
  const active = state.active;
  if (
    active &&
    !state.core.terminal &&
    state.core.phase !== profile.fulfillmentPlan.phase &&
    (active.status !== "committed" ||
      active.completedServices.length !==
        profile.fulfillmentPlan.services.length)
  )
    fail("unfinished plan outside work phase");
  if (state.attemptCounter > Math.floor(Number.MAX_SAFE_INTEGER / 2))
    fail("attempt exhaustion");
  if (!active) {
    if (
      state.revision !== state.attemptCounter * 2 ||
      !sameResources(state.escrow, EMPTY_RESOURCES) ||
      !sameResources(state.committedExpenditure, EMPTY_RESOURCES)
    )
      fail("inactive ledger");
  } else {
    const recipes = selectedRecipes(profile, active.selection);
    if (
      !recipes ||
      active.attempt !== state.attemptCounter ||
      active.attempt < 1
    )
      fail("selected identity");
    const selected = recipes ?? [];
    const total = recipeTotal(selected);
    if (
      state.revision !==
      state.attemptCounter * 2 - (active.status === "reserved" ? 1 : 0)
    )
      fail("lifecycle revision");
    if (active.status === "reserved") {
      if (
        !sameResources(state.escrow, total) ||
        !sameResources(state.committedExpenditure, EMPTY_RESOURCES) ||
        active.committedAtSequence !== null ||
        active.committedShares.length ||
        Object.keys(active.departures).length ||
        Object.keys(active.work).length ||
        active.generated.length ||
        active.completedServices.length
      )
        fail("uncommitted reservation");
    } else {
      if (
        !sameResources(state.escrow, EMPTY_RESOURCES) ||
        !sameResources(state.committedExpenditure, total) ||
        !sameValue(
          active.committedShares,
          committedShares(profile, active.selection),
        ) ||
        active.committedAtSequence === null
      )
        fail("committed shares");
      const last = state.core.liveSpatialObservation?.sequence;
      if (
        last === null ||
        last === undefined ||
        (active.committedAtSequence ?? Infinity) > last
      )
        fail("commit observation");
      for (const [id, sequence] of Object.entries(active.departures))
        if (
          !selected.some((recipe) => recipe.id === id) ||
          sequence <= (active.committedAtSequence ?? Infinity) ||
          sequence > (last ?? -1)
        )
          fail("departure receipt");
      for (const [id, sequence] of Object.entries(active.work))
        if (
          !Object.hasOwn(active.departures, id) ||
          sequence <= (active.departures[id] ?? Infinity) ||
          sequence > (last ?? -1)
        )
          fail("work receipt");
      if (
        new Set(active.generated).size !== active.generated.length ||
        active.generated.some((id) => !Object.hasOwn(active.work, id))
      )
        fail("generated receipt");
      if (
        new Set(active.completedServices).size !==
          active.completedServices.length ||
        active.completedServices.some(
          (id) =>
            !active.selection.some(
              (item) =>
                item.serviceId === id &&
                active.generated.includes(item.recipeId),
            ),
        )
      )
        fail("service receipt");
    }
  }
  const knownEntities = new Set([
    ...profile.worldContract.entities.map((entity) => entity.id),
    ...profile.secondaryObjectives.flatMap((side) =>
      side.world.entities.map((entity) => entity.id),
    ),
  ]);
  if (
    Object.keys(state.core.entityStates).length !== knownEntities.size ||
    Object.keys(state.core.entityStates).some((id) => !knownEntities.has(id))
  )
    fail("world identity membership");
  const recipes = profile.fulfillmentPlan.services.flatMap(
    (service) => service.recipes,
  );
  const knownZones = new Set([
    ...profile.worldContract.zones.map((zone) => zone.id),
    ...profile.secondaryObjectives.flatMap((side) =>
      side.world.zones.map((zone) => zone.id),
    ),
  ]);
  for (const [id, observation] of Object.entries(
    state.core.liveSpatialObservation?.entities ?? {},
  )) {
    if (
      !knownEntities.has(id) ||
      observation.zones.length > 1 ||
      observation.zones.some((zone) => !knownZones.has(zone)) ||
      (!observation.alive && observation.zones.length > 0) ||
      (observation.alive && state.core.entityStates[id] === "destroyed")
    )
      fail("observation membership");
    if (
      recipes.some(
        (recipe) =>
          recipe.outputEntityId === id &&
          !active?.generated.includes(recipe.id),
      )
    )
      fail("observation of unavailable output");
  }
  for (const recipe of recipes)
    if (
      !active?.generated.includes(recipe.id) &&
      state.core.entityStates[recipe.outputEntityId] !== "alive"
    )
      fail("unavailable output changed");
  if (
    state.core.terminal === "victory" &&
    (!active ||
      active.status !== "committed" ||
      active.completedServices.length !==
        profile.fulfillmentPlan.services.length ||
      !fulfillmentPresent(profile, state))
  )
    fail("victory without selected reception");
  return state;
}

/** Historical latches alone never establish final residence. */
export function fulfillmentPresent(
  profile: CapabilityProfileV3,
  state: FulfillmentSnapshot,
) {
  const active = state.active;
  if (!active || active.status !== "committed") return false;
  const recipes = selectedRecipes(profile, active.selection);
  if (!recipes) return false;
  let sharedProfile: ReturnType<typeof sharedCapabilityProfile> | undefined;
  const isCurrentlyPresent = (id: string, receptionZoneId: string) => {
    if (state.core.entityStates[id] === "destroyed") return false;
    if (sharedProfile === undefined)
      sharedProfile = sharedCapabilityProfile(profile);
    if (!generationReady(sharedProfile, state.core, id)) return false;
    const observation = state.core.liveSpatialObservation?.entities[id];
    return (
      observation?.alive === true && observation.zones.includes(receptionZoneId)
    );
  };
  return recipes.every(
    (recipe) =>
      active.generated.includes(recipe.id) &&
      [recipe.outputEntityId, ...recipe.recipientIds].every((id) =>
        isCurrentlyPresent(id, recipe.receptionZoneId),
      ),
  );
}

/** Rotate this ephemeral input context whenever a world/save is restored. */
export const createFulfillmentInputContext = () => ({
  epoch: crypto.randomUUID(),
});

export function loadFulfillmentSnapshot(
  profile: CapabilityProfileV3,
  input: unknown,
) {
  assertValid(validateScenarioCapability(profile));
  return {
    snapshot: validateFulfillmentSnapshot(profile, input),
    inputContext: createFulfillmentInputContext(),
  };
}
