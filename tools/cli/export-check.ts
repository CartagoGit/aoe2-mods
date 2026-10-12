import { mkdir, rm } from "node:fs/promises";
import { join } from "node:path";
import { runAdapter } from "../../packages/aoe2-adapter";
import {
  compileCampaign,
  validateCampaign,
} from "../../packages/campaign-compiler";
import { assertValid, writeJson } from "../../packages/core";
import type { StringLock } from "../../packages/localization";
import type { Campaign } from "../../packages/schemas";
export async function exportVariants(
  root: string,
  fixture: Campaign,
  lock: StringLock,
) {
  const testRoot = join(root, "build/export-variants");
  await rm(testRoot, { recursive: true, force: true });
  await mkdir(testRoot, { recursive: true });
  const variant = structuredClone(fixture);
  const s = variant.scenarios[0];
  if (
    !s?.factions[0] ||
    !s.factions[1] ||
    !s.units[0] ||
    !s.units[1] ||
    !s.objectives[1]
  )
    throw new Error("Fixture incompleto");
  s.units.push({
    ...s.units[1],
    id: "enemy-alternate",
    position: { x: 23, y: 23 },
  });
  s.objectives.push({
    ...s.objectives[1],
    id: "alternate",
    completion: { type: "destroy", unit: "enemy-alternate" },
  });
  s.victory = {
    objectives: ["prepare"],
    routes: [
      {
        id: "route-a",
        objectives: ["defeat-guard"],
        progressKey: "progress.technical-pilot.route-a",
      },
      {
        id: "route-b",
        objectives: ["alternate"],
        progressKey: "progress.technical-pilot.route-b",
      },
    ],
  };
  s.narrative.events.push({
    id: "event-line",
    speaker: variant.campaignNarrator.id,
    textKey: s.narrative.intro[0]?.textKey ?? variant.titleKey,
    claimIds: [],
    delivery: "Neutral",
    durationSeconds: 3,
  });
  s.factions[1].reinforcements = [
    {
      id: "reserve",
      origin: "Reserva inicial",
      cause: "Evento finito",
      counterplay: "Defender acceso",
      maxWaves: 1,
      unitsPerWave: 1,
      intervalSeconds: 10,
      totalBudget: 1,
    },
  ];
  s.triggers = [
    {
      id: "bounded-event",
      conditions: [
        { type: "timer", seconds: 10 },
        {
          type: "bring",
          unit: "guard",
          from: { x: 0, y: 0 },
          to: { x: 31, y: 31 },
        },
        {
          type: "resource",
          faction: s.factions[0]?.id ?? "player",
          resource: "gold",
          amount: 50,
        },
      ],
      effects: [
        { type: "line", line: "event-line" },
        {
          type: "diplomacy",
          source: s.factions[0]?.id ?? "player",
          target: "enemy",
          state: "neutral",
          mutual: true,
        },
        {
          type: "tribute",
          source: s.factions[0]?.id ?? "player",
          target: "enemy",
          resource: "gold",
          amount: 50,
        },
        { type: "set-variable", variable: "choice", value: 1 },
        { type: "task", unit: "enemy-guard", target: "guard" },
        {
          type: "spawn",
          faction: "enemy",
          unitType: "militia",
          reinforcement: "reserve",
          count: 1,
          position: { x: 22, y: 22 },
        },
      ],
    },
  ];
  s.messages = Object.fromEntries(
    ["instructions", "hints", "victory", "loss", "history", "scouts"].map(
      (field) => [field, s.titleKey],
    ),
  );
  s.units[0].nameKey = s.titleKey;
  s.factions[0].nameKey = variant.titleKey;
  s.technologies = ["loom"];
  s.map.tiles = [{ position: { x: 1, y: 1 }, terrain: "dirt-1", elevation: 1 }];
  assertValid(validateCampaign(variant).issues);
  const irPath = join(testRoot, "routes-ir.json");
  await writeJson(irPath, compileCampaign(variant, lock));
  await runAdapter(root, ["build", irPath, join(testRoot, "routes")]);
  s.factions[1].economy.model = "scripted";
  s.factions[1].aiScript = "(defrule (true) => (disable-self))";
  await writeJson(irPath, compileCampaign(variant, lock));
  await runAdapter(root, ["build", irPath, join(testRoot, "custom-ai")]);
  const unsupported = compileCampaign(variant, lock);
  unsupported.mode = "return-of-rome";
  await writeJson(irPath, unsupported);
  let failed = false;
  try {
    await runAdapter(root, ["build", irPath, join(testRoot, "unsupported")]);
  } catch (e) {
    failed = String(e).includes("Return of Rome pendiente");
  }
  if (!failed) throw new Error("Return of Rome no se rechazó explícitamente");
  return {
    variants: 3,
    roundTrips: 2,
    unsupportedModeRejected: true,
    gameVerified: false,
  };
}
