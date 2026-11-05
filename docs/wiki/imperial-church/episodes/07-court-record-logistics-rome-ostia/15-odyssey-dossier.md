# 7. A Day beneath the Law

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `07-court-record-logistics-rome-ostia` · 321 CE; distinguish judicial rule from agricultural exception · 400×400

## Historical frame and fixed outcome

EN: A constitution dated 7 March 321 and preserved in Justinian’s later code orders urban judges, population and trades to rest on the day of the sun, while allowing agricultural work in the countryside. A distinct constitution preserved in the Theodosian Code and published at Caralis on 3 July 321 permits emancipation, manumission and their records on that day. These are transmitted prescriptions, not evidence of uniform compliance, forced conversion or the enactment of a law in Rome. Our local Roman work courts are fiction.

ES: Una constitución fechada el 7 de marzo de 321 y conservada en el posterior código de Justiniano ordena descansar a jueces, población y oficios urbanos en el día del sol, y permite labores agrícolas en el campo. Otra constitución, conservada en el Código Teodosiano y publicada en Caralis el 3 de julio de 321, permite ese día emancipaciones, manumisiones y sus actas. Son prescripciones transmitidas, no pruebas de cumplimiento uniforme, conversión forzada ni promulgación de una ley en Roma. Nuestros patios locales romanos son ficticios.

EN: Two rural provision allocations and three separately labelled fictional working summaries reached their assigned receivers. That local circuit neither enacted a constitution nor manumitted an actual historical person. The March agricultural exception and the July permission for legal acts remain different transmitted rules. The later Interpretatio is not treated as a second 321 enactment.

