import type {
  FulfillmentAction,
  FulfillmentInputContext,
} from "../../../packages/gameplay-state/fulfillment-action.model";
import {
  createFulfillmentInputContext,
  createFulfillmentSnapshot,
} from "../../../packages/gameplay-state/fulfillment-snapshot.factory";
import type {
  FulfillmentSelection,
  FulfillmentSnapshot,
} from "../../../packages/gameplay-state/fulfillment-snapshot.schema";
import { reduceFulfillmentState } from "../../../packages/gameplay-state/fulfillment-state.reducer";
import { validateScenarioCapability } from "../../../packages/gameplay-validation/scenario-capability.validator";
import {
  type CapabilityProfileV3,
  capabilityProfileV3Schema,
} from "../../../packages/schemas/alternative-fulfillment.schema";
import type { LiveSpatialBatch } from "../../../packages/schemas/live-spatial-batch.schema";
import {
  type CapabilityProfileV2,
  capabilityProfileV2Schema,
  type SecondaryObjective,
} from "../../../packages/schemas/scenario-capability.schema";
import {
  actor,
  makeProfile,
  side,
  zone,
} from "../../unit/checkpoint-presence.fixture";

/**
 * Artificial reference identities only. Costs and budgets mirror the
 * Constantinople 380 design study's accounting fixture; they are not gameplay
 * evidence, historical quantities, approved geography, or engine behavior.
 */
export const fixtureIds = {
  plan: "fulfillment-fixture.plan",
  mealService: "fulfillment-fixture.meal-service",
  shelterService: "fulfillment-fixture.shelter-service",
  mealWorker: "fulfillment-fixture.meal-worker",
  shelterWorker: "fulfillment-fixture.shelter-worker",
  mealRecipient: "fulfillment-fixture.meal-recipient",
  householdA: "fulfillment-fixture.household-a",
  householdB: "fulfillment-fixture.household-b",
} as const;

export const recipeIds = {
  mealDirect: "fulfillment-fixture.meal-direct",
  mealHearth: "fulfillment-fixture.meal-shared-hearth",
  mealPurchased: "fulfillment-fixture.meal-purchased",
  shelterMaterials: "fulfillment-fixture.shelter-materials",
  shelterKit: "fulfillment-fixture.shelter-local-kit",
  shelterRented: "fulfillment-fixture.shelter-rented",
} as const;

export const outputIds = {
  mealDirect: "fulfillment-fixture.meal-direct-parcel",
  mealHearth: "fulfillment-fixture.meal-hearth-parcel",
  mealPurchased: "fulfillment-fixture.meal-purchased-parcel",
  shelterMaterials: "fulfillment-fixture.shelter-materials-parcel",
  shelterKit: "fulfillment-fixture.shelter-kit-parcel",
  shelterRented: "fulfillment-fixture.shelter-arrangement-parcel",
} as const;

export const zoneIds = {
  mealReception: "fulfillment-fixture.meal-reception",
  materialsCourt: "fulfillment-fixture.materials-court",
  kitCourt: "fulfillment-fixture.kit-court",
  hostCourt: "fulfillment-fixture.host-court",
  mealDirectSource: "fulfillment-fixture.meal-direct-source",
  hearthWorksite: "fulfillment-fixture.hearth-worksite",
  merchantWorksite: "fulfillment-fixture.merchant-worksite",
  materialsSource: "fulfillment-fixture.materials-source",
  kitWorksite: "fulfillment-fixture.kit-worksite",
  hostWorksite: "fulfillment-fixture.host-worksite",
} as const;

const stockByDifficulty = {
  easy: { food: 420, wood: 380, gold: 260, stone: 0 },
  standard: { food: 340, wood: 280, gold: 150, stone: 0 },
  hard: { food: 300, wood: 220, gold: 120, stone: 0 },
} as const;
export const optionalRewardReserve = {
  food: 400,
  wood: 150,
  gold: 25,
  stone: 0,
} as const;

const recipe = (
  id: string,
  cost: { food: number; wood: number; gold: number; stone: number },
  workerId: string,
  workZoneId: string,
  outputEntityId: string,
  receptionZoneId: string,
  recipientIds: string[],
) => ({
  id,
  cost,
  workerId,
  workZoneId,
  outputEntityId,
  receptionZoneId,
  recipientIds,
});

