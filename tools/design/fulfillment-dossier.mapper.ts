import { z } from "zod";
import {
  debit,
  enough,
  normalizeResources,
  RESOURCES,
} from "../../packages/gameplay-state/resource-accounts.helper";
import { validateScenarioCapability } from "../../packages/gameplay-validation/scenario-capability.validator";
import {
  type CapabilityProfileV3,
  capabilityProfileV3Schema,
  type FulfillmentResources,
} from "../../packages/schemas/alternative-fulfillment.schema";

const bilingual = z.strictObject({
  en: z.string().trim().min(1),
  "es-ES": z.string().trim().min(1),
});
const presentationId = z
  .string()
  .min(1)
  .refine(
    (id) => !Object.hasOwn(Object.prototype, id),
    "Reserved JavaScript object key",
  );
const vector = z.tuple([z.number().finite(), z.number().finite()]);
const resources = z.strictObject({
  food: z.number().int().safe().nonnegative(),
  wood: z.number().int().safe().nonnegative(),
  gold: z.number().int().safe().nonnegative(),
  stone: z.number().int().safe().nonnegative(),
});
type ResourceVector = {
  food: number;
  wood: number;
  gold: number;
  stone: number;
};
const account = z.strictObject({
  spendable: resources,
  protectedRecovery: resources,
  optionalReserve: resources,
});
const projectionScreen = z.strictObject({
  id: presentationId,
  key: presentationId,
  text: bilingual,
  condition: z.string().min(1),
  narrator: z.string().min(1),
  skippable: z.boolean(),
  captionPolicy: z.string().min(1),
  captionSegments: z.strictObject({
    en: z.array(z.string()),
    "es-ES": z.array(z.string()),
  }),
  nativeSurface: z.string().min(1),
  voiceDurationSecondsEstimated: z.number().int().positive(),
});
const projectionRequestSchema = z.strictObject({
  episodeId: presentationId,
  referenceCapabilityProfile: z.unknown(),
  accountsByDifficulty: z.strictObject({
    easy: account,
    standard: account,
    hard: account,
  }),
  mapSize: z.number().int().min(300).max(400),
  hubs: z.array(z.strictObject({ id: presentationId, centre: vector })),
  pointZoneBindings: z.array(
    z.strictObject({
      pointId: presentationId,
      tile: vector,
      zoneId: presentationId,
      hubId: presentationId,
      offsetTiles: vector,
    }),
  ),
  recipeBindings: z.array(
    z.strictObject({
      serviceId: presentationId,
      recipeId: presentationId,
      workPointId: presentationId,
      receptionPointId: presentationId,
      title: bilingual,
      goalScreenId: presentationId,
    }),
  ),
  serviceBindings: z.array(
    z.strictObject({
      serviceId: presentationId,
      goalScreenId: presentationId,
      completeScreenId: presentationId,
    }),
  ),
  planScreenIds: z.strictObject({
    preview: presentationId,
    reserved: presentationId,
    cancelled: presentationId,
    started: presentationId,
    complete: presentationId,
  }),
  screens: z.array(projectionScreen),
});

export type ProjectionRequest = z.infer<typeof projectionRequestSchema>;
export type DossierProjection = {
  episodeId: string;
  referenceCapabilityProfile: CapabilityProfileV3;
  worldContract: CapabilityProfileV3["worldContract"];
  objectivePlan: CapabilityProfileV3["objectivePlan"];
  stateMachine: CapabilityProfileV3["stateMachine"];
  secondaryObjectives: CapabilityProfileV3["secondaryObjectives"];
  secondaryBudget: CapabilityProfileV3["secondaryBudget"];
  fulfillmentServices: Array<{
    serviceId: string;
    goalScreenId: string;
    completeScreenId: string;
    recipes: Array<{
      serviceId: string;
      recipeId: string;
      workPointId: string;
      receptionPointId: string;
      workZoneId: string;
      receptionZoneId: string;
      title: { en: string; "es-ES": string };
      goalScreenId: string;
      workerId: string;
      outputEntityId: string;
      recipientIds: string[];
      cost: FulfillmentResources;
    }>;
  }>;
  selectionAnalysisByDifficulty: Record<string, unknown>;
  optionalFinancialInputs: Record<string, unknown>;
  mapBindings: {
    hubs: ProjectionRequest["hubs"];
    points: Array<
      ProjectionRequest["pointZoneBindings"][number] & {
        absoluteTile: [number, number];
        radiusTiles: number;
      }
    >;
  };
  planScreenIds: ProjectionRequest["planScreenIds"];
  screens: ProjectionRequest["screens"];
};

