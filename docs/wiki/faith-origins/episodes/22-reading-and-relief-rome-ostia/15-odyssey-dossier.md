# 22. Bread Read Aloud

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `22-reading-and-relief-rome-ostia` · c. 150–160 CE · 400×400

## Historical frame and fixed outcome

EN: Justin’s First Apology describes Sunday readings, instruction, prayer, shared rites and voluntary giving for people in need, including those absent. It is an apologetic account of Christian practice, not a survey of all communities. The local Roman households, reading-work notes and aid posts here are fictional.

ES: La Primera Apología de Justino describe lecturas dominicales, enseñanza, oración, ritos compartidos y aportaciones voluntarias para personas necesitadas, incluidas las ausentes. Es un relato apologético de prácticas cristianas, no un estudio de todas las comunidades. Los hogares romanos, notas de trabajo de lectura y puestos de ayuda de este escenario son ficticios.

EN: Three fictional aid circuits have completed their paid distributions and returned local registers. This does not certify a historical congregation, universal welfare system or the truth of Justin’s theological arguments. His description remains the attributed source for the scene’s broad theme.

ES: Tres circuitos ficticios de ayuda completaron sus distribuciones pagadas y devolvieron registros locales. Esto no acredita una congregación histórica, un sistema universal de auxilio ni la verdad de los argumentos teológicos de Justino. Su descripción sigue siendo la fuente atribuida de la temática general.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 15,
      "episodeId": "22-reading-and-relief-rome-ostia",
      "order": 22,
      "selectedSourceUrl": "https://www.newadvent.org/fathers/0126.htm",
      "consultedUrl": "https://www.newadvent.org/fathers/0126.htm",
      "passage": "Justin, First Apology 65–67, especially 67: Sunday assembly, apostolic memoirs/prophets read, instruction, prayer, bread/wine, collection for those in need.",
      "supportedClaim": {
        "en": "Justin describes Sunday gatherings, readings, prayer, Eucharist, and collections for people in need.",
        "es-ES": "Justino describe reuniones dominicales, lecturas, oración, eucaristía y colectas para personas necesitadas."
      },
      "limitations": "The passage describes Christian practice in general terms; it does not itself establish Justin's teaching location or prove these exact practices were unique to Rome. Apologetic self-description, not a neutral census.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/0126.htm",
      "passage": "Justin, First Apology65–67; architect read rites, reading and giving descriptions",
      "limitations": "Apologetic self-description, not a universal census or precise Roman congregation address. Ordinary local reading-work notes and household logistics are fictional, theological assertions not objective facts or mechanical meters.",
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

EN: Collect four distinct ordinary reading-work notes and bring them to the central reading court.

