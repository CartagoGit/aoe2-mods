import { z } from "zod";
import { duplicates } from "../../packages/core/diagnostics.helper";
import { campaignSchema } from "../../packages/schemas/campaign.schema";

export const campaignFileSchema = campaignSchema
  .omit({ scenarios: true })
  .extend({ scenarioFiles: z.array(z.string().min(1)).min(1) });
export const collectionLocales = [
  "en",
  "fr",
  "it",
  "de",
  "ja",
  "ko",
  "pt-BR",
  "ru",
  "zh-Hans",
  "es-LATAM",
  "zh-Hant",
  "tr",
  "vi",
  "es-ES",
  "pl",
  "hi",
  "ms",
] as const;
export const languagesSchema = z
  .strictObject({
    schemaVersion: z.literal(1),
    checked: z.iso.date(),
    source: z.url(),
    targets: z
      .array(
        z.strictObject({
          locale: z.enum(collectionLocales),
          engineFolder: z.string().regex(/^[a-z]+$/),
          folderVerified: z.boolean(),
        }),
      )
      .length(collectionLocales.length),
  })
  .superRefine((config, ctx) => {
    for (const field of ["locale", "engineFolder"] as const)
      for (const value of duplicates(config.targets.map((t) => t[field])))
        ctx.addIssue({
          code: "custom",
          path: ["targets"],
          message: `${field} repetido: ${value}`,
        });
  });
export const engineSchema = z.strictObject({
  schemaVersion: z.literal(1),
  scenarioVersion: z.string(),
  parserVersion: z.string(),
  stringRangeStatus: z.enum(["fixture-only", "verified"]),
  mode: z.literal("aoe2-de"),
  rgeCommit: z.string(),
  difficultyProfiles: z.strictObject({
    easy: z.number().int(),
    standard: z.number().int(),
    hard: z.number().int(),
  }),
  difficultyMappingVerified: z.boolean(),
});
export const lockSchema = z.strictObject({
  schemaVersion: z.literal(1),
  nextId: z.number().int(),
  ids: z.record(z.string(), z.number().int()),
  retired: z.array(z.string()),
});
export const glossarySchema = z.strictObject({
  schemaVersion: z.literal(1),
  terms: z.array(
    z.strictObject({
      id: z.string(),
      locales: z.record(
        z.string(),
        z.strictObject({
          preferred: z.string().min(1),
          forbidden: z.array(z.string().min(1)),
        }),
      ),
    }),
  ),
  policy: z.string(),
});
export const engineCatalogSchema = z.strictObject({
  civilizations: z.array(z.string()),
  units: z.array(z.string()),
  buildings: z.array(z.string()),
  technologies: z.array(z.string()),
  terrains: z.array(z.string()),
});
