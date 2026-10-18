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

const normativePlan = JSON.parse(
  readFileSync(
    new URL(
      "../../../docs/research/odyssey-research/imperial34-care-allocation-plan.json",
      import.meta.url,
    ),
    "utf8",
  ),
) as {
  operatingStockByDifficulty: Record<
    "easy" | "standard" | "hard",
    Record<string, number>
  >;
  services: Array<{
    id: string;
    recipes: Array<{ id: string; cost: Record<string, number> }>;
  }>;
};
const normativeMatrix = JSON.parse(
  readFileSync(
    new URL(
      "../../../docs/qa/alternative-fulfillment/decision/portfolio-matrix.json",
      import.meta.url,
    ),
    "utf8",
  ),
) as {
  initialOptionalRewardReserve: Record<string, number>;
  optionalMechanics: Record<
    string,
    { kind: string; cost: Record<string, number>; reward: Record<string, number> }
  >;
};
const resources = (source: Record<string, number>) => ({
  food: source.food ?? 0,
  wood: source.wood ?? 0,
  gold: source.gold ?? 0,
  stone: source.stone ?? 0,
});
const stockByDifficulty = Object.fromEntries(
  Object.entries(normativePlan.operatingStockByDifficulty).map(
    ([difficulty, stock]) => [difficulty, resources(stock)],
  ),
) as Record<"easy" | "standard" | "hard", ReturnType<typeof resources>>;
export const optionalRewardReserve = resources(
  normativeMatrix.initialOptionalRewardReserve,
);
const recipeCost = (id: string) => {
  const found = normativePlan.services
    .flatMap((service) => service.recipes)
    .find((item) => item.id === id);
  if (!found) throw new Error(`Missing normative recipe cost: ${id}`);
  return resources(found.cost);
};
const optionalMechanics = Object.values(normativeMatrix.optionalMechanics);
const optionalMechanicForKind = (kind: string) =>
  optionalMechanics.find((item) => item.kind === kind);

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
            ...resources(optionalMechanicForKind(kind)?.reward ?? {}),
          })
        : kind === "extract"
          ? effect("finite-supply-withdrawal", {
              ...resources(optionalMechanicForKind(kind)?.reward ?? {}),
            })
          : effect(
              "unlock-context-and-hint",
              resources(optionalMechanicForKind(kind)?.reward ?? {}),
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
        resources(optionalMechanicForKind(kind)?.reward ?? {}),
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
        resources(optionalMechanicForKind(kind)?.reward ?? {}),
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
        resources: resources(
          normativeMatrix.optionalMechanics["damaged-civilian-store"]?.cost ??
            {},
        ),
        receipt: `${id}.payment`,
        afterArrival: false,
        once: true,
        protectedRecoveryCannotBeSpent: true,
      },
    ];
    base.effects = [
      effect("finite-supply-withdrawal", {
        ...resources(
          normativeMatrix.optionalMechanics["damaged-civilian-store"]?.reward ??
            {},
        ),
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
  objective.entities = [fixtureIds.mealRecipient].map(actor);
  objective.threshold = 1;
  objective.countLedger.required = 1;
  objective.predicate.requiredCount = 1;
  for (const requirement of objective.predicate.requirements) {
    if (
      requirement.kind === "entity-state" &&
      requirement.id === "first-receipt"
    ) {
      requirement.entities = [fixtureIds.mealWorker];
      requirement.destinations = { [fixtureIds.mealWorker]: "store-1" };
    }
    if (requirement.kind === "current-entity-presence") {
      requirement.entities = [fixtureIds.mealRecipient];
      requirement.destinations = {
        [fixtureIds.mealRecipient]: zoneIds.mealReception,
      };
      requirement.requiredCount = 1;
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
      maxOptionalCosts: resources(
        normativeMatrix.optionalMechanics["damaged-civilian-store"]?.cost ?? {},
      ),
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
              recipeCost("meal-direct"),
              fixtureIds.mealWorker,
              zoneIds.mealDirectSource,
              outputIds.mealDirect,
              zoneIds.mealReception,
              [fixtureIds.mealRecipient],
            ),
            recipe(
              recipeIds.mealHearth,
              recipeCost("meal-shared-hearth"),
              fixtureIds.mealWorker,
              zoneIds.hearthWorksite,
              outputIds.mealHearth,
              zoneIds.mealReception,
              [fixtureIds.mealRecipient],
            ),
            recipe(
              recipeIds.mealPurchased,
              recipeCost("meal-purchased"),
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
              recipeCost("shelter-materials"),
              fixtureIds.shelterWorker,
              zoneIds.materialsSource,
              outputIds.shelterMaterials,
              zoneIds.materialsCourt,
              [fixtureIds.householdA, fixtureIds.householdB],
            ),
            recipe(
              recipeIds.shelterKit,
              recipeCost("shelter-local-kit"),
              fixtureIds.shelterWorker,
              zoneIds.kitWorksite,
              outputIds.shelterKit,
              zoneIds.kitCourt,
              [fixtureIds.householdA, fixtureIds.householdB],
            ),
            recipe(
              recipeIds.shelterRented,
              recipeCost("shelter-rented"),
              fixtureIds.shelterWorker,
              zoneIds.hostWorksite,
              outputIds.shelterRented,
              zoneIds.hostCourt,
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
      const isDead =
        dead.includes(item.id) ||
        state.core.entityStates[item.id] === "destroyed";
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

import { readFileSync } from "node:fs";
