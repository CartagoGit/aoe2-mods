import type { ResourceAmounts } from "../schemas/scenario-capability.schema";

export const RESOURCES = ["food", "wood", "gold", "stone"] as const;

export const EMPTY_RESOURCES = { food: 0, wood: 0, gold: 0, stone: 0 };

export const normalizeResources = (amounts: ResourceAmounts) => ({
  food: amounts.food ?? 0,
  wood: amounts.wood ?? 0,
  gold: amounts.gold ?? 0,
  stone: amounts.stone ?? 0,
});

export const enough = (
  balance: Record<(typeof RESOURCES)[number], number>,
  cost: ResourceAmounts,
) => RESOURCES.every((resource) => balance[resource] >= (cost[resource] ?? 0));

export const debit = (
  balance: Record<(typeof RESOURCES)[number], number>,
  cost: ResourceAmounts,
) => {
  const normalized = normalizeResources(cost);
  return Object.fromEntries(
    RESOURCES.map((resource) => [
      resource,
      balance[resource] - normalized[resource],
    ]),
  ) as typeof EMPTY_RESOURCES;
};

export const credit = (
  balance: Record<(typeof RESOURCES)[number], number>,
  amount: ResourceAmounts,
) => {
  const normalized = normalizeResources(amount);
  return Object.fromEntries(
    RESOURCES.map((resource) => [
      resource,
      balance[resource] + normalized[resource],
    ]),
  ) as typeof EMPTY_RESOURCES;
};
