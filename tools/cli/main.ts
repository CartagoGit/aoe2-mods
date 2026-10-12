import { mkdir, readdir, readFile, rm } from "node:fs/promises";
import { join, resolve } from "node:path";
import { z } from "zod";
import { runAdapter } from "../../packages/aoe2-adapter";
import { renderNativeCampaign } from "../../packages/aoe2-adapter/native";
import { validateAssets } from "../../packages/assets";
import { validateAudio } from "../../packages/audio";
import {
  compileCampaign,
  validateCampaign,
} from "../../packages/campaign-compiler";
import {
  assertValid,
  atomicWrite,
  hash,
  portableRelativePath,
  sourceFile,
  within,
  writeJson,
} from "../../packages/core";
import {
  allocate,
  campaignKeys,
  exportStrings,
  validateCatalogs,
} from "../../packages/localization";
import { schemas } from "../../packages/schemas";
import { candidateFingerprint } from "./candidate";
import { exportVariants } from "./export-check";
import { buildAudio } from "./media";
import {
  campaignFileSchema,
  docsCheck,
  inspectStaging,
  loadCampaign,
  loadProject,
  releaseIssues,
  requireProject,
  validateProject,
} from "./project";

const root = resolve(import.meta.dir, "../..");
async function build(
  id: string,
  exportNative: boolean,
  nativeTemplates = false,
  candidate = false,
) {
  const p = await requireProject(root);
  const c = await loadCampaign(root, id);
  if (candidate) await candidateFingerprint(root, c, p);
  const buildRoot = within(root, `build/${id}`);
  await mkdir(buildRoot, { recursive: true });
  const ir = compileCampaign(c, p.lock);
  const irPath = join(buildRoot, "campaign-ir.json");
  await writeJson(irPath, ir);
  await writeJson(join(buildRoot, "narrative-ir.json"), {
    kind: "cdf-intermediate-not-native",
    campaign: c.id,
    introduction: c.introduction,
    epilogue: c.epilogue,
    scenarios: c.scenarios.map((s) => ({ id: s.id, narrative: s.narrative })),
    recommendedPrevious: c.recommendedPrevious.map((prev) => ({
      condition: {
        Type: "CampaignVariable",
        Campaign: prev.internalName,
        Key: prev.endingKey,
        Comparison: "<=0",
      },
      recommendationKey: prev.recommendationKey,
      recapKey: prev.recapKey,
    })),
  });
  const modRoot = join(buildRoot, "mod");
  await rm(modRoot, { recursive: true, force: true });
  for (const cat of c.localization) {
    const target = p.languages.targets.find((l) => l.locale === cat.locale);
    if (!target) throw new Error(`Idioma sin destino: ${cat.locale}`);
    await atomicWrite(
      join(
        modRoot,
        `resources/${target.engineFolder}/strings/key-value/key-value-modded-strings-utf8.txt`,
      ),
      exportStrings(cat, p.lock),
    );
  }
  for (const asset of c.assets) {
    if (!asset.enginePath) continue;
    const target = within(modRoot, portableRelativePath(asset.enginePath));
    await atomicWrite(
      target,
      await readFile(await sourceFile(root, asset.path)),
    );
  }
  const report = {
    campaign: c.id,
    sourceSha256: hash(JSON.stringify(c)),
    mode: exportNative ? "binary-export" : "intermediate-only",
    gameVerified: false,
    localizationSnapshot: c.localization.map((c) => c.locale),
  };
  await writeJson(join(buildRoot, "build-report.json"), report);
  if (exportNative) {
    const native = join(modRoot, "resources/_common/campaign");
    await runAdapter(root, ["build", irPath, native]);
    const nativeManifest = nativeTemplates
      ? await renderNativeCampaign(root, c, p.lock, native)
      : undefined;
    // Escenarios sueltos y reportes quedan fuera del mod distribuible.
    const privateRoot = join(buildRoot, "native-checks");
    await mkdir(privateRoot, { recursive: true });
    for (const f of await readdir(native))
      if (f.endsWith(".aoe2scenario") || f === "export-report.json") {
        const { rename } = await import("node:fs/promises");
        await rename(join(native, f), join(privateRoot, f));
      }
    await mkdir(join(root, "dist"), { recursive: true });
    const archive = join(
      root,
      "dist",
      `${id}-${candidate ? "release" : "fixture"}.zip`,
    );
    await runAdapter(root, ["zip", modRoot, archive]);
    if (candidate) {
      await writeJson(join(buildRoot, "candidate-report.json"), {
        schemaVersion: 1,
        campaign: c.id,
        artifactSha256: hash(await readFile(archive)),
        fingerprint: await candidateFingerprint(root, c, p),
        nativeManifest,
        gameVerified: false,
      });
    }
    return { report, archive };
  }
  return { report, irPath };
}
async function main() {
  const [command, ...args] = process.argv.slice(2);
  const id = args.find((a) => !a.startsWith("--"));
  if (command === "staging:check") {
    if (!id) throw new Error("Uso: bun run staging:check ID [--partial]");
    const report = await inspectStaging(root, id);
    assertValid(report.issues);
    if (!report.complete && !args.includes("--partial"))
      throw new Error(`Borrador incompleto: ${report.pending.join(", ")}`);
    console.log({
      ...report,
      scope: "draft-schema; sin IDs, archivos multimedia ni exportación",
    });
    return;
  }
  if (command === "audio:build") {
    if (!id) throw new Error("Uso: bun run audio:build ID --locale=es-ES");
    const locale =
      args.find((a) => a.startsWith("--locale="))?.slice(9) ?? "es-ES";
    console.log(await buildAudio(root, await loadCampaign(root, id), locale));
    return;
  }
  if (command === "campaigns:list") {
    console.log(
      (await loadProject(root)).campaigns
        .map((c) => `${c.publicId}\t${c.id}\t${c.status}`)
        .join("\n"),
    );
    return;
  }
  if (command === "docs:check") {
    await docsCheck(root);
    console.log("Documentación y enlaces locales válidos");
    return;
  }
  if (command === "schema:export") {
    for (const [name, schema] of Object.entries({
      ...schemas,
      campaignFile: campaignFileSchema,
    }))
      await writeJson(
        join(root, `build/schemas/${name}.schema.json`),
        z.toJSONSchema(schema),
      );
    console.log("JSON Schema generado en build/schemas");
    return;
  }
  if (command === "ids:allocate") {
    const p = await loadProject(root);
    const next = allocate(
      p.lock,
      p.campaigns.flatMap((c) =>
        Object.keys(
          c.localization.find((l) => l.locale === "es-ES")?.strings ?? {},
        ),
      ),
    );
    await writeJson(join(root, "config/string-ids.lock.json"), next);
    console.log("Registro de IDs actualizado; revisar diff antes de publicar");
    return;
  }
  if (command === "build") {
    const p = await requireProject(root);
    for (const c of p.campaigns) console.log(await build(c.id, false));
    return;
  }
  if (command === "campaign:candidate") {
    if (!id) throw new Error("Uso: bun run campaign:candidate ID");
    console.log(await build(id, true, true, true));
    return;
  }
  if (command === "campaign:build") {
    if (!id)
      throw new Error("Uso: bun run campaign:build <campaign-id> [--export]");
    console.log(
      await build(id, args.includes("--export"), args.includes("--templates")),
    );
    return;
  }
  if (command === "export:check") {
    console.log(await build("technical-pilot", true));
    const p = await loadProject(root);
    console.log(
      await exportVariants(
        root,
        await loadCampaign(root, "technical-pilot"),
        p.lock,
      ),
    );
    return;
  }
  if (
    [
      "campaign:validate",
      "i18n:check",
      "assets:check",
      "audio:check",
      "release:check",
    ].includes(command ?? "")
  ) {
    const p = await loadProject(root);
    const cs = id ? [await loadCampaign(root, id)] : p.campaigns;
    if (!cs.length) throw new Error("No hay campañas para validar");
    if (command === "campaign:validate") {
      assertValid(await validateProject(root));
      for (const c of cs) assertValid(validateCampaign(c).issues);
    }
    if (command === "i18n:check")
      for (const c of cs)
        assertValid(validateCatalogs(c.localization, campaignKeys(c)));
    if (command === "assets:check")
      for (const c of cs) assertValid(await validateAssets(root, c.assets));
    if (command === "audio:check")
      for (const c of cs)
        for (const a of c.assets.filter((a) => a.kind === "audio"))
          await validateAudio(root, a.path);
    if (command === "release:check") {
      assertValid(await validateProject(root));
      for (const c of cs) {
        let candidateHash: string | undefined;
        try {
          candidateHash = hash(
            await readFile(join(root, `dist/${c.id}-release.zip`)),
          );
        } catch {}
        assertValid(releaseIssues(c, p, candidateHash));
        const candidateReport = await Bun.file(
          join(root, `build/${c.id}/candidate-report.json`),
        ).json();
        if (candidateReport.nativeManifest?.status !== "game-verified")
          throw new Error("Plantillas nativas todavía no acreditadas en AoE2");
        if (
          candidateReport.artifactSha256 !== candidateHash ||
          candidateReport.fingerprint !==
            (await candidateFingerprint(root, c, p))
        )
          throw new Error(
            "Candidato obsoleto: recompilar y repetir QA si cambia el ZIP",
          );
      }
    }
    console.log(`${command}: ${cs.length} campaña(s) comprobadas`);
    return;
  }
  throw new Error(
    `Comando desconocido: ${command ?? "(vacío)"}. Consulta README.md.`,
  );
}
main().catch((e) => {
  console.error(e instanceof Error ? e.message : e);
  process.exitCode = 1;
});
