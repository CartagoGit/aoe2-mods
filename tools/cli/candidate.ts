import { readFile } from "node:fs/promises";
import { canonical, hash, jsonFile, sourceFile } from "../../packages/core";
import type { Campaign } from "../../packages/schemas";
import type { loadProject } from "./project";

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
  ];
  const fileHashes = await Promise.all(
    files.map(async (path) => ({
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
