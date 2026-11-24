import { join } from "node:path";
import {
  validateAssetDestinations,
  validateAssets,
} from "../../packages/assets/assets.validator";
import { validateAudio } from "../../packages/audio/audio.pipeline";
import { validateCampaign } from "../../packages/campaign-compiler/campaign.compiler";
import {
  assertValid,
  duplicates,
  type Issue,
  issue,
} from "../../packages/core/diagnostics.helper";
import {
  destinationKey,
  jsonFile,
} from "../../packages/core/filesystem.helper";
import {
  type GlossaryTerm,
  validateGlossary,
} from "../../packages/localization/glossary.validator";
import {
  campaignKeys,
  sourceCatalog,
} from "../../packages/localization/localization.catalog";
import { loadProject } from "./project.loader";
import { glossarySchema } from "./project-config.schema";

export async function validateProject(root: string): Promise<Issue[]> {
  const p = await loadProject(root);
  const glossary = glossarySchema.parse(
    await jsonFile(join(root, "config/glossary.json")),
  );
  const out: Issue[] = [];
  const reservedPaths = [
    ...p.languages.targets.map(
      (t) =>
        `resources/${t.engineFolder}/strings/key-value/key-value-modded-strings-utf8.txt`,
    ),
    ...p.campaigns.flatMap((c) =>
      [
        `${c.internalName}.aoe2campaign`,
        `${c.internalName}.json`,
        `${c.internalName}_layout.json`,
      ].map((name) => `resources/_common/campaign/${name}`),
    ),
  ];
  for (const path of duplicates(reservedPaths.map(destinationKey)))
    out.push(
      issue(
        "project.native-destination",
        path,
        "Campañas con archivos nativos coincidentes",
      ),
    );
  out.push(
    ...validateAssetDestinations(
      p.campaigns.map((c) => ({ owner: c.id, assets: c.assets })),
      reservedPaths,
    ),
  );
  for (const c of p.campaigns) {
    out.push(
      ...validateGlossary(c.localization, glossary.terms as GlossaryTerm[]),
    );
    for (const cat of c.localization)
      if (!p.languages.targets.some((t) => t.locale === cat.locale))
        out.push(issue("i18n.target", cat.locale, "Locale no registrado"));

    out.push(
      ...validateCampaign(c).issues,
      ...(await validateAssets(root, c.assets)),
    );
    for (const a of c.assets.filter((a) => a.kind === "audio"))
      try {
        await validateAudio(root, a.path);
      } catch (e) {
        out.push(issue("audio.file", a.id, String(e)));
      }
    for (const s of c.scenarios) {
      for (const terrain of [
        s.map.baseTerrain,
        ...s.map.tiles.map((t) => t.terrain),
      ])
        if (!p.catalog.terrains.includes(terrain))
          out.push(
            issue("engine.terrain", s.id, `Terreno desconocido ${terrain}`),
          );
      for (const f of s.factions)
        if (!p.catalog.civilizations.includes(f.civilization))
          out.push(
            issue(
              "engine.civilization",
              f.id,
              `Civilización desconocida ${f.civilization}`,
            ),
          );
      for (const t of s.technologies)
        if (!p.catalog.technologies.includes(t))
          out.push(
            issue("engine.technology", s.id, `Tecnología desconocida ${t}`),
          );
      for (const trigger of s.triggers)
        for (const effect of trigger.effects)
          if (
            effect.type === "spawn" &&
            ![...p.catalog.units, ...p.catalog.buildings].includes(
              effect.unitType,
            )
          )
            out.push(
              issue(
                "engine.spawn",
                trigger.id,
                `Unidad desconocida ${effect.unitType}`,
              ),
            );
      for (const u of s.units)
        if (![...p.catalog.units, ...p.catalog.buildings].includes(u.type))
          out.push(issue("engine.unit", u.id, `Unidad desconocida ${u.type}`));
    }
    for (const k of campaignKeys(c))
      if (p.lock.ids[k] === undefined)
        out.push(issue("ids.unallocated", k, "Ejecuta bun run ids:allocate"));
  }
  for (const [kind, values] of [
    ["internalName", p.campaigns.map((c) => c.internalName)],
    ["publicId", p.campaigns.map((c) => c.publicId)],
  ] as const)
    for (const dup of duplicates([...values]))
      out.push(issue("project.id", dup, `${kind} duplicado`));
  const owners = new Map<string, string>();
  for (const c of p.campaigns)
    for (const key of Object.keys(sourceCatalog(c)?.strings ?? {})) {
      const owner = owners.get(key);
      if (owner && owner !== c.id)
        out.push(
          issue(
            "project.key",
            key,
            `Clave compartida entre ${owner} y ${c.id}`,
          ),
        );
      owners.set(key, c.id);
    }
  return out;
}

export async function requireProject(root: string) {
  assertValid(await validateProject(root));
  return loadProject(root);
}
