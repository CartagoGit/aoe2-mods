# 7. The Doors That Closed

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `07-household-relocation-rome-ostia` · c. 49 CE · 360×360

## Historical frame and fixed outcome

EN: Suetonius reports disturbances among Jews in Rome and an expulsion under Claudius, mentioning Chrestus. The identification and conventional dating around 49 remain debated. The households here are fictional.

ES: Suetonio informa de disturbios entre judíos de Roma y una expulsión bajo Claudio, y menciona a Chrestus. Su identificación y la fecha convencional hacia 49 siguen debatidas. Los hogares del escenario son ficticios.

EN: The relocation illustrates a consequence of the expulsion account. It does not establish that all Roman Jews left, identify Chrestus, or prove this specific departure route.

ES: El traslado ilustra una consecuencia del relato de expulsión. No demuestra que todos los judíos romanos se marcharan, identifica a Chrestus ni acredita esta ruta concreta.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 31,
      "episodeId": "07-household-relocation-rome-ostia",
      "order": 7,
      "selectedSourceUrl": "https://lexundria.com/suet_cl/25.4/r",
      "consultedUrl": "https://lexundria.com/suet_cl/25.4/r",
      "passage": "Suetonius, Claudius 25.4: Claudius expels Jews from Rome after disturbances 'impulsore Chresto'. Cambridge scholarly article search result notes scholarly disagreement in dating this incident (41 vs c.49).",
      "supportedClaim": {
        "en": "Suetonius reports disturbances among Jews in Rome and an expulsion under Claudius, mentioning 'Chrestus'.",
        "es-ES": "Suetonio informa de disturbios entre judíos de Roma y una expulsión bajo Claudio, y menciona a «Chrestus»."
      },
      "limitations": "The text does not identify Chrestus with Jesus/Christ, specify a year, or show that Christians were the only people expelled. The c.49 date is conventional and debated; this candidate's Christian-conflict reading is a hypothesis.",
      "consultationDate": "2026-10-12",
      "status": "disputed",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
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

EN: Collect three luggage consignments and assemble six of the eight households alive at the supply yard.

