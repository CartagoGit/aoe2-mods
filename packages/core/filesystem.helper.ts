import { mkdir, readFile, realpath, rename, writeFile } from "node:fs/promises";
import { dirname, isAbsolute, relative, resolve, sep } from "node:path";

/** Destino nativo canónico, portable a Windows y sin alias de normalización. */
export function portableRelativePath(path: string): string {
  if (
    !/^[A-Za-z0-9._/-]+$/.test(path) ||
    path
      .split("/")
      .some(
        (part) =>
          !part ||
          part === "." ||
          part === ".." ||
          part.endsWith(".") ||
          /^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)/i.test(part),
      )
  )
    throw new Error(`Destino nativo no portable: ${path}`);
  return path;
}

export const destinationKey = (path: string): string =>
  portableRelativePath(path).toLowerCase();

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
