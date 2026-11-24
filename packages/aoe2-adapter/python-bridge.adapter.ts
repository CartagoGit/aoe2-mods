import { access } from "node:fs/promises";
import { join } from "node:path";
export async function pythonCommand(root: string): Promise<string> {
  if (process.env.COF_PYTHON) return process.env.COF_PYTHON;
  const venv = join(
    root,
    ".venv",
    process.platform === "win32" ? "Scripts/python.exe" : "bin/python",
  );
  try {
    await access(venv);
    return venv;
  } catch {
    return process.platform === "win32" ? "python" : "python3";
  }
}
export async function runAdapter(
  root: string,
  args: string[],
): Promise<string> {
  const proc = Bun.spawn(
    [
      await pythonCommand(root),
      join(root, "tools/python/export_aoe2.py"),
      ...args,
    ],
    { cwd: root, stdout: "pipe", stderr: "pipe" },
  );
  const [out, err, exit] = await Promise.all([
    new Response(proc.stdout).text(),
    new Response(proc.stderr).text(),
    proc.exited,
  ]);
  if (exit !== 0)
    throw new Error(`Adaptador AoE2 (${exit}): ${err}\n${out.slice(-2000)}`);
  return out;
}
