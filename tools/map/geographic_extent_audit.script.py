"""Report reference-extent coverage questions; do not approve geographic terrain."""

import argparse
import hashlib
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FRAME = runpy.run_path(str(Path(__file__).with_name("geographic_frame.helper.py")))
CATALOG = runpy.run_path(str(ROOT / "tools/design/odyssey_catalog.helper.py"))


def semantic_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def contains(parent, child):
    return parent[0] <= child[0] < child[2] <= parent[2] and parent[1] <= child[1] < child[3] <= parent[3]


def audit_episode(campaign_id, episode, profile):
    frame = FRAME["make_frame"](episode["mapPlan"]["bbox"], episode["mapSize"])
    centres, cells = frame.bounds_at(0, frame.size - 1), frame.bounds_at(-0.5, frame.size - 0.5)
    parent = profile["bbox"]
    requested_inside, centres_inside, cells_inside = (contains(parent, box) for box in (frame.bbox, centres, cells))
    return {"campaignId": campaign_id, "episodeId": episode["id"], "displayOrder": episode["order"],
            "geographyId": episode["geographyId"], "mapSize": episode["mapSize"],
            "requestedBBox": list(frame.bbox), "referenceBBox": parent,
            "paddedSampleCenterBounds": centres, "outerCellBounds": cells,
            "requestedBBoxWithinReference": requested_inside,
            "paddedSampleCentersWithinReference": centres_inside,
            "outerCellsWithinReference": cells_inside,
            "onlyOuterHalfCellExceedsReference": centres_inside and not cells_inside,
            "coverageReviewNeeded": not (requested_inside and cells_inside),
            "status": "reference extent question; no geographic/historical/native approval"}


def build_report(policy, campaigns, profiles, source_hashes):
    expected = {row["id"] for row in policy["campaigns"]}
    if len(campaigns) != len(expected) or {row["campaignId"] for row in campaigns} != expected:
        raise ValueError("Campaign sources do not match the existing odyssey policy")
    records, coverage = [], []
    for campaign in campaigns:
        episodes = campaign.get("episodes")
        if not isinstance(episodes, list):
            raise ValueError("Each campaign must explicitly declare its dossier list, including []")
        ids = [row["id"] for row in episodes]
        if len(set(ids)) != len(ids):
            raise ValueError("Duplicate authored episode identity")
        start = len(records)
        for episode in episodes:
            profile = profiles.get(episode["geographyId"])
            if not profile:
                raise ValueError(f"Missing geographic reference: {episode['geographyId']}")
            records.append(audit_episode(campaign["campaignId"], episode, profile))
        coverage.append({"campaignId": campaign["campaignId"], "authoredDossiers": len(episodes),
                         "selectedEpisodes": len(campaign["episodeSelection"]),
                         "extentQuestions": sum(row["coverageReviewNeeded"] for row in records[start:])})
    return {"schemaVersion": 1, "kind": "geographic-reference-extent-audit",
            "status": "coverage questions only; no source, terrain, native or gameplay approval",
            "referenceMeaning": "Regional source-control rectangle, not a political boundary, historical land mask or DEM coverage certificate.",
            "sourceSemanticHashes": source_hashes, "campaignCoverage": coverage,
            "authoredDossiers": len(records), "selectedEpisodes": sum(row["selectedEpisodes"] for row in coverage),
            "extentQuestions": sum(row["coverageReviewNeeded"] for row in records),
            "onlyOuterHalfCellQuestions": sum(row["onlyOuterHalfCellExceedsReference"] for row in records),
            "gameVerified": False, "records": records,
            "limits": ["Containment is arithmetic only. An inside result does not prove source coverage, ancient coastline, relief, walkability or actor packing.",
                       "An outside result requires coverage review; do not shrink a map or expand a historical source boundary merely to silence this report.",
                       "DEM interpolation needs sample-center coverage. Dated terrain/footprint layers need the full outer-cell envelope. They are different requirements.",
                       "Missing profiles or malformed frames fail rather than disappearing as apparently covered episodes. Zero-dossier campaigns remain explicit."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="Optional explicit generated report path; otherwise JSON goes to stdout")
    args = parser.parse_args()
    policy, campaigns = CATALOG["odyssey_catalog"]()
    failures = CATALOG["audit_selections"](policy, campaigns)
    if failures:
        raise ValueError("Existing catalogue validation failed: " + "; ".join(failures))
    profiles, hashes = {}, {"docs/design/odyssey-policy.json": semantic_hash(policy)}
    for path in ("docs/design/geography.json", "docs/research/odyssey-research/episode-geography.json"):
        data = json.loads((ROOT / path).read_text())
        hashes[path] = semantic_hash(data)
        profiles.update({row["id"]: row for row in data["profiles"]})
    for campaign in campaigns:
        hashes[f"docs/design/odysseys/{campaign['campaignId']}.json"] = semantic_hash(campaign)
    report = build_report(policy, campaigns, profiles, hashes)
    text = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if args.output:
        output = Path(args.output)
        # This optional artifact is generated output, not a campaign or source edit.
        destination = output.resolve()
        if destination.is_relative_to(ROOT) and not destination.is_relative_to(ROOT / "build"):
            raise ValueError("Generated extent reports inside the repository belong under build/")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text)
        print(f"Extent audit: {report['authoredDossiers']} drafts, {report['extentQuestions']} coverage questions; gameVerified=false")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
