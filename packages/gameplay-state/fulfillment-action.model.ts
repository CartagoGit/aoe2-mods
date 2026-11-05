import { z } from "zod";
import { fulfillmentResourcesSchema } from "../schemas/alternative-fulfillment.schema";
import { liveSpatialBatchSchema } from "../schemas/live-spatial-batch.schema";
import { capabilityActionSchema } from "./capability-action.model";
import { fulfillmentSelectionSchema } from "./fulfillment-snapshot.schema";

const counter = z.number().int().safe().nonnegative();
const common = {
  epoch: z.string().uuid(),
  contractFingerprint: z.string().regex(/^[a-f0-9]{64}$/),
  nowSeconds: z.number().finite().nonnegative(),
  liveSpatialBatch: liveSpatialBatchSchema,
};
const attempt = { attempt: counter, revision: counter };
const qualified = { ...attempt, serviceId: z.string(), recipeId: z.string() };
// This is an authoritative adapter event, not a player-supplied account/fact API.
export const fulfillmentActionSchema = z.discriminatedUnion("type", [
  z.strictObject({
    type: z.literal("reserve"),
    ...common,
    ...attempt,
    selection: fulfillmentSelectionSchema,
    expectedSpendable: fulfillmentResourcesSchema,
  }),
  z.strictObject({ type: z.literal("cancel"), ...common, ...attempt }),
  z.strictObject({ type: z.literal("commit"), ...common, ...attempt }),
  z.strictObject({
    type: z.literal("depart-for-work"),
    ...common,
    ...qualified,
  }),
  z.strictObject({ type: z.literal("record-work"), ...common, ...qualified }),
  z.strictObject({
    type: z.literal("generate-output"),
    ...common,
    ...qualified,
  }),
  z.strictObject({
    type: z.literal("complete-service"),
    ...common,
    ...qualified,
  }),
  z.strictObject({ type: z.literal("observe"), ...common }),
  z.strictObject({
    type: z.literal("shared"),
    ...common,
    action: capabilityActionSchema,
  }),
]);
export type FulfillmentAction = z.infer<typeof fulfillmentActionSchema>;
export type FulfillmentInputContext = { readonly epoch: string };
