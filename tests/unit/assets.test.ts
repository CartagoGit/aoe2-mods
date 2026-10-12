import { expect, test } from "bun:test";
import { mkdtemp, rm, symlink, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { validateAssets } from "../../packages/assets";
import { hash, sourceFile } from "../../packages/core";
import { validateGlossary } from "../../packages/localization/glossary";
import type { Asset } from "../../packages/schemas";

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
