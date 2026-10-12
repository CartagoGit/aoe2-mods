import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { z } from "zod";
import {
  CommandVoiceProvider,
  inspectWav,
  normalizePeak,
  produceAudio,
  RecordedVoiceProvider,
  subtitles,
  type VoiceProvider,
} from "../../packages/audio";
import {
  atomicWrite,
  duplicates,
  hash,
  jsonFile,
  sourceFile,
  writeJson,
} from "../../packages/core";
import type { Campaign } from "../../packages/schemas";

const providerSchema = z
  .strictObject({
    schemaVersion: z.literal(1),
    providers: z.array(
      z.strictObject({
        id: z.string(),
        version: z.string(),
        license: z.string(),
        command: z.string(),
        args: z.array(z.string()),
        enabled: z.boolean(),
      }),
    ),
    normalizationDbFS: z.number().min(-30).max(0),
  })
  .superRefine((config, ctx) => {
    for (const id of duplicates(config.providers.map((p) => p.id)))
      ctx.addIssue({
        code: "custom",
        message: `Proveedor duplicado: ${id}`,
        path: ["providers"],
      });
    if (config.providers.some((p) => p.id === "recorded"))
      ctx.addIssue({
        code: "custom",
        message: "ID de proveedor reservado: recorded",
        path: ["providers"],
      });
  });
export async function buildAudio(root: string, c: Campaign, locale: string) {
  const catalog = c.localization.find((l) => l.locale === locale);
  if (!catalog) throw new Error(`Locale inexistente ${locale}`);
  const config = providerSchema.parse(
    await jsonFile(join(root, "config/audio-providers.json")),
  );
  const narrators = new Map(
    [c.generalNarrator, c.campaignNarrator, ...c.characters].map((n) => [
      n.id,
      n,
    ]),
  );
  const lines = [
    ...c.introduction,
    ...c.epilogue,
    ...c.scenarios.flatMap((s) => [
      ...s.narrative.intro,
      ...s.narrative.events,
      ...s.narrative.outro,
    ]),
  ];
  const reports = [];
  for (const line of lines) {
    const voice = narrators.get(line.speaker)?.voices[locale];
    if (!voice) throw new Error(`Voz no asignada ${line.speaker}.${locale}`);
    const text = catalog.strings[line.textKey];
    if (!text) throw new Error(`Texto ausente ${line.textKey}`);
    let provider: VoiceProvider;
    if (voice.provider === "recorded") {
      const asset = c.assets.find(
        (a) =>
          a.kind === "audio" && a.lineId === line.id && a.locale === locale,
      );
      if (!asset || asset.kind !== "audio")
        throw new Error(`Grabación ausente para ${line.id}`);
      const bytes = await readFile(await sourceFile(root, asset.path));
      if (hash(bytes) !== asset.sha256)
        throw new Error(`Hash de audio incorrecto ${asset.id}`);
      provider = new RecordedVoiceProvider(bytes, asset.license);
    } else {
      const definition = config.providers.find(
        (p) => p.id === voice.provider && p.enabled,
      );
      if (!definition)
        throw new Error(`Proveedor local no configurado ${voice.provider}`);
      provider = new CommandVoiceProvider(
        definition.id,
        definition.version,
        definition.license,
        definition.command,
        definition.args,
      );
    }
    const result = await produceAudio(
      join(root, ".cache/audio"),
      {
        text,
        locale,
        voice: voice.voice,
        delivery: line.delivery,
        rate: 1,
        pronunciation: {},
      },
      provider,
    );
    const normalized = normalizePeak(
      await readFile(result.path),
      config.normalizationDbFS,
    );
    const duration = inspectWav(normalized).duration;
    const output = join(root, `build/${c.id}/audio/${locale}/${line.id}.wav`);
    await atomicWrite(output, normalized);
    await atomicWrite(
      output.replace(/\.wav$/, ".srt"),
      subtitles([{ text, duration }]),
    );
    reports.push({
      line: line.id,
      speaker: line.speaker,
      locale,
      voice: voice.voice,
      provider: provider.id,
      version: provider.version,
      license: provider.license,
      sha256: hash(normalized),
      duration,
      cached: result.cached,
      cost: { basis: "not-billed-local", amount: 0 },
      normalization: {
        method: "PCM peak",
        targetDbFS: config.normalizationDbFS,
      },
    });
  }
  await writeJson(
    join(root, `build/${c.id}/audio/${locale}/manifest.json`),
    reports,
  );
  return reports;
}
