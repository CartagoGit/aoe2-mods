import { readFile } from "node:fs/promises";
import { type Issue, issue } from "../core/diagnostics.helper";
import { destinationKey, sourceFile } from "../core/filesystem.helper";
import { hash } from "../core/serialization.helper";
import type { Asset } from "../schemas/campaign.schema";
export function validateAssetDestinations(
  groups: { owner: string; assets: Asset[] }[],
  reservedPaths: string[] = [],
): Issue[] {
  const issues: Issue[] = [];
  const reserved = new Set(reservedPaths.map(destinationKey));
  const destinations = new Map<string, { owner: string; sha256: string }>();
  for (const { owner, assets } of groups) {
    const local = new Set<string>();
    for (const asset of assets) {
      if (!asset.enginePath) continue;
      const path = `${owner}.${asset.id}`;
      try {
        const key = destinationKey(asset.enginePath);
        if (reserved.has(key))
          issues.push(
            issue(
              "assets.reserved-path",
              path,
              "El recurso sobrescribe un archivo compilado",
            ),
          );
        if (local.has(key))
          issues.push(
            issue("assets.destination", path, "Destino nativo repetido"),
          );
        const previous = destinations.get(key);
        if (
          previous &&
          previous.owner !== owner &&
          previous.sha256 !== asset.sha256
        )
          issues.push(
            issue(
              "assets.global-destination",
              path,
              `Destino compartido con contenido distinto en ${previous.owner}`,
            ),
          );
        local.add(key);
        destinations.set(key, { owner, sha256: asset.sha256 });
      } catch (error) {
        issues.push(issue("assets.destination-path", path, String(error)));
      }
    }
  }
  return issues;
}
export async function validateAssets(
  root: string,
  assets: Asset[],
): Promise<Issue[]> {
  const issues: Issue[] = validateAssetDestinations([
    { owner: "assets", assets },
  ]);
  const ids = new Set<string>();
  for (const a of assets) {
    const expectedFormat = { image: "png", audio: "wav", map: "json" }[a.kind];
    if (a.format !== expectedFormat)
      issues.push(issue("assets.format", a.id, "Tipo y formato no coinciden"));
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
