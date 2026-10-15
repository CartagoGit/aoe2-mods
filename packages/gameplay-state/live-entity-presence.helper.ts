import { isSameOrRequiredPredecessor } from "../gameplay-validation/objective-ancestry.helper";
import {
  type LiveSpatialBatch,
  liveSpatialBatchSchema,
} from "../schemas/live-spatial-batch.schema";
import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";
import type { MainRequirement } from "./capability-action.model";
import { generationReady } from "./capability-generation.helper";
import type { CapabilitySnapshot } from "./capability-snapshot.schema";

type PresenceRequirement = Extract<
  MainRequirement,
  { kind: "current-entity-presence" }
>;

export function profileHasLivePresence(profile: CapabilityProfileV2) {
  return profile.objectivePlan.some((objective) =>
    objective.predicate.requirements.some(
      (req) => req.kind === "current-entity-presence",
    ),
  );
}

export function objectiveHasLivePresence(
  profile: CapabilityProfileV2,
  objectiveId: string,
) {
  return profile.objectivePlan.some(
    (objective) =>
      objective.id === objectiveId &&
      objective.predicate.requirements.some(
        (req) => req.kind === "current-entity-presence",
      ),
  );
}

/** Invalid or stale input is rejected as a whole; it never reuses old membership. */
export function applyLiveSpatialBatch(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  input: LiveSpatialBatch,
): CapabilitySnapshot | null {
  const parsed = liveSpatialBatchSchema.safeParse(input);
  if (!parsed.success || !profileHasLivePresence(profile)) return null;
  const batch = parsed.data;
  const previous = state.liveSpatialObservation;
  if (
    !previous ||
    (previous.sequence !== null && batch.sequence <= previous.sequence)
  )
    return null;
  const knownEntities = new Set([
    ...profile.worldContract.entities.map((entity) => entity.id),
    ...profile.secondaryObjectives.flatMap((objective) =>
      objective.world.entities.map((entity) => entity.id),
    ),
  ]);
  const knownZones = new Set([
    ...profile.worldContract.zones.map((zone) => zone.id),
    ...profile.secondaryObjectives.flatMap((objective) =>
      objective.world.zones.map((zone) => zone.id),
    ),
  ]);
  const observed = new Set<string>();
  const entities: NonNullable<
    CapabilitySnapshot["liveSpatialObservation"]
  >["entities"] = {};
  const entityStates = { ...state.entityStates };
  const secondaryStates = { ...state.secondaryStates };
  for (const item of batch.entities) {
    if (
      !knownEntities.has(item.entityId) ||
      observed.has(item.entityId) ||
      new Set(item.zones).size !== item.zones.length ||
      item.zones.some((zone) => !knownZones.has(zone)) ||
      (!item.alive && item.zones.length > 0) ||
      (item.alive && state.entityStates[item.entityId] === "destroyed")
    )
      return null;
    observed.add(item.entityId);
    entities[item.entityId] = {
      alive: item.alive,
      zones: [...item.zones].sort(),
    };
    if (!item.alive) {
      entityStates[item.entityId] = "destroyed";
      for (const side of profile.secondaryObjectives)
        if (
          secondaryStates[side.id] === "available" &&
          side.predicate.requirements.some(
            (req) =>
              (req.kind === "entity-arrival" &&
                req.entities.includes(item.entityId)) ||
              (req.kind === "entity-health" && req.entity === item.entityId),
          )
        )
          secondaryStates[side.id] = "failed-optional";
    }
  }
  return {
    ...state,
    entityStates,
    secondaryStates,
    liveSpatialObservation: { sequence: batch.sequence, entities },
  };
}

export function livePresenceSatisfied(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  requirement: PresenceRequirement,
) {
  const observed = state.liveSpatialObservation;
  if (!observed || observed.sequence === null) return false;
  return (
    [...new Set(requirement.entities)].filter((id) => {
      const current = observed.entities[id];
      return (
        current?.alive === true &&
        generationReady(profile, state, id) &&
        state.entityStates[id] !== "destroyed" &&
        current.zones.includes(requirement.destinations[id] ?? "")
      );
    }).length >= requirement.requiredCount
  );
}

/** A prior latch never certifies residence at the later victory decision. */
export function livePresenceStillSatisfiedForVictory(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  victoryObjectiveId: string,
) {
  return profile.objectivePlan
    .filter(
      (objective) =>
        state.objectiveLatches.includes(objective.id) &&
        isSameOrRequiredPredecessor(profile, objective.id, victoryObjectiveId),
    )
    .every((objective) =>
      objective.predicate.requirements.every(
        (req) =>
          req.kind !== "current-entity-presence" ||
          livePresenceSatisfied(profile, state, req),
      ),
    );
}

export function victoryNeedsLivePresence(
  profile: CapabilityProfileV2,
  state: CapabilitySnapshot,
  victoryObjectiveId: string,
) {
  return profile.objectivePlan.some(
    (objective) =>
      state.objectiveLatches.includes(objective.id) &&
      isSameOrRequiredPredecessor(profile, objective.id, victoryObjectiveId) &&
      objectiveHasLivePresence(profile, objective.id),
  );
}
