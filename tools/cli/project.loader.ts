import { readdir } from "node:fs/promises";
import { join } from "node:path";
import { jsonFile, sourceFile } from "../../packages/core/filesystem.helper";
import {
  type StringLock,
  validateLock,
} from "../../packages/localization/localization.catalog";
import {
  type Campaign,
  campaignSchema,
  scenarioSchema,
} from "../../packages/schemas/campaign.schema";
import {
  campaignFileSchema,
  engineCatalogSchema,
  engineSchema,
  languagesSchema,
  lockSchema,
} from "./project-config.schema";

export async function campaignMetadata(
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
  const catalog = engineCatalogSchema.parse(
    await jsonFile(join(root, "config/engine-catalog.json")),
  );
  return { campaigns, languages, engine, lock, catalog };
}

export type Project = Awaited<ReturnType<typeof loadProject>>;
