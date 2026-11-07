import { type Issue, issue } from "../core/diagnostics.helper";
import type { Catalog } from "../schemas/campaign.schema";
export type GlossaryTerm = {
  id: string;
  locales: Record<string, { preferred: string; forbidden: string[] }>;
};
export function validateGlossary(
  catalogs: Catalog[],
  terms: GlossaryTerm[],
): Issue[] {
  const out: Issue[] = [];
  for (const cat of catalogs)
    for (const term of terms) {
      const entry = term.locales[cat.locale];
      if (!entry) {
        out.push(
          issue(
            "glossary.missing",
            term.id,
            `Término sin forma en ${cat.locale}`,
          ),
        );
        continue;
      }
      for (const [key, text] of Object.entries(cat.strings))
        for (const forbidden of entry.forbidden)
          if (text.toLocaleLowerCase().includes(forbidden.toLocaleLowerCase()))
            out.push(
              issue(
                "glossary.variant",
                `${cat.locale}.${key}`,
                `Usar ${entry.preferred} en lugar de ${forbidden}`,
              ),
            );
    }
  return out;
}
