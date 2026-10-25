"""Rebuild explicit long-odyssey drafts and their readable episode wiki pages."""

import argparse
import html
import textwrap
import importlib.util
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def module(name):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).with_name(name + ".py")
    )
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


factory = module("episode_dossier.factory")
validator = module("episode_dossier.validator")
layers_helper = module("geographic_layers.helper")
catalog = module("odyssey_catalog.helper")
fulfillment = module("fulfillment-dossier.helper")
frame_helper = runpy.run_path(str(ROOT / "tools/map/geographic_frame.helper.py"))


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def emit(path, text, check):
    file = ROOT / path
    if check:
        if not file.is_file() or file.read_text(encoding="utf-8") != text:
            raise ValueError("Stale dossier artifact: " + path)
    else:
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding="utf-8")


def pair(text):
    return f"EN: {text['en']}\n\nES: {text['es-ES']}"


def fulfillment_wiki(campaign, episode):
    profile = episode["referenceCapabilityProfile"]
    rows = [
        f"# {episode['order']}. {episode['title']['en']}", "", episode["status"], "",
        "Design-only draft. Historical, geographic, native and game review remain pending; this typed projection is not an implemented map or played route.", "",
        f"{campaign['editorialContract']['publicId']} · `{episode['id']}` · {episode['dateRange']} · {episode['mapSize']}×{episode['mapSize']}", "",
        "## Historical frame and source record", "", pair(episode["event"]), "", pair(episode["historicalOutcome"]), "",
        pair(episode["dramatizationNotice"]), "", "```json",
        json.dumps({"sourcePassages": episode["sourcePassages"], "knowledgeBasis": episode["knowledgeBasis"]}, ensure_ascii=False, indent=2),
        "```", "", "## Shared objective and typed profile", "",
    ]
    for objective in profile["objectivePlan"]:
        rows += [f"### {objective['id']} / {objective['phase']}", "", pair(objective["text"]), "", "```json",
                 json.dumps(objective["predicate"], ensure_ascii=False, indent=2), "```", ""]
    rows += ["## Alternative services", "", "A selection is one authored recipe per service. Costs are alternatives and are never lowered to simultaneous fixed-payment predicates.", ""]
    for service in episode["fulfillmentServices"]:
        rows += [f"### {service['serviceId']}", "", f"Goal screen: `{service['goalScreenId']}` · completion screen: `{service['completeScreenId']}`", ""]
        for recipe in service["recipes"]:
            rows += [f"#### {recipe['recipeId']} — {recipe['title']['en']}", "", pair(recipe["title"]), "",
                     f"Work point `{recipe['workPointId']}` → reception point `{recipe['receptionPointId']}`; worker `{recipe['workerId']}`; output `{recipe['outputEntityId']}`; recipients: {', '.join(f'`{item}`' for item in recipe['recipientIds'])}.", "",
                     "Cost: `" + json.dumps(recipe["cost"], sort_keys=True) + "`.", ""]
    rows += ["## Difficulty accounting", "", "Finite selection arithmetic only; it is not resource gathering, a schedule or a playthrough.", ""]
    for level in ("easy", "standard", "hard"):
        analysis = episode["selectionAnalysisByDifficulty"][level]
        optional = episode["optionalPrefixAnalysisByDifficulty"][level]
        after_funding = {
            tuple(row["recipeIds"]): row
            for row in optional["afterFundingSelections"]
        }
        rows += [f"### {level}", "", "Accounts:", "", "```json", json.dumps(episode["accountsByDifficulty"][level], ensure_ascii=False, indent=2), "```", "",
                 f"Before main funding: {optional['reachableSubsetCount']} of {2 ** len(profile['secondaryObjectives'])} optional subsets are reachable from initial spendable stock; all optional tasks are reachable in that prefix: {optional['allOptionalTasksAffordable']}. This prefix does not include a service selection.", "",
                 f"After main funding: {optional['mainAffordableSelectionCount']} of {len(analysis['selections'])} recipe selections are affordable from initial spendable stock; {optional['allOptionalTasksAffordableAfterFundingCount']} affordable selections permit all optional tasks in an affordable prefix. Unaffordable selections have no after-funding witness. These are finite accounting cases and assume spatial predicates and actor availability succeed.", "",
                 "| Recipe selection | Total cost | Main affordable | Spendable stock after main selection | Reachable optional subsets after funding | All optional tasks affordable after funding |", "|---|---|---:|---|---:|---|"]
        for row in analysis["selections"]:
            funded = after_funding[tuple(row["recipeIds"])]
            remainder = json.dumps(funded["initialRemainder"], sort_keys=True) if row["affordable"] else "—"
            reachable = funded["reachableSubsetCount"] if row["affordable"] else "—"
            all_optionals = funded["allOptionalTasksAffordable"] if row["affordable"] else "—"
            rows.append(f"| {', '.join(f'`{item}`' for item in row['recipeIds'])} | `{json.dumps(row['totalCost'], sort_keys=True)}` | {row['affordable']} | `{remainder}` | {reachable} | {all_optionals} |")
        rows.append("")
    rows += ["## Optional objectives", "", "The exact authored v3 contracts follow; their presence does not establish task reachability in the game.", "", "```json",
             json.dumps(profile["secondaryObjectives"], ensure_ascii=False, indent=2), "```", "",
             "## Geography and map controls", "", f"[Proposed map](../../../../design/maps/{episode['mapPlan']['asset'].split('/')[-3]}/odyssey/{episode['id']}.svg)", "",
             "```json", json.dumps(episode["mapPlan"], ensure_ascii=False, indent=2), "```", "",
             "## Authored presentation", ""]
    for screen in episode["screens"]:
        role = next((key for key, value in episode["screenRoles"].items() if value == screen["id"]), "unassigned authored screen")
        rows += [f"### {screen['id']} ({role})", "", pair(screen["text"]), "", f"Condition: {screen['condition']} · narrator: {screen['narrator']} · native surface: {screen['nativeSurface']}.", ""]
    rows += ["## QA and capability limits", "", "```json", json.dumps({"qa": episode["qa"], "requiredCapabilities": episode["requiredCapabilities"], "continuation": episode["continuation"], "gameplayIdentity": episode["gameplayIdentity"], "failureRecovery": episode["failureRecovery"]}, ensure_ascii=False, indent=2), "```", "",
             "A reference-profile projection is not native support. Native rendering, actual UI, audio, world footprints, pathfinding, difficulty, engine behavior and historical approval remain separate gates.", ""]
    return "\n".join(rows)


