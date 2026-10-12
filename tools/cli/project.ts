import { readdir, readFile } from "node:fs/promises";
import { join } from "node:path";
import { z } from "zod";
import { pythonCommand } from "../../packages/aoe2-adapter";
import {
  validateAssetDestinations,
  validateAssets,
} from "../../packages/assets";
import { validateAudio } from "../../packages/audio";
import { validateCampaign } from "../../packages/campaign-compiler";
import {
  assertValid,
  destinationKey,
  duplicates,
  type Issue,
  issue,
  jsonFile,
  sourceFile,
} from "../../packages/core";
import {
  campaignKeys,
  type StringLock,
  sourceCatalog,
  validateLock,
} from "../../packages/localization";
import {
  type GlossaryTerm,
  validateGlossary,
} from "../../packages/localization/glossary";
import {
  type Campaign,
  campaignSchema,
  scenarioSchema,
} from "../../packages/schemas";
export const campaignFileSchema = campaignSchema
  .omit({ scenarios: true })
  .extend({ scenarioFiles: z.array(z.string().min(1)).min(1) });
export const collectionLocales = [
  "en",
  "fr",
  "it",
  "de",
  "ja",
  "ko",
  "pt-BR",
  "ru",
  "zh-Hans",
  "es-LATAM",
  "zh-Hant",
  "tr",
  "vi",
  "es-ES",
  "pl",
  "hi",
  "ms",
] as const;
export const languagesSchema = z
  .strictObject({
    schemaVersion: z.literal(1),
    checked: z.iso.date(),
    source: z.url(),
    targets: z
      .array(
        z.strictObject({
          locale: z.enum(collectionLocales),
          engineFolder: z.string().regex(/^[a-z]+$/),
          folderVerified: z.boolean(),
        }),
      )
      .length(collectionLocales.length),
  })
  .superRefine((config, ctx) => {
    for (const field of ["locale", "engineFolder"] as const)
      for (const value of duplicates(config.targets.map((t) => t[field])))
        ctx.addIssue({
          code: "custom",
          path: ["targets"],
          message: `${field} repetido: ${value}`,
        });
  });
