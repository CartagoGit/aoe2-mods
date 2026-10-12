import { join } from "node:path";
import { z } from "zod";
import { jsonFile, sourceFile, writeJson } from "../core/filesystem.helper";
import type { StringLock } from "../localization/localization.catalog";
import type { Campaign } from "../schemas/campaign.schema";
import { bindNativeTemplate } from "./native-template.adapter";

const manifest = z.strictObject({
  schemaVersion: z.literal(1),
  source: z.string().min(1),
  license: z.string().min(1),
  restrictions: z.array(z.string().min(1)),
  gameBuild: z.string().min(1),
  reviewer: z.string().min(1),
  status: z.enum(["experimental", "game-verified"]),
  narrativeTemplate: z.string().min(1),
  layoutTemplate: z.string().min(1),
  values: z.record(z.string(), z.union([z.string(), z.number()])),
});
/** Las envolturas de slides/layout vienen de la versión objetivo, nunca de un JSON imaginado. */
export async function renderNativeCampaign(
  root: string,
  c: Campaign,
  lock: StringLock,
  output: string,
) {
  const base = `campaigns/${c.id}/native`;
  const m = manifest.parse(
    await jsonFile(await sourceFile(root, `${base}/manifest.json`)),
  );
  for (const [filename, path] of [
    [`${c.internalName}.json`, m.narrativeTemplate],
    [`${c.internalName}_layout.json`, m.layoutTemplate],
  ] as const) {
    const template = await jsonFile(await sourceFile(root, `${base}/${path}`));
    const bound = bindNativeTemplate(template, lock, {
      ...m.values,
      campaignInternalName: c.internalName,
    });
    await writeJson(join(output, filename), bound);
  }
  return {
    status: m.status,
    source: m.source,
    gameBuild: m.gameBuild,
    reviewer: m.reviewer,
  };
}
