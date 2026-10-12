import { z } from "zod";

export const id = z.string().regex(/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/);
export const key = z.string().regex(/^[a-z][a-z0-9-]*(?:\.[a-z][a-z0-9-]*)+$/);
const text = z.string().trim().min(1);
const unique = <T extends z.ZodType>(item: T) => z.array(item);
export const resources = z.strictObject({
  food: z.number().int().nonnegative(),
  wood: z.number().int().nonnegative(),
  gold: z.number().int().nonnegative(),
  stone: z.number().int().nonnegative(),
});
export const point = z.strictObject({
  x: z.number().int().nonnegative(),
  y: z.number().int().nonnegative(),
});
export const sourceSchema = z.strictObject({
  id,
  kind: z.enum(["primary", "academic", "technical"]),
  title: text,
  url: z.url(),
  locator: text,
  accessed: z.iso.date(),
  license: text,
});
export const claimSchema = z.strictObject({
  id,
  classification: z.enum([
    "documented",
    "disputed",
    "tradition",
    "dramatized",
    "counterfactual",
  ]),
  statement: text,
  sources: z.array(id),
  locator: text,
  qualification: text,
  review: z.enum(["draft", "reviewed", "approved"]),
});
export const narratorSchema = z.strictObject({
  id,
  role: z.enum(["general", "campaign", "character"]),
  identity: text,
  kind: z.enum(["documented", "fictional", "retrospective"]),
  perspective: text,
  register: text,
  age: text,
  pace: text,
  justification: text,
  restrictions: z.array(text),
  voices: z.record(
    z.string(),
    z.strictObject({
      provider: id,
      voice: text,
      accent: text,
      license: text,
      review: z.enum(["draft", "approved"]),
    }),
  ),
});
export const lineSchema = z.strictObject({
  id,
  speaker: id,
  textKey: key,
  claimIds: z.array(id),
  delivery: text,
  imageId: id.optional(),
  audioId: id.optional(),
  durationSeconds: z.number().positive(),
});
const baseConditions = [
  z.strictObject({
    type: z.literal("timer"),
    seconds: z.number().int().positive(),
  }),
  z.strictObject({ type: z.literal("destroy"), unit: id }),
  z.strictObject({
    type: z.literal("variable"),
    variable: id,
    value: z.number().int(),
  }),
  z.strictObject({
    type: z.literal("bring"),
    unit: id,
    from: point,
    to: point,
  }),
  z.strictObject({
    type: z.literal("resource"),
    faction: id,
    resource: z.enum(["food", "wood", "gold", "stone"]),
    amount: z.number().int().positive(),
  }),
] as const;
export const conditionSchema = z.discriminatedUnion("type", baseConditions);
export const objectiveSchema = z.strictObject({
  id,
  textKey: key,
  kind: z.enum(["main", "secondary"]),
  requires: z.array(id),
  completion: conditionSchema,
  location: point,
});
export const factionSchema = z.strictObject({
  id,
  player: z.number().int().min(1).max(8),
  civilization: id,
  nameKey: key.optional(),
  justification: text,
  claimIds: z.array(id),
  role: z.enum(["human", "enemy", "ally"]),
  economy: z.strictObject({
    model: z.enum(["standard", "finite-reserve", "scripted"]),
    initial: resources,
    supply: text,
    production: z.array(text),
    reserve: z.number().int().nonnegative(),
  }),
  aiScript: text.optional(),
  strategy: z.strictObject({
    goals: z.array(text).min(1),
    mobilization: text,
    reactions: z.array(text),
    limits: text,
    retreat: text,
  }),
  reinforcements: z.array(
    z.strictObject({
      id,
      origin: text,
      cause: text,
      counterplay: text,
      maxWaves: z.number().int().min(1).max(100),
      unitsPerWave: z.number().int().min(1).max(500),
      intervalSeconds: z.number().int().positive(),
      totalBudget: z.number().int().positive(),
    }),
  ),
});
export const balanceSchema = z.strictObject({
  easy: z.strictObject({
    resources,
    enemyReactionSeconds: z.number().int().positive(),
    hints: z.boolean(),
  }),
  standard: z.strictObject({
    resources,
    enemyReactionSeconds: z.number().int().positive(),
    hints: z.boolean(),
  }),
  hard: z.strictObject({
    resources,
    enemyReactionSeconds: z.number().int().positive(),
    hints: z.boolean(),
  }),
});
export const eventSchema = z.strictObject({
  id,
  conditions: z
    .array(
      z.discriminatedUnion("type", [
        ...baseConditions,
        z.strictObject({ type: z.literal("objective"), objective: id }),
      ]),
    )
    .min(1),
  effects: z
    .array(
      z.discriminatedUnion("type", [
        z.strictObject({
          type: z.literal("set-variable"),
          variable: id,
          value: z.number().int(),
        }),
        z.strictObject({ type: z.literal("line"), line: id }),
        z.strictObject({
          type: z.literal("diplomacy"),
          source: id,
          target: id,
          state: z.enum(["ally", "neutral", "enemy"]),
          mutual: z.boolean(),
        }),
        z.strictObject({
          type: z.literal("tribute"),
          source: id,
          target: id,
          resource: z.enum(["food", "wood", "gold", "stone"]),
          amount: z.number().int().positive(),
        }),
        z.strictObject({ type: z.literal("task"), unit: id, target: id }),
        z.strictObject({
          type: z.literal("spawn"),
          reinforcement: id,
          faction: id,
          unitType: id,
          count: z.number().int().positive().max(500),
          position: point,
        }),
      ]),
    )
    .min(1),
});
export const scenarioSchema = z.strictObject({
  schemaVersion: z.literal(1),
  id: z.string().regex(/^[0-9]{2}-[a-z][a-z0-9-]*$/),
  titleKey: key,
  messages: z
    .partialRecord(
      z.enum(["instructions", "hints", "victory", "loss", "history", "scouts"]),
      key,
    )
    .default({}),
  period: text,
  date: text,
  location: text,
  claimIds: z.array(id),
  characters: z.array(id),
  mechanic: z.enum([
    "battle",
    "siege",
    "diplomacy",
    "trade",
    "escort",
    "survival",
    "naval",
    "defense",
    "civil-war",
    "economy",
    "intrigue",
  ]),
  secondaryMechanics: z.array(text),
  map: z.strictObject({
    width: z.number().int().min(16).max(480),
    height: z.number().int().min(16).max(480),
    blocked: z.array(point),
    baseTerrain: id.default("grass-1"),
    tiles: z
      .array(
        z.strictObject({
          position: point,
          terrain: id,
          elevation: z.number().int().min(0).max(7),
        }),
      )
      .default([]),
    start: point,
    geography: text,
  }),
  units: z.array(
    z.strictObject({
      id,
      faction: id,
      type: id,
      nameKey: key.optional(),
      position: point,
      essential: z.boolean(),
    }),
  ),
  factions: z.array(factionSchema).min(1),
  objectives: z.array(objectiveSchema).min(1),
  victory: z.strictObject({
    objectives: z.array(id).min(1),
    progressKey: key.optional(),
    routes: z
      .array(
        z.strictObject({
          id,
          objectives: z.array(id).min(1),
          progressKey: key,
        }),
      )
      .default([]),
  }),
  defeat: z.strictObject({
    essentialUnits: z.array(id),
    timeoutSeconds: z.number().int().positive().optional(),
    arbitration: z.literal("defeat-first"),
  }),
  variables: z.array(z.strictObject({ id, initial: z.number().int() })),
  balance: balanceSchema,
  narrative: z.strictObject({
    intro: z.array(lineSchema).min(1),
    events: z.array(lineSchema),
    outro: z.array(lineSchema).min(1),
  }),
  technologies: z.array(id),
  triggers: z.array(eventSchema).default([]),
  rewards: z.array(text),
  dependencies: z.array(text),
  media: z.array(id),
  qa: z
    .array(
      z.strictObject({
        id,
        steps: z.array(text).min(1),
        expected: text,
        severity: z.enum(["blocking", "major", "minor"]),
        status: z.enum(["pending", "passed", "failed"]),
        evidence: text,
      }),
    )
    .min(1),
  metrics: z.strictObject({
    basis: z.enum(["estimated", "measured"]),
    durationMinutes: z.tuple([z.number().positive(), z.number().positive()]),
    stagnation: text,
    alternativeRoutes: text,
  }),
});
export const catalogSchema = z.strictObject({
  locale: text,
  status: z.enum(["draft", "translated", "reviewed", "approved"]),
  reviewer: text,
  strings: z.record(key, text),
});
export const assetSchema = z.strictObject({
  id,
  kind: z.enum(["image", "audio", "map"]),
  description: text,
  path: text,
  enginePath: text.optional(),
  origin: z.enum(["public-domain", "cc0", "licensed", "original", "generated"]),
  creator: text,
  url: z.url(),
  license: text,
  restrictions: z.array(text),
  obtained: z.iso.date(),
  locale: text.optional(),
  lineId: id.optional(),
  campaigns: z.array(id),
  prompt: text.optional(),
  model: text.optional(),
  review: z.enum(["draft", "approved"]),
  format: z.enum(["png", "wav", "json"]),
  width: z.number().int().positive().optional(),
  height: z.number().int().positive().optional(),
  sha256: z.string().regex(/^[a-f0-9]{64}$/),
  cost: z.number().nonnegative(),
});
export const evidenceSchema = z.strictObject({
  id,
  result: z.enum(["pending", "passed", "failed"]),
  gameBuild: text,
  platform: text,
  artifactSha256: text,
  reviewer: text,
  notes: text,
});
export const campaignSchema = z.strictObject({
  schemaVersion: z.literal(1),
  id,
  publicId: z.string().regex(/^CDF-[A-Z]+\d{2}$/),
  internalName: z.string().regex(/^CDF_[A-Za-z0-9_]+$/),
  sourceLocale: text,
  titleKey: key,
  descriptionKey: key,
  mode: z.enum(["aoe2-de", "return-of-rome"]),
  status: z.enum(["fixture", "draft", "reviewed", "release"]),
  recommendedPrevious: z.array(
    z.strictObject({
      campaignId: id,
      internalName: text,
      endingKey: key,
      recommendationKey: key,
      recapKey: key,
    }),
  ),
  enforceRequirement: z.literal(false),
  generalNarrator: narratorSchema,
  campaignNarrator: narratorSchema,
  characters: unique(narratorSchema),
  sources: z.array(sourceSchema),
  claims: z.array(claimSchema),
  introduction: z.array(lineSchema).min(1),
  epilogue: z.array(lineSchema).min(1),
  scenarios: z.array(scenarioSchema).min(1),
  localization: z.array(catalogSchema).min(1),
  assets: z.array(assetSchema),
  editorial: z.strictObject({
    neutrality: text,
    sensitiveDepictions: text,
    anachronisms: text,
    review: z.enum(["draft", "approved"]),
    reviewer: text,
  }),
  compatibility: z.array(evidenceSchema),
});
export type Campaign = z.infer<typeof campaignSchema>;
export type Scenario = z.infer<typeof scenarioSchema>;
export type Catalog = z.infer<typeof catalogSchema>;
export type Asset = z.infer<typeof assetSchema>;
export type Narrator = z.infer<typeof narratorSchema>;
export type Line = z.infer<typeof lineSchema>;
export const schemas = {
  campaign: campaignSchema,
  scenario: scenarioSchema,
  asset: assetSchema,
  narrator: narratorSchema,
};
