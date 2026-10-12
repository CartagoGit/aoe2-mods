import { validateCampaign } from "../../packages/campaign-compiler/campaign.compiler";
import { jsonFile, sourceFile } from "../../packages/core/filesystem.helper";
import type { Campaign } from "../../packages/schemas/campaign.schema";
import { scenarioSchema } from "../../packages/schemas/campaign.schema";
import { campaignMetadata } from "./project.loader";

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
