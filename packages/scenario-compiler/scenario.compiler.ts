import { assertValid } from "../core/diagnostics.helper";
import { validateGameplay } from "../gameplay-validation/gameplay.validator";
import type { StringLock } from "../localization/localization.catalog";
import type { Scenario } from "../schemas/campaign.schema";
export function compileScenario(s: Scenario, lock: StringLock) {
  assertValid(validateGameplay(s));
  const textId = (key: string): number => {
    const id = lock.ids[key];
    if (id === undefined) throw new Error(`ID ausente: ${key}`);
    return id;
  };
  return {
    schemaVersion: 1 as const,
    scenario: s,
    titleId: textId(s.titleKey),
    messageIds: Object.fromEntries(
      Object.entries(s.messages)
        .filter((entry): entry is [string, string] => !!entry[1])
        .map(([field, key]) => [field, textId(key)]),
    ),
    unitNameIds: Object.fromEntries(
      s.units
        .filter((u) => u.nameKey)
        .map((u) => [u.id, textId(u.nameKey as string)]),
    ),
    factionNameIds: Object.fromEntries(
      s.factions
        .filter((f) => f.nameKey)
        .map((f) => [f.id, textId(f.nameKey as string)]),
    ),
    objectiveIds: Object.fromEntries(
      s.objectives.map((o) => [o.id, textId(o.textKey)]),
    ),
    lineIds: Object.fromEntries(
      [...s.narrative.intro, ...s.narrative.events, ...s.narrative.outro].map(
        (l) => [l.id, textId(l.textKey)],
      ),
    ),
    terminalVariable: "cdf-terminal",
    objectiveVariables: Object.fromEntries(
      s.objectives.map((o, i) => [o.id, i + 1]),
    ),
    arbitration: "defeat-first" as const,
  };
}
export type ScenarioIR = ReturnType<typeof compileScenario>;
