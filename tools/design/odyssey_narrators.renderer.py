"""Render explicit persona bibles without treating fictional biography as evidence."""

import json


def render_narrator(campaign, narrator, common):
    def pair(value):
        return f"EN: {value['en']}\n\nES: {value['es-ES']}"

    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", "<br>")

    body = [
        f"# {narrator['name']['en']} / {narrator['name']['es-ES']}", "",
        f"{campaign['editorialContract']['campaignTitle']['en']} · `{narrator['id']}` · c. {narrator['birthYearApprox']}–{narrator['deathYearApprox']} CE", "",
        "Expanded odyssey voice bible. Architect-authored fiction; independent editorial, native and audio review pending. This biography is not an ancient source or evidence of a historical eyewitness. It does not approve any scenario or portrait.", "",
        "## Common narrator and handover", "", pair(common["role"]), "",
        " → ".join(common["sequence"]), "", common["causePolicy"], "", common["modernEvidence"], "",
        "## Personal history and delivery", "",
    ]
    for field in ("profession", "temperament", "backstory", "spokenRegister", "blindSpot", "refrain", "samplePersonalVoice"):
        body += [f"### {field}", "", pair(narrator[field]), ""]
    body += ["The sample voice is invented prose, never an authentic historical quotation.", "", "## Five-act emotional development", ""]
    for act in narrator["fiveActEmotionalArc"]:
        body += [f"### {act['actId']}", "", pair(act["personalDevelopment"]), ""]
    body += ["## Fictional itinerary and limits", "", "```json", json.dumps({
        "itinerary": narrator["fictionalItinerary"], "knowledgeBoundaries": narrator["knowledgeBoundaries"],
        "migration": narrator["migration"], "personalImagery": narrator["personalImagery"],
        "portrait": narrator["portrait"], "delivery": narrator["delivery"],
    }, ensure_ascii=False, indent=2), "```", "", "## Knowledge framing for every episode", "",
        "Every row requires scene-specific placement in its complete dossier. Ordinary fictional local life never grants access to private councils, revelation, a sacred figure’s mind or a distant battle. Historical facts stay attributed to sources in the common voice; the campaign persona adds explicitly situated interpretation.", "",
        "| Order / scenario | Date / place | Framing | Access EN / ES |", "|---|---|---|---|",
    ]
    for row in narrator["episodeKnowledgePlan"]:
        body.append("| " + " | ".join(cell(value) for value in (
            f"{row['order']} / {row['scenarioId']}", f"{row['historicalDate']} / {row['geographyId']}",
            row["mode"], f"{row['access']['en']} / {row['access']['es-ES']}",
        )) + " |")
    body += ["", "[Editable source](odyssey-narrators.json) · [Campaign selection](../odysseys/" + campaign["campaignId"] + ".json)", ""]
    return "\n".join(body)
