import { describe, expect, test } from "bun:test";
import { unlinkSync, writeFileSync } from "node:fs";
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

function threeServiceProfile() {
  const profile = makeFulfillmentProfile();
  const baseEntity = profile.worldContract.entities[0];
  const baseZone = profile.worldContract.zones[0];
  if (!baseEntity || !baseZone) throw new Error("missing fixture records");
  return capabilityProfileV3Schema.parse({
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
}

describe("typed fulfillment dossier projection", () => {
  test("keeps dotted authored IDs and exact alternatives with an artificial three-service profile", () => {
    const extended = threeServiceProfile();
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

  test("rejects captions that lose text or exceed the 32-word display limit", () => {
    const lost = requestFor();
    const lostCaptions = at(lost.screens, 0).captionSegments as {
      en: string[];
      "es-ES": string[];
    };
    lostCaptions.en = [];
    expect(() => projectFulfillmentDossiers({ requests: [lost] })).toThrow(
      /caption segments lose or alter screen text/,
    );

    const tooLong = requestFor();
    const longCaptions = at(tooLong.screens, 0).captionSegments as {
      en: string[];
      "es-ES": string[];
    };
    longCaptions.en = [
      Array.from({ length: 33 }, (_, index) => `word${index}`).join(" "),
    ];
    expect(() => projectFulfillmentDossiers({ requests: [tooLong] })).toThrow(
      /caption segment exceeds 32 words/,
    );
  });

  test("rejects coordinates on the exclusive map edge", () => {
    const profile = makeFulfillmentProfile();
    profile.districts.push("fixture.unused-district");
    const request = requestFor(profile);
    at(request.hubs, 1).centre = [request.mapSize, request.mapSize];
    expect(() => projectFulfillmentDossiers({ requests: [request] })).toThrow(
      /hub outside map bounds/,
    );
  });

  test("checks the full zone footprint against tile centres and honors authored tolerance", () => {
    const edgeProfile = makeFulfillmentProfile();
    const edgeZone = at(edgeProfile.worldContract.zones, 0);
    edgeZone.offsetTiles = [1, 100];
    edgeZone.radiusTiles = 2;
    const edgeRequest = requestFor(edgeProfile);
    at(edgeRequest.hubs, 0).centre = [0, 0];
    const edgePoint = found(
      edgeRequest.pointZoneBindings.find(
        (point) => point.zoneId === edgeZone.id,
      ),
    );
    edgePoint.tile = [1, 100];
    expect(() =>
      projectFulfillmentDossiers({ requests: [edgeRequest] }),
    ).toThrow(/zone footprint outside map bounds/);

    const within = requestFor();
    at(within.pointZoneBindings, 0).tile[0] += 0.000001 - 0.000000001;
    expect(
      projectFulfillmentDossiers({ requests: [within] }).projections,
    ).toHaveLength(1);
    const atLimit = requestFor();
    at(atLimit.pointZoneBindings, 0).tile[0] += 0.000001;
    expect(
      projectFulfillmentDossiers({ requests: [atLimit] }).projections,
    ).toHaveLength(1);
    const outside = requestFor();
    at(outside.pointZoneBindings, 0).tile[0] += 0.000001 + 0.000000001;
    expect(() => projectFulfillmentDossiers({ requests: [outside] })).toThrow(
      /authored tile disagrees/,
    );
  });

  test("requires distinct plan screens and distinct service goal/completion IDs", () => {
    const repeatedPlan = requestFor();
    repeatedPlan.planScreenIds.started = repeatedPlan.planScreenIds.reserved;
    expect(() =>
      projectFulfillmentDossiers({ requests: [repeatedPlan] }),
    ).toThrow(/plan screen IDs must be distinct/);
    const reusedConfirmation = requestFor();
    at(reusedConfirmation.serviceBindings, 0).completeScreenId =
      reusedConfirmation.planScreenIds.reserved;
    expect(() =>
      projectFulfillmentDossiers({ requests: [reusedConfirmation] }),
    ).toThrow(/cannot reuse reserved\/started confirmation/);
    const sameGoalAndComplete = requestFor();
    const service = at(sameGoalAndComplete.serviceBindings, 0);
    service.completeScreenId = service.goalScreenId;
    expect(() =>
      projectFulfillmentDossiers({ requests: [sameGoalAndComplete] }),
    ).toThrow(/goal and completion screens must differ/);
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

  test("rejects work and reception overlap across different hubs", () => {
    const profile = makeFulfillmentProfile();
    profile.districts.push("fixture.second-hub");
    const recipe = at(at(profile.fulfillmentPlan.services, 0).recipes, 0);
    const workZone = found(
      profile.worldContract.zones.find((zone) => zone.id === recipe.workZoneId),
    );
    const receptionZone = found(
      profile.worldContract.zones.find(
        (zone) => zone.id === recipe.receptionZoneId,
      ),
    );
    receptionZone.hub = "fixture.second-hub";
    const request = requestFor(profile);
    const workPoint = found(
      request.pointZoneBindings.find((point) => point.zoneId === workZone.id),
    );
    const receptionPoint = found(
      request.pointZoneBindings.find(
        (point) => point.zoneId === receptionZone.id,
      ),
    );
    at(request.hubs, 1).centre = [
      workPoint.tile[0] - receptionZone.offsetTiles[0],
      workPoint.tile[1] - receptionZone.offsetTiles[1],
    ];
    receptionPoint.tile = [...workPoint.tile];
    expect(() => projectFulfillmentDossiers({ requests: [request] })).toThrow(
      /work\/reception footprints overlap/,
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
          {
            reachableSubsetCount: number;
            protectedRecoveryExcluded: boolean;
            examples: Array<{ completedTaskIds: string[] }>;
            scope: string;
            afterFundingSelections: Array<{
              recipeIds: string[];
              mainAffordable: boolean;
              initialRemainder: Record<string, number> | null;
              scope: string;
              reachableSubsetCount: number | null;
              allOptionalTasksAffordable: boolean | null;
              examples: Array<{ completedTaskIds: string[] }> | null;
              reason?: string;
            }>;
            mainAffordableSelectionCount: number;
            allOptionalTasksAffordableAfterFundingCount: number;
          }
        >;
        selectionAnalysisByDifficulty: Record<
          string,
          { affordableSelections: string[][]; selections: unknown[] }
        >;
        optionalFinancialInputs: {
          optionalTasks: Array<{
            id: string;
            cost: { food: number; wood: number; gold: number; stone: number };
          }>;
        };
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
    const projection = response.projections[0];
    expect(
      projection?.selectionAnalysisByDifficulty.easy?.affordableSelections,
    ).toHaveLength(9);
    expect(
      projection?.selectionAnalysisByDifficulty.standard?.affordableSelections,
    ).toHaveLength(7);
    expect(
      projection?.selectionAnalysisByDifficulty.hard?.affordableSelections,
    ).toHaveLength(3);
    const hardAnalysis = projection?.optionalPrefixAnalysisByDifficulty.hard;
    expect(hardAnalysis?.scope).toBe("before-main-funding");
    expect(hardAnalysis?.afterFundingSelections).toHaveLength(
      projection?.selectionAnalysisByDifficulty.hard?.selections.length ?? -1,
    );
    expect(hardAnalysis?.mainAffordableSelectionCount).toBe(3);
    expect(projectFulfillmentDossiers({ requests: [request] })).toEqual(
      projectFulfillmentDossiers({ requests: [request] }),
    );
    const kindsById = Object.fromEntries(
      (
        request.referenceCapabilityProfile as ReturnType<
          typeof makeFulfillmentProfile
        >
      ).secondaryObjectives.map((side) => [side.id, side.kind]),
    );
    const hardSelection = found(
      hardAnalysis?.afterFundingSelections.find(
        (row) =>
          row.recipeIds.includes(recipeIds.mealHearth) &&
          row.recipeIds.includes(recipeIds.shelterRented),
      ),
    );
    expect(hardSelection.scope).toBe("after-main-funding");
    expect(hardSelection.mainAffordable).toBe(true);
    expect(hardSelection.initialRemainder?.wood).toBe(20);
    const aidId = Object.keys(kindsById).find((id) => kindsById[id] === "aid");
    const repairId = Object.keys(kindsById).find(
      (id) => kindsById[id] === "repair",
    );
    expect(aidId).toBeDefined();
    expect(repairId).toBeDefined();
    expect(
      projection?.optionalFinancialInputs.optionalTasks.find(
        (task) => task.id === repairId,
      )?.cost.wood,
    ).toBe(50);
    expect(
      hardSelection.examples?.some(
        (example) =>
          example.completedTaskIds.length === 1 &&
          example.completedTaskIds[0] === repairId,
      ),
    ).toBe(false);
    expect(
      hardSelection.examples?.some(
        (example) =>
          example.completedTaskIds.length === 2 &&
          example.completedTaskIds[0] === aidId &&
          example.completedTaskIds[1] === repairId,
      ),
    ).toBe(true);
  });

  test("runs a complete artificial three-service blueprint through bridge, composer, audit, wiki, and SVG", async () => {
    const profile = threeServiceProfile();
    const request = requestFor(profile);
    const selectionId = "fixture.intermediate";
    request.episodeId = selectionId;
    const roles = {
      title: "plan.preview",
      factualIntro: "plan.reserved",
      handover: "plan.cancelled",
      personalIntro: "plan.started",
      factualOutro: "plan.complete",
      personalOutro: "service.fulfillment-fixture.meal-service.goal",
      defeat: "service.fulfillment-fixture.meal-service.complete",
      continuation: "service.fulfillment-fixture.shelter-service.goal",
    };
    const roleText = {
      factualIntro: {
        en: "A synthetic documented frame.",
        "es-ES": "Un marco documentado sintético.",
      },
      factualOutro: {
        en: "A synthetic documented outcome.",
        "es-ES": "Un resultado documentado sintético.",
      },
    };
    const narrator = "fixture.narrator";
    for (const screen of request.screens) {
      if (screen.id === roles.factualIntro) screen.text = roleText.factualIntro;
      if (screen.id === roles.factualOutro) screen.text = roleText.factualOutro;
      if (
        screen.id === roles.factualIntro ||
        screen.id === roles.factualOutro ||
        screen.id === roles.handover
      )
        screen.narrator = "collection-narrator";
      if (
        screen.id === roles.personalIntro ||
        screen.id === roles.personalOutro
      )
        screen.narrator = narrator;
      if (screen.id === roles.title) screen.narrator = "none";
      const text = screen.text as { en: string; "es-ES": string };
      screen.captionSegments = { en: [text.en], "es-ES": [text["es-ES"]] };
    }
    const bbox = [-1, -1, 1, 1];
    const size = request.mapSize;
    const span = 2 * 1.12;
    const lonLatFor = (tile: readonly [number, number]) => [
      (tile[0] / (size - 1) - 0.5) * span,
      (0.5 - tile[1] / (size - 1)) * span,
    ];
    const hubs = request.hubs.map((hub) => ({
      id: hub.id,
      centre: hub.centre,
      lonLat: lonLatFor(hub.centre),
      name: { en: hub.id, "es-ES": hub.id },
      radiusTiles: 3,
      certainty: "synthetic test fixture only",
    }));
    const points = request.pointZoneBindings.map((point) => ({
      id: point.pointId,
      lonLat: lonLatFor(point.tile),
      tile: point.tile,
      name: { en: point.pointId, "es-ES": point.pointId },
      certainty: "synthetic test fixture only",
    }));
    const corridorIds = new Set<string>();
    for (const side of profile.secondaryObjectives) {
      side.reachability.corridorIds.forEach((id) => {
        corridorIds.add(id);
      });
      for (const effect of side.effects)
        if (effect.kind === "mark-alternative-route" && effect.corridorId)
          corridorIds.add(effect.corridorId);
    }
    const fixtureHubId = found(request.hubs[0]).id;
    const portfolioSideIds = profile.secondaryObjectives
      .slice(0, 5)
      .map((side) => side.id);
    if (portfolioSideIds.length !== 5)
      throw new Error("fixture requires five distinct optional IDs");
    const corridors = [...corridorIds].map((id) => ({
      id,
      hubOrder: [fixtureHubId, fixtureHubId],
      mode: "land",
      widthTiles: 1,
    }));
    const factualIntro = roleText.factualIntro;
    const factualOutro = roleText.factualOutro;
    const dossierMetadata = {
      factualIntro,
      factualOutro,
      dramatizationNotice: {
        en: "Synthetic only.",
        "es-ES": "Sólo sintético.",
      },
      mapPlan: {
        bbox,
        terrainProfile: "fixture.region",
        orientation: "north-up",
        projection: "synthetic WGS84 test frame",
        hubs,
        points,
        corridors,
        terrainInstructions: "Synthetic test controls only.",
        geographicLayers: [],
        geometryStatus: "fixture only; no geographic assertion",
        asset: "docs/design/maps/fixture/odyssey/fixture-intermediate.svg",
      },
      historicalMaterialPolicyByEntity: Object.fromEntries(
        profile.worldContract.entities.map((entity) => [
          entity.id,
          "Synthetic fixture identity; no historical claim.",
        ]),
      ),
      artDirection: {
        style: "synthetic fixture",
        historicalControls: [],
        referenceAssets: [],
        productionApproved: false,
      },
      failureRecovery: {
        policy: "Synthetic fixture; no gameplay behavior asserted.",
      },
      requiredCapabilities: [
        { id: "fixture.capability", status: "pending; synthetic fixture" },
      ],
      qaCases: ["Synthetic bridge and composition path only."],
      playstyles: [
        [at(portfolioSideIds, 0), at(portfolioSideIds, 1)],
        [at(portfolioSideIds, 2), at(portfolioSideIds, 3)],
        [at(portfolioSideIds, 4)],
      ].map((optionalObjectives, index) => ({
        id: `fixture.playstyle.${index + 1}`,
        optionalObjectives,
        costOfOpportunity: `Synthetic opportunity ${index + 1}`,
        mainObjectivesUnchanged: true,
        historicalOutcomeUnchanged: true,
      })),
      gameplayIdentity: Object.fromEntries(
        ["problem", "decision", "density", "replay"].map((key) => [
          key,
          "Synthetic test fixture only.",
        ]),
      ),
      editorialReviewNotes: { status: "synthetic test; review pending" },
      screenRoles: roles,
      continuation: {
        nextEpisodeId: "fixture.next",
        campaignComplete: false,
        sourceScreenId: roles.continuation,
      },
    };
    const blueprint = {
      designProfile: "alternative-fulfillment-v3",
      ...request,
      dossierMetadata,
    };
    const campaign = {
      campaignId: "fixture",
      editorialContract: { publicId: "fixture", narratorId: narrator },
    };
    const selection = {
      id: selectionId,
      order: 2,
      actId: "fixture.act",
      title: { en: "Fixture", "es-ES": "Prueba" },
      date: "synthetic",
      knowledgeBasis: { speaker: narrator },
      coreMechanic: "synthetic typed projection",
      geographyId: "fixture.region",
      historicalPersonPolicy: "No historical person represented.",
      historicalSelection: { selectedClaim: "Synthetic fixture claim." },
    };

    const root = new URL("../..", import.meta.url).pathname;
    const helper = new URL(
      "../../tools/design/fulfillment-dossier.helper.py",
      import.meta.url,
    ).pathname;
    const bridgeInput = `/tmp/fulfillment-bridge-${crypto.randomUUID()}.json`;
    writeFileSync(bridgeInput, JSON.stringify({ requests: [request] }));
    const bridge = Bun.spawnSync(["python3", helper], {
      cwd: root,
      stdin: Bun.file(bridgeInput),
      stdout: "pipe",
      stderr: "pipe",
    });
    unlinkSync(bridgeInput);
    expect(bridge.exitCode, bridge.stderr.toString()).toBe(0);
    const projection = (
      JSON.parse(bridge.stdout.toString()) as {
        projections: Array<Record<string, unknown>>;
      }
    ).projections[0];
    if (!projection)
      throw new Error("bridge returned no artificial projection");
    const payload = JSON.stringify({
      campaign,
      selection,
      blueprint,
      projection,
      request,
    });
    const python = [
      "import importlib.util,json,sys",
      "from pathlib import Path",
      `root=Path(${JSON.stringify(root)})`,
      "sys.path.insert(0,str(root/'tools/design'))",
      "def load(name):\n p=root/'tools/design'/f'{name}.py'\n s=importlib.util.spec_from_file_location(name,p)\n m=importlib.util.module_from_spec(s)\n s.loader.exec_module(m)\n return m",
      "factory=load('episode_dossier.factory'); validator=load('episode_dossier.validator'); pipeline=load('episode_dossiers.script'); civic=load('civic_difficulty_audit.script')",
      "p=json.load(sys.stdin); e=factory.build_fulfillment_dossier(p['campaign'],p['selection'],p['blueprint'],p['projection'],{'bbox':[-1,-1,1,1]}, {'id':'fixture.previous'}, {'id':'fixture.next'})",
      "req={k:p['request'][k] for k in ('episodeId','referenceCapabilityProfile','accountsByDifficulty','mapSize','hubs','pointZoneBindings','recipeBindings','serviceBindings','planScreenIds','screens')}",
      "errors=validator.audit_dossier(e,p['campaign'],projection_context={'request':req,'projection':p['projection']})",
      "assert not errors, errors",
      "civic_row=civic.episode_audit(p['campaign']['campaignId'],e)",
      "assert civic_row['designProfile']=='alternative-fulfillment-v3' and civic_row['accountsByDifficulty']==req['accountsByDifficulty']",
      "assert civic_row['selectionAnalysisByDifficulty']==p['projection']['selectionAnalysisByDifficulty'] and civic_row['authoredEnemyRoster']==p['projection']['referenceCapabilityProfile']['enemyRoster']",
      "assert civic_row['affordableSelectionCountByDifficulty']=={level:len(p['projection']['selectionAnalysisByDifficulty'][level]['affordableSelections']) for level in ('easy','standard','hard')}",
      "assert civic_row['budgetBasis']=='v3 initial spendable operating account; excludes protected recovery and unearned optional rewards' and 'enemyTotalCapByDifficulty' not in civic_row",
      "assert 'bridgeDossierProjection' not in e and e['referenceCapabilityProfile']==p['projection']['referenceCapabilityProfile'] and e['id']==p['projection']['episodeId']",
      "import copy",
      "duplicate_portfolios=copy.deepcopy(p['blueprint']); a,b=duplicate_portfolios['dossierMetadata']['playstyles'][:2]; b['optionalObjectives']=list(reversed(a['optionalObjectives'])); b['costOfOpportunity']='Different wording must not make a duplicate task set distinct';\ntry: factory.build_fulfillment_dossier(p['campaign'],p['selection'],duplicate_portfolios,p['projection'],{'bbox':[-1,-1,1,1]}, {'id':'fixture.previous'}, {'id':'fixture.next'}); raise AssertionError('duplicate portfolios accepted')\nexcept ValueError as error: assert 'portfolios must be distinct' in str(error), error",
      "for field,mutate in [('service',lambda d: d['fulfillmentServices'][0]['recipes'][0]['cost'].__setitem__('food',d['fulfillmentServices'][0]['recipes'][0]['cost']['food']+1)),('worker',lambda d: d['fulfillmentServices'][0]['recipes'][0].__setitem__('workerId','fixture.drift-worker')),('recipient',lambda d: d['fulfillmentServices'][0]['recipes'][0]['recipientIds'].append('fixture.drift-recipient')),('analysis',lambda d: d['selectionAnalysisByDifficulty']['hard']['spendable'].__setitem__('food',-1)),('financial',lambda d: d['optionalFinancialInputs']['optionalTasks'][0]['cost'].__setitem__('food',999))]:\n d=copy.deepcopy(e); mutate(d); assert validator.audit_dossier(d,p['campaign'],projection_context={'request':req,'projection':p['projection']}), field",
      "profile_drift=copy.deepcopy(e); profile_drift['referenceCapabilityProfile']['fulfillmentPlan']['services'][0]['recipes'][0]['cost']['food']+=1; assert validator.audit_dossier(profile_drift,p['campaign'],projection_context={'request':req,'projection':p['projection']})",
      "wiki=pipeline.fulfillment_wiki(p['campaign'],e); svg=pipeline.diagram(e,[])",
      "assert 'Alternative services' in wiki and 'Authored presentation' in wiki and 'Before main funding:' in wiki and 'After main funding:' in wiki and 'Reachable optional subsets after funding' in wiki and '<svg' in svg",
      "import xml.etree.ElementTree as ET",
      "svg_root=ET.fromstring(svg); svg_texts=svg_root.findall('{http://www.w3.org/2000/svg}text')",
      "narrow_rows=[row for row in svg_texts if row.text and ('Olive dashed:' in row.text or row.text.startswith('connections under'))]; narrow_label=' '.join(row.text for row in narrow_rows)",
      "assert narrow_label=='Olive dashed: proposed narrow land connections under 10 tiles' and len(narrow_rows)==2, [(row.text,row.attrib) for row in svg_texts]",
      "assert all(int(row.attrib['x'])==730 and len(row.text)<=42 for row in narrow_rows) and int(narrow_rows[1].attrib['y'])-int(narrow_rows[0].attrib['y'])==24, [(row.text,row.attrib) for row in narrow_rows]",
      "assert not any('boat' in (row.text or '').lower() or 'schematic regional water' in (row.text or '').lower() for row in svg_texts), [row.text for row in svg_texts]",
      "water_index=pipeline.layers_helper.index_layer({'features':[{'geometry':{'type':'LineString','coordinates':[[-0.5,0],[0.5,0]]}}]})",
      "water_svg=pipeline.diagram(e,[{'index':water_index,'colour':'#247b96'}]); water_root=ET.fromstring(water_svg)",
      "water_texts=water_root.findall('{http://www.w3.org/2000/svg}text'); water_rows=[row for row in water_texts if row.text and ('Solid blue:' in row.text or row.text=='controls')]",
      "water_lines=[row for row in water_root.findall('{http://www.w3.org/2000/svg}polyline') if row.attrib.get('stroke')=='#247b96']",
      "assert ' '.join(row.text for row in water_rows)=='Solid blue: modern geographic water controls' and len(water_rows)==2",
      "assert all(int(row.attrib['x'])==730 and len(row.text)<=42 for row in water_rows) and int(water_rows[1].attrib['y'])-int(water_rows[0].attrib['y'])==24",
      "assert water_lines and all('stroke-dasharray' not in row.attrib for row in water_lines)",
      "legacy=copy.deepcopy(e); legacy.pop('designProfile'); legacy_svg=pipeline.diagram(legacy,[]); legacy_root=ET.fromstring(legacy_svg); legacy_texts=[row for row in legacy_root.findall('{http://www.w3.org/2000/svg}text') if row.attrib.get('x')=='730' and int(row.attrib['y'])>=420]; assert [row.text for row in legacy_texts]==['Geographic district controls only','Brown dashed: proposed land route','Cyan dashed: proposed boat passage','Not a surveyed path or terrain raster','Blue: modern geographic water controls','Dashed blue: schematic regional water','Native footprints and navigation pending','No ancient shore or elevation inferred'], [(row.text,row.attrib) for row in legacy_texts]",
      "tall=copy.deepcopy(e); base_hub=tall['mapPlan']['hubs'][0]['id']; tall['mapPlan']['hubs']=[{'id': (base_hub if i==1 else f'{base_hub}.{i}'),'centre':[min(20+i*18,380),60],'lonLat':[0,0],'name':{'en':f'Synthetic district {i}','es-ES':f'Distrito sintético {i}'},'radiusTiles':3,'certainty':'synthetic only'} for i in range(1,20)]",
      "tall_svg=pipeline.diagram(tall,[]); root_svg=ET.fromstring(tall_svg); canvas_height=float(root_svg.attrib['viewBox'].split()[3]); text_rows=root_svg.findall('{http://www.w3.org/2000/svg}text'); final_label=next(row for row in text_rows if row.text=='19: Synthetic district 19'); final_legend=next(row for row in text_rows if row.text=='No ancient shore or elevation inferred'); assert canvas_height>850 and canvas_height>=max(float(final_label.attrib['y']),float(final_legend.attrib['y']))+12",
      "print(json.dumps({'audit':errors,'civic':civic_row,'wiki':wiki,'svg':svg,'serviceCount':len(e['fulfillmentServices']),'portfolioCount':len(e['playstyles'])}))",
    ].join("\n");
    const composeInput = `/tmp/fulfillment-compose-${crypto.randomUUID()}.json`;
    writeFileSync(composeInput, payload);
    const composed = Bun.spawnSync(["python3", "-c", python], {
      cwd: root,
      stdin: Bun.file(composeInput),
      stdout: "pipe",
      stderr: "pipe",
    });
    unlinkSync(composeInput);
    expect(composed.exitCode, composed.stderr.toString()).toBe(0);
    const output = JSON.parse(composed.stdout.toString()) as {
      serviceCount: number;
      portfolioCount: number;
      civic: {
        designProfile: string;
        affordableSelectionCountByDifficulty: Record<string, number>;
      };
      wiki: string;
      svg: string;
    };
    expect(output.serviceCount).toBe(3);
    expect(output.portfolioCount).toBe(3);
    expect(output.civic.designProfile).toBe("alternative-fulfillment-v3");
    expect(output.civic.affordableSelectionCountByDifficulty).toEqual({
      easy: 9,
      standard: 6,
      hard: 2,
    });
    expect(output.wiki).toContain("Synthetic only.");
    expect(output.svg).toContain("Fixture");
  });
});
