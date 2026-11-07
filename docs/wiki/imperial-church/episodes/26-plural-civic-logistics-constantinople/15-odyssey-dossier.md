# 26. Altars of a New Reign

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `26-plural-civic-logistics-constantinople` · December 361–early 362 CE; policy sequence, no fixed local reopening day · 400×400

## Historical frame and fixed outcome

EN: After Constantius’ death, Julian entered Constantinople in December 361. Ammianus later describes decrees reopening temples and restoring sacrifice. Orders are evidence of policy, not proof that every site reopened or every resident changed belief. This fictional civic network serves ordinary local work courts without assigning religious identity to the people receiving supplies. No goal chooses, reverses or enforces an imperial creed.

ES: Tras la muerte de Constancio, Juliano entró en Constantinopla en diciembre de 361. Amiano describe después decretos que reabren templos y restablecen sacrificios. Las órdenes prueban una política, no que todos los lugares abrieran ni que todos los habitantes cambiaran de creencia. Esta red cívica ficticia atiende patios locales de trabajo cotidiano sin asignar identidad religiosa a quienes reciben provisiones. Ningún objetivo elige, revoca ni impone un credo imperial.

EN: Three fictional work courts recorded their own helpers, supply allocations and local notes. These deliveries do not establish present residence, a temple’s location or religious compliance. Julian’s policy remains part of the historical account; local outcomes cannot measure everyone’s response. The next episode follows received accounts of Athanasius’ return and renewed expulsion at Alexandria, with the Persian campaign kept off-map.

