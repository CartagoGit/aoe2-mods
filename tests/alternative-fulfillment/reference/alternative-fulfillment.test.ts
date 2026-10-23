import { describe, expect, test } from "bun:test";
import { readFileSync } from "node:fs";
import { renderNativeCampaign } from "../../../packages/aoe2-adapter/native-campaign.renderer";
import { canonical, hash } from "../../../packages/core/serialization.helper";
import {
  capabilityFingerprint,
  createCapabilitySnapshot,
} from "../../../packages/gameplay-state/capability-snapshot.factory";
import {
  createFulfillmentInputContext,
  createFulfillmentSnapshot,
  fulfillmentFingerprint,
  loadFulfillmentSnapshot,
} from "../../../packages/gameplay-state/fulfillment-snapshot.factory";
import {
  previewFulfillment,
  reduceFulfillmentState,
} from "../../../packages/gameplay-state/fulfillment-state.reducer";
import { validateScenarioCapability } from "../../../packages/gameplay-validation/scenario-capability.validator";
import type { StringLock } from "../../../packages/localization/localization.catalog";
import { compileCapabilityProfile } from "../../../packages/scenario-compiler/capability.compiler";
import {
  capabilityProfileV3Schema,
  sharedCapabilityProfile,
} from "../../../packages/schemas/alternative-fulfillment.schema";
import type { Campaign } from "../../../packages/schemas/campaign.schema";
import { makeProfile } from "../../unit/checkpoint-presence.fixture";
import {
  accountsFor as accounts,
  dispatch,
  enterFulfillment,
  fixtureIds,
  fulfillmentCommand,
  liveBatch,
  makeFulfillmentProfile,
  outputIds,
  recipeIds,
  selection,
  zoneIds,
} from "./alternative-fulfillment.fixture";

const recipes = [
  [recipeIds.mealDirect, recipeIds.shelterMaterials],
  [recipeIds.mealDirect, recipeIds.shelterKit],
  [recipeIds.mealDirect, recipeIds.shelterRented],
  [recipeIds.mealHearth, recipeIds.shelterMaterials],
  [recipeIds.mealHearth, recipeIds.shelterKit],
  [recipeIds.mealHearth, recipeIds.shelterRented],
  [recipeIds.mealPurchased, recipeIds.shelterMaterials],
  [recipeIds.mealPurchased, recipeIds.shelterKit],
  [recipeIds.mealPurchased, recipeIds.shelterRented],
] as const;
const serviceSelections = recipes.map(([meal, shelter]) =>
  selection(meal, shelter),
);

type MatrixResources = {
  food: number;
  wood: number;
  gold: number;
  stone: number;
};
type MatrixPortfolioExpectation = {
  portfolioId: string;
  expectedFinalSpendable: MatrixResources;
  expectedOptionalReserveRemaining: MatrixResources;
  expectedOptionalExpenditure: MatrixResources;
};
type MatrixRow = {
  difficulty: "easy" | "standard" | "hard";
  recipes: [string, string];
  expectedAfterReserve: {
    spendable: MatrixResources;
    escrow: MatrixResources;
  };
  expectedAfterCommit: { committedExpenditure: MatrixResources };
  portfolioExpectations: MatrixPortfolioExpectation[];
};
type BeforeFundingWitness = {
  difficulty: "easy" | "standard" | "hard";
  recipes: [string, string];
  optionalOrderBeforeFunding: string[];
  expectedBeforeReserveSpendable: MatrixResources;
  expectedAfterReserveSpendable: MatrixResources;
  expectedEscrow: MatrixResources;
  expectedOptionalExpenditure: MatrixResources;
  expectedOptionalReserveRemaining: MatrixResources;
  alreadyAffordableWithoutOptionals: boolean;
};
const matrix = JSON.parse(
  readFileSync(
    new URL(
      "../../../docs/qa/alternative-fulfillment/decision/portfolio-matrix.json",
      import.meta.url,
    ),
    "utf8",
  ),
) as {
  fundingFirst: MatrixRow[];
  beforeFundingWitnesses: BeforeFundingWitness[];
  portfolios: Array<{ id: string; optionalOrder: string[] }>;
};
const matrixRecipeIds: Record<string, string> = {
  "meal-direct": recipeIds.mealDirect,
  "meal-shared-hearth": recipeIds.mealHearth,
  "meal-purchased": recipeIds.mealPurchased,
  "shelter-materials": recipeIds.shelterMaterials,
  "shelter-local-kit": recipeIds.shelterKit,
  "shelter-rented": recipeIds.shelterRented,
};
const matrixOptionalIds: Record<string, string> = {
  "neighbor-provisions": "fulfillment-fixture.optional-1",
  "voluntary-household-return": "fulfillment-fixture.optional-2",
  "source-comparison": "fulfillment-fixture.optional-3",
  "local-wayfinding": "fulfillment-fixture.optional-4",
  "slope-survey": "fulfillment-fixture.optional-5",
  "service-observation": "fulfillment-fixture.optional-6",
  "damaged-civilian-store": "fulfillment-fixture.optional-7",
};

function required<T>(value: T | undefined): T {
  if (value === undefined)
    throw new Error("Missing required reference fixture value");
  return value;
}

function selectedRecipeFor(
  profile: ReturnType<typeof makeFulfillmentProfile>,
  selected: ReturnType<typeof selection>[number],
) {
  const service = required(
    profile.fulfillmentPlan.services.find(
      (item) => item.id === selected.serviceId,
    ),
  );
  return required(
    service.recipes.find((item) => item.id === selected.recipeId),
  );
}

function finalPositionsFor(
  profile: ReturnType<typeof makeFulfillmentProfile>,
  planSelection: ReturnType<typeof selection>,
) {
  return Object.fromEntries(
    planSelection.flatMap((selected) => {
      const recipe = selectedRecipeFor(profile, selected);
      return [recipe.outputEntityId, ...recipe.recipientIds].map((id) => [
        id,
        recipe.receptionZoneId,
      ]);
    }),
  );
}

const resourceKey = (resources: Record<string, number>) =>
  [resources.food, resources.wood, resources.gold, resources.stone].join(":");

function selectionForMatrix(recipesByName: string[]) {
  const meal = matrixRecipeIds[recipesByName[0] ?? ""];
  const shelter = matrixRecipeIds[recipesByName[1] ?? ""];
  if (!meal || !shelter) throw new Error("Unknown normative matrix recipe");
  return selection(meal, shelter);
}

function completeOptional(
  profile: ReturnType<typeof makeFulfillmentProfile>,
  state: ReturnType<typeof enterFulfillment>["state"],
  context: ReturnType<typeof enterFulfillment>["context"],
  matrixOptionalId: string,
) {
  const objectiveId = matrixOptionalIds[matrixOptionalId];
  const objective = profile.secondaryObjectives.find(
    (item) => item.id === objectiveId,
  );
  if (!objectiveId || !objective)
    throw new Error(`Unknown optional matrix item: ${matrixOptionalId}`);
  let next = state;
  const dispatchShared = (action: unknown) =>
    dispatch(profile, next, context, "shared", { action });
  for (const requirement of objective.predicate.requirements) {
    if (requirement.kind === "atomic-payment")
      next = dispatchShared({
        type: "pay-secondary",
        objectiveId,
        receipt: requirement.receipt,
      });
  }
  for (const requirement of objective.predicate.requirements) {
    if (requirement.kind === "entity-arrival") {
      for (const entityId of requirement.entities)
        next = dispatchShared({
          type: "record-arrival",
          entityId,
          zoneId: requirement.destinations[entityId],
        });
    } else if (requirement.kind === "visit-zones") {
      for (const zoneId of requirement.zones)
        next = dispatchShared({ type: "visit-zone", zoneId });
    } else if (requirement.kind === "entity-health") {
      const index = objective.predicate.requirements.indexOf(requirement);
      next = dispatchShared({
        type: "record-secondary-predicate",
        objectiveId,
        requirementIndex: index,
        healthFraction: 1,
      });
    }
  }
  next = dispatchShared({ type: "award-secondary", objectiveId });
  if (next.core.secondaryStates[objectiveId] !== "completed")
    throw new Error(`Optional reference path failed: ${objectiveId}`);
  return next;
}

