"""Audit designated mechanical work against episode identity and chronological order."""

import re


def audit_assignments(root, campaigns, assignments):
    errors = []
    by_campaign = {campaign["campaignId"]: campaign for campaign in campaigns}
    for assignment in assignments["assignments"]:
        cid = assignment["campaignId"]
        campaign = by_campaign[cid]
        episodes = campaign["episodeSelection"]
        rows = assignment.get("episodeSlices", [])
        if [(row["episodeId"], row["order"], row["actId"]) for row in rows] != [
            (episode["id"], episode["order"], episode["actId"]) for episode in episodes
        ]:
            errors.append(f"{cid}: assigned episodes differ from canonical chronology")
        if len({row["sliceId"] for row in rows}) != len(rows):
            errors.append(f"{cid}: two episodes share one authoring slice")
        path = root / "docs/delendai/proposals" / assignment["path"]
        if not path.is_file():
            errors.append(f"{cid}: official proposal document missing")
            continue
        content = path.read_text(encoding="utf-8")
        sections = re.split(r"(?m)^### (S\d+) — ", content)
        slices = dict(zip(sections[1::2], sections[2::2]))
        previous = "S2"
        for row in rows:
            body = slices.get(row["sliceId"], "")
            if f"- **DependsOn**: [{previous}]" not in body:
                errors.append(
                    f"{cid}/{row['sliceId']}: authoring dependency breaks chronological order"
                )
            if (
                f"- **ScenarioId**: {row['episodeId']}\n" not in body
                or f"- **Order**: {row['order']}\n" not in body
            ):
                errors.append(
                    f"{cid}/{row['sliceId']}: proposal identity/order diverges"
                )
            previous = row["sliceId"]
        if f"- **DependsOn**: [{previous}]" not in slices.get(
            assignment["promotionSlice"], ""
        ):
            errors.append(f"{cid}: promotion precedes the final expanded episode")
        expected = {"S1", "S2", assignment["promotionSlice"]} | {
            row["sliceId"] for row in rows
        }
        if len(sections[1::2]) != len(slices) or set(slices) != expected:
            errors.append(f"{cid}: duplicate, missing or undesignated slices")
    if {row["campaignId"] for row in assignments["assignments"]} != set(by_campaign):
        errors.append("Missing odyssey assignment")
    return errors