ES: Recoge cuatro notas ordinarias distintas de trabajo de lectura y llévalas al patio central.

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
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-1",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-2",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-3",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-4"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-1",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-2",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-3",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-4"
      ],
      "destinations": {
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-1": "faith-origins.22-reading-and-relief-rome-ostia.destination-1",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-2": "faith-origins.22-reading-and-relief-rome-ostia.destination-1",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-3": "faith-origins.22-reading-and-relief-rome-ostia.destination-1",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-4": "faith-origins.22-reading-and-relief-rome-ostia.destination-1"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Four original local work notes reached the reading court; no canonical original was placed.

ES: Cuatro notas locales originales de trabajo han llegado al patio de lectura; no se ha colocado un original canónico.

EN: The notes are our working fiction, not Justin’s own pages.

ES: Las notas son nuestra ficción de trabajo, no las páginas del propio Justino.

### o2 / phase-2

EN: Deliver two assigned households alive to each relief post; pay 120 food at each of the northern, southern and eastern posts, 360 food in total.

ES: Lleva con vida dos hogares asignados a cada puesto de ayuda; paga 120 de alimento en cada puesto norte, sur y este: 360 en total.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "state": "arrived",
      "requiredCount": 6,
      "id": "req-1",
      "entities": [
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-1",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-2",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-3",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-4",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-5",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-6"
      ],
      "destinations": {
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-1": "faith-origins.22-reading-and-relief-rome-ostia.destination-2",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-2": "faith-origins.22-reading-and-relief-rome-ostia.destination-2",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-3": "faith-origins.22-reading-and-relief-rome-ostia.destination-3",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-4": "faith-origins.22-reading-and-relief-rome-ostia.destination-3",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-5": "faith-origins.22-reading-and-relief-rome-ostia.destination-4",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-6": "faith-origins.22-reading-and-relief-rome-ostia.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 360
      },
      "id": "req-2",
      "receivingZones": [
        "faith-origins.22-reading-and-relief-rome-ostia.destination-2",
        "faith-origins.22-reading-and-relief-rome-ostia.destination-3",
        "faith-origins.22-reading-and-relief-rome-ostia.destination-4"
      ],
      "allocations": {
        "faith-origins.22-reading-and-relief-rome-ostia.destination-2": {
          "food": 120
        },
        "faith-origins.22-reading-and-relief-rome-ostia.destination-3": {
          "food": 120
        },
        "faith-origins.22-reading-and-relief-rome-ostia.destination-4": {
          "food": 120
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.22-reading-and-relief-rome-ostia.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Six distinct original households and three exact paid allocations are recorded at their assigned posts.

ES: Se registran seis hogares originales distintos y tres pagos exactos en sus puestos asignados.

EN: The total is not enough. The northern count cannot feed a missing southern household.

ES: La suma no basta. El recuento norte no alimenta a un hogar meridional ausente.

### o3 / phase-3

EN: After the three-post aid receipt, prepare one local register for each post and return all three original register identities to the central court.

ES: Tras el recibo de ayuda de los tres puestos, prepara un registro local por puesto y devuelve las tres identidades originales al patio central.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-1",
      "inputEntities": [
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-1",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-2",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-3",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-4"
      ],
      "outputEntities": [
        "faith-origins.22-reading-and-relief-rome-ostia.north-aid-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.22-reading-and-relief-rome-ostia.o2.req-2.paid",
          "fromObjective": "o2",
          "amounts": {
            "food": 360
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-1",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-2",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-3",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-4"
      ],
      "outputEntities": [
        "faith-origins.22-reading-and-relief-rome-ostia.south-aid-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.22-reading-and-relief-rome-ostia.o2.req-2.paid",
          "fromObjective": "o2",
          "amounts": {
            "food": 360
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-3",
      "inputEntities": [
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-1",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-2",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-3",
        "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-4"
      ],
      "outputEntities": [
        "faith-origins.22-reading-and-relief-rome-ostia.east-aid-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.22-reading-and-relief-rome-ostia.o2.req-2.paid",
          "fromObjective": "o2",
          "amounts": {
            "food": 360
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "faith-origins.22-reading-and-relief-rome-ostia.north-aid-register-1"
      ],
      "destinations": {
        "faith-origins.22-reading-and-relief-rome-ostia.north-aid-register-1": "faith-origins.22-reading-and-relief-rome-ostia.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-5",
      "entities": [
        "faith-origins.22-reading-and-relief-rome-ostia.south-aid-register-1"
      ],
      "destinations": {
        "faith-origins.22-reading-and-relief-rome-ostia.south-aid-register-1": "faith-origins.22-reading-and-relief-rome-ostia.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-6",
      "entities": [
        "faith-origins.22-reading-and-relief-rome-ostia.east-aid-register-1"
      ],
      "destinations": {
        "faith-origins.22-reading-and-relief-rome-ostia.east-aid-register-1": "faith-origins.22-reading-and-relief-rome-ostia.destination-1"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The three separate local aid registers returned after their paid, identity-matched deliveries.

ES: Los tres registros locales separados de ayuda han vuelto tras sus entregas pagadas e identificadas.

EN: I can check the three registers. I will not weigh the faith of the six people behind them.

ES: Puedo comprobar los tres registros. No pesaré la fe de las seis personas que hay tras ellos.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/22-reading-and-relief-rome-ostia.svg)

```json
{
  "bbox": [
    12.48,
    41.87,
    12.555,
    41.93
  ],
  "terrainProfile": "rome-ostia",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        206.13,
        193.56
      ],
      "lonLat": [
        12.519,
        41.901
      ],
      "name": {
        "en": "Central reading and accounting court",
        "es-ES": "Patio central de lectura y cuentas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        170.77,
        74.81
      ],
      "lonLat": [
        12.511,
        41.921
      ],
      "name": {
        "en": "Northern relief post",
        "es-ES": "Puesto septentrional de ayuda"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        153.1,
        324.19
      ],
      "lonLat": [
        12.507,
        41.879
      ],
      "name": {
        "en": "Southern relief post",
        "es-ES": "Puesto meridional de ayuda"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        334.29,
        181.69
      ],
      "lonLat": [
        12.548,
        41.903
      ],
      "name": {
        "en": "Eastern relief post",
        "es-ES": "Puesto oriental de ayuda"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-relief",
      "hubOrder": [
        "hub-1",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "south-relief",
      "hubOrder": [
        "hub-1",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-relief",
      "hubOrder": [
        "hub-1",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
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
      "routePolicy": "independent outer collection/aid circuit, east of Tiber"
    }
  ],
  "terrainInstructions": "Local Rome scene east of the Tiber. North/south collection and eastern inland departure remain on land; Other regions are off-map, no miracle arrival or coast-to-Greece ground route. No later basilica, Vatican court, medieval bound Bible or exact named church location. Ordinary fictional workshops and household courts; terrain, dated streets and receiving footprints pending. Do not treat modern shore controls as Roman harbor geometry.",
  "corridorStraightLengthsTiles": {
    "north-relief": 123.9,
    "south-relief": 140.98,
    "east-relief": 128.71,
    "relief": 425.86
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
  "asset": "docs/design/maps/faith-origins/odyssey/22-reading-and-relief-rome-ostia.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-1",
      "role": "fictional-local-reading-work-note",
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
      "id": "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-2",
      "role": "fictional-local-reading-work-note",
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
      "id": "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-3",
      "role": "fictional-local-reading-work-note",
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
    },
    {
      "id": "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-4",
      "role": "fictional-local-reading-work-note",
      "initialHub": "hub-2",
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
      "id": "faith-origins.22-reading-and-relief-rome-ostia.relief-households-1",
      "role": "fictional-voluntary-relief-household",
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
      "id": "faith-origins.22-reading-and-relief-rome-ostia.relief-households-2",
      "role": "fictional-voluntary-relief-household",
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
      "id": "faith-origins.22-reading-and-relief-rome-ostia.relief-households-3",
      "role": "fictional-voluntary-relief-household",
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
      "id": "faith-origins.22-reading-and-relief-rome-ostia.relief-households-4",
      "role": "fictional-voluntary-relief-household",
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
      "id": "faith-origins.22-reading-and-relief-rome-ostia.relief-households-5",
      "role": "fictional-voluntary-relief-household",
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
      "id": "faith-origins.22-reading-and-relief-rome-ostia.relief-households-6",
      "role": "fictional-voluntary-relief-household",
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
      "id": "faith-origins.22-reading-and-relief-rome-ostia.north-aid-register-1",
      "role": "fictional-local-aid-register",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.22-reading-and-relief-rome-ostia.south-aid-register-1",
      "role": "fictional-local-aid-register",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.22-reading-and-relief-rome-ostia.east-aid-register-1",
      "role": "fictional-local-aid-register",
      "initialHub": "hub-4",
      "offsetTiles": [
        -10,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.22-reading-and-relief-rome-ostia.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.22-reading-and-relief-rome-ostia.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.22-reading-and-relief-rome-ostia.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.22-reading-and-relief-rome-ostia.destination-4",
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
    "reading-work-notes": [
      "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-1",
      "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-2",
      "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-3",
      "faith-origins.22-reading-and-relief-rome-ostia.reading-work-notes-4"
    ],
    "relief-households": [
      "faith-origins.22-reading-and-relief-rome-ostia.relief-households-1",
      "faith-origins.22-reading-and-relief-rome-ostia.relief-households-2",
      "faith-origins.22-reading-and-relief-rome-ostia.relief-households-3",
      "faith-origins.22-reading-and-relief-rome-ostia.relief-households-4",
      "faith-origins.22-reading-and-relief-rome-ostia.relief-households-5",
      "faith-origins.22-reading-and-relief-rome-ostia.relief-households-6"
    ],
    "north-aid-register": [
      "faith-origins.22-reading-and-relief-rome-ostia.north-aid-register-1"
    ],
    "south-aid-register": [
      "faith-origins.22-reading-and-relief-rome-ostia.south-aid-register-1"
    ],
    "east-aid-register": [
      "faith-origins.22-reading-and-relief-rome-ostia.east-aid-register-1"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-1",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-2",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-3",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-4",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-5",
        "faith-origins.22-reading-and-relief-rome-ostia.relief-households-6"
      ],
      "minimumAliveOrAlreadySafe": 6
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Independent neighbors’ provisions / Provisiones de vecinos independientes

EN: Bring each of the two aid crates to its assigned household at independent neighbors’ provisions. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en provisiones de vecinos independientes. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Two optional household deliveries remain separate from the six mandatory recipients.

ES: Dos entregas opcionales a hogares permanecen separadas de los seis receptores obligatorios.

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
          "22-reading-and-relief-rome-ostia.side-1.entity-1",
          "22-reading-and-relief-rome-ostia.side-1.entity-2"
        ],
        "destinations": {
          "22-reading-and-relief-rome-ostia.side-1.entity-1": "22-reading-and-relief-rome-ostia.side-1.zone-1",
          "22-reading-and-relief-rome-ostia.side-1.entity-2": "22-reading-and-relief-rome-ostia.side-1.zone-2"
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
        "id": "22-reading-and-relief-rome-ostia.side-1.entity-1",
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
        "id": "22-reading-and-relief-rome-ostia.side-1.entity-2",
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
        "id": "22-reading-and-relief-rome-ostia.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "22-reading-and-relief-rome-ostia.side-1.zone-2",
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
      "onceFlag": "22-reading-and-relief-rome-ostia.side-1.rewarded",
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
      "north-relief",
      "south-relief",
      "east-relief",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Reading-context annotations / Anotaciones de contexto de lectura

EN: Recover both separate copies from reading-context annotations and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de anotaciones de contexto de lectura y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Fictional work annotations unlock source context, not an authentic text or a faith meter.

ES: Anotaciones de trabajo ficticias desbloquean contexto, no un texto auténtico ni un medidor de fe.

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
          "22-reading-and-relief-rome-ostia.side-2.entity-1",
          "22-reading-and-relief-rome-ostia.side-2.entity-2"
        ],
        "destinations": {
          "22-reading-and-relief-rome-ostia.side-2.entity-1": "22-reading-and-relief-rome-ostia.side-2.zone-1",
          "22-reading-and-relief-rome-ostia.side-2.entity-2": "22-reading-and-relief-rome-ostia.side-2.zone-1"
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
        "id": "22-reading-and-relief-rome-ostia.side-2.entity-1",
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
        "id": "22-reading-and-relief-rome-ostia.side-2.entity-2",
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
        "id": "22-reading-and-relief-rome-ostia.side-2.zone-1",
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
      "onceFlag": "22-reading-and-relief-rome-ostia.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.22-reading-and-relief-rome-ostia"
      ],
      "historicalNote": {
        "en": "Justin’s First Apology describes Sunday readings, instruction, prayer, shared rites and voluntary giving for people in need, including those absent. It is an apologetic account of Christian practice, not a survey of all communities. The local Roman households, reading-work notes and aid posts here are fictional.",
        "es-ES": "La Primera Apología de Justino describe lecturas dominicales, enseñanza, oración, ritos compartidos y aportaciones voluntarias para personas necesitadas, incluidas las ausentes. Es un relato apologético de prácticas cristianas, no un estudio de todas las comunidades. Los hogares romanos, notas de trabajo de lectura y puestos de ayuda de este escenario son ficticios."
      },
      "hint": {
        "en": "Collect four distinct ordinary reading-work notes and bring them to the central reading court.",
        "es-ES": "Recoge cuatro notas ordinarias distintas de trabajo de lectura y llévalas al patio central."
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
      "north-relief",
      "south-relief",
      "east-relief",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A separate supply workshop / Un taller separado de suministros

EN: Pay 50 wood and restore the damaged store of a separate supply workshop to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de un taller separado de suministros. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair finite ordinary craft storage without unlocking an unproved church building.

ES: Repara un almacén artesanal ordinario finito sin desbloquear un edificio eclesial no acreditado.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "22-reading-and-relief-rome-ostia.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "22-reading-and-relief-rome-ostia.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "22-reading-and-relief-rome-ostia.side-3.payment",
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
        "id": "22-reading-and-relief-rome-ostia.side-3.entity-1",
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
        "id": "22-reading-and-relief-rome-ostia.side-3.zone-1",
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
      "onceFlag": "22-reading-and-relief-rome-ostia.side-3.rewarded",
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
      "north-relief",
      "south-relief",
      "east-relief",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### An independent grain share / Una parte independiente de grano

EN: Escort the trader of an independent grain share to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de una parte independiente de grano hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Bounded supply investment never pays the main360food receipt twice.

ES: Una inversión limitada en suministros nunca paga dos veces el recibo principal de360alimento.

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
          "22-reading-and-relief-rome-ostia.side-4.entity-1"
        ],
        "destinations": {
          "22-reading-and-relief-rome-ostia.side-4.entity-1": "22-reading-and-relief-rome-ostia.side-4.zone-1"
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
        "receipt": "22-reading-and-relief-rome-ostia.side-4.payment",
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
        "id": "22-reading-and-relief-rome-ostia.side-4.entity-1",
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
        "id": "22-reading-and-relief-rome-ostia.side-4.zone-1",
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
      "onceFlag": "22-reading-and-relief-rome-ostia.side-4.rewarded",
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
      "north-relief",
      "south-relief",
      "east-relief",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Outer aid-road viewpoints / Miradores de los caminos exteriores de ayuda

EN: Scout both marked viewpoints of outer aid-road viewpoints. Benefit: Mark the surveyed relief land circuit once; main receiver markers and requirements remain available without it.

ES: Explora los dos miradores señalados de miradores de los caminos exteriores de ayuda. Ventaja: Señala una vez el circuito terrestre trazado relief; los receptores principales y sus requisitos siguen disponibles sin él.

EN: Survey a real outer land circuit and keep all three receiver posts individually marked.

ES: Reconoce un circuito exterior terrestre real y mantén señalados por separado los tres receptores.

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
          "22-reading-and-relief-rome-ostia.side-5.zone-1",
          "22-reading-and-relief-rome-ostia.side-5.zone-2"
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
        "id": "22-reading-and-relief-rome-ostia.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "22-reading-and-relief-rome-ostia.side-5.zone-2",
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
      "onceFlag": "22-reading-and-relief-rome-ostia.side-5.rewarded",
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
    "originHub": "hub-3",
    "receivingHub": "hub-2",
    "corridorIds": [
      "north-relief",
      "south-relief",
      "east-relief",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Eastern relief-road guide / Guía del camino oriental de ayuda

EN: Escort the local guide of eastern relief-road guide to the marked road junction. Benefit: Mark the surveyed east-relief land circuit once; main receiver markers and requirements remain available without it.

ES: Escolta al guía local de guía del camino oriental de ayuda hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado east-relief; los receptores principales y sus requisitos siguen disponibles sin él.

EN: Shows eastern access; cannot let one post count as three.

ES: Muestra el acceso oriental; no permite contar un puesto como tres.

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
          "22-reading-and-relief-rome-ostia.side-6.entity-1"
        ],
        "destinations": {
          "22-reading-and-relief-rome-ostia.side-6.entity-1": "22-reading-and-relief-rome-ostia.side-6.zone-1"
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
        "id": "22-reading-and-relief-rome-ostia.side-6.entity-1",
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
        "id": "22-reading-and-relief-rome-ostia.side-6.zone-1",
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
      "target": "east-relief surveyed land circuit",
      "resources": {},
      "onceFlag": "22-reading-and-relief-rome-ostia.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "east-relief"
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
      "north-relief",
      "south-relief",
      "east-relief",
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
      "food": 450,
      "wood": 200,
      "gold": 0,
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
      "id": "three-courier-relief",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Invest separate finite supplies and allocate teams across three sites; keep360foodmain reserved.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "reading-and-route-context",
      "optionalObjectives": [
        "side-2",
        "side-5"
      ],
      "costOfOpportunity": "Read qualified source context, then survey outer access while three independent relief pairs travel.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "community-and-east-circuit",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Help separate neighbors and guide the eastern branch; never replace mandatory identities with optional ones.",
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
      "food": 1478,
      "wood": 708,
      "gold": 204,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 360,
      "wood": 0,
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
      "food": 1430,
      "wood": 680,
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
      "food": 1530,
      "wood": 730,
      "gold": 215,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 360,
      "wood": 0,
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
      "food": 1430,
      "wood": 680,
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
      "food": 1583,
      "wood": 753,
      "gold": 227,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 360,
      "wood": 0,
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
      "food": 1430,
      "wood": 680,
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
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.title / always | none | Bread Read Aloud | Pan leído en voz alta |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.fact-intro / intro first | collection-narrator | Justin’s First Apology describes Sunday readings, instruction, prayer, shared rites and voluntary giving for people in need, including those absent. It is an apologetic account of Christian practice, not a survey of all communities. The local Roman households, reading-work notes and aid posts here are fictional. | La Primera Apología de Justino describe lecturas dominicales, enseñanza, oración, ritos compartidos y aportaciones voluntarias para personas necesitadas, incluidas las ausentes. Es un relato apologético de prácticas cristianas, no un estudio de todas las comunidades. Los hogares romanos, notas de trabajo de lectura y puestos de ayuda de este escenario son ficticios. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.persona-intro / after handover | miriam-archive | A page was easier for me to notice than an absent neighbor. That is a failing I learned to recognize in my own work. Reading Justin’s account, I want to attend to both the voice in the room and those whose chairs are empty. | Me resultaba más fácil fijarme en una página que en un vecino ausente. Aprendí a reconocer ese fallo en mi propio trabajo. Al leer el relato de Justino quiero atender tanto a la voz de la sala como a quienes dejan sus sillas vacías. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.route-help / available from start; repeatable without effect | none | Bring the four ordinary reading-work notes to the central court. Help two assigned households at each of three separate posts and pay 120 food at each. Only after that receipt, prepare the three local aid registers and return all three original register identities to the central court. | Lleva las cuatro notas ordinarias de trabajo de lectura al patio central. Ayuda a dos hogares asignados en cada uno de los tres puestos separados y paga 120 de alimento en cada uno. Solo tras ese recibo prepara los tres registros locales de ayuda y devuelve las tres identidades originales al patio central. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.o1-goal / phase-1 active | none | Collect four distinct ordinary reading-work notes and bring them to the central reading court. | Recoge cuatro notas ordinarias distintas de trabajo de lectura y llévalas al patio central. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.o1-receipt / o1 latched once | none | Four original local work notes reached the reading court; no canonical original was placed. | Cuatro notas locales originales de trabajo han llegado al patio de lectura; no se ha colocado un original canónico. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.o1-reaction / after o1 receipt | miriam-archive | The notes are our working fiction, not Justin’s own pages. | Las notas son nuestra ficción de trabajo, no las páginas del propio Justino. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.o2-goal / phase-2 active | none | Deliver two assigned households alive to each relief post; pay 120 food at each of the northern, southern and eastern posts, 360 food in total. | Lleva con vida dos hogares asignados a cada puesto de ayuda; paga 120 de alimento en cada puesto norte, sur y este: 360 en total. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.o2-receipt / o2 latched once | none | Six distinct original households and three exact paid allocations are recorded at their assigned posts. | Se registran seis hogares originales distintos y tres pagos exactos en sus puestos asignados. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.o2-reaction / after o2 receipt | miriam-archive | The total is not enough. The northern count cannot feed a missing southern household. | La suma no basta. El recuento norte no alimenta a un hogar meridional ausente. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.o3-goal / phase-3 active | none | After the three-post aid receipt, prepare one local register for each post and return all three original register identities to the central court. | Tras el recibo de ayuda de los tres puestos, prepara un registro local por puesto y devuelve las tres identidades originales al patio central. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.o3-receipt / o3 latched once | none | The three separate local aid registers returned after their paid, identity-matched deliveries. | Los tres registros locales separados de ayuda han vuelto tras sus entregas pagadas e identificadas. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.o3-reaction / after o3 receipt | miriam-archive | I can check the three registers. I will not weigh the faith of the six people behind them. | Puedo comprobar los tres registros. No pesaré la fe de las seis personas que hay tras ellos. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at independent neighbors’ provisions. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en provisiones de vecinos independientes. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-1-complete / side-1 completed | none | Independent neighbors’ provisions completed. Its stated benefit has been granted once. | Provisiones de vecinos independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-1-lost / side-1 failed-optional | none | Independent neighbors’ provisions is unavailable after the loss of its unique participant or object. The main mission continues. | Provisiones de vecinos independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from reading-context annotations and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de anotaciones de contexto de lectura y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-2-complete / side-2 completed | none | Reading-context annotations completed. Its stated benefit has been granted once. | Anotaciones de contexto de lectura: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-2-lost / side-2 failed-optional | none | Reading-context annotations is unavailable after the loss of its unique participant or object. The main mission continues. | Anotaciones de contexto de lectura: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of a separate supply workshop to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de un taller separado de suministros. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-3-complete / side-3 completed | none | A separate supply workshop completed. Its stated benefit has been granted once. | Un taller separado de suministros: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-3-lost / side-3 failed-optional | none | A separate supply workshop is unavailable after the loss of its unique participant or object. The main mission continues. | Un taller separado de suministros: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-4-goal / optional list from start | none | Escort the trader of an independent grain share to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de una parte independiente de grano hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-4-complete / side-4 completed | none | An independent grain share completed. Its stated benefit has been granted once. | Una parte independiente de grano: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-4-lost / side-4 failed-optional | none | An independent grain share is unavailable after the loss of its unique participant or object. The main mission continues. | Una parte independiente de grano: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of outer aid-road viewpoints. Benefit: Mark the surveyed relief land circuit once; main receiver markers and requirements remain available without it. | Explora los dos miradores señalados de miradores de los caminos exteriores de ayuda. Ventaja: Señala una vez el circuito terrestre trazado relief; los receptores principales y sus requisitos siguen disponibles sin él. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-5-complete / side-5 completed | none | Outer aid-road viewpoints completed. Its stated benefit has been granted once. | Miradores de los caminos exteriores de ayuda: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-5-lost / side-5 failed-optional | none | Outer aid-road viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores de los caminos exteriores de ayuda: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-6-goal / optional list from start | none | Escort the local guide of eastern relief-road guide to the marked road junction. Benefit: Mark the surveyed east-relief land circuit once; main receiver markers and requirements remain available without it. | Escolta al guía local de guía del camino oriental de ayuda hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado east-relief; los receptores principales y sus requisitos siguen disponibles sin él. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-6-complete / side-6 completed | none | Eastern relief-road guide completed. Its stated benefit has been granted once. | Guía del camino oriental de ayuda: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.side-6-lost / side-6 failed-optional | none | Eastern relief-road guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del camino oriental de ayuda: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.fact-outro / victory first | collection-narrator | Three fictional aid circuits have completed their paid distributions and returned local registers. This does not certify a historical congregation, universal welfare system or the truth of Justin’s theological arguments. His description remains the attributed source for the scene’s broad theme. | Tres circuitos ficticios de ayuda completaron sus distribuciones pagadas y devolvieron registros locales. Esto no acredita una congregación histórica, un sistema universal de auxilio ni la verdad de los argumentos teológicos de Justino. Su descripción sigue siendo la fuente atribuida de la temática general. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.persona-outro / after fact-outro | miriam-archive | The register tells me whom our imagined work reached. It cannot measure devotion. I put down the pen when I catch myself confusing those two things. | El registro me dice a quién llegó nuestro trabajo imaginado. No mide la devoción. Dejo la pluma cuando me sorprendo confundiendo ambas cosas. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.22-reading-and-relief-rome-ostia.odyssey.next-episode / after persona-outro | none | Continue with A Petition from Sardes. This episode does not complete the campaign. | Continúa con Una petición desde Sardes. Este episodio no termina la campaña. |

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
      "two northern households cannot substitute for two southern or eastern identities",
      "360foodatonepost cannot substitute three120foodallocations",
      "one local register cannot count as allthree",
      "register creation requires completed o2 receipt and exact360fooddebit, never aseconddebit",
      "same six main household identities; independent optional ones cannot replace",
      "no mandatory rite or miracle proof gameplay",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
