import { canonical } from "../core/serialization.helper";
import type {
  CapabilityProfileV3,
  FulfillmentRecipe,
  FulfillmentResources,
} from "../schemas/alternative-fulfillment.schema";
import type { FulfillmentSelection } from "./fulfillment-snapshot.schema";
import { credit, EMPTY_RESOURCES, RESOURCES } from "./resource-accounts.helper";

export const sameResources = (
  left: FulfillmentResources,
  right: FulfillmentResources,
) => RESOURCES.every((resource) => left[resource] === right[resource]);
export const sameValue = (left: unknown, right: unknown) =>
  canonical(left) === canonical(right);

export function selectedRecipes(
  profile: CapabilityProfileV3,
  selection: FulfillmentSelection,
): FulfillmentRecipe[] | null {
  const services = profile.fulfillmentPlan.services;
  if (
    selection.length !== services.length ||
    new Set(selection.map((item) => item.serviceId)).size !== selection.length
  )
    return null;
  const found: FulfillmentRecipe[] = [];
  for (const service of services) {
    const selected = selection.find((item) => item.serviceId === service.id);
    const recipe = service.recipes.find(
      (item) => item.id === selected?.recipeId,
    );
    if (!recipe) return null;
    found.push(recipe);
  }
  return found;
}

export const recipeTotal = (
  recipes: FulfillmentRecipe[],
): FulfillmentResources =>
  recipes.reduce((sum, recipe) => credit(sum, recipe.cost), {
    ...EMPTY_RESOURCES,
  });

export function committedShares(
  profile: CapabilityProfileV3,
  selection: FulfillmentSelection,
) {
  const recipes = selectedRecipes(profile, selection);
  return (
    recipes?.map((recipe, index) => ({
      serviceId: profile.fulfillmentPlan.services[index]?.id ?? "",
      recipeId: recipe.id,
      cost: recipe.cost,
    })) ?? []
  );
}
