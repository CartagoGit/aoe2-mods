import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { atomicWrite, canonical, hash, sourceFile } from "../core";
export type AudioRequest = {
  text: string;
  locale: string;
  voice: string;
  delivery: string;
  rate: number;
  pronunciation: Record<string, string>;
};
export interface VoiceProvider {
  id: string;
  version: string;
  license: string;
  cacheIdentity?: string;
  synthesize(request: AudioRequest): Promise<Uint8Array>;
}
export function inspectWav(data: Uint8Array): {
  duration: number;
  sampleRate: number;
  channels: number;
} {
  const b = Buffer.from(data);
  if (
    b.length < 44 ||
    b.toString("ascii", 0, 4) !== "RIFF" ||
    b.toString("ascii", 8, 12) !== "WAVE" ||
    b.readUInt32LE(4) + 8 !== b.length
  )
    throw new Error("WAV RIFF inválido");
  let rate = 0,
    channels = 0,
    byteRate = 0,
    size = 0,
    alignment = 0,
    format = false;
  const dataSizes: number[] = [];
  let p = 12;
  while (p < b.length) {
    if (p + 8 > b.length)
      throw new Error("WAV con cabecera de chunk incompleta");
    const n = b.readUInt32LE(p + 4);
    if (p + 8 + n + (n % 2) > b.length) throw new Error("WAV truncado");
    const tag = b.toString("ascii", p, p + 4);
    if (tag === "fmt ") {
      if (format || n < 16 || b.readUInt16LE(p + 8) !== 1)
        throw new Error("Solo PCM WAV");
      channels = b.readUInt16LE(p + 10);
      rate = b.readUInt32LE(p + 12);
      byteRate = b.readUInt32LE(p + 16);
      alignment = b.readUInt16LE(p + 20);
      const bits = b.readUInt16LE(p + 22);
      if (
        ![16, 24].includes(bits) ||
        alignment !== (channels * bits) / 8 ||
        byteRate !== rate * alignment
      )
        throw new Error("PCM inconsistente");
      format = true;
    }
    if (tag === "data") {
      size += n;
      dataSizes.push(n);
    }
    p += 8 + n + (n % 2);
  }
  if (
    !format ||
    ![1, 2].includes(channels) ||
    rate < 16000 ||
    rate > 96000 ||
    !size ||
    !byteRate ||
    dataSizes.some((n) => n % alignment !== 0)
  )
    throw new Error("WAV sin audio válido");
  return { duration: size / byteRate, sampleRate: rate, channels };
}
export class RecordedVoiceProvider implements VoiceProvider {
  readonly id = "recorded";
  readonly version: string;
  constructor(
    private readonly bytes: Uint8Array,
    readonly license: string,
  ) {
    inspectWav(bytes);
    this.version = hash(bytes);
  }
  async synthesize(): Promise<Uint8Array> {
    return this.bytes;
  }
}
export class CommandVoiceProvider implements VoiceProvider {
  readonly cacheIdentity: string;
  constructor(
    readonly id: string,
    readonly version: string,
    readonly license: string,
    private readonly executable: string,
    private readonly args: string[],
  ) {
    if (!id.trim() || !version.trim() || !license.trim() || !executable.trim())
      throw new Error("Proveedor sin identidad/versión/licencia/comando");
    this.cacheIdentity = hash(canonical({ executable, args }));
  }
  async synthesize(request: AudioRequest): Promise<Uint8Array> {
    const proc = Bun.spawn([this.executable, ...this.args], {
      stdin: new Blob([JSON.stringify(request)]),
      stdout: "pipe",
      stderr: "pipe",
    });
    const [bytes, stderr, code] = await Promise.all([
      new Response(proc.stdout).arrayBuffer(),
      new Response(proc.stderr).text(),
      proc.exited,
    ]);
    if (code !== 0)
      throw new Error(`TTS local falló (${code}): ${stderr.slice(0, 1000)}`);
    return new Uint8Array(bytes);
  }
}
export async function produceAudio(
  cache: string,
  request: AudioRequest,
  provider: VoiceProvider,
): Promise<{
  path: string;
  sha256: string;
  duration: number;
  cached: boolean;
}> {
  const key = hash(
    canonical({
      request,
      provider: {
        id: provider.id,
        version: provider.version,
        license: provider.license,
        configuration: provider.cacheIdentity ?? null,
      },
    }),
  );
  const path = join(cache, `${key}.wav`);
  let bytes: Uint8Array;
  let cached = true;
  try {
    bytes = await readFile(path);
    inspectWav(bytes);
    const meta = JSON.parse(await readFile(`${path}.json`, "utf8")) as {
      sha256: string;
    };
    if (meta.sha256 !== hash(bytes)) throw new Error("Cache de audio alterada");
  } catch {
    cached = false;
    bytes = await provider.synthesize(request);
    inspectWav(bytes);
    await atomicWrite(path, bytes);
    await atomicWrite(
      `${path}.json`,
      JSON.stringify({
        sha256: hash(bytes),
        request,
        provider: provider.id,
        version: provider.version,
      }),
    );
  }
  return {
    path,
    sha256: hash(bytes),
    duration: inspectWav(bytes).duration,
    cached,
  };
}
export async function validateAudio(root: string, path: string) {
  return inspectWav(await readFile(await sourceFile(root, path)));
}
export function subtitles(lines: { text: string; duration: number }[]): string {
  const stamp = (seconds: number): string => {
    const ms = Math.round(seconds * 1000);
    return (
      `${Math.floor(ms / 3600000)
        .toString()
        .padStart(2, "0")}:${Math.floor(ms / 60000) % 60}`.replace(
        /:(\d)$/,
        ":0$1",
      ) +
      `:${(Math.floor(ms / 1000) % 60).toString().padStart(2, "0")},${(ms % 1000).toString().padStart(3, "0")}`
    );
  };
  let start = 0;
  return lines
    .map((l, i) => {
      if (l.duration <= 0 || !l.text.trim())
        throw new Error("Subtítulo inválido");
      const end = start + l.duration;
      const out = `${i + 1}\n${stamp(start)} --> ${stamp(end)}\n${l.text}\n`;
      start = end;
      return out;
    })
    .join("\n");
}

