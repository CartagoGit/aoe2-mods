import { describe, expect, test } from "bun:test";
import { capabilityFingerprint } from "../../../packages/gameplay-state/capability-snapshot.factory";
import {
  createFulfillmentSnapshot,
  fulfillmentFingerprint,
  fulfillmentPresent,
  validateFulfillmentSnapshot,
} from "../../../packages/gameplay-state/fulfillment-snapshot.factory";
import type { FulfillmentSnapshot } from "../../../packages/gameplay-state/fulfillment-snapshot.schema";
import { sharedCapabilityProfile } from "../../../packages/schemas/alternative-fulfillment.schema";
import {
  accountsFor,
  fixtureIds,
  makeFulfillmentProfile,
  outputIds,
  recipeIds,
  selection,
  zoneIds,
} from "./alternative-fulfillment.fixture";

function committedPresenceFixture() {
  const profile = makeFulfillmentProfile();
  const initial = createFulfillmentSnapshot(profile, accountsFor("standard"));
  const state: FulfillmentSnapshot = {
    ...initial,
    active: {
      attempt: 1,
      selection: selection(),
      status: "committed",
      committedAtSequence: 0,
      committedShares: [],
      departures: {},
      work: {},
      generated: [recipeIds.mealDirect, recipeIds.shelterMaterials],
      completedServices: [fixtureIds.mealService, fixtureIds.shelterService],
    },
    core: {
      ...initial.core,
      liveSpatialObservation: {
        sequence: 1,
        entities: {
          [outputIds.mealDirect]: {
            alive: true,
            zones: [zoneIds.mealReception],
          },
          [fixtureIds.mealRecipient]: {
            alive: true,
            zones: [zoneIds.mealReception],
          },
          [outputIds.shelterMaterials]: {
            alive: true,
            zones: [zoneIds.materialsCourt],
          },
          [fixtureIds.householdA]: {
            alive: true,
            zones: [zoneIds.materialsCourt],
          },
          [fixtureIds.householdB]: {
            alive: true,
            zones: [zoneIds.materialsCourt],
          },
        },
      },
    },
  };
  return { profile, initial, state };
}

describe("fulfillment projection reuse", () => {
  test("validates a fresh projection after mutation of the same profile object", () => {
    const profile = makeFulfillmentProfile();
    const state = createFulfillmentSnapshot(profile, accountsFor("standard"));

    expect(fulfillmentFingerprint(profile)).toBe(
      "5edf2cca5e5ab4f33e03022ccade53c6cec5a943b8378b4bf248bb70de12d986",
    );
    expect(capabilityFingerprint(sharedCapabilityProfile(profile))).toBe(
      "b7b5e6f3fb4f4a55c6f5138cf3b1d6987644ca7c1b158b0943b40a7a3b67d975",
    );
    expect(validateFulfillmentSnapshot(profile, state)).toEqual(state);

    const firstRecipe = profile.fulfillmentPlan.services[0]?.recipes[0];
    if (!firstRecipe) throw new Error("Missing fixture recipe");
    firstRecipe.cost.food += 1;

    expect(() => validateFulfillmentSnapshot(profile, state)).toThrow(
      "fulfillment.snapshot-invalid: contract mismatch",
    );
  });

  test("requires current output and recipient presence without mutating inputs", () => {
    const { profile, state } = committedPresenceFixture();
    const beforeProfile = structuredClone(profile);
    const beforeState = structuredClone(state);

    expect(fulfillmentPresent(profile, state)).toBe(true);

    const missingOutput = structuredClone(state);
    if (!missingOutput.core.liveSpatialObservation)
      throw new Error("Fixture requires live spatial observations");
    delete missingOutput.core.liveSpatialObservation.entities[
      outputIds.mealDirect
    ];
    expect(fulfillmentPresent(profile, missingOutput)).toBe(false);

    const missingRecipient = structuredClone(state);
    if (!missingRecipient.core.liveSpatialObservation)
      throw new Error("Fixture requires live spatial observations");
    delete missingRecipient.core.liveSpatialObservation.entities[
      fixtureIds.householdA
    ];
    expect(fulfillmentPresent(profile, missingRecipient)).toBe(false);

    expect(profile).toEqual(beforeProfile);
    expect(state).toEqual(beforeState);

    const mutableProfile = profile as unknown as { objectivePlan: unknown };
    mutableProfile.objectivePlan = undefined;
    expect(() => fulfillmentPresent(profile, state)).toThrow();
  });

  test("keeps projection lazy until a selected generated entity is checked", () => {
    const { profile, initial, state } = committedPresenceFixture();
    const malformedProfile = {
      ...profile,
      objectivePlan: undefined,
    } as unknown as typeof profile;
    const inactive = initial;
    expect(fulfillmentPresent(malformedProfile, inactive)).toBe(false);

    const invalidSelection = structuredClone(state);
    if (!invalidSelection.active) throw new Error("Missing active selection");
    invalidSelection.active.selection = selection("unknown.recipe");
    expect(fulfillmentPresent(malformedProfile, invalidSelection)).toBe(false);

    const missingGenerated = structuredClone(state);
    if (!missingGenerated.active) throw new Error("Missing active selection");
    missingGenerated.active.generated = [];
    expect(fulfillmentPresent(malformedProfile, missingGenerated)).toBe(false);

    const destroyedOutput = structuredClone(state);
    destroyedOutput.core.entityStates[outputIds.mealDirect] = "destroyed";
    expect(fulfillmentPresent(malformedProfile, destroyedOutput)).toBe(false);

    expect(() => fulfillmentPresent(malformedProfile, state)).toThrow();
  });
});
