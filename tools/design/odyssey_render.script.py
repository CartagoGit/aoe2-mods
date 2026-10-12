"""Render honest selection/research status; never certify unfinished missions."""

import argparse
import importlib.util
import json
from pathlib import Path

helper_path = Path(__file__).with_name("odyssey_catalog.helper.py")
spec = importlib.util.spec_from_file_location("odyssey_catalog_helper", helper_path)
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def render(check=False):
    policy, campaigns = catalog.odyssey_catalog()
    failures = catalog.audit_selections(policy, campaigns)
    if failures:
        raise ValueError("\n".join(failures))
    outputs = {}
    index = [
        "# Historical odyssey selections",
        "",
        "273 selected episodes across nine campaigns. This is an editorial selection, not 273 completed dossiers or playable maps. The approved baseline catalogue still contains 39 historical missions. Source checks, complete objectives, map footprints, all player-facing text and native difficulty calibration remain separate acceptance gates.",
        "",
        "Each campaign has five acts and its own situated fictional narrator. The shared factual narrator opens and closes each episode before yielding to that person. English titles are the source; Spanish titles are supplied. The original raw corpus preserves research provenance even when an architect correction supersedes a candidate.",
        "",
        "| Campaign | Selected episodes | Acts | Source-check annotations | Authored expanded drafts | Approved expanded dossiers |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for campaign in campaigns:
        cid = campaign["campaignId"]
        editorial = campaign["editorialContract"]
        episodes = campaign["episodeSelection"]
        audited = sum(
            bool(
                e["historicalSelection"].get("researchAudit")
                or e["historicalSelection"].get("auditedSourcePassages")
                or e["historicalSelection"].get("sourceConsultation")
            )
            for e in episodes
        )
        complete = sum(
            e.get("contractStatus") == "approved-complete-dossier" for e in episodes
        )
        index.append(
            f"| [{cell(editorial['campaignTitle']['en'])}](../wiki/{cid}/14-odyssey-arc.md) | {len(episodes)} | 5 | {audited} | {len(campaign.get('episodes', []))} | {complete} |"
        )
        body = [
            f"# {editorial['campaignTitle']['en']} / {editorial['campaignTitle']['es-ES']}",
            "",
            f"`{cid}` · {editorial['publicId']} · {len(episodes)} selected episodes · source locale `en`",
            "",
            "**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.",
            "",
            "## Campaign voice and continuity",
            "",
            "```json",
            json.dumps(
                {"editorial": editorial, "continuity": campaign["continuityContract"]},
                ensure_ascii=False,
                indent=2,
            ),
            "```",
            "",
            "Only the final expanded episode may complete this campaign or present the successor recommendation. Former baseline finales become intermediate episodes when later episodes exist. Preserve every existing semantic scenario ID; display order is a separate field.",
            "",
        ]
        for act in campaign["acts"]:
            body += [
                f"## {act['id']}: {act['title']['en']} / {act['title']['es-ES']}",
                "",
                f"Historical year band: {act['historicalYearBand']}. {act['dramaticPurpose']}",
                "",
                "| Order / semantic ID | English / Español | Date | Local geography | Main operation |",
                "|---|---|---|---|---|",
            ]
            for e in episodes:
                if e["actId"] == act["id"]:
                    body.append(
                        "| "
                        + " | ".join(
                            cell(v)
                            for v in [
                                f"{e['order']} / {e['id']}",
                                f"{e['title']['en']} / {e['title']['es-ES']}",
                                e["date"],
                                e["geographyId"],
                                e["coreMechanic"],
                            ]
                        )
                        + " |"
                    )
            body += [
                "",
                "The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.",
                "",
                "```json",
                json.dumps(act["difficultyCurve"], ensure_ascii=False, indent=2),
                "```",
                "",
            ]
        body += ["## Episode source and knowledge ledger", ""]
        for e in episodes:
            h = e["historicalSelection"]
            body += [
                f"### {e['order']}. {e['title']['en']}",
                "",
                f"[Candidate source]({h['sourceUrl']}): {h['passage']}",
                "",
                "Research candidate (not yet approved narration): "
                + h["candidateEvent"],
                "",
                h["qualification"],
                "",
                f"Knowledge: {e['knowledgeBasis']['mode']}. {e['locationPolicy']}",
                "",
                f"Dossier status: {e['contractStatus']}",
                "",
            ]
            if any(draft["id"] == e["id"] for draft in campaign.get("episodes", [])):
                body += [
                    f"[Authored episode dossier](episodes/{e['id']}/15-odyssey-dossier.md) — independent approval pending",
                    "",
                ]
            if h.get("selectedClaim"):
                body += [
                    "Architect-corrected claim EN: " + h["selectedClaim"]["en"],
                    "",
                    "ES: " + h["selectedClaim"]["es-ES"],
                    "",
                ]
            for passage in h.get("auditedSourcePassages", []):
                body += [
                    f"[Corrected primary passage]({passage['url']}): {passage['passage']}. {passage['caution']}",
                    "",
                ]
            if h.get("sourceConsultation"):
                row = h["sourceConsultation"]
                body += [
                    (f"[Consulted source]({row['consultedUrl']}): {row['passage']}" if row.get("consultedUrl") else "Source consultation pending: " + row["passage"]),
                    "",
                    "Limit: " + row["limitations"],
                    "",
                    "Status: " + row["status"],
                    "",
                ]
            for row in h.get("additionalConsultations", []):
                body += [
                    f"[Additional consulted passage]({row['consultedUrl']}): {row['passage']}",
                    "",
                    "Limit: " + row["limitations"],
                    "",
                ]
            if h.get("researchAudit"):
                row = h["researchAudit"]
                body += [
                    f"[Source-audit passage]({row['correctUrlConsulted']}): {row['passage']}",
                    "",
                    row["supportedClaim"],
                    "",
                    "Limit: " + row["problems"],
                    "",
                    "Coverage: " + row["coverageRead"],
                    "",
                ]
        outputs[f"docs/wiki/{cid}/14-odyssey-arc.md"] = "\n".join(body)
    index += [
        "",
        "Every episode must receive 6–8 optional objectives, at least four secondary mechanics and three combinable playstyles. Optional loss cannot defeat a main objective; rewards require unique delivery receipts, finite reserved stock and atomic persistent completion. Main success must remain feasible when all optional tasks are skipped.",
        "",
        "The catalogue currently has 234 authored optional objectives for the 39 baseline historical missions. No generated title table proves the 273 extended scenarios have these contracts already.",
        "",
        "[Production plan](odyssey-production-plan.md) · [Policy](odyssey-policy.json) · [Baseline catalogue](README.md) · [Research provenance](../research/odyssey-research/README.md)",
        "",
        "Regenerate: `python3 tools/design/odyssey_render.script.py`. Check: `python3 tools/design/odyssey_render.script.py --check`. No native scenarios are emitted.",
        "",
    ]
    outputs["docs/design/odyssey-selections.md"] = "\n".join(index)
    for relative, text in outputs.items():
        path = catalog.ROOT / relative
        if check:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                raise ValueError(f"Stale odyssey document:{relative}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    print(
        f"Checked {len(campaigns)} campaigns / {sum(len(c['episodeSelection']) for c in campaigns)} selections; expanded dossiers not certified"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    render(parser.parse_args().check)
