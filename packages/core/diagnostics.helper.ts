export type Issue = {
  code: string;
  path: string;
  message: string;
  severity: "error" | "warning";
};

export const issue = (
  code: string,
  path: string,
  message: string,
  severity: Issue["severity"] = "error",
): Issue => ({ code, path, message, severity });

export function assertValid(issues: Issue[]): void {
  const errors = issues.filter((i) => i.severity === "error");
  if (errors.length)
    throw new Error(
      errors.map((i) => `${i.code} ${i.path}: ${i.message}`).join("\n"),
    );
}

export function duplicates(values: string[]): string[] {
  return [...new Set(values.filter((x, i) => values.indexOf(x) !== i))];
}
