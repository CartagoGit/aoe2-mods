import { projectFulfillmentDossiers } from "./fulfillment-dossier.mapper";

async function readStdin() {
  const chunks: Uint8Array[] = [];
  for await (const chunk of process.stdin) {
    chunks.push(typeof chunk === "string" ? Buffer.from(chunk) : chunk);
  }
  return Buffer.concat(chunks).toString("utf8");
}

export function runFulfillmentProjection(input: unknown) {
  return projectFulfillmentDossiers(input);
}

if (import.meta.main) {
  try {
    const input = JSON.parse(await readStdin()) as unknown;
    const result = runFulfillmentProjection(input);
    process.stdout.write(`${JSON.stringify(result)}\n`);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    process.stderr.write(`fulfillment-dossier projection failed: ${message}\n`);
    process.exitCode = 1;
  }
}
