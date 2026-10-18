import { duplicates, type Issue, issue } from "../core/diagnostics.helper";
import { profileHasLivePresence } from "../gameplay-state/live-entity-presence.helper";
import { RESOURCES } from "../gameplay-state/resource-accounts.helper";
import {
  type CapabilityProfileV3,
  sharedCapabilityProfile,
} from "../schemas/alternative-fulfillment.schema";

/** Additional v3 checks; the caller also validates the shared v2 contract. */
export function validateAlternativeFulfillment(
  profile: CapabilityProfileV3,
): Issue[] {
  const plan = profile.fulfillmentPlan;
  const out: Issue[] = [];
  const add = (message: string) =>
    out.push(issue("fulfillment.contract", plan.id, message));
  const recipes = plan.services.flatMap((service) => service.recipes);
  const outputs = recipes.map((recipe) => recipe.outputEntityId);
  const originals = recipes.flatMap((recipe) => [
    recipe.workerId,
    ...recipe.recipientIds,
  ]);
  const entities = new Map(
    profile.worldContract.entities.map((entity) => [entity.id, entity]),
  );
  const zones = new Map(
    profile.worldContract.zones.map((zone) => [zone.id, zone]),
  );
  if (
    !profile.stateMachine.states.includes(plan.phase) ||
    ["briefing", "victory", "defeat"].includes(plan.phase)
  )
    add("Plan must activate in a declared nonterminal work phase");
  if (!profileHasLivePresence(sharedCapabilityProfile(profile)))
    add("Shared profile must support authoritative live spatial batches");
  if (
    plan.services.reduce(
      (count, service) => count * service.recipes.length,
      1,
    ) > 4096
  )
    add("At most 4096 complete selections supported");
  for (const ids of [
    plan.services.map((service) => service.id),
    recipes.map((recipe) => recipe.id),
    outputs,
  ])
    if (duplicates(ids).length)
      add("Service, recipe and output IDs must each be unique");
  if (outputs.some((id) => originals.includes(id)))
    add("An output cannot be an original worker or recipient");
  const workers = plan.services.map(
    (service) => new Set(service.recipes.map((recipe) => recipe.workerId)),
  );
  if (
    workers.some((set, index) =>
      workers.some(
        (other, otherIndex) =>
          index !== otherIndex && [...set].some((id) => other.has(id)),
      ),
    )
  )
    add(
      "First reference implementation requires distinct workers across services",
    );
  for (const recipe of recipes) {
    if (
      !entities.has(recipe.workerId) ||
      recipe.recipientIds.some((id) => !entities.has(id)) ||
      !entities.has(recipe.outputEntityId)
    )
      add(`Unknown main-world identity in ${recipe.id}`);
    if (duplicates(recipe.recipientIds).length)
      add(`Duplicate recipient in ${recipe.id}`);
    const source = zones.get(recipe.workZoneId);
    const reception = zones.get(recipe.receptionZoneId);
    if (!source || !reception || source.id === reception.id)
      add(`Work and reception must use distinct declared zones: ${recipe.id}`);
    if (
      source &&
      reception &&
      source.hub === reception.hub &&
      Math.hypot(
        source.offsetTiles[0] - reception.offsetTiles[0],
        source.offsetTiles[1] - reception.offsetTiles[1],
      ) <=
        source.radiusTiles + reception.radiusTiles
    )
      add(`Work and reception footprints overlap: ${recipe.id}`);
  }
  for (const resource of RESOURCES) {
    const maximum = plan.services.reduce(
      (sum, service) =>
        sum +
        Math.max(...service.recipes.map((recipe) => recipe.cost[resource])),
      0,
    );
    if (!Number.isSafeInteger(maximum))
      add(`Selection cost can overflow ${resource}`);
  }
  // An output has one producer. Shared ledgers must not bypass this producer.
  const sharedReferences = JSON.stringify({
    objectives: profile.objectivePlan,
    secondaries: profile.secondaryObjectives,
    survivors: profile.worldContract.survivorGroups,
    enemies: profile.enemyRoster,
  });
  if (outputs.some((id) => sharedReferences.includes(JSON.stringify(id))))
    add(
      "Recipe outputs cannot also occur in shared predicates, optional worlds, survivor groups or enemy rosters",
    );
  return out;
}
