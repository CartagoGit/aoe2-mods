# 12. Many Hands in One House

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `12-bounded-community-aid-ephesus` · c. 54–55 CE · 380×380

## Historical frame and fixed outcome

EN: First Corinthians addresses disputes and community practices in Corinth. At 16:8 its author says he will remain in Ephesus. The local supply network in this scenario is fictional; it is not the Corinthian assembly transported to Asia.

ES: Primera a los Corintios aborda disputas y prácticas comunitarias en Corinto. En 16:8 su autor dice que permanecerá en Éfeso. La red local de suministros del escenario es ficticia; no traslada la comunidad corintia a Asia.

EN: The letter provides evidence for its author’s concerns and stated travel plans. The three local recipients and their deliveries are a gameplay reconstruction, not a documented Ephesian relief event.

ES: La carta acredita las preocupaciones de su autor y los planes de viaje que declara. Los tres receptores locales y sus entregas son una reconstrucción jugable, no un auxilio efesio documentado.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 4,
      "episodeId": "12-bounded-community-aid-ephesus",
      "order": 12,
      "selectedSourceUrl": "https://academic.oup.com/book/3544",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=1+Corinthians&version=NRSVUE",
      "passage": "1 Corinthians 1–16: Paul addresses factions, food, lawsuits, worship, gifts, collection and resurrection in a community he addresses as Corinth.",
      "supportedClaim": {
        "en": "1 Corinthians addresses multiple community disputes and practices at Corinth.",
        "es-ES": "1 Corintios aborda diversas disputas y prácticas comunitarias en Corinto."
      },
      "limitations": "Primary letter supports the topics but not the selection's c.54–55 date or Ephesus writing location by itself. OUP abstract is not full-text evidence and should be described only as abstract consulted.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.biblegateway.com/passage/?search=1+Corinthians+16%3A5-9&version=NRSVUE",
      "passage": "1Cor16:5–9;16:8 stated stay at Ephesus",
      "supportedClaim": {
        "en": "The author states he will remain in Ephesus until Pentecost.",
        "es-ES": "El autor declara que permanecerá en Éfeso hasta Pentecostés."
      },
      "limitations": "Direct authorial statement; exact date and archaeological house not established. Source concerns addressed Corinthian community; playable local Ephesian network fictional.",
      "consultationDate": "2026-10-13",
      "status": "consulted directly by architect"
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

EN: Collect six separate provision crates.

