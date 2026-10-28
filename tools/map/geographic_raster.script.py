"""Build an internal height candidate, with byte provenance and explicit gaps."""

import argparse
import hashlib
import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COMPILER = runpy.run_path(str(Path(__file__).with_name("geographic_raster.compiler.py")))


def verify_local_source(source):
    if source["sourceClassification"] == "synthetic-test":
        return False
    provenance = source.get("provenance", {})
    path, expected = provenance.get("localSourcePath"), provenance.get("sourceSha256")
    if not isinstance(path, str) or not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
        raise ValueError("Modern grid requires a local source path and SHA-256")
    artifact = (ROOT / path).resolve()
    if not artifact.is_relative_to(ROOT) or not artifact.is_file():
        raise ValueError("Source artifact must exist inside the project")
    digest = hashlib.sha256()
    with artifact.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    if digest.hexdigest() != expected:
        raise ValueError("Local source byte hash does not match reported provenance")
    notice = provenance.get("licenseNoticePath")
    if not isinstance(notice, str):
        raise ValueError("Modern grid requires a local license/provenance notice")
    notice_path = (ROOT / notice).resolve()
    if not notice_path.is_relative_to(ROOT) or not notice_path.is_file():
        raise ValueError("Local source notice is missing")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-grid", required=True)
    parser.add_argument("--bbox", nargs=4, type=float, required=True, metavar=("WEST", "SOUTH", "EAST", "NORTH"))
    parser.add_argument("--size", type=int, required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--allow-incomplete", action="store_true")
    args = parser.parse_args()
    input_path, output_path = Path(args.source_grid).resolve(), Path(args.output).resolve()
    if output_path == input_path:
        raise ValueError("Output cannot overwrite the source sample grid")
    raw = input_path.read_bytes()
    source = json.loads(raw)
    COMPILER["validate_source"](source)
    verified = verify_local_source(source)
    reported_path = source.get("provenance", {}).get("localSourcePath")
    if isinstance(reported_path, str) and output_path == (ROOT / reported_path).resolve():
        raise ValueError("Output cannot overwrite the original source artifact")
    candidate = COMPILER["compile_height_candidate"](source, args.bbox, args.size, args.allow_incomplete)
    candidate["sourceGridBytesSha256"] = hashlib.sha256(raw).hexdigest()
    candidate["localSourceHashVerified"] = verified
    if verified:
        candidate["sourceLicenseNoticeText"] = (ROOT / source["provenance"]["licenseNoticePath"]).read_text()
    candidate["sourceEvidenceLimit"] = "A matching original-file hash identifies that file; it does not verify extraction, georeference, units, history or resampling suitability."
    output_path.write_text(json.dumps(candidate, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(f"Height research candidate {args.size}x{args.size}; coverage={candidate['completeSampleCoverage']}; nativeTerrainWritten=false; gameVerified=false")


if __name__ == "__main__":
    main()
