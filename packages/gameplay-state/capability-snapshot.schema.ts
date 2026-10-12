import { z } from "zod";

const stringList = z
  .array(z.string())
  .refine((items) => new Set(items).size === items.length);

const accountSchema = z.strictObject({
  food: z.number().int().nonnegative(),
  wood: z.number().int().nonnegative(),
  gold: z.number().int().nonnegative(),
  stone: z.number().int().nonnegative(),
});

export const capabilitySnapshotSchema = z.strictObject({
  schemaVersion: z.literal(2),
  profile: z.literal("composed-world-ledger"),
  contractFingerprint: z.string().regex(/^[a-f0-9]{64}$/),
  phase: z.string().min(1),
  phaseEnteredAtSeconds: z.number().nonnegative().nullable(),
  phaseElapsedSeconds: z.number().nonnegative(),
  difficulty: z.enum(["easy", "standard", "hard"]),
  terminal: z.enum(["victory", "defeat"]).nullable(),
  objectiveLatches: stringList,
  requirementFacts: z.record(z.string(), stringList),
  entityStates: z.record(z.string(), z.enum(["alive", "arrived", "destroyed"])),
  arrivedEntities: z.record(z.string(), z.string()),
  arrivalLedger: stringList,
  exportedLedgers: z.record(z.string(), stringList),
  observedEntityStates: z.record(z.string(), stringList),
  zoneConditions: z.record(
    z.string(),
    z.strictObject({
      controlled: z.boolean(),
      passable: z.boolean(),
      protected: z.boolean(),
    }),
  ),
  enteredPhases: stringList,
  visitedZones: stringList,
  forbiddenEntries: stringList,
  paidReceipts: stringList,
  spendable: accountSchema,
  protectedRecovery: accountSchema,
  optionalReserve: accountSchema,
  secondaryStates: z.record(
    z.string(),
    z.enum(["available", "completed", "failed-optional", "closed-at-terminal"]),
  ),
  rewardFlags: stringList,
  releasedRosterIds: stringList,
  resolvedWaves: stringList,
  selectedRoutes: z.record(z.string(), z.string()),
  heldSeconds: z.record(z.string(), z.number().int().nonnegative()),
  deadlineWarnings: stringList,
  departedEntities: stringList,
});

export type CapabilitySnapshot = z.infer<typeof capabilitySnapshotSchema>;
