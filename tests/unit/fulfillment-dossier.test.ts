import { describe, expect, test } from "bun:test";
import { capabilityProfileV3Schema } from "../../packages/schemas/alternative-fulfillment.schema";
import { projectFulfillmentDossiers } from "../../tools/design/fulfillment-dossier.mapper";
import {
  accountsFor,
  fixtureIds,
  makeFulfillmentProfile,
  recipeIds,
} from "../alternative-fulfillment/reference/alternative-fulfillment.fixture";

function at<T>(items: T[], index: number): T {
  const item = items[index];
  if (item === undefined) throw new Error(`missing fixture item at ${index}`);
  return item;
}

function found<T>(item: T | undefined): T {
  if (item === undefined) throw new Error("missing fixture item");
  return item;
}

function requestFor(profile = makeFulfillmentProfile()) {
  const hubs = profile.districts.map((id, index) => ({
    id,
    centre: [50 + index * 100, 50] as [number, number],
  }));
  const hubById = new Map(hubs.map((hub) => [hub.id, hub]));
  const points = profile.worldContract.zones.map((zone, index) => {
    const hub = hubById.get(zone.hub);
    if (!hub) throw new Error(`missing fixture hub ${zone.hub}`);
    const tile: [number, number] = [
      hub.centre[0] + zone.offsetTiles[0],
      hub.centre[1] + zone.offsetTiles[1],
    ];
    return {
      pointId: `map-point.${zone.id}.${index}`,
      tile,
      zoneId: zone.id,
      hubId: zone.hub,
      offsetTiles: zone.offsetTiles,
    };
  });
  const pointByZone = new Map(points.map((point) => [point.zoneId, point]));
  const screens: Array<Record<string, unknown>> = [];
  const addScreen = (id: string) => {
    screens.push({
      id,
      key: `scenario.fixture.${id}`,
      text: { en: `Authored ${id}`, "es-ES": `Texto ${id}` },
      condition: "authored condition",
      narrator: "collection-narrator",
      skippable: true,
      captionPolicy: "split without loss",
      captionSegments: { en: [`Authored ${id}`], "es-ES": [`Texto ${id}`] },
      nativeSurface: "pending",
      voiceDurationSecondsEstimated: 2,
    });
  };
  for (const id of [
    "plan.preview",
    "plan.reserved",
    "plan.cancelled",
    "plan.started",
    "plan.complete",
  ])
    addScreen(id);
  const serviceBindings = profile.fulfillmentPlan.services.map((service) => {
    const goalScreenId = `service.${service.id}.goal`;
    const completeScreenId = `service.${service.id}.complete`;
    addScreen(goalScreenId);
    addScreen(completeScreenId);
    return { serviceId: service.id, goalScreenId, completeScreenId };
  });
  const recipeBindings = profile.fulfillmentPlan.services.flatMap((service) =>
    service.recipes.map((recipe) => {
      const goalScreenId = `recipe.${recipe.id}.goal`;
      addScreen(goalScreenId);
      const workPoint = pointByZone.get(recipe.workZoneId);
      const receptionPoint = pointByZone.get(recipe.receptionZoneId);
      if (!workPoint || !receptionPoint)
        throw new Error(`missing zone binding for ${recipe.id}`);
      return {
        serviceId: service.id,
        recipeId: recipe.id,
        workPointId: workPoint.pointId,
        receptionPointId: receptionPoint.pointId,
        title: { en: `Recipe ${recipe.id}`, "es-ES": `Receta ${recipe.id}` },
        goalScreenId,
      };
    }),
  );
  return {
    episodeId: "fixture.episode",
    referenceCapabilityProfile: profile,
    accountsByDifficulty: {
      easy: accountsFor("easy"),
      standard: accountsFor("standard"),
      hard: accountsFor("hard"),
    },
    mapSize: 400,
    hubs,
    pointZoneBindings: points,
    recipeBindings,
    serviceBindings,
    planScreenIds: {
      preview: "plan.preview",
      reserved: "plan.reserved",
      cancelled: "plan.cancelled",
      started: "plan.started",
      complete: "plan.complete",
    },
    screens,
  };
}

