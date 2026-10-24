import { readdir, readFile } from "node:fs/promises";
import { join } from "node:path";
import { pythonCommand } from "../../packages/aoe2-adapter/python-bridge.adapter";
import { sourceFile } from "../../packages/core/filesystem.helper";

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