ES: Recoge tres remesas de equipaje y reúne con vida seis de los ocho hogares en el patio de suministros.

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
        "faith-origins.07-household-relocation-rome-ostia.luggage-1",
        "faith-origins.07-household-relocation-rome-ostia.luggage-2",
        "faith-origins.07-household-relocation-rome-ostia.luggage-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.07-household-relocation-rome-ostia.departing-households-1",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-4",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-5",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-6",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-7",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-8"
      ],
      "destinations": {
        "faith-origins.07-household-relocation-rome-ostia.departing-households-1": "faith-origins.07-household-relocation-rome-ostia.destination-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-2": "faith-origins.07-household-relocation-rome-ostia.destination-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-3": "faith-origins.07-household-relocation-rome-ostia.destination-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-4": "faith-origins.07-household-relocation-rome-ostia.destination-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-5": "faith-origins.07-household-relocation-rome-ostia.destination-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-6": "faith-origins.07-household-relocation-rome-ostia.destination-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-7": "faith-origins.07-household-relocation-rome-ostia.destination-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-8": "faith-origins.07-household-relocation-rome-ostia.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true,
  "exportedLedgers": [
    {
      "id": "staged-households",
      "operator": "intersection",
      "fromRequirements": [
        "req-2"
      ],
      "minimumCount": 6
    }
  ]
}
```

EN: Three luggage identities and six household arrivals are required.

ES: Se requieren tres identidades de equipaje y seis llegadas de hogares.

EN: Their bundles do not tell us what Chrestus meant.

ES: Sus bultos no nos dicen qué significaba Chrestus.

### o2 / phase-2

EN: Fund one onward provision of 280 food and 40 wood.

ES: Financia una provisión de salida de 280 de alimento y 40 de madera.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 280,
        "wood": 40
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.07-household-relocation-rome-ostia.destination-2"
      ],
      "allocations": {
        "faith-origins.07-household-relocation-rome-ostia.destination-2": {
          "food": 280,
          "wood": 40
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.07-household-relocation-rome-ostia.o2.req-1.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: One onward-provision receipt is registered.

ES: Un único recibo de provisión de salida queda registrado.

EN: Keep the food separate from the money promised for later.

ES: Distingue la comida de lo que se promete pagar después.

### o3 / phase-3

EN: Bring at least six of the recorded households and all three luggage consignments to the north-bank departure district.

ES: Lleva al menos seis hogares registrados y las tres remesas de equipaje al barrio de salida de la orilla norte.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o1",
        "ledger": "staged-households"
      },
      "id": "req-1",
      "entities": [
        "faith-origins.07-household-relocation-rome-ostia.departing-households-1",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-4",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-5",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-6",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-7",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-8"
      ],
      "destinations": {
        "faith-origins.07-household-relocation-rome-ostia.departing-households-1": "faith-origins.07-household-relocation-rome-ostia.destination-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-2": "faith-origins.07-household-relocation-rome-ostia.destination-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-3": "faith-origins.07-household-relocation-rome-ostia.destination-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-4": "faith-origins.07-household-relocation-rome-ostia.destination-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-5": "faith-origins.07-household-relocation-rome-ostia.destination-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-6": "faith-origins.07-household-relocation-rome-ostia.destination-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-7": "faith-origins.07-household-relocation-rome-ostia.destination-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-8": "faith-origins.07-household-relocation-rome-ostia.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.07-household-relocation-rome-ostia.luggage-1",
        "faith-origins.07-household-relocation-rome-ostia.luggage-2",
        "faith-origins.07-household-relocation-rome-ostia.luggage-3"
      ],
      "destinations": {
        "faith-origins.07-household-relocation-rome-ostia.luggage-1": "faith-origins.07-household-relocation-rome-ostia.destination-3",
        "faith-origins.07-household-relocation-rome-ostia.luggage-2": "faith-origins.07-household-relocation-rome-ostia.destination-3",
        "faith-origins.07-household-relocation-rome-ostia.luggage-3": "faith-origins.07-household-relocation-rome-ostia.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The same households and three distinct consignments reached departure.

ES: Los mismos hogares y tres remesas distintas han llegado a la salida.

EN: The ledger records a departure, not the disappearance of a people.

ES: El registro recoge una salida, no la desaparición de un pueblo.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/07-household-relocation-rome-ostia.svg)

```json
{
  "bbox": [
    12.18,
    41.69,
    12.56,
    41.96
  ],
  "terrainProfile": "rome-ostia",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        245.29,
        117.24
      ],
      "lonLat": [
        12.448,
        41.88
      ],
      "name": {
        "en": "West-bank staging households",
        "es-ES": "Hogares de preparación en la orilla oeste"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        199.74,
        161.39
      ],
      "lonLat": [
        12.394,
        41.841
      ],
      "name": {
        "en": "Western road supply yard",
        "es-ES": "Patio de suministros del camino occidental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        144.07,
        207.8
      ],
      "lonLat": [
        12.328,
        41.8
      ],
      "name": {
        "en": "North-bank departure district",
        "es-ES": "Barrio de salida en la orilla norte"
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
      "widthTiles": 10
    },
    {
      "id": "relief",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "alternative surveyed land access in the same districts; exact intermediate geometry pending, never invent a crossing"
    }
  ],
  "terrainInstructions": "One-bank land itinerary toward the lower Tiber; departure is off-map travel, not a complete ship voyage. Avoid the later imperial Portus basin in a c49 scene. No forced bridge or cross-sea foot route.",
  "mainRouteLengthStraightTiles": 135.91,
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
        12.477,
        41.95
      ],
      [
        12.47,
        41.925
      ],
      [
        12.47,
        41.9
      ],
      [
        12.475,
        41.87
      ],
      [
        12.42,
        41.85
      ],
      [
        12.4,
        41.8
      ],
      [
        12.28,
        41.76
      ],
      [
        12.23,
        41.73
      ]
    ],
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
  "asset": "docs/design/maps/faith-origins/odyssey/07-household-relocation-rome-ostia.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.departing-households-1",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.departing-households-2",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.departing-households-3",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.departing-households-4",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.departing-households-5",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.departing-households-6",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.departing-households-7",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.departing-households-8",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.luggage-1",
      "role": "fictional-household-consignment",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.luggage-2",
      "role": "fictional-household-consignment",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.luggage-3",
      "role": "fictional-household-consignment",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.07-household-relocation-rome-ostia.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    }
  ],
  "objectGroups": {
    "departing-households": [
      "faith-origins.07-household-relocation-rome-ostia.departing-households-1",
      "faith-origins.07-household-relocation-rome-ostia.departing-households-2",
      "faith-origins.07-household-relocation-rome-ostia.departing-households-3",
      "faith-origins.07-household-relocation-rome-ostia.departing-households-4",
      "faith-origins.07-household-relocation-rome-ostia.departing-households-5",
      "faith-origins.07-household-relocation-rome-ostia.departing-households-6",
      "faith-origins.07-household-relocation-rome-ostia.departing-households-7",
      "faith-origins.07-household-relocation-rome-ostia.departing-households-8"
    ],
    "luggage": [
      "faith-origins.07-household-relocation-rome-ostia.luggage-1",
      "faith-origins.07-household-relocation-rome-ostia.luggage-2",
      "faith-origins.07-household-relocation-rome-ostia.luggage-3"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.07-household-relocation-rome-ostia.departing-households-1",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-2",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-3",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-4",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-5",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-6",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-7",
        "faith-origins.07-household-relocation-rome-ostia.departing-households-8"
      ],
      "minimumAliveOrAlreadySafe": 6
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Roadside households / Hogares del camino

EN: Bring each of the two aid crates to its assigned household at roadside households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del camino. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid supports departure without changing the expulsion claim.

ES: El auxilio apoya la salida sin cambiar la afirmación sobre expulsión.

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
          "07-household-relocation-rome-ostia.side-1.entity-1",
          "07-household-relocation-rome-ostia.side-1.entity-2"
        ],
        "destinations": {
          "07-household-relocation-rome-ostia.side-1.entity-1": "07-household-relocation-rome-ostia.side-1.zone-1",
          "07-household-relocation-rome-ostia.side-1.entity-2": "07-household-relocation-rome-ostia.side-1.zone-2"
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
        "id": "07-household-relocation-rome-ostia.side-1.entity-1",
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
        "id": "07-household-relocation-rome-ostia.side-1.entity-2",
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
        "id": "07-household-relocation-rome-ostia.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "07-household-relocation-rome-ostia.side-1.zone-2",
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
      "onceFlag": "07-household-relocation-rome-ostia.side-1.rewarded",
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
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Property lists / Listas de pertenencias

EN: Recover both separate copies from property lists and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de listas de pertenencias y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Copies preserve fictional possessions.

ES: Las copias conservan pertenencias ficticias.

```json
{
  "id": "side-2",
  "kind": "copy",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "07-household-relocation-rome-ostia.side-2.entity-1",
          "07-household-relocation-rome-ostia.side-2.entity-2"
        ],
        "destinations": {
          "07-household-relocation-rome-ostia.side-2.entity-1": "07-household-relocation-rome-ostia.side-2.zone-1",
          "07-household-relocation-rome-ostia.side-2.entity-2": "07-household-relocation-rome-ostia.side-2.zone-1"
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
        "id": "07-household-relocation-rome-ostia.side-2.entity-1",
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
        "id": "07-household-relocation-rome-ostia.side-2.entity-2",
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
        "id": "07-household-relocation-rome-ostia.side-2.zone-1",
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
      "onceFlag": "07-household-relocation-rome-ostia.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.07-household-relocation-rome-ostia"
      ],
      "historicalNote": {
        "en": "Suetonius reports disturbances among Jews in Rome and an expulsion under Claudius, mentioning Chrestus. The identification and conventional dating around 49 remain debated. The households here are fictional.",
        "es-ES": "Suetonio informa de disturbios entre judíos de Roma y una expulsión bajo Claudio, y menciona a Chrestus. Su identificación y la fecha convencional hacia 49 siguen debatidas. Los hogares del escenario son ficticios."
      },
      "hint": {
        "en": "Collect three luggage consignments and assemble six of the eight households alive at the supply yard.",
        "es-ES": "Recoge tres remesas de equipaje y reúne con vida seis de los ocho hogares en el patio de suministros."
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
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Waystation roof / Techo de la parada

EN: Pay 50 wood and restore the damaged store of waystation roof to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de techo de la parada. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Finite repair supports land logistics.

ES: La reparación finita facilita la logística terrestre.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "07-household-relocation-rome-ostia.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "07-household-relocation-rome-ostia.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "07-household-relocation-rome-ostia.side-3.payment",
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
        "id": "07-household-relocation-rome-ostia.side-3.entity-1",
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
        "id": "07-household-relocation-rome-ostia.side-3.zone-1",
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
      "onceFlag": "07-household-relocation-rome-ostia.side-3.rewarded",
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
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Road consignment / Remesa del camino

EN: Escort the trader of road consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de remesa del camino hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One trade provides bounded food.

ES: Un intercambio aporta alimento limitado.

```json
{
  "id": "side-4",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "07-household-relocation-rome-ostia.side-4.entity-1"
        ],
        "destinations": {
          "07-household-relocation-rome-ostia.side-4.entity-1": "07-household-relocation-rome-ostia.side-4.zone-1"
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
        "receipt": "07-household-relocation-rome-ostia.side-4.payment",
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
        "id": "07-household-relocation-rome-ostia.side-4.entity-1",
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
        "id": "07-household-relocation-rome-ostia.side-4.zone-1",
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
      "onceFlag": "07-household-relocation-rome-ostia.side-4.rewarded",
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
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### North-bank guide / Guía de la orilla norte

EN: Escort the local guide of north-bank guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía de la orilla norte hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: Keeps the journey on one bank; no invented Tiber crossing.

ES: Mantiene el viaje en una orilla; no inventa un cruce del Tíber.

```json
{
  "id": "side-5",
  "kind": "guide",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "07-household-relocation-rome-ostia.side-5.entity-1"
        ],
        "destinations": {
          "07-household-relocation-rome-ostia.side-5.entity-1": "07-household-relocation-rome-ostia.side-5.zone-1"
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
        "id": "07-household-relocation-rome-ostia.side-5.entity-1",
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
        "id": "07-household-relocation-rome-ostia.side-5.zone-1",
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
      "target": "relief corridor",
      "resources": {},
      "onceFlag": "07-household-relocation-rome-ostia.side-5.rewarded",
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
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Independent travelers / Viajeros independientes

EN: Bring both voluntary evacuee groups from independent travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de viajeros independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Two optional groups never substitute for main households.

ES: Dos grupos opcionales nunca sustituyen a los hogares principales.

```json
{
  "id": "side-6",
  "kind": "extract",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "07-household-relocation-rome-ostia.side-6.entity-1",
          "07-household-relocation-rome-ostia.side-6.entity-2"
        ],
        "destinations": {
          "07-household-relocation-rome-ostia.side-6.entity-1": "07-household-relocation-rome-ostia.side-6.zone-1",
          "07-household-relocation-rome-ostia.side-6.entity-2": "07-household-relocation-rome-ostia.side-6.zone-1"
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
        "id": "07-household-relocation-rome-ostia.side-6.entity-1",
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
        "id": "07-household-relocation-rome-ostia.side-6.entity-2",
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
        "id": "07-household-relocation-rome-ostia.side-6.zone-1",
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
      "onceFlag": "07-household-relocation-rome-ostia.side-6.rewarded",
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
      "id": "household-provision",
      "optionalObjectives": [
        "side-1",
        "side-3",
        "side-4"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Detours and 50 wood/50 gold buy finite material reserves; no mandatory dependency."
    },
    {
      "id": "records-and-route",
      "optionalObjectives": [
        "side-2",
        "side-5"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Travel to the copyist and guide buys context and route information; no new historical certainty."
    },
    {
      "id": "civilian-care",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Voluntary arrivals protect distinct optional households; no substitution for main participants."
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
      "food": 1498,
      "wood": 748,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 280,
      "wood": 40,
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
      "food": 1350,
      "wood": 720,
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
      "food": 1550,
      "wood": 770,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 280,
      "wood": 40,
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
      "food": 1350,
      "wood": 720,
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
      "food": 1603,
      "wood": 793,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 280,
      "wood": 40,
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
      "food": 1350,
      "wood": 720,
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
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.title / always | none | The Doors That Closed | Las puertas que se cerraron |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.fact-intro / intro first | collection-narrator | Suetonius reports disturbances among Jews in Rome and an expulsion under Claudius, mentioning Chrestus. The identification and conventional dating around 49 remain debated. The households here are fictional. | Suetonio informa de disturbios entre judíos de Roma y una expulsión bajo Claudio, y menciona a Chrestus. Su identificación y la fecha convencional hacia 49 siguen debatidas. Los hogares del escenario son ficticios. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.persona-intro / after handover | miriam-archive | A distant writer leaves a name we cannot securely identify. I will not turn that uncertainty into a reason to erase the people who had to leave. | Un autor lejano deja un nombre que no podemos identificar con certeza. No convertiré esa incertidumbre en una razón para borrar a quienes tuvieron que marcharse. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.route-help / available from start; repeatable without effect | none | Keep to the north-bank land itinerary. The final departure is a fictional off-map continuation; do not enter water to reach it. | Sigue el itinerario terrestre de la orilla norte. La salida final es una continuación ficticia fuera del mapa; no entres en el agua para alcanzarla. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.o1-goal / phase-1 active | none | Collect three luggage consignments and assemble six of the eight households alive at the supply yard. | Recoge tres remesas de equipaje y reúne con vida seis de los ocho hogares en el patio de suministros. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.o1-receipt / o1 latched once | none | Three luggage identities and six household arrivals are required. | Se requieren tres identidades de equipaje y seis llegadas de hogares. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.o1-reaction / after o1 receipt | miriam-archive | Their bundles do not tell us what Chrestus meant. | Sus bultos no nos dicen qué significaba Chrestus. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.o2-goal / phase-2 active | none | Fund one onward provision of 280 food and 40 wood. | Financia una provisión de salida de 280 de alimento y 40 de madera. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.o2-receipt / o2 latched once | none | One onward-provision receipt is registered. | Un único recibo de provisión de salida queda registrado. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.o2-reaction / after o2 receipt | miriam-archive | Keep the food separate from the money promised for later. | Distingue la comida de lo que se promete pagar después. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.o3-goal / phase-3 active | none | Bring at least six of the recorded households and all three luggage consignments to the north-bank departure district. | Lleva al menos seis hogares registrados y las tres remesas de equipaje al barrio de salida de la orilla norte. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.o3-receipt / o3 latched once | none | The same households and three distinct consignments reached departure. | Los mismos hogares y tres remesas distintas han llegado a la salida. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.o3-reaction / after o3 receipt | miriam-archive | The ledger records a departure, not the disappearance of a people. | El registro recoge una salida, no la desaparición de un pueblo. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at roadside households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del camino. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-1-complete / side-1 completed | none | Roadside households completed. Its stated benefit has been granted once. | Hogares del camino: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-1-lost / side-1 failed-optional | none | Roadside households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares del camino: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from property lists and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de listas de pertenencias y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-2-complete / side-2 completed | none | Property lists completed. Its stated benefit has been granted once. | Listas de pertenencias: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-2-lost / side-2 failed-optional | none | Property lists is unavailable after the loss of its unique participant or object. The main mission continues. | Listas de pertenencias: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of waystation roof to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de techo de la parada. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-3-complete / side-3 completed | none | Waystation roof completed. Its stated benefit has been granted once. | Techo de la parada: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-3-lost / side-3 failed-optional | none | Waystation roof is unavailable after the loss of its unique participant or object. The main mission continues. | Techo de la parada: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-4-goal / optional list from start | none | Escort the trader of road consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de remesa del camino hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-4-complete / side-4 completed | none | Road consignment completed. Its stated benefit has been granted once. | Remesa del camino: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-4-lost / side-4 failed-optional | none | Road consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Remesa del camino: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-5-goal / optional list from start | none | Escort the local guide of north-bank guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía de la orilla norte hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-5-complete / side-5 completed | none | North-bank guide completed. Its stated benefit has been granted once. | Guía de la orilla norte: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-5-lost / side-5 failed-optional | none | North-bank guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía de la orilla norte: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from independent travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de viajeros independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-6-complete / side-6 completed | none | Independent travelers completed. Its stated benefit has been granted once. | Viajeros independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.side-6-lost / side-6 failed-optional | none | Independent travelers is unavailable after the loss of its unique participant or object. The main mission continues. | Viajeros independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.fact-outro / victory first | collection-narrator | The relocation illustrates a consequence of the expulsion account. It does not establish that all Roman Jews left, identify Chrestus, or prove this specific departure route. | El traslado ilustra una consecuencia del relato de expulsión. No demuestra que todos los judíos romanos se marcharan, identifica a Chrestus ni acredita esta ruta concreta. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.persona-outro / after fact-outro | miriam-archive | A household carries more than a label another person gave it. Our archive should leave room for that burden. | Un hogar lleva más que la etiqueta que otra persona le puso. Nuestro archivo debe dejar espacio para esa carga. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.07-household-relocation-rome-ostia.odyssey.next-episode / after persona-outro | none | Continue with A Place for the Stranger. This episode does not complete the campaign. | Continúa con Un lugar para el extranjero. Este episodio no termina la campaña. |

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
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "same six households from staging ledger required",
      "six families without three consignments cannot win",
      "no Portus Claudian completed harbor assumed before its construction",
      "no unexplained whole-city expulsion or exclusive Christian victim claim",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
