import { expect, test } from "bun:test";
import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import {
  CommandVoiceProvider,
  inspectWav,
  produceAudio,
  RecordedVoiceProvider,
  subtitles,
} from "../../packages/audio";

function wav() {
  const b = Buffer.alloc(44 + 32000);
  b.write("RIFF");
  b.writeUInt32LE(b.length - 8, 4);
  b.write("WAVEfmt ", 8);
  b.writeUInt32LE(16, 16);
  b.writeUInt16LE(1, 20);
  b.writeUInt16LE(1, 22);
  b.writeUInt32LE(16000, 24);
  b.writeUInt32LE(32000, 28);
  b.writeUInt16LE(2, 32);
  b.writeUInt16LE(16, 34);
  b.write("data", 36);
  b.writeUInt32LE(32000, 40);
  return b;
}
test("WAV PCM y duración", () => {
  expect(inspectWav(wav()).duration).toBe(1);
  expect(() => inspectWav(wav().subarray(0, 50))).toThrow();
});
test("WAV rechaza alineación, frames y chunks incompletos", () => {
  const misaligned = wav();
  misaligned.writeUInt16LE(0, 32);
  expect(() => inspectWav(misaligned)).toThrow("PCM inconsistente");
  const partialFrame = wav();
  partialFrame.writeUInt32LE(31999, 40);
  expect(() => inspectWav(partialFrame)).toThrow("WAV sin audio válido");
  const trailing = Buffer.concat([wav(), Buffer.alloc(1)]);
  trailing.writeUInt32LE(trailing.length - 8, 4);
  expect(() => inspectWav(trailing)).toThrow("chunk incompleta");
  const missingPadding = wav().subarray(0, 32043);
  missingPadding.writeUInt32LE(missingPadding.length - 8, 4);
  missingPadding.writeUInt32LE(31999, 40);
  expect(() => inspectWav(missingPadding)).toThrow("WAV truncado");
});
test("proveedores de comando aíslan identidad y argumentos en caché", async () => {
  const cache = await mkdtemp(join(tmpdir(), "cdf-command-audio-"));
  try {
    const request = {
      text: "Hola",
      locale: "es-ES",
      voice: "narrator",
      delivery: "normal",
      rate: 1,
      pronunciation: {},
    };
    const a = wav();
    const b = wav();
    b.writeInt16LE(1234, 44);
    const args = (bytes: Buffer) => [
      "-e",
      `process.stdout.write(Buffer.from("${bytes.toString("base64")}", "base64"))`,
    ];
    const provider = (id: string, bytes: Buffer) =>
      new CommandVoiceProvider(
        id,
        "1",
        "Original",
        process.execPath,
        args(bytes),
      );
    const first = await produceAudio(cache, request, provider("voice-a", a));
    const otherId = await produceAudio(cache, request, provider("voice-b", a));
    expect(otherId.cached).toBe(false);
    expect(otherId.path).not.toBe(first.path);
    const otherArgs = await produceAudio(
      cache,
      request,
      provider("voice-a", b),
    );
    expect(otherArgs.cached).toBe(false);
    expect(otherArgs.sha256).not.toBe(first.sha256);
    expect(
      (await produceAudio(cache, request, provider("voice-a", b))).cached,
    ).toBe(true);
  } finally {
    await rm(cache, { recursive: true, force: true });
  }
});
test("cache por contenido, voz y proveedor", async () => {
  const path = await mkdtemp(join(tmpdir(), "cof-audio-"));
  try {
    const provider = new RecordedVoiceProvider(wav(), "Original");
    const request = {
      text: "Hola",
      locale: "es-ES",
      voice: "narrator",
      delivery: "normal",
      rate: 1,
      pronunciation: {},
    };
    const first = await produceAudio(path, request, provider);
    expect(first.cached).toBe(false);
    expect((await produceAudio(path, request, provider)).cached).toBe(true);
    await writeFile(first.path, Buffer.from("corrupted"));
    expect((await produceAudio(path, request, provider)).cached).toBe(false);
    expect(inspectWav(await Bun.file(first.path).bytes()).duration).toBe(1);
    expect(
      (await produceAudio(path, { ...request, voice: "other" }, provider)).path,
    ).not.toBe(first.path);
  } finally {
    await rm(path, { recursive: true, force: true });
  }
});
test("SRT sincronizado", () => {
  expect(
    subtitles([
      { text: "Primero", duration: 1.5 },
      { text: "Segundo", duration: 2 },
    ]),
  ).toContain("00:00:01,500 --> 00:00:03,500");
});

test("normalización de pico y silencio", async () => {
  const { normalizePeak } = await import("../../packages/audio");
  const data = wav();
  data.writeInt16LE(1000, 44);
  const result = Buffer.from(normalizePeak(data, -6));
  expect(result.readInt16LE(44)).toBeCloseTo(
    Math.round(32767 * 10 ** (-6 / 20)),
    0,
  );
  expect(inspectWav(normalizePeak(wav())).duration).toBe(1);
});
