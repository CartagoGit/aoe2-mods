import { duplicates, type Issue, issue } from "../core/diagnostics.helper";
import type { Campaign, Catalog } from "../schemas/campaign.schema";

export type StringLock = {
  schemaVersion: 1;
  nextId: number;
  ids: Record<string, number>;
  retired: string[];
};
export const placeholders = (text: string): string[] =>
  [...text.matchAll(/\{([a-zA-Z][a-zA-Z0-9_]*)\}/g)]
    .map((m) => m[1] ?? "")
    .sort();
const markers = (text: string): string[] =>
  [...text.matchAll(/<[^>]+>|%\d?\$?[sd]|\\[nr]/g)].map((m) => m[0]).sort();
export function validateCatalogs(
  catalogs: Catalog[],
  required: string[],
  maxLength = 4000,
  sourceLocale = "en",
): Issue[] {
  const issues: Issue[] = [];
  const base = catalogs.find((c) => c.locale === sourceLocale);
  if (!base)
    return [
      issue("i18n.source", "localization", `Falta ${sourceLocale} canónico`),
    ];
  for (const locale of duplicates(catalogs.map((c) => c.locale)))
    issues.push(issue("i18n.duplicate", locale, "Catálogo repetido"));
  for (const k of required)
    if (!base.strings[k])
      issues.push(issue("i18n.key", k, "Referencia inexistente"));
  for (const cat of catalogs) {
    for (const k of Object.keys(base.strings)) {
      const value = cat.strings[k];
      if (!value) {
        issues.push(
          issue("i18n.missing", `${cat.locale}.${k}`, "Traducción ausente"),
        );
        continue;
      }
      if (
        JSON.stringify(placeholders(value)) !==
        JSON.stringify(placeholders(base.strings[k] ?? ""))
      )
        issues.push(
          issue(
            "i18n.placeholder",
            `${cat.locale}.${k}`,
            "Variables distintas",
          ),
        );
      if (
        JSON.stringify(markers(value)) !==
        JSON.stringify(markers(base.strings[k] ?? ""))
      )
        issues.push(
          issue("i18n.marker", `${cat.locale}.${k}`, "Marcadores distintos"),
        );
      if (value.replace(/\{[a-zA-Z][a-zA-Z0-9_]*\}/g, "").match(/[{}]/))
        issues.push(
          issue("i18n.braces", `${cat.locale}.${k}`, "Marcador mal formado"),
        );
      if (
        value.length > maxLength ||
        Array.from(value).some((c) => {
          const code = c.charCodeAt(0);
          return (
            (code < 32 && ![9, 10, 13].includes(code)) ||
            code === 127 ||
            code === 0xfeff
          );
        })
      )
        issues.push(
          issue(
            "i18n.encoding",
            `${cat.locale}.${k}`,
            "Longitud editorial o carácter de control inválido",
          ),
        );
    }
    for (const k of Object.keys(cat.strings))
      if (!(k in base.strings))
        issues.push(
          issue(
            "i18n.extra",
            `${cat.locale}.${k}`,
            "Clave ajena al catálogo canónico",
          ),
        );
  }
  return issues;
}
export function sourceCatalog(
  c: Pick<Campaign, "sourceLocale" | "localization">,
): Catalog | undefined {
  return c.localization.find((catalog) => catalog.locale === c.sourceLocale);
}
export function campaignKeys(c: Campaign): string[] {
  const keys = [
    c.titleKey,
    c.descriptionKey,
    ...c.recommendedPrevious.flatMap((p) => [p.recommendationKey, p.recapKey]),
  ];
  const lines = [
    ...c.introduction,
    ...c.epilogue,
    ...c.scenarios.flatMap((s) => [
      ...s.narrative.intro,
      ...s.narrative.events,
      ...s.narrative.outro,
    ]),
  ];
  return [
    ...new Set([
      ...keys,
      ...lines.map((l) => l.textKey),
      ...c.scenarios.flatMap((s) => [
        s.titleKey,
        ...Object.values(s.messages).filter((k): k is string => !!k),
        ...s.units.flatMap((u) => (u.nameKey ? [u.nameKey] : [])),
        ...s.factions.flatMap((f) => (f.nameKey ? [f.nameKey] : [])),
        ...s.objectives.map((o) => o.textKey),
      ]),
    ]),
  ].sort();
}
export function validateLock(lock: StringLock): void {
  if (
    lock.schemaVersion !== 1 ||
    !Number.isSafeInteger(lock.nextId) ||
    lock.nextId < 1 ||
    lock.nextId > 2147483647
  )
    throw new Error("Registro de IDs inválido");
  const ids = Object.values(lock.ids);
  if (
    ids.some(
      (id) => !Number.isSafeInteger(id) || id < 1 || id >= lock.nextId,
    ) ||
    new Set(ids).size !== ids.length
  )
    throw new Error("Colisión o ID fuera de rango");
  if (lock.retired.some((k) => !(k in lock.ids)))
    throw new Error("Tombstone sin ID reservado");
}
export function allocate(
  lock: StringLock,
  keys: string[],
  reserved: number[] = [],
): StringLock {
  validateLock(lock);
  const next = structuredClone(lock);
  const used = new Set([...Object.values(next.ids), ...reserved]);
  if (Object.values(next.ids).some((n) => reserved.includes(n)))
    throw new Error("IDs existentes colisionan con recursos externos");
  for (const k of [...new Set(keys)].sort()) {
    if (next.retired.includes(k)) throw new Error(`Clave retirada: ${k}`);
    if (next.ids[k] !== undefined) continue;
    while (used.has(next.nextId)) next.nextId++;
    if (next.nextId >= 2147483647) throw new Error("Registro agotado");
    next.ids[k] = next.nextId;
    used.add(next.nextId++);
  }
  return next;
}
export function exportStrings(catalog: Catalog, lock: StringLock): string {
  validateLock(lock);
  return `${Object.entries(catalog.strings)
    .sort(([a], [b]) => (lock.ids[a] ?? 0) - (lock.ids[b] ?? 0))
    .map(([k, v]) => {
      const id = lock.ids[k];
      if (id === undefined || lock.retired.includes(k))
        throw new Error(`Clave sin ID activo: ${k}`);
      if (placeholders(v).length)
        throw new Error(`Interpolación sin resolver: ${k}`);
      return `${id} ${JSON.stringify(v)}`;
    })
    .join("\n")}\n`;
}
export function interpolate(
  text: string,
  values: Record<string, string>,
): string {
  for (const k of placeholders(text))
    if (values[k] === undefined) throw new Error(`Variable ausente: ${k}`);
  return text.replace(
    /\{([a-zA-Z][a-zA-Z0-9_]*)\}/g,
    (_, k: string) => values[k] ?? "",
  );
}
