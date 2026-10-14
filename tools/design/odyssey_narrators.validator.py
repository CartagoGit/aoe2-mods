"""Audit fictional voice identity and knowledge limits; never certify history or audio."""

LOCALES = {"en", "es-ES"}
PERSONAL_FIELDS = (
    "name", "profession", "temperament", "backstory", "spokenRegister",
    "blindSpot", "refrain", "samplePersonalVoice",
)
KNOWLEDGE_MODES = {
    "inherited-account", "received-report", "received-reports-with-childhood-limit",
    "fictional-local-life-plus-received-reports",
}


def audit_narrators(document, campaigns):
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def localized(value):
        return isinstance(value, dict) and set(value) == LOCALES and all(
            isinstance(text, str) and text.strip() for text in value.values()
        )

    require(document.get("sourceLocale") == "en", "Narrators: English source required")
    common = document.get("commonNarrator", {})
    require(common.get("id") == "collection-narrator", "Shared factual narrator identity changed")
    require(common.get("sequence") == [
        "factual-date-place-event", "relevant-evidence-uncertainty", "handover",
        "campaign-personal-interpretation",
    ], "Factual narrator must hand over before personal interpretation")
    require(common.get("sameSpeakerAcrossCampaigns") is True, "Shared narrator differs between campaigns")
    require(localized(common.get("role")), "Shared narrator needs bilingual role")
    by_campaign = {campaign["campaignId"]: campaign for campaign in campaigns}
    narrators = document.get("narrators", [])
    require(len(narrators) == len(by_campaign), "One expanded narrator required per campaign")
    require({n.get("campaignId") for n in narrators} == set(by_campaign), "Narrator campaign coverage differs")
    require(len({n.get("id") for n in narrators}) == len(narrators), "Personal narrator IDs must be distinct")
    require(len({n.get("campaignId") for n in narrators}) == len(narrators), "Duplicate campaign narrator")
    for narrator in narrators:
        cid = narrator.get("campaignId")
        campaign = by_campaign.get(cid)
        if campaign is None:
            continue
        require(narrator.get("id") == campaign["editorialContract"]["narratorId"], f"{cid}: narrator identity differs from editorial contract")
        require(narrator.get("fictional") is True, f"{cid}: invented persona presented as historical witness")
        birth, death = narrator.get("birthYearApprox"), narrator.get("deathYearApprox")
        require(type(birth) is int and type(death) is int and birth < death, f"{cid}: invalid narrator lifespan")
        for field in PERSONAL_FIELDS:
            require(localized(narrator.get(field)), f"{cid}: missing bilingual {field}")
        require(bool(narrator.get("fictionalItinerary")) and all(
            row.get("classification") == "author-created personal biography, never historical witness evidence"
            and row.get("place") and row.get("knowledgeAccess")
            for row in narrator.get("fictionalItinerary", [])
        ), f"{cid}: fictional itinerary evidence boundary missing")
        acts = narrator.get("fiveActEmotionalArc", [])
        require([row.get("actId") for row in acts] == [row["id"] for row in campaign["acts"]], f"{cid}: emotional arc must cover the five ordered acts")
        require(all(localized(row.get("personalDevelopment")) for row in acts), f"{cid}: missing bilingual act development")
        require(len(narrator.get("knowledgeBoundaries", [])) >= 3, f"{cid}: knowledge limits missing")
        require(narrator.get("portrait", {}).get("productionApproved") is False, f"{cid}: unreviewed portrait declared production approved")
        require(set(narrator.get("delivery", {}).get("languages", [])) == LOCALES, f"{cid}: delivery locales differ")
        require(bool(narrator.get("approvalStatus")) and "pending" in narrator["approvalStatus"], f"{cid}: fictional design must retain pending review")
        plan = narrator.get("episodeKnowledgePlan", [])
        selections = campaign["episodeSelection"]
        require(len(plan) == len(selections), f"{cid}: episode knowledge coverage incomplete")
        for row, episode in zip(plan, selections):
            label = f"{cid}/{episode['id']}"
            for key, expected in (
                ("scenarioId", episode["id"]), ("order", episode["order"]),
                ("actId", episode["actId"]), ("historicalDate", episode["date"]),
                ("geographyId", episode["geographyId"]),
            ):
                require(row.get(key) == expected, f"{label}: knowledge plan {key} drift")
            require(row.get("mode") in KNOWLEDGE_MODES, f"{label}: unsupported knowledge mode")
            require(localized(row.get("access")), f"{label}: bilingual knowledge access missing")
            require(row.get("historicalEyewitnessClaimAllowed") is False and row.get("biographyIsEvidence") is False, f"{label}: fictional biography became historical witness evidence")
            require(row.get("completeDossierPlacementRequired") is True, f"{label}: scene placement cannot be inferred from lifespan")
        if cid == "imperial-church":
            require(bool(narrator.get("migration")) and birth == 334 and death == 403, "Marcus expanded chronology migration missing")
            require(all(row.get("mode") == "inherited-account" for row in plan[:20]), "Marcus cannot remember early imperial episodes")
        if cid == "faith-origins":
            require(all(row.get("mode") == "inherited-account" for row in plan[:29]), "Miriam cannot remember pre-birth episodes")
    return errors
