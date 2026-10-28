# 24. The River Kept Their Names

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `24-witness-and-evacuation-lyon` · 177 CE · 400×400

## Historical frame and fixed outcome

EN: A community letter transmitted by Eusebius reports arrests, trials and deaths at Lyon and Vienne in 177. It names Blandina, Pothinus and others and interprets their suffering through Christian belief. Those explanations remain attributed to the letter. The deaths are not reversed by this fictional local household evacuation.

ES: Una carta comunitaria transmitida por Eusebio relata detenciones, procesos y muertes en Lyon y Vienne en 177. Nombra a Blandina, Potino y otros e interpreta su sufrimiento desde la fe cristiana. Esas explicaciones se atribuyen a la carta. Esta evacuación local ficticia de hogares no revierte las muertes.

EN: The recorded fictional household group reached its inland reception, and six separate local work notes reached two preservation yards. None is an ancient witness, recovered relic or rescued martyr. The source’s deaths and destruction of remains remain outside the player’s power.

ES: El grupo registrado de hogares ficticios llegó a su recepción interior y seis notas locales separadas llegaron a dos patios de conservación. No son testigos antiguos, reliquias recuperadas ni mártires rescatados. Las muertes y la destrucción de restos relatadas por la fuente permanecen fuera del poder del jugador.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 17,
      "episodeId": "24-witness-and-evacuation-lyon",
      "order": 24,
      "selectedSourceUrl": "https://www.newadvent.org/fathers/250106.htm",
      "consultedUrl": "https://www.newadvent.org/fathers/250105.htm",
      "passage": "Eusebius, Ecclesiastical History 5.1: preserved letter from Christians of Vienne and Lugdunum to Asian and Phrygian communities; narratives of arrest, trial, and deaths.",
      "supportedClaim": {
        "en": "Eusebius preserves a letter reporting trials and violence against Christians at Lyon and Vienne.",
        "es-ES": "Eusebio conserva una carta que informa de procesos y violencia contra cristianos en Lyon y Vienne."
      },
      "limitations": "Eusebius is later than the events and transmits a community letter; date 177 is inferred. The letter has theological rhetoric, visions and miracles that must remain source-attributed, not asserted as verified events.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/250105.htm",
      "passage": "HEV1.1–63; architect read communal letter, arrests, interrogations, deaths of Pothinus/Blandina/Ponticus and destruction of remains",
      "limitations": "Letter transmitted by later historian. Religious explanations, healing and private motives remain attributed, not neutral causation. Household convoy and local work notes are declared fiction; no historical martyr rescue or recovered ashes.",
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

EN: Bring at least eight distinct original households alive to the westward provision court.

