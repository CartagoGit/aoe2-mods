import { assertValid, duplicates, type Issue, issue } from "../core";
import { validateGameplay, validateVariety } from "../gameplay-validation";
import { validateHistory } from "../historical-validation";
import {
  campaignKeys,
  type StringLock,
  validateCatalogs,
} from "../localization";
import { compileScenario } from "../scenario-compiler";
import { type Campaign, campaignSchema } from "../schemas";
export function validateCampaign(input: unknown): {
  campaign: Campaign;
  issues: Issue[];
} {
  const c = campaignSchema.parse(input);
  const issues = [
    ...validateHistory(c),
    ...validateCatalogs(c.localization, campaignKeys(c)),
    ...c.scenarios.flatMap(validateGameplay),
    ...validateVariety(c),
  ];
  for (const id of duplicates(c.scenarios.map((s) => s.id)))
    issues.push(issue("campaign.scenario-duplicate", id, "Escenario repetido"));
  const speakers = [c.generalNarrator, c.campaignNarrator, ...c.characters];
  const speakerIds = new Set(speakers.map((s) => s.id));
  for (const id of duplicates(speakers.map((s) => s.id)))
    issues.push(issue("narrative.identity", id, "Voz o personaje duplicado"));
  if (
    c.generalNarrator.role !== "general" ||
    c.campaignNarrator.role !== "campaign"
  )
    issues.push(issue("narrative.role", c.id, "Roles de narrador incorrectos"));
  const lines = [
    ...c.introduction,
    ...c.epilogue,
    ...c.scenarios.flatMap((s) => [
      ...s.narrative.intro,
      ...s.narrative.events,
      ...s.narrative.outro,
    ]),
  ];
  for (const id of duplicates(lines.map((l) => l.id)))
    issues.push(
      issue("narrative.line-duplicate", id, "Intervención duplicada"),
    );
  for (const l of lines) {
    if (!speakerIds.has(l.speaker))
      issues.push(issue("narrative.speaker", l.id, "Narrador desconocido"));
    for (const ref of [l.imageId, l.audioId].filter((x): x is string => !!x))
      if (!c.assets.some((a) => a.id === ref))
        issues.push(
          issue("narrative.asset", l.id, `Recurso inexistente ${ref}`),
        );
  }
  for (const l of lines) {
    const image = c.assets.find((a) => a.id === l.imageId);
    const audio = c.assets.find((a) => a.id === l.audioId);
    if (image && image.kind !== "image")
      issues.push(
        issue(
          "narrative.asset-kind",
          l.id,
          "Imagen apunta a otro tipo de recurso",
        ),
      );
    if (audio && (audio.kind !== "audio" || audio.lineId !== l.id))
      issues.push(
        issue(
          "narrative.asset-kind",
          l.id,
          "Audio no corresponde a esta intervención",
        ),
      );
  }
  for (const a of c.assets)
    if (!a.campaigns.includes(c.id))
      issues.push(
        issue("assets.owner", a.id, "Campaña fuera del alcance del recurso"),
      );
  for (const s of c.scenarios) {
    for (const ch of s.characters)
      if (!speakerIds.has(ch))
        issues.push(
          issue("narrative.character", s.id, `Personaje desconocido ${ch}`),
        );
    for (const a of s.media)
      if (!c.assets.some((asset) => asset.id === a))
        issues.push(issue("game.media", s.id, `Recurso inexistente ${a}`));
  }
  if (c.status !== "fixture") {
    if (
      !c.introduction.some((l) => l.speaker === c.generalNarrator.id) ||
      !c.introduction.some((l) => l.speaker === c.campaignNarrator.id)
    )
      issues.push(
        issue(
          "narrative.structure",
          c.id,
          "Presentación general y del narrador particular obligatoria",
        ),
      );
    for (const s of c.scenarios)
      for (const field of [
        "instructions",
        "hints",
        "victory",
        "loss",
        "history",
        "scouts",
      ] as const)
        if (!s.messages[field])
          issues.push(issue("i18n.panel", s.id, `Falta panel ${field}`));
    for (const s of c.scenarios)
      if (
        !s.narrative.intro.some((l) => l.speaker === c.campaignNarrator.id) ||
        !s.narrative.outro.some((l) => l.speaker === c.campaignNarrator.id)
      )
        issues.push(
          issue(
            "narrative.structure",
            s.id,
            "Intro y epílogo del narrador particular obligatorios",
          ),
        );
  }
  if (c.recommendedPrevious.some((p) => p.campaignId === c.id))
    issues.push(issue("progress.self", c.id, "Predecesora autorreferencial"));
  return { campaign: c, issues };
}
export function compileCampaign(c: Campaign, lock: StringLock) {
  assertValid(validateCampaign(c).issues);
  return {
    schemaVersion: 1 as const,
    id: c.id,
    internalName: c.internalName,
    mode: c.mode,
    titleId: lock.ids[c.titleKey],
    scenarios: c.scenarios.map((s) => compileScenario(s, lock)),
  };
}
export function recommendation(
  previous: { internalName: string; endingKey: string },
  read: (campaign: string, key: string) => number | undefined,
): boolean {
  return (read(previous.internalName, previous.endingKey) ?? 0) <= 0;
}
