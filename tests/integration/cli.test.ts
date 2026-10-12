import { expect, test } from "bun:test";
import { resolve } from "node:path";

const root = resolve(import.meta.dir, "../..");
async function cli(...args: string[]) {
  const p = Bun.spawn(
    [process.execPath, "tools/cli/chronicles.script.ts", ...args],
    {
      cwd: root,
      stdout: "pipe",
      stderr: "pipe",
    },
  );
  const [out, err, code] = await Promise.all([
    new Response(p.stdout).text(),
    new Response(p.stderr).text(),
    p.exited,
  ]);
  return { out, err, code };
}
test("CLI rechaza comando/ID inválidos y release prematura", async () => {
  expect((await cli("missing-command")).code).not.toBe(0);
  expect((await cli("campaign:build", "../escape")).code).not.toBe(0);
  const release = await cli("release:check", "technical-pilot");
  expect(release.code).not.toBe(0);
  expect(release.err).toContain("release.evidence");
  expect(release.err).toContain("release.artifact");
});
test("compilación intermedia y validación reales", async () => {
  expect((await cli("campaign:validate", "technical-pilot")).code).toBe(0);
  expect((await cli("campaign:build", "technical-pilot")).code).toBe(0);
  const ir = await Bun.file(
    resolve(root, "build/technical-pilot/campaign-ir.json"),
  ).json();
  expect(ir.scenarios[0].objectiveIds.prepare).toBeGreaterThan(0);
  const report = await Bun.file(
    resolve(root, "build/technical-pilot/build-report.json"),
  ).json();
  expect(report.gameVerified).toBe(false);
});
test("audio sin grabación falla de forma explícita", async () => {
  const result = await cli("audio:build", "technical-pilot");
  expect(result.code).not.toBe(0);
  expect(result.err).toContain("Grabación ausente");
});

test("candidato exige plantillas reales antes de exportar", async () => {
  const result = await cli("campaign:candidate", "technical-pilot");
  expect(result.code).not.toBe(0);
  expect(result.err).toContain("native/manifest.json");
});