ES: Lleva con vida al menos ocho hogares originales distintos al patio occidental de provisiones.

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
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-1",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-3",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-5",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-6",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-7",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-8",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-9",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-10"
      ],
      "destinations": {
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-1": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-2": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-3": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-4": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-5": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-6": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-7": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-8": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-9": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-10": "faith-origins.24-witness-and-evacuation-lyon.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true,
  "exportedLedgers": [
    {
      "id": "received-households",
      "operator": "intersection",
      "fromRequirements": [
        "req-1"
      ],
      "minimumCount": 8
    }
  ]
}
```

EN: The actual received household set is fixed for onward delivery.

ES: Se fija el conjunto de hogares recibido realmente para su entrega posterior.

EN: Our imagined neighbors are not the people named in that letter.

ES: Nuestros vecinos imaginados no son las personas nombradas en aquella carta.

### o2 / phase-2

EN: Pay 320 food and 100 wood once at the westward provision court.

ES: Paga una vez 320 de alimento y 100 de madera en el patio occidental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 320,
        "wood": 100
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.24-witness-and-evacuation-lyon.destination-2"
      ],
      "allocations": {
        "faith-origins.24-witness-and-evacuation-lyon.destination-2": {
          "food": 320,
          "wood": 100
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.24-witness-and-evacuation-lyon.o2.req-1.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The local convoy provisions are paid once.

ES: Se han pagado una vez las provisiones del convoy local.

EN: Supplies buy a journey here, not a governor’s pardon.

ES: Las provisiones permiten aquí un viaje, no compran el perdón de un gobernador.

### o3 / phase-3

EN: Deliver at least eight members of the actual received household group alive to the southern inland reception yard.

ES: Entrega con vida al menos ocho miembros del grupo de hogares recibido realmente en el patio interior meridional.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 8,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o1",
        "ledger": "received-households"
      },
      "id": "req-1",
      "entities": [
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-1",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-3",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-5",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-6",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-7",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-8",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-9",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-10"
      ],
      "destinations": {
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-1": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-2": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-3": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-4": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-5": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-6": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-7": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-8": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-9": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-10": "faith-origins.24-witness-and-evacuation-lyon.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: At least eight actual staged household identities reached their onward reception.

ES: Al menos ocho identidades de hogares realmente preparados han llegado a su recepción posterior.

EN: A later arrival cannot erase a loss among those entrusted to us.

ES: Una llegada posterior no borra una pérdida entre quienes nos confiaron.

### o4 / phase-4

EN: Collect all six ordinary working notes. Deliver the three northern notes to the northwestern preservation yard and the three southern notes to the southern reception yard.

ES: Recoge las seis notas ordinarias. Entrega las tres septentrionales en el patio noroccidental y las tres meridionales en el patio receptor meridional.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "collected",
      "id": "req-1",
      "entities": [
        "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-1",
        "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-2",
        "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-1",
        "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-2",
        "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-1",
        "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-2",
        "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-3"
      ],
      "destinations": {
        "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-1": "faith-origins.24-witness-and-evacuation-lyon.destination-3",
        "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-2": "faith-origins.24-witness-and-evacuation-lyon.destination-3",
        "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-3": "faith-origins.24-witness-and-evacuation-lyon.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-1",
        "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-2",
        "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-3"
      ],
      "destinations": {
        "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-1": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-2": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
        "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-3": "faith-origins.24-witness-and-evacuation-lyon.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both fictional note groups arrived at their separately assigned yards.

ES: Ambos grupos ficticios de notas han llegado a sus patios asignados por separado.

EN: A preserved work note is not the recovered voice of a dead person.

ES: Una nota de trabajo conservada no recupera la voz de una persona muerta.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/24-witness-and-evacuation-lyon.svg)

```json
{
  "bbox": [
    4.788,
    45.748,
    4.832,
    45.781
  ],
  "terrainProfile": "lyon",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        191.97,
        248.08
      ],
      "lonLat": [
        4.809,
        45.76
      ],
      "name": {
        "en": "Western local pickup court",
        "es-ES": "Patio local occidental de recogida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        94.07,
        215.69
      ],
      "lonLat": [
        4.796,
        45.763
      ],
      "name": {
        "en": "Westward provision court",
        "es-ES": "Patio occidental de provisiones"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        146.78,
        96.94
      ],
      "lonLat": [
        4.803,
        45.774
      ],
      "name": {
        "en": "Northwestern preservation yard",
        "es-ES": "Patio noroccidental de conservación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        222.09,
        312.85
      ],
      "lonLat": [
        4.813,
        45.754
      ],
      "name": {
        "en": "Southern inland reception yard",
        "es-ES": "Patio receptor interior meridional"
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
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10,
      "routePolicy": "graded westward approach, no Saone crossing"
    },
    {
      "id": "southern-road",
      "hubOrder": [
        "hub-1",
        "hub-4",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "relief",
      "hubOrder": [
        "hub-2",
        "hub-4",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "graded western hill circuit; exact native intermediate turns pending"
    }
  ],
  "terrainInstructions": "Local Lugdunum western hill scene: Fourviere and its westward/lower approaches, entirely west of the schematic Saone. Maintain hill-to-river descent and graded western travel; do not flatten the whole city. The Rhone, Condate amphitheater and river confluence are contextual/outside the activity frame, not rescue destinations. No forced Saone bridge, recovery of ashes from the Rhone, modern tunnel, nineteenth-century Fourviere basilica, later funerary church, cathedral or monastery. Exact second-century street/household placements and navigable gradients remain pending. The museum’s second-century plan explicitly separates current and hypothetical ancient rivers; neither is an exact GIS mask.",
  "corridorStraightLengthsTiles": {
    "main": 233.04,
    "southern-road": 232.15,
    "relief": 389.38
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
    "coordinates": [
      [
        4.812,
        45.805
      ],
      [
        4.813,
        45.788
      ],
      [
        4.813,
        45.782
      ],
      [
        4.817,
        45.776
      ],
      [
        4.828,
        45.771
      ],
      [
        4.829,
        45.766
      ],
      [
        4.825,
        45.759
      ],
      [
        4.823,
        45.753
      ],
      [
        4.816,
        45.745
      ],
      [
        4.81,
        45.74
      ]
    ],
    "certainty": "architect schematic Saone relation, no surveyed ancient channel; do not rasterize as native water",
    "renderAs": "river-line"
  },
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/24-witness-and-evacuation-lyon.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-1",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-2",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-3",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-4",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-5",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-6",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-7",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-8",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-9",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-10",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-1",
      "role": "fictional-local-circulation-note",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-2",
      "role": "fictional-local-circulation-note",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-3",
      "role": "fictional-local-circulation-note",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-1",
      "role": "fictional-local-circulation-note",
      "initialHub": "hub-2",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-2",
      "role": "fictional-local-circulation-note",
      "initialHub": "hub-2",
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
      "id": "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-3",
      "role": "fictional-local-circulation-note",
      "initialHub": "hub-2",
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
    }
  ],
  "zones": [
    {
      "id": "faith-origins.24-witness-and-evacuation-lyon.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.24-witness-and-evacuation-lyon.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.24-witness-and-evacuation-lyon.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.24-witness-and-evacuation-lyon.destination-4",
      "hub": "hub-4",
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
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-1",
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-2",
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-3",
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-4",
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-5",
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-6",
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-7",
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-8",
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-9",
      "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-10"
    ],
    "north-working-notes": [
      "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-1",
      "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-2",
      "faith-origins.24-witness-and-evacuation-lyon.north-working-notes-3"
    ],
    "south-working-notes": [
      "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-1",
      "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-2",
      "faith-origins.24-witness-and-evacuation-lyon.south-working-notes-3"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-1",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-2",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-3",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-4",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-5",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-6",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-7",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-8",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-9",
        "faith-origins.24-witness-and-evacuation-lyon.evacuation-households-10"
      ],
      "minimumAliveOrAlreadySafe": 8
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### A separate household supply stop / Una parada separada de provisiones domésticas

EN: Bring each of the two aid crates to its assigned household at a separate household supply stop. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en una parada separada de provisiones domésticas. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Independent aid households cannot replace losses in the staged main group.

ES: Los hogares de ayuda independientes no sustituyen pérdidas del grupo principal preparado.

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
          "24-witness-and-evacuation-lyon.side-1.entity-1",
          "24-witness-and-evacuation-lyon.side-1.entity-2"
        ],
        "destinations": {
          "24-witness-and-evacuation-lyon.side-1.entity-1": "24-witness-and-evacuation-lyon.side-1.zone-1",
          "24-witness-and-evacuation-lyon.side-1.entity-2": "24-witness-and-evacuation-lyon.side-1.zone-2"
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
        "id": "24-witness-and-evacuation-lyon.side-1.entity-1",
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
        "id": "24-witness-and-evacuation-lyon.side-1.entity-2",
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
        "id": "24-witness-and-evacuation-lyon.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "24-witness-and-evacuation-lyon.side-1.zone-2",
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
      "onceFlag": "24-witness-and-evacuation-lyon.side-1.rewarded",
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
      "southern-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Two independent inland travelers / Dos viajeros interiores independientes

EN: Bring both voluntary evacuee groups from two independent inland travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de dos viajeros interiores independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Voluntary fictional travelers never bear a martyr’s historical identity.

ES: Los viajeros ficticios voluntarios nunca llevan la identidad histórica de un mártir.

```json
{
  "id": "side-2",
  "kind": "extract",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "24-witness-and-evacuation-lyon.side-2.entity-1",
          "24-witness-and-evacuation-lyon.side-2.entity-2"
        ],
        "destinations": {
          "24-witness-and-evacuation-lyon.side-2.entity-1": "24-witness-and-evacuation-lyon.side-2.zone-1",
          "24-witness-and-evacuation-lyon.side-2.entity-2": "24-witness-and-evacuation-lyon.side-2.zone-1"
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
        "id": "24-witness-and-evacuation-lyon.side-2.entity-1",
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
        "id": "24-witness-and-evacuation-lyon.side-2.entity-2",
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
        "id": "24-witness-and-evacuation-lyon.side-2.zone-1",
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
      "onceFlag": "24-witness-and-evacuation-lyon.side-2.rewarded",
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
      "southern-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The attributed letter’s context / El contexto de la carta atribuida

EN: Recover both separate copies from the attributed letter’s context and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de el contexto de la carta atribuida y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Unlock source context without copying invented testimony or theological causation into the objective voice.

ES: Desbloquea contexto sin incorporar testimonio inventado ni causalidad teológica a la voz objetiva.

```json
{
  "id": "side-3",
  "kind": "copy",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "24-witness-and-evacuation-lyon.side-3.entity-1",
          "24-witness-and-evacuation-lyon.side-3.entity-2"
        ],
        "destinations": {
          "24-witness-and-evacuation-lyon.side-3.entity-1": "24-witness-and-evacuation-lyon.side-3.zone-1",
          "24-witness-and-evacuation-lyon.side-3.entity-2": "24-witness-and-evacuation-lyon.side-3.zone-1"
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
        "id": "24-witness-and-evacuation-lyon.side-3.entity-1",
        "role": "copy",
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
        "id": "24-witness-and-evacuation-lyon.side-3.entity-2",
        "role": "copy",
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
        "id": "24-witness-and-evacuation-lyon.side-3.zone-1",
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
      "kind": "unlock-context-and-hint",
      "target": "documented context and a main-goal hint",
      "resources": {},
      "onceFlag": "24-witness-and-evacuation-lyon.side-3.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.24-witness-and-evacuation-lyon"
      ],
      "historicalNote": {
        "en": "A community letter transmitted by Eusebius reports arrests, trials and deaths at Lyon and Vienne in 177. It names Blandina, Pothinus and others and interprets their suffering through Christian belief. Those explanations remain attributed to the letter. The deaths are not reversed by this fictional local household evacuation.",
        "es-ES": "Una carta comunitaria transmitida por Eusebio relata detenciones, procesos y muertes en Lyon y Vienne en 177. Nombra a Blandina, Potino y otros e interpreta su sufrimiento desde la fe cristiana. Esas explicaciones se atribuyen a la carta. Esta evacuación local ficticia de hogares no revierte las muertes."
      },
      "hint": {
        "en": "Bring at least eight distinct original households alive to the westward provision court.",
        "es-ES": "Lleva con vida al menos ocho hogares originales distintos al patio occidental de provisiones."
      }
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
      "southern-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The west-road supply store / El almacén de provisiones del camino oeste

EN: Pay 50 wood and restore the damaged store of the west-road supply store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el almacén de provisiones del camino oeste. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: An ordinary finite supply repair cannot restore a prison, sanctuary or burnt remains.

ES: Una reparación ordinaria y finita no restaura una prisión, santuario ni restos quemados.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "24-witness-and-evacuation-lyon.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "24-witness-and-evacuation-lyon.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "24-witness-and-evacuation-lyon.side-4.payment",
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
        "id": "24-witness-and-evacuation-lyon.side-4.entity-1",
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
        "id": "24-witness-and-evacuation-lyon.side-4.zone-1",
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
      "onceFlag": "24-witness-and-evacuation-lyon.side-4.rewarded",
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
      "southern-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Southern approach viewpoints / Miradores del acceso meridional

EN: Scout both marked viewpoints of southern approach viewpoints. Benefit: Mark the surveyed southern-road land circuit once. All main receivers remain disclosed without this optional task.

ES: Explora los dos miradores señalados de miradores del acceso meridional. Ventaja: Señala una vez el circuito terrestre trazado southern-road. Todos los receptores principales siguen identificados sin esta tarea opcional.

EN: Observe an actual inland approach, not a secret route into the amphitheater.

ES: Observa un acceso interior real, no una ruta secreta al anfiteatro.

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
          "24-witness-and-evacuation-lyon.side-5.zone-1",
          "24-witness-and-evacuation-lyon.side-5.zone-2"
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
        "id": "24-witness-and-evacuation-lyon.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "24-witness-and-evacuation-lyon.side-5.zone-2",
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
      "target": "southern-road surveyed land circuit",
      "resources": {},
      "onceFlag": "24-witness-and-evacuation-lyon.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "southern-road"
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
      "southern-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A western hill guide / Un guía de las colinas occidentales

EN: Escort the local guide of a western hill guide to the marked road junction. Benefit: Mark the surveyed relief land circuit once. All main receivers remain disclosed without this optional task.

ES: Escolta al guía local de un guía de las colinas occidentales hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado relief. Todos los receptores principales siguen identificados sin esta tarea opcional.

EN: Marks a graded land circuit; does not open a fictitious river escape or revive people.

ES: Señala un circuito terrestre graduado; no abre una huida fluvial ficticia ni revive personas.

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
          "24-witness-and-evacuation-lyon.side-6.entity-1"
        ],
        "destinations": {
          "24-witness-and-evacuation-lyon.side-6.entity-1": "24-witness-and-evacuation-lyon.side-6.zone-1"
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
        "id": "24-witness-and-evacuation-lyon.side-6.entity-1",
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
        "id": "24-witness-and-evacuation-lyon.side-6.zone-1",
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
      "target": "relief surveyed land circuit",
      "resources": {},
      "onceFlag": "24-witness-and-evacuation-lyon.side-6.rewarded",
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
      "southern-road",
      "relief"
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
      "food": 400,
      "wood": 150,
      "gold": 25,
      "stone": 0
    },
    "maxOptionalCosts": {
      "food": 0,
      "wood": 50,
      "gold": 0,
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
      "id": "households-first",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Secure the actual staged group and disclosed onward route before assigning note collection teams.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "split-preservation",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Send separate north/south note teams while gathering mandatory convoy provisions; no identity may count at both receivers.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "independent-travel-support",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Combine voluntary side extraction and finite repairs while delivering at least eight actual staged main identities.",
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
      "food": 1388,
      "wood": 758,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 320,
      "wood": 100,
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
      "food": 1390,
      "wood": 780,
      "gold": 290,
      "stone": 100
    },
    "maxVillagers": 12,
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      30,
      55
    ],
    "difficultyLevers": "12 workers; fully marked route; independent pickups can be completed in any order.",
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
      "food": 1440,
      "wood": 780,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 320,
      "wood": 100,
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
      "food": 1390,
      "wood": 780,
      "gold": 290,
      "stone": 100
    },
    "maxVillagers": 9,
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      35,
      65
    ],
    "difficultyLevers": "9 workers; geographic approach markers with local fog; plan deliveries and gathering in parallel.",
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
      "food": 1493,
      "wood": 803,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 320,
      "wood": 100,
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
      "food": 1390,
      "wood": 780,
      "gold": 290,
      "stone": 100
    },
    "maxVillagers": 6,
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      40,
      75
    ],
    "difficultyLevers": "6 workers; fewer initial supplies; all essential receiving zones and costs remain disclosed; no invented hostile army or secret deadline.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.title / always | none | The River Kept Their Names | El río conservó sus nombres |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.fact-intro / intro first | collection-narrator | A community letter transmitted by Eusebius reports arrests, trials and deaths at Lyon and Vienne in 177. It names Blandina, Pothinus and others and interprets their suffering through Christian belief. Those explanations remain attributed to the letter. The deaths are not reversed by this fictional local household evacuation. | Una carta comunitaria transmitida por Eusebio relata detenciones, procesos y muertes en Lyon y Vienne en 177. Nombra a Blandina, Potino y otros e interpreta su sufrimiento desde la fe cristiana. Esas explicaciones se atribuyen a la carta. Esta evacuación local ficticia de hogares no revierte las muertes. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.persona-intro / after handover | miriam-archive | I read this letter long after its grief was first put into words. My faith draws me toward its courage; my work requires me to say whose courage the letter describes. The imagined households on our map must not take the martyrs’ names. | Leo esta carta mucho después de que su dolor se pusiera por primera vez en palabras. Mi fe me acerca a su valentía; mi trabajo me exige decir de quién es la valentía que describe la carta. Los hogares imaginados del mapa no deben tomar los nombres de los mártires. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.route-help / available from start; repeatable without effect | none | Stage at least eight of the ten original households at the westward provision court and preserve that exact received group. Pay 320 food and 100 wood there once. Bring at least eight members of that actual received group alive to the southern inland yard. Collect all six ordinary work notes; send the three northern notes to the northwestern yard and the three southern notes to the southern yard. No martyr, prison or relic can be rescued. | Reúne al menos ocho de los diez hogares originales en el patio occidental y conserva ese grupo recibido exacto. Paga allí una vez 320 de alimento y 100 de madera. Lleva con vida al menos ocho miembros de ese grupo recibido realmente al patio interior meridional. Recoge las seis notas ordinarias: entrega las tres septentrionales en el patio noroccidental y las tres meridionales en el meridional. No puedes rescatar mártires, prisiones ni reliquias. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o1-goal / phase-1 active | none | Bring at least eight distinct original households alive to the westward provision court. | Lleva con vida al menos ocho hogares originales distintos al patio occidental de provisiones. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o1-receipt / o1 latched once | none | The actual received household set is fixed for onward delivery. | Se fija el conjunto de hogares recibido realmente para su entrega posterior. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o1-reaction / after o1 receipt | miriam-archive | Our imagined neighbors are not the people named in that letter. | Nuestros vecinos imaginados no son las personas nombradas en aquella carta. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o2-goal / phase-2 active | none | Pay 320 food and 100 wood once at the westward provision court. | Paga una vez 320 de alimento y 100 de madera en el patio occidental. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o2-receipt / o2 latched once | none | The local convoy provisions are paid once. | Se han pagado una vez las provisiones del convoy local. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o2-reaction / after o2 receipt | miriam-archive | Supplies buy a journey here, not a governor’s pardon. | Las provisiones permiten aquí un viaje, no compran el perdón de un gobernador. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o3-goal / phase-3 active | none | Deliver at least eight members of the actual received household group alive to the southern inland reception yard. | Entrega con vida al menos ocho miembros del grupo de hogares recibido realmente en el patio interior meridional. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o3-receipt / o3 latched once | none | At least eight actual staged household identities reached their onward reception. | Al menos ocho identidades de hogares realmente preparados han llegado a su recepción posterior. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o3-reaction / after o3 receipt | miriam-archive | A later arrival cannot erase a loss among those entrusted to us. | Una llegada posterior no borra una pérdida entre quienes nos confiaron. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o4-goal / phase-4 active | none | Collect all six ordinary working notes. Deliver the three northern notes to the northwestern preservation yard and the three southern notes to the southern reception yard. | Recoge las seis notas ordinarias. Entrega las tres septentrionales en el patio noroccidental y las tres meridionales en el patio receptor meridional. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o4-receipt / o4 latched once | none | Both fictional note groups arrived at their separately assigned yards. | Ambos grupos ficticios de notas han llegado a sus patios asignados por separado. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.o4-reaction / after o4 receipt | miriam-archive | A preserved work note is not the recovered voice of a dead person. | Una nota de trabajo conservada no recupera la voz de una persona muerta. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at a separate household supply stop. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en una parada separada de provisiones domésticas. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-1-complete / side-1 completed | none | A separate household supply stop completed. Its stated benefit has been granted once. | Una parada separada de provisiones domésticas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-1-lost / side-1 failed-optional | none | A separate household supply stop is unavailable after the loss of its unique participant or object. The main mission continues. | Una parada separada de provisiones domésticas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-2-goal / optional list from start | none | Bring both voluntary evacuee groups from two independent inland travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de dos viajeros interiores independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-2-complete / side-2 completed | none | Two independent inland travelers completed. Its stated benefit has been granted once. | Dos viajeros interiores independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-2-lost / side-2 failed-optional | none | Two independent inland travelers is unavailable after the loss of its unique participant or object. The main mission continues. | Dos viajeros interiores independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-3-goal / optional list from start | none | Recover both separate copies from the attributed letter’s context and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de el contexto de la carta atribuida y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-3-complete / side-3 completed | none | The attributed letter’s context completed. Its stated benefit has been granted once. | El contexto de la carta atribuida: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-3-lost / side-3 failed-optional | none | The attributed letter’s context is unavailable after the loss of its unique participant or object. The main mission continues. | El contexto de la carta atribuida: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the west-road supply store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el almacén de provisiones del camino oeste. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-4-complete / side-4 completed | none | The west-road supply store completed. Its stated benefit has been granted once. | El almacén de provisiones del camino oeste: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-4-lost / side-4 failed-optional | none | The west-road supply store is unavailable after the loss of its unique participant or object. The main mission continues. | El almacén de provisiones del camino oeste: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of southern approach viewpoints. Benefit: Mark the surveyed southern-road land circuit once. All main receivers remain disclosed without this optional task. | Explora los dos miradores señalados de miradores del acceso meridional. Ventaja: Señala una vez el circuito terrestre trazado southern-road. Todos los receptores principales siguen identificados sin esta tarea opcional. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-5-complete / side-5 completed | none | Southern approach viewpoints completed. Its stated benefit has been granted once. | Miradores del acceso meridional: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-5-lost / side-5 failed-optional | none | Southern approach viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores del acceso meridional: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-6-goal / optional list from start | none | Escort the local guide of a western hill guide to the marked road junction. Benefit: Mark the surveyed relief land circuit once. All main receivers remain disclosed without this optional task. | Escolta al guía local de un guía de las colinas occidentales hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado relief. Todos los receptores principales siguen identificados sin esta tarea opcional. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-6-complete / side-6 completed | none | A western hill guide completed. Its stated benefit has been granted once. | Un guía de las colinas occidentales: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.side-6-lost / side-6 failed-optional | none | A western hill guide is unavailable after the loss of its unique participant or object. The main mission continues. | Un guía de las colinas occidentales: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.fact-outro / victory first | collection-narrator | The recorded fictional household group reached its inland reception, and six separate local work notes reached two preservation yards. None is an ancient witness, recovered relic or rescued martyr. The source’s deaths and destruction of remains remain outside the player’s power. | El grupo registrado de hogares ficticios llegó a su recepción interior y seis notas locales separadas llegaron a dos patios de conservación. No son testigos antiguos, reliquias recuperadas ni mártires rescatados. Las muertes y la destrucción de restos relatadas por la fuente permanecen fuera del poder del jugador. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.persona-outro / after fact-outro | miriam-archive | Keeping invented neighbors alive has not made that old letter less sorrowful. I can care for the small story entrusted to my hands without claiming to mend the larger one. | Mantener vivos a vecinos inventados no ha hecho menos triste aquella carta. Puedo cuidar la pequeña historia confiada a mis manos sin pretender reparar la mayor. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.24-witness-and-evacuation-lyon.odyssey.next-episode / after persona-outro | none | Continue with Voices Against the Fragments. This episode does not complete the campaign. | Continúa con Voces frente a los fragmentos. Este episodio no termina la campaña. |