ES: Dos asignaciones rurales de provisiones y tres resúmenes ficticios con etiquetas separadas llegaron a sus receptores asignados. Ese circuito local no promulgó una constitución ni manumitió a una persona histórica real. La excepción agrícola de marzo y el permiso de actos jurídicos de julio siguen siendo normas transmitidas diferentes. La posterior Interpretatio no se presenta como una segunda promulgación de 321.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "CJ3.12.2 preserves7March321 urban rest and the rural agricultural exception. CTh2.8.1 separately permits emancipation/manumission and their acts, published at Caralis3July321. Norms and later interpretation do not prove universal enforcement or mandatory conversion.",
        "es-ES": "CJ3.12.2 conserva descanso urbano y excepción agrícola rural del7de marzo de321. CTh2.8.1 permite por separado emancipación/manumisión y sus actas, publicado en Caralis el3de julio de321. Las normas y la interpretación posterior no prueban aplicación universal ni conversión obligatoria."
      },
      "architectCorrection": {
        "date": "2026-10-13",
        "author": "gpt-6",
        "approval": "independent historical review pending",
        "reason": "Direct primary passages and geographical controls replace candidate conflations; local participants and outputs remain fiction."
      }
    },
    {
      "consultedUrl": "https://www.thelatinlibrary.com/codtheod.html",
      "passage": "Codex Theodosianus 2.8.1 (Constantine to Elpidius; Latin transcription, 3 July 321).",
      "limitations": "The cited law does not contain the agricultural-work exception; that appears in a different legal context. Replace or remove that claim. Website is a transcription rather than critical edition.",
      "status": "disputed",
      "supportedClaim": "Supports restrictions on judicial business on Sunday, with emancipation/manumission allowed. / Respalda restricciones a la actividad judicial dominical, con excepción para manumisiones.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "Checked CTh 2.8.1 text and adjacent law; agricultural exception absent here.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://droitromain.univ-grenoble-alpes.fr/Corpus/CJ3.htm",
      "passage": "CJ3.12.2, Constantine to Helpidius, datedPP VNONMART321",
      "coverageActuallyRead": "Read full Latin constitution, urban judges/population/trades, rural cultivation exception and subscription.",
      "limitations": "Later codification/transcription; no321 Rome enactment venue or uniform compliance. Number3.12.3 in some older references must be matched by text.",
      "consultationDate": "2026-10-13",
      "approval": "architect interpretation; independent approval pending"
    },
    {
      "consultedUrl": "https://droitromain.univ-grenoble-alpes.fr/Constitutiones/CTh02.html",
      "passage": "CTh2.8.1 including subscription and separately labelled Interpretatio",
      "coverageActuallyRead": "Read full displayed Latin law permitting emancipation/manumission and acts; PP VNONIULCaralis equals3July321. Read later Interpretatio but did not attribute it to321.",
      "limitations": "This is not the agricultural-exception text. Caralis is the displayed publication place; local Rome gameplay is fiction. Later interpretative text is separate, not an additional contemporary decree.",
      "consultationDate": "2026-10-13",
      "approval": "architect interpretation; independent approval pending"
    }
  ],
  "knowledgeBasis": {
    "speaker": "imperial-clerk",
    "proposedLifespan": "c.334–403",
    "mode": "inherited family papers, not direct adult memory",
    "noOmniscience": true
  }
}
```

## Main objectives and individual contracts

### o1 / phase-1

EN: Visit both rural receivers and pay 300 food once:180 north and 120 east.

ES: Visita ambos receptores rurales y paga una vez 300 de alimento:180 norte y 120 este.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "area-state",
      "requiredCount": 2,
      "state": "visited-and-passable",
      "blockingEnemies": [],
      "id": "req-1",
      "zones": [
        "imperial-church.07-court-record-logistics-rome-ostia.destination-3",
        "imperial-church.07-court-record-logistics-rome-ostia.destination-4"
      ]
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 300
      },
      "id": "req-2",
      "receivingZones": [
        "imperial-church.07-court-record-logistics-rome-ostia.destination-3",
        "imperial-church.07-court-record-logistics-rome-ostia.destination-4"
      ],
      "allocations": {
        "imperial-church.07-court-record-logistics-rome-ostia.destination-3": {
          "food": 180
        },
        "imperial-church.07-court-record-logistics-rome-ostia.destination-4": {
          "food": 120
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.07-court-record-logistics-rome-ostia.o1.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both rural receivers were actually visited and received their distinct conserved shares.

ES: Se visitaron realmente ambos receptores rurales y recibieron sus partes distintas conservadas.

EN: Food in one court does not become food in the other because I write a total.

ES: El alimento de un patio no llega al otro porque yo escriba una suma.

### o2 / phase-2

EN: Collect the three separately labelled original context notes and deliver all three to common dispatch.

ES: Recoge las tres notas originales con etiquetas separadas y entrega las tres en el despacho común.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-1",
      "entities": [
        "imperial-church.07-court-record-logistics-rome-ostia.urban-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.07-court-record-logistics-rome-ostia.urban-note-1"
      ],
      "destinations": {
        "imperial-church.07-court-record-logistics-rome-ostia.urban-note-1": "imperial-church.07-court-record-logistics-rome-ostia.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.07-court-record-logistics-rome-ostia.agricultural-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "imperial-church.07-court-record-logistics-rome-ostia.agricultural-note-1"
      ],
      "destinations": {
        "imperial-church.07-court-record-logistics-rome-ostia.agricultural-note-1": "imperial-church.07-court-record-logistics-rome-ostia.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-5",
      "entities": [
        "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-6",
      "entities": [
        "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-note-1"
      ],
      "destinations": {
        "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-note-1": "imperial-church.07-court-record-logistics-rome-ostia.destination-1"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three distinct fictional notes reached common dispatch without losing their labels.

ES: Tres notas ficticias distintas llegaron al despacho común sin perder sus etiquetas.

EN: They are our local notes, not pages torn from books compiled after this day.

ES: Son nuestras notas locales, no páginas arrancadas de libros compilados después de este día.

### o3 / phase-3

EN: Pay 90 wood and 30 gold once, then prepare one separate summary from each collected context note.

ES: Paga una vez 90 de madera y 30 de oro, y prepara un resumen separado con cada nota de contexto recogida.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 90,
        "gold": 30
      },
      "id": "req-1",
      "receivingZones": [
        "imperial-church.07-court-record-logistics-rome-ostia.destination-1"
      ],
      "allocations": {
        "imperial-church.07-court-record-logistics-rome-ostia.destination-1": {
          "wood": 90,
          "gold": 30
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.07-court-record-logistics-rome-ostia.o3.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "imperial-church.07-court-record-logistics-rome-ostia.urban-note-1"
      ],
      "outputEntities": [
        "imperial-church.07-court-record-logistics-rome-ostia.urban-summary-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.07-court-record-logistics-rome-ostia.o3.req-1.paid",
          "fromObjective": "o3",
          "amounts": {
            "wood": 90,
            "gold": 30
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
        "imperial-church.07-court-record-logistics-rome-ostia.agricultural-note-1"
      ],
      "outputEntities": [
        "imperial-church.07-court-record-logistics-rome-ostia.agricultural-summary-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.07-court-record-logistics-rome-ostia.o3.req-1.paid",
          "fromObjective": "o3",
          "amounts": {
            "wood": 90,
            "gold": 30
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-4",
      "inputEntities": [
        "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-note-1"
      ],
      "outputEntities": [
        "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-summary-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.07-court-record-logistics-rome-ostia.o3.req-1.paid",
          "fromObjective": "o3",
          "amounts": {
            "wood": 90,
            "gold": 30
          },
          "newDebit": false
        }
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three distinct summaries share one funded receipt and preserve their separate inputs.

ES: Tres resúmenes distintos comparten un recibo de financiación y conservan sus entradas separadas.

EN: The exception is not a footnote I am free to throw away.

ES: La excepción no es una nota que pueda tirar libremente.

### o4 / phase-4

EN: Deliver the urban summary to the urban desk, the agricultural summary to the north rural court and the permitted-acts summary to the southeastern archive.

ES: Entrega el resumen urbano a la mesa urbana, el agrícola al patio rural norteño y el de actos permitidos al archivo sureste.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "imperial-church.07-court-record-logistics-rome-ostia.urban-summary-1"
      ],
      "destinations": {
        "imperial-church.07-court-record-logistics-rome-ostia.urban-summary-1": "imperial-church.07-court-record-logistics-rome-ostia.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.07-court-record-logistics-rome-ostia.agricultural-summary-1"
      ],
      "destinations": {
        "imperial-church.07-court-record-logistics-rome-ostia.agricultural-summary-1": "imperial-church.07-court-record-logistics-rome-ostia.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-summary-1"
      ],
      "destinations": {
        "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-summary-1": "imperial-church.07-court-record-logistics-rome-ostia.destination-5"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All three original derived summaries reached their own assigned destinations.

ES: Los tres resúmenes derivados originales llegaron a sus propios destinos asignados.

EN: A clean record keeps the limits beside the heading.

ES: Un registro claro conserva los límites junto al encabezamiento.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/07-court-record-logistics-rome-ostia.svg)

```json
{
  "bbox": [
    12.478,
    41.88,
    12.558,
    41.955
  ],
  "terrainProfile": "rome-ostia",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        135.88,
        235.13
      ],
      "lonLat": [
        12.5,
        41.91
      ],
      "name": {
        "en": "Common fictional dispatch court",
        "es-ES": "Patio ficticio común de despacho"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        100.53,
        296.88
      ],
      "lonLat": [
        12.49,
        41.897
      ],
      "name": {
        "en": "Urban context desk",
        "es-ES": "Mesa de contexto urbano"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        220.71,
        68.88
      ],
      "lonLat": [
        12.524,
        41.945
      ],
      "name": {
        "en": "Northern rural provision court",
        "es-ES": "Patio rural norteño de provisiones"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        302.0,
        92.63
      ],
      "lonLat": [
        12.547,
        41.94
      ],
      "name": {
        "en": "Eastern rural and legal context court",
        "es-ES": "Patio oriental rural y de contexto jurídico"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        298.47,
        330.13
      ],
      "lonLat": [
        12.546,
        41.89
      ],
      "name": {
        "en": "Southeastern separate-label archive",
        "es-ES": "Archivo sureste de etiquetas separadas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-rural-work",
      "hubOrder": [
        "hub-1",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-rural-archive",
      "hubOrder": [
        "hub-1",
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "urban-context-circuit",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "rural-link",
      "hubOrder": [
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 6
    }
  ],
  "terrainInstructions": "Local city/hinterland work frame east of the schematic Tiber in Rome. The two proposed rural courts are northeast of the compact urban core, not in the central forum districts. Five fictional work courts: common dispatch, urban context desk, northern rural provision, eastern rural provision and south-eastern receiving archive. No authentic judicial room, actual 321 promulgation venue, church-manumission address or later basilica footprint is asserted. Rural courtyards are local dramatization of the northeastern hinterland, not archaeological proof of dated 321 parcels or an excavated estate. Exact Aurelian-wall/road phase overlays and the city–hinterland boundary must be verified before placement approval. All mandatory travel stays on east-bank land; no Ostia voyage, downstream barges or mandatory river crossing. Ancient parcels, drainage, city/hinterland relation and roads require audit; no Baroque façades, railways or modern embankments.",
  "corridorStraightLengthsTiles": {
    "north-rural-work": 186.64,
    "east-rural-archive": 456.39,
    "urban-context-circuit": 271.87,
    "rural-link": 84.69
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
  "asset": "docs/design/maps/imperial-church/odyssey/07-court-record-logistics-rome-ostia.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.urban-note-1",
      "role": "fictional-urban-rule-context-note",
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
      "id": "imperial-church.07-court-record-logistics-rome-ostia.agricultural-note-1",
      "role": "fictional-rural-exception-context-note",
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
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-note-1",
      "role": "fictional-permitted-acts-context-note",
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
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.urban-summary-1",
      "role": "fictional-urban-working-summary",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.agricultural-summary-1",
      "role": "fictional-agricultural-working-summary",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-summary-1",
      "role": "fictional-permitted-acts-working-summary",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.07-court-record-logistics-rome-ostia.destination-5",
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
    "urban-note": [
      "imperial-church.07-court-record-logistics-rome-ostia.urban-note-1"
    ],
    "agricultural-note": [
      "imperial-church.07-court-record-logistics-rome-ostia.agricultural-note-1"
    ],
    "permitted-acts-note": [
      "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-note-1"
    ],
    "urban-summary": [
      "imperial-church.07-court-record-logistics-rome-ostia.urban-summary-1"
    ],
    "agricultural-summary": [
      "imperial-church.07-court-record-logistics-rome-ostia.agricultural-summary-1"
    ],
    "permitted-acts-summary": [
      "imperial-church.07-court-record-logistics-rome-ostia.permitted-acts-summary-1"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Between the rural courts / Entre los patios rurales

EN: Scout both marked viewpoints of between the rural courts. Benefit: Mark the proposed rural-link local land circuit once. All mandatory receivers are already disclosed.

ES: Explora los dos miradores señalados de entre los patios rurales. Ventaja: Señala una vez el circuito terrestre local propuesto rural-link. Todos los receptores obligatorios ya se indican.

EN: Mark the proposed local rural link; no ancient field survey or mandatory secret receiver.

ES: Señala el enlace rural local propuesto; no es una prospección de campos antiguos ni un receptor secreto obligatorio.

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
          "07-court-record-logistics-rome-ostia.side-1.zone-1",
          "07-court-record-logistics-rome-ostia.side-1.zone-2"
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
        "id": "07-court-record-logistics-rome-ostia.side-1.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "07-court-record-logistics-rome-ostia.side-1.zone-2",
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
      "target": "rural-link proposed local land approach",
      "resources": {},
      "onceFlag": "07-court-record-logistics-rome-ostia.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "rural-link"
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
      "north-rural-work",
      "east-rural-archive",
      "urban-context-circuit",
      "rural-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### March and July in separate margins / Marzo y julio en márgenes separados

EN: Recover both separate copies from march and july in separate margins and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de marzo y julio en márgenes separados y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Optional attributed context distinguishes the two 321 constitutions and later interpretation; it does not replace main notes.

ES: El contexto opcional atribuido distingue las dos constituciones de 321 y la interpretación posterior; no sustituye las notas principales.

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
          "07-court-record-logistics-rome-ostia.side-2.entity-1",
          "07-court-record-logistics-rome-ostia.side-2.entity-2"
        ],
        "destinations": {
          "07-court-record-logistics-rome-ostia.side-2.entity-1": "07-court-record-logistics-rome-ostia.side-2.zone-1",
          "07-court-record-logistics-rome-ostia.side-2.entity-2": "07-court-record-logistics-rome-ostia.side-2.zone-1"
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
        "id": "07-court-record-logistics-rome-ostia.side-2.entity-1",
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
        "id": "07-court-record-logistics-rome-ostia.side-2.entity-2",
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
        "id": "07-court-record-logistics-rome-ostia.side-2.zone-1",
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
      "onceFlag": "07-court-record-logistics-rome-ostia.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.07-court-record-logistics-rome-ostia"
      ],
      "historicalNote": {
        "en": "A constitution dated 7 March 321 and preserved in Justinian’s later code orders urban judges, population and trades to rest on the day of the sun, while allowing agricultural work in the countryside. A distinct constitution preserved in the Theodosian Code and published at Caralis on 3 July 321 permits emancipation, manumission and their records on that day. These are transmitted prescriptions, not evidence of uniform compliance, forced conversion or the enactment of a law in Rome. Our local Roman work courts are fiction.",
        "es-ES": "Una constitución fechada el 7 de marzo de 321 y conservada en el posterior código de Justiniano ordena descansar a jueces, población y oficios urbanos en el día del sol, y permite labores agrícolas en el campo. Otra constitución, conservada en el Código Teodosiano y publicada en Caralis el 3 de julio de 321, permite ese día emancipaciones, manumisiones y sus actas. Son prescripciones transmitidas, no pruebas de cumplimiento uniforme, conversión forzada ni promulgación de una ley en Roma. Nuestros patios locales romanos son ficticios."
      },
      "hint": {
        "en": "Visit both rural receivers and pay 300 food once:180 north and 120 east.",
        "es-ES": "Visita ambos receptores rurales y paga una vez 300 de alimento:180 norte y 120 este."
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
      "north-rural-work",
      "east-rural-archive",
      "urban-context-circuit",
      "rural-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Households on both circuits / Hogares de ambos circuitos

EN: Bring each of the two aid crates to its assigned household at households on both circuits. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de ambos circuitos. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Voluntary independent household support does not pay the 180/120 main shares or score religious obedience.

ES: La ayuda voluntaria independiente no paga las partes principales de 180/120 ni puntúa obediencia religiosa.

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
          "07-court-record-logistics-rome-ostia.side-3.entity-1",
          "07-court-record-logistics-rome-ostia.side-3.entity-2"
        ],
        "destinations": {
          "07-court-record-logistics-rome-ostia.side-3.entity-1": "07-court-record-logistics-rome-ostia.side-3.zone-1",
          "07-court-record-logistics-rome-ostia.side-3.entity-2": "07-court-record-logistics-rome-ostia.side-3.zone-2"
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
        "id": "07-court-record-logistics-rome-ostia.side-3.entity-1",
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
        "id": "07-court-record-logistics-rome-ostia.side-3.entity-2",
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
        "id": "07-court-record-logistics-rome-ostia.side-3.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "07-court-record-logistics-rome-ostia.side-3.zone-2",
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
      "onceFlag": "07-court-record-logistics-rome-ostia.side-3.rewarded",
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
      "north-rural-work",
      "east-rural-archive",
      "urban-context-circuit",
      "rural-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A rural working shelter / Un cobertizo rural de trabajo

EN: Pay 50 wood and restore the damaged store of a rural working shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de un cobertizo rural de trabajo. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair an ordinary separate shelter for bounded supplies; no universal ban on construction is simulated.

ES: Repara un cobertizo separado para provisiones limitadas; no se simula prohibición universal de construcción.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "07-court-record-logistics-rome-ostia.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "07-court-record-logistics-rome-ostia.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "07-court-record-logistics-rome-ostia.side-4.payment",
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
        "id": "07-court-record-logistics-rome-ostia.side-4.entity-1",
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
        "id": "07-court-record-logistics-rome-ostia.side-4.zone-1",
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
      "onceFlag": "07-court-record-logistics-rome-ostia.side-4.rewarded",
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
      "north-rural-work",
      "east-rural-archive",
      "urban-context-circuit",
      "rural-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### One rural supply consignment / Una remesa rural de provisiones

EN: Escort the trader of one rural supply consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de una remesa rural de provisiones hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One finite exchange supports provisioning without buying an exemption, conversion or person’s freedom.

ES: Un intercambio finito apoya provisiones sin comprar una exención, conversión ni libertad personal.

```json
{
  "id": "side-5",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "07-court-record-logistics-rome-ostia.side-5.entity-1"
        ],
        "destinations": {
          "07-court-record-logistics-rome-ostia.side-5.entity-1": "07-court-record-logistics-rome-ostia.side-5.zone-1"
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
        "receipt": "07-court-record-logistics-rome-ostia.side-5.payment",
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
        "id": "07-court-record-logistics-rome-ostia.side-5.entity-1",
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
        "id": "07-court-record-logistics-rome-ostia.side-5.zone-1",
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
      "onceFlag": "07-court-record-logistics-rome-ostia.side-5.rewarded",
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
      "north-rural-work",
      "east-rural-archive",
      "urban-context-circuit",
      "rural-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The eastern receiving circuit / El circuito receptor oriental

EN: Escort the local guide of the eastern receiving circuit to the marked road junction. Benefit: Mark the proposed east-rural-archive local land circuit once. All mandatory receivers are already disclosed.

ES: Escolta al guía local de el circuito receptor oriental hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local propuesto east-rural-archive. Todos los receptores obligatorios ya se indican.

EN: Mark the proposed eastern local land circuit, not the historical promulgation journey from Caralis.

ES: Señala el circuito terrestre local oriental propuesto, no un viaje histórico de promulgación desde Caralis.

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
          "07-court-record-logistics-rome-ostia.side-6.entity-1"
        ],
        "destinations": {
          "07-court-record-logistics-rome-ostia.side-6.entity-1": "07-court-record-logistics-rome-ostia.side-6.zone-1"
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
        "id": "07-court-record-logistics-rome-ostia.side-6.entity-1",
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
        "id": "07-court-record-logistics-rome-ostia.side-6.zone-1",
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
      "target": "east-rural-archive proposed local land approach",
      "resources": {},
      "onceFlag": "07-court-record-logistics-rome-ostia.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "east-rural-archive"
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
      "north-rural-work",
      "east-rural-archive",
      "urban-context-circuit",
      "rural-link"
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
      "id": "rural-provision-first",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Survey both rural approaches and split300food into180/120 before collecting notes.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "context-and-workshop",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Keep normative distinctions visible while an independent team prepares shelter; reserve main90wood/30gold.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "households-and-supply",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Support ordinary households and bounded trade while main runners return distinct notes.",
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
      "food": 1418,
      "wood": 798,
      "gold": 234,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 90,
      "gold": 30,
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
      "wood": 770,
      "gold": 320,
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
      "food": 1470,
      "wood": 820,
      "gold": 245,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 90,
      "gold": 30,
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
      "wood": 770,
      "gold": 320,
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
      "food": 1523,
      "wood": 843,
      "gold": 257,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 90,
      "gold": 30,
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
      "wood": 770,
      "gold": 320,
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
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.title / always | none | A Day beneath the Law | Un día bajo la ley |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.fact-intro / intro first | collection-narrator | A constitution dated 7 March 321 and preserved in Justinian’s later code orders urban judges, population and trades to rest on the day of the sun, while allowing agricultural work in the countryside. A distinct constitution preserved in the Theodosian Code and published at Caralis on 3 July 321 permits emancipation, manumission and their records on that day. These are transmitted prescriptions, not evidence of uniform compliance, forced conversion or the enactment of a law in Rome. Our local Roman work courts are fiction. | Una constitución fechada el 7 de marzo de 321 y conservada en el posterior código de Justiniano ordena descansar a jueces, población y oficios urbanos en el día del sol, y permite labores agrícolas en el campo. Otra constitución, conservada en el Código Teodosiano y publicada en Caralis el 3 de julio de 321, permite ese día emancipaciones, manumisiones y sus actas. Son prescripciones transmitidas, no pruebas de cumplimiento uniforme, conversión forzada ni promulgación de una ley en Roma. Nuestros patios locales romanos son ficticios. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.persona-intro / after handover | imperial-clerk | The heading says rest. The lines beneath it do not all say the same thing. I know the office’s temptation to shorten an instruction until the exception disappears. In these inherited rules, a field and an urban dispute have different margins. I will not pretend that this imagined desk is the emperor’s lawgiver. | El encabezamiento dice descanso. Las líneas siguientes no dicen todas lo mismo. Conozco la tentación de la oficina de acortar una instrucción hasta que desaparece la excepción. En estas normas heredadas, un campo y una disputa urbana tienen márgenes distintos. No fingiré que esta mesa imaginada es la del legislador imperial. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.route-help / available from start; repeatable without effect | none | First visit both rural receivers and provide 300 food:180 to the northern court and 120 to the eastern one. Then collect one urban-context note, one northern rural note and one eastern legal-context note and bring all three to common dispatch. Pay 90 wood and 30 gold once, then make three separately labelled working summaries from their own collected note and the same funded receipt. Deliver the urban summary to the urban desk, the agricultural summary to the north rural court and the permitted-acts summary to the south-eastern archive. This circuit is not a simulation that freezes all urban work or grants personal legal freedom. | Primero visita ambos receptores rurales y entrega 300 de alimento:180 al patio norteño y 120 al oriental. Recoge después una nota de contexto urbano, una rural norteña y una jurídica oriental, y lleva las tres al despacho común. Paga una vez 90 de madera y 30 de oro, y prepara tres resúmenes con etiquetas separadas a partir de su propia nota recogida y el mismo recibo de financiación. Entrega el resumen urbano a la mesa urbana, el agrícola al patio rural norteño y el de actos permitidos al archivo sureste. Este circuito no simula la congelación de todo trabajo urbano ni concede libertad jurídica personal. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o1-goal / phase-1 active | none | Visit both rural receivers and pay 300 food once:180 north and 120 east. | Visita ambos receptores rurales y paga una vez 300 de alimento:180 norte y 120 este. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o1-receipt / o1 latched once | none | Both rural receivers were actually visited and received their distinct conserved shares. | Se visitaron realmente ambos receptores rurales y recibieron sus partes distintas conservadas. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o1-reaction / after o1 receipt | imperial-clerk | Food in one court does not become food in the other because I write a total. | El alimento de un patio no llega al otro porque yo escriba una suma. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o2-goal / phase-2 active | none | Collect the three separately labelled original context notes and deliver all three to common dispatch. | Recoge las tres notas originales con etiquetas separadas y entrega las tres en el despacho común. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o2-receipt / o2 latched once | none | Three distinct fictional notes reached common dispatch without losing their labels. | Tres notas ficticias distintas llegaron al despacho común sin perder sus etiquetas. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o2-reaction / after o2 receipt | imperial-clerk | They are our local notes, not pages torn from books compiled after this day. | Son nuestras notas locales, no páginas arrancadas de libros compilados después de este día. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o3-goal / phase-3 active | none | Pay 90 wood and 30 gold once, then prepare one separate summary from each collected context note. | Paga una vez 90 de madera y 30 de oro, y prepara un resumen separado con cada nota de contexto recogida. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o3-receipt / o3 latched once | none | Three distinct summaries share one funded receipt and preserve their separate inputs. | Tres resúmenes distintos comparten un recibo de financiación y conservan sus entradas separadas. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o3-reaction / after o3 receipt | imperial-clerk | The exception is not a footnote I am free to throw away. | La excepción no es una nota que pueda tirar libremente. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o4-goal / phase-4 active | none | Deliver the urban summary to the urban desk, the agricultural summary to the north rural court and the permitted-acts summary to the southeastern archive. | Entrega el resumen urbano a la mesa urbana, el agrícola al patio rural norteño y el de actos permitidos al archivo sureste. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o4-receipt / o4 latched once | none | All three original derived summaries reached their own assigned destinations. | Los tres resúmenes derivados originales llegaron a sus propios destinos asignados. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.o4-reaction / after o4 receipt | imperial-clerk | A clean record keeps the limits beside the heading. | Un registro claro conserva los límites junto al encabezamiento. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of between the rural courts. Benefit: Mark the proposed rural-link local land circuit once. All mandatory receivers are already disclosed. | Explora los dos miradores señalados de entre los patios rurales. Ventaja: Señala una vez el circuito terrestre local propuesto rural-link. Todos los receptores obligatorios ya se indican. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-1-complete / side-1 completed | none | Between the rural courts completed. Its stated benefit has been granted once. | Entre los patios rurales: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-1-lost / side-1 failed-optional | none | Between the rural courts is unavailable after the loss of its unique participant or object. The main mission continues. | Entre los patios rurales: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from march and july in separate margins and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de marzo y julio en márgenes separados y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-2-complete / side-2 completed | none | March and July in separate margins completed. Its stated benefit has been granted once. | Marzo y julio en márgenes separados: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-2-lost / side-2 failed-optional | none | March and July in separate margins is unavailable after the loss of its unique participant or object. The main mission continues. | Marzo y julio en márgenes separados: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at households on both circuits. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de ambos circuitos. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-3-complete / side-3 completed | none | Households on both circuits completed. Its stated benefit has been granted once. | Hogares de ambos circuitos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-3-lost / side-3 failed-optional | none | Households on both circuits is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares de ambos circuitos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of a rural working shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de un cobertizo rural de trabajo. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-4-complete / side-4 completed | none | A rural working shelter completed. Its stated benefit has been granted once. | Un cobertizo rural de trabajo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-4-lost / side-4 failed-optional | none | A rural working shelter is unavailable after the loss of its unique participant or object. The main mission continues. | Un cobertizo rural de trabajo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-5-goal / optional list from start | none | Escort the trader of one rural supply consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de una remesa rural de provisiones hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-5-complete / side-5 completed | none | One rural supply consignment completed. Its stated benefit has been granted once. | Una remesa rural de provisiones: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-5-lost / side-5 failed-optional | none | One rural supply consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Una remesa rural de provisiones: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the eastern receiving circuit to the marked road junction. Benefit: Mark the proposed east-rural-archive local land circuit once. All mandatory receivers are already disclosed. | Escolta al guía local de el circuito receptor oriental hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local propuesto east-rural-archive. Todos los receptores obligatorios ya se indican. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-6-complete / side-6 completed | none | The eastern receiving circuit completed. Its stated benefit has been granted once. | El circuito receptor oriental: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.side-6-lost / side-6 failed-optional | none | The eastern receiving circuit is unavailable after the loss of its unique participant or object. The main mission continues. | El circuito receptor oriental: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.fact-outro / victory first | collection-narrator | Two rural provision allocations and three separately labelled fictional working summaries reached their assigned receivers. That local circuit neither enacted a constitution nor manumitted an actual historical person. The March agricultural exception and the July permission for legal acts remain different transmitted rules. The later Interpretatio is not treated as a second 321 enactment. | Dos asignaciones rurales de provisiones y tres resúmenes ficticios con etiquetas separadas llegaron a sus receptores asignados. Ese circuito local no promulgó una constitución ni manumitió a una persona histórica real. La excepción agrícola de marzo y el permiso de actos jurídicos de julio siguen siendo normas transmitidas diferentes. La posterior Interpretatio no se presenta como una segunda promulgación de 321. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.persona-outro / after fact-outro | imperial-clerk | Three labels take more space than one slogan. I have made space. I am not counting believers, and I cannot measure every household’s obedience from this yard. An exception kept visible is part of the account, not a flaw I must erase. | Tres etiquetas ocupan más espacio que una consigna. He hecho espacio. No cuento creyentes ni puedo medir la obediencia de cada hogar desde este patio. Una excepción visible forma parte de la cuenta, no es un defecto que deba borrar. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.07-court-record-logistics-rome-ostia.odyssey.next-episode / after persona-outro | none | Continue with The Maritsa Crossing. This episode does not complete the campaign. | Continúa con El paso del Maritsa. Este episodio no termina la campaña. |

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
    },
    {
      "id": "receipt-gated-ordered-departure",
      "status": "reference implemented; native observers and real navigation pending"
    }
  ],
  "artDirection": {
    "style": "sober late Roman local work and land routes",
    "historicalControls": "fictional courts and field pockets; no exact emperor deployment, legal autograph or modern monument",
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "north180/east120 food shares cannot be replaced by300atonehub",
      "both rural visits require actual observation",
      "urban/agricultural/permitted-acts notes are disjoint inputs",
      "three generated summaries require their own exacto3 funded receipt and correct input; repeat events never regenerate",
      "each summary has its own destination; one delivery cannot satisfy allthree",
      "optional March/July context does not add canonical books to321 world",
      "no actual people bought or manumitted by resource payment",
      "CJ3.12.2 contains agricultural exception; CTh2.8.1 contains permitted acts, not that exception",
      "CTh publication Caralis3July differs from local fictional Rome scene",
      "later Interpretatio not falsely attributed as321 enactment",
      "all main paths passable without optional tasks; no office work lock promised",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
