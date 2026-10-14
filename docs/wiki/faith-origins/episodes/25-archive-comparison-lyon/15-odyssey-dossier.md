# 25. Voices Against the Fragments

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `25-archive-comparison-lyon` · c. 180–200 CE · 360×360

## Historical frame and fixed outcome

EN: In Against Heresies, Irenaeus argues for inherited teaching and episcopal succession, using Rome as one example. This is a theological polemic with claims about authority and opponents. It is not an impartial catalogue of every community. The local comparison exercise here is fiction and decides no doctrine.

ES: En Contra las herejías, Ireneo argumenta a favor de la enseñanza heredada y la sucesión episcopal, con Roma como uno de sus ejemplos. Es una polémica teológica con afirmaciones sobre autoridad y adversarios. No es un catálogo imparcial de todas las comunidades. El ejercicio local de comparación es ficticio y no decide doctrina.

EN: Two separate fictional working registers were produced from their own collected notes and delivered to their assigned yards. Their preservation neither authenticates a disputed succession nor proves or refutes the positions of Irenaeus or his opponents.

ES: Se produjeron dos registros ficticios separados a partir de sus propias notas recogidas y se entregaron en sus patios asignados. Conservarlos no autentica una sucesión disputada ni demuestra o refuta las posiciones de Ireneo o sus adversarios.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 18,
      "episodeId": "25-archive-comparison-lyon",
      "order": 25,
      "selectedSourceUrl": "https://www.newadvent.org/fathers/0103.htm",
      "consultedUrl": "https://www.newadvent.org/fathers/0103.htm",
      "passage": "Irenaeus, Against Heresies 3.3.2–3: Roman episcopal succession argument; Book I preface and Book III identify polemical target and tradition claims.",
      "supportedClaim": {
        "en": "Irenaeus' polemic argues from inherited teaching and episcopal succession, using Rome as an example.",
        "es-ES": "La polémica de Ireneo argumenta desde la enseñanza heredada y la sucesión episcopal, y usa Roma como ejemplo."
      },
      "limitations": "This is a theological polemic, not a neutral account of all communities or uncontested institutional history. It supports debate over authority/tradition, not a specific Lyon archival event; composition c.180–200 is external dating.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/0103303.htm",
      "passage": "Against HeresiesIII3.1–4; architect read succession argument, Roman example and attributed memories of Polycarp",
      "limitations": "Polemical advocacy, not neutral ethnography or independent consensus; exact Lyon archival exercise and opponent quotations are not documented. Local two-register comparison is fictional and awards no doctrinal truth.",
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

EN: Collect both separate groups of three context notes. Deliver the authority group to the western court and the comparison group to the southern yard.

