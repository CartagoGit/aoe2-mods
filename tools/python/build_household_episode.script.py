"""Build the episode-02 household controller on a separately labelled synthetic fixture.

The architect's private binding draft for `02-civilian-refuge-jerusalem` is not
approved for a historical build: it carries no approved topographic/route
decision, no native elevation and no footprint inspection, and its empty
`map.corridors` leave the guide circuit's `mark-alternative-route` effect
without its authored relief corridor. Those are blockers, not instructions to
paint a flat open map or to reuse the coastal painter.

This builder therefore has **no code path that can emit a historical Jerusalem
campaign, container or mod**. It verifies the real authored source through the
binding's own pins, reports the exact historical-build blockers, and compiles
the household ledger controller on a separately labelled synthetic physical
frame that is not the Jerusalem map and not a historical build.

The household adapter stays the only household-ledger controller; this script
reuses it, the shared native base factory, the shared spatial and transaction
helpers and the optional-circuit adapter instead of copying any of them. The
base envelope and the native write/reopen/signature/XS verification are the
shared private services, so this builder and the private geographic preview
cannot drift apart; the labels, the source checks, the exact controller XS,
the semantic signature and the unconditional historical-build refusal stay
here. Source and XS inspection support compilation evidence only; they do not
execute the game engine.
"""

import argparse
import contextlib
import hashlib
import io
import json
import math
import runpy
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
native_signature = runpy.run_path(str(HERE / "native_signature.helper.py"))[
    "native_signature"
]
BASE_FACTORY = runpy.run_path(str(HERE / "private_household_base.factory.py"))
ARTIFACT_SERVICE = runpy.run_path(str(HERE / "private_native_artifact.service.py"))

