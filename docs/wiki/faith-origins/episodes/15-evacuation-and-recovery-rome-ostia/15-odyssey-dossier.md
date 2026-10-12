# 15. Ash over the Seven Hills

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `15-evacuation-and-recovery-rome-ostia` · 64 CE · 400×400

## Historical frame and fixed outcome

EN: Tacitus reports that after Rome’s fire in 64 Nero punished people called Christians. He wrote decades later and did not establish that Christians caused the fire. The local civilian evacuation here is a fictional reconstruction, not a separately documented event.

ES: Tácito relata que tras el incendio de Roma en 64 Nerón castigó a personas llamadas cristianas. Escribió décadas después y no demostró que los cristianos causaran el incendio. La evacuación civil local es una reconstrucción ficticia, no un hecho documentado por separado.

EN: Fictional households and property have reached the local departure district. This does not reverse the deaths Tacitus reports, identify every punishment site or make a Roman episode into an empire-wide policy.

ES: Los hogares y bienes ficticios han alcanzado el barrio local de salida. Esto no revierte las muertes relatadas por Tácito, identifica todos los lugares de castigo ni transforma un episodio romano en una política de todo el imperio.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 8,
      "episodeId": "15-evacuation-and-recovery-rome-ostia",
      "order": 15,
      "selectedSourceUrl": "https://www.perseus.tufts.edu/hopper/text?doc=Tac.+Ann.+15.44",
      "consultedUrl": "https://dcc.dickinson.edu/tacitus-annals/15-44",
      "passage": "Tacitus, Annals 15.44, relating the Rome fire, Nero's response, and punishments of Christians; DCC notes source limits and comparison with Suetonius/Pliny.",
      "supportedClaim": {
        "en": "Tacitus reports that after the Rome fire Nero punished people called Christians and describes Christus' execution under Pilate.",
        "es-ES": "Tácito informa de que, tras el incendio de Roma, Nerón castigó a personas llamadas cristianas y describe la ejecución de Christus bajo Pilato."
      },
      "limitations": "Tacitus wrote decades later and is not an eyewitness to the punishment. His account does not prove Christians caused the fire; indeed he portrays the arson charge as a scapegoating measure. No separately documented evacuation/recovery episode.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
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

EN: Collect all four property chests and bring at least eight of the ten households alive to the refuge yard.

