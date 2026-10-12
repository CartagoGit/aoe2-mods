import { describe, expect, test } from "bun:test";
import { resolve } from "node:path";
import {
  bindNativeTemplate,
  progressCondition,
} from "../../packages/aoe2-adapter/templates";
import {
  compileCampaign,
  recommendation,
  validateCampaign,
} from "../../packages/campaign-compiler";
import { canonical, hash, within } from "../../packages/core";
import { validateGameplay } from "../../packages/gameplay-validation";
import {
  allocate,
  exportStrings,
  interpolate,
  validateCatalogs,
  validateLock,
} from "../../packages/localization";
import { campaignSchema } from "../../packages/schemas";
import {
  loadCampaign,
  loadProject,
  releaseIssues,
} from "../../tools/cli/project";

const root = resolve(import.meta.dir, "../..");
const campaign = await loadCampaign(root, "technical-pilot");
const codes = (c: typeof campaign) =>
  validateCampaign(c).issues.map((i) => i.code);

describe("Contratos y trazabilidad", () => {
  test("fixture válido y contrato estricto", () => {
    expect(codes(campaign)).toEqual([]);
    expect(() => campaignSchema.parse({ ...campaign, extra: true })).toThrow();
  });
  test("no imponer progresión", () => {
    expect(() =>
      campaignSchema.parse({ ...campaign, enforceRequirement: true }),
    ).toThrow();
    expect(
      recommendation(
        { internalName: "CDF_Missing", endingKey: "progress.missing.done" },
        () => undefined,
      ),
    ).toBe(true);
    expect(
      recommendation(
        { internalName: "CDF_Missing", endingKey: "progress.missing.done" },
        () => 1,
      ),
    ).toBe(false);
  });
  test("IDs globales, personajes y fuentes rotas", () => {
    const c = structuredClone(campaign);
    c.claims = [
      {
        id: "claim",
        classification: "documented",
        statement: "afirmación",
        sources: ["missing"],
        locator: "p. 1",
        qualification: "Certeza pendiente",
        review: "draft",
      },
    ];
    c.scenarios[0]?.claimIds.push("absent");
    expect(codes(c)).toContain("history.source");
    expect(codes(c)).toContain("history.claim");
  });
  test("hechos documentados necesitan evidencia", () => {
    const c = structuredClone(campaign);
    c.claims = [
      {
        id: "claim",
        classification: "documented",
        statement: "afirmación",
        sources: [],
        locator: "p. 1",
        qualification: "Certeza pendiente",
        review: "draft",
      },
    ];
    expect(codes(c)).toContain("history.evidence");
  });
  test("civilización y ruta no se traducen", () => {
    expect(campaign.scenarios[0]?.victory.progressKey).toBe(
      "progress.technical-pilot.route-a",
    );
    expect(campaign.internalName).toBe("CDF_TechnicalPilot");
  });
});
describe("Juego y exploits estáticos", () => {
  test("objetivo final inexistente", () => {
    const c = structuredClone(campaign);
    c.scenarios[0]?.victory.objectives.push("missing");
    expect(codes(c)).toContain("game.victory");
  });
  test("ciclo de requisitos", () => {
    const s = structuredClone(campaign.scenarios[0]);
    if (!s) throw Error();
    s.objectives[0]?.requires.push("defeat-guard");
    expect(validateGameplay(s).map((i) => i.code)).toContain("game.cycle");
  });
  test("mapa bloqueado y spawn atrapado", () => {
    const s = structuredClone(campaign.scenarios[0]);
    if (!s) throw Error();
    s.map.blocked = [{ x: 4, y: 4 }];
    expect(validateGameplay(s).map((i) => i.code)).toContain(
      "game.connectivity",
    );
    expect(validateGameplay(s).map((i) => i.code)).toContain("game.spawn");
  });
  test("reinforcements must consume finite reserve", () => {
    const s = structuredClone(campaign.scenarios[0]);
    if (!s?.factions[1]) throw Error();
    s.factions[1].reinforcements = [
      {
        id: "reserve",
        origin: "Ciudad aliada",
        cause: "Llamada",
        counterplay: "Cortar camino",
        maxWaves: 4,
        unitsPerWave: 10,
        intervalSeconds: 30,
        totalBudget: 20,
      },
    ];
    expect(validateGameplay(s).map((i) => i.code)).toContain("game.reserve");
  });
  test("variable no inicializada", () => {
    const s = structuredClone(campaign.scenarios[0]);
    if (!s?.objectives[0]) throw Error();
    s.objectives[0].completion = {
      type: "variable",
      variable: "missing",
      value: 1,
    };
    expect(validateGameplay(s).map((i) => i.code)).toContain("game.variable");
  });
});
describe("Localización estable", () => {
  const lock = { schemaVersion: 1 as const, nextId: 100, ids: {}, retired: [] };
  test("asignación ordenada, estable e idempotente", () => {
    const a = allocate(lock, ["campaign.z.title", "campaign.a.title"], [100]);
    expect(a.ids["campaign.a.title"]).toBe(101);
    const b = allocate(a, ["campaign.new.title", "campaign.a.title"]);
    expect(b.ids["campaign.a.title"]).toBe(101);
    expect(allocate(b, Object.keys(b.ids))).toEqual(b);
  });
  test("colisiones y tombstones", () => {
    expect(() =>
      validateLock({ ...lock, nextId: 103, ids: { a: 101, b: 101 } }),
    ).toThrow();
    expect(() =>
      allocate({ ...lock, nextId: 102, ids: { a: 101 }, retired: ["a"] }, [
        "a",
      ]),
    ).toThrow();
  });
  test("traducción requiere placeholders y marcadores", () => {
    const catalogs = [
      {
        locale: "es-ES",
        status: "draft" as const,
        reviewer: "test",
        strings: { "test.title": "<b>Hola {name}</b>" },
      },
      {
        locale: "en",
        status: "draft" as const,
        reviewer: "test",
        strings: { "test.title": "Hello {other}" },
      },
    ];
    expect(
      validateCatalogs(catalogs, ["test.title"]).map((i) => i.code),
    ).toContain("i18n.placeholder");
    expect(validateCatalogs(catalogs, []).map((i) => i.code)).toContain(
      "i18n.marker",
    );
  });
  test("UTF8 y comillas escapadas", () => {
    const c = {
      locale: "es-ES",
      status: "draft" as const,
      reviewer: "test",
      strings: { "campaign.a.title": 'Fe: "diálogo" 日本語' },
    };
    const result = exportStrings(c, allocate(lock, Object.keys(c.strings)));
    expect(result).toContain('100 "Fe: \\"'.replace("\\\\", "\\"));
    expect(result).toContain("日本語");
  });
  test("interpolación previa a exportación", () => {
    expect(interpolate("Hola {name}", { name: "Olga" })).toBe("Hola Olga");
    expect(() => interpolate("Hola {name}", {})).toThrow();
  });
});
describe("Compilación y límites", () => {
  test("IR determinista", async () => {
    const p = await loadProject(root);
    expect(canonical(compileCampaign(campaign, p.lock))).toBe(
      canonical(compileCampaign(campaign, p.lock)),
    );
    expect(hash(canonical({ b: 1, a: 2 }))).toBe(
      hash(canonical({ a: 2, b: 1 })),
    );
  });
  test("release no confunde tests con jugar", async () => {
    const p = await loadProject(root);
    const issues = releaseIssues(campaign, p);
    expect(issues.map((i) => i.code)).toContain("release.evidence");
    expect(issues.map((i) => i.code)).toContain("release.language");
  });
  test("rutas no salen del proyecto", () => {
    for (const path of ["../secret", "a/../../secret", "/tmp/x", "a\\x"])
      expect(() => within(root, path)).toThrow();
  });
  test("plantilla nativa preservada y tokens resueltos", () => {
    const lock = allocate(
      { schemaVersion: 1, nextId: 100, ids: {}, retired: [] },
      ["campaign.test.title"],
    );
    expect(
      bindNativeTemplate(
        {
          String: "@cdf:string:campaign.test.title",
          Duration: "@cdf:value:seconds",
          Original: true,
        },
        lock,
        { seconds: 5 },
      ),
    ).toEqual({ String: 100, Duration: 5, Original: true });
    expect(
      progressCondition("CDF_Test", "progress.test.done", true).Comparison,
    ).toBe("<=0");
  });
});

