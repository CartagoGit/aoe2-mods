"""Rebuild explicit long-odyssey drafts and their readable episode wiki pages."""

import argparse
import html
import importlib.util
import json
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


def table(rows):
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", "<br>")

    return "\n".join(
        "| " + " | ".join(cell(value) for value in row) + " |" for row in rows
    )


def wiki(campaign, episode):
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
            "## Finite opposition and guaranteed no-combat alternative",
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
                    "artDirection",
                    "qa",
                )
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
    point = lambda h: (55 + h["centre"][0] * factor, 85 + h["centre"][1] * factor)
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1050 850" role="img" aria-label="{html.escape(episode["title"]["en"])} geographic districts">',
        '<rect width="1050" height="850" fill="#f6f0dc"/>',
        '<rect x="55" y="85" width="650" height="650" fill="#dfdfba" stroke="#556344"/>',
        f'<text x="40" y="35" font-family="sans-serif" font-size="22">{html.escape(episode["title"]["en"])}</text>',
        f'<text x="40" y="63" font-family="sans-serif" font-size="15">{size} × {size} · {html.escape(episode["geographyId"])} · N ↑ E →</text>',
    ]
    for layer in geographic_layers:
        segments = layers_helper.clipped_tile_segments(
            layer["index"], episode["mapPlan"]["bbox"], size
        )
        for segment in segments:
            coordinates = " ".join(
                f"{55 + x * factor:.2f},{85 + y * factor:.2f}" for x, y in segment
            )
            lines.append(
                f'<polyline points="{coordinates}" fill="none" stroke="{layer["colour"]}" stroke-width="2"/>'
            )
    schematic = episode["mapPlan"].get("schematicWaterControl")
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
        for segment in layers_helper.clipped_tile_segments(
            index, episode["mapPlan"]["bbox"], size
        ):
            coords = " ".join(
                f"{55 + x * factor:.2f},{85 + y * factor:.2f}" for x, y in segment
            )
            lines.append(
                f'<polyline data-control="schematic-water" points="{coords}" fill="none" stroke="#478bba" stroke-width="2" stroke-dasharray="4 5"><title>{html.escape(schematic["certainty"])}</title></polyline>'
            )
    hubs = {hub["id"]: hub for hub in episode["mapPlan"]["hubs"]}
    for corridor in episode["mapPlan"]["corridors"]:
        coords = " ".join(
            f"{x:.2f},{y:.2f}"
            for x, y in (point(hubs[hid]) for hid in corridor["hubOrder"])
        )
        colour = "#91512f" if corridor["widthTiles"] >= 10 else "#757547"
        lines.append(
            f'<polyline data-corridor="{html.escape(corridor["id"])}" points="{coords}" fill="none" stroke="{colour}" stroke-width="3" stroke-dasharray="8 6"><title>{html.escape(corridor["id"])}: proposed district connection, intermediate path pending</title></polyline>'
        )
    for i, h in enumerate(episode["mapPlan"]["hubs"], 1):
        x, y = point(h)
        lines += [
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="20" fill="none" stroke="#91512f"/>',
            f'<text x="{x + 23:.2f}" y="{y:.2f}" font-family="sans-serif">{i}</text>',
            f'<text x="730" y="{140 + i * 50}" font-family="sans-serif" font-size="12">{i}: {html.escape(h["name"]["en"])}</text>',
        ]
    for i, text in enumerate(
        [
            "Geographic district controls only",
            "Dashed connector: proposed route",
            "Not a surveyed path or terrain raster",
            "Blue: modern geographic water controls",
            "Dashed blue: schematic regional water",
            "Native footprints and navigation pending",
        ]
    ):
        lines.append(
            f'<text x="730" y="{420 + i * 24}" font-family="sans-serif" font-size="12">{text}</text>'
        )
    lines.append(
        '<text x="730" y="560" font-family="sans-serif" font-size="12">No ancient shore or elevation inferred</text>'
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
        episodes = []
        for plan in campaign["episodeBlueprints"]:
            selection = selected[plan["episodeId"]]
            next_selection = next(
                (s for s in selected.values() if s["order"] == selection["order"] + 1),
                None,
            )
            episode = factory.build_dossier(
                campaign,
                selection,
                plan,
                profiles[selection["geographyId"]],
                next_selection,
                baseline,
            )
            failures = validator.audit_dossier(episode, campaign, baseline)
            if failures:
                raise ValueError("\n".join(failures))
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