function optionalObjective(index: number) {
  const id = `fulfillment-fixture.optional-${index}`;
  const base = structuredClone(side(index)) as unknown as SecondaryObjective;
  const kindByIndex = [
    "aid",
    "extract",
    "copy",
    "guide",
    "scout",
    "watch",
    "repair",
  ] as const;
  const kind = kindByIndex[index - 1];
  if (!kind) throw new Error(`Unknown optional fixture ${index}`);
  base.id = id;
  base.kind = kind;
  base.title = { en: kind, "es-ES": kind };
  base.subject = { en: "Reference subject", "es-ES": "Sujeto de referencia" };
  base.rationale = { en: "Artificial fixture", "es-ES": "Fixture artificial" };
  base.text = { en: "Technical reference", "es-ES": "Referencia técnica" };
  base.completionFlag = `${id}.complete`;
  base.world = { entities: [], zones: [] };
  base.predicate = {
    operator: "all",
    requirements: [],
    neverUseTimerInstead: true,
  };
  base.effects = [];
  base.stateContract.persistentLedgers = [
    "arrival-ids",
    "visits",
    "payment-receipts",
    "health-receipts",
    "reward-flags",
  ];
  base.reachability = {
    originHub: "hub",
    receivingHub: "hub",
    corridorIds: [`${id}.corridor`],
    maxRequiredRoundTrips: 1,
    spawnOutsideReceivingZone: true,
    placementGate: "reference fixture only",
  };
  const entity = (suffix: string, role: string) => ({
    ...actor(`${id}.${suffix}`),
    role,
    playerControllable: role !== "damaged-store",
    ...(role === "damaged-store"
      ? { initialHealthFraction: 0.5, damageSource: "fictional prior damage" }
      : {}),
  });
  const sideZone = (suffix: string, x: number) => {
    const coordinate = 12 + index * 26 + x;
    return {
      ...zone(`${id}.${suffix}`, coordinate),
      offsetTiles: [coordinate, 210] as [number, number],
    };
  };
  const arrival = (
    entities: Array<{ id: string }>,
    zones: Array<{ id: string }>,
  ): SecondaryObjective["predicate"]["requirements"][number] =>
    ({
      kind: "entity-arrival",
      entities: entities.map((item) => item.id),
      destinations: Object.fromEntries(
        entities.map((item, i) => [item.id, zones[i % zones.length]?.id ?? ""]),
      ),
      requiredCount: entities.length,
      aliveAtDelivery: true,
      oncePerEntity: true,
      noSubstitutes: true,
      initialPlacementDoesNotCount: true,
    }) as SecondaryObjective["predicate"]["requirements"][number];
  const effect = (
    effectKind:
      | "finite-supply-withdrawal"
      | "unlock-context-and-hint"
      | "mark-alternative-route"
      | "reveal-enemy-approach",
    resources: { food: number; wood: number; gold: number; stone: number },
    extra: Record<string, unknown> = {},
  ) =>
    ({
      kind: effectKind,
      target: `${id}.effect`,
      resources,
      onceFlag: `${id}.rewarded`,
      funding: "reserved-optional-stock",
      changesHistoricalOutcome: false,
      ...extra,
    }) as SecondaryObjective["effects"][number];

  if (kind === "aid" || kind === "extract" || kind === "copy") {
    const roles =
      kind === "aid"
        ? ["aid-crate", "aid-crate"]
        : kind === "extract"
          ? ["evacuee-group", "evacuee-group"]
          : ["source-copy", "source-copy"];
    const entities = roles.map((role, i) => entity(`entity-${i + 1}`, role));
    const zones = [
      sideZone("receiving-zone-a", 0),
      sideZone("receiving-zone-b", 16),
    ];
    base.world = { entities, zones };
    base.predicate.requirements = [arrival(entities, zones)];
    base.effects = [
      kind === "aid"
        ? effect("finite-supply-withdrawal", {
            food: 100,
            wood: 50,
            gold: 0,
            stone: 0,
          })
        : kind === "extract"
          ? effect("finite-supply-withdrawal", {
              food: 100,
              wood: 0,
              gold: 25,
              stone: 0,
            })
          : effect(
              "unlock-context-and-hint",
              { food: 0, wood: 0, gold: 0, stone: 0 },
              {
                sourceIds: ["fixture-source-a", "fixture-source-b"],
                historicalNote: {
                  en: "Technical fixture",
                  "es-ES": "Fixture técnico",
                },
                hint: { en: "Technical hint", "es-ES": "Pista técnica" },
              },
            ),
    ];
  } else if (kind === "guide") {
    const entities = [entity("guide", "local-guide")];
    const zones = [sideZone("junction", 0)];
    base.world = { entities, zones };
    base.predicate.requirements = [arrival(entities, zones)];
    base.effects = [
      effect(
        "mark-alternative-route",
        { food: 0, wood: 0, gold: 0, stone: 0 },
        { corridorId: `${id}.relief` },
      ),
    ];
  } else if (kind === "scout" || kind === "watch") {
    const zones = [sideZone("viewpoint-a", 0), sideZone("viewpoint-b", 16)];
    base.world = { entities: [], zones };
    base.predicate.requirements = [
      {
        kind: "visit-zones",
        zones: zones.map((item) => item.id),
        actor: "any-player-controlled-unit",
        requiredCount: 2,
        observationsPersistent: true,
        countInitialVisibility: false,
      },
    ];
    base.effects = [
      effect(
        "reveal-enemy-approach",
        { food: 0, wood: 0, gold: 0, stone: 0 },
        {
          rosterIds: kind === "scout" ? ["wave-2"] : ["wave-1", "wave-3"],
          alreadyReleasedPolicy:
            "reveal current surviving members; never spawn replacement",
        },
      ),
    ];
  } else {
    const damaged = entity("damaged-store", "damaged-store");
    const zones = [sideZone("store-source", 0)];
    base.world = { entities: [damaged], zones };
    base.predicate.requirements = [
      {
        kind: "entity-health",
        entity: damaged.id,
        health: "full",
        paymentReceipt: `${id}.payment`,
        restoration:
          "atomic 50-wood repair restores full health; no extra engine charge",
      },
      {
        kind: "atomic-payment",
        resources: { wood: 50 },
        receipt: `${id}.payment`,
        afterArrival: false,
        once: true,
        protectedRecoveryCannotBeSpent: true,
      },
    ];
    base.effects = [
      effect("finite-supply-withdrawal", {
        food: 200,
        wood: 100,
        gold: 0,
        stone: 0,
      }),
    ];
  }
  return base;
}

