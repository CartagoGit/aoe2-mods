import { expect, test } from "bun:test";
import { cp, mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { writeJson } from "../../packages/core/filesystem.helper";
import { hash } from "../../packages/core/serialization.helper";
import type { Campaign } from "../../packages/schemas/campaign.schema";
import {
  inspectStaging,
  loadCampaign,
  loadProject,
  validateProject,
} from "../../tools/cli/project.helper";

const source = resolve(import.meta.dir, "../..");
const fixture = await loadCampaign(source, "technical-pilot");
async function writeCampaign(
  root: string,
  area: string,
  c: Campaign,
  scenarios = true,
) {
  const { scenarios: missions, ...metadata } = c;
  const scenarioFiles = missions.map((s) => `scenarios/${s.id}/scenario.json`);
  await writeJson(join(root, area, c.id, "campaign.json"), {
    ...metadata,
    scenarioFiles,
  });
  if (scenarios)
    for (const [index, scenario] of missions.entries())
      await writeJson(
        join(root, area, c.id, scenarioFiles[index] ?? ""),
        scenario,
      );
}
test("staging distingue borradores parciales de fuentes completas y no activa campañas", async () => {
  const root = await mkdtemp(join(tmpdir(), "cdf-staging-"));
  try {
    await cp(join(source, "config"), join(root, "config"), { recursive: true });
    await writeCampaign(root, "campaigns", fixture);
    await writeCampaign(root, "staging/campaigns", fixture, false);
    expect((await inspectStaging(root, fixture.id)).complete).toBe(false);
    expect((await inspectStaging(root, fixture.id)).pending).toHaveLength(1);
    expect((await loadProject(root)).campaigns).toHaveLength(1);
    await writeCampaign(root, "staging/campaigns", fixture);
    expect(await inspectStaging(root, fixture.id)).toEqual({
      campaign: fixture.id,
      pending: [],
      complete: true,
      issues: [],
    });
    const path = join(
      root,
      "staging/campaigns",
      fixture.id,
      "scenarios",
      fixture.scenarios[0]?.id ?? "",
      "scenario.json",
    );
    await writeJson(path, { invalid: true });
    await expect(inspectStaging(root, fixture.id)).rejects.toThrow();
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});
test("validación global detecta destinos multimedia distintos entre mods", async () => {
  const root = await mkdtemp(join(tmpdir(), "cdf-global-assets-"));
  try {
    await cp(join(source, "config"), join(root, "config"), { recursive: true });
    const other = structuredClone(fixture);
    other.id = "another-pilot";
    other.internalName = "CDF_AnotherPilot";
    other.publicId = "CDF-T02";
    const campaigns = [structuredClone(fixture), other];
    for (const [index, c] of campaigns.entries()) {
      const bytes = `${JSON.stringify({ campaign: c.id })}\n`;
      await Bun.write(join(root, `map-${index}.json`), bytes);
      c.assets = [
        {
          id: "shared",
          kind: "map",
          description: "Plano",
          path: `map-${index}.json`,
          origin: "original",
          creator: "Test",
          url: "https://example.com",
          license: "Original",
          restrictions: [],
          obtained: "2026-10-12",
          campaigns: [c.id],
          review: "draft",
          format: "json",
          sha256: hash(bytes),
          cost: 0,
          enginePath: "resources/_common/maps/shared.json",
        },
      ];
      await writeCampaign(root, "campaigns", c);
    }
    expect((await validateProject(root)).map((i) => i.code)).toContain(
      "assets.global-destination",
    );
    other.internalName = fixture.internalName.toUpperCase();
    await writeCampaign(root, "campaigns", other);
    expect((await validateProject(root)).map((i) => i.code)).toContain(
      "project.native-destination",
    );
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});
