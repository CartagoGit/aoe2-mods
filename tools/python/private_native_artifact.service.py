"""Write, reopen and verify one private native artifact.

The labelled synthetic fixture and the private geographic preview share one
verification operation: write the scenario, reopen the written file, compare
the complete semantic signature of the in-memory scenario and the reopened
file, and run the pinned XS check on the reopened file.

The comparison uses the shared complete signature, terrain included, so a
write that loses the derived relief is a failure and not a receipt line. A
caller cannot skip a step: the service either returns a verified artifact or
raises. It proves serialization and static XS validity only; it never
executes the game engine and never approves a historical build.
"""

import hashlib
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
native_signature = runpy.run_path(str(HERE / "native_signature.helper.py"))[
    "native_signature"
]

DEFAULT_XS_FILENAME = "native-controller.xs"


def sha256(path):
    """The SHA-256 of a file's bytes."""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_and_verify_artifact(
    scenario,
    output,
    scenario_id,
    *,
    xs_source,
    xs_filename=DEFAULT_XS_FILENAME,
):
    """Write one private artifact, reopen it and verify it.

    Returns the artifact facts the receipts need: the file names, the file
    hash, the round-trip result and the XS check result.
    """
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

    if not isinstance(xs_source, str) or not xs_source.strip():
        raise ValueError("a private artifact needs its controller XS source")
    directory = Path(output)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / (scenario_id + ".aoe2scenario")
    scenario.write_to_file(str(path))
    reopened = AoE2DEScenario.from_file(str(path))
    before, after = native_signature(scenario), native_signature(reopened)
    if before != after:
        differences = [key for key in before if before[key] != after[key]]
        raise RuntimeError(
            "native round-trip changed fields: " + ", ".join(differences)
        )
    reopened.xs_manager.xs_check.raise_on_error = True
    reopened.xs_manager.validate_scenario_xs()
    xs_path = directory / xs_filename
    xs_path.write_text(xs_source, encoding="utf8")
    return {
        "scenario": path.name,
        "scenarioSha256": sha256(path),
        "xsFile": xs_filename,
        "xsSha256": sha256(xs_path),
        "nativeRoundTripVerified": True,
        "nativeSignatureFieldsCompared": sorted(before),
        "xsChecked": True,
    }
