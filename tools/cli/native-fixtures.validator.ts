import { pythonCommand } from "../../packages/aoe2-adapter/python-bridge.adapter";

export interface NativeFixtureReport {
  discovery: string;
  exitCode: number;
  testsRun: number;
  skipped: number;
  failures: number;
  errors: number;
  stdout: string;
  stderr: string;
  status: string;
}

const DISCOVERY_DIRECTORY = "tests/fixtures/native-history";
const DISCOVERY_PATTERN = "test_*.py";

/**
 * Run the native fixture discovery of the project and report what happened.
 *
 * The discovery uses the existing Python resolver and the pinned parser, XS
 * checker and toolchain of the project, rooted in the project directory. An
 * empty discovery is a failure: a green gate that ran nothing is not a
 * green gate. The actual stdout and stderr are preserved, and the actual
 * number of skipped cases is reported: a skipped native case is not a
 * verified native case.
 */
export async function validateNativeFixtures(
  root: string,
  directory = DISCOVERY_DIRECTORY,
  pattern = DISCOVERY_PATTERN,
): Promise<NativeFixtureReport> {
  const python = await pythonCommand(root);
  const proc = Bun.spawn(
    [python, "-m", "unittest", "discover", "-s", directory, "-p", pattern],
    { cwd: root, stdout: "pipe", stderr: "pipe" },
  );
  const [out, err, code] = await Promise.all([
    new Response(proc.stdout).text(),
    new Response(proc.stderr).text(),
    proc.exited,
  ]);
  const combined = `${err}\n${out}`;
  const ran = /Ran (\d+) tests?/.exec(combined);
  const testsRun = ran ? Number(ran[1]) : 0;
  const skipped = /skipped=(\d+)/.exec(combined);
  const failures = /failures=(\d+)/.exec(combined);
  const errors = /errors=(\d+)/.exec(combined);
  const report: NativeFixtureReport = {
    discovery: `${directory} ${pattern}`,
    exitCode: code,
    testsRun,
    skipped: skipped ? Number(skipped[1]) : 0,
    failures: failures ? Number(failures[1]) : 0,
    errors: errors ? Number(errors[1]) : 0,
    stdout: out,
    stderr: err,
    status: "native fixture discovery executed",
  };
  if (code !== 0)
    throw new Error(
      `Native fixture discovery (${code}): ${err}\n${out.slice(-4000)}`,
    );
  if (testsRun === 0)
    throw new Error(
      `Native fixture discovery found no test in ${report.discovery}; an empty discovery is not a verification`,
    );
  if (report.failures > 0 || report.errors > 0)
    throw new Error(
      `Native fixture discovery reported ${report.failures} failure(s) and ${report.errors} error(s)`,
    );
  report.status =
    report.skipped > 0
      ? `native fixture discovery executed ${testsRun} test(s); ${report.skipped} skipped case(s) are not verified cases`
      : `native fixture discovery executed ${testsRun} test(s) without a skip`;
  return report;
}
