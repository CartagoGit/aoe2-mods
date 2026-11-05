import { expect, test } from "bun:test";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { resolve } from "node:path";
import { atomicWrite, writeJson } from "../../packages/core/filesystem.helper";
import { candidateFingerprint } from "../../tools/cli/campaign-candidate.helper";
import { loadProject } from "../../tools/cli/project.loader";

const root = resolve(import.meta.dir, "../..");
test("candidato invalida cambios de contenido y preserva anotaciones de QA", async () => {
  const p = await loadProject(root);
  const c = structuredClone(p.campaigns[0]);
  if (!c) throw new Error("Fixture ausente");
  const dir = await mkdtemp(resolve(tmpdir(), "cdf-candidate-"));
  try {
    const native = `${dir}/campaigns/${c.id}/native`;
    // Plantillas sintéticas de test de huella; no son formatos del motor ni se distribuyen.
    await writeJson(`${native}/manifest.json`, {
      narrativeTemplate: "story.json",
      layoutTemplate: "layout.json",
    });
    await writeJson(`${native}/story.json`, { token: "one" });
    await writeJson(`${native}/layout.json`, { token: "two" });
    await atomicWrite(`${dir}/tools/python/export_aoe2.py`, "test-generator");
    await writeJson(`${dir}/config/toolchain.json`, { version: 1 });
    await writeJson(`${dir}/config/engine.json`, { scenarioVersion: "1.59" });
    await writeJson(`${dir}/package.json`, { version: "test" });
    await atomicWrite(`${dir}/bun.lock`, "test-lock");
    await atomicWrite(`${dir}/requirements.lock.txt`, "test-parser-lock");
    await atomicWrite(
      `${dir}/packages/compiler/compiler.compiler.ts`,
      "test-compiler",
    );
    await atomicWrite(`${dir}/tools/cli/chronicles.script.ts`, "test-cli");
    const first = await candidateFingerprint(dir, c, p);
    c.compatibility = [];
    c.editorial.review = "approved";
    if (c.scenarios[0]?.qa[0])
      c.scenarios[0].qa[0].evidence = "Resultado registrado";
    expect(await candidateFingerprint(dir, c, p)).toBe(first);
    const cat = c.localization[0];
    if (!cat) throw new Error("Catálogo ausente");
    cat.strings[c.titleKey] = "Texto alterado";
    expect(await candidateFingerprint(dir, c, p)).not.toBe(first);
    cat.strings[c.titleKey] =
      p.campaigns[0]?.localization[0]?.strings[c.titleKey] ?? "";
    for (const [file, replacement] of [
      ["config/engine.json", '{"scenarioVersion":"1.58"}\n'],
      ["requirements.lock.txt", "changed-parser"],
      ["packages/compiler/compiler.compiler.ts", "changed-compiler"],
      ["tools/cli/chronicles.script.ts", "changed-cli"],
      ["bun.lock", "changed-lock"],
    ]) {
      if (!file || replacement === undefined) throw new Error("Caso inválido");
      const original = await readFile(`${dir}/${file}`);
      await atomicWrite(`${dir}/${file}`, replacement);
      expect(await candidateFingerprint(dir, c, p)).not.toBe(first);
      await atomicWrite(`${dir}/${file}`, original);
      expect(await candidateFingerprint(dir, c, p)).toBe(first);
    }
    await writeJson(`${native}/layout.json`, { token: "changed" });
    expect(await candidateFingerprint(dir, c, p)).not.toBe(first);
  } finally {
    await rm(dir, { recursive: true, force: true });
  }
});