SYNTHETIC_NOTICE = (
    "explicitly nonhistorical synthetic physical fixture for the episode-02 "
    "household controller; not the Jerusalem map, not an approved route, not a "
    "historical build and not a game-played mission"
)
SYNTHETIC_SCENARIO_ID = "faith-origins-02-household-synthetic-fixture"
SYNTHETIC_SIZE = 64
SYNTHETIC_BODY_ROWS = (16, 26, 36, 46)
SYNTHETIC_BODY_COLUMNS = (4, 16, 28, 40, 52)
SYNTHETIC_ZONE_ROWS = (8, 56)
SYNTHETIC_ZONE_COLUMNS = (8, 20, 32, 44, 56)
SYNTHETIC_CORRIDOR_WIDTH = 3


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _root_path(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("input path must stay in the source workspace")
    return path


def load_household_source(root, binding_path):
    """Verify the authored source through the binding's own pins; fail closed."""
    binding = json.loads(binding_path.read_text(encoding="utf8"))
    source = _root_path(root, binding["sourcePath"])
    if sha256(source) != binding["sourceSha256"]:
        raise ValueError(
            "household source hash mismatch; re-review the changed source"
        )
    campaign = json.loads(source.read_text(encoding="utf8"))
    dossier = campaign["episodes"][binding["sourceDossierIndex"]]
    if (
        campaign["campaignId"] != binding["campaignId"]
        or dossier["id"] != binding["episodeId"]
    ):
        raise ValueError("household source identity mismatch")
    for level, profile in binding["difficulty"].items():
        if (
            dossier["difficulty"][level]["startingResources"]
            != profile["startingResources"]
        ):
            raise ValueError(
                "native starting resources must match the authored profile"
            )
    return campaign, dossier, binding


def historical_build_blockers(binding):
    """Name the gates that keep this binding out of a historical build."""
    blockers = []
    readiness = binding.get("nativeReadiness") or {}
    if not readiness.get("bindingApprovedForHistoricalBuild"):
        blockers.append("the binding is not approved for a historical build")
    blockers.extend(readiness.get("blockedBy") or [])
    native_map = binding.get("map") or {}
    if not native_map.get("routeApproved"):
        blockers.append("no approved topographic/route decision")
    if not native_map.get("corridors"):
        blockers.append("no authored corridor geometry")
    if native_map.get("nativeElevation") is None:
        blockers.append("no native elevation assignment")
    if not binding.get("layoutEvidence"):
        blockers.append("no native footprint and approach inspection")
    seen = []
    for blocker in blockers:
        if blocker not in seen:
            seen.append(blocker)
    return seen


def refuse_historical_build(binding):
    """Refuse a historical build and name every missing gate."""
    blockers = historical_build_blockers(binding)
    raise ValueError(
        "historical Jerusalem build refused; missing gates: " + "; ".join(blockers)
    )


def _required_corridor_ids(dossier):
    """Every corridor the authored optional circuits actually reference."""
    corridor_ids = []
    for side in dossier["secondaryObjectives"]:
        for effect in side["effects"]:
            if effect["kind"] != "mark-alternative-route":
                continue
            corridor_id = effect.get("corridorId")
            if not isinstance(corridor_id, str) or not corridor_id:
                raise ValueError("the guide effect needs an authored corridor id")
            if corridor_id not in corridor_ids:
                corridor_ids.append(corridor_id)
    return corridor_ids


def _synthetic_positions(count):
    """A deterministic, nonhistorical body layout with separated centres."""
    slots = [
        (x, y)
        for y in SYNTHETIC_BODY_ROWS
        for x in SYNTHETIC_BODY_COLUMNS
    ]
    if count > len(slots):
        raise ValueError("the synthetic frame has no free body slot left")
    return slots[:count]


def _synthetic_zone_centres(count):
    """A deterministic, nonhistorical receiving-circle layout."""
    centres = [
        (x, y)
        for y in SYNTHETIC_ZONE_ROWS
        for x in SYNTHETIC_ZONE_COLUMNS
    ]
    if count > len(centres):
        raise ValueError("the synthetic frame has no free circle slot left")
    return centres[:count]


def _clearance(entities, zones):
    """Minimum distance from a body centre to any receiving-circle edge."""
    worst = None
    for entity in entities:
        for zone in zones:
            distance = math.dist(entity["position"], zone["centre"]) - zone["radius"]
            worst = distance if worst is None else min(worst, distance)
    return worst


def synthetic_physical_binding(binding, dossier):
    """Derive a separately labelled synthetic physical frame.

    Only the physical geometry is replaced. Identities, unit types, owners,
    bilingual labels, the household block, the optional payment costs, the
    authored narration order and the difficulty profiles stay exactly as the
    architect wrote them, so the adapter validates the same semantic contract.
    The real coordinates, the real hubs and the real terrain claims are
    discarded: they are not approved ground.
    """
    entities = [dict(entity) for entity in binding["entities"]]
    zones = [dict(zone) for zone in binding["zones"]]
    positions = _synthetic_positions(len(entities))
    centres = _synthetic_zone_centres(len(zones))
    for entity, position in zip(entities, positions):
        entity["position"] = [float(position[0]), float(position[1])]
        entity.pop("sourcePosition", None)
        entity.pop("sourceOffsetTiles", None)
        entity.pop("offsetTiles", None)
    for zone, centre in zip(zones, centres):
        zone["centre"] = [float(centre[0]), float(centre[1])]
        zone.pop("sourceOffsetTiles", None)
        zone.pop("offsetTiles", None)
    clearance = _clearance(entities, zones)
    if clearance < 3.0:
        raise ValueError(
            "the synthetic frame must keep every body outside every circle"
        )
    corridors = []
    for index, corridor_id in enumerate(_required_corridor_ids(dossier)):
        start = (6 + 12 * index, 30)
        corridors.append(
            {
                "id": corridor_id,
                "widthTiles": SYNTHETIC_CORRIDOR_WIDTH,
                "points": [[start[0], start[1]], [start[0] + 8, start[1] + 6]],
                "synthetic": True,
                "notice": "synthetic fixture geometry; no route is approved",
            }
        )
    synthetic = {
        key: value
        for key, value in binding.items()
        if key
        not in ("map", "entities", "zones", "layoutEvidence", "nativeReadiness")
    }
    synthetic.update(
        {
            "kind": "private-historical-household-native-binding",
            "schemaVersion": 1,
            "synthetic": True,
            "syntheticNotice": SYNTHETIC_NOTICE,
            "entities": entities,
            "zones": zones,
            "map": {
                "size": SYNTHETIC_SIZE,
                "corridors": corridors,
                "synthetic": True,
                "syntheticNotice": SYNTHETIC_NOTICE,
                "routeApproved": False,
                "nativeElevation": None,
            },
        }
    )
    return synthetic


def synthetic_base(binding, dossier, level):
    """Construct an explicit small supported v1 base envelope.

    The envelope construction itself is shared with the private geographic
    preview; this wrapper keeps the labelled synthetic fixture's own default:
    its 64 tile frame, its scenario identifier and no terrain of its own.
    """
    return BASE_FACTORY["build_private_household_base"](
        binding,
        dossier,
        level,
        scenario_id=SYNTHETIC_SCENARIO_ID,
    )


def label_synthetic_scenario(scenario, dossier, locale):
    """Keep the nonhistorical label inside the artifact, not only in the receipt."""
    screens = {screen["id"]: screen for screen in dossier["screens"]}
    goals = [
        objective["text"][locale]
        for objective in dossier["objectivePlan"] + dossier["secondaryObjectives"]
    ]
    scenario.message_manager.instructions = (
        SYNTHETIC_NOTICE
        + "\n\n"
        + dossier["title"][locale]
        + "\n\n"
        + "\n\n".join(goals)
    )
    scenario.message_manager.hints = "\n\n".join(
        screens[key]["text"][locale]
        for key in ("route-help", "economy-help", "recovery-help")
    )
    scenario.message_manager.history = (
        dossier["historicalBrief"][locale]
        + "\n\n"
        + dossier["dramatizationNotice"][locale]
    )
    scenario.message_manager.victory = "\n\n".join(
        screens[key]["text"][locale] for key in ("fact-outro", "persona-outro")
    )
    scenario.message_manager.loss = screens["defeat"]["text"][locale]


def build_variant(root, dossier, binding, output, locale, level, version):
    """Compile the household controller on the synthetic frame and prove it."""
    factory = runpy.run_path(str(HERE / "native_scenario.factory.py"))
    adapter = runpy.run_path(str(HERE / "native_household.adapter.py"))
    base, mapping = synthetic_base(binding, dossier, level)
    scenario, native_ids, _ = factory["create_native_scenario_base"](base, version)
    units = {
        entity_id: native_ids[native_name]
        for entity_id, native_name in mapping.items()
    }
    result = adapter["compile_household_controller"](
        scenario, units, dossier, binding, locale
    )
    label_synthetic_scenario(scenario, dossier, locale)
    xs_source = result.pop("xsSource")
    artifact = ARTIFACT_SERVICE["write_and_verify_artifact"](
        scenario, output, SYNTHETIC_SCENARIO_ID, xs_source=xs_source
    )
    result.update(
        {
            "scenario": artifact["scenario"],
            "scenarioSha256": artifact["scenarioSha256"],
            "locale": locale,
            "difficulty": level,
            "scenarioVersion": version,
            "syntheticFixture": True,
            "syntheticNotice": SYNTHETIC_NOTICE,
            "syntheticScenarioId": SYNTHETIC_SCENARIO_ID,
            "triggers": len(scenario.trigger_manager.triggers),
            "initialUnitCountIncludingMarkers": len(
                scenario.unit_manager.get_all_units()
            ),
            "status": (
                "synthetic household controller fixture; not a historical build, "
                "not a campaign release and not game verified"
            ),
            "historicalApproval": False,
            "generalComposedExportEnabled": False,
        }
    )
    (output / "native-receipt.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
    )
    return output / (SYNTHETIC_SCENARIO_ID + ".aoe2scenario"), result


def build_preview(
    root,
    binding_path,
    output,
    locales=("en", "es-ES"),
    levels=("easy", "standard", "hard"),
):
    """Build the synthetic fixture only; a historical build is always refused."""
    campaign, dossier, binding = load_household_source(root, binding_path)
    if any(locale not in binding["locales"] for locale in locales) or any(
        level not in binding["difficulty"] for level in levels
    ):
        raise ValueError("unsupported preview locale or difficulty")
    blockers = historical_build_blockers(binding)
    if not blockers:
        # A future approved binding still needs an explicit architect decision
        # before a historical build exists; this builder does not implement one.
        raise ValueError(
            "historical build refused; this builder only compiles the labelled "
            "synthetic fixture"
        )
    synthetic = synthetic_physical_binding(binding, dossier)
    version = json.loads((root / "config/engine.json").read_text())["scenarioVersion"]
    reports = []
    for locale in locales:
        for level in levels:
            folder = output / locale / level
            captured = io.StringIO()
            try:
                with contextlib.redirect_stdout(captured):
                    _, receipt = build_variant(
                        root, dossier, synthetic, folder, locale, level, version
                    )
            except Exception:
                print(captured.getvalue(), file=sys.stderr)
                raise
            reports.append(receipt)
    report = {
        "campaignId": campaign["campaignId"],
        "episodeId": dossier["id"],
        "sourceSha256": binding["sourceSha256"],
        "bindingSha256": sha256(binding_path),
        "syntheticFixture": True,
        "syntheticNotice": SYNTHETIC_NOTICE,
        "syntheticScenarioId": SYNTHETIC_SCENARIO_ID,
        "historicalBuild": {
            "attempted": False,
            "refused": True,
            "blockers": blockers,
        },
        "variants": reports,
        "gameVerified": False,
        "historicalApproval": False,
        "pending": [
            "an approved topographic and route decision for the real frame",
            "real native building footprint and approach inspection",
            "engine pathfinding, save/load and terminal arbitration evidence",
            "difficulty and reward utility calibration",
            "certified campaign UI/SequenceItems and release localization IDs",
        ],
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "preview-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
    )
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("binding", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--locale", choices=["en", "es-ES"], action="append")
    parser.add_argument(
        "--difficulty", choices=["easy", "standard", "hard"], action="append"
    )
    args = parser.parse_args()
    print(
        json.dumps(
            build_preview(
                args.root.resolve(),
                args.binding.resolve(),
                args.output.resolve(),
                args.locale or ("en", "es-ES"),
                args.difficulty or ("easy", "standard", "hard"),
            )
        )
    )


if __name__ == "__main__":
    main()
