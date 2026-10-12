import { expect, test } from "bun:test";
import { mkdtemp, rm, symlink, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import {
  validateAssetDestinations,
  validateAssets,
} from "../../packages/assets";
import { hash, portableRelativePath, sourceFile } from "../../packages/core";
import { validateGlossary } from "../../packages/localization/glossary";
import type { Asset } from "../../packages/schemas";

test("destinos nativos rechazan alias y colisiones locales/globales", () => {
  const reserved =
    "resources/es/strings/key-value/key-value-modded-strings-utf8.txt";
  for (const path of [
    "resources/./es/x",
    "resources//es/x",
    "../x",
    "/x",
    "a\\x",
    "a/NUL.wav",
    "a/x.",
    "a/x:stream",
  ])
    expect(() => portableRelativePath(path)).toThrow();
  const asset = (id: string, enginePath: string, sha256 = "a".repeat(64)) =>
    ({ id, enginePath, sha256 }) as Asset;
  const groups = [
    { owner: "one", assets: [asset("a", "resources/_common/sound/CDF.wav")] },
    {
      owner: "two",
      assets: [asset("b", "resources/_common/sound/cdf.wav", "b".repeat(64))],
    },
  ];
  expect(validateAssetDestinations(groups).map((i) => i.code)).toContain(
    "assets.global-destination",
  );
  const shared = groups[1]?.assets[0];
  if (!shared) throw new Error("Recurso ausente");
  shared.sha256 = "a".repeat(64);
  expect(validateAssetDestinations(groups)).toEqual([]);
  expect(
    validateAssetDestinations(
      [{ owner: "one", assets: [asset("a", reserved.toUpperCase())] }],
      [reserved],
    ).map((i) => i.code),
  ).toContain("assets.reserved-path");
  expect(
    validateAssetDestinations([
      {
        owner: "one",
        assets: [asset("a", "resources/x.wav"), asset("b", "resources/X.wav")],
      },
    ]).map((i) => i.code),
  ).toContain("assets.destination");
  expect(
    validateAssetDestinations([
      { owner: "one", assets: [asset("a", "resources/./x.wav")] },
    ]).map((i) => i.code),
  ).toContain("assets.destination-path");
});

test("manifiesto rechaza PNG inválido y hash alterado", async () => {
  const root = await mkdtemp(join(tmpdir(), "cof-assets-"));
  try {
    const bytes = Buffer.from("invalid png");
    await writeFile(join(root, "image.png"), bytes);
    const a: Asset = {
      id: "image",
      kind: "image",
      description: "Test",
      path: "image.png",
      origin: "original",
      creator: "test",
      url: "https://example.com/image",
      license: "Original",
      restrictions: [],
      obtained: "2026-10-12",
      campaigns: [],
      review: "draft",
      format: "png",
      width: 1,
      height: 1,
      sha256: hash(bytes),
      cost: 0,
    };
    const out = await validateAssets(root, [a]);
    expect(out.map((i) => i.code)).toContain("assets.file");
    a.sha256 = "0".repeat(64);
    expect((await validateAssets(root, [a])).map((i) => i.code)).toContain(
      "assets.hash",
    );
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});
test("fuentes no siguen enlaces fuera de raíz", async () => {
  if (process.platform === "win32") return;
  const root = await mkdtemp(join(tmpdir(), "cof-path-"));
  try {
    await symlink(tmpdir(), join(root, "escape"));
    await expect(sourceFile(root, "escape")).rejects.toThrow("Enlace fuera");
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});
test("glosario exige variantes de cada idioma", () => {
  const catalogs = [
    {
      locale: "en",
      status: "draft" as const,
      reviewer: "test",
      strings: { "test.title": "forbidden" },
    },
  ];
  expect(
    validateGlossary(catalogs, [{ id: "term", locales: {} }]).map(
      (i) => i.code,
    ),
  ).toContain("glossary.missing");
  expect(
    validateGlossary(catalogs, [
      {
        id: "term",
        locales: { en: { preferred: "preferred", forbidden: ["forbidden"] } },
      },
    ]).map((i) => i.code),
  ).toContain("glossary.variant");
});
