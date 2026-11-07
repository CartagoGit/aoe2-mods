import { z } from "zod";
import {
  fulfillmentIdSchema,
  fulfillmentResourcesSchema,
} from "../schemas/alternative-fulfillment.schema";
import { capabilitySnapshotSchema } from "./capability-snapshot.schema";

export const fulfillmentSelectionSchema = z
  .array(
    z.strictObject({
      serviceId: fulfillmentIdSchema,
      recipeId: fulfillmentIdSchema,
    }),
  )
  .min(1)
  .max(8);
const sequence = z.number().int().safe().nonnegative();
export const fulfillmentSnapshotSchema = z.strictObject({
  schemaVersion: z.literal(3),
  profile: z.literal("composed-world-ledger"),
  contractFingerprint: z.string().regex(/^[a-f0-9]{64}$/),
  planId: fulfillmentIdSchema,
  initialTotal: fulfillmentResourcesSchema,
  core: capabilitySnapshotSchema,
  escrow: fulfillmentResourcesSchema,
  committedExpenditure: fulfillmentResourcesSchema,
  fixedMainExpenditure: fulfillmentResourcesSchema,
  optionalExpenditure: fulfillmentResourcesSchema,
  attemptCounter: sequence,
  revision: sequence,
  active: z
    .strictObject({
      attempt: sequence,
      selection: fulfillmentSelectionSchema,
      status: z.enum(["reserved", "committed"]),
      committedAtSequence: sequence.nullable(),
      committedShares: z.array(
        z.strictObject({
          serviceId: fulfillmentIdSchema,
          recipeId: fulfillmentIdSchema,
          cost: fulfillmentResourcesSchema,
        }),
      ),
      departures: z.record(fulfillmentIdSchema, sequence),
      work: z.record(fulfillmentIdSchema, sequence),
      generated: z.array(fulfillmentIdSchema),
      completedServices: z.array(fulfillmentIdSchema),
    })
    .nullable(),
});
export type FulfillmentSnapshot = z.infer<typeof fulfillmentSnapshotSchema>;
export type FulfillmentSelection = z.infer<typeof fulfillmentSelectionSchema>;