ES: Recoge ambos grupos separados de tres notas de contexto. Entrega el grupo de autoridad en el patio occidental y el de comparación en el meridional.

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
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-1",
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-2",
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-1",
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-2",
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-1",
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-2",
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-3"
      ],
      "destinations": {
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-1": "faith-origins.25-archive-comparison-lyon.destination-2",
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-2": "faith-origins.25-archive-comparison-lyon.destination-2",
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-3": "faith-origins.25-archive-comparison-lyon.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-1",
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-2",
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-3"
      ],
      "destinations": {
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-1": "faith-origins.25-archive-comparison-lyon.destination-4",
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-2": "faith-origins.25-archive-comparison-lyon.destination-4",
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-3": "faith-origins.25-archive-comparison-lyon.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Two distinct labelled input groups reached their own preparation sites.

ES: Dos grupos distintos y etiquetados de entradas llegaron a sus lugares propios de preparación.

EN: A label records a viewpoint; it does not announce a winner.

ES: Una etiqueta registra una perspectiva; no anuncia un ganador.

### o2 / phase-2

EN: Pay 60 wood and 20 gold once at the western court and once at the southern yard.

ES: Paga una vez 60 de madera y 20 de oro en el patio occidental y otra en el meridional.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 60,
        "gold": 20
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.25-archive-comparison-lyon.destination-2"
      ],
      "allocations": {
        "faith-origins.25-archive-comparison-lyon.destination-2": {
          "wood": 60,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.25-archive-comparison-lyon.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 60,
        "gold": 20
      },
      "id": "req-2",
      "receivingZones": [
        "faith-origins.25-archive-comparison-lyon.destination-4"
      ],
      "allocations": {
        "faith-origins.25-archive-comparison-lyon.destination-4": {
          "wood": 60,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.25-archive-comparison-lyon.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both independent exact payments are recorded; neither can fund both preparations.

ES: Constan ambos pagos exactos independientes; ninguno financia las dos preparaciones.

EN: The same coin cannot pay for both tables merely because I favor one.

ES: La misma moneda no paga ambas mesas porque yo prefiera una.

### o3 / phase-3

EN: Create the authority register from its three notes and western payment, and the comparison register from its three notes and southern payment.

ES: Crea el registro de autoridad con sus tres notas y pago occidental, y el de comparación con sus tres notas y pago meridional.

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
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-1",
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-2",
        "faith-origins.25-archive-comparison-lyon.authority-context-notes-3"
      ],
      "outputEntities": [
        "faith-origins.25-archive-comparison-lyon.authority-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.25-archive-comparison-lyon.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 60,
            "gold": 20
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
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-1",
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-2",
        "faith-origins.25-archive-comparison-lyon.comparison-context-notes-3"
      ],
      "outputEntities": [
        "faith-origins.25-archive-comparison-lyon.comparison-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.25-archive-comparison-lyon.o2.req-2.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 60,
            "gold": 20
          },
          "newDebit": false
        }
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Separate input lineage and separate payment receipts produced two registers.

ES: Linajes separados de entradas y recibos separados de pago produjeron dos registros.

EN: A second register is not a second ancient source. Both belong to this imagined exercise.

ES: Un segundo registro no es una segunda fuente antigua. Ambos pertenecen a este ejercicio imaginado.

### o4 / phase-4

EN: Deliver the original authority register to the northwestern yard and the original comparison register to the central court.

ES: Entrega el registro original de autoridad en el patio noroccidental y el original de comparación en el patio central.

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
        "faith-origins.25-archive-comparison-lyon.authority-register-1"
      ],
      "destinations": {
        "faith-origins.25-archive-comparison-lyon.authority-register-1": "faith-origins.25-archive-comparison-lyon.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.25-archive-comparison-lyon.comparison-register-1"
      ],
      "destinations": {
        "faith-origins.25-archive-comparison-lyon.comparison-register-1": "faith-origins.25-archive-comparison-lyon.destination-1"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both separately assigned register deliveries are complete.

ES: Se han completado ambas entregas de registros asignadas por separado.

EN: I can preserve both labels without lending my own voice to someone I have never heard.

ES: Puedo conservar ambas etiquetas sin prestar mi voz a alguien a quien nunca he oído.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/25-archive-comparison-lyon.svg)

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
        172.72,
        223.21
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
        84.64,
        194.07
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
        132.07,
        87.22
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
        199.83,
        281.49
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
    "main": 209.68,
    "southern-road": 208.88,
    "relief": 350.35
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
  "asset": "docs/design/maps/faith-origins/odyssey/25-archive-comparison-lyon.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.25-archive-comparison-lyon.authority-context-notes-1",
      "role": "fictional-labelled-context-note",
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
      "id": "faith-origins.25-archive-comparison-lyon.authority-context-notes-2",
      "role": "fictional-labelled-context-note",
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
      "id": "faith-origins.25-archive-comparison-lyon.authority-context-notes-3",
      "role": "fictional-labelled-context-note",
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
      "id": "faith-origins.25-archive-comparison-lyon.comparison-context-notes-1",
      "role": "fictional-labelled-context-note",
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
      "id": "faith-origins.25-archive-comparison-lyon.comparison-context-notes-2",
      "role": "fictional-labelled-context-note",
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
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.25-archive-comparison-lyon.comparison-context-notes-3",
      "role": "fictional-labelled-context-note",
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
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.25-archive-comparison-lyon.authority-register-1",
      "role": "fictional-labelled-working-register",
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
      "id": "faith-origins.25-archive-comparison-lyon.comparison-register-1",
      "role": "fictional-labelled-working-register",
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
      "id": "faith-origins.25-archive-comparison-lyon.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.25-archive-comparison-lyon.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.25-archive-comparison-lyon.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.25-archive-comparison-lyon.destination-4",
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
    "authority-context-notes": [
      "faith-origins.25-archive-comparison-lyon.authority-context-notes-1",
      "faith-origins.25-archive-comparison-lyon.authority-context-notes-2",
      "faith-origins.25-archive-comparison-lyon.authority-context-notes-3"
    ],
    "comparison-context-notes": [
      "faith-origins.25-archive-comparison-lyon.comparison-context-notes-1",
      "faith-origins.25-archive-comparison-lyon.comparison-context-notes-2",
      "faith-origins.25-archive-comparison-lyon.comparison-context-notes-3"
    ],
    "authority-register": [
      "faith-origins.25-archive-comparison-lyon.authority-register-1"
    ],
    "comparison-register": [
      "faith-origins.25-archive-comparison-lyon.comparison-register-1"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### The argument’s source margin / El margen de fuentes del argumento

EN: Recover both separate copies from the argument’s source margin and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de el margen de fuentes del argumento y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Qualified source context preserves polemic attribution; no invented rival quotation or literal canonical copy.

ES: El contexto mantiene la atribución polémica; no crea citas de adversarios ni copias canónicas literales.

```json
{
  "id": "side-1",
  "kind": "copy",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "25-archive-comparison-lyon.side-1.entity-1",
          "25-archive-comparison-lyon.side-1.entity-2"
        ],
        "destinations": {
          "25-archive-comparison-lyon.side-1.entity-1": "25-archive-comparison-lyon.side-1.zone-1",
          "25-archive-comparison-lyon.side-1.entity-2": "25-archive-comparison-lyon.side-1.zone-1"
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
        "id": "25-archive-comparison-lyon.side-1.entity-1",
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
        "id": "25-archive-comparison-lyon.side-1.entity-2",
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
        "id": "25-archive-comparison-lyon.side-1.zone-1",
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
      "onceFlag": "25-archive-comparison-lyon.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.25-archive-comparison-lyon"
      ],
      "historicalNote": {
        "en": "In Against Heresies, Irenaeus argues for inherited teaching and episcopal succession, using Rome as one example. This is a theological polemic with claims about authority and opponents. It is not an impartial catalogue of every community. The local comparison exercise here is fiction and decides no doctrine.",
        "es-ES": "En Contra las herejías, Ireneo argumenta a favor de la enseñanza heredada y la sucesión episcopal, con Roma como uno de sus ejemplos. Es una polémica teológica con afirmaciones sobre autoridad y adversarios. No es un catálogo imparcial de todas las comunidades. El ejercicio local de comparación es ficticio y no decide doctrina."
      },
      "hint": {
        "en": "Collect both separate groups of three context notes. Deliver the authority group to the western court and the comparison group to the southern yard.",
        "es-ES": "Recoge ambos grupos separados de tres notas de contexto. Entrega el grupo de autoridad en el patio occidental y el de comparación en el meridional."
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

### Two tables’ supply share / La aportación de provisiones de dos mesas

EN: Escort the trader of two tables’ supply share to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de la aportación de provisiones de dos mesas hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A separate finite exchange never reuses either main funding receipt.

ES: Un intercambio separado y finito nunca reutiliza ninguno de los recibos principales.

```json
{
  "id": "side-2",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "25-archive-comparison-lyon.side-2.entity-1"
        ],
        "destinations": {
          "25-archive-comparison-lyon.side-2.entity-1": "25-archive-comparison-lyon.side-2.zone-1"
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
        "receipt": "25-archive-comparison-lyon.side-2.payment",
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
        "id": "25-archive-comparison-lyon.side-2.entity-1",
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
        "id": "25-archive-comparison-lyon.side-2.zone-1",
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
      "onceFlag": "25-archive-comparison-lyon.side-2.rewarded",
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

### The outer-road work store / El almacén de trabajo del camino exterior

EN: Pay 50 wood and restore the damaged store of the outer-road work store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el almacén de trabajo del camino exterior. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Finite supplies support independent teams, not destruction of rival religious buildings.

ES: Los suministros finitos apoyan equipos independientes, no la destrucción de edificios religiosos rivales.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "25-archive-comparison-lyon.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "25-archive-comparison-lyon.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "25-archive-comparison-lyon.side-3.payment",
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
        "id": "25-archive-comparison-lyon.side-3.entity-1",
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
        "id": "25-archive-comparison-lyon.side-3.zone-1",
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
      "onceFlag": "25-archive-comparison-lyon.side-3.rewarded",
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

### Neighbors outside the dispute / Vecinos ajenos a la disputa

EN: Bring each of the two aid crates to its assigned household at neighbors outside the dispute. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en vecinos ajenos a la disputa. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Voluntary separate household aid never depends on accepting a doctrinal position.

ES: La ayuda doméstica voluntaria y separada nunca depende de aceptar una posición doctrinal.

```json
{
  "id": "side-4",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "25-archive-comparison-lyon.side-4.entity-1",
          "25-archive-comparison-lyon.side-4.entity-2"
        ],
        "destinations": {
          "25-archive-comparison-lyon.side-4.entity-1": "25-archive-comparison-lyon.side-4.zone-1",
          "25-archive-comparison-lyon.side-4.entity-2": "25-archive-comparison-lyon.side-4.zone-2"
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
        "id": "25-archive-comparison-lyon.side-4.entity-1",
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
        "id": "25-archive-comparison-lyon.side-4.entity-2",
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
        "id": "25-archive-comparison-lyon.side-4.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "25-archive-comparison-lyon.side-4.zone-2",
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
      "onceFlag": "25-archive-comparison-lyon.side-4.rewarded",
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

### The southern comparison road / El camino meridional de comparación

EN: Scout both marked viewpoints of the southern comparison road. Benefit: Mark the surveyed southern-road land circuit once. All main receivers remain disclosed without this optional task.

ES: Explora los dos miradores señalados de el camino meridional de comparación. Ventaja: Señala una vez el circuito terrestre trazado southern-road. Todos los receptores principales siguen identificados sin esta tarea opcional.

EN: Survey the southern land circuit without opening a hidden archive or authenticating succession.

ES: Reconoce el circuito terrestre meridional sin abrir un archivo oculto ni autenticar sucesiones.

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
          "25-archive-comparison-lyon.side-5.zone-1",
          "25-archive-comparison-lyon.side-5.zone-2"
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
        "id": "25-archive-comparison-lyon.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "25-archive-comparison-lyon.side-5.zone-2",
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
      "onceFlag": "25-archive-comparison-lyon.side-5.rewarded",
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

### The outer hill circuit / El circuito exterior de colinas

EN: Escort the local guide of the outer hill circuit to the marked road junction. Benefit: Mark the surveyed relief land circuit once. All main receivers remain disclosed without this optional task.

ES: Escolta al guía local de el circuito exterior de colinas hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado relief. Todos los receptores principales siguen identificados sin esta tarea opcional.

EN: Marks the graded outer road; cannot merge labels or substitute one delivery for both.

ES: Señala el camino exterior graduado; no fusiona etiquetas ni sustituye dos entregas por una.

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
          "25-archive-comparison-lyon.side-6.entity-1"
        ],
        "destinations": {
          "25-archive-comparison-lyon.side-6.entity-1": "25-archive-comparison-lyon.side-6.zone-1"
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
        "id": "25-archive-comparison-lyon.side-6.entity-1",
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
        "id": "25-archive-comparison-lyon.side-6.zone-1",
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
      "onceFlag": "25-archive-comparison-lyon.side-6.rewarded",
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
      "id": "two-independent-work-crews",
      "optionalObjectives": [
        "side-2",
        "side-3"
      ],
      "costOfOpportunity": "Divide northern and southern preparation teams;120wood40goldmandatorycost stays reserved.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "careful-source-comparison",
      "optionalObjectives": [
        "side-1",
        "side-5"
      ],
      "costOfOpportunity": "Read source context while surveying the southern route; explicit labels survive all derivation and delivery.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "neighbors-and-outer-circuit",
      "optionalObjectives": [
        "side-4",
        "side-6"
      ],
      "costOfOpportunity": "Combine care outside the dispute with outer-road movement; no conversion or doctrinal victory meter.",
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
      "food": 1118,
      "wood": 828,
      "gold": 244,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 120,
      "gold": 40,
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
      "food": 1070,
      "wood": 800,
      "gold": 330,
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
      "food": 1170,
      "wood": 850,
      "gold": 255,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 120,
      "gold": 40,
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
      "food": 1070,
      "wood": 800,
      "gold": 330,
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
      "food": 1223,
      "wood": 873,
      "gold": 267,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 120,
      "gold": 40,
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
      "food": 1070,
      "wood": 800,
      "gold": 330,
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
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.title / always | none | Voices Against the Fragments | Voces frente a los fragmentos |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.fact-intro / intro first | collection-narrator | In Against Heresies, Irenaeus argues for inherited teaching and episcopal succession, using Rome as one example. This is a theological polemic with claims about authority and opponents. It is not an impartial catalogue of every community. The local comparison exercise here is fiction and decides no doctrine. | En Contra las herejías, Ireneo argumenta a favor de la enseñanza heredada y la sucesión episcopal, con Roma como uno de sus ejemplos. Es una polémica teológica con afirmaciones sobre autoridad y adversarios. No es un catálogo imparcial de todas las comunidades. El ejercicio local de comparación es ficticio y no decide doctrina. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.persona-intro / after handover | miriam-archive | I share some of the convictions in these inherited pages. That makes the work harder: I am tempted to give agreement the neatest label and disagreement the smallest shelf. Today I want the labels to show which argument belongs to whom. | Comparto algunas convicciones de estas páginas heredadas. Eso dificulta el trabajo: me tienta darle al acuerdo la etiqueta más limpia y al desacuerdo el estante más pequeño. Hoy quiero que las etiquetas muestren de quién es cada argumento. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.route-help / available from start; repeatable without effect | none | Keep the two fictional argument-note groups separate. Bring three authority-context notes to the western court and three comparison-context notes to the southern yard. Pay 60 wood and 20 gold once at each site. Create one register from each group and its own payment, then send the western register to the northwestern yard and the southern register to the central court. | Mantén separados ambos grupos ficticios de notas. Lleva tres notas de contexto de autoridad al patio occidental y tres de comparación al patio meridional. Paga una vez 60 de madera y 20 de oro en cada lugar. Crea un registro por grupo con su pago propio; envía el occidental al patio noroccidental y el meridional al patio central. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o1-goal / phase-1 active | none | Collect both separate groups of three context notes. Deliver the authority group to the western court and the comparison group to the southern yard. | Recoge ambos grupos separados de tres notas de contexto. Entrega el grupo de autoridad en el patio occidental y el de comparación en el meridional. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o1-receipt / o1 latched once | none | Two distinct labelled input groups reached their own preparation sites. | Dos grupos distintos y etiquetados de entradas llegaron a sus lugares propios de preparación. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o1-reaction / after o1 receipt | miriam-archive | A label records a viewpoint; it does not announce a winner. | Una etiqueta registra una perspectiva; no anuncia un ganador. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o2-goal / phase-2 active | none | Pay 60 wood and 20 gold once at the western court and once at the southern yard. | Paga una vez 60 de madera y 20 de oro en el patio occidental y otra en el meridional. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o2-receipt / o2 latched once | none | Both independent exact payments are recorded; neither can fund both preparations. | Constan ambos pagos exactos independientes; ninguno financia las dos preparaciones. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o2-reaction / after o2 receipt | miriam-archive | The same coin cannot pay for both tables merely because I favor one. | La misma moneda no paga ambas mesas porque yo prefiera una. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o3-goal / phase-3 active | none | Create the authority register from its three notes and western payment, and the comparison register from its three notes and southern payment. | Crea el registro de autoridad con sus tres notas y pago occidental, y el de comparación con sus tres notas y pago meridional. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o3-receipt / o3 latched once | none | Separate input lineage and separate payment receipts produced two registers. | Linajes separados de entradas y recibos separados de pago produjeron dos registros. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o3-reaction / after o3 receipt | miriam-archive | A second register is not a second ancient source. Both belong to this imagined exercise. | Un segundo registro no es una segunda fuente antigua. Ambos pertenecen a este ejercicio imaginado. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o4-goal / phase-4 active | none | Deliver the original authority register to the northwestern yard and the original comparison register to the central court. | Entrega el registro original de autoridad en el patio noroccidental y el original de comparación en el patio central. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o4-receipt / o4 latched once | none | Both separately assigned register deliveries are complete. | Se han completado ambas entregas de registros asignadas por separado. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.o4-reaction / after o4 receipt | miriam-archive | I can preserve both labels without lending my own voice to someone I have never heard. | Puedo conservar ambas etiquetas sin prestar mi voz a alguien a quien nunca he oído. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from the argument’s source margin and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de el margen de fuentes del argumento y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-1-complete / side-1 completed | none | The argument’s source margin completed. Its stated benefit has been granted once. | El margen de fuentes del argumento: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-1-lost / side-1 failed-optional | none | The argument’s source margin is unavailable after the loss of its unique participant or object. The main mission continues. | El margen de fuentes del argumento: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-2-goal / optional list from start | none | Escort the trader of two tables’ supply share to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de la aportación de provisiones de dos mesas hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-2-complete / side-2 completed | none | Two tables’ supply share completed. Its stated benefit has been granted once. | La aportación de provisiones de dos mesas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-2-lost / side-2 failed-optional | none | Two tables’ supply share is unavailable after the loss of its unique participant or object. The main mission continues. | La aportación de provisiones de dos mesas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the outer-road work store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el almacén de trabajo del camino exterior. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-3-complete / side-3 completed | none | The outer-road work store completed. Its stated benefit has been granted once. | El almacén de trabajo del camino exterior: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-3-lost / side-3 failed-optional | none | The outer-road work store is unavailable after the loss of its unique participant or object. The main mission continues. | El almacén de trabajo del camino exterior: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-4-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at neighbors outside the dispute. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en vecinos ajenos a la disputa. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-4-complete / side-4 completed | none | Neighbors outside the dispute completed. Its stated benefit has been granted once. | Vecinos ajenos a la disputa: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-4-lost / side-4 failed-optional | none | Neighbors outside the dispute is unavailable after the loss of its unique participant or object. The main mission continues. | Vecinos ajenos a la disputa: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of the southern comparison road. Benefit: Mark the surveyed southern-road land circuit once. All main receivers remain disclosed without this optional task. | Explora los dos miradores señalados de el camino meridional de comparación. Ventaja: Señala una vez el circuito terrestre trazado southern-road. Todos los receptores principales siguen identificados sin esta tarea opcional. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-5-complete / side-5 completed | none | The southern comparison road completed. Its stated benefit has been granted once. | El camino meridional de comparación: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-5-lost / side-5 failed-optional | none | The southern comparison road is unavailable after the loss of its unique participant or object. The main mission continues. | El camino meridional de comparación: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the outer hill circuit to the marked road junction. Benefit: Mark the surveyed relief land circuit once. All main receivers remain disclosed without this optional task. | Escolta al guía local de el circuito exterior de colinas hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado relief. Todos los receptores principales siguen identificados sin esta tarea opcional. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-6-complete / side-6 completed | none | The outer hill circuit completed. Its stated benefit has been granted once. | El circuito exterior de colinas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.side-6-lost / side-6 failed-optional | none | The outer hill circuit is unavailable after the loss of its unique participant or object. The main mission continues. | El circuito exterior de colinas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.fact-outro / victory first | collection-narrator | Two separate fictional working registers were produced from their own collected notes and delivered to their assigned yards. Their preservation neither authenticates a disputed succession nor proves or refutes the positions of Irenaeus or his opponents. | Se produjeron dos registros ficticios separados a partir de sus propias notas recogidas y se entregaron en sus patios asignados. Conservarlos no autentica una sucesión disputada ni demuestra o refuta las posiciones de Ireneo o sus adversarios. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.persona-outro / after fact-outro | miriam-archive | I have beliefs, and I have responsibilities to the record. I cannot become impartial by pretending to have no faith. I can say where my faith speaks, and where an inherited argument speaks instead. | Tengo creencias y responsabilidades hacia lo escrito. No me vuelvo imparcial fingiendo carecer de fe. Puedo decir dónde habla mi fe y dónde habla, en cambio, un argumento heredado. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.25-archive-comparison-lyon.odyssey.next-episode / after persona-outro | none | Continue with The Advocate's Harbour. This episode does not complete the campaign. | Continúa con El puerto del defensor. Este episodio no termina la campaña. |

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
      "authority notes cannot supply comparison register",
      "western payment cannot fund southern register",
      "one register delivered to both sites cannot replace the other identity",
      "no derivation creates additional payment debit",
      "both registers can stage independently after correct funded creation",
      "no invented opponent voice or neutral endorsement of Irenaeus polemic",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
