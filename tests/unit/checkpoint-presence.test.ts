import { describe, expect, test } from "bun:test";
import { mainRequirementSatisfied } from "../../packages/gameplay-state/capability-predicates.validator";
import { createCapabilitySnapshot } from "../../packages/gameplay-state/capability-snapshot.factory";
import { reduceCapabilityState } from "../../packages/gameplay-state/capability-state.reducer";
import { validateScenarioCapability } from "../../packages/gameplay-validation/scenario-capability.validator";
import { compileCapabilityProfile } from "../../packages/scenario-compiler/capability.compiler";
import type { LiveSpatialBatch } from "../../packages/schemas/live-spatial-batch.schema";
import { capabilityProfileV2Schema } from "../../packages/schemas/scenario-capability.schema";
import {
  destinations,
  makeProfile,
  originalIds,
  zone,
} from "./checkpoint-presence.fixture";

type MutableProfile = {
  objectivePlan: Array<{
    id: string;
    after: string[];
    phase: string;
    predicate: {
      requirements: Array<{ id: string; kind: string; [key: string]: unknown }>;
      requiredLedgers: string[];
    };
  }>;
  stateMachine: {
    states: string[];
    phaseTransitions: Array<{
      from: string;
      to: string;
      on: string;
      objectiveId?: string;
    }>;
  };
  worldContract: { zones: unknown[] };
};

function profileWithCheckpoint() {
  const profile = structuredClone(makeProfile()) as unknown as MutableProfile;
  profile.worldContract.zones.push(zone("other-receiver", 90));
  const first = profile.objectivePlan[0];
  if (!first) throw new Error("Missing fixture objective");
  const presence = first.predicate.requirements.find(
    (req) => req.kind === "current-entity-presence",
  );
  if (!presence || presence.kind !== "current-entity-presence")
    throw new Error("Missing current presence");
  presence.kind = "checkpoint-entity-presence";
  const payment = {
    id: "checkpoint-payment",
    kind: "resource-transaction" as const,
    amounts: { food: 1 },
    receivingZones: ["store-1"],
    allocations: { "store-1": { food: 1 } },
    paidFlag: "checkpoint-paid",
    account: "spendable" as const,
    atomic: true as const,
    once: true as const,
    commit: "atomic",
  };
  first.predicate.requirements.push(payment);
  first.predicate.requiredLedgers.push(payment.id);
  const final = structuredClone(first);
  final.id = "final-return";
  final.after = [first.id];
  final.phase = "phase-2";
  final.predicate.requirements = final.predicate.requirements.filter(
    (req) => req.id !== payment.id,
  );
  final.predicate.requiredLedgers = final.predicate.requiredLedgers.filter(
    (id) => id !== payment.id,
  );
  final.predicate.requirements = final.predicate.requirements.map((req) =>
    req.id === presence.id ? { ...req, kind: "current-entity-presence" } : req,
  );
  profile.objectivePlan.push(final);
  profile.stateMachine.states.push("phase-2");
  profile.stateMachine.phaseTransitions = [
    { from: "briefing", to: "phase-1", on: "intro-accepted" },
    {
      from: "phase-1",
      to: "phase-2",
      on: "objective-latched",
      objectiveId: first.id,
    },
    {
      from: "phase-2",
      to: "victory",
      on: "objective-latched",
      objectiveId: final.id,
    },
  ];
  return capabilityProfileV2Schema.parse(profile);
}

function batch(sequence: number, zones = destinations): LiveSpatialBatch {
  return {
    sequence,
    entities: originalIds.map((entityId) => ({
      entityId,
      alive: true,
      zones: [zones[entityId] ?? ""],
    })),
  };
}

function first(batchValue: LiveSpatialBatch) {
  const entity = batchValue.entities[0];
  if (!entity) throw new Error("Expected fixture entity");
  return entity;
}

function enter(profile: ReturnType<typeof profileWithCheckpoint>) {
  return reduceCapabilityState(
    profile,
    createCapabilitySnapshot(profile, {
      spendable: { food: 20 },
      protectedRecovery: {},
      optionalReserve: {},
    }),
    { type: "enter-phase", phase: "phase-1", nowSeconds: 0 },
  );
}