def table(rows):
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", "<br>")

    return "\n".join(
        "| " + " | ".join(cell(value) for value in row) + " |" for row in rows
    )


def wiki(campaign, episode):
    if "referenceCapabilityProfile" in episode:
        return fulfillment_wiki(campaign, episode)
    base = [
        f"# {episode['order']}. {episode['title']['en']}",
        "",
        episode["status"],
        "",
        "Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.",
        "",
        f"{campaign['editorialContract']['publicId']} · `{episode['id']}` · {episode['dateRange']} · {episode['mapSize']}×{episode['mapSize']}",
        "",
        "## Historical frame and fixed outcome",
        "",
        pair(episode["event"]),
        "",
        pair(episode["historicalOutcome"]),
        "",
        pair(episode["dramatizationNotice"]),
        "",
        "```json",
        json.dumps(
            {
                "sourcePassages": episode["sourcePassages"],
                "knowledgeBasis": episode["knowledgeBasis"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
        "",
        "## Main objectives and individual contracts",
        "",
    ]
    for o in episode["objectivePlan"]:
        base += [
            f"### {o['id']} / {o['phase']}",
            "",
            pair(o["text"]),
            "",
            "```json",
            json.dumps(o["predicate"], ensure_ascii=False, indent=2),
            "```",
            "",
            pair(o["receiptText"]),
            "",
            pair(o["personaReaction"]),
            "",
        ]
    if "oppositionPlan" in episode:
        base += [
            "## Finite opposition and authored engagement constraints",
            "",
            "```json",
            json.dumps(episode["oppositionPlan"], ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    if "finaleContract" in episode:
        base += ["## Campaign finale and optional successor recommendations", "",
                 "Design-only continuity contract. Native variable writes, menu rendering and save/load behavior remain unverified.", "",
                 "```json", json.dumps(episode["finaleContract"], ensure_ascii=False, indent=2), "```", ""]
    if "entryContract" in episode:
        base += ["## Optional predecessor recommendation and entry recap", "",
                 "Design-only entry contract. Starting without the predecessor remains allowed; native menu and save/load QA are pending.", "",
                 "```json", json.dumps(episode["entryContract"], ensure_ascii=False, indent=2), "```", ""]
    base += [
        "## Geographic districts and routes",
        "",
        f"[Own geographic control plan](../../../../design/maps/{campaign['campaignId']}/odyssey/{episode['id']}.svg)",
        "",
        "```json",
        json.dumps(episode["mapPlan"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## Finite world identities",
        "",
        "```json",
        json.dumps(episode["worldContract"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## Optional tasks and combinable playstyles",
        "",
    ]
    for o in episode["secondaryObjectives"]:
        base += [
            f"### {o['title']['en']} / {o['title']['es-ES']}",
            "",
            pair(o["text"]),
            "",
            pair(o["rationale"]),
            "",
            "```json",
            json.dumps(
                {
                    k: o[k]
                    for k in (
                        "id",
                        "kind",
                        "predicate",
                        "world",
                        "effects",
                        "stateContract",
                        "reachability",
                    )
                },
                ensure_ascii=False,
                indent=2,
            ),
            "```",
            "",
        ]
    base += [
        "```json",
        json.dumps(
            {
                "secondaryBudget": episode["secondaryBudget"],
                "playstyles": episode["playstyles"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
        "",
        "## Three difficulty budgets and limits",
        "",
        "```json",
        json.dumps(episode["difficulty"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## All player-facing screens",
        "",
        table(
            [
                ["Key / condition", "Speaker", "English", "Español"],
                ["---", "---", "---", "---"],
            ]
            + [
                [
                    s["key"] + " / " + s["condition"],
                    s["narrator"],
                    s["text"]["en"],
                    s["text"]["es-ES"],
                ]
                for s in episode["screens"]
            ]
        ),
        "",
        "## Production, recovery and verification",
        "",
        "```json",
        json.dumps(
            {
                k: episode[k]
                for k in (
                    "stateMachine",
                    "failureRecovery",
                    "requiredCapabilities",
                    "presencePlan",
                    "checkpointPresencePlan",
                    "deadlinePlan",
                    "transportPlan",
                    "artDirection",
                    "qa",
                ) if k in episode
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
        "",
    ]
    return "\n".join(base)


def diagram(episode, geographic_layers):
    size = episode["mapSize"]
    factor = 650 / (size - 1)
    projection_bbox = episode["mapPlan"]["bbox"]
    clip_bbox = frame_helper["make_frame"](projection_bbox, size).bounds_at(0, size - 1)
    point = lambda h: (55 + h["centre"][0] * factor, 85 + h["centre"][1] * factor)
    authored_hubs = episode["mapPlan"]["hubs"]
    last_hub_label_y = max(
        (
            140 + index * 50
            + (len(textwrap.wrap(f"{index}: {hub['name']['en']}", width=42)) - 1) * 14
            for index, hub in enumerate(authored_hubs, 1)
        ),
        default=0,
    )
    geographic_segments = [
        (
            layer,
            layers_helper.clipped_tile_segments(
                layer["index"], projection_bbox, size, clip_bbox=clip_bbox
            ),
        )
        for layer in geographic_layers
    ]
    schematic = episode["mapPlan"].get("schematicWaterControl")
    schematic_segments = []
    if schematic and len(schematic.get("coordinates", [])) >= 2:
        index = layers_helper.index_layer(
            {
                "features": [
                    {
                        "geometry": {
                            "type": "LineString",
                            "coordinates": schematic["coordinates"],
                        }
                    }
                ]
            }
        )
        schematic_segments = layers_helper.clipped_tile_segments(
            index, projection_bbox, size, clip_bbox=clip_bbox
        )
    v3_map = episode.get("designProfile") == "alternative-fulfillment-v3"
    if v3_map:
        legend_entries = ["Geographic district controls only"]
        has_modern_water = any(segments for _, segments in geographic_segments) or (
            schematic
            and schematic.get("renderAs") == "modern-river-line"
            and schematic_segments
        )
        if has_modern_water:
            legend_entries.append("Solid blue: modern geographic water controls")
        corridors = episode["mapPlan"]["corridors"]
        if any(c["mode"] == "water" for c in corridors):
            legend_entries.append("Cyan dashed: proposed water district connection")
        if any(c["mode"] == "land" and c["widthTiles"] < 10 for c in corridors):
            legend_entries.append("Olive dashed: proposed narrow land connections under 10 tiles")
        if any(c["mode"] == "land" and c["widthTiles"] >= 10 for c in corridors):
            legend_entries.append("Brown dashed: proposed wide land connections (10+ tiles)")
        if schematic_segments and schematic.get("renderAs") != "modern-river-line":
            legend_entries.append("Dashed blue: schematic regional water")
        legend_entries.extend(
            [
                "Not a surveyed path or terrain raster",
                "Native footprints and navigation pending",
            ]
        )
    else:
        legend_entries = [
            "Geographic district controls only",
            "Brown dashed: proposed land route",
            "Cyan dashed: proposed boat passage",
            "Not a surveyed path or terrain raster",
            "Blue: modern geographic water controls",
            "Dashed blue: schematic regional water",
            "Native footprints and navigation pending",
        ]
    legend_y = max(420, 175 + len(authored_hubs) * 50)
    last_legend_y = legend_y + len(legend_entries) * 24
    canvas_height = max(850, int(max(last_hub_label_y, last_legend_y, 780) + 28))
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1050 {canvas_height}" role="img" aria-label="{html.escape(episode["title"]["en"])} geographic districts">',
        f'<rect width="1050" height="{canvas_height}" fill="#f6f0dc"/>',
        '<rect x="55" y="85" width="650" height="650" fill="#dfdfba" stroke="#556344"/>',
        f'<text x="40" y="35" font-family="sans-serif" font-size="22">{html.escape(episode["title"]["en"])}</text>',
        f'<text x="40" y="63" font-family="sans-serif" font-size="15">{size} × {size} · {html.escape(episode["geographyId"])} · N ↑ E →</text>',
    ]
    for layer, segments in geographic_segments:
        for segment in segments:
            coordinates = " ".join(
                f"{55 + x * factor:.2f},{85 + y * factor:.2f}" for x, y in segment
            )
            lines.append(
                f'<polyline points="{coordinates}" fill="none" stroke="{layer["colour"]}" stroke-width="2"/>'
            )
    if schematic_segments:
        modern = schematic.get("renderAs") == "modern-river-line"
        water_kind = "modern-river-control" if modern else "schematic-water"
        dash = "" if modern else 'stroke-dasharray="4 5"'
        for segment in schematic_segments:
            coords = " ".join(
                f"{55 + x * factor:.2f},{85 + y * factor:.2f}" for x, y in segment
            )
            lines.append(
                f'<polyline data-control="{water_kind}" points="{coords}" fill="none" stroke="#478bba" stroke-width="2" {dash}><title>{html.escape(schematic["certainty"])}</title></polyline>'
            )
    hubs = {hub["id"]: hub for hub in episode["mapPlan"]["hubs"]}
    for corridor in episode["mapPlan"]["corridors"]:
        coords = " ".join(
            f"{x:.2f},{y:.2f}"
            for x, y in (point(hubs[hid]) for hid in corridor["hubOrder"])
        )
        colour = "#368da3" if corridor["mode"] == "water" else "#91512f" if corridor["widthTiles"] >= 10 else "#757547"
        lines.append(
            f'<polyline data-corridor="{html.escape(corridor["id"])}" points="{coords}" fill="none" stroke="{colour}" stroke-width="3" stroke-dasharray="8 6"><title>{html.escape(corridor["id"])}: proposed {html.escape(corridor["mode"])} district connection, intermediate path pending</title></polyline>'
        )
    for i, h in enumerate(authored_hubs, 1):
        x, y = point(h)
        lines += [
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="20" fill="none" stroke="#91512f"/>',
            f'<text x="{x + 23:.2f}" y="{y:.2f}" font-family="sans-serif">{i}</text>',

        ]
        for row, label in enumerate(textwrap.wrap(f"{i}: {h['name']['en']}", width=42)):
            lines.append(f'<text x="730" y="{140 + i * 50 + row * 14}" font-family="sans-serif" font-size="12">{html.escape(label)}</text>')
    for i, text in enumerate(legend_entries):
        lines.append(
            f'<text x="730" y="{legend_y + i * 24}" font-family="sans-serif" font-size="12">{text}</text>'
        )
    lines.append(
        f'<text x="730" y="{legend_y + len(legend_entries) * 24}" font-family="sans-serif" font-size="12">No ancient shore or elevation inferred</text>'
    )
    lines += [
        f'<text x="40" y="780" font-family="sans-serif" font-size="13">WGS84 bbox {episode["mapPlan"]["bbox"]}; cosine-corrected longitude; approximate districts</text>',
        "</svg>\n",
    ]
    return "\n".join(lines)


def run(check=False):
    geographic_layers = [
        {
            "index": layers_helper.index_layer(
                read(
                    "docs/research/odyssey-research/geography/ne_10m_coastline.geojson"
                )
            ),
            "colour": "#247b96",
        },
        {
            "index": layers_helper.index_layer(
                read(
                    "docs/design/reference/geography/regional-rivers_lake_centerlines.geojson"
                )
            ),
            "colour": "#5aa4b8",
        },
    ]
    profiles = {p["id"]: p for p in read("docs/design/geography.json")["profiles"]}
    profiles.update(
        {
            p["id"]: p
            for p in read("docs/research/odyssey-research/episode-geography.json")[
                "profiles"
            ]
        }
    )
    count = 0
    baseline = read("docs/design/catalog.json")["campaigns"]
    for campaign_row in read("docs/design/odyssey-policy.json")["campaigns"]:
        path = f"docs/design/odysseys/{campaign_row['id']}.json"
        campaign = read(path)
        if not campaign.get("episodeBlueprints"):
            continue
        selected = {e["id"]: e for e in campaign["episodeSelection"]}
        v3_plans = [plan for plan in campaign.get("episodeBlueprints", [])
                    if isinstance(plan, dict) and "designProfile" in plan]
        v3_projections = {}
        v3_projection_contexts = {}
        if v3_plans:
            request_fields = (
                "episodeId", "referenceCapabilityProfile", "accountsByDifficulty", "mapSize",
                "hubs", "pointZoneBindings", "recipeBindings", "serviceBindings", "planScreenIds", "screens",
            )
            batch = []
            for plan in v3_plans:
                # Deliberately extract only the closed ProjectionRequest; the envelope
                # and metadata are checked independently by the v3 composer.
                batch.append({field: plan[field] for field in request_fields if field in plan})
            projected = fulfillment.project_batch(batch)
            v3_projections = {row["episodeId"]: row for row in projected["projections"]}
            v3_projection_contexts = {
                request["episodeId"]: {"request": request, "projection": row}
                for request, row in zip(batch, projected["projections"])
            }
        episodes = []
        for plan in campaign["episodeBlueprints"]:
            selection = selected[plan["episodeId"]]
            previous_selection = next(
                (s for s in selected.values() if s["order"] == selection["order"] - 1),
                None,
            )
            next_selection = next(
                (s for s in selected.values() if s["order"] == selection["order"] + 1),
                None,
            )
            geography_profile = profiles[selection["geographyId"]]
            if "designProfile" in plan:
                projection = v3_projections.get(plan.get("episodeId"))
                if projection is None:
                    raise ValueError(f"Missing typed projection result for {plan.get('episodeId')}")
                episode = factory.build_fulfillment_dossier(
                    campaign, selection, plan, projection, geography_profile,
                    previous_selection, next_selection, baseline,
                )
            else:
                episode = factory.build_dossier(
                    campaign, selection, plan, geography_profile, next_selection, baseline,
                )
            failures = validator.audit_dossier(
                episode, campaign, baseline,
                projection_context=v3_projection_contexts.get(plan.get("episodeId")),
            )
            if failures:
                raise ValueError("\n".join(failures))
            if selection.get("contractStatus") == "approved-complete-dossier":
                raise ValueError("Draft regeneration cannot overwrite an approved dossier")
            selection["contractStatus"] = catalog.DRAFT_DOSSIER_STATUS
            episodes.append(episode)
            emit(
                f"docs/wiki/{campaign['campaignId']}/episodes/{episode['id']}/15-odyssey-dossier.md",
                wiki(campaign, episode),
                check,
            )
            emit(
                episode["mapPlan"]["asset"], diagram(episode, geographic_layers), check
            )
        campaign["episodes"] = episodes
        campaign["editorialContract"]["authoredDossierCount"] = len(episodes)
        campaign["status"] = (
            "explicit episode dossiers authored; independent approval and remaining episodes pending"
        )
        emit(path, json.dumps(campaign, ensure_ascii=False, indent=2) + "\n", check)
        count += len(episodes)
    print(
        f"{count} explicit expanded dossiers checked; no historical/native approval asserted"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    run(parser.parse_args().check)