ES: Recoge seis cajas distintas de provisiones.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "collected",
      "id": "req-1",
      "entities": [
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-1",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-2",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-3",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-4",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-5",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-6"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Six crate identities collected.

ES: Seis identidades de cajas recogidas.

EN: Count the actual bundles, not the number of times we approach them.

ES: Cuenta los bultos reales, no cuántas veces nos acercamos.

### o2 / phase-2

EN: Deliver crates 1–2 to the southern yard,3–4 inland and 5–6 east. Pay 300 food once:100 for each receiving district.

ES: Entrega las cajas 1–2 al patio del sur,3–4 al interior y 5–6 al este. Paga 300 de alimento una vez:100 por cada barrio receptor.

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
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-1",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-2",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-3",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-4",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-5",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-6"
      ],
      "destinations": {
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-1": "faith-origins.12-bounded-community-aid-ephesus.destination-1",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-2": "faith-origins.12-bounded-community-aid-ephesus.destination-1",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-3": "faith-origins.12-bounded-community-aid-ephesus.destination-2",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-4": "faith-origins.12-bounded-community-aid-ephesus.destination-2",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-5": "faith-origins.12-bounded-community-aid-ephesus.destination-3",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-6": "faith-origins.12-bounded-community-aid-ephesus.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 300
      },
      "id": "req-2",
      "receivingZones": [
        "faith-origins.12-bounded-community-aid-ephesus.destination-1",
        "faith-origins.12-bounded-community-aid-ephesus.destination-2",
        "faith-origins.12-bounded-community-aid-ephesus.destination-3"
      ],
      "allocations": {
        "faith-origins.12-bounded-community-aid-ephesus.destination-1": {
          "food": 100
        },
        "faith-origins.12-bounded-community-aid-ephesus.destination-2": {
          "food": 100
        },
        "faith-origins.12-bounded-community-aid-ephesus.destination-3": {
          "food": 100
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.12-bounded-community-aid-ephesus.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Six assigned arrivals and all three exact allocations recorded.

ES: Seis llegadas asignadas y las tres asignaciones exactas registradas.

EN: Even a full store cannot speak for a household that received nothing.

ES: Ni un almacén lleno puede hablar por un hogar que no recibió nada.

### o3 / phase-3

EN: Compile three fictional receiving notes from the collected crate identities and bring them to the inland district.

ES: Elabora tres notas ficticias de recepción a partir de las cajas recogidas y llévalas al barrio interior.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "derived-token",
      "once": true,
      "requiresInputsCollected": true,
      "id": "req-1",
      "inputEntities": [
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-1",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-2",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-3",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-4",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-5",
        "faith-origins.12-bounded-community-aid-ephesus.provision-crates-6"
      ],
      "outputEntities": [
        "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-1",
        "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-2",
        "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-3"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.12-bounded-community-aid-ephesus.o2.req-2.paid",
          "fromObjective": "o2",
          "amounts": {
            "food": 300
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-1",
        "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-2",
        "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-3"
      ],
      "destinations": {
        "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-1": "faith-origins.12-bounded-community-aid-ephesus.destination-2",
        "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-2": "faith-origins.12-bounded-community-aid-ephesus.destination-2",
        "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-3": "faith-origins.12-bounded-community-aid-ephesus.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three locally derived notes arrived.

ES: Han llegado tres notas derivadas locales.

EN: These are our working notes. I will not pass them off as a lost page of the letter.

ES: Son nuestras notas de trabajo. No las presentaré como una página perdida de la carta.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/12-bounded-community-aid-ephesus.svg)

```json
{
  "bbox": [
    27.255,
    37.875,
    27.405,
    37.995
  ],
  "terrainProfile": "ephesus",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        242.88,
        243.08
      ],
      "lonLat": [
        27.354,
        37.916
      ],
      "name": {
        "en": "Southern provision yard",
        "es-ES": "Patio de provisión del sur"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        251.78,
        144.38
      ],
      "lonLat": [
        27.358,
        37.951
      ],
      "name": {
        "en": "Inland receiving district",
        "es-ES": "Barrio receptor interior"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        307.38,
        90.8
      ],
      "lonLat": [
        27.383,
        37.97
      ],
      "name": {
        "en": "East-road receiving post",
        "es-ES": "Puesto receptor del camino oriental"
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
  "terrainInstructions": "Three fictional inland recipients, land-only dispatch. Do not portray Corinth assembly members as historical Ephesian households. Boundaries follow real regional slopes only after DEM; no modern roads, Celsus facade or later Christian churches.",
  "corridorStraightLengthsTiles": {
    "main": 176.32,
    "relief": 176.32
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
  "schematicWaterControl": null,
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/12-bounded-community-aid-ephesus.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.12-bounded-community-aid-ephesus.provision-crates-1",
      "role": "fictional-local-food-crate",
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
      "id": "faith-origins.12-bounded-community-aid-ephesus.provision-crates-2",
      "role": "fictional-local-food-crate",
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
      "id": "faith-origins.12-bounded-community-aid-ephesus.provision-crates-3",
      "role": "fictional-local-food-crate",
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
      "id": "faith-origins.12-bounded-community-aid-ephesus.provision-crates-4",
      "role": "fictional-local-food-crate",
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
      "id": "faith-origins.12-bounded-community-aid-ephesus.provision-crates-5",
      "role": "fictional-local-food-crate",
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
      "id": "faith-origins.12-bounded-community-aid-ephesus.provision-crates-6",
      "role": "fictional-local-food-crate",
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
      "id": "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-1",
      "role": "fictional-independent-receiving-note",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-2",
      "role": "fictional-independent-receiving-note",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-3",
      "role": "fictional-independent-receiving-note",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.12-bounded-community-aid-ephesus.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.12-bounded-community-aid-ephesus.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.12-bounded-community-aid-ephesus.destination-3",
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
    "provision-crates": [
      "faith-origins.12-bounded-community-aid-ephesus.provision-crates-1",
      "faith-origins.12-bounded-community-aid-ephesus.provision-crates-2",
      "faith-origins.12-bounded-community-aid-ephesus.provision-crates-3",
      "faith-origins.12-bounded-community-aid-ephesus.provision-crates-4",
      "faith-origins.12-bounded-community-aid-ephesus.provision-crates-5",
      "faith-origins.12-bounded-community-aid-ephesus.provision-crates-6"
    ],
    "local-receiving-notes": [
      "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-1",
      "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-2",
      "faith-origins.12-bounded-community-aid-ephesus.local-receiving-notes-3"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Independent labor households / Hogares independientes de trabajadores

EN: Bring each of the two aid crates to its assigned household at independent labor households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes de trabajadores. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Optional aid goes to separate identities, never the three mandatory receivers.

ES: La ayuda opcional corresponde a identidades separadas, nunca a los tres receptores obligatorios.

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
          "12-bounded-community-aid-ephesus.side-1.entity-1",
          "12-bounded-community-aid-ephesus.side-1.entity-2"
        ],
        "destinations": {
          "12-bounded-community-aid-ephesus.side-1.entity-1": "12-bounded-community-aid-ephesus.side-1.zone-1",
          "12-bounded-community-aid-ephesus.side-1.entity-2": "12-bounded-community-aid-ephesus.side-1.zone-2"
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
        "id": "12-bounded-community-aid-ephesus.side-1.entity-1",
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
        "id": "12-bounded-community-aid-ephesus.side-1.entity-2",
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
        "id": "12-bounded-community-aid-ephesus.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "12-bounded-community-aid-ephesus.side-1.zone-2",
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
      "onceFlag": "12-bounded-community-aid-ephesus.side-1.rewarded",
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

### Port-road trader / Comerciante del camino portuario

EN: Escort the trader of port-road trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de comerciante del camino portuario hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One inland exchange avoids making shipping a hidden requirement.

ES: Un intercambio interior evita convertir la navegación en un requisito oculto.

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
          "12-bounded-community-aid-ephesus.side-2.entity-1"
        ],
        "destinations": {
          "12-bounded-community-aid-ephesus.side-2.entity-1": "12-bounded-community-aid-ephesus.side-2.zone-1"
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
        "receipt": "12-bounded-community-aid-ephesus.side-2.payment",
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
        "id": "12-bounded-community-aid-ephesus.side-2.entity-1",
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
        "id": "12-bounded-community-aid-ephesus.side-2.zone-1",
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
      "onceFlag": "12-bounded-community-aid-ephesus.side-2.rewarded",
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

### Terrace junction guide / Guía del cruce entre terrazas

EN: Escort the local guide of terrace junction guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task.

ES: Escolta al guía local de guía del cruce entre terrazas hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea.

EN: A surveyed local route supports multi-post scheduling.

ES: Una ruta local comprobada apoya la planificación entre puestos.

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
          "12-bounded-community-aid-ephesus.side-3.entity-1"
        ],
        "destinations": {
          "12-bounded-community-aid-ephesus.side-3.entity-1": "12-bounded-community-aid-ephesus.side-3.zone-1"
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
        "id": "12-bounded-community-aid-ephesus.side-3.entity-1",
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
        "id": "12-bounded-community-aid-ephesus.side-3.zone-1",
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
      "onceFlag": "12-bounded-community-aid-ephesus.side-3.rewarded",
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

### Separate provision lists / Listas separadas de provisión

EN: Recover both separate copies from separate provision lists and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de listas separadas de provisión y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Contemporary fictional lists unlock letter context without becoming canonical objects.

ES: Las listas contemporáneas ficticias desbloquean contexto de la carta sin convertirse en objetos canónicos.

```json
{
  "id": "side-4",
  "kind": "copy",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "12-bounded-community-aid-ephesus.side-4.entity-1",
          "12-bounded-community-aid-ephesus.side-4.entity-2"
        ],
        "destinations": {
          "12-bounded-community-aid-ephesus.side-4.entity-1": "12-bounded-community-aid-ephesus.side-4.zone-1",
          "12-bounded-community-aid-ephesus.side-4.entity-2": "12-bounded-community-aid-ephesus.side-4.zone-1"
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
        "id": "12-bounded-community-aid-ephesus.side-4.entity-1",
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
        "id": "12-bounded-community-aid-ephesus.side-4.entity-2",
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
        "id": "12-bounded-community-aid-ephesus.side-4.zone-1",
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
      "onceFlag": "12-bounded-community-aid-ephesus.side-4.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.12-bounded-community-aid-ephesus"
      ],
      "historicalNote": {
        "en": "First Corinthians addresses disputes and community practices in Corinth. At 16:8 its author says he will remain in Ephesus. The local supply network in this scenario is fictional; it is not the Corinthian assembly transported to Asia.",
        "es-ES": "Primera a los Corintios aborda disputas y prácticas comunitarias en Corinto. En 16:8 su autor dice que permanecerá en Éfeso. La red local de suministros del escenario es ficticia; no traslada la comunidad corintia a Asia."
      },
      "hint": {
        "en": "Collect six separate provision crates.",
        "es-ES": "Recoge seis cajas distintas de provisiones."
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

### Common store shelter / Cobertizo del almacén común

EN: Pay 50 wood and restore the damaged store of common store shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de cobertizo del almacén común. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair has its own one-time charge separate from main 300 food.

ES: La reparación tiene su propio cobro único, separado de los 300 de alimento principales.

```json
{
  "id": "side-5",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "12-bounded-community-aid-ephesus.side-5.entity-1",
        "health": "full",
        "paymentReceipt": "12-bounded-community-aid-ephesus.side-5.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "12-bounded-community-aid-ephesus.side-5.payment",
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
        "id": "12-bounded-community-aid-ephesus.side-5.entity-1",
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
        "id": "12-bounded-community-aid-ephesus.side-5.zone-1",
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
      "onceFlag": "12-bounded-community-aid-ephesus.side-5.rewarded",
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

### Voluntary hill-road travelers / Viajeros voluntarios del camino alto

EN: Bring both voluntary evacuee groups from voluntary hill-road travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de viajeros voluntarios del camino alto al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Travelers may be helped independently of supply completion.

ES: Se puede ayudar a los viajeros con independencia de la provisión principal.

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
          "12-bounded-community-aid-ephesus.side-6.entity-1",
          "12-bounded-community-aid-ephesus.side-6.entity-2"
        ],
        "destinations": {
          "12-bounded-community-aid-ephesus.side-6.entity-1": "12-bounded-community-aid-ephesus.side-6.zone-1",
          "12-bounded-community-aid-ephesus.side-6.entity-2": "12-bounded-community-aid-ephesus.side-6.zone-1"
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
        "id": "12-bounded-community-aid-ephesus.side-6.entity-1",
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
        "id": "12-bounded-community-aid-ephesus.side-6.entity-2",
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
        "id": "12-bounded-community-aid-ephesus.side-6.zone-1",
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
      "onceFlag": "12-bounded-community-aid-ephesus.side-6.rewarded",
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
      "id": "district-scheduling",
      "optionalObjectives": [
        "side-2",
        "side-3"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Divide three receiver circuits among transport teams; spend optional50gold only after reserving main provisions."
    },
    {
      "id": "records-before-reward",
      "optionalObjectives": [
        "side-4",
        "side-5"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Use context and one paid repair detour while mandatory deliveries proceed."
    },
    {
      "id": "neighbor-care",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Help independent households/travelers; the main third receiver remains mandatory even with abundant optional aid."
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
      "wood": 708,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
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
      "food": 1370,
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
      "wood": 730,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
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
      "food": 1370,
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
      "wood": 753,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
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
      "food": 1370,
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
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.title / always | none | Many Hands in One House | Muchas manos en una casa |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.fact-intro / intro first | collection-narrator | First Corinthians addresses disputes and community practices in Corinth. At 16:8 its author says he will remain in Ephesus. The local supply network in this scenario is fictional; it is not the Corinthian assembly transported to Asia. | Primera a los Corintios aborda disputas y prácticas comunitarias en Corinto. En 16:8 su autor dice que permanecerá en Éfeso. La red local de suministros del escenario es ficticia; no traslada la comunidad corintia a Asia. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.persona-intro / after handover | miriam-archive | In my archive, a generous promise meant little until we knew who received the bread. I read these arguments with that memory beside me, without pretending I heard them spoken. | En mi archivo, una promesa generosa significaba poco hasta saber quién había recibido el pan. Leo estos argumentos con ese recuerdo cerca, sin fingir que los oí pronunciar. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.route-help / available from start; repeatable without effect | none | Each crate has one assigned receiving district. Delivering all crates to one place cannot complete the task. Keep every route on the inland side of the proposed harbor. | Cada caja tiene un barrio receptor asignado. Llevarlas todas a un lugar no completa la tarea. Mantén todas las rutas al interior del puerto propuesto. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.o1-goal / phase-1 active | none | Collect six separate provision crates. | Recoge seis cajas distintas de provisiones. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.o1-receipt / o1 latched once | none | Six crate identities collected. | Seis identidades de cajas recogidas. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.o1-reaction / after o1 receipt | miriam-archive | Count the actual bundles, not the number of times we approach them. | Cuenta los bultos reales, no cuántas veces nos acercamos. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.o2-goal / phase-2 active | none | Deliver crates 1–2 to the southern yard,3–4 inland and 5–6 east. Pay 300 food once:100 for each receiving district. | Entrega las cajas 1–2 al patio del sur,3–4 al interior y 5–6 al este. Paga 300 de alimento una vez:100 por cada barrio receptor. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.o2-receipt / o2 latched once | none | Six assigned arrivals and all three exact allocations recorded. | Seis llegadas asignadas y las tres asignaciones exactas registradas. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.o2-reaction / after o2 receipt | miriam-archive | Even a full store cannot speak for a household that received nothing. | Ni un almacén lleno puede hablar por un hogar que no recibió nada. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.o3-goal / phase-3 active | none | Compile three fictional receiving notes from the collected crate identities and bring them to the inland district. | Elabora tres notas ficticias de recepción a partir de las cajas recogidas y llévalas al barrio interior. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.o3-receipt / o3 latched once | none | Three locally derived notes arrived. | Han llegado tres notas derivadas locales. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.o3-reaction / after o3 receipt | miriam-archive | These are our working notes. I will not pass them off as a lost page of the letter. | Son nuestras notas de trabajo. No las presentaré como una página perdida de la carta. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at independent labor households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes de trabajadores. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-1-complete / side-1 completed | none | Independent labor households completed. Its stated benefit has been granted once. | Hogares independientes de trabajadores: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-1-lost / side-1 failed-optional | none | Independent labor households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares independientes de trabajadores: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-2-goal / optional list from start | none | Escort the trader of port-road trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de comerciante del camino portuario hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-2-complete / side-2 completed | none | Port-road trader completed. Its stated benefit has been granted once. | Comerciante del camino portuario: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-2-lost / side-2 failed-optional | none | Port-road trader is unavailable after the loss of its unique participant or object. The main mission continues. | Comerciante del camino portuario: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-3-goal / optional list from start | none | Escort the local guide of terrace junction guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task. | Escolta al guía local de guía del cruce entre terrazas hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-3-complete / side-3 completed | none | Terrace junction guide completed. Its stated benefit has been granted once. | Guía del cruce entre terrazas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-3-lost / side-3 failed-optional | none | Terrace junction guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del cruce entre terrazas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-4-goal / optional list from start | none | Recover both separate copies from separate provision lists and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de listas separadas de provisión y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-4-complete / side-4 completed | none | Separate provision lists completed. Its stated benefit has been granted once. | Listas separadas de provisión: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-4-lost / side-4 failed-optional | none | Separate provision lists is unavailable after the loss of its unique participant or object. The main mission continues. | Listas separadas de provisión: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-5-goal / optional list from start | none | Pay 50 wood and restore the damaged store of common store shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de cobertizo del almacén común. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-5-complete / side-5 completed | none | Common store shelter completed. Its stated benefit has been granted once. | Cobertizo del almacén común: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-5-lost / side-5 failed-optional | none | Common store shelter is unavailable after the loss of its unique participant or object. The main mission continues. | Cobertizo del almacén común: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from voluntary hill-road travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de viajeros voluntarios del camino alto al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-6-complete / side-6 completed | none | Voluntary hill-road travelers completed. Its stated benefit has been granted once. | Viajeros voluntarios del camino alto: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.side-6-lost / side-6 failed-optional | none | Voluntary hill-road travelers is unavailable after the loss of its unique participant or object. The main mission continues. | Viajeros voluntarios del camino alto: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.fact-outro / victory first | collection-narrator | The letter provides evidence for its author’s concerns and stated travel plans. The three local recipients and their deliveries are a gameplay reconstruction, not a documented Ephesian relief event. | La carta acredita las preocupaciones de su autor y los planes de viaje que declara. Los tres receptores locales y sus entregas son una reconstrucción jugable, no un auxilio efesio documentado. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.persona-outro / after fact-outro | miriam-archive | No household should disappear into a total. I have kept three names in our invented ledger; the letter’s argument remains its own. | Ningún hogar debería desaparecer dentro de un total. He conservado tres nombres en nuestro registro inventado; la argumentación de la carta sigue siendo la suya. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.12-bounded-community-aid-ephesus.odyssey.next-episode / after persona-outro | none | Continue with Words for a Distant City. This episode does not complete the campaign. | Continúa con Palabras para una ciudad lejana. Este episodio no termina la campaña. |

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
      "one receiver cannot substitute for all three",
      "same crate repeated never fulfills another assigned receiver",
      "exact100food each;300paid to one yard invalid",
      "FirstCor letter context remains Corinth; playable households remain fictional Ephesus",
      "hub1 pickup outside receiving zone must be physically moved",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
