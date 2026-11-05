"""Check an internal finite-choice study without authoring campaign content."""

import argparse
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
build_report = runpy.run_path(str(Path(__file__).with_name("finite_allocation.helper.py")))["build_report"]
DEFAULT_STEM = "docs/research/odyssey-research/imperial34-care-allocation"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", default=f"{DEFAULT_STEM}-plan.json")
    parser.add_argument("--output", default=f"{DEFAULT_STEM}-audit.json")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    source, output = (ROOT / args.plan).resolve(), (ROOT / args.output).resolve()
    default_output = (ROOT / f"{DEFAULT_STEM}-audit.json").resolve()
    if output.is_relative_to(ROOT) and output != default_output and not output.is_relative_to(ROOT / "build"):
        raise ValueError("Repository reports belong at the designated report or under build")
    if source == output:
        raise ValueError("A report must not overwrite its plan")
    report = build_report(json.loads(source.read_text(encoding="utf-8")))
    serialized = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        output.write_text(serialized, encoding="utf-8")
    elif not output.exists() or output.read_text(encoding="utf-8") != serialized:
        raise ValueError("Stale finite-allocation study; review inputs before --write")
    print("Finite allocation candidate:", report["combinationCount"], "combinations; all-skip easy/standard/hard:",
          "/".join(str(report["profiles"][level]["allSkipAffordableCount"]) for level in ("easy", "standard", "hard")),
          "; nativeImplemented=false; gameVerified=false")


if __name__ == "__main__":
    main()
