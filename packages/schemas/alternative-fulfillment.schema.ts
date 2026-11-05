import { z } from "zod";
import { capabilityProfileV2Schema } from "./scenario-capability.schema";

export const fulfillmentIdSchema = z
  .string()
  .regex(/^[a-z0-9][a-z0-9.-]*$/)
  .refine(
    (id) => !Object.hasOwn(Object.prototype, id),
    "Reserved JavaScript object key",
  );
export const fulfillmentResourcesSchema = z.strictObject({
  food: z.number().int().safe().nonnegative(),
  wood: z.number().int().safe().nonnegative(),
  gold: z.number().int().safe().nonnegative(),
  stone: z.number().int().safe().nonnegative(),
});
const recipeSchema = z.strictObject({
  id: fulfillmentIdSchema,
  cost: fulfillmentResourcesSchema,
  workerId: fulfillmentIdSchema,
  workZoneId: fulfillmentIdSchema,
  outputEntityId: fulfillmentIdSchema,
  receptionZoneId: fulfillmentIdSchema,
  recipientIds: z.array(fulfillmentIdSchema).min(1).max(16),
});
export const fulfillmentPlanSchema = z.strictObject({
  id: fulfillmentIdSchema,
  phase: fulfillmentIdSchema,
  services: z
    .array(
      z.strictObject({
        id: fulfillmentIdSchema,
        recipes: z.array(recipeSchema).min(1).max(8),
      }),
    )
    .min(1)
    .max(8),
});

/** Opt-in successor: the strict v2 schema itself is never widened. */
export const capabilityProfileV3Schema = capabilityProfileV2Schema.extend({
  schemaVersion: z.literal(3),
  fulfillmentPlan: fulfillmentPlanSchema,
});
export const capabilityProfileSchema = z.discriminatedUnion("schemaVersion", [
  capabilityProfileV2Schema,
  capabilityProfileV3Schema,
]);
export type CapabilityProfileV3 = z.infer<typeof capabilityProfileV3Schema>;
export type FulfillmentRecipe = z.infer<typeof recipeSchema>;
export type FulfillmentResources = z.infer<typeof fulfillmentResourcesSchema>;
export type CapabilityProfile = z.infer<typeof capabilityProfileSchema>;

/** Explicit projection for shared reference machinery; never a native fallback. */
export function sharedCapabilityProfile(profile: CapabilityProfileV3) {
  const {
    fulfillmentPlan: _plan,
    schemaVersion: _version,
    ...shared
  } = profile;
  return capabilityProfileV2Schema.parse({ ...shared, schemaVersion: 2 });
}