function completeSelectedService(
  profile: ReturnType<typeof makeFulfillmentProfile>,
  state: ReturnType<typeof enterFulfillment>["state"],
  context: ReturnType<typeof enterFulfillment>["context"],
  serviceId: string,
  recipeId: string,
  workerId: string,
  worksite: string,
  reception: string,
  recipients: string[],
  outputId: string,
  attempt: number,
) {
  let next = dispatch(profile, state, context, "depart-for-work", {
    attempt,
    revision: state.revision,
    serviceId,
    recipeId,
  });
  next = dispatch(profile, next, context, "record-work", {
    attempt,
    revision: next.revision,
    serviceId,
    recipeId,
    positions: { [workerId]: worksite },
  });
  next = dispatch(profile, next, context, "generate-output", {
    attempt,
    revision: next.revision,
    serviceId,
    recipeId,
  });
  next = dispatch(profile, next, context, "complete-service", {
    attempt,
    revision: next.revision,
    serviceId,
    recipeId,
    positions: {
      [outputId]: reception,
      ...Object.fromEntries(recipients.map((id) => [id, reception])),
    },
  });
  return next;
}

function completeSelectedPlan(
  profile: ReturnType<typeof makeFulfillmentProfile>,
  initial: ReturnType<typeof enterFulfillment>["state"],
  context: ReturnType<typeof enterFulfillment>["context"],
  planSelection: ReturnType<typeof selection>,
  attempt: number,
  terminalApi: "enter-phase" | "tick" | "none",
) {
  let state = initial;
  for (const selected of planSelection) {
    const service = profile.fulfillmentPlan.services.find(
      (item) => item.id === selected.serviceId,
    );
    const selectedRecipe = service?.recipes.find(
      (item) => item.id === selected.recipeId,
    );
    if (!service || !selectedRecipe)
      throw new Error(`Unknown selected service ${selected.serviceId}`);
    state = completeSelectedService(
      profile,
      state,
      context,
      service.id,
      selectedRecipe.id,
      selectedRecipe.workerId,
      selectedRecipe.workZoneId,
      selectedRecipe.receptionZoneId,
      selectedRecipe.recipientIds,
      selectedRecipe.outputEntityId,
      attempt,
    );
    if (!state.active?.completedServices.includes(service.id))
      throw new Error(`Selected service did not complete: ${service.id}`);
  }
  const finalPositions = finalPositionsFor(profile, planSelection);
  state = dispatch(profile, state, context, "shared", {
    action: {
      type: "record-arrival",
      entityId: fixtureIds.mealRecipient,
      zoneId: zoneIds.mealReception,
    },
    positions: finalPositions,
  });
  state = dispatch(profile, state, context, "shared", {
    action: { type: "latch-objective", objectiveId: "return" },
    positions: finalPositions,
  });
  if (!state.core.objectiveLatches.includes("return"))
    throw new Error("Final current-presence objective did not latch");
  if (terminalApi === "none") return state;
  state = dispatch(profile, state, context, "shared", {
    action:
      terminalApi === "enter-phase"
        ? { type: "enter-phase", phase: "victory", nowSeconds: 0 }
        : {
            type: "tick",
            nowSeconds: 0,
            difficulty: state.core.difficulty,
            defeatConditions: [],
            victoryConditions: ["return"],
          },
    positions: finalPositions,
  });
  if (state.core.terminal !== "victory")
    throw new Error(
      JSON.stringify({
        terminalApi,
        phase: state.core.phase,
        terminal: state.core.terminal,
        services: state.active?.completedServices,
        latches: state.core.objectiveLatches,
        observed: state.core.liveSpatialObservation?.entities,
        selected: state.active?.selection,
        generated: state.active?.generated,
        elapsed: state.core.phaseElapsedSeconds,
      }),
    );
  return state;
}