export function makeFulfillmentProfile(): CapabilityProfileV3 {
  const base = structuredClone(makeProfileV2());
  const originals = [
    fixtureIds.mealWorker,
    fixtureIds.shelterWorker,
    fixtureIds.mealRecipient,
    fixtureIds.householdA,
    fixtureIds.householdB,
  ];
  const outputs = Object.values(outputIds);
  const objective = base.objectivePlan[0];
  if (!objective) throw new Error("Missing common main objective");
  objective.entities = originals.map(actor);
  objective.threshold = originals.length;
  objective.countLedger.required = originals.length;
  objective.predicate.requiredCount = originals.length;
  for (const requirement of objective.predicate.requirements) {
    if (
      requirement.kind === "entity-state" &&
      requirement.id === "first-receipt"
    ) {
      requirement.entities = [fixtureIds.mealWorker];
      requirement.destinations = { [fixtureIds.mealWorker]: "store-1" };
    }
    if (requirement.kind === "current-entity-presence") {
      requirement.entities = originals;
      requirement.destinations = {
        [fixtureIds.mealWorker]: "store-1",
        [fixtureIds.shelterWorker]: "store-2",
        [fixtureIds.mealRecipient]: zoneIds.mealReception,
        [fixtureIds.householdA]: zoneIds.materialsCourt,
        [fixtureIds.householdB]: zoneIds.materialsCourt,
      };
      requirement.requiredCount = originals.length;
    }
  }
  const zones = [
    zone(zoneIds.mealReception, 20),
    zone(zoneIds.materialsCourt, 40),
    zone(zoneIds.kitCourt, 60),
    zone(zoneIds.hostCourt, 80),
    zone(zoneIds.mealDirectSource, 140),
    zone(zoneIds.hearthWorksite, 160),
    zone(zoneIds.merchantWorksite, 180),
    zone(zoneIds.materialsSource, 200),
    zone(zoneIds.kitWorksite, 220),
    zone(zoneIds.hostWorksite, 240),
  ];
  const worldContract = {
    ...base.worldContract,
    entities: [...originals.map(actor), ...outputs.map(actor)],
    zones: [...base.worldContract.zones, ...zones],
  };
  const budgetResources = { ...optionalRewardReserve };
  const v2 = capabilityProfileV2Schema.parse({
    ...base,
    worldContract,
    secondaryObjectives: Array.from({ length: 7 }, (_, i) =>
      optionalObjective(i + 1),
    ),
    secondaryBudget: {
      ...base.secondaryBudget,
      reservedRewards: budgetResources,
      reallocatedCacheAllowance: budgetResources,
      maxOptionalCosts: { food: 0, wood: 50, gold: 0, stone: 0 },
    },
  }) satisfies CapabilityProfileV2;
  const profile = capabilityProfileV3Schema.parse({
    ...v2,
    schemaVersion: 3,
    fulfillmentPlan: {
      id: fixtureIds.plan,
      phase: "phase-1",
      services: [
        {
          id: fixtureIds.mealService,
          recipes: [
            recipe(
              recipeIds.mealDirect,
              { food: 240, wood: 40, gold: 0, stone: 0 },
              fixtureIds.mealWorker,
              zoneIds.mealDirectSource,
              outputIds.mealDirect,
              zoneIds.mealReception,
              [fixtureIds.mealRecipient],
            ),
            recipe(
              recipeIds.mealHearth,
              { food: 160, wood: 140, gold: 0, stone: 0 },
              fixtureIds.mealWorker,
              zoneIds.hearthWorksite,
              outputIds.mealHearth,
              zoneIds.mealReception,
              [fixtureIds.mealRecipient],
            ),
            recipe(
              recipeIds.mealPurchased,
              { food: 100, wood: 40, gold: 100, stone: 0 },
              fixtureIds.mealWorker,
              zoneIds.merchantWorksite,
              outputIds.mealPurchased,
              zoneIds.mealReception,
              [fixtureIds.mealRecipient],
            ),
          ],
        },
        {
          id: fixtureIds.shelterService,
          recipes: [
            recipe(
              recipeIds.shelterMaterials,
              { food: 80, wood: 200, gold: 0, stone: 0 },
              fixtureIds.shelterWorker,
              zoneIds.materialsSource,
              outputIds.shelterMaterials,
              zoneIds.materialsCourt,
              [fixtureIds.householdA, fixtureIds.householdB],
            ),
            recipe(
              recipeIds.shelterKit,
              { food: 100, wood: 120, gold: 20, stone: 0 },
              fixtureIds.shelterWorker,
              zoneIds.kitWorksite,
              outputIds.shelterKit,
              zoneIds.materialsCourt,
              [fixtureIds.householdA, fixtureIds.householdB],
            ),
            recipe(
              recipeIds.shelterRented,
              { food: 60, wood: 60, gold: 110, stone: 0 },
              fixtureIds.shelterWorker,
              zoneIds.hostWorksite,
              outputIds.shelterRented,
              zoneIds.materialsCourt,
              [fixtureIds.householdA, fixtureIds.householdB],
            ),
          ],
        },
      ],
    },
  });
  const issues = validateScenarioCapability(profile);
  if (issues.length)
    throw new Error(`Invalid fulfillment fixture: ${JSON.stringify(issues)}`);
  return profile;
}