describe("checkpoint entity presence reference", () => {
  test("strict schema and compiler accept the additive contract at profile v2", () => {
    const profile = profileWithCheckpoint();
    expect(validateScenarioCapability(profile)).toEqual([]);
    expect(compileCapabilityProfile(profile).schemaVersion).toBe(2);
    expect(profile.schemaVersion).toBe(2);
    const fake = structuredClone(profile);
    const req = fake.objectivePlan[0]?.predicate.requirements.find(
      (item) => item.kind === "checkpoint-entity-presence",
    );
    if (!req) throw new Error("Missing checkpoint");
    Object.assign(req, { record: true });
    expect(capabilityProfileV2Schema.safeParse(fake).success).toBe(false);
  });

  test("checkpoint latches once, withdrawal is allowed, final current presence gates both victory APIs", () => {
    const profile = profileWithCheckpoint();
    let state = enter(profile);
    state = reduceCapabilityState(profile, state, {
      type: "pay-main",
      objectiveId: "return",
      requirementId: "checkpoint-payment",
    });
    const oncePaid = state.spendable.food;
    state = reduceCapabilityState(profile, state, {
      type: "pay-main",
      objectiveId: "return",
      requirementId: "checkpoint-payment",
    });
    expect(state.spendable.food).toBe(oncePaid);
    expect(state.paidReceipts).toContain("checkpoint-paid");
    state = reduceCapabilityState(profile, state, {
      type: "record-arrival",
      entityId: "bundle-1",
      zoneId: "store-1",
    });
    state = reduceCapabilityState(profile, state, {
      type: "latch-objective",
      objectiveId: "return",
      liveSpatialBatch: batch(1),
    });
    expect(state.objectiveLatches).toEqual(["return"]);
    const saved = JSON.parse(JSON.stringify(state));
    state = reduceCapabilityState(profile, state, {
      type: "enter-phase",
      phase: "phase-2",
      nowSeconds: 1,
    });
    expect(state.phase).toBe("phase-2");
    const withdrawn = batch(2);
    withdrawn.entities.forEach((item) => {
      item.zones = ["other-receiver"];
    });
    state = reduceCapabilityState(profile, state, {
      type: "observe-live-spatial-batch",
      liveSpatialBatch: withdrawn,
    });
    expect(state.objectiveLatches).toContain("return");
    const finalRequirement =
      profile.objectivePlan[1]?.predicate.requirements.find(
        (req) => req.kind === "current-entity-presence",
      );
    if (!finalRequirement) throw new Error("Missing final requirement");
    expect(
      mainRequirementSatisfied(
        profile,
        state,
        "final-return",
        finalRequirement,
      ),
    ).toBe(false);
    const finalArrived = reduceCapabilityState(profile, state, {
      type: "latch-objective",
      objectiveId: "final-return",
      liveSpatialBatch: batch(3),
    });
    expect(finalArrived.objectiveLatches).toContain("final-return");
    expect(JSON.parse(JSON.stringify(finalArrived))).toEqual(finalArrived);
    expect(
      reduceCapabilityState(profile, finalArrived, {
        type: "tick",
        nowSeconds: 2,
        difficulty: "standard",
        defeatConditions: [],
        victoryConditions: ["final-return"],
        liveSpatialBatch: batch(4),
      }).terminal,
    ).toBe("victory");
    expect(
      reduceCapabilityState(profile, finalArrived, {
        type: "enter-phase",
        phase: "victory",
        nowSeconds: 2,
        liveSpatialBatch: batch(4),
      }).terminal,
    ).toBe("victory");
    expect(
      reduceCapabilityState(profile, saved, {
        type: "enter-phase",
        phase: "victory",
        nowSeconds: 1,
      }).terminal,
    ).toBeNull();
    const finalSaved = JSON.parse(JSON.stringify(finalArrived));
    const movedAfterLatch = batch(4);
    movedAfterLatch.entities.forEach((item) => {
      item.zones = ["other-receiver"];
    });
    expect(
      reduceCapabilityState(profile, finalSaved, {
        type: "enter-phase",
        phase: "victory",
        nowSeconds: 2,
        liveSpatialBatch: movedAfterLatch,
      }).terminal,
    ).toBeNull();
    expect(
      reduceCapabilityState(profile, finalSaved, {
        type: "tick",
        nowSeconds: 2,
        difficulty: "standard",
        defeatConditions: [],
        victoryConditions: ["final-return"],
        liveSpatialBatch: movedAfterLatch,
      }).terminal,
    ).toBeNull();
  });

  test("stale, unknown, dead, lookalike, wrong-zone and premature derivation cannot certify a checkpoint", () => {
    const profile = profileWithCheckpoint();
    const state = enter(profile);
    const latch = (observation: LiveSpatialBatch) =>
      reduceCapabilityState(profile, state, {
        type: "latch-objective",
        objectiveId: "return",
        liveSpatialBatch: observation,
      });
    const stale = batch(0);
    expect(latch(stale).objectiveLatches).toEqual([]);
    const unknown = batch(1);
    first(unknown).entityId = "not-known";
    expect(latch(unknown).objectiveLatches).toEqual([]);
    const dead = batch(1);
    first(dead).alive = false;
    first(dead).zones = [];
    expect(latch(dead).objectiveLatches).toEqual([]);
    const lookalike = batch(1);
    first(lookalike).entityId = "lookalike";
    expect(latch(lookalike).objectiveLatches).toEqual([]);
    const wrong = batch(1);
    first(wrong).zones = ["other-receiver"];
    expect(latch(wrong).objectiveLatches).toEqual([]);
    const recorded = reduceCapabilityState(profile, state, {
      type: "record-predicate",
      objectiveId: "return",
      requirementId: "stores-current",
    });
    expect(recorded.requirementFacts["return.stores-current"]).toBeUndefined();
    const directVictory = structuredClone(profile);
    directVictory.stateMachine.phaseTransitions =
      directVictory.stateMachine.phaseTransitions.map((transition) =>
        transition.objectiveId === "return"
          ? { ...transition, to: "victory" }
          : transition,
      );
    expect(
      validateScenarioCapability(directVictory).some(
        (issue) => issue.code === "capability.checkpoint-presence-terminal",
      ),
    ).toBe(true);

    const protectedProfile = profileWithCheckpoint();
    protectedProfile.worldContract.survivorGroups.push({
      entities: originalIds,
      minimumAliveOrAlreadySafe: 6,
      loss: "defeat",
    });
    const protectedStart = enter(protectedProfile);
    const killed = batch(1);
    first(killed).alive = false;
    first(killed).zones = [];
    expect(
      reduceCapabilityState(protectedProfile, protectedStart, {
        type: "tick",
        nowSeconds: 1,
        difficulty: "standard",
        defeatConditions: [],
        victoryConditions: ["return"],
        liveSpatialBatch: killed,
      }).terminal,
    ).toBe("defeat");
  });

  test("a declared generated identity needs its causal producer before checkpoint latch", () => {
    const profile = profileWithCheckpoint();
    const producer = structuredClone(profile.objectivePlan[0]);
    if (!producer) throw new Error("Missing checkpoint objective");
    producer.id = "producer";
    producer.after = [];
    producer.predicate.requirements = [
      {
        id: "collect-input",
        kind: "entity-state",
        state: "collected",
        entities: ["lookalike"],
        requiredCount: 1,
        oncePerEntity: true,
      },
      {
        id: "derive-custodian",
        kind: "derived-token",
        inputEntities: ["lookalike"],
        outputEntities: ["custodian-1"],
        once: true,
        deriveWhen: "after the named input is collected",
      },
    ];
    producer.predicate.requiredLedgers = ["collect-input", "derive-custodian"];
    profile.objectivePlan.push(producer);
    const parsed = capabilityProfileV2Schema.parse(profile);
    let state = enter(parsed);
    state = reduceCapabilityState(parsed, state, {
      type: "record-arrival",
      entityId: "bundle-1",
      zoneId: "store-1",
    });
    state = reduceCapabilityState(parsed, state, {
      type: "pay-main",
      objectiveId: "return",
      requirementId: "checkpoint-payment",
    });
    state = reduceCapabilityState(parsed, state, {
      type: "latch-objective",
      objectiveId: "return",
      liveSpatialBatch: batch(1),
    });
    expect(state.objectiveLatches).toEqual([]);
    state = reduceCapabilityState(parsed, state, {
      type: "observe-entity-state",
      objectiveId: "producer",
      requirementId: "collect-input",
      entityId: "lookalike",
    });
    state = reduceCapabilityState(parsed, state, {
      type: "derive-token",
      objectiveId: "producer",
      requirementId: "derive-custodian",
    });
    state = reduceCapabilityState(parsed, state, {
      type: "latch-objective",
      objectiveId: "return",
      liveSpatialBatch: batch(2),
    });
    expect(state.objectiveLatches).toContain("return");
  });
});
