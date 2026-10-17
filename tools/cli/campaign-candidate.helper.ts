import { readdir, readFile } from "node:fs/promises";
import { jsonFile, sourceFile } from "../../packages/core/filesystem.helper";
import { canonical, hash } from "../../packages/core/serialization.helper";
import type { Campaign } from "../../packages/schemas/campaign.schema";
import type { loadProject } from "./project.loader";

/** El QA/editorial no altera el artefacto; textos, gameplay, medios y plantillas sí. */
export async function candidateFingerprint(
  root: string,
  c: Campaign,
  project: Awaited<ReturnType<typeof loadProject>>,
) {
  const base = `campaigns/${c.id}/native`;
  const manifest = await jsonFile(
    await sourceFile(root, `${base}/manifest.json`),
  );
  const m = manifest as { narrativeTemplate: string; layoutTemplate: string };
  if (
    typeof m.narrativeTemplate !== "string" ||
    typeof m.layoutTemplate !== "string"
  )
    throw new Error("Plantillas nativas no declaradas");
  const files = [
    `${base}/manifest.json`,
    `${base}/${m.narrativeTemplate}`,
    `${base}/${m.layoutTemplate}`,
    "tools/python/export_aoe2.py",
    "config/toolchain.json",
    "config/engine.json",
    "package.json",
    "bun.lock",
    "requirements.lock.txt",
  ];
  async function sources(directory: string): Promise<string[]> {
    const entries = await readdir(await sourceFile(root, directory), {
      withFileTypes: true,
    });
    return (
      await Promise.all(
        entries.map(async (entry) => {
          const path = `${directory}/${entry.name}`;
          if (entry.isSymbolicLink())
            throw new Error(`Generador enlazado no permitido: ${path}`);
          if (entry.isDirectory()) return sources(path);
          return /\.(?:ts|py)$/.test(entry.name) ? [path] : [];
        }),
      )
    ).flat();
  }
  files.push(
    ...(
      await Promise.all(["packages", "tools/cli", "tools/python"].map(sources))
    ).flat(),
  );
  const fileHashes = await Promise.all(
    [...new Set(files)].sort().map(async (path) => ({
      path,
      sha256: hash(await readFile(await sourceFile(root, path))),
    })),
  );
  return hash(
    canonical({
      id: c.id,
      internalName: c.internalName,
      mode: c.mode,
      titleKey: c.titleKey,
      recommendedPrevious: c.recommendedPrevious,
      introduction: c.introduction,
      epilogue: c.epilogue,
      scenarios: c.scenarios.map(({ qa: _, ...s }) => s),
      catalogs: c.localization.map(({ locale, strings }) => ({
        locale,
        strings,
      })),
      assets: c.assets.map(({ id, path, sha256, enginePath }) => ({
        id,
        path,
        sha256,
        enginePath,
      })),
      ids: project.lock.ids,
      targets: project.languages.targets.map(({ locale, engineFolder }) => ({
        locale,
        engineFolder,
      })),
      fileHashes,
    }),
  );
}