describe("typed fulfillment dossier projection", () => {
  test("keeps dotted authored IDs and exact alternatives with an artificial three-service profile", () => {
    const profile = makeFulfillmentProfile();
    const baseEntity = profile.worldContract.entities[0];
    const baseZone = profile.worldContract.zones[0];
    if (!baseEntity || !baseZone) throw new Error("missing fixture records");
    const extended = capabilityProfileV3Schema.parse({
      ...profile,
      worldContract: {
        ...profile.worldContract,
        entities: [
          ...profile.worldContract.entities,
          { ...baseEntity, id: "fixture.third-worker" },
          { ...baseEntity, id: "fixture.third-output" },
        ],
        zones: [
          ...profile.worldContract.zones,
          { ...baseZone, id: "fixture.third-work", offsetTiles: [270, 0] },
          { ...baseZone, id: "fixture.third-reception", offsetTiles: [290, 0] },
        ],
      },
      fulfillmentPlan: {
        ...profile.fulfillmentPlan,
        services: [
          ...profile.fulfillmentPlan.services,
          {
            id: "fixture.third-service",
            recipes: [
              {
                id: "fixture.third-recipe",
                cost: { food: 17, wood: 3, gold: 0, stone: 0 },
                workerId: "fixture.third-worker",
                workZoneId: "fixture.third-work",
                outputEntityId: "fixture.third-output",
                receptionZoneId: "fixture.third-reception",
                recipientIds: [fixtureIds.mealRecipient],
              },
            ],
          },
        ],
      },
    });
    const request = requestFor(extended);
    const projection = projectFulfillmentDossiers({ requests: [request] })
      .projections[0];
    expect(projection?.fulfillmentServices).toHaveLength(3);
    expect(projection?.referenceCapabilityProfile.fulfillmentPlan).toEqual(
      extended.fulfillmentPlan,
    );
    expect(
      projection?.fulfillmentServices
        .flatMap((service) => service.recipes)
        .some((recipe) => recipe.recipeId === recipeIds.mealDirect),
    ).toBe(true);
    expect(projection?.selectionAnalysisByDifficulty.hard).toBeDefined();
    expect(projection?.worldContract).toEqual(extended.worldContract);
    expect(projection?.objectivePlan).toEqual(extended.objectivePlan);
    expect(projection?.stateMachine).toEqual(extended.stateMachine);
    expect(projection?.secondaryObjectives).toEqual(
      extended.secondaryObjectives,
    );
    expect(projection?.secondaryBudget).toEqual(extended.secondaryBudget);
    expect(
      (
        projection?.optionalFinancialInputs as {
          optionalTasks: Array<{ id: string }>;
        }
      ).optionalTasks.map((item) => item.id),
    ).toEqual(extended.secondaryObjectives.map((item) => item.id));
  });

  test("rejects unknown fields, binding drift, reserve duplication, and unaffordable all-skip", () => {
    const base = requestFor();
    expect(() =>
      projectFulfillmentDossiers({ requests: [{ ...base, invented: true }] }),
    ).toThrow(/Unrecognized key/);
    const moved = structuredClone(base);
    at(moved.pointZoneBindings, 0).tile[0] += 1;
    expect(() => projectFulfillmentDossiers({ requests: [moved] })).toThrow(
      /authored tile disagrees/,
    );
    const reserve = structuredClone(base);
    reserve.accountsByDifficulty.standard.optionalReserve.food += 1;
    expect(() => projectFulfillmentDossiers({ requests: [reserve] })).toThrow(
      /does not equal secondaryBudget/,
    );
    const poor = structuredClone(base);
    poor.accountsByDifficulty.hard.spendable = {
      food: 0,
      wood: 0,
      gold: 0,
      stone: 0,
    };
    expect(() => projectFulfillmentDossiers({ requests: [poor] })).toThrow(
      /no affordable all-skip/,
    );
  });

  test("preserves the schema failure for an unknown or malformed opt-in profile", () => {
    const input = requestFor();
    (
      input as { referenceCapabilityProfile: unknown }
    ).referenceCapabilityProfile = { schemaVersion: 99 };
    expect(() => projectFulfillmentDossiers({ requests: [input] })).toThrow(
      /invalid schemaVersion 3/,
    );
  });

  test("rejects reserved prototype IDs, duplicate point bindings, and cross-hub zone bindings", () => {
    const reserved = requestFor();
    at(reserved.screens, 0).id = "__proto__";
    expect(() => projectFulfillmentDossiers({ requests: [reserved] })).toThrow(
      /Reserved JavaScript object key/,
    );

    const duplicate = requestFor();
    at(duplicate.pointZoneBindings, 1).pointId = at(
      duplicate.pointZoneBindings,
      0,
    ).pointId;
    expect(() => projectFulfillmentDossiers({ requests: [duplicate] })).toThrow(
      /duplicate pointId/,
    );

    const crossHub = requestFor();
    at(crossHub.pointZoneBindings, 0).hubId = "not-the-zone-hub";
    expect(() => projectFulfillmentDossiers({ requests: [crossHub] })).toThrow(
      /hub does not match zone/,
    );
  });

  test("rejects overlapping work and reception footprints even for distinct zones in one hub", () => {
    const profile = makeFulfillmentProfile();
    const recipe = at(at(profile.fulfillmentPlan.services, 0).recipes, 0);
    const workZoneId = recipe.workZoneId;
    const receptionZoneId = recipe.receptionZoneId;
    const workZone = found(
      profile.worldContract.zones.find((zone) => zone.id === workZoneId),
    );
    const receptionZone = found(
      profile.worldContract.zones.find((zone) => zone.id === receptionZoneId),
    );
    receptionZone.offsetTiles = [...workZone.offsetTiles];
    receptionZone.radiusTiles = workZone.radiusTiles;
    const request = requestFor(profile);
    expect(
      request.pointZoneBindings.find((point) => point.zoneId === workZoneId)
        ?.hubId,
    ).toBe(
      request.pointZoneBindings.find(
        (point) => point.zoneId === receptionZoneId,
      )?.hubId,
    );
    expect(() => projectFulfillmentDossiers({ requests: [request] })).toThrow(
      /Work and reception footprints overlap/,
    );
  });

  test("rejects resource overflow, negative authored costs, and duplicate optional IDs", () => {
    const overflow = requestFor();
    const profile = overflow.referenceCapabilityProfile as ReturnType<
      typeof makeFulfillmentProfile
    >;
    at(at(profile.fulfillmentPlan.services, 0).recipes, 0).cost.food =
      Number.MAX_SAFE_INTEGER;
    at(at(profile.fulfillmentPlan.services, 1).recipes, 0).cost.food =
      Number.MAX_SAFE_INTEGER;
    expect(() => projectFulfillmentDossiers({ requests: [overflow] })).toThrow(
      /overflow food/,
    );

    const negative = requestFor();
    const negativeProfile = negative.referenceCapabilityProfile as ReturnType<
      typeof makeFulfillmentProfile
    >;
    at(at(negativeProfile.fulfillmentPlan.services, 0).recipes, 0).cost.food =
      -1;
    expect(() => projectFulfillmentDossiers({ requests: [negative] })).toThrow(
      /Too small/,
    );

    const duplicateOptional = requestFor();
    const optionals = (
      duplicateOptional.referenceCapabilityProfile as ReturnType<
        typeof makeFulfillmentProfile
      >
    ).secondaryObjectives;
    at(optionals, 1).id = at(optionals, 0).id;
    expect(() =>
      projectFulfillmentDossiers({ requests: [duplicateOptional] }),
    ).toThrow(/repetido/);

    const unauthorizedIncome = requestFor();
    const incomeProfile =
      unauthorizedIncome.referenceCapabilityProfile as ReturnType<
        typeof makeFulfillmentProfile
      >;
    at(incomeProfile.objectivePlan, 0).predicate.resourceAmounts.food = 1;
    expect(() =>
      projectFulfillmentDossiers({ requests: [unauthorizedIncome] }),
    ).toThrow(/resourceAmounts/);
  });

  test("keeps batch IDs unique and rejects a service binding that is not a profile service", () => {
    const duplicateBatch = requestFor();
    expect(() =>
      projectFulfillmentDossiers({
        requests: [duplicateBatch, structuredClone(duplicateBatch)],
      }),
    ).toThrow(/duplicate episodeId/);

    const invalidService = requestFor();
    at(invalidService.recipeBindings, 0).serviceId = "unowned.service";
    expect(() =>
      projectFulfillmentDossiers({ requests: [invalidService] }),
    ).toThrow(/missing or cross-service recipe binding/);
  });

  test("derives optional financial vectors from authored profile values, not presets", () => {
    const profile = makeFulfillmentProfile();
    const side = profile.secondaryObjectives.find((item) =>
      item.effects.some((effect) => effect.kind === "finite-supply-withdrawal"),
    );
    if (!side) throw new Error("fixture needs an optional finite withdrawal");
    const withdrawal = side.effects.find(
      (effect) => effect.kind === "finite-supply-withdrawal",
    );
    if (!withdrawal || withdrawal.kind !== "finite-supply-withdrawal")
      throw new Error("missing fixture withdrawal");
    withdrawal.resources.food = (withdrawal.resources.food ?? 0) + 1;
    profile.secondaryBudget.reservedRewards.food =
      (profile.secondaryBudget.reservedRewards.food ?? 0) + 1;
    profile.secondaryBudget.reallocatedCacheAllowance.food =
      (profile.secondaryBudget.reallocatedCacheAllowance.food ?? 0) + 1;
    const request = requestFor(profile);
    for (const account of Object.values(request.accountsByDifficulty))
      account.optionalReserve.food += 1;

    const projection = projectFulfillmentDossiers({ requests: [request] })
      .projections[0];
    const rows = (
      projection?.optionalFinancialInputs as {
        optionalTasks: Array<{ id: string; cost: unknown; reward: unknown }>;
      }
    ).optionalTasks;
    const financial = rows.find((row) => row.id === side.id);
    expect(financial?.reward).toEqual(withdrawal.resources);
    const payment = side.predicate.requirements.find(
      (requirement) => requirement.kind === "atomic-payment",
    );
    expect(financial?.cost).toEqual(
      payment?.kind === "atomic-payment"
        ? payment.resources
        : { food: 0, wood: 0, gold: 0, stone: 0 },
    );
  });

  test("runs the JSON bridge and Python finite-allocation wrapper once for the batch", async () => {
    const request = requestFor();
    const helper = new URL(
      "../../tools/design/fulfillment-dossier.helper.py",
      import.meta.url,
    ).pathname;
    const process = Bun.spawn(["python3", helper], {
      cwd: new URL("../..", import.meta.url).pathname,
      stdin: "pipe",
      stdout: "pipe",
      stderr: "pipe",
    });
    process.stdin.write(JSON.stringify({ requests: [request] }));
    process.stdin.end();
    const [exitCode, stdout] = await Promise.all([
      process.exited,
      new Response(process.stdout).text(),
    ]);
    expect(exitCode).toBe(0);
    const response = JSON.parse(stdout) as {
      projections: Array<{
        episodeId: string;
        optionalPrefixAnalysisByDifficulty: Record<
          string,
          { reachableSubsetCount: number; protectedRecoveryExcluded: boolean }
        >;
      }>;
    };
    expect(response.projections).toHaveLength(1);
    expect(response.projections[0]?.episodeId).toBe("fixture.episode");
    expect(
      response.projections[0]?.optionalPrefixAnalysisByDifficulty.standard
        ?.reachableSubsetCount,
    ).toBeGreaterThan(0);
    expect(
      response.projections[0]?.optionalPrefixAnalysisByDifficulty.standard
        ?.protectedRecoveryExcluded,
    ).toBe(true);
  });
});