function makeProfileV2(): CapabilityProfileV2 {
  // Keep the checkpoint fixture's exact legacy v2 shape as the shared core.
  return capabilityProfileV2Schema.parse(makeProfile());
}

export const selection = (
  mealRecipe: string = recipeIds.mealDirect,
  shelterRecipe: string = recipeIds.shelterMaterials,
): FulfillmentSelection => [
  { serviceId: fixtureIds.mealService, recipeId: mealRecipe },
  { serviceId: fixtureIds.shelterService, recipeId: shelterRecipe },
];

export type FixtureDifficulty = keyof typeof stockByDifficulty;
export function accountsFor(difficulty: FixtureDifficulty) {
  return {
    spendable: { ...stockByDifficulty[difficulty] },
    protectedRecovery: { food: 0, wood: 0, gold: 0, stone: 0 },
    optionalReserve: { ...optionalRewardReserve },
  };
}

export const mainOriginalIds = [
  fixtureIds.mealWorker,
  fixtureIds.shelterWorker,
  fixtureIds.mealRecipient,
  fixtureIds.householdA,
  fixtureIds.householdB,
];
export const allOutputIds = outputsForTests();
function outputsForTests() {
  return Object.values(outputIds);
}

export function liveBatch(
  profile: CapabilityProfileV3,
  state: FulfillmentSnapshot,
  sequence: number,
  positions: Record<string, string | null> = {},
  dead: string[] = [],
): LiveSpatialBatch {
  const generated = new Set(state.active?.generated ?? []);
  const recipes = profile.fulfillmentPlan.services.flatMap(
    (service) => service.recipes,
  );
  const unavailable = new Set(
    recipes
      .filter((item) => !generated.has(item.id))
      .map((item) => item.outputEntityId),
  );
  const entities = [
    ...profile.worldContract.entities,
    ...profile.secondaryObjectives.flatMap((item) => item.world.entities),
  ];
  const seen = new Set<string>();
  return {
    sequence,
    entities: entities.flatMap((item) => {
      if (seen.has(item.id) || unavailable.has(item.id)) return [];
      seen.add(item.id);
      const isDead = dead.includes(item.id);
      const position = positions[item.id];
      return [
        {
          entityId: item.id,
          alive: !isDead,
          zones: isDead || position === null ? [] : position ? [position] : [],
        },
      ];
    }),
  };
}

