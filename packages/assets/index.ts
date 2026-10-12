import { readFile } from "node:fs/promises";
import { hash, type Issue, issue, sourceFile } from "../core";
import type { Asset } from "../schemas";
export async function validateAssets(
  root: string,
  assets: Asset[],
): Promise<Issue[]> {
  const issues: Issue[] = [];
  const ids = new Set<string>();
  const destinations = new Set<string>();
  for (const a of assets) {
    const expectedFormat = { image: "png", audio: "wav", map: "json" }[a.kind];
    if (a.format !== expectedFormat)
      issues.push(issue("assets.format", a.id, "Tipo y formato no coinciden"));
    if (a.enginePath) {
      if (destinations.has(a.enginePath))
        issues.push(
          issue("assets.destination", a.id, "Destino nativo repetido"),
        );
      destinations.add(a.enginePath);
    }
    if (ids.has(a.id))
      issues.push(issue("assets.duplicate", a.id, "ID repetido"));
    ids.add(a.id);
    try {
      const bytes = await readFile(await sourceFile(root, a.path));
      if (hash(bytes) !== a.sha256)
        issues.push(issue("assets.hash", a.id, "Hash no coincide"));
      if (a.format === "json") JSON.parse(bytes.toString("utf8"));
      if (a.format === "png") {
        if (
          bytes.length < 24 ||
          bytes.subarray(0, 8).toString("hex") !== "89504e470d0a1a0a" ||
          bytes.subarray(12, 16).toString() !== "IHDR"
        )
          throw new Error("PNG inválido");
        if (
          a.width !== bytes.readUInt32BE(16) ||
          a.height !== bytes.readUInt32BE(20)
        )
          issues.push(
            issue("assets.dimensions", a.id, "Resolución no coincide"),
          );
      }
      if (a.origin === "generated" && (!a.prompt || !a.model))
        issues.push(issue("assets.provenance", a.id, "Faltan prompt/modelo"));
    } catch (e) {
      issues.push(issue("assets.file", a.id, String(e)));
    }
  }
  return issues;
}
