import { z } from "zod";
import { liveSpatialBatchSchema } from "../schemas/live-spatial-batch.schema";
import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";

const id = z.string();
const observation = { liveSpatialBatch: liveSpatialBatchSchema.optional() };
export const capabilityActionSchema = z.discriminatedUnion("type", [
  z.strictObject({
    type: z.literal("observe-entity-state"),
    objectiveId: id,
    requirementId: id,
    entityId: id,
  }),
  z.strictObject({
    type: z.literal("derive-token"),
    objectiveId: id,
    requirementId: id,
  }),
  z.strictObject({
    type: z.literal("observe-zone"),
    zoneId: id,
    controlled: z.boolean(),
    passable: z.boolean(),
    protected: z.boolean(),
  }),
  z.strictObject({
    type: z.literal("record-arrival"),
    entityId: id,
    zoneId: id,
  }),
  z.strictObject({
    type: z.literal("observe-live-spatial-batch"),
    liveSpatialBatch: liveSpatialBatchSchema,
  }),
  z.strictObject({ type: z.literal("destroy-entity"), entityId: id }),
  z.strictObject({ type: z.literal("visit-zone"), zoneId: id }),
  z.strictObject({
    type: z.literal("record-predicate"),
    objectiveId: id,
    requirementId: id,
  }),
  z.strictObject({
    type: z.literal("record-pair"),
    objectiveId: id,
    requirementId: id,
    cargoId: id,
    receiverId: id,
  }),
  z.strictObject({
    type: z.literal("choose-route"),
    objectiveId: id,
    requirementId: id,
    routeId: id,
  }),
  z.strictObject({
    type: z.literal("pay-main"),
    objectiveId: id,
    requirementId: id,
  }),
  z.strictObject({
    type: z.literal("pay-secondary"),
    objectiveId: id,
    receipt: id,
  }),
  z.strictObject({
    type: z.literal("record-secondary-predicate"),
    objectiveId: id,
    requirementIndex: z.number(),
    healthFraction: z.number(),
  }),
  z.strictObject({ type: z.literal("award-secondary"), objectiveId: id }),
  z.strictObject({ type: z.literal("record-wave-resolved"), waveId: id }),
  z.strictObject({ type: z.literal("release-wave"), waveId: id }),
  z.strictObject({
    type: z.literal("record-hold"),
    zoneId: id,
    elapsedSeconds: z.number(),
  }),
  z.strictObject({
    type: z.literal("record-forbidden-entry"),
    requirementId: id,
    actorId: id,
  }),
  z.strictObject({
    type: z.literal("record-departure"),
    objectiveId: id,
    requirementId: id,
    entityId: id,
  }),
  z.strictObject({
    type: z.literal("enter-phase"),
    phase: id,
    nowSeconds: z.number(),
    ...observation,
  }),
  z.strictObject({
    type: z.literal("latch-objective"),
    objectiveId: id,
    ...observation,
  }),
  z.strictObject({
    type: z.literal("tick"),
    nowSeconds: z.number(),
    difficulty: z.enum(["easy", "standard", "hard"]),
    defeatConditions: z.array(id),
    victoryConditions: z.array(id),
    ...observation,
  }),
]);
export type CapabilityAction = z.infer<typeof capabilityActionSchema>;

export type MainRequirement =
  CapabilityProfileV2["objectivePlan"][number]["predicate"]["requirements"][number];