export function enterFulfillment(
  profile: CapabilityProfileV3 = makeFulfillmentProfile(),
  difficulty: FixtureDifficulty = "standard",
): {
  profile: CapabilityProfileV3;
  state: FulfillmentSnapshot;
  context: FulfillmentInputContext;
} {
  const context = createFulfillmentInputContext();
  const initial = createFulfillmentSnapshot(
    profile,
    accountsFor(difficulty),
    difficulty,
  );
  const batch = liveBatch(profile, initial, 0);
  const state = reduceFulfillmentState(
    profile,
    initial,
    {
      type: "shared",
      epoch: context.epoch,
      contractFingerprint: initial.contractFingerprint,
      nowSeconds: 0,
      liveSpatialBatch: batch,
      action: { type: "enter-phase", phase: "phase-1", nowSeconds: 0 },
    },
    context,
  );
  return { profile, state, context };
}

export function fulfillmentCommand(
  profile: CapabilityProfileV3,
  state: FulfillmentSnapshot,
  context: FulfillmentInputContext,
  type: FulfillmentAction["type"],
  overrides: Record<string, unknown> = {},
): FulfillmentAction {
  const sequence = (state.core.liveSpatialObservation?.sequence ?? -1) + 1;
  const options = overrides as {
    positions?: Record<string, string | null>;
    dead?: string[];
    liveSpatialBatch?: LiveSpatialBatch;
    [key: string]: unknown;
  };
  const { positions = {}, dead = [], liveSpatialBatch, ...rest } = options;
  return {
    type,
    epoch: context.epoch,
    contractFingerprint: state.contractFingerprint,
    nowSeconds:
      (state.core.phaseEnteredAtSeconds ?? 0) + state.core.phaseElapsedSeconds,
    liveSpatialBatch:
      liveSpatialBatch ?? liveBatch(profile, state, sequence, positions, dead),
    ...rest,
  } as FulfillmentAction;
}

export function dispatch(
  profile: CapabilityProfileV3,
  state: FulfillmentSnapshot,
  context: FulfillmentInputContext,
  type: FulfillmentAction["type"],
  overrides: Record<string, unknown> = {},
): FulfillmentSnapshot {
  return reduceFulfillmentState(
    profile,
    state,
    fulfillmentCommand(profile, state, context, type, overrides),
    context,
  );
}