test("evento de refuerzo no supera reserva y no se repite infinitamente", () => {
  const s = structuredClone(campaign.scenarios[0]);
  if (!s?.factions[1]) throw Error();
  s.factions[1].reinforcements = [
    {
      id: "reserve",
      origin: "Ciudad",
      cause: "Movilización",
      counterplay: "Bloquear camino",
      maxWaves: 1,
      unitsPerWave: 2,
      intervalSeconds: 20,
      totalBudget: 2,
    },
  ];
  s.triggers = [
    {
      id: "wave-one",
      conditions: [{ type: "timer", seconds: 20 }],
      effects: [
        {
          type: "spawn",
          reinforcement: "reserve",
          faction: "enemy",
          unitType: "militia",
          count: 2,
          position: { x: 20, y: 20 },
        },
      ],
    },
    {
      id: "wave-two",
      conditions: [{ type: "timer", seconds: 40 }],
      effects: [
        {
          type: "spawn",
          reinforcement: "reserve",
          faction: "enemy",
          unitType: "militia",
          count: 2,
          position: { x: 20, y: 20 },
        },
      ],
    },
  ];
  expect(validateGameplay(s).map((i) => i.code)).toContain("game.event-budget");
});

test("áreas, tributos y terrenos rechazan referencias, saldo y límites inválidos", () => {
  const c = structuredClone(campaign);
  const s = c.scenarios[0];
  if (!s) throw new Error("Fixture ausente");
  s.triggers = [
    {
      id: "invalid",
      conditions: [
        {
          type: "bring",
          unit: "missing",
          from: { x: 20, y: 20 },
          to: { x: 10, y: 10 },
        },
      ],
      effects: [
        {
          type: "tribute",
          source: "player",
          target: "enemy",
          resource: "gold",
          amount: 100,
        },
      ],
    },
  ];
  s.map.tiles = [
    { position: { x: 33, y: 33 }, terrain: "dirt-1", elevation: 1 },
    { position: { x: 33, y: 33 }, terrain: "dirt-1", elevation: 1 },
  ];
  expect(codes(c)).toContain("game.area-unit");
  expect(codes(c)).toContain("game.area-bounds");
  expect(codes(c)).toContain("game.tribute-budget");
  expect(codes(c)).toContain("game.tile-duplicate");
  expect(codes(c)).toContain("game.bounds");
});
