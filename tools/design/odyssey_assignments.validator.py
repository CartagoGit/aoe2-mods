"""Audit designated mechanical work against episode identity and chronological order."""

import re
import runpy
from pathlib import Path

authored_dossier_status = runpy.run_path(
    str(Path(__file__).with_name("odyssey_catalog.helper.py"))
)["authored_dossier_status"]



def audit_authoring_dependencies(slices, episode_slices, promotion):
    """Audit work dependencies independently of the player's canonical order.

    Legacy serial work and source work after shared metadata are both valid.
    Promotion must transitively await every episode in either graph.
    """
    errors = []
    graph = {}
    for sid, body in slices.items():
        declarations = re.findall(r"(?m)^- \*\*DependsOn\*\*: (.+)$", body)
        if not declarations:
            graph[sid] = []
            continue
        if len(declarations) != 1 or not re.fullmatch(
            r"\[(?:S\d+(?:,\s*S\d+)*)?\]", declarations[0]
        ):
            errors.append(f"{sid}: malformed or repeated dependency declaration")
            graph[sid] = []
            continue
        dependencies = re.findall(r"S\d+", declarations[0])
        graph[sid] = dependencies
        if len(set(dependencies)) != len(dependencies):
            errors.append(f"{sid}: duplicate dependency")
        for dependency in dependencies:
            if dependency not in slices:
                errors.append(f"{sid}: unknown dependency {dependency}")

    ancestors = {}
    visiting = set()

    def visit(sid):
        if sid in ancestors:
            return ancestors[sid]
        if sid in visiting:
            errors.append(f"{sid}: dependency cycle")
            return set()
        visiting.add(sid)
        reachable = set()
        for dependency in graph.get(sid, []):
            if dependency in graph:
                reachable.add(dependency)
                reachable.update(visit(dependency))
        visiting.remove(sid)
        ancestors[sid] = reachable
        return reachable

    for sid in graph:
        visit(sid)
    if graph.get("S1") or "S1" not in ancestors.get("S2", set()):
        errors.append("metadata: S1 must be a root and precede S2")
    for sid in episode_slices:
        if "S2" not in ancestors.get(sid, set()):
            errors.append(f"{sid}: authoring dependency bypasses shared metadata S2")
    missing = set(episode_slices) - ancestors.get(promotion, set())
    if missing:
        errors.append("promotion precedes required episodes: " + ", ".join(sorted(missing)))
    return errors


def audit_assignments(root, campaigns, assignments):
    errors = []
    by_campaign = {campaign["campaignId"]: campaign for campaign in campaigns}
    for assignment in assignments["assignments"]:
        cid = assignment["campaignId"]
        campaign = by_campaign[cid]
        episodes = campaign["episodeSelection"]
        rows = assignment.get("episodeSlices", [])
        selected = {episode["id"]: episode for episode in episodes}
        for row in rows:
            expected_status = authored_dossier_status(campaign, row["episodeId"])
            if (row.get("dossierStatus") != expected_status
                    or selected.get(row["episodeId"], {}).get("contractStatus") != expected_status):
                errors.append(f"{cid}/{row['episodeId']}: dossier status diverges from authored draft coverage")
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
        errors.extend(
            f"{cid}: {error}" for error in audit_authoring_dependencies(
                slices, [row["sliceId"] for row in rows], assignment["promotionSlice"]
            )
        )
        for row in rows:
            body = slices.get(row["sliceId"], "")
            if (
                f"- **ScenarioId**: {row['episodeId']}\n" not in body
                or f"- **Order**: {row['order']}\n" not in body
            ):
                errors.append(
                    f"{cid}/{row['sliceId']}: proposal identity/order diverges"
                )
        expected = {"S1", "S2", assignment["promotionSlice"]} | {
            row["sliceId"] for row in rows
        }
        if len(sections[1::2]) != len(slices) or set(slices) != expected:
            errors.append(f"{cid}: duplicate, missing or undesignated slices")
    if {row["campaignId"] for row in assignments["assignments"]} != set(by_campaign):
        errors.append("Missing odyssey assignment")
    return errors