describe("alternative fulfillment reference fixture", () => {
  test("difficulty previews expose 9 / 7 / 3 affordable pairs without treating the matrix as runtime evidence", () => {
    const profile = makeFulfillmentProfile();
    const counts = (
      Object.keys({ easy: 1, standard: 1, hard: 1 }) as Array<
        "easy" | "standard" | "hard"
      >
    ).map((difficulty) => {
      const snapshot = enterFulfillment(profile, difficulty).state;
      return serviceSelections.filter(
        (choice) => previewFulfillment(profile, snapshot, choice)?.affordable,
      ).length;
    });
    expect(counts).toEqual([9, 7, 3]);
  });

  test("editing preview output cannot mutate the profile or snapshot contract", () => {
    const profile = makeFulfillmentProfile();
    const { state } = enterFulfillment(profile);
    const profileHash = fulfillmentFingerprint(profile);
    const before = structuredClone(state);
    const preview = previewFulfillment(profile, state, selection());
    if (!preview) throw new Error("Expected a draft preview");
    const previewSelection = preview.selection[0];
    const previewRecipe = preview.recipes[0];
    if (!previewSelection || !previewRecipe)
      throw new Error("Expected complete preview projections");
    previewSelection.recipeId = "mutated.recipe";
    previewRecipe.cost.food = 0;
    expect(fulfillmentFingerprint(profile)).toBe(profileHash);
    expect(state).toEqual(before);
  });

  test("27 difficulty and recipe-pair trials execute reserve, atomic rejection, cancel, and commit", () => {
    const profile = makeFulfillmentProfile();
    let trials = 0;
    for (const difficulty of ["easy", "standard", "hard"] as const) {
      for (const choice of serviceSelections) {
        trials += 1;
        const { state: initial, context } = enterFulfillment(
          profile,
          difficulty,
        );
        const preview = previewFulfillment(profile, initial, choice);
        if (!preview)
          throw new Error("Expected available preview for each fixture pair");
        let state = dispatch(profile, initial, context, "reserve", {
          attempt: 1,
          revision: 0,
          selection: choice,
          expectedSpendable: initial.core.spendable,
        });
        if (!preview.affordable) {
          expect(state.active).toBeNull();
          expect(state.attemptCounter).toBe(0);
          expect(state.core.spendable).toEqual(initial.core.spendable);
          expect(state.escrow).toEqual(initial.escrow);
          continue;
        }
        expect(state.active?.status).toBe("reserved");
        expect(state.escrow).toEqual(preview.total);
        state = dispatch(profile, state, context, "cancel", {
          attempt: 1,
          revision: 1,
        });
        expect(state.active).toBeNull();
        expect(state.core.spendable).toEqual(initial.core.spendable);
        state = dispatch(profile, state, context, "reserve", {
          attempt: 2,
          revision: 2,
          selection: choice,
          expectedSpendable: state.core.spendable,
        });
        state = dispatch(profile, state, context, "commit", {
          attempt: 2,
          revision: 3,
        });
        expect(state.active?.status).toBe("committed");
        expect(state.committedExpenditure).toEqual(preview.total);
        expect(state.core.protectedRecovery).toEqual(
          initial.core.protectedRecovery,
        );
      }
    }
    expect(trials).toBe(27);
  });

  test("the 95 matrix portfolio rows execute selected work, optional tasks, exact outputs, and fresh victory", () => {
    const profile = makeFulfillmentProfile();
    let cases = 0;
    expect(matrix.fundingFirst).toHaveLength(19);
    for (const row of matrix.fundingFirst) {
      const choice = selectionForMatrix(row.recipes);
      for (const expectation of row.portfolioExpectations) {
        cases += 1;
        const { state: initial, context } = enterFulfillment(
          profile,
          row.difficulty,
        );
        let state = dispatch(profile, initial, context, "reserve", {
          attempt: 1,
          revision: 0,
          selection: choice,
          expectedSpendable: initial.core.spendable,
        });
        expect(state.active?.status).toBe("reserved");
        expect(state.core.spendable).toEqual(
          row.expectedAfterReserve.spendable,
        );
        expect(state.escrow).toEqual(row.expectedAfterReserve.escrow);
        state = dispatch(profile, state, context, "commit", {
          attempt: 1,
          revision: 1,
        });
        expect(state.committedExpenditure).toEqual(
          row.expectedAfterCommit.committedExpenditure,
        );
        const portfolio = matrix.portfolios.find(
          (item) => item.id === expectation.portfolioId,
        );
        if (!portfolio)
          throw new Error(`Unknown portfolio ${expectation.portfolioId}`);
        for (const optionalId of portfolio.optionalOrder)
          state = completeOptional(profile, state, context, optionalId);
        state = completeSelectedPlan(
          profile,
          state,
          context,
          choice,
          1,
          cases % 2 === 0 ? "enter-phase" : "tick",
        );
        expect(state.core.spendable).toEqual(
          expectation.expectedFinalSpendable,
        );
        expect(state.core.optionalReserve).toEqual(
          expectation.expectedOptionalReserveRemaining,
        );
        expect(state.optionalExpenditure).toEqual(
          expectation.expectedOptionalExpenditure,
        );
        expect(state.active?.generated).toHaveLength(2);
        expect(state.active?.completedServices).toHaveLength(2);
        expect(state.core.terminal).toBe("victory");
      }
    }
    expect(cases).toBe(95);
  }, 30_000);

  test("all 24 before-funding witnesses perform real optional actions before their reservation", () => {
    const profile = makeFulfillmentProfile();
    expect(matrix.beforeFundingWitnesses).toHaveLength(24);
    let newlyAffordable = 0;
    for (const witness of matrix.beforeFundingWitnesses) {
      const choice = selectionForMatrix(witness.recipes);
      const { state: initial, context } = enterFulfillment(
        profile,
        witness.difficulty,
      );
      const before = previewFulfillment(profile, initial, choice);
      if (!before)
        throw new Error("Expected a pre-funding available selection");
      expect(before.affordable).toBe(witness.alreadyAffordableWithoutOptionals);
      let state = initial;
      for (const optionalId of witness.optionalOrderBeforeFunding)
        state = completeOptional(profile, state, context, optionalId);
      expect(state.core.spendable).toEqual(
        witness.expectedBeforeReserveSpendable,
      );
      if (!witness.alreadyAffordableWithoutOptionals) newlyAffordable += 1;
      state = dispatch(profile, state, context, "reserve", {
        attempt: 1,
        revision: 0,
        selection: choice,
        expectedSpendable: state.core.spendable,
      });
      expect(state.active?.status).toBe("reserved");
      expect(state.core.spendable).toEqual(
        witness.expectedAfterReserveSpendable,
      );
      expect(state.escrow).toEqual(witness.expectedEscrow);
      expect(state.optionalExpenditure).toEqual(
        witness.expectedOptionalExpenditure,
      );
      expect(state.core.optionalReserve).toEqual(
        witness.expectedOptionalReserveRemaining,
      );
    }
    expect(newlyAffordable).toBe(5);
  });

  test("reserve is atomic, cancellation refunds once, and stale replay cannot reserve twice", () => {
    const { profile, state: initial, context } = enterFulfillment();
    const reserve = fulfillmentCommand(profile, initial, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: initial.core.spendable,
    });
    const reserved = reduce(profile, initial, reserve, context);
    expect(reserved.active?.status).toBe("reserved");
    expect(resourceKey(reserved.core.spendable)).not.toBe(
      resourceKey(initial.core.spendable),
    );
    expect(reserved.escrow).toEqual({
      food: 320,
      wood: 240,
      gold: 0,
      stone: 0,
    });
    expect(reduce(profile, reserved, reserve, context)).toEqual(reserved);

    const cancelled = dispatch(profile, reserved, context, "cancel", {
      attempt: 1,
      revision: 1,
    });
    expect(cancelled.active).toBeNull();
    expect(cancelled.escrow).toEqual({ food: 0, wood: 0, gold: 0, stone: 0 });
    expect(cancelled.core.spendable).toEqual(initial.core.spendable);
    expect(cancelled.revision).toBe(2);
  });

  test("an unaffordable fresh reservation updates observation but leaves all accounts and attempt ledgers unchanged", () => {
    const profile = makeFulfillmentProfile();
    const context = createFulfillmentInputContextForTest();
    const snapshot = createSnapshot(profile, "hard");
    const entered = dispatch(profile, snapshot, context, "shared", {
      action: { type: "enter-phase", phase: "phase-1", nowSeconds: 0 },
    });
    const before = entered;
    const rejected = dispatch(profile, entered, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(recipeIds.mealDirect, recipeIds.shelterMaterials),
      expectedSpendable: entered.core.spendable,
    });
    expect(rejected.active).toBeNull();
    expect(rejected.attemptCounter).toBe(0);
    expect(rejected.escrow).toEqual(before.escrow);
    expect(rejected.core.spendable).toEqual(before.core.spendable);
    expect(rejected.core.liveSpatialObservation?.sequence).toBeGreaterThan(
      before.core.liveSpatialObservation?.sequence ?? -1,
    );
  });

  test("departure, work, generation, and delivery require causal observations and exact selected identities", () => {
    const { profile, state: initial, context } = enterFulfillment();
    const selected = selection();
    let state = dispatch(profile, initial, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selected,
      expectedSpendable: initial.core.spendable,
    });
    state = dispatch(profile, state, context, "commit", {
      attempt: 1,
      revision: 1,
    });
    const beforeWork = state;
    state = dispatch(profile, state, context, "depart-for-work", {
      attempt: 2,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
    });
    expect(state.active?.departures).toEqual(beforeWork.active?.departures);
    state = dispatch(profile, state, context, "record-work", {
      attempt: 1,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
      positions: { [fixtureIds.mealWorker]: zoneIds.mealDirectSource },
    });
    expect(state.active?.work).toEqual(beforeWork.active?.work);

    state = completeSelectedService(
      profile,
      state,
      context,
      fixtureIds.mealService,
      recipeIds.mealDirect,
      fixtureIds.mealWorker,
      zoneIds.mealDirectSource,
      zoneIds.mealReception,
      [fixtureIds.mealRecipient],
      outputIds.mealDirect,
      1,
    );
    expect(state.active?.generated).toContain(recipeIds.mealDirect);
    expect(state.active?.completedServices).toContain(fixtureIds.mealService);
    expect(state.active?.work[recipeIds.mealDirect]).toBeDefined();
    const generatedOnce = state.active?.generated;
    state = dispatch(profile, state, context, "generate-output", {
      attempt: 1,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
    });
    expect(state.active?.generated).toEqual(generatedOnce);
  });

  test("all selected outputs plus fresh original presence gate both objective latch and victory", () => {
    const { profile, state: initial, context } = enterFulfillment();
    let state = dispatch(profile, initial, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: initial.core.spendable,
    });
    state = dispatch(profile, state, context, "commit", {
      attempt: 1,
      revision: 1,
    });
    state = completeSelectedService(
      profile,
      state,
      context,
      fixtureIds.mealService,
      recipeIds.mealDirect,
      fixtureIds.mealWorker,
      zoneIds.mealDirectSource,
      zoneIds.mealReception,
      [fixtureIds.mealRecipient],
      outputIds.mealDirect,
      1,
    );
    state = completeSelectedService(
      profile,
      state,
      context,
      fixtureIds.shelterService,
      recipeIds.shelterMaterials,
      fixtureIds.shelterWorker,
      zoneIds.materialsSource,
      zoneIds.materialsCourt,
      [fixtureIds.householdA, fixtureIds.householdB],
      outputIds.shelterMaterials,
      1,
    );

    const positions = {
      [fixtureIds.mealWorker]: "store-1",
      [fixtureIds.mealRecipient]: zoneIds.mealReception,
      [fixtureIds.householdA]: zoneIds.materialsCourt,
      [fixtureIds.householdB]: zoneIds.materialsCourt,
      [outputIds.mealDirect]: zoneIds.mealReception,
      [outputIds.shelterMaterials]: zoneIds.materialsCourt,
    };
    const staleTerminal = dispatch(profile, state, context, "shared", {
      action: { type: "enter-phase", phase: "victory", nowSeconds: 0 },
    });
    expect(staleTerminal.core.phase).toBe("phase-1");
    state = dispatch(profile, state, context, "shared", {
      action: {
        type: "record-arrival",
        entityId: fixtureIds.mealRecipient,
        zoneId: zoneIds.mealReception,
      },
      positions,
    });
    state = dispatch(profile, state, context, "shared", {
      action: { type: "latch-objective", objectiveId: "return" },
      positions,
    });
    expect(state.core.objectiveLatches).toContain("return");
    const latched = state;
    state = dispatch(profile, latched, context, "shared", {
      action: { type: "enter-phase", phase: "victory", nowSeconds: 0 },
      positions,
    });
    expect(state.core.phase).toBe("victory");
    const tickVictory = dispatch(profile, latched, context, "shared", {
      action: {
        type: "tick",
        nowSeconds: 0,
        difficulty: "standard",
        defeatConditions: [],
        victoryConditions: ["return"],
      },
      positions,
    });
    expect(tickVictory.core.terminal).toBe("victory");
  });

  test("load rotates epoch; old queued input is rejected and unknown payload fields do not advance observation", () => {
    const { profile, state, context } = enterFulfillment();
    const loaded = loadFulfillmentSnapshot(profile, state);
    expect(loaded.inputContext.epoch).not.toBe(context.epoch);
    const oldCommand = fulfillmentCommand(profile, state, context, "observe");
    const stale = reduce(
      profile,
      loaded.snapshot,
      oldCommand,
      loaded.inputContext,
    );
    expect(stale).toEqual(loaded.snapshot);

    const malformed = {
      ...fulfillmentCommand(
        profile,
        loaded.snapshot,
        loaded.inputContext,
        "observe",
      ),
      unrecognized: true,
    };
    const rejected = reduce(
      profile,
      loaded.snapshot,
      malformed,
      loaded.inputContext,
    );
    expect(rejected).toEqual(loaded.snapshot);
  });

  test("v3 compilation is opt-in and leaves the projected v2 core byte-equivalent", () => {
    const profile = makeFulfillmentProfile();
    const compiledV3 = compileCapabilityProfile(profile);
    if (compiledV3.schemaVersion !== 3)
      throw new Error("Expected opt-in v3 compiler output");
    const {
      schemaVersion: _version,
      fulfillmentPlan,
      ...projected
    } = compiledV3;
    expect(fulfillmentPlan).toEqual(profile.fulfillmentPlan);
    expect({ schemaVersion: 2, ...projected }).toEqual(
      compileCapabilityProfile(sharedCapabilityProfile(profile)),
    );
    const v3 = createFulfillmentSnapshot(profile, accounts("standard"));
    expect(v3.core.contractFingerprint).toBe(
      capabilityFingerprint(sharedCapabilityProfile(profile)),
    );
  });

  test("the untouched legacy v2 fixture retains its established fingerprint and serialization hashes", () => {
    const legacyProfile = makeProfile();
    const accounts = {
      spendable: { food: 10, wood: 20, gold: 30, stone: 40 },
      protectedRecovery: { food: 0, wood: 0, gold: 0, stone: 0 },
      optionalReserve: { food: 0, wood: 0, gold: 0, stone: 0 },
    };
    const snapshot = createCapabilitySnapshot(legacyProfile, accounts);
    const compiled = compileCapabilityProfile(legacyProfile);
    expect(capabilityFingerprint(legacyProfile)).toBe(
      "6ce58d83eb099c0324dce3a0e338773b390d1c49d7b47b2d5605276a769a5ac1",
    );
    expect(hash(canonical(snapshot))).toBe(
      "0b3281bdca1992db26f0a1c1f38be1ab8a4e1f32da38da025dad8c0a58aafbab",
    );
    expect(hash(canonical(compiled))).toBe(
      "bd53f051c74e7abf75dba31f6a7c30fff0bb9124906756cc7213161fb0e6b329",
    );
  });

  test("load rejects unknown phases, latches, secondary states, reward receipts, and inconsistent terminals", () => {
    const profile = makeFulfillmentProfile();
    const valid = createSnapshot(profile, "standard");
    const invalidSnapshots = [
      {
        ...valid,
        core: {
          ...valid.core,
          secondaryStates: {
            ...valid.core.secondaryStates,
            [required(profile.secondaryObjectives[0]).id]: "closed-at-terminal",
          },
        },
      },
      { ...valid, core: { ...valid.core, phase: "unknown-phase" } },
      {
        ...valid,
        core: { ...valid.core, objectiveLatches: ["unknown-objective"] },
      },
      {
        ...valid,
        core: {
          ...valid.core,
          secondaryStates: Object.fromEntries(
            Object.entries(valid.core.secondaryStates).slice(1),
          ),
        },
      },
      { ...valid, core: { ...valid.core, rewardFlags: ["unknown-reward"] } },
      {
        ...valid,
        core: { ...valid.core, phase: "briefing", terminal: "defeat" },
      },
    ];
    for (const invalid of invalidSnapshots)
      expect(() => loadFulfillmentSnapshot(profile, invalid)).toThrow();
  });

  test("load rejects an optional reward snapshot whose arrival, visit, or payment evidence was erased", () => {
    const profile = makeFulfillmentProfile();
    for (const optionalId of [
      "neighbor-provisions",
      "slope-survey",
      "damaged-civilian-store",
    ]) {
      const { state, context } = enterFulfillment(profile);
      const complete = completeOptional(profile, state, context, optionalId);
      const objectiveId = matrixOptionalIds[optionalId];
      const keyPrefix = `${objectiveId}.`;
      const corrupted = {
        ...complete,
        core: {
          ...complete.core,
          requirementFacts: Object.fromEntries(
            Object.entries(complete.core.requirementFacts).filter(
              ([key]) => !key.startsWith(keyPrefix),
            ),
          ),
          ...(optionalId === "neighbor-provisions"
            ? {
                arrivalLedger: [],
                arrivedEntities: {},
              }
            : {}),
          ...(optionalId === "slope-survey" ? { visitedZones: [] } : {}),
          ...(optionalId === "damaged-civilian-store"
            ? { paidReceipts: [] }
            : {}),
        },
      };
      expect(() => loadFulfillmentSnapshot(profile, corrupted)).toThrow();
    }
  });

  test("invalid raw destroy events do not throw or mutate shared ledgers", () => {
    const { profile, state, context } = enterFulfillment();
    const before = state.core.entityStates;
    const after = dispatch(profile, state, context, "shared", {
      action: { type: "destroy-entity", entityId: "unknown-actor" },
    });
    expect(after.core.entityStates).toEqual(before);
    expect(after.core.terminal).toBeNull();
  });

  test("v3 rejects ambiguous side-arrival fact layouts without changing v2 receipts", () => {
    const profile = makeFulfillmentProfile();
    const objective = profile.secondaryObjectives[0];
    const arrival = objective?.predicate.requirements[0];
    if (!objective || arrival?.kind !== "entity-arrival")
      throw new Error("Expected the fixture's leading arrival predicate");
    objective.predicate.requirements.push(structuredClone(arrival));
    expect(
      validateScenarioCapability(profile).some(
        (issue) =>
          issue.code === "fulfillment.contract" &&
          issue.message.includes(objective.id),
      ),
    ).toBe(true);
  });

  test("a defeated worker wins defeat priority before a reservation debit", () => {
    const { profile, state: initial, context } = enterFulfillment();
    const before = initial.core.spendable;
    const defeated = dispatch(profile, initial, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: before,
      dead: [fixtureIds.mealWorker],
    });
    expect(defeated.core.terminal).toBe("defeat");
    expect(defeated.core.spendable).toEqual(before);
    expect(defeated.attemptCounter).toBe(0);
  });

  test("all seven optional objectives complete through their distinct arrival, visit, health, and payment inputs", () => {
    const profile = makeFulfillmentProfile();
    for (const objective of profile.secondaryObjectives) {
      const { state: initial, context } = enterFulfillment(profile);
      let state = initial;
      for (const requirement of objective.predicate.requirements) {
        if (requirement.kind === "atomic-payment") {
          state = dispatch(profile, state, context, "shared", {
            action: {
              type: "pay-secondary",
              objectiveId: objective.id,
              receipt: requirement.receipt,
            },
          });
        } else if (requirement.kind === "entity-arrival") {
          for (const entityId of requirement.entities) {
            state = dispatch(profile, state, context, "shared", {
              action: {
                type: "record-arrival",
                entityId,
                zoneId: requirement.destinations[entityId],
              },
            });
          }
        } else if (requirement.kind === "visit-zones") {
          for (const zoneId of requirement.zones) {
            state = dispatch(profile, state, context, "shared", {
              action: { type: "visit-zone", zoneId },
            });
          }
        }
      }
      for (const [
        index,
        requirement,
      ] of objective.predicate.requirements.entries()) {
        if (requirement.kind === "entity-health") {
          state = dispatch(profile, state, context, "shared", {
            action: {
              type: "record-secondary-predicate",
              objectiveId: objective.id,
              requirementIndex: index,
              healthFraction: 1,
            },
          });
        }
      }
      state = dispatch(profile, state, context, "shared", {
        action: { type: "award-secondary", objectiveId: objective.id },
      });
      expect(state.core.secondaryStates[objective.id]).toBe("completed");
    }
  });

  test("clock defeat takes priority over invalid spatial batches and freezes escrow", () => {
    const profile = makeFulfillmentProfile();
    const invalidBatchKinds = [
      "unknown",
      "stale",
      "multi-zone",
      "unavailable-output",
    ] as const;
    for (const kind of invalidBatchKinds) {
      const { state: initial, context } = enterFulfillment(profile);
      const reserved = dispatch(profile, initial, context, "reserve", {
        attempt: 1,
        revision: 0,
        selection: selection(),
        expectedSpendable: initial.core.spendable,
      });
      const sequence = reserved.core.liveSpatialObservation?.sequence ?? 0;
      const batch = liveBatch(profile, reserved, sequence + 1);
      if (kind === "unknown")
        batch.entities.push({
          entityId: "unknown-actor",
          alive: true,
          zones: [],
        });
      if (kind === "stale") batch.sequence = sequence;
      if (kind === "multi-zone") {
        const entity = batch.entities.find(
          (item) => item.entityId === fixtureIds.mealWorker,
        );
        if (entity) entity.zones = ["store-1", "store-2"];
      }
      if (kind === "unavailable-output")
        batch.entities.push({
          entityId: outputIds.mealHearth,
          alive: true,
          zones: [],
        });
      const beforeSpendable = reserved.core.spendable;
      const beforeEscrow = reserved.escrow;
      const defeated = dispatch(profile, reserved, context, "shared", {
        action: {
          type: "tick",
          nowSeconds: 0,
          difficulty: "standard",
          defeatConditions: ["known-defeat"],
          victoryConditions: [],
        },
        liveSpatialBatch: batch,
      });
      expect(defeated.core.terminal).toBe("defeat");
      expect(defeated.core.spendable).toEqual(beforeSpendable);
      expect(defeated.escrow).toEqual(beforeEscrow);
    }
  });

  test("a phase deadline is evaluated even when the accompanying observation is invalid", () => {
    const profile = makeFulfillmentProfile();
    profile.objectivePlan[0]?.predicate.requirements.push({
      id: "fixture.deadline",
      kind: "phase-deadline",
      phase: "phase-1",
      clock: "relative-to-phase-entry",
      onExpiry: "defeat",
      warningSeconds: 1,
      secondsByDifficulty: { easy: 2, standard: 2, hard: 2 },
    });
    profile.objectivePlan[0]?.predicate.requiredLedgers.push(
      "fixture.deadline",
    );
    const { state: initial, context } = enterFulfillment(profile);
    const invalid = liveBatch(profile, initial, 1);
    invalid.entities.push({
      entityId: "unknown-deadline-actor",
      alive: true,
      zones: [],
    });
    const defeated = dispatch(profile, initial, context, "shared", {
      nowSeconds: 2,
      action: {
        type: "tick",
        nowSeconds: 2,
        difficulty: "standard",
        defeatConditions: [],
        victoryConditions: [],
      },
      liveSpatialBatch: invalid,
    });
    expect(defeated.core.terminal).toBe("defeat");
  });

  test("an active plan cannot leave its work phase before commit and service completion", () => {
    const profile = makeFulfillmentProfile();
    profile.stateMachine.states.push("phase-2");
    profile.stateMachine.transitions.push(
      "phase-1 → phase-2",
      "phase-2 → victory",
    );
    profile.stateMachine.phaseTransitions.push(
      { from: "phase-1", to: "phase-2", on: "intro-accepted" },
      {
        from: "phase-2",
        to: "victory",
        on: "objective-latched",
        objectiveId: "return",
      },
    );

    const first = enterFulfillment(profile);
    let reserved = dispatch(profile, first.state, first.context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: first.state.core.spendable,
    });
    const reservedExit = dispatch(profile, reserved, first.context, "shared", {
      action: { type: "enter-phase", phase: "phase-2", nowSeconds: 0 },
    });
    expect(reservedExit.core.phase).toBe("phase-1");
    expect(() =>
      loadFulfillmentSnapshot(profile, {
        ...reserved,
        core: { ...reserved.core, phase: "phase-2" },
      }),
    ).toThrow();
    reserved = dispatch(profile, reserved, first.context, "cancel", {
      attempt: 1,
      revision: 1,
    });
    const cancelledExit = dispatch(profile, reserved, first.context, "shared", {
      action: { type: "enter-phase", phase: "phase-2", nowSeconds: 0 },
    });
    expect(cancelledExit.core.phase).toBe("phase-1");

    const second = enterFulfillment(profile);
    let active = dispatch(profile, second.state, second.context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: second.state.core.spendable,
    });
    active = dispatch(profile, active, second.context, "commit", {
      attempt: 1,
      revision: 1,
    });
    const committedExit = dispatch(profile, active, second.context, "shared", {
      action: { type: "enter-phase", phase: "phase-2", nowSeconds: 0 },
    });
    expect(committedExit.core.phase).toBe("phase-1");
    active = completeSelectedService(
      profile,
      active,
      second.context,
      fixtureIds.mealService,
      recipeIds.mealDirect,
      fixtureIds.mealWorker,
      zoneIds.mealDirectSource,
      zoneIds.mealReception,
      [fixtureIds.mealRecipient],
      outputIds.mealDirect,
      1,
    );
    active = completeSelectedService(
      profile,
      active,
      second.context,
      fixtureIds.shelterService,
      recipeIds.shelterMaterials,
      fixtureIds.shelterWorker,
      zoneIds.materialsSource,
      zoneIds.materialsCourt,
      [fixtureIds.householdA, fixtureIds.householdB],
      outputIds.shelterMaterials,
      1,
    );
    const finalPositions = {
      [fixtureIds.mealWorker]: "store-1",
      [fixtureIds.mealRecipient]: zoneIds.mealReception,
      [fixtureIds.householdA]: zoneIds.materialsCourt,
      [fixtureIds.householdB]: zoneIds.materialsCourt,
      [outputIds.mealDirect]: zoneIds.mealReception,
      [outputIds.shelterMaterials]: zoneIds.materialsCourt,
    };
    active = dispatch(profile, active, second.context, "shared", {
      action: {
        type: "record-arrival",
        entityId: fixtureIds.mealRecipient,
        zoneId: zoneIds.mealReception,
      },
      positions: finalPositions,
    });
    active = dispatch(profile, active, second.context, "shared", {
      action: { type: "latch-objective", objectiveId: "return" },
      positions: finalPositions,
    });
    active = dispatch(profile, active, second.context, "shared", {
      action: { type: "enter-phase", phase: "phase-2", nowSeconds: 0 },
      positions: finalPositions,
    });
    expect(active.core.phase).toBe("phase-2");
    active = dispatch(profile, active, second.context, "shared", {
      action: { type: "enter-phase", phase: "victory", nowSeconds: 0 },
      positions: finalPositions,
    });
    expect(active.core.terminal).toBe("victory");
  });

  test("zero-cost services still require one reservation, commit, departure, work, and exact output", () => {
    const profile = makeFulfillmentProfile();
    for (const recipe of profile.fulfillmentPlan.services.flatMap(
      (item) => item.recipes,
    ))
      recipe.cost = { food: 0, wood: 0, gold: 0, stone: 0 };
    const { state: initial, context } = enterFulfillment(profile);
    let state = dispatch(profile, initial, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: initial.core.spendable,
    });
    expect(state.active?.status).toBe("reserved");
    expect(state.escrow).toEqual({ food: 0, wood: 0, gold: 0, stone: 0 });
    state = dispatch(profile, state, context, "commit", {
      attempt: 1,
      revision: 1,
    });
    const noWork = dispatch(profile, state, context, "generate-output", {
      attempt: 1,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
    });
    expect(noWork.active?.generated).toEqual([]);
    state = completeSelectedService(
      profile,
      state,
      context,
      fixtureIds.mealService,
      recipeIds.mealDirect,
      fixtureIds.mealWorker,
      zoneIds.mealDirectSource,
      zoneIds.mealReception,
      [fixtureIds.mealRecipient],
      outputIds.mealDirect,
      1,
    );
    const once = state.active?.generated;
    const repeated = dispatch(profile, state, context, "generate-output", {
      attempt: 1,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
    });
    expect(repeated.active?.generated).toEqual(once);
    const secondReservation = dispatch(profile, state, context, "reserve", {
      attempt: 2,
      revision: state.revision,
      selection: selection(),
      expectedSpendable: state.core.spendable,
    });
    expect(secondReservation.attemptCounter).toBe(1);
  });

  test("selection and recipe validation reject partial, duplicate, mixed, unknown, and unsafe plans atomically", () => {
    const profile = makeFulfillmentProfile();
    const malformedSelections = [
      [
        {
          serviceId: fixtureIds.mealService,
          recipeId: recipeIds.shelterMaterials,
        },
        {
          serviceId: fixtureIds.shelterService,
          recipeId: recipeIds.shelterMaterials,
        },
      ],
      [{ serviceId: fixtureIds.mealService, recipeId: recipeIds.mealDirect }],
      [
        { serviceId: fixtureIds.mealService, recipeId: recipeIds.mealDirect },
        { serviceId: fixtureIds.mealService, recipeId: recipeIds.mealHearth },
      ],
      [
        { serviceId: fixtureIds.mealService, recipeId: recipeIds.mealDirect },
        {
          serviceId: fixtureIds.shelterService,
          recipeId: recipeIds.shelterMaterials,
        },
        {
          serviceId: fixtureIds.shelterService,
          recipeId: recipeIds.shelterKit,
        },
      ],
      [
        { serviceId: fixtureIds.mealService, recipeId: "unknown.recipe" },
        {
          serviceId: fixtureIds.shelterService,
          recipeId: recipeIds.shelterMaterials,
        },
      ],
    ];
    for (const choice of malformedSelections) {
      const { state, context } = enterFulfillment(profile);
      const rejected = dispatch(profile, state, context, "reserve", {
        attempt: 1,
        revision: 0,
        selection: choice,
        expectedSpendable: state.core.spendable,
      });
      expect(rejected.active).toBeNull();
      expect(rejected.attemptCounter).toBe(0);
      expect(rejected.escrow).toEqual(state.escrow);
    }
    for (const cost of [
      { food: 1.5, wood: 0, gold: 0, stone: 0 },
      { food: Number.MAX_SAFE_INTEGER + 1, wood: 0, gold: 0, stone: 0 },
    ]) {
      const invalid = structuredClone(profile);
      const recipe = invalid.fulfillmentPlan.services[0]?.recipes[0];
      if (recipe) recipe.cost = cost;
      expect(capabilityProfileV3Schema.safeParse(invalid).success).toBe(false);
    }
    const overflowing = structuredClone(profile);
    const first = overflowing.fulfillmentPlan.services[0]?.recipes[0];
    const second = overflowing.fulfillmentPlan.services[1]?.recipes[0];
    if (first && second) {
      first.cost = {
        food: Number.MAX_SAFE_INTEGER,
        wood: 0,
        gold: 0,
        stone: 0,
      };
      second.cost = { food: 1, wood: 0, gold: 0, stone: 0 };
      expect(() =>
        createFulfillmentSnapshot(overflowing, accounts("standard")),
      ).toThrow();
    }
  });

  test("stale expected spendable, protected accounts, and rewards cannot silently finance a selection", () => {
    const profile = makeFulfillmentProfile();
    const { state: initial, context } = enterFulfillment(profile, "hard");
    const richer = completeOptional(
      profile,
      initial,
      context,
      "neighbor-provisions",
    );
    expect(richer.core.spendable.food).toBeGreaterThan(
      initial.core.spendable.food,
    );
    const stale = dispatch(profile, richer, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: initial.core.spendable,
    });
    expect(stale.active).toBeNull();
    expect(stale.attemptCounter).toBe(0);
    expect(stale.core.spendable).toEqual(richer.core.spendable);

    const protectedOnly = createFulfillmentSnapshot(profile, {
      spendable: { food: 0, wood: 0, gold: 0, stone: 0 },
      protectedRecovery: { food: 1000, wood: 1000, gold: 1000, stone: 1000 },
      optionalReserve: { food: 1000, wood: 1000, gold: 1000, stone: 1000 },
    });
    const entered = dispatch(profile, protectedOnly, context, "shared", {
      action: { type: "enter-phase", phase: "phase-1", nowSeconds: 0 },
    });
    const rejected = dispatch(profile, entered, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: entered.core.spendable,
    });
    expect(rejected.active).toBeNull();
    expect(rejected.core.spendable).toEqual({
      food: 0,
      wood: 0,
      gold: 0,
      stone: 0,
    });
    expect(rejected.core.protectedRecovery).toEqual(
      protectedOnly.core.protectedRecovery,
    );
    expect(rejected.core.optionalReserve).toEqual(
      protectedOnly.core.optionalReserve,
    );

    const repair = profile.secondaryObjectives.find(
      (item) => item.kind === "repair",
    );
    if (!repair) throw new Error("Missing repair optional");
    const repairRun = enterFulfillment(profile);
    const prematureAward = dispatch(
      profile,
      repairRun.state,
      repairRun.context,
      "shared",
      {
        action: { type: "award-secondary", objectiveId: repair.id },
      },
    );
    expect(prematureAward.core.secondaryStates[repair.id]).not.toBe(
      "completed",
    );
    expect(prematureAward.core.rewardFlags).not.toContain(
      `${repair.id}.rewarded`,
    );
  });

  test("optional award during reservation survives cancellation while only plan escrow is refunded", () => {
    const profile = makeFulfillmentProfile();
    const { state: initial, context } = enterFulfillment(profile);
    const reserved = dispatch(profile, initial, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: initial.core.spendable,
    });
    const rewarded = completeOptional(
      profile,
      reserved,
      context,
      "neighbor-provisions",
    );
    const duplicate = completeOptional(
      profile,
      rewarded,
      context,
      "neighbor-provisions",
    );
    expect(duplicate.core.spendable).toEqual(rewarded.core.spendable);
    expect(duplicate.core.optionalReserve).toEqual(
      rewarded.core.optionalReserve,
    );
    const cancelled = dispatch(profile, duplicate, context, "cancel", {
      attempt: 1,
      revision: duplicate.revision,
    });
    expect(cancelled.active).toBeNull();
    expect(cancelled.escrow).toEqual({ food: 0, wood: 0, gold: 0, stone: 0 });
    expect(cancelled.core.spendable.food).toBe(
      rewarded.core.spendable.food + reserved.escrow.food,
    );
    expect(cancelled.core.rewardFlags).toContain(
      "fulfillment-fixture.optional-1.rewarded",
    );
    const cancelledAgain = dispatch(profile, cancelled, context, "cancel", {
      attempt: 1,
      revision: cancelled.revision,
    });
    expect(cancelledAgain.core.spendable).toEqual(cancelled.core.spendable);
  });

  test("commit cannot be cancelled or changed, duplicate commit cannot spend twice, and unselected outputs are rejected", () => {
    const profile = makeFulfillmentProfile();
    const { state: initial, context } = enterFulfillment(profile);
    const reserved = dispatch(profile, initial, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: initial.core.spendable,
    });
    const committed = dispatch(profile, reserved, context, "commit", {
      attempt: 1,
      revision: 1,
    });
    const spend = committed.committedExpenditure;
    const duplicate = dispatch(profile, committed, context, "commit", {
      attempt: 1,
      revision: committed.revision,
    });
    expect(duplicate.committedExpenditure).toEqual(spend);
    expect(duplicate.revision).toBe(committed.revision);
    const cancelled = dispatch(profile, committed, context, "cancel", {
      attempt: 1,
      revision: committed.revision,
    });
    expect(cancelled.active?.status).toBe("committed");
    const changed = dispatch(profile, committed, context, "generate-output", {
      attempt: 1,
      revision: committed.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealHearth,
    });
    expect(changed.active?.generated).toEqual([]);
    const batch = liveBatch(
      profile,
      committed,
      (committed.core.liveSpatialObservation?.sequence ?? 0) + 1,
    );
    batch.entities.push({
      entityId: outputIds.mealHearth,
      alive: true,
      zones: [],
    });
    const rejected = dispatch(profile, committed, context, "observe", {
      liveSpatialBatch: batch,
    });
    expect(rejected).toEqual(committed);
  });

  test("schema and scenario validation enforce plan bounds, distinct workers, and acyclic generation inputs", () => {
    const base = makeFulfillmentProfile();
    for (const overlapById of [true, false]) {
      const overlapping = structuredClone(base);
      const meal = required(
        required(overlapping.fulfillmentPlan.services[0]).recipes[0],
      );
      const court = required(
        overlapping.worldContract.zones.find(
          (zone) => zone.id === zoneIds.materialsCourt,
        ),
      );
      if (overlapById) meal.workZoneId = court.id;
      else {
        const work = required(
          overlapping.worldContract.zones.find(
            (zone) => zone.id === meal.workZoneId,
          ),
        );
        work.hub = court.hub;
        work.offsetTiles = [...court.offsetTiles];
      }
      expect(
        validateScenarioCapability(overlapping).some(
          (item) => item.code === "fulfillment.contract",
        ),
      ).toBe(true);
    }
    const overServices = structuredClone(base);
    overServices.fulfillmentPlan.services = Array.from(
      { length: 9 },
      (_, i) => ({
        id: `service-${i}`,
        recipes: [
          {
            ...structuredClone(
              required(required(base.fulfillmentPlan.services[0]).recipes[0]),
            ),
            id: `recipe-${i}`,
            workerId: fixtureIds.mealWorker,
            outputEntityId: outputIds.mealDirect,
          },
        ],
      }),
    );
    expect(capabilityProfileV3Schema.safeParse(overServices).success).toBe(
      false,
    );
    const overRecipes = structuredClone(base);
    required(overRecipes.fulfillmentPlan.services[0]).recipes = Array.from(
      { length: 9 },
      (_, i) => ({
        ...structuredClone(
          required(required(base.fulfillmentPlan.services[0]).recipes[0]),
        ),
        id: `meal-recipe-${i}`,
      }),
    );
    expect(capabilityProfileV3Schema.safeParse(overRecipes).success).toBe(
      false,
    );

    const sharedWorker = structuredClone(base);
    required(
      required(sharedWorker.fulfillmentPlan.services[1]).recipes[0],
    ).workerId = fixtureIds.mealWorker;
    expect(
      validateScenarioCapability(sharedWorker).some(
        (item) => item.code === "fulfillment.contract",
      ),
    ).toBe(true);
    const cycle = structuredClone(base);
    required(required(cycle.fulfillmentPlan.services[0]).recipes[0]).workerId =
      outputIds.mealDirect;
    expect(
      validateScenarioCapability(cycle).some(
        (item) => item.code === "fulfillment.contract",
      ),
    ).toBe(true);
  });

  test("real optional payments need spendable stock and cannot be funded by their own reward or protected reserve", () => {
    const profile = makeFulfillmentProfile();
    const repair = profile.secondaryObjectives.find(
      (item) => item.kind === "repair",
    );
    if (!repair) throw new Error("Missing repair objective");
    const noSpend = createFulfillmentSnapshot(profile, {
      spendable: { food: 0, wood: 0, gold: 0, stone: 0 },
      protectedRecovery: { food: 0, wood: 100, gold: 0, stone: 0 },
      optionalReserve: { food: 0, wood: 100, gold: 0, stone: 0 },
    });
    const context = createFulfillmentInputContext();
    let state = dispatch(profile, noSpend, context, "shared", {
      action: { type: "enter-phase", phase: "phase-1", nowSeconds: 0 },
    });
    const paid = dispatch(profile, state, context, "shared", {
      action: {
        type: "pay-secondary",
        objectiveId: repair.id,
        receipt: `${repair.id}.payment`,
      },
    });
    expect(paid.core.paidReceipts).not.toContain(`${repair.id}.payment`);
    expect(paid.core.spendable.wood).toBe(0);
    expect(paid.core.protectedRecovery.wood).toBe(100);
    expect(paid.core.optionalReserve.wood).toBe(100);
    state = dispatch(profile, paid, context, "shared", {
      action: { type: "award-secondary", objectiveId: repair.id },
    });
    expect(state.core.secondaryStates[repair.id]).not.toBe("completed");
    expect(state.core.rewardFlags).not.toContain(`${repair.id}.rewarded`);
  });

  test("load preserves valid lifecycle checkpoints and rejects altered escrow or recipe contracts", () => {
    const profile = makeFulfillmentProfile();
    const { state: initial, context } = enterFulfillment(profile);
    const checkpoints = [initial];
    let state = dispatch(profile, initial, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: initial.core.spendable,
    });
    checkpoints.push(state);
    const cancelled = dispatch(profile, state, context, "cancel", {
      attempt: 1,
      revision: 1,
    });
    checkpoints.push(cancelled);
    state = dispatch(profile, cancelled, context, "reserve", {
      attempt: 2,
      revision: cancelled.revision,
      selection: selection(),
      expectedSpendable: cancelled.core.spendable,
    });
    state = dispatch(profile, state, context, "commit", {
      attempt: 2,
      revision: state.revision,
    });
    checkpoints.push(state);
    state = dispatch(profile, state, context, "depart-for-work", {
      attempt: 2,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
    });
    checkpoints.push(state);
    state = dispatch(profile, state, context, "record-work", {
      attempt: 2,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
      positions: { [fixtureIds.mealWorker]: zoneIds.mealDirectSource },
    });
    checkpoints.push(state);
    state = dispatch(profile, state, context, "generate-output", {
      attempt: 2,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
    });
    checkpoints.push(state);
    state = dispatch(profile, state, context, "complete-service", {
      attempt: 2,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
      positions: {
        [outputIds.mealDirect]: zoneIds.mealReception,
        [fixtureIds.mealRecipient]: zoneIds.mealReception,
      },
    });
    checkpoints.push(state);
    state = completeSelectedPlan(
      profile,
      state,
      context,
      selection(),
      2,
      "none",
    );
    checkpoints.push(state);
    checkpoints.push(
      completeSelectedPlan(profile, state, context, selection(), 2, "tick"),
    );
    checkpoints.push(
      dispatch(profile, required(checkpoints[1]), context, "observe", {
        dead: [fixtureIds.mealRecipient],
      }),
    );
    for (const checkpoint of checkpoints) {
      const loaded = loadFulfillmentSnapshot(profile, checkpoint);
      expect(loaded.snapshot).toEqual(checkpoint);
      expect(loaded.inputContext.epoch).not.toBe(context.epoch);
      const staleReplay = reduceFulfillmentState(
        profile,
        loaded.snapshot,
        fulfillmentCommand(profile, checkpoint, context, "observe"),
        loaded.inputContext,
      );
      expect(staleReplay).toEqual(loaded.snapshot);
      let resumed = loaded.snapshot;
      const newContext = loaded.inputContext;
      if (resumed.core.terminal) {
        expect(
          dispatch(profile, resumed, newContext, "cancel", {
            attempt: resumed.attemptCounter,
            revision: resumed.revision,
          }),
        ).toEqual(resumed);
        expect(
          dispatch(profile, resumed, newContext, "shared", {
            action: { type: "enter-phase", phase: "victory", nowSeconds: 0 },
          }),
        ).toEqual(resumed);
        continue;
      }
      if (!resumed.active) {
        resumed = dispatch(profile, resumed, newContext, "reserve", {
          attempt: resumed.attemptCounter + 1,
          revision: resumed.revision,
          selection: selection(),
          expectedSpendable: resumed.core.spendable,
        });
      }
      const active = required(resumed.active ?? undefined);
      const beforeReplay = resumed;
      resumed = dispatch(profile, resumed, newContext, "reserve", {
        attempt: resumed.attemptCounter + 1,
        revision: resumed.revision,
        selection: selection(),
        expectedSpendable: resumed.core.spendable,
      });
      expect(resumed.core.spendable).toEqual(beforeReplay.core.spendable);
      expect(resumed.escrow).toEqual(beforeReplay.escrow);
      expect(resumed.attemptCounter).toBe(beforeReplay.attemptCounter);
      resumed = dispatch(profile, resumed, newContext, "commit", {
        attempt: active.attempt,
        revision: resumed.revision,
      });
      const paid = resumed;
      resumed = dispatch(profile, resumed, newContext, "commit", {
        attempt: active.attempt,
        revision: resumed.revision,
      });
      expect(resumed.committedExpenditure).toEqual(paid.committedExpenditure);
      expect(resumed.core.spendable).toEqual(paid.core.spendable);
      expect(resumed.revision).toBe(paid.revision);
      resumed = completeSelectedPlan(
        profile,
        resumed,
        newContext,
        selection(),
        active.attempt,
        "none",
      );
      const completed = resumed;
      resumed = dispatch(profile, resumed, newContext, "generate-output", {
        attempt: active.attempt,
        revision: resumed.revision,
        serviceId: fixtureIds.mealService,
        recipeId: recipeIds.mealDirect,
        positions: finalPositionsFor(profile, selection()),
      });
      expect(resumed.active?.generated).toEqual(completed.active?.generated);
      expect(resumed.active?.generated.length).toBe(2);
      expect(resumed.committedExpenditure).toEqual(paid.committedExpenditure);
      resumed = completeSelectedPlan(
        profile,
        resumed,
        newContext,
        selection(),
        active.attempt,
        "tick",
      );
      expect(resumed.core.terminal).toBe("victory");
      expect(loadFulfillmentSnapshot(profile, resumed).snapshot).toEqual(
        resumed,
      );
    }
    for (const schemaVersion of [2, 4])
      expect(() =>
        loadFulfillmentSnapshot(profile, { ...initial, schemaVersion }),
      ).toThrow();
    const badShares = structuredClone(required(checkpoints[3]));
    if (!badShares.active) throw new Error("Missing committed checkpoint");
    badShares.active.committedShares = [];
    expect(() => loadFulfillmentSnapshot(profile, badShares)).toThrow();
    const badEscrow = {
      ...required(checkpoints[1]),
      escrow: { food: 0, wood: 0, gold: 0, stone: 0 },
    };
    expect(() => loadFulfillmentSnapshot(profile, badEscrow)).toThrow();
    const changedCost = structuredClone(profile);
    required(
      required(changedCost.fulfillmentPlan.services[0]).recipes[0],
    ).cost.food += 1;
    expect(() =>
      loadFulfillmentSnapshot(changedCost, checkpoints[1]),
    ).toThrow();
    const changedDestination = structuredClone(profile);
    required(
      required(changedDestination.fulfillmentPlan.services[0]).recipes[0],
    ).receptionZoneId = zoneIds.materialsCourt;
    expect(() =>
      loadFulfillmentSnapshot(changedDestination, checkpoints[1]),
    ).toThrow();
    const changedVersion = structuredClone(profile);
    changedVersion.schemaVersion = 2 as 3;
    expect(capabilityProfileV3Schema.safeParse(changedVersion).success).toBe(
      false,
    );
  });

  test("native renderer rejects the opt-in v3 profile before opening templates or writing artifacts", async () => {
    const campaign = {
      id: "test-campaign",
      scenarios: [{ capabilityProfile: makeFulfillmentProfile() }],
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

  test("fresh output or recipient death in the victory batch wins both terminal races", () => {
    const profile = makeFulfillmentProfile();
    for (const terminalApi of ["enter-phase", "tick"] as const) {
      for (const victim of [
        outputIds.mealDirect,
        outputIds.shelterMaterials,
        fixtureIds.mealRecipient,
        fixtureIds.householdB,
      ]) {
        const { state: initial, context } = enterFulfillment(profile);
        let state = dispatch(profile, initial, context, "reserve", {
          attempt: 1,
          revision: 0,
          selection: selection(),
          expectedSpendable: initial.core.spendable,
        });
        state = dispatch(profile, state, context, "commit", {
          attempt: 1,
          revision: state.revision,
        });
        state = completeSelectedPlan(
          profile,
          state,
          context,
          selection(),
          1,
          "none",
        );
        expect(state.core.terminal).toBeNull();
        expect(state.core.objectiveLatches).toContain("return");
        const defeated = dispatch(profile, state, context, "shared", {
          action:
            terminalApi === "enter-phase"
              ? { type: "enter-phase", phase: "victory", nowSeconds: 0 }
              : {
                  type: "tick",
                  nowSeconds: 0,
                  difficulty: "standard",
                  defeatConditions: [],
                  victoryConditions: ["return"],
                },
          positions: finalPositionsFor(profile, selection()),
          dead: [victim],
        });
        expect(defeated.core.terminal).toBe("defeat");
        expect(defeated.committedExpenditure).toEqual(
          state.committedExpenditure,
        );
        expect(defeated.core.spendable).toEqual(state.core.spendable);
        expect(defeated.active?.generated).toEqual(state.active?.generated);
        const loaded = loadFulfillmentSnapshot(profile, defeated);
        expect(
          dispatch(profile, loaded.snapshot, loaded.inputContext, "shared", {
            action: { type: "enter-phase", phase: "victory", nowSeconds: 0 },
            positions: finalPositionsFor(profile, selection()),
          }),
        ).toEqual(defeated);
      }
    }
  });

  test("losing a worker after recorded work preserves its output and allows the actual recipients to win", () => {
    const profile = makeFulfillmentProfile();
    const { state: initial, context } = enterFulfillment(profile);
    let state = dispatch(profile, initial, context, "reserve", {
      attempt: 1,
      revision: 0,
      selection: selection(),
      expectedSpendable: initial.core.spendable,
    });
    state = dispatch(profile, state, context, "commit", {
      attempt: 1,
      revision: state.revision,
    });
    state = dispatch(profile, state, context, "depart-for-work", {
      attempt: 1,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
    });
    state = dispatch(profile, state, context, "record-work", {
      attempt: 1,
      revision: state.revision,
      serviceId: fixtureIds.mealService,
      recipeId: recipeIds.mealDirect,
      positions: { [fixtureIds.mealWorker]: zoneIds.mealDirectSource },
    });
    state = dispatch(profile, state, context, "observe", {
      dead: [fixtureIds.mealWorker],
    });
    expect(state.core.terminal).toBeNull();
    state = completeSelectedPlan(
      profile,
      state,
      context,
      selection(),
      1,
      "tick",
    );
    expect(state.core.entityStates[fixtureIds.mealWorker]).toBe("destroyed");
    expect(state.core.terminal).toBe("victory");
    expect(loadFulfillmentSnapshot(profile, state).snapshot).toEqual(state);
  });

  test("generated output or recipient loss defeats before either victory API, while optional-only loss gives no reward", () => {
    const profile = makeFulfillmentProfile();
    for (const victim of [outputIds.mealDirect, fixtureIds.mealRecipient]) {
      for (const terminalApi of ["enter-phase", "tick"] as const) {
        const { state: initial, context } = enterFulfillment(profile);
        let state = dispatch(profile, initial, context, "reserve", {
          attempt: 1,
          revision: 0,
          selection: selection(),
          expectedSpendable: initial.core.spendable,
        });
        state = dispatch(profile, state, context, "commit", {
          attempt: 1,
          revision: state.revision,
        });
        state = completeSelectedService(
          profile,
          state,
          context,
          fixtureIds.mealService,
          recipeIds.mealDirect,
          fixtureIds.mealWorker,
          zoneIds.mealDirectSource,
          zoneIds.mealReception,
          [fixtureIds.mealRecipient],
          outputIds.mealDirect,
          1,
        );
        const lost = dispatch(profile, state, context, "observe", {
          dead: [victim],
        });
        expect(lost.core.terminal).toBe("defeat");
        const terminal = dispatch(profile, lost, context, "shared", {
          action:
            terminalApi === "enter-phase"
              ? { type: "enter-phase", phase: "victory", nowSeconds: 0 }
              : {
                  type: "tick",
                  nowSeconds: 0,
                  difficulty: "standard",
                  defeatConditions: [],
                  victoryConditions: ["return"],
                },
        });
        expect(terminal.core.terminal).toBe("defeat");
      }
    }
    const optional = profile.secondaryObjectives[0];
    if (!optional) throw new Error("Missing optional fixture");
    const { state, context } = enterFulfillment(profile);
    const optionalLoss = dispatch(profile, state, context, "observe", {
      dead: optional.world.entities.map((item) => item.id),
    });
    expect(optionalLoss.core.secondaryStates[optional.id]).toBe(
      "failed-optional",
    );
    expect(optionalLoss.core.rewardFlags).not.toContain(
      `${optional.id}.rewarded`,
    );
    expect(optionalLoss.core.terminal).toBeNull();
    const failedAward = dispatch(profile, optionalLoss, context, "shared", {
      action: { type: "award-secondary", objectiveId: optional.id },
    });
    expect(failedAward.core.secondaryStates[optional.id]).toBe(
      "failed-optional",
    );
    expect(failedAward.core.rewardFlags).not.toContain(
      `${optional.id}.rewarded`,
    );
    expect(failedAward.core.terminal).toBeNull();
  });

  test("each shelter alternative requires its own reception court for delivery and victory", () => {
    const profile = makeFulfillmentProfile();
    for (const [recipeId, ownCourt] of [
      [recipeIds.shelterKit, zoneIds.kitCourt],
      [recipeIds.shelterRented, zoneIds.hostCourt],
    ] as const) {
      const { state: initial, context } = enterFulfillment(profile);
      let state = dispatch(profile, initial, context, "reserve", {
        attempt: 1,
        revision: 0,
        selection: selection(recipeIds.mealDirect, recipeId),
        expectedSpendable: initial.core.spendable,
      });
      state = dispatch(profile, state, context, "commit", {
        attempt: 1,
        revision: state.revision,
      });
      const service = required(
        profile.fulfillmentPlan.services.find(
          (item) => item.id === fixtureIds.shelterService,
        ),
      );
      const recipe = required(
        service.recipes.find((item) => item.id === recipeId),
      );
      state = dispatch(profile, state, context, "depart-for-work", {
        attempt: 1,
        revision: state.revision,
        serviceId: service.id,
        recipeId,
      });
      state = dispatch(profile, state, context, "record-work", {
        attempt: 1,
        revision: state.revision,
        serviceId: service.id,
        recipeId,
        positions: { [recipe.workerId]: recipe.workZoneId },
      });
      state = dispatch(profile, state, context, "generate-output", {
        attempt: 1,
        revision: state.revision,
        serviceId: service.id,
        recipeId,
      });
      const wrong = dispatch(profile, state, context, "complete-service", {
        attempt: 1,
        revision: state.revision,
        serviceId: service.id,
        recipeId,
        positions: {
          [recipe.outputEntityId]: zoneIds.materialsCourt,
          [fixtureIds.householdA]: zoneIds.materialsCourt,
          [fixtureIds.householdB]: zoneIds.materialsCourt,
        },
      });
      expect(wrong.active?.completedServices).not.toContain(service.id);
      const right = dispatch(profile, state, context, "complete-service", {
        attempt: 1,
        revision: state.revision,
        serviceId: service.id,
        recipeId,
        positions: {
          [recipe.outputEntityId]: ownCourt,
          [fixtureIds.householdA]: ownCourt,
          [fixtureIds.householdB]: ownCourt,
        },
      });
      expect(right.active?.completedServices).toContain(service.id);
    }
  });
});

function createSnapshot(
  profile: ReturnType<typeof makeFulfillmentProfile>,
  difficulty: "easy" | "standard" | "hard",
) {
  return createFulfillmentSnapshot(profile, accounts(difficulty), difficulty);
}
function createFulfillmentInputContextForTest() {
  return createFulfillmentInputContext();
}
function reduce(
  profile: ReturnType<typeof makeFulfillmentProfile>,
  state: ReturnType<typeof enterFulfillment>["state"],
  action: unknown,
  context: ReturnType<typeof enterFulfillment>["context"],
) {
  return reduceFulfillmentState(profile, state, action, context);
}
