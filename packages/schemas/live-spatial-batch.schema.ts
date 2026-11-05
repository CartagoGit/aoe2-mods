import { z } from "zod";

const contractId = z.string().regex(/^[a-z0-9][a-z0-9.-]*$/);

/** Trusted future observer input: memberships are current, not arrival receipts. */
export const liveSpatialBatchSchema = z.strictObject({
  sequence: z.number().int().safe().nonnegative(),
  entities: z.array(
    z.strictObject({
      entityId: contractId,
      alive: z.boolean(),
      zones: z.array(contractId),
    }),
  ),
});

export type LiveSpatialBatch = z.infer<typeof liveSpatialBatchSchema>;
