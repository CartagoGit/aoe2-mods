import type { LiveSpatialBatch } from "../schemas/live-spatial-batch.schema";
import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";

export type CapabilityAction =
  | {
      type: "observe-entity-state";
      objectiveId: string;
      requirementId: string;
      entityId: string;
    }
  | { type: "derive-token"; objectiveId: string; requirementId: string }
  | {
      type: "observe-zone";
      zoneId: string;
      controlled: boolean;
      passable: boolean;
      protected: boolean;
    }
  | { type: "record-arrival"; entityId: string; zoneId: string }
  | { type: "observe-live-spatial-batch"; liveSpatialBatch: LiveSpatialBatch }
  | { type: "destroy-entity"; entityId: string }
  | { type: "visit-zone"; zoneId: string }
  | { type: "record-predicate"; objectiveId: string; requirementId: string }
  | {
      type: "record-pair";
      objectiveId: string;
      requirementId: string;
      cargoId: string;
      receiverId: string;
    }
  | {
      type: "choose-route";
      objectiveId: string;
      requirementId: string;
      routeId: string;
    }
  | { type: "pay-main"; objectiveId: string; requirementId: string }
  | { type: "pay-secondary"; objectiveId: string; receipt: string }
  | {
      type: "record-secondary-predicate";
      objectiveId: string;
      requirementIndex: number;
      healthFraction: number;
    }
  | { type: "award-secondary"; objectiveId: string }
  | { type: "record-wave-resolved"; waveId: string }
  | { type: "release-wave"; waveId: string }
  | { type: "record-hold"; zoneId: string; elapsedSeconds: number }
  | { type: "record-forbidden-entry"; requirementId: string; actorId: string }
  | {
      type: "record-departure";
      objectiveId: string;
      requirementId: string;
      entityId: string;
    }
  | {
      type: "enter-phase";
      phase: string;
      nowSeconds: number;
      liveSpatialBatch?: LiveSpatialBatch;
    }
  | {
      type: "latch-objective";
      objectiveId: string;
      liveSpatialBatch?: LiveSpatialBatch;
    }
  | {
      type: "tick";
      nowSeconds: number;
      difficulty: "easy" | "standard" | "hard";
      defeatConditions: string[];
      victoryConditions: string[];
      liveSpatialBatch?: LiveSpatialBatch;
    };

export type MainRequirement =
  CapabilityProfileV2["objectivePlan"][number]["predicate"]["requirements"][number];