/** Normaliza el pico PCM; no equivale a normalización perceptual LUFS. */
export function normalizePeak(data: Uint8Array, targetDbFS = -3): Uint8Array {
  inspectWav(data);
  if (targetDbFS > 0 || targetDbFS < -30)
    throw new Error("Objetivo de pico fuera de rango");
  const b = Buffer.from(data);
  let bits = 0;
  const chunks: { start: number; length: number }[] = [];
  for (let p = 12; p + 8 <= b.length; ) {
    const n = b.readUInt32LE(p + 4);
    const tag = b.toString("ascii", p, p + 4);
    if (tag === "fmt ") bits = b.readUInt16LE(p + 22);
    if (tag === "data") chunks.push({ start: p + 8, length: n });
    p += 8 + n + (n % 2);
  }
  const width = bits / 8;
  let peak = 0;
  for (const chunk of chunks) {
    if (chunk.length % width) throw new Error("PCM sin muestras completas");
    for (let p = chunk.start; p < chunk.start + chunk.length; p += width)
      peak = Math.max(peak, Math.abs(b.readIntLE(p, width)));
  }
  if (!peak) return new Uint8Array(b);
  const maximum = 2 ** (bits - 1) - 1;
  const gain = (maximum * 10 ** (targetDbFS / 20)) / peak;
  for (const chunk of chunks)
    for (let p = chunk.start; p < chunk.start + chunk.length; p += width)
      b.writeIntLE(
        Math.max(
          -maximum,
          Math.min(maximum, Math.round(b.readIntLE(p, width) * gain)),
        ),
        p,
        width,
      );
  return new Uint8Array(b);
}

export async function convertPcm(
  source: string,
  target: string,
  executable = "ffmpeg",
): Promise<{ sha256: string; duration: number }> {
  const proc = Bun.spawn(
    [
      executable,
      "-nostdin",
      "-v",
      "error",
      "-y",
      "-i",
      source,
      "-ac",
      "1",
      "-ar",
      "48000",
      "-c:a",
      "pcm_s16le",
      target,
    ],
    { stdout: "pipe", stderr: "pipe" },
  );
  const [stderr, code] = await Promise.all([
    new Response(proc.stderr).text(),
    proc.exited,
  ]);
  if (code !== 0) throw new Error(`Conversión WAV falló: ${stderr}`);
  const bytes = await readFile(target);
  return { sha256: hash(bytes), duration: inspectWav(bytes).duration };
}