const engineSchema = z.strictObject({
  schemaVersion: z.literal(1),
  scenarioVersion: z.string(),
  parserVersion: z.string(),
  stringRangeStatus: z.enum(["fixture-only", "verified"]),
  mode: z.literal("aoe2-de"),
  rgeCommit: z.string(),
  difficultyProfiles: z.strictObject({
    easy: z.number().int(),
    standard: z.number().int(),
    hard: z.number().int(),
  }),
  difficultyMappingVerified: z.boolean(),
});
const lockSchema = z.strictObject({
  schemaVersion: z.literal(1),
  nextId: z.number().int(),
  ids: z.record(z.string(), z.number().int()),
  retired: z.array(z.string()),
});
async function campaignMetadata(
  root: string,
  id: string,
  area: "campaigns" | "staging/campaigns",
) {
  if (!/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(id))
    throw new Error("ID de campaña inválido");
  const base = `${area}/${id}`;
  const metadata = campaignFileSchema.parse(
    await jsonFile(await sourceFile(root, `${base}/campaign.json`)),
  );
  if (metadata.id !== id)
    throw new Error("ID y carpeta de campaña no coinciden");
  if (new Set(metadata.scenarioFiles).size !== metadata.scenarioFiles.length)
    throw new Error("scenarioFiles contiene rutas repetidas");
  return { base, metadata };
}
export async function loadCampaign(
  root: string,
  id: string,
): Promise<Campaign> {
  const { base, metadata } = await campaignMetadata(root, id, "campaigns");
  const scenarios = await Promise.all(
    metadata.scenarioFiles.map(async (p) =>
      scenarioSchema.parse(
        await jsonFile(await sourceFile(root, `${base}/${p}`)),
      ),
    ),
  );
  const { scenarioFiles: _, ...rest } = metadata;
  return campaignSchema.parse({ ...rest, scenarios });
}
/** Los borradores parciales nunca forman parte de loadProject ni de un mod. */
export async function inspectStaging(root: string, id: string) {
  const { base, metadata } = await campaignMetadata(
    root,
    id,
    "staging/campaigns",
  );
  const pending: string[] = [];
  const scenarios: Campaign["scenarios"] = [];
  for (const path of metadata.scenarioFiles) {
    let source: string;
    try {
      source = await sourceFile(root, `${base}/${path}`);
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error;
      pending.push(path);
      continue;
    }
    scenarios.push(scenarioSchema.parse(await jsonFile(source)));
  }
  const { scenarioFiles: _, ...rest } = metadata;
  const issues = pending.length
    ? []
    : validateCampaign({ ...rest, scenarios }).issues;
  return { campaign: id, pending, complete: pending.length === 0, issues };
}
export async function loadProject(root: string) {
  const dirs = await readdir(join(root, "campaigns"), { withFileTypes: true });
  const campaigns = await Promise.all(
    dirs.filter((d) => d.isDirectory()).map((d) => loadCampaign(root, d.name)),
  );
  const languages = languagesSchema.parse(
    await jsonFile(join(root, "config/languages.json")),
  );
  const engine = engineSchema.parse(
    await jsonFile(join(root, "config/engine.json")),
  );
  const lock: StringLock = lockSchema.parse(
    await jsonFile(join(root, "config/string-ids.lock.json")),
  );
  validateLock(lock);
  const catalog = z
    .strictObject({
      civilizations: z.array(z.string()),
      units: z.array(z.string()),
      buildings: z.array(z.string()),
      technologies: z.array(z.string()),
      terrains: z.array(z.string()),
    })
    .parse(await jsonFile(join(root, "config/engine-catalog.json")));
  return { campaigns, languages, engine, lock, catalog };
}
export async function validateProject(root: string): Promise<Issue[]> {
  const p = await loadProject(root);
  const glossary = z
    .strictObject({
      schemaVersion: z.literal(1),
      terms: z.array(
        z.strictObject({
          id: z.string(),
          locales: z.record(
            z.string(),
            z.strictObject({
              preferred: z.string().min(1),
              forbidden: z.array(z.string().min(1)),
            }),
          ),
        }),
      ),
      policy: z.string(),
    })
    .parse(await jsonFile(join(root, "config/glossary.json")));
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
export async function docsCheck(root: string): Promise<void> {
  for (const [script, ...args] of [
    ["render.py", "--check"],
    ["verify.py"],
    ["test_design.py"],
  ]) {
    if (!script) throw new Error("Missing design check script");
    const proc = Bun.spawn(
      [
        await pythonCommand(root),
        await sourceFile(root, `tools/design/${script}`),
        ...args,
      ],
      { cwd: root, stdout: "pipe", stderr: "pipe" },
    );
    const [out, err, code] = await Promise.all([
      new Response(proc.stdout).text(),
      new Response(proc.stderr).text(),
      proc.exited,
    ]);
    if (code !== 0)
      throw new Error(`Design check ${script} (${code}): ${err}\n${out}`);
  }
  const mandatory = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "docs/architecture/overview.md",
    "docs/production/plan.md",
    "docs/research/aoe2-capabilities.md",
    "docs/qa/audit.md",
    ...["START", "WORKFLOW", "CONTEXT", "QUALITY-GATES", "NEXT-PROPOSALS"].map(
      (s) => `docs/handoffs/MINIMAX-M3.1-${s}.md`,
    ),
  ];
  for (const path of mandatory) {
    const text = await readFile(await sourceFile(root, path), "utf8");
    if (text.trim().length < 120)
      throw new Error(`Documentación incompleta: ${path}`);
  }
  async function walk(dir: string): Promise<string[]> {
    const entries = await readdir(dir, { withFileTypes: true });
    return (
      await Promise.all(
        entries.map(async (e) =>
          e.isDirectory()
            ? walk(join(dir, e.name))
            : e.name.endsWith(".md")
              ? [join(dir, e.name)]
              : [],
        ),
      )
    ).flat();
  }
  for (const path of await walk(join(root, "docs"))) {
    const text = await readFile(path, "utf8");
    for (const m of text.matchAll(/\]\(([^)]+)\)/g)) {
      const url = m[1] ?? "";
      if (
        !url ||
        url.startsWith("http") ||
        url.startsWith("#") ||
        url.startsWith("mailto:") ||
        url.includes(" ")
      )
        continue;
      const { resolve, dirname } = await import("node:path");
      const target = resolve(dirname(path), url.split("#")[0] ?? url);
      await readFile(target);
    }
  }
}
export function releaseIssues(
  c: Campaign,
  p: Awaited<ReturnType<typeof loadProject>>,
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
export async function requireProject(root: string) {
  assertValid(await validateProject(root));
  return loadProject(root);
}