ES: Recoge los cuatro arcones de bienes y lleva con vida al menos ocho de los diez hogares al patio de refugio.

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
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-1",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-4"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 8,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-1",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-4",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-5",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-6",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-7",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-8",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-9",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-10"
      ],
      "destinations": {
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-1": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-2": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-3": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-4": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-5": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-6": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-7": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-8": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-9": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-10": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true,
  "exportedLedgers": [
    {
      "id": "sheltered-households",
      "operator": "intersection",
      "fromRequirements": [
        "req-2"
      ],
      "minimumCount": 8
    }
  ]
}
```

EN: Four chests collected and at least eight original household identities sheltered.

ES: Cuatro arcones recogidos y al menos ocho identidades originales de hogares refugiadas.

EN: The household names are ours to invent; the victims in the source are not ours to erase.

ES: Podemos inventar los nombres de estos hogares; no podemos borrar las víctimas de la fuente.

### o2 / phase-2

EN: Take the four chests to the refuge, pay 300 food and 80 wood once, and derive two fictional departure notes from the collected chests.

ES: Lleva los cuatro arcones al refugio, paga una sola vez 300 de alimento y 80 de madera y elabora dos notas ficticias de salida a partir de los arcones recogidos.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-1",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-4"
      ],
      "destinations": {
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-1": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-2": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-3": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-4": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 300,
        "wood": 80
      },
      "id": "req-2",
      "receivingZones": [
        "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2"
      ],
      "allocations": {
        "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2": {
          "food": 300,
          "wood": 80
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.15-evacuation-and-recovery-rome-ostia.o2.req-2.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "requiresInputsCollected": true,
      "id": "req-3",
      "inputEntities": [
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-1",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-4"
      ],
      "outputEntities": [
        "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-1",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-2"
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Four property arrivals, one provisioning debit and two derived notes recorded.

ES: Cuatro llegadas de bienes, un cobro de provisiones y dos notas derivadas registrados.

EN: Food for departure is concrete; a promise to restore everything is not.

ES: El alimento para salir es concreto; la promesa de restaurarlo todo no.

### o3 / phase-3

EN: Bring at least eight of the same sheltered households, all four chests and both notes to the eastern land departure court.

ES: Lleva al menos ocho de los mismos hogares refugiados, los cuatro arcones y ambas notas al patio terrestre de salida oriental.

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
        "ledger": "sheltered-households"
      },
      "id": "req-1",
      "entities": [
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-1",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-4",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-5",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-6",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-7",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-8",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-9",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-10"
      ],
      "destinations": {
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-1": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-2": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-3": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-4": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-5": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-6": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-7": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-8": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-9": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-10": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-1",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-4"
      ],
      "destinations": {
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-1": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-2": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-3": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-4": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-1",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-2"
      ],
      "destinations": {
        "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-1": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-2": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The same eight-or-more sheltered identities and all required property/notes arrived.

ES: Han llegado las mismas ocho o más identidades refugiadas y todos los bienes y notas requeridos.

EN: A local escape is the most this fiction can promise. It cannot rewrite the account.

ES: Una salida local es cuanto puede prometer esta ficción. No puede reescribir el relato.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/15-evacuation-and-recovery-rome-ostia.svg)

```json
{
  "bbox": [
    12.47,
    41.84,
    12.555,
    41.91
  ],
  "terrainProfile": "rome-ostia",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        163.5,
        128.25
      ],
      "lonLat": [
        12.503,
        41.889
      ],
      "name": {
        "en": "Eastern local assembly yard",
        "es-ES": "Patio local de reunión oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        114.24,
        230.04
      ],
      "lonLat": [
        12.49,
        41.869
      ],
      "name": {
        "en": "Southern inland refuge yard",
        "es-ES": "Patio interior de refugio al sur"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        299.92,
        301.29
      ],
      "lonLat": [
        12.539,
        41.855
      ],
      "name": {
        "en": "Eastern land departure court",
        "es-ES": "Patio de salida terrestre oriental"
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
  "terrainInstructions": "Local east/south Rome land scene, all three main districts east of Tiber; do not use giant Rome–Ostia profile as a complete burn map. No forced river crossing or Vatican punishment-site claim. Blocked/burnt areas require dated topography and independently certified finite hazard observation; always one disclosed main-safe land corridor and one longer alternative, never adaptive closure of both.",
  "mainRouteLengthStraightTiles": 311.96,
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
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/15-evacuation-and-recovery-rome-ostia.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-1",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-2",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-3",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-4",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-5",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-6",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-7",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-8",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-9",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-10",
      "role": "fictional-independent-civilian-household",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-1",
      "role": "fictional-household-property-chest",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-2",
      "role": "fictional-household-property-chest",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-3",
      "role": "fictional-household-property-chest",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-4",
      "role": "fictional-household-property-chest",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-1",
      "role": "fictional-local-departure-note",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-2",
      "role": "fictional-local-departure-note",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.15-evacuation-and-recovery-rome-ostia.destination-3",
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
    "evacuation-households": [
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-1",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-2",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-3",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-4",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-5",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-6",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-7",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-8",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-9",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-10"
    ],
    "household-chests": [
      "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-1",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-2",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-3",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.household-chests-4"
    ],
    "local-departure-notes": [
      "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-1",
      "faith-origins.15-evacuation-and-recovery-rome-ostia.local-departure-notes-2"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-1",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-2",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-3",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-4",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-5",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-6",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-7",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-8",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-9",
        "faith-origins.15-evacuation-and-recovery-rome-ostia.evacuation-households-10"
      ],
      "minimumAliveOrAlreadySafe": 8
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Separate displaced families / Familias desplazadas separadas

EN: Bring both voluntary evacuee groups from separate displaced families to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de familias desplazadas separadas al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Two voluntary groups are distinct from the ten mandatory household identities.

ES: Dos grupos voluntarios son distintos de las diez identidades de hogares principales.

```json
{
  "id": "side-1",
  "kind": "extract",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "15-evacuation-and-recovery-rome-ostia.side-1.entity-1",
          "15-evacuation-and-recovery-rome-ostia.side-1.entity-2"
        ],
        "destinations": {
          "15-evacuation-and-recovery-rome-ostia.side-1.entity-1": "15-evacuation-and-recovery-rome-ostia.side-1.zone-1",
          "15-evacuation-and-recovery-rome-ostia.side-1.entity-2": "15-evacuation-and-recovery-rome-ostia.side-1.zone-1"
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-1.entity-1",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-1.entity-2",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-1.zone-1",
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
      "onceFlag": "15-evacuation-and-recovery-rome-ostia.side-1.rewarded",
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

### Independent refuge households / Hogares independientes del refugio

EN: Bring each of the two aid crates to its assigned household at independent refuge households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes del refugio. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid gives finite supplies without altering Tacitus’ reported victims.

ES: La ayuda aporta suministros finitos sin alterar las víctimas relatadas por Tácito.

```json
{
  "id": "side-2",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "15-evacuation-and-recovery-rome-ostia.side-2.entity-1",
          "15-evacuation-and-recovery-rome-ostia.side-2.entity-2"
        ],
        "destinations": {
          "15-evacuation-and-recovery-rome-ostia.side-2.entity-1": "15-evacuation-and-recovery-rome-ostia.side-2.zone-1",
          "15-evacuation-and-recovery-rome-ostia.side-2.entity-2": "15-evacuation-and-recovery-rome-ostia.side-2.zone-2"
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-2.entity-1",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-2.entity-2",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "15-evacuation-and-recovery-rome-ostia.side-2.zone-2",
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
      "onceFlag": "15-evacuation-and-recovery-rome-ostia.side-2.rewarded",
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

### Eastern land guide / Guía terrestre oriental

EN: Escort the local guide of eastern land guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía terrestre oriental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: Marks an alternative land corridor; never creates a bridge over the Tiber.

ES: Señala un corredor terrestre alternativo; nunca crea un puente sobre el Tíber.

```json
{
  "id": "side-3",
  "kind": "guide",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "15-evacuation-and-recovery-rome-ostia.side-3.entity-1"
        ],
        "destinations": {
          "15-evacuation-and-recovery-rome-ostia.side-3.entity-1": "15-evacuation-and-recovery-rome-ostia.side-3.zone-1"
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-3.entity-1",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-3.zone-1",
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
      "onceFlag": "15-evacuation-and-recovery-rome-ostia.side-3.rewarded",
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

### Unburned roadside store / Almacén del camino sin quemar

EN: Pay 50 wood and restore the damaged store of unburned roadside store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén del camino sin quemar. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair occurs in a safe fictional store, not under a lethal mandatory deadline.

ES: La reparación sucede en un almacén ficticio seguro, no bajo un plazo mortal obligatorio.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "15-evacuation-and-recovery-rome-ostia.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "15-evacuation-and-recovery-rome-ostia.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "15-evacuation-and-recovery-rome-ostia.side-4.payment",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-4.entity-1",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-4.zone-1",
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
      "onceFlag": "15-evacuation-and-recovery-rome-ostia.side-4.rewarded",
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

### Independent property notes / Notas independientes de pertenencias

EN: Recover both separate copies from independent property notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de notas independientes de pertenencias y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Fictional local notes unlock attributed historical context, not Tacitus manuscripts in 64.

ES: Las notas locales ficticias desbloquean contexto histórico atribuido, no manuscritos de Tácito en 64.

```json
{
  "id": "side-5",
  "kind": "copy",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "15-evacuation-and-recovery-rome-ostia.side-5.entity-1",
          "15-evacuation-and-recovery-rome-ostia.side-5.entity-2"
        ],
        "destinations": {
          "15-evacuation-and-recovery-rome-ostia.side-5.entity-1": "15-evacuation-and-recovery-rome-ostia.side-5.zone-1",
          "15-evacuation-and-recovery-rome-ostia.side-5.entity-2": "15-evacuation-and-recovery-rome-ostia.side-5.zone-1"
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-5.entity-1",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-5.entity-2",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-5.zone-1",
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
      "onceFlag": "15-evacuation-and-recovery-rome-ostia.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.15-evacuation-and-recovery-rome-ostia"
      ],
      "historicalNote": {
        "en": "Tacitus reports that after Rome’s fire in 64 Nero punished people called Christians. He wrote decades later and did not establish that Christians caused the fire. The local civilian evacuation here is a fictional reconstruction, not a separately documented event.",
        "es-ES": "Tácito relata que tras el incendio de Roma en 64 Nerón castigó a personas llamadas cristianas. Escribió décadas después y no demostró que los cristianos causaran el incendio. La evacuación civil local es una reconstrucción ficticia, no un hecho documentado por separado."
      },
      "hint": {
        "en": "Collect all four property chests and bring at least eight of the ten households alive to the refuge yard.",
        "es-ES": "Recoge los cuatro arcones de bienes y lleva con vida al menos ocho de los diez hogares al patio de refugio."
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

### Eastern provision trader / Comerciante oriental de provisiones

EN: Escort the trader of eastern provision trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de comerciante oriental de provisiones hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A voluntary bounded trade does not buy impunity from Nero.

ES: Un intercambio voluntario limitado no compra impunidad ante Nerón.

```json
{
  "id": "side-6",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "15-evacuation-and-recovery-rome-ostia.side-6.entity-1"
        ],
        "destinations": {
          "15-evacuation-and-recovery-rome-ostia.side-6.entity-1": "15-evacuation-and-recovery-rome-ostia.side-6.zone-1"
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
        "receipt": "15-evacuation-and-recovery-rome-ostia.side-6.payment",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-6.entity-1",
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
        "id": "15-evacuation-and-recovery-rome-ostia.side-6.zone-1",
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
      "onceFlag": "15-evacuation-and-recovery-rome-ostia.side-6.rewarded",
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
      "id": "immediate-care",
      "optionalObjectives": [
        "side-1",
        "side-2"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Optional civilian help can run with main household staging; two losses tolerated only among ten declared main households."
    },
    {
      "id": "surveyed-departure",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Prioritize land-route information and records; never infer historical guilt from fictional hazard placement."
    },
    {
      "id": "finite-recovery",
      "optionalObjectives": [
        "side-4",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Invest in bounded stores/trade while reserving300food/80wood main provisioning; no free resurrection."
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
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      30,
      55
    ],
    "difficultyLevers": "12 workers; all pickup sites and receiving posts marked; open work order and detour choice.",
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
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      35,
      65
    ],
    "difficultyLevers": "9 workers; parallel work and local fog; essential receivers/costs always shown.",
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
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      40,
      75
    ],
    "difficultyLevers": "6 workers; lower start stock; organize parallel gathering and deliveries. No concealed requirements, unlimited enemies or changes to native health/movement.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.title / always | none | Ash over the Seven Hills | Ceniza sobre las siete colinas |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.fact-intro / intro first | collection-narrator | Tacitus reports that after Rome’s fire in 64 Nero punished people called Christians. He wrote decades later and did not establish that Christians caused the fire. The local civilian evacuation here is a fictional reconstruction, not a separately documented event. | Tácito relata que tras el incendio de Roma en 64 Nerón castigó a personas llamadas cristianas. Escribió décadas después y no demostró que los cristianos causaran el incendio. La evacuación civil local es una reconstrucción ficticia, no un hecho documentado por separado. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.persona-intro / after handover | miriam-archive | I have smelled scorched parchment in my own lifetime. That memory is mine; the fire in these accounts is not. I can bring grief to the telling without claiming another century as my experience. | He olido pergamino quemado en mi propia vida. Ese recuerdo es mío; el incendio de estos relatos no lo es. Puedo aportar dolor al relato sin apropiarme de otro siglo como experiencia. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.route-help / available from start; repeatable without effect | none | Keep to the disclosed eastern land route. The households and fire-related obstacles are a reconstruction; they do not identify who caused the fire. No required route crosses the Tiber. | Sigue la ruta terrestre oriental indicada. Los hogares y obstáculos relacionados con el fuego son una reconstrucción; no identifican quién causó el incendio. Ninguna ruta necesaria cruza el Tíber. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.o1-goal / phase-1 active | none | Collect all four property chests and bring at least eight of the ten households alive to the refuge yard. | Recoge los cuatro arcones de bienes y lleva con vida al menos ocho de los diez hogares al patio de refugio. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.o1-receipt / o1 latched once | none | Four chests collected and at least eight original household identities sheltered. | Cuatro arcones recogidos y al menos ocho identidades originales de hogares refugiadas. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.o1-reaction / after o1 receipt | miriam-archive | The household names are ours to invent; the victims in the source are not ours to erase. | Podemos inventar los nombres de estos hogares; no podemos borrar las víctimas de la fuente. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.o2-goal / phase-2 active | none | Take the four chests to the refuge, pay 300 food and 80 wood once, and derive two fictional departure notes from the collected chests. | Lleva los cuatro arcones al refugio, paga una sola vez 300 de alimento y 80 de madera y elabora dos notas ficticias de salida a partir de los arcones recogidos. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.o2-receipt / o2 latched once | none | Four property arrivals, one provisioning debit and two derived notes recorded. | Cuatro llegadas de bienes, un cobro de provisiones y dos notas derivadas registrados. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.o2-reaction / after o2 receipt | miriam-archive | Food for departure is concrete; a promise to restore everything is not. | El alimento para salir es concreto; la promesa de restaurarlo todo no. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.o3-goal / phase-3 active | none | Bring at least eight of the same sheltered households, all four chests and both notes to the eastern land departure court. | Lleva al menos ocho de los mismos hogares refugiados, los cuatro arcones y ambas notas al patio terrestre de salida oriental. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.o3-receipt / o3 latched once | none | The same eight-or-more sheltered identities and all required property/notes arrived. | Han llegado las mismas ocho o más identidades refugiadas y todos los bienes y notas requeridos. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.o3-reaction / after o3 receipt | miriam-archive | A local escape is the most this fiction can promise. It cannot rewrite the account. | Una salida local es cuanto puede prometer esta ficción. No puede reescribir el relato. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-1-goal / optional list from start | none | Bring both voluntary evacuee groups from separate displaced families to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de familias desplazadas separadas al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-1-complete / side-1 completed | none | Separate displaced families completed. Its stated benefit has been granted once. | Familias desplazadas separadas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-1-lost / side-1 failed-optional | none | Separate displaced families is unavailable after the loss of its unique participant or object. The main mission continues. | Familias desplazadas separadas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at independent refuge households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes del refugio. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-2-complete / side-2 completed | none | Independent refuge households completed. Its stated benefit has been granted once. | Hogares independientes del refugio: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-2-lost / side-2 failed-optional | none | Independent refuge households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares independientes del refugio: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-3-goal / optional list from start | none | Escort the local guide of eastern land guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía terrestre oriental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-3-complete / side-3 completed | none | Eastern land guide completed. Its stated benefit has been granted once. | Guía terrestre oriental: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-3-lost / side-3 failed-optional | none | Eastern land guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía terrestre oriental: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of unburned roadside store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén del camino sin quemar. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-4-complete / side-4 completed | none | Unburned roadside store completed. Its stated benefit has been granted once. | Almacén del camino sin quemar: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-4-lost / side-4 failed-optional | none | Unburned roadside store is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén del camino sin quemar: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-5-goal / optional list from start | none | Recover both separate copies from independent property notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de notas independientes de pertenencias y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-5-complete / side-5 completed | none | Independent property notes completed. Its stated benefit has been granted once. | Notas independientes de pertenencias: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-5-lost / side-5 failed-optional | none | Independent property notes is unavailable after the loss of its unique participant or object. The main mission continues. | Notas independientes de pertenencias: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-6-goal / optional list from start | none | Escort the trader of eastern provision trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de comerciante oriental de provisiones hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-6-complete / side-6 completed | none | Eastern provision trader completed. Its stated benefit has been granted once. | Comerciante oriental de provisiones: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.side-6-lost / side-6 failed-optional | none | Eastern provision trader is unavailable after the loss of its unique participant or object. The main mission continues. | Comerciante oriental de provisiones: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.fact-outro / victory first | collection-narrator | Fictional households and property have reached the local departure district. This does not reverse the deaths Tacitus reports, identify every punishment site or make a Roman episode into an empire-wide policy. | Los hogares y bienes ficticios han alcanzado el barrio local de salida. Esto no revierte las muertes relatadas por Tácito, identifica todos los lugares de castigo ni transforma un episodio romano en una política de todo el imperio. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.persona-outro / after fact-outro | miriam-archive | Our saved bundles do not cancel the people absent from the account. I leave a silence for them, and do not fill it with a triumph they never witnessed. | Los bultos salvados no borran a las personas ausentes del relato. Dejo un silencio para ellas y no lo lleno con un triunfo que nunca presenciaron. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.next-episode / after persona-outro | none | Continue with A Story in the Shadow of War. This episode does not complete the campaign. | Continúa con Un relato a la sombra de la guerra. Este episodio no termina la campaña. |
| scenario.faith-origins.15-evacuation-and-recovery-rome-ostia.odyssey.act-turning-point / after next-episode | collection-narrator | The next act follows the destruction of Jerusalem and later community survival. Tacitus’ Roman account must not be turned into an explanation of every later conflict. | El siguiente acto sigue la destrucción de Jerusalén y la supervivencia posterior de comunidades. El relato romano de Tácito no debe convertirse en explicación de todos los conflictos posteriores. |

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
    },
    {
      "id": "finite-environmental-hazards",
      "status": "required design contract; reference/native implementation pending; no decorative fire counted as functional hazard"
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
      "same eight actual sheltered households required at exit",
      "three surviving households plus duplicatedIDs cannot meet eight",
      "optionalfamilies cannot replace main household losses",
      "both disclosed corridors never sealed by hazard sequence",
      "hazards finite and nativeobserved, no actorassignedas historical arsonist",
      "no Christian arson claim or empirewide64 policy in neutral voice",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