ES: Tres patios ficticios de trabajo registraron sus propios ayudantes, asignaciones de suministros y notas locales. Las entregas no prueban permanencia actual, la ubicación de un templo ni cumplimiento religioso. La política de Juliano sigue en el relato histórico; los resultados locales no miden la respuesta de todos. El próximo episodio sigue relatos recibidos del regreso y nueva expulsión de Atanasio en Alejandría, con la campaña persa fuera del mapa.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "Ammianus describes Julian entering Constantinople after Constantius’ death and later ordering temples opened and sacrifice restored. His explanation of the emperor’s motives is authorial interpretation; the decree does not establish uniform implementation or belief.",
        "es-ES": "Amiano describe la entrada de Juliano en Constantinopla tras la muerte de Constancio y su posterior orden de abrir templos y restablecer sacrificios. Su explicación de los motivos imperiales es interpretación del autor; el decreto no demuestra aplicación ni creencia uniformes."
      },
      "architectCorrection": {
        "date": "2026-10-15",
        "author": "gpt-6",
        "approval": "independent review pending",
        "reason": "XXII.2 supports accession/entry; XXII.5.2 supports temple and sacrifice policy. Broadened working date to December361–early362 rather than assert one reopening day. Ammianus admires Julian but also criticizes him; neither admiration, hostile generalizations nor inferred policy motives become the objective narrator’s own judgment. Civic logistics are fiction, not actual temple construction or a decree enforcement counter."
      }
    },
    {
      "consultedUrl": "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/22*.html",
      "passage": "Ammianus XXII.2 §1 checked for Julian’s entry into Constantinople and sole rule.",
      "limitations": "This passage does not support reopening temples/restoring sacrifices; that needs a separate exact source. Ammianus is an admiring pagan narrator.",
      "status": "disputed",
      "supportedClaim": "Supports Julian entering Constantinople after Constantius’ death and becoming sole ruler. / Respalda la entrada de Juliano en Constantinopla tras la muerte de Constancio y su gobierno único.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "XXII.2 §1 checked; no temple-policy passage located.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/22*.html",
      "passage": "XXII.2.1–5 and XXII.5.1–4; especially2.4 and5.2",
      "coverageActuallyRead": "Architect directly read selected entry/accession chapter2 and religious policy5.1–4 in the displayed English edition; adjacent criticisms recognized as context, not wholebook reading.",
      "limitations": "Later fourth-century narrator and former officer, not a neutral stenographer of the palace. Entry11December in this edition; use broad working frame for subsequent policy. Reopening/sacrifice orders do not quantify each local temple, acceptance or practice. Christian discord and imperial calculation in5.4 remain attributed interpretation; no recycled hostile generalization or authentic dialogue.",
      "consultationDate": "2026-10-15",
      "approval": "independent review pending"
    }
  ],
  "knowledgeBasis": {
    "speaker": "imperial-clerk",
    "proposedLifespan": "c.334–403",
    "mode": "fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports",
    "noOmniscience": true
  }
}
```

## Main objectives and individual contracts

### o1 / phase-1

EN: Visit all three ordinary work courts and register the six original helpers and three separately labelled supply notes. All local destinations are disclosed.

ES: Visita los tres patios de trabajo cotidiano y registra a los seis ayudantes originales y las tres notas de provisión etiquetadas por separado. Todos los destinos locales están indicados.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "area-state",
      "blockingEnemies": [],
      "requiredCount": 3,
      "state": "visited-and-passable",
      "id": "req-1",
      "zones": [
        "imperial-church.26-plural-civic-logistics-constantinople.destination-2",
        "imperial-church.26-plural-civic-logistics-constantinople.destination-3",
        "imperial-church.26-plural-civic-logistics-constantinople.destination-5"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-1",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-2",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-3",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-4",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-5",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-6"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-1",
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-2",
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-3"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three distinct local work courts and all nine original work identities are registered.

ES: Quedan registrados tres patios locales distintos de trabajo y las nueve identidades originales.

EN: A new title cannot tell me which door needs timber.

ES: Un título nuevo no me dice qué puerta necesita madera.

### o2 / phase-2

EN: Deliver the assigned pair of original helpers to each work court. Allocate exactly 120 food, 80 wood and 20 stone to each court once: 360 food, 240 wood and 60 stone total.

ES: Entrega la pareja asignada de ayudantes originales a cada patio. Asigna una vez exactamente 120 de alimento, 80 de madera y 20 de piedra a cada patio: 360 de alimento, 240 de madera y 60 de piedra en total.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-1",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-2",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-3",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-4",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-5",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-6"
      ],
      "destinations": {
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-1": "imperial-church.26-plural-civic-logistics-constantinople.destination-2",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-2": "imperial-church.26-plural-civic-logistics-constantinople.destination-2",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-3": "imperial-church.26-plural-civic-logistics-constantinople.destination-3",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-4": "imperial-church.26-plural-civic-logistics-constantinople.destination-3",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-5": "imperial-church.26-plural-civic-logistics-constantinople.destination-5",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-6": "imperial-church.26-plural-civic-logistics-constantinople.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 360,
        "wood": 240,
        "stone": 60
      },
      "id": "req-2",
      "receivingZones": [
        "imperial-church.26-plural-civic-logistics-constantinople.destination-2",
        "imperial-church.26-plural-civic-logistics-constantinople.destination-3",
        "imperial-church.26-plural-civic-logistics-constantinople.destination-5"
      ],
      "allocations": {
        "imperial-church.26-plural-civic-logistics-constantinople.destination-2": {
          "food": 120,
          "wood": 80,
          "stone": 20
        },
        "imperial-church.26-plural-civic-logistics-constantinople.destination-3": {
          "food": 120,
          "wood": 80,
          "stone": 20
        },
        "imperial-church.26-plural-civic-logistics-constantinople.destination-5": {
          "food": 120,
          "wood": 80,
          "stone": 20
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.26-plural-civic-logistics-constantinople.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three different assigned pairs and three conserved local shares are recorded.

ES: Quedan registradas tres parejas asignadas distintas y tres partes locales conservadas.

EN: The same grand total at one doorway would leave two yards waiting.

ES: El mismo gran total en una puerta dejaría esperando a dos patios.

### o3 / phase-3

EN: Deliver the first original supply note west, the second north and the third south. Keep all six original helpers and all three notes intact; prior work-court receptions remain recorded without requiring current residence.

ES: Entrega la primera nota original al oeste, la segunda al norte y la tercera al sur. Conserva intactos los seis ayudantes originales y las tres notas; las acogidas anteriores siguen registradas sin exigir permanencia actual.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-1",
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-2",
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-3"
      ],
      "destinations": {
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-1": "imperial-church.26-plural-civic-logistics-constantinople.destination-2",
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-2": "imperial-church.26-plural-civic-logistics-constantinople.destination-3",
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-3": "imperial-church.26-plural-civic-logistics-constantinople.destination-5"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All three distinct original notes reached their own assigned courts; the civic delivery contract is complete.

ES: Las tres notas originales distintas han llegado a sus propios patios asignados; el contrato de entrega cívica está completo.

EN: My ledger records a delivery. It cannot record a change of heart.

ES: Mi registro recoge una entrega. No puede recoger un cambio de convicción.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/26-plural-civic-logistics-constantinople.svg)

```json
{
  "bbox": [
    28.942,
    41.0,
    28.987,
    41.03
  ],
  "terrainProfile": "constantinople",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        235.13,
        220.48
      ],
      "lonLat": [
        28.969,
        41.013
      ],
      "name": {
        "en": "Fictional central civic dispatch yard",
        "es-ES": "Patio ficticio central de despachos cívicos"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        108.46,
        189.01
      ],
      "lonLat": [
        28.953,
        41.016
      ],
      "name": {
        "en": "Fictional western ordinary work court",
        "es-ES": "Patio ficticio occidental de trabajo cotidiano"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        219.29,
        105.07
      ],
      "lonLat": [
        28.967,
        41.024
      ],
      "name": {
        "en": "Fictional northern ordinary work court",
        "es-ES": "Patio ficticio septentrional de trabajo cotidiano"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        338.04,
        241.47
      ],
      "lonLat": [
        28.982,
        41.011
      ],
      "name": {
        "en": "Fictional eastern local note yard",
        "es-ES": "Patio ficticio oriental de notas locales"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        243.04,
        304.42
      ],
      "lonLat": [
        28.97,
        41.005
      ],
      "name": {
        "en": "Fictional southern ordinary work court",
        "es-ES": "Patio ficticio meridional de trabajo cotidiano"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-6",
      "centre": [
        124.29,
        241.47
      ],
      "lonLat": [
        28.955,
        41.011
      ],
      "name": {
        "en": "Fictional southwestern helper yard",
        "es-ES": "Patio ficticio suroccidental de ayudantes"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "western-civic-branch",
      "hubOrder": [
        "hub-6",
        "hub-2",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "northern-civic-branch",
      "hubOrder": [
        "hub-6",
        "hub-1",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "southern-civic-branch",
      "hubOrder": [
        "hub-6",
        "hub-5",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "local-note-distribution",
      "hubOrder": [
        "hub-4",
        "hub-1",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "northern-relief",
      "hubOrder": [
        "hub-2",
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "southern-relief",
      "hubOrder": [
        "hub-2",
        "hub-6",
        "hub-5",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 8
    }
  ],
  "terrainInstructions": "Constantinople peninsula: Golden Horn north, Marmara south and Bosporus east. All courts are fictional local urban or periurban activities, not identified temples or excavated palace rooms. Check each district against the Constantinian city and dated early fourth-century extensions; do not use the later Theodosian land walls as361geometry. No mandatory sea or Golden Horn crossing, Galata work destination, later Justinianic Hagia Sophia, medieval harbor defenses or modern fill. Sparse modern shoreline controls cannot prove ancient usable land; dated shore, drainage, terrain slope and full corridor widths require independent/native checks. Exact ritual sites and palace audience remain narrated context, never invented map venues.",
  "corridorStraightLengthsTiles": {
    "western-civic-branch": 185.32,
    "northern-civic-branch": 229.3,
    "southern-civic-branch": 248.37,
    "local-note-distribution": 235.55,
    "northern-relief": 319.88,
    "southern-relief": 273.51
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
  "asset": "docs/design/maps/imperial-church/odyssey/26-plural-civic-logistics-constantinople.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-1",
      "role": "fictional-voluntary-ordinary-work-helper",
      "initialHub": "hub-6",
      "offsetTiles": [
        -14,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "Fictional local participants or work items; no canonical autograph, authentic quotation or historical eyewitness."
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-2",
      "role": "fictional-voluntary-ordinary-work-helper",
      "initialHub": "hub-6",
      "offsetTiles": [
        -12,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "Fictional local participants or work items; no canonical autograph, authentic quotation or historical eyewitness."
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-3",
      "role": "fictional-voluntary-ordinary-work-helper",
      "initialHub": "hub-6",
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
      "historicalMaterialPolicy": "Fictional local participants or work items; no canonical autograph, authentic quotation or historical eyewitness."
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-4",
      "role": "fictional-voluntary-ordinary-work-helper",
      "initialHub": "hub-6",
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
      "historicalMaterialPolicy": "Fictional local participants or work items; no canonical autograph, authentic quotation or historical eyewitness."
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-5",
      "role": "fictional-voluntary-ordinary-work-helper",
      "initialHub": "hub-6",
      "offsetTiles": [
        -14,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "Fictional local participants or work items; no canonical autograph, authentic quotation or historical eyewitness."
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-6",
      "role": "fictional-voluntary-ordinary-work-helper",
      "initialHub": "hub-6",
      "offsetTiles": [
        -12,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "Fictional local participants or work items; no canonical autograph, authentic quotation or historical eyewitness."
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-1",
      "role": "fictional-separately-labelled-local-supply-note",
      "initialHub": "hub-4",
      "offsetTiles": [
        0,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "Fictional local participants or work items; no canonical autograph, authentic quotation or historical eyewitness."
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-2",
      "role": "fictional-separately-labelled-local-supply-note",
      "initialHub": "hub-4",
      "offsetTiles": [
        2,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "Fictional local participants or work items; no canonical autograph, authentic quotation or historical eyewitness."
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-3",
      "role": "fictional-separately-labelled-local-supply-note",
      "initialHub": "hub-4",
      "offsetTiles": [
        4,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "Fictional local participants or work items; no canonical autograph, authentic quotation or historical eyewitness."
    }
  ],
  "zones": [
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.destination-5",
      "hub": "hub-5",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.26-plural-civic-logistics-constantinople.destination-6",
      "hub": "hub-6",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    }
  ],
  "objectGroups": {
    "original-civic-helpers": [
      "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-1",
      "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-2",
      "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-3",
      "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-4",
      "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-5",
      "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-6"
    ],
    "original-local-supply-notes": [
      "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-1",
      "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-2",
      "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-3"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-1",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-2",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-3",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-4",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-5",
        "imperial-church.26-plural-civic-logistics-constantinople.original-civic-helpers-6"
      ],
      "minimumAliveOrAlreadySafe": 6
    },
    {
      "entities": [
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-1",
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-2",
        "imperial-church.26-plural-civic-logistics-constantinople.original-local-supply-notes-3"
      ],
      "minimumAliveOrAlreadySafe": 3
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Three courts, two approaches / Tres patios, dos accesos

EN: Visit both marked viewpoints at the northern and eastern yards to identify the northern local alternative. Benefit: Mark this proposed local land alternative once; main destinations remain disclosed.

ES: Visita los dos miradores señalados en los patios norte y este para identificar la alternativa local septentrional. Ventaja: Señala una vez esta alternativa terrestre local propuesta; los destinos principales siguen indicados.

EN: A local survey marks an alternative without locating a temple or changing civic access.

ES: Un reconocimiento local señala una alternativa sin situar un templo ni cambiar el acceso cívico.

```json
{
  "id": "side-1",
  "kind": "scout",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "visit-zones",
        "zones": [
          "26-plural-civic-logistics-constantinople.side-1.zone-1",
          "26-plural-civic-logistics-constantinople.side-1.zone-2"
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
        "id": "26-plural-civic-logistics-constantinople.side-1.zone-1",
        "hub": "hub-3",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "26-plural-civic-logistics-constantinople.side-1.zone-2",
        "hub": "hub-4",
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
      "target": "northern-relief",
      "resources": {},
      "onceFlag": "26-plural-civic-logistics-constantinople.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "northern-relief"
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
      "western-civic-branch",
      "northern-civic-branch",
      "southern-civic-branch",
      "local-note-distribution",
      "northern-relief",
      "southern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### An ordinary southern roof / Un tejado cotidiano al sur

EN: Pay 50 wood once to restore the damaged southern work shelter fully. Benefit: 200 food, 100 wood, once.

ES: Paga una vez 50 de madera para restaurar por completo el cobertizo meridional de trabajo. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: One paid repair releases a finite work reserve, without inventing historical temple destruction.

ES: Una reparación pagada libera una reserva finita de trabajo sin inventar destrucción histórica de templos.

```json
{
  "id": "side-2",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "26-plural-civic-logistics-constantinople.side-2.entity-1",
        "health": "full",
        "paymentReceipt": "26-plural-civic-logistics-constantinople.side-2.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "26-plural-civic-logistics-constantinople.side-2.payment",
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
        "id": "26-plural-civic-logistics-constantinople.side-2.entity-1",
        "role": "repair",
        "initialHub": "hub-5",
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
        "id": "26-plural-civic-logistics-constantinople.side-2.zone-1",
        "hub": "hub-5",
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
      "onceFlag": "26-plural-civic-logistics-constantinople.side-2.rewarded",
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
    "originHub": "hub-5",
    "receivingHub": "hub-5",
    "corridorIds": [
      "western-civic-branch",
      "northern-civic-branch",
      "southern-civic-branch",
      "local-note-distribution",
      "northern-relief",
      "southern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Households beside the western road / Hogares junto al camino occidental

EN: Take the two original aid crates from the southwest yard to their two assigned households by the western work court. Benefit: 100 food, 50 wood, once.

ES: Lleva las dos cajas originales de ayuda del patio suroccidental a sus dos hogares asignados junto al patio occidental. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Independent voluntary support is unrelated to the recipients’ beliefs.

ES: El auxilio voluntario independiente no depende de las creencias de los destinatarios.

```json
{
  "id": "side-3",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "26-plural-civic-logistics-constantinople.side-3.entity-1",
          "26-plural-civic-logistics-constantinople.side-3.entity-2"
        ],
        "destinations": {
          "26-plural-civic-logistics-constantinople.side-3.entity-1": "26-plural-civic-logistics-constantinople.side-3.zone-1",
          "26-plural-civic-logistics-constantinople.side-3.entity-2": "26-plural-civic-logistics-constantinople.side-3.zone-2"
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
        "id": "26-plural-civic-logistics-constantinople.side-3.entity-1",
        "role": "aid",
        "initialHub": "hub-6",
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
        "id": "26-plural-civic-logistics-constantinople.side-3.entity-2",
        "role": "aid",
        "initialHub": "hub-6",
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
        "id": "26-plural-civic-logistics-constantinople.side-3.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "26-plural-civic-logistics-constantinople.side-3.zone-2",
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
      "onceFlag": "26-plural-civic-logistics-constantinople.side-3.rewarded",
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
    "originHub": "hub-6",
    "receivingHub": "hub-2",
    "corridorIds": [
      "western-civic-branch",
      "northern-civic-branch",
      "southern-civic-branch",
      "local-note-distribution",
      "northern-relief",
      "southern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A single eastern consignment / Una sola remesa oriental

EN: Escort the eastern merchant to the central yard and pay 50 gold once for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante oriental al patio central y paga una vez 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A bounded local exchange can support parallel gathering; no purchase of policy compliance.

ES: Un intercambio local limitado puede apoyar la recolección paralela; no compra cumplimiento político.

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
          "26-plural-civic-logistics-constantinople.side-4.entity-1"
        ],
        "destinations": {
          "26-plural-civic-logistics-constantinople.side-4.entity-1": "26-plural-civic-logistics-constantinople.side-4.zone-1"
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
        "receipt": "26-plural-civic-logistics-constantinople.side-4.payment",
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
        "id": "26-plural-civic-logistics-constantinople.side-4.entity-1",
        "role": "trade",
        "initialHub": "hub-4",
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
        "id": "26-plural-civic-logistics-constantinople.side-4.zone-1",
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
        "food": 150,
        "wood": 50
      },
      "onceFlag": "26-plural-civic-logistics-constantinople.side-4.rewarded",
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
    "originHub": "hub-4",
    "receivingHub": "hub-1",
    "corridorIds": [
      "western-civic-branch",
      "northern-civic-branch",
      "southern-civic-branch",
      "local-note-distribution",
      "northern-relief",
      "southern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### An order and its limits / Una orden y sus límites

EN: Bring both separate local context notes from the northern yard to the central copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Lleva ambas notas locales separadas de contexto del patio norte al copista central. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Optional context distinguishes the reported decree from its unmeasured local reach.

ES: El contexto opcional distingue el decreto referido de su alcance local no medido.

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
          "26-plural-civic-logistics-constantinople.side-5.entity-1",
          "26-plural-civic-logistics-constantinople.side-5.entity-2"
        ],
        "destinations": {
          "26-plural-civic-logistics-constantinople.side-5.entity-1": "26-plural-civic-logistics-constantinople.side-5.zone-1",
          "26-plural-civic-logistics-constantinople.side-5.entity-2": "26-plural-civic-logistics-constantinople.side-5.zone-1"
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
        "id": "26-plural-civic-logistics-constantinople.side-5.entity-1",
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
        "id": "26-plural-civic-logistics-constantinople.side-5.entity-2",
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
        "id": "26-plural-civic-logistics-constantinople.side-5.zone-1",
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
      "onceFlag": "26-plural-civic-logistics-constantinople.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.26-plural-civic-logistics-constantinople"
      ],
      "historicalNote": {
        "en": "After Constantius’ death, Julian entered Constantinople in December 361. Ammianus later describes decrees reopening temples and restoring sacrifice. Orders are evidence of policy, not proof that every site reopened or every resident changed belief. This fictional civic network serves ordinary local work courts without assigning religious identity to the people receiving supplies. No goal chooses, reverses or enforces an imperial creed.",
        "es-ES": "Tras la muerte de Constancio, Juliano entró en Constantinopla en diciembre de 361. Amiano describe después decretos que reabren templos y restablecen sacrificios. Las órdenes prueban una política, no que todos los lugares abrieran ni que todos los habitantes cambiaran de creencia. Esta red cívica ficticia atiende patios locales de trabajo cotidiano sin asignar identidad religiosa a quienes reciben provisiones. Ningún objetivo elige, revoca ni impone un credo imperial."
      },
      "hint": {
        "en": "Visit all three ordinary work courts and register the six original helpers and three separately labelled supply notes. All local destinations are disclosed.",
        "es-ES": "Visita los tres patios de trabajo cotidiano y registra a los seis ayudantes originales y las tres notas de provisión etiquetadas por separado. Todos los destinos locales están indicados."
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
      "western-civic-branch",
      "northern-civic-branch",
      "southern-civic-branch",
      "local-note-distribution",
      "northern-relief",
      "southern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The southern work circuit / El circuito meridional de trabajo

EN: Accompany the southwest guide to the marked southern junction. Benefit: Mark this proposed local land alternative once; main destinations remain disclosed.

ES: Acompaña al guía suroccidental hasta el cruce meridional señalado. Ventaja: Señala una vez esta alternativa terrestre local propuesta; los destinos principales siguen indicados.

EN: Guidance marks an alternative land circuit without inventing sea transport or a ritual venue.

ES: La guía señala un circuito terrestre alternativo sin inventar transporte marítimo ni sede ritual.

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
          "26-plural-civic-logistics-constantinople.side-6.entity-1"
        ],
        "destinations": {
          "26-plural-civic-logistics-constantinople.side-6.entity-1": "26-plural-civic-logistics-constantinople.side-6.zone-1"
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
        "id": "26-plural-civic-logistics-constantinople.side-6.entity-1",
        "role": "guide",
        "initialHub": "hub-6",
        "offsetTiles": [
          -10,
          -6
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "26-plural-civic-logistics-constantinople.side-6.zone-1",
        "hub": "hub-5",
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
      "target": "southern-relief",
      "resources": {},
      "onceFlag": "26-plural-civic-logistics-constantinople.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "southern-relief"
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
    "originHub": "hub-6",
    "receivingHub": "hub-5",
    "corridorIds": [
      "western-civic-branch",
      "northern-civic-branch",
      "southern-civic-branch",
      "local-note-distribution",
      "northern-relief",
      "southern-relief"
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
      "id": "survey-and-attribution",
      "optionalObjectives": [
        "side-1",
        "side-5"
      ],
      "costOfOpportunity": "Read the policy limits and survey before dispatching three parallel teams; no main recipient is hidden.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "finite-work-investment",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Choose bounded roof/trade investment while preserving360F240W60S for the main three-way allocation.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "ordinary-local-care",
      "optionalObjectives": [
        "side-3",
        "side-6"
      ],
      "costOfOpportunity": "Split a voluntary household/guidance team from mandatory supply work; religious labels never alter costs or eligibility.",
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
      "food": 299,
      "wood": 161,
      "gold": 69,
      "stone": 46
    },
    "gatherableBank": {
      "food": 1481,
      "wood": 919,
      "gold": 141,
      "stone": 194
    },
    "mandatoryDeliveries": {
      "food": 360,
      "wood": 240,
      "gold": 0,
      "stone": 60
    },
    "protectedRecoveryStock": {
      "food": 320,
      "wood": 240,
      "gold": 60,
      "stone": 80
    },
    "replacementBudget": {
      "food": 0,
      "wood": 0,
      "gold": 0,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 1330,
      "wood": 880,
      "gold": 210,
      "stone": 240
    },
    "maxVillagers": 12,
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      30,
      55
    ],
    "difficultyLevers": "12 workers, all three pair/note assignments and route markers disclosed, higher finite start.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  },
  "standard": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 260,
      "wood": 140,
      "gold": 60,
      "stone": 40
    },
    "gatherableBank": {
      "food": 1520,
      "wood": 940,
      "gold": 150,
      "stone": 200
    },
    "mandatoryDeliveries": {
      "food": 360,
      "wood": 240,
      "gold": 0,
      "stone": 60
    },
    "protectedRecoveryStock": {
      "food": 320,
      "wood": 240,
      "gold": 60,
      "stone": 80
    },
    "replacementBudget": {
      "food": 0,
      "wood": 0,
      "gold": 0,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 1330,
      "wood": 880,
      "gold": 210,
      "stone": 240
    },
    "maxVillagers": 9,
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      35,
      65
    ],
    "difficultyLevers": "9 workers; choose parallel distribution or serial routes while gathering exact three-way shares under local fog.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  },
  "hard": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 221,
      "wood": 119,
      "gold": 51,
      "stone": 34
    },
    "gatherableBank": {
      "food": 1559,
      "wood": 961,
      "gold": 159,
      "stone": 206
    },
    "mandatoryDeliveries": {
      "food": 360,
      "wood": 240,
      "gold": 0,
      "stone": 60
    },
    "protectedRecoveryStock": {
      "food": 320,
      "wood": 240,
      "gold": 60,
      "stone": 80
    },
    "replacementBudget": {
      "food": 0,
      "wood": 0,
      "gold": 0,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 1330,
      "wood": 880,
      "gold": 210,
      "stone": 240
    },
    "maxVillagers": 6,
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      40,
      75
    ],
    "difficultyLevers": "6 workers and lower finite start; optional roof/trade expenditure competes with gathering and three destinations. All-skip main solvency remains protected. No unannounced time limit, enemy army, conversion quota or altered unit speed.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.title / always | none | Altars of a New Reign | Los altares de un nuevo reinado |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.fact-intro / intro first | collection-narrator | After Constantius’ death, Julian entered Constantinople in December 361. Ammianus later describes decrees reopening temples and restoring sacrifice. Orders are evidence of policy, not proof that every site reopened or every resident changed belief. This fictional civic network serves ordinary local work courts without assigning religious identity to the people receiving supplies. No goal chooses, reverses or enforces an imperial creed. | Tras la muerte de Constancio, Juliano entró en Constantinopla en diciembre de 361. Amiano describe después decretos que reabren templos y restablecen sacrificios. Las órdenes prueban una política, no que todos los lugares abrieran ni que todos los habitantes cambiaran de creencia. Esta red cívica ficticia atiende patios locales de trabajo cotidiano sin asignar identidad religiosa a quienes reciben provisiones. Ningún objetivo elige, revoca ni impone un credo imperial. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.handover / after fact-intro | collection-narrator | Marcus describes an invented temporary work visit within his eastern office years. He receives news of imperial decisions and has no access to private palace discussion. | Marco describe una visita temporal de trabajo inventada dentro de sus años en oficinas orientales. Recibe noticias de decisiones imperiales y no accede a deliberaciones privadas del palacio. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.persona-intro / after handover | imperial-clerk | I was twenty-seven. A porter laid a split carrying pole beside my desk. I had made the three shares add up and forgotten how far each load still had to go. He watched as I drew the routes again. I remember resenting his patience. A new reign had given me a new heading; it had not given him a sound pole. | Tenía veintisiete años. Un porteador apoyó una vara de carga partida junto a mi mesa. Había conseguido que las tres partes sumaran y olvidado cuánto camino le quedaba a cada carga. Él miró mientras yo volvía a dibujar las rutas. Recuerdo que me irritó su paciencia. Un reinado nuevo me había dado un encabezamiento nuevo; a él no le había dado una vara entera. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.route-help / available from start; repeatable without effect | none | Three ordinary work courts need distinct original helpers, distinct note identities and their exact own shares. All required sites are known. Stay within the peninsula’s proposed land circuits; later city walls, modern fill and missing water lines cannot certify ancient paths. No temple must be built, converted or taken from anyone. | Tres patios de trabajo cotidiano necesitan ayudantes originales distintos, notas distintas y sus propias partes exactas. Los lugares principales son conocidos. Mantente en los circuitos terrestres propuestos de la península; murallas posteriores, rellenos modernos y ausencia de líneas de agua no certifican caminos antiguos. No hay que construir, convertir ni quitar un templo a nadie. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.o1-goal / phase-1 active | none | Visit all three ordinary work courts and register the six original helpers and three separately labelled supply notes. All local destinations are disclosed. | Visita los tres patios de trabajo cotidiano y registra a los seis ayudantes originales y las tres notas de provisión etiquetadas por separado. Todos los destinos locales están indicados. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.o1-receipt / o1 latched once | none | Three distinct local work courts and all nine original work identities are registered. | Quedan registrados tres patios locales distintos de trabajo y las nueve identidades originales. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.o1-reaction / after o1 receipt | imperial-clerk | A new title cannot tell me which door needs timber. | Un título nuevo no me dice qué puerta necesita madera. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.o2-goal / phase-2 active | none | Deliver the assigned pair of original helpers to each work court. Allocate exactly 120 food, 80 wood and 20 stone to each court once: 360 food, 240 wood and 60 stone total. | Entrega la pareja asignada de ayudantes originales a cada patio. Asigna una vez exactamente 120 de alimento, 80 de madera y 20 de piedra a cada patio: 360 de alimento, 240 de madera y 60 de piedra en total. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.o2-receipt / o2 latched once | none | Three different assigned pairs and three conserved local shares are recorded. | Quedan registradas tres parejas asignadas distintas y tres partes locales conservadas. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.o2-reaction / after o2 receipt | imperial-clerk | The same grand total at one doorway would leave two yards waiting. | El mismo gran total en una puerta dejaría esperando a dos patios. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.o3-goal / phase-3 active | none | Deliver the first original supply note west, the second north and the third south. Keep all six original helpers and all three notes intact; prior work-court receptions remain recorded without requiring current residence. | Entrega la primera nota original al oeste, la segunda al norte y la tercera al sur. Conserva intactos los seis ayudantes originales y las tres notas; las acogidas anteriores siguen registradas sin exigir permanencia actual. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.o3-receipt / o3 latched once | none | All three distinct original notes reached their own assigned courts; the civic delivery contract is complete. | Las tres notas originales distintas han llegado a sus propios patios asignados; el contrato de entrega cívica está completo. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.o3-reaction / after o3 receipt | imperial-clerk | My ledger records a delivery. It cannot record a change of heart. | Mi registro recoge una entrega. No puede recoger un cambio de convicción. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-1-goal / optional list from start | none | Visit both marked viewpoints at the northern and eastern yards to identify the northern local alternative. Benefit: Mark this proposed local land alternative once; main destinations remain disclosed. | Visita los dos miradores señalados en los patios norte y este para identificar la alternativa local septentrional. Ventaja: Señala una vez esta alternativa terrestre local propuesta; los destinos principales siguen indicados. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-1-complete / side-1 completed | none | Three courts, two approaches completed. Its stated benefit has been granted once. | Tres patios, dos accesos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-1-lost / side-1 failed-optional | none | Three courts, two approaches is unavailable after the loss of its unique participant or object. The main mission continues. | Tres patios, dos accesos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-2-goal / optional list from start | none | Pay 50 wood once to restore the damaged southern work shelter fully. Benefit: 200 food, 100 wood, once. | Paga una vez 50 de madera para restaurar por completo el cobertizo meridional de trabajo. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-2-complete / side-2 completed | none | An ordinary southern roof completed. Its stated benefit has been granted once. | Un tejado cotidiano al sur: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-2-lost / side-2 failed-optional | none | An ordinary southern roof is unavailable after the loss of its unique participant or object. The main mission continues. | Un tejado cotidiano al sur: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-3-goal / optional list from start | none | Take the two original aid crates from the southwest yard to their two assigned households by the western work court. Benefit: 100 food, 50 wood, once. | Lleva las dos cajas originales de ayuda del patio suroccidental a sus dos hogares asignados junto al patio occidental. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-3-complete / side-3 completed | none | Households beside the western road completed. Its stated benefit has been granted once. | Hogares junto al camino occidental: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-3-lost / side-3 failed-optional | none | Households beside the western road is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares junto al camino occidental: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-4-goal / optional list from start | none | Escort the eastern merchant to the central yard and pay 50 gold once for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante oriental al patio central y paga una vez 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-4-complete / side-4 completed | none | A single eastern consignment completed. Its stated benefit has been granted once. | Una sola remesa oriental: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-4-lost / side-4 failed-optional | none | A single eastern consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Una sola remesa oriental: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-5-goal / optional list from start | none | Bring both separate local context notes from the northern yard to the central copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Lleva ambas notas locales separadas de contexto del patio norte al copista central. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-5-complete / side-5 completed | none | An order and its limits completed. Its stated benefit has been granted once. | Una orden y sus límites: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-5-lost / side-5 failed-optional | none | An order and its limits is unavailable after the loss of its unique participant or object. The main mission continues. | Una orden y sus límites: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-6-goal / optional list from start | none | Accompany the southwest guide to the marked southern junction. Benefit: Mark this proposed local land alternative once; main destinations remain disclosed. | Acompaña al guía suroccidental hasta el cruce meridional señalado. Ventaja: Señala una vez esta alternativa terrestre local propuesta; los destinos principales siguen indicados. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-6-complete / side-6 completed | none | The southern work circuit completed. Its stated benefit has been granted once. | El circuito meridional de trabajo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.side-6-lost / side-6 failed-optional | none | The southern work circuit is unavailable after the loss of its unique participant or object. The main mission continues. | El circuito meridional de trabajo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.fact-outro / victory first | collection-narrator | Three fictional work courts recorded their own helpers, supply allocations and local notes. These deliveries do not establish present residence, a temple’s location or religious compliance. Julian’s policy remains part of the historical account; local outcomes cannot measure everyone’s response. The next episode follows received accounts of Athanasius’ return and renewed expulsion at Alexandria, with the Persian campaign kept off-map. | Tres patios ficticios de trabajo registraron sus propios ayudantes, asignaciones de suministros y notas locales. Las entregas no prueban permanencia actual, la ubicación de un templo ni cumplimiento religioso. La política de Juliano sigue en el relato histórico; los resultados locales no miden la respuesta de todos. El próximo episodio sigue relatos recibidos del regreso y nueva expulsión de Atanasio en Alejandría, con la campaña persa fuera del mapa. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.persona-outro / after fact-outro | imperial-clerk | The porter came back to ask whether the southern yard had received its share. I checked that line before answering. He no longer laughed, and I was not sure whether to be grateful. That small hesitation is my memory of the work. The decrees reached us as reports; their authors did not tell me what anyone prayed behind a closed door. | El porteador volvió a preguntar si el patio sur había recibido su parte. Comprobé esa línea antes de responder. Ya no se reía y yo no sabía si agradecérselo. Esa pequeña vacilación es mi recuerdo del trabajo. Los decretos nos llegaban como noticias; sus autores no me contaban qué rezaba nadie detrás de una puerta cerrada. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.26-plural-civic-logistics-constantinople.odyssey.next-episode / after persona-outro | none | Continue with The Return That Did Not Last. This episode does not complete the campaign. | Continúa con El regreso que no duró. Este episodio no termina la campaña. |

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
      "status": "caption text authored; certified native Sequence Items pending"
    }
  ],
  "artDirection": {
    "style": "restrained early Constantinian urban/periurban civic work with differing ordinary households",
    "historicalControls": "No identified reopened temple or private palace room claimed. No later Justinianic dome, Theodosian walls or medieval skyline copied into361. Common policy narration precedes Marcus personal interpretation. Existing geographic sources are research controls, not period backgrounds.",
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "Each original helper pair is assigned to exactly one court.",
      "Exactly120F80W20S at each of three receivers; the total at one receiver is insufficient.",
      "Three original notes cannot substitute for one another.",
      "Historical receptions do not imply current residence; original identities must remain alive.",
      "All-skip optional solvency at each difficulty.",
      "No religious identity, conversion, temple capture or policy-compliance counter.",
      "Ammianus5.4 political motive remains attributed interpretation.",
      "No guaranteed single reopening day or universal practice.",
      "Map remains peninsula land; no later walls, sea crossing or modern fill.",
      "Common objective narrator precedes Marcus and fictional experience stays labelled.",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
