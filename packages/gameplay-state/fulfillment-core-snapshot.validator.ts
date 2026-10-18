import type { CapabilityProfileV2 } from "../schemas/scenario-capability.schema";
import { computeExportedLedgers, factKey } from "./capability-ledgers.helper";
import { secondaryRequirementsSatisfied } from "./capability-predicates.validator";
import type { CapabilitySnapshot } from "./capability-snapshot.schema";
import { sameValue } from "./fulfillment-plan.helper";

/** Semantic checks for a v3-owned shared snapshot. V2 loading is unchanged. */
export function validateFulfillmentCore(
  profile: CapabilityProfileV2,
  core: CapabilitySnapshot,
) {
  const fail = (detail: string): never => {
    throw new Error(`fulfillment.snapshot-invalid: ${detail}`);
  };
  const phases = new Set(profile.stateMachine.states);
  if (
    !core.liveSpatialObservation ||
    (core.liveSpatialObservation.sequence === null &&
      Object.keys(core.liveSpatialObservation.entities).length > 0)
  )
    fail("live observation envelope");
  const entities = new Set([
    ...profile.worldContract.entities.map((entity) => entity.id),
    ...profile.secondaryObjectives.flatMap((side) =>
      side.world.entities.map((entity) => entity.id),
    ),
  ]);
  const zones = new Set([
    ...profile.worldContract.zones.map((zone) => zone.id),
    ...profile.secondaryObjectives.flatMap((side) =>
      side.world.zones.map((zone) => zone.id),
    ),
  ]);
  const objectives = new Set(
    profile.objectivePlan.map((objective) => objective.id),
  );
  const sides = new Set(profile.secondaryObjectives.map((side) => side.id));
  const subset = (values: string[], known: Set<string>, detail: string) => {
    if (values.some((value) => !known.has(value))) fail(detail);
  };
  if (
    !phases.has(core.phase) ||
    (core.terminal !== null && core.phase !== core.terminal) ||
    (core.terminal === null && ["victory", "defeat"].includes(core.phase))
  )
    fail("phase/terminal lifecycle");
  subset(core.enteredPhases, phases, "entered phase identity");
  if (
    !core.terminal &&
    (!core.enteredPhases.includes(core.phase) ||
      (core.phase !== "briefing" && core.phaseEnteredAtSeconds === null))
  )
    fail("active phase lifecycle");
  subset(core.objectiveLatches, objectives, "objective latch identity");
  if (Object.keys(core.secondaryStates).length !== sides.size)
    fail("secondary membership");
  subset(Object.keys(core.secondaryStates), sides, "secondary identity");
  if (
    core.terminal &&
    Object.values(core.secondaryStates).includes("available")
  )
    fail("terminal optional lifecycle");
  subset(
    Object.keys(core.arrivedEntities),
    entities,
    "arrived entity identity",
  );
  subset(Object.values(core.arrivedEntities), zones, "arrival zone identity");
  subset(core.visitedZones, zones, "visited zone identity");
  subset(core.departedEntities, entities, "departed identity");
  subset(Object.keys(core.zoneConditions), zones, "zone condition identity");
  subset(Object.keys(core.heldSeconds), zones, "held zone identity");
  subset(Object.keys(core.observedEntityStates), entities, "observed identity");
  const observedStates = new Set([
    "collected",
    "prepared",
    "registered-after-arrival",
    "repaired-to-full-health",
    "sealed-and-delivered",
    "alive-and-held",
  ]);
  for (const values of Object.values(core.observedEntityStates))
    subset(values, observedStates, "observed state identity");
  for (const entry of core.arrivalLedger) {
    const parts = entry.split("|");
    if (
      parts.length !== 3 ||
      !phases.has(parts[0] ?? "") ||
      !entities.has(parts[1] ?? "") ||
      !zones.has(parts[2] ?? "")
    )
      fail("arrival ledger identity");
  }
  if (!sameValue(core.exportedLedgers, computeExportedLedgers(profile, core)))
    fail("exported ledger derivation");
  const facts = new Map<string, Set<string>>();
  const routes = new Map<string, Set<string>>();
  const warnings = new Set<string>();
  const forbidden = new Set<string>();
  for (const objective of profile.objectivePlan)
    for (const req of objective.predicate.requirements) {
      const key = factKey(objective.id, req.id);
      let values: string[] = [];
      if (req.kind === "entity-state") values = req.entities;
      else if (req.kind === "area-state") values = req.zones;
      else if (req.kind === "derived-token") values = req.outputEntities;
      else if (req.kind === "paired-delivery")
        values = req.pairs.map((pair) => `${pair.cargo}:${pair.receiver}`);
      else if (req.kind === "resource-transaction") {
        values = [req.paidFlag];
        if (
          core.paidReceipts.includes(req.paidFlag) !==
          (core.requirementFacts[key]?.includes(req.paidFlag) === true)
        )
          fail("fixed payment receipt");
      } else if (req.kind === "ordered-departure")
        values = req.departingEntities;
      if (req.kind === "route-choice")
        routes.set(key, new Set(req.allowedRoutes.map((route) => route.id)));
      if (req.kind === "phase-deadline") warnings.add(key);
      if (req.kind === "forbidden-entry")
        for (const id of entities) forbidden.add(`${key}:${id}`);
      facts.set(key, new Set(values));
    }
  for (const side of profile.secondaryObjectives) {
    const completed = core.secondaryStates[side.id] === "completed";
    if (completed && !secondaryRequirementsSatisfied(profile, core, side.id))
      fail("unearned optional completion");
    facts.set(factKey(side.id, "completed"), new Set([side.completionFlag]));
    if (
      completed !==
      (core.requirementFacts[factKey(side.id, "completed")]?.includes(
        side.completionFlag,
      ) ===
        true)
    )
      fail("optional completion receipt");
    for (const effect of side.effects)
      if (completed !== core.rewardFlags.includes(effect.onceFlag))
        fail("optional reward receipt");
    side.predicate.requirements.forEach((req, index) => {
      facts.set(
        factKey(side.id, `requirement-${index}`),
        new Set(
          req.kind === "visit-zones"
            ? req.zones
            : req.kind === "entity-arrival"
              ? req.entities
              : req.kind === "entity-health"
                ? [req.entity]
                : [],
        ),
      );
      if (
        completed &&
        req.kind === "atomic-payment" &&
        !core.paidReceipts.includes(req.receipt)
      )
        fail("optional payment receipt");
    });
  }
  for (const [key, values] of Object.entries(core.requirementFacts)) {
    const allowed = facts.get(key);
    if (!allowed) fail("requirement fact identity");
    subset(values, allowed ?? new Set(), "requirement fact member");
  }
  subset(
    core.rewardFlags,
    new Set(
      profile.secondaryObjectives.flatMap((side) =>
        side.effects.map((effect) => effect.onceFlag),
      ),
    ),
    "reward identity",
  );
  for (const [key, value] of Object.entries(core.selectedRoutes))
    if (!routes.get(key)?.has(value)) fail("route identity");
  subset(core.deadlineWarnings, warnings, "deadline identity");
  subset(core.forbiddenEntries, forbidden, "forbidden-entry identity");
  subset(
    core.releasedRosterIds,
    new Set(
      profile.enemyRoster.mobilizations.flatMap((wave) => wave.entityIds),
    ),
    "roster identity",
  );
  subset(
    core.resolvedWaves,
    new Set(profile.enemyRoster.mobilizations.map((wave) => wave.id)),
    "wave identity",
  );
}