function fail(episodeId: string, message: string): never {
  throw new Error(`${episodeId}: ${message}`);
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function assertUnique<T>(
  rows: T[],
  key: (row: T) => string,
  label: string,
  episodeId: string,
) {
  const seen = new Set<string>();
  for (const row of rows) {
    const value = key(row);
    if (seen.has(value)) fail(episodeId, `duplicate ${label}: ${value}`);
    seen.add(value);
  }
  return seen;
}

function safeVectorSum(
  a: Record<string, number | undefined>,
  b: Record<string, number | undefined>,
  episodeId: string,
  label: string,
): ResourceVector {
  const total: ResourceVector = { food: 0, wood: 0, gold: 0, stone: 0 };
  for (const resource of RESOURCES) {
    const value = (a[resource] ?? 0) + (b[resource] ?? 0);
    if (!Number.isSafeInteger(value))
      fail(episodeId, `${label} overflows ${resource}`);
    total[resource] = value;
  }
  return total;
}

function checkAccountReserve(
  profile: CapabilityProfileV3,
  request: ProjectionRequest,
) {
  const expected = profile.secondaryBudget.reservedRewards;
  for (const level of ["easy", "standard", "hard"] as const) {
    const got = request.accountsByDifficulty[level].optionalReserve;
    for (const resource of RESOURCES) {
      if ((got[resource] ?? 0) !== (expected[resource] ?? 0))
        fail(
          request.episodeId,
          `${level} optionalReserve.${resource} does not equal secondaryBudget.reservedRewards`,
        );
    }
  }
}

function checkProfileEconomics(
  profile: CapabilityProfileV3,
  episodeId: string,
) {
  for (const objective of profile.objectivePlan) {
    const amounts = objective.predicate.resourceAmounts;
    if (RESOURCES.some((resource) => (amounts[resource] ?? 0) !== 0))
      fail(
        episodeId,
        `unsupported projection: shared objective ${objective.id} has resourceAmounts`,
      );
    for (const requirement of objective.predicate.requirements) {
      if (requirement.kind === "resource-transaction")
        fail(
          episodeId,
          `unsupported projection: shared objective ${objective.id} has fixed resource-transaction ${requirement.id}`,
        );
    }
  }
}

function optionalFinancialInputs(
  profile: CapabilityProfileV3,
  episodeId: string,
) {
  const rows = profile.secondaryObjectives.map((side) => {
    const payments = side.predicate.requirements.filter(
      (req) => req.kind === "atomic-payment",
    );
    if (payments.length > 1)
      fail(
        episodeId,
        `unsupported optional financial shape for ${side.id}: multiple atomic payments`,
      );
    const cost = { food: 0, wood: 0, gold: 0, stone: 0 };
    if (payments[0])
      Object.assign(cost, normalizeResources(payments[0].resources));
    const withdrawals = side.effects.filter(
      (effect) => effect.kind === "finite-supply-withdrawal",
    );
    if (withdrawals.length > 1)
      fail(
        episodeId,
        `unsupported optional financial shape for ${side.id}: multiple finite withdrawals`,
      );
    const reward = { food: 0, wood: 0, gold: 0, stone: 0 };
    if (withdrawals[0])
      Object.assign(reward, normalizeResources(withdrawals[0].resources));
    for (const effect of side.effects) {
      if (
        effect !== withdrawals[0] &&
        RESOURCES.some((resource) => (effect.resources[resource] ?? 0) !== 0)
      )
        fail(
          episodeId,
          `unsupported optional financial shape for ${side.id}: resource-bearing ${effect.kind} effect`,
        );
    }
    for (const req of side.predicate.requirements) {
      if (
        req.kind !== "atomic-payment" &&
        req.kind === "entity-health" &&
        !payments.some((payment) => payment.receipt === req.paymentReceipt)
      )
        fail(
          episodeId,
          `optional ${side.id} health requirement is not linked to an authored payment`,
        );
    }
    return { id: side.id, cost, reward };
  });
  const rewardTotal = rows.reduce<ResourceVector>(
    (sum, row) =>
      safeVectorSum(sum, row.reward, episodeId, "optional reward total"),
    { food: 0, wood: 0, gold: 0, stone: 0 },
  );
  for (const resource of RESOURCES) {
    if (
      rewardTotal[resource] !==
      (profile.secondaryBudget.reservedRewards[resource] ?? 0)
    )
      fail(
        episodeId,
        `optional reward total ${resource} does not conserve secondaryBudget.reservedRewards`,
      );
  }
  return {
    optionalTasks: rows,
    status:
      "candidate finite accounting; spatial predicates assumed successful; not a task completion or route",
  };
}

function projectOne(value: unknown): DossierProjection {
  const parsed = projectionRequestSchema.safeParse(value);
  if (!parsed.success)
    throw new Error(`invalid projection request: ${parsed.error.message}`);
  const request = parsed.data;
  if (!isRecord(request.referenceCapabilityProfile))
    fail(request.episodeId, "referenceCapabilityProfile must be an object");
  const profileResult = capabilityProfileV3Schema.safeParse(
    request.referenceCapabilityProfile,
  );
  if (!profileResult.success)
    fail(
      request.episodeId,
      `invalid schemaVersion 3 referenceCapabilityProfile: ${profileResult.error.message}`,
    );
  const profile = profileResult.data;
  const issues = validateScenarioCapability(profile);
  if (issues.length)
    fail(
      request.episodeId,
      `semantic validation failed: ${issues.map((item) => `${item.code}(${item.path}): ${item.message}`).join("; ")}`,
    );
  checkProfileEconomics(profile, request.episodeId);
  checkAccountReserve(profile, request);

  const hubs = assertUnique(
    request.hubs,
    (row) => row.id,
    "hub id",
    request.episodeId,
  );
  if (
    hubs.size !== profile.districts.length ||
    profile.districts.some((id) => !hubs.has(id))
  )
    fail(
      request.episodeId,
      "hubs must resolve every profile district exactly once",
    );
  for (const hub of request.hubs) {
    if (
      hub.centre.some(
        (coordinate) => coordinate < 0 || coordinate > request.mapSize - 1,
      )
    )
      fail(request.episodeId, `hub outside map bounds: ${hub.id}`);
  }

  const zones = new Map(
    profile.worldContract.zones.map((zone) => [zone.id, zone]),
  );
  assertUnique(
    request.pointZoneBindings,
    (row) => row.pointId,
    "pointId",
    request.episodeId,
  );
  assertUnique(
    request.pointZoneBindings,
    (row) => row.zoneId,
    "zone binding",
    request.episodeId,
  );
  if (
    request.pointZoneBindings.length !== zones.size ||
    [...zones.keys()].some(
      (id) => !request.pointZoneBindings.some((row) => row.zoneId === id),
    )
  )
    fail(
      request.episodeId,
      "pointZoneBindings must resolve every main-world zone exactly once",
    );
  const hubMap = new Map(request.hubs.map((hub) => [hub.id, hub]));
  const points = request.pointZoneBindings.map((binding) => {
    const zone = zones.get(binding.zoneId);
    if (!zone)
      fail(request.episodeId, `unknown zone binding: ${binding.zoneId}`);
    const hub = hubMap.get(binding.hubId);
    if (!hub || zone.hub !== binding.hubId)
      fail(
        request.episodeId,
        `point ${binding.pointId} hub does not match zone ${binding.zoneId}`,
      );
    if (
      binding.offsetTiles[0] !== zone.offsetTiles[0] ||
      binding.offsetTiles[1] !== zone.offsetTiles[1]
    )
      fail(
        request.episodeId,
        `point ${binding.pointId} offset does not match zone ${binding.zoneId}`,
      );
    const absoluteTile: [number, number] = [
      hub.centre[0] + zone.offsetTiles[0],
      hub.centre[1] + zone.offsetTiles[1],
    ];
    for (const axis of [0, 1] as const) {
      if (
        !Number.isFinite(absoluteTile[axis]) ||
        Math.abs(absoluteTile[axis] - binding.tile[axis]) > 0.000001
      )
        fail(
          request.episodeId,
          `point ${binding.pointId} authored tile disagrees with hub plus zone offset on axis ${axis}`,
        );
      if (
        absoluteTile[axis] - zone.radiusTiles < 0 ||
        absoluteTile[axis] + zone.radiusTiles > request.mapSize - 1
      )
        fail(
          request.episodeId,
          `zone footprint outside map bounds: ${zone.id}`,
        );
    }
    return { ...binding, absoluteTile, radiusTiles: zone.radiusTiles };
  });
  const pointMap = new Map(points.map((point) => [point.pointId, point]));
  const recipes = profile.fulfillmentPlan.services.flatMap((service) =>
    service.recipes.map((recipe) => ({ service, recipe })),
  );
  assertUnique(
    request.recipeBindings,
    (row) => row.recipeId,
    "recipe binding",
    request.episodeId,
  );
  if (request.recipeBindings.length !== recipes.length)
    fail(
      request.episodeId,
      "recipeBindings must bind every recipe exactly once",
    );
  const bindingsByRecipe = new Map(
    request.recipeBindings.map((row) => [row.recipeId, row]),
  );
  assertUnique(
    request.screens,
    (row) => row.id,
    "screen id",
    request.episodeId,
  );
  assertUnique(
    request.screens,
    (row) => row.key,
    "screen key",
    request.episodeId,
  );
  const screenById = new Map(
    request.screens.map((screen) => [screen.id, screen]),
  );
  for (const screen of request.screens) {
    for (const locale of ["en", "es-ES"] as const) {
      const expected = screen.text[locale]
        .split(/\s+/)
        .filter(Boolean)
        .join(" ");
      const chunks = screen.captionSegments[locale];
      if (
        chunks.some(
          (chunk) => chunk.trim().split(/\s+/).filter(Boolean).length > 32,
        )
      )
        fail(
          request.episodeId,
          `caption segment exceeds 32 words: ${screen.id}/${locale}`,
        );
      if (chunks.join(" ").split(/\s+/).filter(Boolean).join(" ") !== expected)
        fail(
          request.episodeId,
          `caption segments lose or alter screen text: ${screen.id}/${locale}`,
        );
    }
  }
  const requireScreen = (id: string) => {
    if (!screenById.has(id))
      fail(request.episodeId, `unknown screen binding: ${id}`);
  };
  Object.values(request.planScreenIds).forEach(requireScreen);
  const serviceBindings = assertUnique(
    request.serviceBindings,
    (row) => row.serviceId,
    "service binding",
    request.episodeId,
  );
  if (serviceBindings.size !== profile.fulfillmentPlan.services.length)
    fail(
      request.episodeId,
      "serviceBindings must bind every service exactly once",
    );
  const services = profile.fulfillmentPlan.services.map((service) => {
    const serviceBinding = request.serviceBindings.find(
      (row) => row.serviceId === service.id,
    );
    if (!serviceBinding)
      fail(request.episodeId, `missing service binding ${service.id}`);
    requireScreen(serviceBinding.goalScreenId);
    requireScreen(serviceBinding.completeScreenId);
    const projectedRecipes = service.recipes.map((recipe) => {
      const binding = bindingsByRecipe.get(recipe.id);
      if (!binding || binding.serviceId !== service.id)
        fail(
          request.episodeId,
          `missing or cross-service recipe binding ${recipe.id}`,
        );
      const work = pointMap.get(binding.workPointId);
      const reception = pointMap.get(binding.receptionPointId);
      if (!work || work.zoneId !== recipe.workZoneId)
        fail(request.episodeId, `work point mismatch for recipe ${recipe.id}`);
      if (!reception || reception.zoneId !== recipe.receptionZoneId)
        fail(
          request.episodeId,
          `reception point mismatch for recipe ${recipe.id}`,
        );
      requireScreen(binding.goalScreenId);
      const dx = work.absoluteTile[0] - reception.absoluteTile[0];
      const dy = work.absoluteTile[1] - reception.absoluteTile[1];
      if (Math.hypot(dx, dy) <= work.radiusTiles + reception.radiusTiles)
        fail(
          request.episodeId,
          `work/reception footprints overlap for recipe ${recipe.id}`,
        );
      return {
        serviceId: service.id,
        recipeId: recipe.id,
        workPointId: binding.workPointId,
        receptionPointId: binding.receptionPointId,
        workZoneId: recipe.workZoneId,
        receptionZoneId: recipe.receptionZoneId,
        title: binding.title,
        goalScreenId: binding.goalScreenId,
        workerId: recipe.workerId,
        outputEntityId: recipe.outputEntityId,
        recipientIds: [...recipe.recipientIds],
        cost: { ...recipe.cost },
      };
    });
    return {
      serviceId: service.id,
      goalScreenId: serviceBinding.goalScreenId,
      completeScreenId: serviceBinding.completeScreenId,
      recipes: projectedRecipes,
    };
  });
  if (
    new Set(request.recipeBindings.map((binding) => binding.serviceId)).size !==
    profile.fulfillmentPlan.services.length
  )
    fail(request.episodeId, "recipe binding references unknown service");

  const combinations = profile.fulfillmentPlan.services.reduce(
    (rows, service) => rows * service.recipes.length,
    1,
  );
  const optionalCount = profile.secondaryObjectives.length;
  if (optionalCount > 12 || combinations * 2 ** optionalCount * 3 > 65536)
    fail(
      request.episodeId,
      "combined service/optional/difficulty analysis exceeds 65536 states",
    );
  const rows: Array<{ recipeIds: string[]; cost: ResourceVector }> = [
    { recipeIds: [], cost: { food: 0, wood: 0, gold: 0, stone: 0 } },
  ];
  for (const service of profile.fulfillmentPlan.services) {
    const next: typeof rows = [];
    for (const row of rows)
      for (const recipe of service.recipes) {
        const cost = safeVectorSum(
          row.cost,
          normalizeResources(recipe.cost),
          request.episodeId,
          "selection cost",
        );
        next.push({ recipeIds: [...row.recipeIds, recipe.id], cost });
      }
    rows.splice(0, rows.length, ...next);
  }
  const selectionAnalysisByDifficulty: Record<string, unknown> = {};
  for (const level of ["easy", "standard", "hard"] as const) {
    const spendable = request.accountsByDifficulty[level].spendable;
    const selectionRows = rows.map((row) => {
      const affordable = enough(spendable, row.cost);
      const remainder = affordable
        ? debit(spendable, row.cost)
        : Object.fromEntries(RESOURCES.map((resource) => [resource, null]));
      return {
        recipeIds: row.recipeIds,
        totalCost: row.cost,
        affordable,
        spendableRemainder: remainder,
      };
    });
    const affordable = selectionRows.filter((row) => row.affordable);
    if (!affordable.length)
      fail(
        request.episodeId,
        `${level} has no affordable all-skip complete service selection`,
      );
    selectionAnalysisByDifficulty[level] = {
      spendable: { ...spendable },
      protectedRecovery: {
        ...request.accountsByDifficulty[level].protectedRecovery,
      },
      optionalReserve: {
        ...request.accountsByDifficulty[level].optionalReserve,
      },
      selections: selectionRows,
      affordableSelections: affordable.map((row) => row.recipeIds),
    };
  }
  return {
    episodeId: request.episodeId,
    referenceCapabilityProfile: profile,
    worldContract: profile.worldContract,
    objectivePlan: profile.objectivePlan,
    stateMachine: profile.stateMachine,
    secondaryObjectives: profile.secondaryObjectives,
    secondaryBudget: profile.secondaryBudget,
    fulfillmentServices: services,
    selectionAnalysisByDifficulty,
    optionalFinancialInputs: optionalFinancialInputs(
      profile,
      request.episodeId,
    ),
    mapBindings: { hubs: request.hubs, points },
    planScreenIds: request.planScreenIds,
    screens: request.screens,
  };
}

export function projectFulfillmentDossiers(input: unknown) {
  const batch = z
    .strictObject({ requests: z.array(z.unknown()).min(1) })
    .safeParse(input);
  if (!batch.success)
    throw new Error(`invalid projection batch: ${batch.error.message}`);
  const requests = batch.data.requests;
  const ids = requests.map((row, index) =>
    isRecord(row) && typeof row.episodeId === "string"
      ? row.episodeId
      : `request-${index + 1}`,
  );
  if (new Set(ids).size !== ids.length)
    throw new Error("projection batch contains duplicate episodeId");
  return { projections: requests.map(projectOne) };
}
