import { type Issue, issue } from "../../packages/core/diagnostics.helper";
import type { Campaign } from "../../packages/schemas/campaign.schema";
import type { Project } from "./project.loader";

export function releaseIssues(
  c: Campaign,
  p: Project,
  artifactSha256?: string,
): Issue[] {
  const out: Issue[] = [];
  if (!artifactSha256)
    out.push(
      issue(
        "release.artifact",
        c.id,
        "Falta ZIP candidato con hash verificable",
      ),
    );
  const allLines = [
    ...c.introduction,
    ...c.epilogue,
    ...c.scenarios.flatMap((s) => [
      ...s.narrative.intro,
      ...s.narrative.events,
      ...s.narrative.outro,
    ]),
  ];
  for (const line of allLines) {
    if (!line.imageId)
      out.push(issue("release.visual", line.id, "Falta imagen narrativa"));
    for (const locale of p.languages.targets)
      if (
        !c.assets.some(
          (a) =>
            a.kind === "audio" &&
            a.lineId === line.id &&
            a.locale === locale.locale &&
            a.review === "approved",
        )
      )
        out.push(
          issue(
            "release.audio",
            `${line.id}.${locale.locale}`,
            "Audio localizado aprobado ausente",
          ),
        );
  }
  if (c.status !== "release")
    out.push(issue("release.status", c.id, "No aprobada para release"));
  if (
    p.engine.stringRangeStatus !== "verified" ||
    !p.engine.difficultyMappingVerified
  )
    out.push(
      issue(
        "release.engine",
        c.id,
        "Rango de IDs/dificultad pendientes de prueba",
      ),
    );
  for (const target of p.languages.targets) {
    const cat = c.localization.find((l) => l.locale === target.locale);
    if (!cat || cat.status !== "approved")
      out.push(
        issue("release.language", target.locale, "Traducción no aprobada"),
      );
    if (!target.folderVerified)
      out.push(
        issue(
          "release.folder",
          target.locale,
          "Carpeta del motor no comprobada",
        ),
      );
    for (const n of [c.generalNarrator, c.campaignNarrator, ...c.characters])
      if (n.voices[target.locale]?.review !== "approved")
        out.push(
          issue(
            "release.voice",
            `${n.id}.${target.locale}`,
            "Reparto vocal no aprobado",
          ),
        );
  }
  if (
    c.editorial.review !== "approved" ||
    c.claims.some((cl) => cl.review !== "approved")
  )
    out.push(
      issue("release.history", c.id, "Revisión histórica/editorial pendiente"),
    );
  for (const a of c.assets)
    if (a.review !== "approved")
      out.push(issue("release.asset", a.id, "Recurso sin aprobar"));
  for (const a of c.assets)
    if (!a.enginePath)
      out.push(
        issue(
          "release.asset-path",
          a.id,
          "Ruta nativa del recurso sin acreditar",
        ),
      );
  for (const s of c.scenarios)
    for (const test of s.qa)
      if (test.status !== "passed")
        out.push(
          issue(
            "release.qa",
            `${s.id}.${test.id}`,
            "Caso de juego no superado",
          ),
        );
  const required = [
    "game-load",
    "save-load",
    "progress-cross-campaign",
    "multi-mod-i18n",
    "difficulty",
    "slideshow",
    "audio",
  ];
  for (const id of required) {
    const e = c.compatibility.find((e) => e.id === id);
    if (
      !e ||
      e.result !== "passed" ||
      !/^[a-f0-9]{64}$/.test(e.artifactSha256) ||
      e.artifactSha256 !== artifactSha256 ||
      e.reviewer === "Pendiente"
    )
      out.push(
        issue(
          "release.evidence",
          id,
          "Falta evidencia de juego vinculada al artefacto",
        ),
      );
  }
  return out;
}
