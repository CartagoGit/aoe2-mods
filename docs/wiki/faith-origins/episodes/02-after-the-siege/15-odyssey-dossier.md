# 17. The Names Beyond the Siege

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `02-after-the-siege` · 70 CE · 400×400

## Historical frame and fixed outcome

EN: Roman forces captured Jerusalem and destroyed its Temple in 70 CE. Josephus describes the fire, demolition and a remaining Roman garrison; his account favors Roman command and contains theological judgments. This local evacuation is fiction after the fall. The occupation remains fixed.

ES: Las fuerzas romanas tomaron Jerusalén y destruyeron su Templo en el año 70. Josefo describe el incendio, las demoliciones y una guarnición romana que permaneció; su relato favorece al mando romano e incluye juicios teológicos. Esta evacuación local tras la caída es ficticia. La ocupación permanece fija.

EN: The fictional convoy reached a local departure district. Jerusalem remains under Roman occupation and its Temple remains destroyed. Eusebius later reports a Christian departure to Pella before the war; that report does not document this post-fall convoy or its destination.

ES: El convoy ficticio alcanzó un distrito local de salida. Jerusalén sigue bajo ocupación romana y su Templo permanece destruido. Eusebio relata posteriormente una partida cristiana hacia Pella antes de la guerra; ese relato no documenta este convoy posterior a la caída ni su destino.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 10,
      "episodeId": "02-after-the-siege",
      "order": 17,
      "selectedSourceUrl": "https://www.livius.org/articles/place/jerusalem/jerusalem-70/",
      "consultedUrl": "https://www.livius.org/articles/place/jerusalem/jerusalem-70/",
      "passage": "Livius summary explicitly cites Josephus, Jewish War 6; primary source locator: Josephus, War 6.4.5–7.1.1 (Temple fire/destruction and capture).",
      "supportedClaim": {
        "en": "Josephus narrates the Roman capture and destruction of the Jerusalem Temple in 70 CE.",
        "es-ES": "Josefo narra la toma romana y destrucción del Templo de Jerusalén en el año 70."
      },
      "limitations": "Josephus is a near-contemporary participant writing under Roman patronage; casualty totals and speeches are rhetorically shaped. Livius is a secondary summary, not the primary source itself.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://earlyjewishwritings.com/text/josephus/war6.html",
      "passage": "Jewish War VI.4.5–7, temple fire; VI.1.1 landscape description",
      "limitations": "Whiston translation consulted, not a Greek critical text. Fire chain and Titus’ intent favor Roman command; speeches, theology and casualty figures are not neutral proof or demographic counts. Regional tree-clearance language is not a precise vegetation raster.",
      "consultationDate": "2026-10-13",
      "status": "architect read specified passages; independent approval pending"
    },
    {
      "consultedUrl": "https://earlyjewishwritings.com/text/josephus/war7.html",
      "passage": "Jewish War VII.1.1–2, demolition, surviving towers/west wall and garrison",
      "limitations": "Demolition and Tenth Legion presence narrated; no local ten-household escape, patrol number, route or permission is documented. Dramatic extent and speeches remain attributed.",
      "consultationDate": "2026-10-13",
      "status": "architect read specified passages; independent approval pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/250103.htm",
      "passage": "Ecclesiastical History III.5.3–4, later Pella report",
      "limitations": "Fourth-century account reports departure before war, not a contemporary post-fall evacuation record. Revelation and divine/collective punishment rhetoric are attributed authorial claims and never neutral causation. Pella is outside this map.",
      "consultationDate": "2026-10-13",
      "status": "architect read specified passages; independent approval pending"
    }
  ],
  "knowledgeBasis": {
    "speaker": "miriam-archive",
    "mode": "inherited letters and later sources",
    "noOmniscience": true
  }
}
```

## Main objectives and individual contracts

### o1 / phase-1

EN: Collect all four original household-property chests and deliver them to the northern provision yard.

ES: Recoge los cuatro cofres originales de bienes y entrégalos en el patio septentrional de provisiones.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "collected",
      "id": "req-1",
      "entities": [
        "faith-origins.02-after-the-siege.household-property-1",
        "faith-origins.02-after-the-siege.household-property-2",
        "faith-origins.02-after-the-siege.household-property-3",
        "faith-origins.02-after-the-siege.household-property-4"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.02-after-the-siege.household-property-1",
        "faith-origins.02-after-the-siege.household-property-2",
        "faith-origins.02-after-the-siege.household-property-3",
        "faith-origins.02-after-the-siege.household-property-4"
      ],
      "destinations": {
        "faith-origins.02-after-the-siege.household-property-1": "faith-origins.02-after-the-siege.destination-2",
        "faith-origins.02-after-the-siege.household-property-2": "faith-origins.02-after-the-siege.destination-2",
        "faith-origins.02-after-the-siege.household-property-3": "faith-origins.02-after-the-siege.destination-2",
        "faith-origins.02-after-the-siege.household-property-4": "faith-origins.02-after-the-siege.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Four original chests reached the staging yard; the ten household identities remain available.

ES: Los cuatro cofres originales han llegado al patio de preparación; siguen disponibles las diez identidades de hogares.

EN: An inventory is small beside the ruins. Small is not the same as worthless.

ES: Un inventario es pequeño junto a las ruinas. Pequeño no significa inútil.

### o2 / phase-2

EN: Pay 300 food and 80 wood once at the provision yard; visit and confirm passage through either the western approach or the northern plateau detour. No patrol kill is required.

ES: Paga una vez 300 de alimento y 80 de madera en el patio de provisiones; visita y comprueba el paso por el acceso occidental o por el desvío de la meseta norte. No se exige matar patrullas.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 300,
        "wood": 80
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.02-after-the-siege.destination-2"
      ],
      "allocations": {
        "faith-origins.02-after-the-siege.destination-2": {
          "food": 300,
          "wood": 80
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.02-after-the-siege.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "area-state",
      "state": "visited-and-passable",
      "requiredCount": 1,
      "proof": "actual player-unit visit and native-observed open corridor through one branch; initial visibility or a timer is insufficient",
      "id": "req-2",
      "zones": [
        "faith-origins.02-after-the-siege.destination-3",
        "faith-origins.02-after-the-siege.destination-4"
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Provisions are paid once and at least one actual branch passage is observed.

ES: Las provisiones se han pagado una vez y se ha observado el paso real de al menos una rama.

EN: The longer way asks for patience. It does not ask me to call another death a victory.

ES: El camino más largo pide paciencia. No me pide llamar victoria a otra muerte.

### o3 / phase-3

EN: Bring at least eight of the ten original households alive, together with all four original property chests, to the local western departure district.

ES: Lleva con vida al menos ocho de los diez hogares originales y los cuatro cofres originales al distrito local occidental de salida.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 8,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "faith-origins.02-after-the-siege.evacuation-households-1",
        "faith-origins.02-after-the-siege.evacuation-households-2",
        "faith-origins.02-after-the-siege.evacuation-households-3",
        "faith-origins.02-after-the-siege.evacuation-households-4",
        "faith-origins.02-after-the-siege.evacuation-households-5",
        "faith-origins.02-after-the-siege.evacuation-households-6",
        "faith-origins.02-after-the-siege.evacuation-households-7",
        "faith-origins.02-after-the-siege.evacuation-households-8",
        "faith-origins.02-after-the-siege.evacuation-households-9",
        "faith-origins.02-after-the-siege.evacuation-households-10"
      ],
      "destinations": {
        "faith-origins.02-after-the-siege.evacuation-households-1": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.evacuation-households-2": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.evacuation-households-3": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.evacuation-households-4": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.evacuation-households-5": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.evacuation-households-6": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.evacuation-households-7": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.evacuation-households-8": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.evacuation-households-9": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.evacuation-households-10": "faith-origins.02-after-the-siege.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.02-after-the-siege.household-property-1",
        "faith-origins.02-after-the-siege.household-property-2",
        "faith-origins.02-after-the-siege.household-property-3",
        "faith-origins.02-after-the-siege.household-property-4"
      ],
      "destinations": {
        "faith-origins.02-after-the-siege.household-property-1": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.household-property-2": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.household-property-3": "faith-origins.02-after-the-siege.destination-5",
        "faith-origins.02-after-the-siege.household-property-4": "faith-origins.02-after-the-siege.destination-5"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: At least eight distinct original households and all four original chests reached the local departure district.

ES: Al menos ocho hogares originales distintos y los cuatro cofres originales han llegado al distrito local de salida.

EN: These are invented names. I will not claim them as evidence for an ancient escape.

ES: Son nombres inventados. No los presentaré como prueba de una huida antigua.

## Finite opposition and guaranteed no-combat alternative

```json
{
  "classification": "fictional bounded patrol design; not a historical garrison size or native implementation",
  "historicalActorPolicy": "No Titus, Josephus or venerated figure appears as a combat unit; no religious conversion or collective divine punishment mechanic.",
  "unitSelection": {
    "friendly-light-escort": "four Militia and two Spearman native gameplay proxies, no historical-person identity",
    "patrol-infantry": "Militia native proxy for light fictional patrol infantry",
    "patrol-ranged": "Archer native proxy for fictional ranged patrol guards",
    "identityLookup": "Use named parser catalog entries in native implementation; record exact IDs and asset appearance, do not invent IDs or equate medieval game models with archaeologically authentic Roman kit. No cavalry, artillery or siege engine."
  },
  "placementRules": "Both patrol pockets preplaced outside every receiving/observation footprint around the guarded western hub; only selected difficulty IDs instantiate. 6 friendly escorts begin at pickup. Opposing AI has no base, producers, gatherers or global attack target. Patrols stay in audited leashed areas of the shortcut; safe branch cannot be aggro reached or shot across. Never release a reserve in response to choosing the northern route. No obligatory new recruitment, paid generation or free resurrection.",
  "byDifficulty": {
    "easy": {
      "productionEnabled": false,
      "mobilizations": [],
      "initialEntityIds": [
        "faith-origins.02-after-the-siege.patrol-infantry-1",
        "faith-origins.02-after-the-siege.patrol-infantry-2",
        "faith-origins.02-after-the-siege.patrol-ranged-1",
        "faith-origins.02-after-the-siege.patrol-ranged-2",
        "faith-origins.02-after-the-siege.patrol-ranged-3",
        "faith-origins.02-after-the-siege.patrol-ranged-4"
      ]
    },
    "standard": {
      "productionEnabled": false,
      "mobilizations": [],
      "initialEntityIds": [
        "faith-origins.02-after-the-siege.patrol-infantry-1",
        "faith-origins.02-after-the-siege.patrol-infantry-2",
        "faith-origins.02-after-the-siege.patrol-infantry-3",
        "faith-origins.02-after-the-siege.patrol-infantry-4",
        "faith-origins.02-after-the-siege.patrol-ranged-1",
        "faith-origins.02-after-the-siege.patrol-ranged-2",
        "faith-origins.02-after-the-siege.patrol-ranged-3",
        "faith-origins.02-after-the-siege.patrol-ranged-4",
        "faith-origins.02-after-the-siege.patrol-ranged-5",
        "faith-origins.02-after-the-siege.patrol-ranged-6"
      ]
    },
    "hard": {
      "productionEnabled": false,
      "mobilizations": [],
      "initialEntityIds": [
        "faith-origins.02-after-the-siege.patrol-infantry-1",
        "faith-origins.02-after-the-siege.patrol-infantry-2",
        "faith-origins.02-after-the-siege.patrol-infantry-3",
        "faith-origins.02-after-the-siege.patrol-infantry-4",
        "faith-origins.02-after-the-siege.patrol-infantry-5",
        "faith-origins.02-after-the-siege.patrol-infantry-6",
        "faith-origins.02-after-the-siege.patrol-ranged-1",
        "faith-origins.02-after-the-siege.patrol-ranged-2",
        "faith-origins.02-after-the-siege.patrol-ranged-3",
        "faith-origins.02-after-the-siege.patrol-ranged-4",
        "faith-origins.02-after-the-siege.patrol-ranged-5",
        "faith-origins.02-after-the-siege.patrol-ranged-6",
        "faith-origins.02-after-the-siege.patrol-ranged-7",
        "faith-origins.02-after-the-siege.patrol-ranged-8"
      ]
    }
  },
  "nativeStatus": "not implemented; pathfinding, actual attack range, AI pursuit leash and roster bindings require i00003/S2–S3 and independent engine QA; static counts do not prove combat balance"
}
```

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/02-after-the-siege.svg)

```json
{
  "bbox": [
    35.193,
    31.776,
    35.241,
    31.81
  ],
  "terrainProfile": "jerusalem",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        281.14,
        269.36
      ],
      "lonLat": [
        35.228,
        31.785
      ],
      "name": {
        "en": "Northern urban pickup court",
        "es-ES": "Patio urbano septentrional de recogida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        214.34,
        225.7
      ],
      "lonLat": [
        35.219,
        31.79
      ],
      "name": {
        "en": "Northern provision yard",
        "es-ES": "Patio septentrional de provisiones"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        132.7,
        278.09
      ],
      "lonLat": [
        35.208,
        31.784
      ],
      "name": {
        "en": "Guarded western approach",
        "es-ES": "Acceso occidental vigilado"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        177.23,
        120.91
      ],
      "lonLat": [
        35.214,
        31.802
      ],
      "name": {
        "en": "Northern plateau detour",
        "es-ES": "Desvío por la meseta norte"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        58.48,
        190.77
      ],
      "lonLat": [
        35.198,
        31.794
      ],
      "name": {
        "en": "Local western departure district",
        "es-ES": "Distrito local occidental de salida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "main",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-3",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10,
      "routePolicy": "shorter western route, optional encounter with fixed fictional patrol pockets; never a requirement to destroy the Roman garrison"
    },
    {
      "id": "relief",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 8,
      "routePolicy": "longer disclosed no-combat northern plateau detour; hostile pursuit leash must never reach this corridor or the main origins/receivers; pathfinding certification pending"
    },
    {
      "id": "survey-link",
      "hubOrder": [
        "hub-2",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "short independent scout access to the safe branch observation, no gate opened by optional guide"
    }
  ],
  "terrainInstructions": "Keep limestone plateau, the eastern Kidron ravine and western/southern valley relations. All five main districts lie west of the Temple-platform control and stay on northern/western land approaches; no navigable Kidron, forced ravine ford, Pella destination or exact ancient gate claim. Temple ruins are contextual and cannot be rebuilt or defended as a victory objective. No Ottoman walls, Dome of the Rock, dense immediately post-siege forest, medieval palace or modern road grid. The limited working timber bank is fictional stock, not an intact forest beside the siege. Preserve a collision-certified land detour physically separate from hostile attack range and pursuit leash; native footprints/elevation pending.",
  "corridorStraightLengthsTiles": {
    "main": 291.41,
    "relief": 328.74,
    "survey-link": 111.17
  },
  "interestSpacingTiles": [
    25,
    55
  ],
  "minimumUsableAreaFraction": 0.45,
  "activeAreaPolicy": "main districts, finite supply hinterland and six optional circuits; survey usable terrain, not rectangle area",
  "geometryStatus": "georeferenced proposal; neither raster/DEM nor native footprint/pathfinding certified",
  "geographicLayers": [
    {
      "assetId": "ne-odyssey-coastline",
      "interpretation": "modern regional shoreline control; not ancient harbor geometry"
    },
    {
      "assetId": "regional-rivers_lake_centerlines",
      "interpretation": "modern regional river controls where available; minor channels and ancient courses require separate evidence"
    }
  ],
  "schematicWaterControl": {
    "coordinates": [],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/02-after-the-siege.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-1",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-2",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-3",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -6,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-4",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -4,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-5",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-6",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-7",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -6,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-8",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -4,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-9",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        12
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.evacuation-households-10",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        12
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.household-property-1",
      "role": "fictional-household-property",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        -8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "four fictional household-property chests; ordinary portable goods, no canonical manuscript, Temple treasure or excavated artifact"
    },
    {
      "id": "faith-origins.02-after-the-siege.household-property-2",
      "role": "fictional-household-property",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        -8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "four fictional household-property chests; ordinary portable goods, no canonical manuscript, Temple treasure or excavated artifact"
    },
    {
      "id": "faith-origins.02-after-the-siege.household-property-3",
      "role": "fictional-household-property",
      "initialHub": "hub-1",
      "offsetTiles": [
        -6,
        -8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "four fictional household-property chests; ordinary portable goods, no canonical manuscript, Temple treasure or excavated artifact"
    },
    {
      "id": "faith-origins.02-after-the-siege.household-property-4",
      "role": "fictional-household-property",
      "initialHub": "hub-1",
      "offsetTiles": [
        -4,
        -8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "four fictional household-property chests; ordinary portable goods, no canonical manuscript, Temple treasure or excavated artifact"
    },
    {
      "id": "faith-origins.02-after-the-siege.friendly-light-escort-1",
      "role": "fictional-voluntary-escort",
      "initialHub": "hub-1",
      "offsetTiles": [
        0,
        -8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.friendly-light-escort-2",
      "role": "fictional-voluntary-escort",
      "initialHub": "hub-1",
      "offsetTiles": [
        2,
        -8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.friendly-light-escort-3",
      "role": "fictional-voluntary-escort",
      "initialHub": "hub-1",
      "offsetTiles": [
        4,
        -8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.friendly-light-escort-4",
      "role": "fictional-voluntary-escort",
      "initialHub": "hub-1",
      "offsetTiles": [
        6,
        -8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.friendly-light-escort-5",
      "role": "fictional-voluntary-escort",
      "initialHub": "hub-1",
      "offsetTiles": [
        0,
        -6
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.friendly-light-escort-6",
      "role": "fictional-voluntary-escort",
      "initialHub": "hub-1",
      "offsetTiles": [
        2,
        -6
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-infantry-1",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -10,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-infantry-2",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -8,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-infantry-3",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -6,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-infantry-4",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -4,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-infantry-5",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -10,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-infantry-6",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -8,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-ranged-1",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        0,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-ranged-2",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        2,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-ranged-3",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        4,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-ranged-4",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        6,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-ranged-5",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        0,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-ranged-6",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        2,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-ranged-7",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        4,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.02-after-the-siege.patrol-ranged-8",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        6,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced once only if identity belongs to the selected difficulty roster; no reserve release or reproduction",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.02-after-the-siege.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.02-after-the-siege.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.02-after-the-siege.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.02-after-the-siege.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.02-after-the-siege.destination-5",
      "hub": "hub-5",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    }
  ],
  "objectGroups": {
    "evacuation-households": [
      "faith-origins.02-after-the-siege.evacuation-households-1",
      "faith-origins.02-after-the-siege.evacuation-households-2",
      "faith-origins.02-after-the-siege.evacuation-households-3",
      "faith-origins.02-after-the-siege.evacuation-households-4",
      "faith-origins.02-after-the-siege.evacuation-households-5",
      "faith-origins.02-after-the-siege.evacuation-households-6",
      "faith-origins.02-after-the-siege.evacuation-households-7",
      "faith-origins.02-after-the-siege.evacuation-households-8",
      "faith-origins.02-after-the-siege.evacuation-households-9",
      "faith-origins.02-after-the-siege.evacuation-households-10"
    ],
    "household-property": [
      "faith-origins.02-after-the-siege.household-property-1",
      "faith-origins.02-after-the-siege.household-property-2",
      "faith-origins.02-after-the-siege.household-property-3",
      "faith-origins.02-after-the-siege.household-property-4"
    ],
    "friendly-light-escort": [
      "faith-origins.02-after-the-siege.friendly-light-escort-1",
      "faith-origins.02-after-the-siege.friendly-light-escort-2",
      "faith-origins.02-after-the-siege.friendly-light-escort-3",
      "faith-origins.02-after-the-siege.friendly-light-escort-4",
      "faith-origins.02-after-the-siege.friendly-light-escort-5",
      "faith-origins.02-after-the-siege.friendly-light-escort-6"
    ],
    "patrol-infantry": [
      "faith-origins.02-after-the-siege.patrol-infantry-1",
      "faith-origins.02-after-the-siege.patrol-infantry-2",
      "faith-origins.02-after-the-siege.patrol-infantry-3",
      "faith-origins.02-after-the-siege.patrol-infantry-4",
      "faith-origins.02-after-the-siege.patrol-infantry-5",
      "faith-origins.02-after-the-siege.patrol-infantry-6"
    ],
    "patrol-ranged": [
      "faith-origins.02-after-the-siege.patrol-ranged-1",
      "faith-origins.02-after-the-siege.patrol-ranged-2",
      "faith-origins.02-after-the-siege.patrol-ranged-3",
      "faith-origins.02-after-the-siege.patrol-ranged-4",
      "faith-origins.02-after-the-siege.patrol-ranged-5",
      "faith-origins.02-after-the-siege.patrol-ranged-6",
      "faith-origins.02-after-the-siege.patrol-ranged-7",
      "faith-origins.02-after-the-siege.patrol-ranged-8"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.02-after-the-siege.evacuation-households-1",
        "faith-origins.02-after-the-siege.evacuation-households-2",
        "faith-origins.02-after-the-siege.evacuation-households-3",
        "faith-origins.02-after-the-siege.evacuation-households-4",
        "faith-origins.02-after-the-siege.evacuation-households-5",
        "faith-origins.02-after-the-siege.evacuation-households-6",
        "faith-origins.02-after-the-siege.evacuation-households-7",
        "faith-origins.02-after-the-siege.evacuation-households-8",
        "faith-origins.02-after-the-siege.evacuation-households-9",
        "faith-origins.02-after-the-siege.evacuation-households-10"
      ],
      "minimumAliveOrAlreadySafe": 8
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### A separate quarter’s provisions / Provisiones de un barrio separado

EN: Bring each of the two aid crates to its assigned household at a separate quarter’s provisions. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en provisiones de un barrio separado. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Two optional aid deliveries never substitute for mandatory convoy households or paid main provisions.

ES: Dos entregas opcionales nunca sustituyen hogares del convoy obligatorio ni sus provisiones pagadas.

```json
{
  "id": "side-1",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "02-after-the-siege.side-1.entity-1",
          "02-after-the-siege.side-1.entity-2"
        ],
        "destinations": {
          "02-after-the-siege.side-1.entity-1": "02-after-the-siege.side-1.zone-1",
          "02-after-the-siege.side-1.entity-2": "02-after-the-siege.side-1.zone-2"
        },
        "requiredCount": 2,
        "aliveAtDelivery": true,
        "oncePerEntity": true,
        "noSubstitutes": true,
        "initialPlacementDoesNotCount": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "02-after-the-siege.side-1.entity-1",
        "role": "aid",
        "initialHub": "hub-1",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      },
      {
        "id": "02-after-the-siege.side-1.entity-2",
        "role": "aid",
        "initialHub": "hub-1",
        "offsetTiles": [
          -6,
          6
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "02-after-the-siege.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "02-after-the-siege.side-1.zone-2",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 100,
        "wood": 50
      },
      "onceFlag": "02-after-the-siege.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-1",
    "receivingHub": "hub-2",
    "corridorIds": [
      "main",
      "relief",
      "survey-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The damaged supply shed / El cobertizo de suministros dañado

EN: Pay 50 wood and restore the damaged store of the damaged supply shed to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el cobertizo de suministros dañado. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A local shed repair releases finite supplies; it cannot repair the destroyed Temple.

ES: Reparar un cobertizo local libera provisiones finitas; no repara el Templo destruido.

```json
{
  "id": "side-2",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "02-after-the-siege.side-2.entity-1",
        "health": "full",
        "paymentReceipt": "02-after-the-siege.side-2.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "02-after-the-siege.side-2.payment",
        "afterArrival": false,
        "once": true,
        "protectedRecoveryCannotBeSpent": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "02-after-the-siege.side-2.entity-1",
        "role": "repair",
        "initialHub": "hub-2",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": false,
        "initialHealthFraction": 0.5,
        "damageSource": "fictional prior damage"
      }
    ],
    "zones": [
      {
        "id": "02-after-the-siege.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 200,
        "wood": 100
      },
      "onceFlag": "02-after-the-siege.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-2",
    "receivingHub": "hub-2",
    "corridorIds": [
      "main",
      "relief",
      "survey-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A bounded grain exchange / Un intercambio limitado de grano

EN: Escort the trader of a bounded grain exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de un intercambio limitado de grano hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Voluntary separate trade permits convoy preparation without inventing a universal Roman evacuation permit.

ES: Un intercambio voluntario separado ayuda a preparar el convoy sin inventar un permiso universal romano de evacuación.

```json
{
  "id": "side-3",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "02-after-the-siege.side-3.entity-1"
        ],
        "destinations": {
          "02-after-the-siege.side-3.entity-1": "02-after-the-siege.side-3.zone-1"
        },
        "requiredCount": 1,
        "aliveAtDelivery": true,
        "oncePerEntity": true,
        "noSubstitutes": true,
        "initialPlacementDoesNotCount": true
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "gold": 50
        },
        "receipt": "02-after-the-siege.side-3.payment",
        "afterArrival": true,
        "once": true,
        "protectedRecoveryCannotBeSpent": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "02-after-the-siege.side-3.entity-1",
        "role": "trade",
        "initialHub": "hub-1",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "02-after-the-siege.side-3.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 150,
        "wood": 50
      },
      "onceFlag": "02-after-the-siege.side-3.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-1",
    "receivingHub": "hub-2",
    "corridorIds": [
      "main",
      "relief",
      "survey-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Two independent voluntary travelers / Dos viajeros voluntarios independientes

EN: Bring both voluntary evacuee groups from two independent voluntary travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de dos viajeros voluntarios independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Optional travelers are independent of the ten main households and cannot replace their losses.

ES: Los viajeros opcionales son independientes de los diez hogares principales y no sustituyen sus pérdidas.

```json
{
  "id": "side-4",
  "kind": "extract",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "02-after-the-siege.side-4.entity-1",
          "02-after-the-siege.side-4.entity-2"
        ],
        "destinations": {
          "02-after-the-siege.side-4.entity-1": "02-after-the-siege.side-4.zone-1",
          "02-after-the-siege.side-4.entity-2": "02-after-the-siege.side-4.zone-1"
        },
        "requiredCount": 2,
        "aliveAtDelivery": true,
        "oncePerEntity": true,
        "noSubstitutes": true,
        "initialPlacementDoesNotCount": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "02-after-the-siege.side-4.entity-1",
        "role": "extract",
        "initialHub": "hub-3",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      },
      {
        "id": "02-after-the-siege.side-4.entity-2",
        "role": "extract",
        "initialHub": "hub-3",
        "offsetTiles": [
          -6,
          6
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "02-after-the-siege.side-4.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 100,
        "gold": 25
      },
      "onceFlag": "02-after-the-siege.side-4.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-3",
    "receivingHub": "hub-1",
    "corridorIds": [
      "main",
      "relief",
      "survey-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Western-approach viewpoints / Miradores del acceso occidental

EN: Scout both marked viewpoints of western-approach viewpoints. Benefit: Mark the surveyed main corridor once; no terrain alteration, patrol spawn or change to the main goal.

ES: Explora los dos miradores señalados de miradores del acceso occidental. Ventaja: Señala una vez el corredor trazado main; no altera terreno, crea patrullas ni cambia el objetivo principal.

EN: Survey the known shorter route without requiring a fight or spawning reserves.

ES: Reconoce el recorrido corto conocido sin exigir combate ni crear reservas.

```json
{
  "id": "side-5",
  "kind": "scout",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "visit-zones",
        "zones": [
          "02-after-the-siege.side-5.zone-1",
          "02-after-the-siege.side-5.zone-2"
        ],
        "actor": "any-player-controlled-unit",
        "requiredCount": 2,
        "observationsPersistent": true,
        "countInitialVisibility": false
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [],
    "zones": [
      {
        "id": "02-after-the-siege.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "02-after-the-siege.side-5.zone-2",
        "hub": "hub-3",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "mark-alternative-route",
      "target": "main surveyed land corridor",
      "resources": {},
      "onceFlag": "02-after-the-siege.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "main"
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-3",
    "receivingHub": "hub-2",
    "corridorIds": [
      "main",
      "relief",
      "survey-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A northern plateau guide / Un guía de la meseta norte

EN: Escort the local guide of a northern plateau guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no terrain alteration, patrol spawn or change to the main goal.

ES: Escolta al guía local de un guía de la meseta norte hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no altera terreno, crea patrullas ni cambia el objetivo principal.

EN: Marks the already open longer detour; the safe branch is disclosed without this guide.

ES: Señala el desvío más largo ya abierto; la rama segura es conocida sin este guía.

```json
{
  "id": "side-6",
  "kind": "guide",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "02-after-the-siege.side-6.entity-1"
        ],
        "destinations": {
          "02-after-the-siege.side-6.entity-1": "02-after-the-siege.side-6.zone-1"
        },
        "requiredCount": 1,
        "aliveAtDelivery": true,
        "oncePerEntity": true,
        "noSubstitutes": true,
        "initialPlacementDoesNotCount": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "02-after-the-siege.side-6.entity-1",
        "role": "guide",
        "initialHub": "hub-1",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "02-after-the-siege.side-6.zone-1",
        "hub": "hub-3",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "mark-alternative-route",
      "target": "relief surveyed land corridor",
      "resources": {},
      "onceFlag": "02-after-the-siege.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "relief"
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-1",
    "receivingHub": "hub-3",
    "corridorIds": [
      "main",
      "relief",
      "survey-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

```json
{
  "secondaryBudget": {
    "reservedRewards": {
      "food": 550,
      "wood": 200,
      "gold": 25,
      "stone": 0
    },
    "maxOptionalCosts": {
      "food": 0,
      "wood": 50,
      "gold": 50,
      "stone": 0
    },
    "reallocatedCacheAllowance": {
      "food": 600,
      "wood": 300,
      "gold": 150,
      "stone": 0
    },
    "fundingPolicy": "reward stock is segregated from the finite total bank; no duplicate caches",
    "nativeStatus": "design-only; requires certified reusable predicates and native QA"
  },
  "playstyles": [
    {
      "id": "patient-no-combat-convoy",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Use the disclosed northern plateau detour with aid/guide information; longer transport, no obligatory fight and no unique main replacement.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "surveyed-shortcut",
      "optionalObjectives": [
        "side-2",
        "side-5"
      ],
      "costOfOpportunity": "Scout the shorter branch and spend escort health carefully; repair supplies are finite and defeating patrols never ends the occupation.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "separate-logistics-teams",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Split convoy, gathering and independent-traveler teams; reserve all main provisions before optional trade, route choice stays open.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    }
  ]
}
```

## Three difficulty budgets and limits

```json
{
  "easy": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 402,
      "wood": 172,
      "gold": 86,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1518,
      "wood": 788,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 80,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 300,
      "wood": 200,
      "gold": 100,
      "stone": 0
    },
    "replacementBudget": {
      "food": 120,
      "wood": 80,
      "gold": 40,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 1370,
      "wood": 760,
      "gold": 290,
      "stone": 100
    },
    "maxVillagers": 12,
    "enemyTotalCap": 6,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      30,
      55
    ],
    "difficultyLevers": "12 workers, 6 finite patrols; disclosed safe branch and all main receivers, longer convoy shelter spacing.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  },
  "standard": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 350,
      "wood": 150,
      "gold": 75,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1570,
      "wood": 810,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 80,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 300,
      "wood": 200,
      "gold": 100,
      "stone": 0
    },
    "replacementBudget": {
      "food": 120,
      "wood": 80,
      "gold": 40,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 1370,
      "wood": 760,
      "gold": 290,
      "stone": 100
    },
    "maxVillagers": 9,
    "enemyTotalCap": 10,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      35,
      65
    ],
    "difficultyLevers": "9 workers, 10 finite patrols confined to the western shortcut; local fog outside main receiver markers, parallel cargo/household teams.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  },
  "hard": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 297,
      "wood": 127,
      "gold": 63,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1623,
      "wood": 833,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 80,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 300,
      "wood": 200,
      "gold": 100,
      "stone": 0
    },
    "replacementBudget": {
      "food": 120,
      "wood": 80,
      "gold": 40,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 1370,
      "wood": 760,
      "gold": 290,
      "stone": 100
    },
    "maxVillagers": 6,
    "enemyTotalCap": 14,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      40,
      75
    ],
    "difficultyLevers": "6 workers, 14 finite patrols on the same confined shortcut, lower finite starting stock; safe detour remains disclosed and outside hostility range. No speed/health/damage buffs, hidden deadline or unlimited production.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.faith-origins.02-after-the-siege.odyssey.title / always | none | The Names Beyond the Siege | Los nombres más allá del asedio |
| scenario.faith-origins.02-after-the-siege.odyssey.fact-intro / intro first | collection-narrator | Roman forces captured Jerusalem and destroyed its Temple in 70 CE. Josephus describes the fire, demolition and a remaining Roman garrison; his account favors Roman command and contains theological judgments. This local evacuation is fiction after the fall. The occupation remains fixed. | Las fuerzas romanas tomaron Jerusalén y destruyeron su Templo en el año 70. Josefo describe el incendio, las demoliciones y una guarnición romana que permaneció; su relato favorece al mando romano e incluye juicios teológicos. Esta evacuación local tras la caída es ficticia. La ocupación permanece fija. |
| scenario.faith-origins.02-after-the-siege.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.02-after-the-siege.odyssey.persona-intro / after handover | miriam-archive | I know this loss through books written before my birth, and I distrust how neatly some books explain another person’s suffering. Our imagined households have names in the ledger. I will attend to those names, without pretending that I heard their final conversations. | Conozco esta pérdida por libros anteriores a mi nacimiento y desconfío de las explicaciones demasiado ordenadas del sufrimiento ajeno. Nuestros hogares imaginados tienen nombres en el registro. Atenderé a esos nombres sin fingir que escuché sus últimas conversaciones. |
| scenario.faith-origins.02-after-the-siege.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.02-after-the-siege.odyssey.route-help / available from start; repeatable without effect | none | Gather four property chests at the provision yard. Fund the 300 food and 80 wood supplies and survey either passable branch. Then take at least eight of the ten original households and all four chests to the western departure district. The northern plateau route avoids combat and is always available; the western shortcut has finite patrols. Pella is not this map’s destination. | Reúne cuatro cofres de bienes en el patio de provisiones. Financia 300 de alimento y 80 de madera y reconoce cualquiera de las dos ramas transitables. Después lleva al distrito occidental de salida al menos ocho de los diez hogares originales y los cuatro cofres. La ruta por la meseta norte evita el combate y siempre está disponible; el atajo occidental tiene patrullas finitas. Pella no es el destino de este mapa. |
| scenario.faith-origins.02-after-the-siege.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.o1-goal / phase-1 active | none | Collect all four original household-property chests and deliver them to the northern provision yard. | Recoge los cuatro cofres originales de bienes y entrégalos en el patio septentrional de provisiones. |
| scenario.faith-origins.02-after-the-siege.odyssey.o1-receipt / o1 latched once | none | Four original chests reached the staging yard; the ten household identities remain available. | Los cuatro cofres originales han llegado al patio de preparación; siguen disponibles las diez identidades de hogares. |
| scenario.faith-origins.02-after-the-siege.odyssey.o1-reaction / after o1 receipt | miriam-archive | An inventory is small beside the ruins. Small is not the same as worthless. | Un inventario es pequeño junto a las ruinas. Pequeño no significa inútil. |
| scenario.faith-origins.02-after-the-siege.odyssey.o2-goal / phase-2 active | none | Pay 300 food and 80 wood once at the provision yard; visit and confirm passage through either the western approach or the northern plateau detour. No patrol kill is required. | Paga una vez 300 de alimento y 80 de madera en el patio de provisiones; visita y comprueba el paso por el acceso occidental o por el desvío de la meseta norte. No se exige matar patrullas. |
| scenario.faith-origins.02-after-the-siege.odyssey.o2-receipt / o2 latched once | none | Provisions are paid once and at least one actual branch passage is observed. | Las provisiones se han pagado una vez y se ha observado el paso real de al menos una rama. |
| scenario.faith-origins.02-after-the-siege.odyssey.o2-reaction / after o2 receipt | miriam-archive | The longer way asks for patience. It does not ask me to call another death a victory. | El camino más largo pide paciencia. No me pide llamar victoria a otra muerte. |
| scenario.faith-origins.02-after-the-siege.odyssey.o3-goal / phase-3 active | none | Bring at least eight of the ten original households alive, together with all four original property chests, to the local western departure district. | Lleva con vida al menos ocho de los diez hogares originales y los cuatro cofres originales al distrito local occidental de salida. |
| scenario.faith-origins.02-after-the-siege.odyssey.o3-receipt / o3 latched once | none | At least eight distinct original households and all four original chests reached the local departure district. | Al menos ocho hogares originales distintos y los cuatro cofres originales han llegado al distrito local de salida. |
| scenario.faith-origins.02-after-the-siege.odyssey.o3-reaction / after o3 receipt | miriam-archive | These are invented names. I will not claim them as evidence for an ancient escape. | Son nombres inventados. No los presentaré como prueba de una huida antigua. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at a separate quarter’s provisions. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en provisiones de un barrio separado. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-1-complete / side-1 completed | none | A separate quarter’s provisions completed. Its stated benefit has been granted once. | Provisiones de un barrio separado: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-1-lost / side-1 failed-optional | none | A separate quarter’s provisions is unavailable after the loss of its unique participant or object. The main mission continues. | Provisiones de un barrio separado: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-2-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the damaged supply shed to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el cobertizo de suministros dañado. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-2-complete / side-2 completed | none | The damaged supply shed completed. Its stated benefit has been granted once. | El cobertizo de suministros dañado: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-2-lost / side-2 failed-optional | none | The damaged supply shed is unavailable after the loss of its unique participant or object. The main mission continues. | El cobertizo de suministros dañado: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-3-goal / optional list from start | none | Escort the trader of a bounded grain exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de un intercambio limitado de grano hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-3-complete / side-3 completed | none | A bounded grain exchange completed. Its stated benefit has been granted once. | Un intercambio limitado de grano: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-3-lost / side-3 failed-optional | none | A bounded grain exchange is unavailable after the loss of its unique participant or object. The main mission continues. | Un intercambio limitado de grano: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-4-goal / optional list from start | none | Bring both voluntary evacuee groups from two independent voluntary travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de dos viajeros voluntarios independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-4-complete / side-4 completed | none | Two independent voluntary travelers completed. Its stated benefit has been granted once. | Dos viajeros voluntarios independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-4-lost / side-4 failed-optional | none | Two independent voluntary travelers is unavailable after the loss of its unique participant or object. The main mission continues. | Dos viajeros voluntarios independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of western-approach viewpoints. Benefit: Mark the surveyed main corridor once; no terrain alteration, patrol spawn or change to the main goal. | Explora los dos miradores señalados de miradores del acceso occidental. Ventaja: Señala una vez el corredor trazado main; no altera terreno, crea patrullas ni cambia el objetivo principal. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-5-complete / side-5 completed | none | Western-approach viewpoints completed. Its stated benefit has been granted once. | Miradores del acceso occidental: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-5-lost / side-5 failed-optional | none | Western-approach viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores del acceso occidental: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-6-goal / optional list from start | none | Escort the local guide of a northern plateau guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no terrain alteration, patrol spawn or change to the main goal. | Escolta al guía local de un guía de la meseta norte hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no altera terreno, crea patrullas ni cambia el objetivo principal. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-6-complete / side-6 completed | none | A northern plateau guide completed. Its stated benefit has been granted once. | Un guía de la meseta norte: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-after-the-siege.odyssey.side-6-lost / side-6 failed-optional | none | A northern plateau guide is unavailable after the loss of its unique participant or object. The main mission continues. | Un guía de la meseta norte: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-after-the-siege.odyssey.fact-outro / victory first | collection-narrator | The fictional convoy reached a local departure district. Jerusalem remains under Roman occupation and its Temple remains destroyed. Eusebius later reports a Christian departure to Pella before the war; that report does not document this post-fall convoy or its destination. | El convoy ficticio alcanzó un distrito local de salida. Jerusalén sigue bajo ocupación romana y su Templo permanece destruido. Eusebio relata posteriormente una partida cristiana hacia Pella antes de la guerra; ese relato no documenta este convoy posterior a la caída ni su destino. |
| scenario.faith-origins.02-after-the-siege.odyssey.persona-outro / after fact-outro | miriam-archive | I cannot turn a short list of imagined survivors into the city’s rescue. But a list need not carry the whole city to deserve care. I leave its invented names beside the sources, never inside them. | No puedo convertir una lista breve de supervivientes imaginados en la salvación de la ciudad. Pero una lista merece cuidado sin cargar con toda la ciudad. Dejo sus nombres inventados junto a las fuentes, nunca dentro de ellas. |
| scenario.faith-origins.02-after-the-siege.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.02-after-the-siege.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.02-after-the-siege.odyssey.next-episode / after persona-outro | none | Continue with Two Voices, Unfinished Margins. This episode does not complete the campaign. | Continúa con Dos voces, márgenes sin terminar. Este episodio no termina la campaña. |

## Production, recovery and verification

```json
{
  "stateMachine": {
    "states": [
      "briefing",
      "phase-1",
      "phase-2",
      "phase-3",
      "victory",
      "defeat"
    ],
    "phaseTransitions": [
      {
        "from": "briefing",
        "to": "phase-1",
        "on": "intro-accepted"
      },
      {
        "from": "phase-1",
        "to": "phase-2",
        "on": "objective-latched",
        "objectiveId": "o1"
      },
      {
        "from": "phase-2",
        "to": "phase-3",
        "on": "objective-latched",
        "objectiveId": "o2"
      },
      {
        "from": "phase-3",
        "to": "victory",
        "on": "objective-latched",
        "objectiveId": "o3"
      }
    ],
    "terminalPriority": "defeat first; close side rewards; one terminal latch",
    "saveLoad": "persist object identities, arrivals, collected facts, receipts, phase elapsed time and side reward balances",
    "campaignProgressWrite": false
  },
  "failureRecovery": {
    "mainIdentityLoss": "Any lost irreplaceable property chest defeats once its later delivery is impossible; household survival permits exactly two losses out of ten. Staging grants no immortal or final-safe status.",
    "optionalIdentityLoss": "only corresponding task becomes failed-optional",
    "recoveryImplementation": "inventory/replacement capability pending; reserved resources alone cannot resurrect an identity"
  },
  "requiredCapabilities": [
    {
      "id": "composed-world-ledger",
      "status": "reference model implemented including area-state; native implementation pending"
    },
    {
      "id": "finite-leashed-patrols",
      "status": "explicit roster and proxy roles authored; native AI, pursuit/attack-range separation and identity bindings pending"
    },
    {
      "id": "geographic-land-corridors",
      "status": "real-region local plan; DEM, footprints, collision and route passability pending"
    },
    {
      "id": "two-narrator-sequence",
      "status": "bilingual captions authored; native SequenceItems certification pending"
    }
  ],
  "artDirection": {
    "style": "sober Roman-era regional illustration; own geographic vector plan as research visual",
    "historicalControls": "no modern objects, invented quotation, sacred-person combat unit or later religious architecture",
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "eight original households cannot be replaced by optional travelers or escort IDs",
      "same original four chests must stage and leave",
      "death of three main households defeats; two does not if eight can still arrive",
      "both route observations cannot be required when count is one",
      "no patrol defeat required for the disclosed northern branch",
      "all six/ten/fourteen hostile IDs accounted once; no recruitment or reinforcement spawn",
      "pursuit and ranged attacks cannot reach northern detour, pickup or departure districts",
      "safe branch traversable skipping all optional tasks on every difficulty",
      "Temple cannot be rescued or rebuilt; garrison never destroyed as a condition",
      "late Eusebius Pella story never becomes post-fall survivor evidence",
      "households arriving early must remain alive until terminal victory; no staged immunity",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
