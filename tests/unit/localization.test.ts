import { expect, test } from "bun:test";
import {
  allocate,
  sourceCatalog,
  validateCatalogs,
} from "../../packages/localization/localization.catalog";
import {
  type Catalog,
  campaignSchema,
} from "../../packages/schemas/campaign.schema";

const english: Catalog = {
  locale: "en",
  status: "draft",
  reviewer: "test",
  strings: {
    "campaign.demo.title": "The Eagle and the Cross",
    "campaign.demo.intro": "<b>Hold {count}</b>",
  },
};
const spanish: Catalog = {
  locale: "es-ES",
  status: "draft",
  reviewer: "test",
  strings: {
    "campaign.demo.title": "El águila y la cruz",
    "campaign.demo.intro": "<b>Conserva {count}</b>",
  },
};

test("English is the source even when Spanish is absent or first", () => {
  expect(validateCatalogs([english], Object.keys(english.strings))).toEqual([]);
  expect(
    sourceCatalog({ sourceLocale: "en", localization: [spanish, english] }),
  ).toBe(english);
  expect(
    validateCatalogs([spanish, english], Object.keys(english.strings)),
  ).toEqual([]);
});
test("missing declared source fails; Spanish cannot silently replace English", () => {
  expect(
    validateCatalogs([spanish], [], 4000, "en").map((i) => i.code),
  ).toContain("i18n.source");
  expect(
    validateCatalogs([english], [], 4000, "es-ES").map((i) => i.code),
  ).toContain("i18n.source");
});
test("English controls completeness and placeholders in translated catalogs", () => {
  const invalid = {
    ...spanish,
    strings: {
      "campaign.demo.title": "Título",
      "campaign.demo.intro": "{other}",
    },
  };
  const codes = validateCatalogs([invalid, english], [], 4000, "en").map(
    (i) => i.code,
  );
  expect(codes).toContain("i18n.placeholder");
  expect(codes).toContain("i18n.marker");
  expect(
    validateCatalogs([{ ...spanish, strings: {} }, english], []).map(
      (i) => i.code,
    ),
  ).toContain("i18n.missing");
});
test("source locale migration preserves existing numeric IDs", async () => {
  const fixture = await Bun.file(
    new URL("../../campaigns/technical-pilot/campaign.json", import.meta.url),
  ).json();
  expect(
    campaignSchema.shape.sourceLocale.safeParse(fixture.sourceLocale).success,
  ).toBe(true);
  expect(campaignSchema.shape.sourceLocale.safeParse(undefined).success).toBe(
    false,
  );
  const lock = await Bun.file(
    new URL("../../config/string-ids.lock.json", import.meta.url),
  ).json();
  const canonical = sourceCatalog(fixture);
  if (!canonical) throw new Error("Fixture source catalog missing");
  expect(allocate(lock, Object.keys(canonical.strings))).toEqual(lock);
});
