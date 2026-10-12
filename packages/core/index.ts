import { createHash } from "node:crypto";
import { mkdir, readFile, realpath, rename, writeFile } from "node:fs/promises";
import { dirname, isAbsolute, relative, resolve, sep } from "node:path";

export type Issue = {
  code: string;
  path: string;
  message: string;
  severity: "error" | "warning";
};
export const issue = (
  code: string,
  path: string,
  message: string,
  severity: Issue["severity"] = "error",
): Issue => ({ code, path, message, severity });
export function assertValid(issues: Issue[]): void {
  const errors = issues.filter((i) => i.severity === "error");
  if (errors.length)
    throw new Error(
      errors.map((i) => `${i.code} ${i.path}: ${i.message}`).join("\n"),
    );
}
export function canonical(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonical).join(",")}]`;
  if (value !== null && typeof value === "object")
    return `{${Object.entries(value)
      .sort(([a], [b]) => a.localeCompare(b, "en"))
      .map(([k, v]) => `${JSON.stringify(k)}:${canonical(v)}`)
      .join(",")}}`;
  return JSON.stringify(value);
}
export const hash = (value: string | Uint8Array): string =>
  createHash("sha256").update(value).digest("hex");
export function within(root: string, path: string): string {
  if (isAbsolute(path) || path.includes("\\") || path.split("/").includes(".."))
    throw new Error(`Ruta insegura: ${path}`);
  const target = resolve(root, path);
  const rel = relative(resolve(root), target);
  if (!rel || rel === ".." || rel.startsWith(`..${sep}`))
    throw new Error(`Ruta fuera del proyecto: ${path}`);
  return target;
}
export async function sourceFile(root: string, path: string): Promise<string> {
  const target = await realpath(within(root, path));
  const base = await realpath(root);
  const rel = relative(base, target);
  if (rel === ".." || rel.startsWith(`..${sep}`) || isAbsolute(rel))
    throw new Error(`Enlace fuera del proyecto: ${path}`);
  return target;
}
export async function jsonFile(path: string): Promise<unknown> {
  const text = await readFile(path, "utf8");
  if (text.charCodeAt(0) === 0xfeff) throw new Error(`BOM prohibido: ${path}`);
  return JSON.parse(text);
}
export async function atomicWrite(
  path: string,
  text: string | Uint8Array,
): Promise<void> {
  await mkdir(dirname(path), { recursive: true });
  const temp = `${path}.${crypto.randomUUID()}.tmp`;
  await writeFile(temp, text);
  await rename(temp, path);
}
export const writeJson = (path: string, value: unknown): Promise<void> =>
  atomicWrite(path, `${JSON.stringify(value, null, 2)}\n`);
export function duplicates(values: string[]): string[] {
  return [...new Set(values.filter((x, i) => values.indexOf(x) !== i))];
}
