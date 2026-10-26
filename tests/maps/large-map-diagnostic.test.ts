import { expect, test } from "bun:test";
import { resolve } from "node:path";
import { pythonCommand } from "../../packages/aoe2-adapter/python-bridge.adapter";

const root = resolve(import.meta.dir, "../..");

test("diagnóstico artificial grande clona solo posiciones y cuatro controles de terreno", async () => {
  const proc = Bun.spawn(
    [await pythonCommand(root), "tests/maps/test_large_map_diagnostic.py"],
    { cwd: root, stdout: "pipe", stderr: "pipe" },
  );
  const [out, err, code] = await Promise.all([
    new Response(proc.stdout).text(),
    new Response(proc.stderr).text(),
    proc.exited,
  ]);
  expect(code, `${out}\n${err}`).toBe(0);
  expect(err).toMatch(/Ran [1-9]\d* tests/);
}, 30_000);