## Production, recovery and verification

```json
{
  "stateMachine": {
    "states": [
      "briefing",
      "phase-1",
      "phase-2",
      "phase-3",
      "phase-4",
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
        "to": "phase-4",
        "on": "objective-latched",
        "objectiveId": "o3"
      },
      {
        "from": "phase-4",
        "to": "victory",
        "on": "objective-latched",
        "objectiveId": "o4"
      }
    ],
    "terminalPriority": "defeat first; close side rewards; one terminal latch",
    "saveLoad": "persist object identities, arrivals, collected facts, receipts, phase elapsed time and side reward balances",
    "campaignProgressWrite": false
  },
  "failureRecovery": {
    "mainIdentityLoss": "explicitly irrecoverable main-object loss causes defeat; survivor groups tolerate only their declared loss margin",
    "optionalIdentityLoss": "only corresponding task becomes failed-optional",
    "recoveryImplementation": "inventory/replacement capability pending; reserved resources alone cannot resurrect an identity"
  },
  "requiredCapabilities": [
    {
      "id": "composed-world-ledger",
      "status": "reference model implemented; native implementation pending"
    },
    {
      "id": "geographic-land-corridors",
      "status": "real-world plan authored; DEM/footprints/pathfinding pending"
    },
    {
      "id": "two-narrator-sequence",
      "status": "caption text authored; certified native SequenceItems pending"
    }
  ],
  "artDirection": {
    "style": "sober Roman-era regional illustration; own geographic vector plan as research visual",
    "historicalControls": "no modern objects, invented quotation, sacred-person combat unit or later religious architecture",
    "referenceAssets": [
      "lyon-fourviere-theatre"
    ],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "stage nine households: any eight of those actual nine may reach onward; an unstaged tenth cannot substitute",
      "stage exactly eight, lose one: later unstaged household cannot replace that ledger member; main contract fails",
      "a north note at the southern yard cannot satisfy the north delivery",
      "no martyr identity or authentic testimony is an entity",
      "no optional traveler replaces staged household",
      "no prison liberation, amphitheater assault, forced apostasy or ash-recovery goal",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
