import { duplicates, type Issue, issue } from "../core";
import type { Campaign } from "../schemas";
export function validateHistory(c: Campaign): Issue[] {
  const issues: Issue[] = [];
  const sources = new Map(c.sources.map((s) => [s.id, s]));
  const claims = new Map(c.claims.map((s) => [s.id, s]));
  for (const id of duplicates(c.sources.map((s) => s.id)))
    issues.push(issue("history.source-duplicate", id, "Fuente duplicada"));
  for (const id of duplicates(c.claims.map((s) => s.id)))
    issues.push(issue("history.claim-duplicate", id, "Afirmación duplicada"));
  for (const claim of c.claims) {
    if (
      ["documented", "disputed", "tradition"].includes(claim.classification) &&
      !claim.sources.length
    )
      issues.push(
        issue("history.evidence", claim.id, "Falta evidencia localizada"),
      );
    for (const source of claim.sources)
      if (!sources.has(source))
        issues.push(
          issue("history.source", claim.id, `Fuente desconocida: ${source}`),
        );
  }
  const references = [
    ...c.scenarios.flatMap((s) => [
      { id: s.id, refs: s.claimIds },
      ...s.factions.map((f) => ({ id: f.id, refs: f.claimIds })),
    ]),
    ...[
      ...c.introduction,
      ...c.epilogue,
      ...c.scenarios.flatMap((s) => [
        ...s.narrative.intro,
        ...s.narrative.events,
        ...s.narrative.outro,
      ]),
    ].map((l) => ({ id: l.id, refs: l.claimIds })),
  ];
  for (const { id, refs } of references)
    for (const ref of refs)
      if (!claims.has(ref))
        issues.push(
          issue("history.claim", id, `Afirmación inexistente: ${ref}`),
        );
  if (c.status !== "fixture" && !c.claims.length)
    issues.push(
      issue("history.empty", c.id, "Campaña histórica sin afirmaciones"),
    );
  return issues;
}
