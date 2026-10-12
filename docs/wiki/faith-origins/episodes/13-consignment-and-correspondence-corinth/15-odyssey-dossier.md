# 13. Words for a Distant City

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `13-consignment-and-correspondence-corinth` · c. 56–58 CE · 400×400

## Historical frame and fixed outcome

EN: Romans commends Phoebe in connection with the community at Cenchreae and addresses people in Rome. Corinth around 56–58 is a conventional composition reconstruction, not a location stated by the letter. The consignment and its carriers here are fictional.

ES: Romanos recomienda a Febe vinculándola con la comunidad de Céncreas y se dirige a personas de Roma. Corinto hacia 56–58 es una reconstrucción habitual de su composición, no un lugar indicado por la carta. La remesa y sus portadores son ficticios.

EN: The local consignment ends at the Cenchreae approach. Rome and Jerusalem remain off-map. This fictional departure neither proves Phoebe carried Romans nor establishes an ancient ship or writing address.

ES: La remesa local termina en el acceso a Céncreas. Roma y Jerusalén quedan fuera del mapa. Esta salida ficticia no demuestra que Febe transportara Romanos ni identifica una nave o dirección de escritura antiguas.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 5,
      "episodeId": "13-consignment-and-correspondence-corinth",
      "order": 13,
      "selectedSourceUrl": "https://academic.oup.com/book/3544",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Romans+16&version=NRSVUE",
      "passage": "Romans 16: Paul commends Phoebe of Cenchreae, greets multiple named people, and mentions a house-church; Romans 1:13 says Paul had often intended to visit Rome.",
      "supportedClaim": {
        "en": "Romans 16 attests a network of people and communities in Rome and Phoebe's connection to Cenchreae; Paul says he had not yet visited Rome.",
        "es-ES": "Romanos 16 acredita una red de personas y comunidades en Roma y el vínculo de Febe con Cencreas; Pablo dice que aún no había visitado Roma."
      },
      "limitations": "It does not itself give composition date/place. Corinth is a scholarly inference; the dossier's Oxford source was an abstract only. The claim 'community he did not found' is supported by Romans 1:13, not chapter 16 alone.",
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

EN: Collect three consignments and assemble all three carriers alive at the east-road yard.

ES: Recoge tres remesas y reúne con vida a los tres portadores en el patio del camino oriental.

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
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-1",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-2",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-1",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-2",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-3"
      ],
      "destinations": {
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-1": "faith-origins.13-consignment-and-correspondence-corinth.destination-2",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-2": "faith-origins.13-consignment-and-correspondence-corinth.destination-2",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-3": "faith-origins.13-consignment-and-correspondence-corinth.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true,
  "exportedLedgers": [
    {
      "id": "staged-carriers",
      "operator": "intersection",
      "fromRequirements": [
        "req-2"
      ],
      "minimumCount": 3
    }
  ]
}
```

EN: Three consignments collected and three distinct carriers staged.

ES: Tres remesas recogidas y tres portadores distintos preparados.

EN: They are invented carriers, not historical people borrowed to fill a unit list.

ES: Son portadores inventados, no personas históricas prestadas para llenar una lista de unidades.

### o2 / phase-2

EN: Deliver all three consignments to the staging yard and pay 240 food and 60 wood once for onward provisioning.

ES: Entrega las tres remesas en el patio de preparación y paga una sola vez 240 de alimento y 60 de madera para provisiones de salida.

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
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-1",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-2",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-3"
      ],
      "destinations": {
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-1": "faith-origins.13-consignment-and-correspondence-corinth.destination-2",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-2": "faith-origins.13-consignment-and-correspondence-corinth.destination-2",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-3": "faith-origins.13-consignment-and-correspondence-corinth.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 240,
        "wood": 60
      },
      "id": "req-2",
      "receivingZones": [
        "faith-origins.13-consignment-and-correspondence-corinth.destination-2"
      ],
      "allocations": {
        "faith-origins.13-consignment-and-correspondence-corinth.destination-2": {
          "food": 240,
          "wood": 60
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.13-consignment-and-correspondence-corinth.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three original consignment arrivals and one exact provisioning receipt recorded.

ES: Tres llegadas de remesas originales y un recibo exacto de provisión registrados.

EN: A promise of passage is not yet an arrival. Keep the difference clear.

ES: Una promesa de paso aún no es una llegada. Conserva clara la diferencia.

### o3 / phase-3

EN: Bring the same three staged carriers, the three consignments and both local journey notes to the inland Cenchreae departure yard.

ES: Lleva los mismos tres portadores preparados, las tres remesas y ambas notas locales de viaje al patio interior de salida de Céncreas.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o1",
        "ledger": "staged-carriers"
      },
      "id": "req-1",
      "entities": [
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-1",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-2",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-3"
      ],
      "destinations": {
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-1": "faith-origins.13-consignment-and-correspondence-corinth.destination-3",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-2": "faith-origins.13-consignment-and-correspondence-corinth.destination-3",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-3": "faith-origins.13-consignment-and-correspondence-corinth.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-1",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-2",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-3"
      ],
      "destinations": {
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-1": "faith-origins.13-consignment-and-correspondence-corinth.destination-3",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-2": "faith-origins.13-consignment-and-correspondence-corinth.destination-3",
        "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-3": "faith-origins.13-consignment-and-correspondence-corinth.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-1",
        "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-1",
        "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-2"
      ],
      "destinations": {
        "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-1": "faith-origins.13-consignment-and-correspondence-corinth.destination-3",
        "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-2": "faith-origins.13-consignment-and-correspondence-corinth.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The same carriers, original consignments and two notes reached the local departure district.

ES: Los mismos portadores, las remesas originales y dos notas han llegado al barrio local de salida.

EN: The horizon is not a receipt for a voyage we have not shown.

ES: El horizonte no es un recibo de una travesía que no hemos mostrado.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/13-consignment-and-correspondence-corinth.svg)

```json
{
  "bbox": [
    22.83,
    37.875,
    23.065,
    37.975
  ],
  "terrainProfile": "corinth",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        109.3,
        228.33
      ],
      "lonLat": [
        22.888,
        37.91
      ],
      "name": {
        "en": "Old-city dispatch court",
        "es-ES": "Patio de salida de la ciudad antigua"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        218.45,
        241.78
      ],
      "lonLat": [
        22.96,
        37.903
      ],
      "name": {
        "en": "East-road staging yard",
        "es-ES": "Patio de preparación del camino oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        268.48,
        268.69
      ],
      "lonLat": [
        22.993,
        37.889
      ],
      "name": {
        "en": "Cenchreae inland departure yard",
        "es-ES": "Patio interior de salida de Céncreas"
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
  "terrainInstructions": "Old city southwest of isthmus, eastern road toward Cenchreae on Saronic Gulf. Final yard inland northwest of shoreline, never over water. Do not put Rome, Jerusalem or Delphi inside this regional map. No modern canal or claim to know first-century pier shape.",
  "mainRouteLengthStraightTiles": 166.78,
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
  "asset": "docs/design/maps/faith-origins/odyssey/13-consignment-and-correspondence-corinth.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-1",
      "role": "fictional-independent-local-consignment",
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
      "id": "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-2",
      "role": "fictional-independent-local-consignment",
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
      "id": "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-3",
      "role": "fictional-independent-local-consignment",
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
      "id": "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-1",
      "role": "fictional-independent-consignment-carrier",
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
      "id": "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-2",
      "role": "fictional-independent-consignment-carrier",
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
      "id": "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-3",
      "role": "fictional-independent-consignment-carrier",
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
      "id": "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-1",
      "role": "fictional-contemporary-journey-note",
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
      "id": "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-2",
      "role": "fictional-contemporary-journey-note",
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
    }
  ],
  "zones": [
    {
      "id": "faith-origins.13-consignment-and-correspondence-corinth.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.13-consignment-and-correspondence-corinth.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.13-consignment-and-correspondence-corinth.destination-3",
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
    "local-consignments": [
      "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-1",
      "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-2",
      "faith-origins.13-consignment-and-correspondence-corinth.local-consignments-3"
    ],
    "dispatch-carriers": [
      "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-1",
      "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-2",
      "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-3"
    ],
    "journey-notes": [
      "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-1",
      "faith-origins.13-consignment-and-correspondence-corinth.journey-notes-2"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-1",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-2",
        "faith-origins.13-consignment-and-correspondence-corinth.dispatch-carriers-3"
      ],
      "minimumAliveOrAlreadySafe": 3
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Eastern road guide / Guía del camino oriental

EN: Escort the local guide of eastern road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía del camino oriental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: Marks a land approach to Cenchreae, not a journey through the Saronic Gulf.

ES: Señala una aproximación terrestre a Céncreas, no una travesía por el golfo Sarónico.

```json
{
  "id": "side-1",
  "kind": "guide",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "13-consignment-and-correspondence-corinth.side-1.entity-1"
        ],
        "destinations": {
          "13-consignment-and-correspondence-corinth.side-1.entity-1": "13-consignment-and-correspondence-corinth.side-1.zone-1"
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
        "id": "13-consignment-and-correspondence-corinth.side-1.entity-1",
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
        "id": "13-consignment-and-correspondence-corinth.side-1.zone-1",
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
      "onceFlag": "13-consignment-and-correspondence-corinth.side-1.rewarded",
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

### Port provision seller / Vendedor de provisiones portuarias

EN: Escort the trader of port provision seller to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de vendedor de provisiones portuarias hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One separate fictional trader supplies finite reserves.

ES: Un comerciante ficticio separado aporta reservas finitas.

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
          "13-consignment-and-correspondence-corinth.side-2.entity-1"
        ],
        "destinations": {
          "13-consignment-and-correspondence-corinth.side-2.entity-1": "13-consignment-and-correspondence-corinth.side-2.zone-1"
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
        "receipt": "13-consignment-and-correspondence-corinth.side-2.payment",
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
        "id": "13-consignment-and-correspondence-corinth.side-2.entity-1",
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
        "id": "13-consignment-and-correspondence-corinth.side-2.zone-1",
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
      "onceFlag": "13-consignment-and-correspondence-corinth.side-2.rewarded",
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

### Hospitality slips / Notas de hospitalidad

EN: Recover both separate copies from hospitality slips and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de notas de hospitalidad y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Contemporary fictional slips unlock context about attributed networks.

ES: Notas contemporáneas ficticias desbloquean contexto sobre redes atribuidas.

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
          "13-consignment-and-correspondence-corinth.side-3.entity-1",
          "13-consignment-and-correspondence-corinth.side-3.entity-2"
        ],
        "destinations": {
          "13-consignment-and-correspondence-corinth.side-3.entity-1": "13-consignment-and-correspondence-corinth.side-3.zone-1",
          "13-consignment-and-correspondence-corinth.side-3.entity-2": "13-consignment-and-correspondence-corinth.side-3.zone-1"
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
        "id": "13-consignment-and-correspondence-corinth.side-3.entity-1",
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
        "id": "13-consignment-and-correspondence-corinth.side-3.entity-2",
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
        "id": "13-consignment-and-correspondence-corinth.side-3.zone-1",
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
      "onceFlag": "13-consignment-and-correspondence-corinth.side-3.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.13-consignment-and-correspondence-corinth"
      ],
      "historicalNote": {
        "en": "Romans commends Phoebe in connection with the community at Cenchreae and addresses people in Rome. Corinth around 56–58 is a conventional composition reconstruction, not a location stated by the letter. The consignment and its carriers here are fictional.",
        "es-ES": "Romanos recomienda a Febe vinculándola con la comunidad de Céncreas y se dirige a personas de Roma. Corinto hacia 56–58 es una reconstrucción habitual de su composición, no un lugar indicado por la carta. La remesa y sus portadores son ficticios."
      },
      "hint": {
        "en": "Collect three consignments and assemble all three carriers alive at the east-road yard.",
        "es-ES": "Recoge tres remesas y reúne con vida a los tres portadores en el patio del camino oriental."
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

### Roadside port households / Hogares del camino portuario

EN: Bring each of the two aid crates to its assigned household at roadside port households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del camino portuario. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid recipients remain distinct from main carriers.

ES: Los receptores de ayuda siguen siendo distintos de los portadores principales.

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
          "13-consignment-and-correspondence-corinth.side-4.entity-1",
          "13-consignment-and-correspondence-corinth.side-4.entity-2"
        ],
        "destinations": {
          "13-consignment-and-correspondence-corinth.side-4.entity-1": "13-consignment-and-correspondence-corinth.side-4.zone-1",
          "13-consignment-and-correspondence-corinth.side-4.entity-2": "13-consignment-and-correspondence-corinth.side-4.zone-2"
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
        "id": "13-consignment-and-correspondence-corinth.side-4.entity-1",
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
        "id": "13-consignment-and-correspondence-corinth.side-4.entity-2",
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
        "id": "13-consignment-and-correspondence-corinth.side-4.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "13-consignment-and-correspondence-corinth.side-4.zone-2",
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
      "onceFlag": "13-consignment-and-correspondence-corinth.side-4.rewarded",
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

### Independent departure families / Familias independientes de salida

EN: Bring both voluntary evacuee groups from independent departure families to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de familias independientes de salida al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Two optional groups do not count among main dispatch carriers.

ES: Dos grupos opcionales no cuentan como portadores principales.

```json
{
  "id": "side-5",
  "kind": "extract",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "13-consignment-and-correspondence-corinth.side-5.entity-1",
          "13-consignment-and-correspondence-corinth.side-5.entity-2"
        ],
        "destinations": {
          "13-consignment-and-correspondence-corinth.side-5.entity-1": "13-consignment-and-correspondence-corinth.side-5.zone-1",
          "13-consignment-and-correspondence-corinth.side-5.entity-2": "13-consignment-and-correspondence-corinth.side-5.zone-1"
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
        "id": "13-consignment-and-correspondence-corinth.side-5.entity-1",
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
        "id": "13-consignment-and-correspondence-corinth.side-5.entity-2",
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
        "id": "13-consignment-and-correspondence-corinth.side-5.zone-1",
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
      "onceFlag": "13-consignment-and-correspondence-corinth.side-5.rewarded",
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

### Inland port store / Almacén portuario interior

EN: Pay 50 wood and restore the damaged store of inland port store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén portuario interior. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A repaired store does not recreate an ancient excavated wharf.

ES: Un almacén reparado no recrea un muelle antiguo excavado.

```json
{
  "id": "side-6",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "13-consignment-and-correspondence-corinth.side-6.entity-1",
        "health": "full",
        "paymentReceipt": "13-consignment-and-correspondence-corinth.side-6.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "13-consignment-and-correspondence-corinth.side-6.payment",
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
        "id": "13-consignment-and-correspondence-corinth.side-6.entity-1",
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
        "id": "13-consignment-and-correspondence-corinth.side-6.zone-1",
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
      "onceFlag": "13-consignment-and-correspondence-corinth.side-6.rewarded",
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
      "id": "careful-caravan",
      "optionalObjectives": [
        "side-1",
        "side-3"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Scout dispatch context and land route before moving staged carrier identities onward."
    },
    {
      "id": "merchant-reserve",
      "optionalObjectives": [
        "side-2",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Choose bounded50gold/50wood investment while keeping240food/60wood main debit available."
    },
    {
      "id": "shared-departure",
      "optionalObjectives": [
        "side-4",
        "side-5"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Help independent households and families along the east-road approach without changing main cargo identity."
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
      "food": 1458,
      "wood": 768,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
      "wood": 60,
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
      "food": 1310,
      "wood": 740,
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
      "food": 1510,
      "wood": 790,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
      "wood": 60,
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
      "food": 1310,
      "wood": 740,
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
      "food": 1563,
      "wood": 813,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
      "wood": 60,
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
      "food": 1310,
      "wood": 740,
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
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.title / always | none | Words for a Distant City | Palabras para una ciudad lejana |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.fact-intro / intro first | collection-narrator | Romans commends Phoebe in connection with the community at Cenchreae and addresses people in Rome. Corinth around 56–58 is a conventional composition reconstruction, not a location stated by the letter. The consignment and its carriers here are fictional. | Romanos recomienda a Febe vinculándola con la comunidad de Céncreas y se dirige a personas de Roma. Corinto hacia 56–58 es una reconstrucción habitual de su composición, no un lugar indicado por la carta. La remesa y sus portadores son ficticios. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.persona-intro / after handover | miriam-archive | Some names survived because someone bothered to write them in a greeting. I have always loved those small margins of an archive. They also remind me how much was never written down. | Algunos nombres sobrevivieron porque alguien se molestó en escribirlos en un saludo. Siempre he querido esos pequeños márgenes del archivo. También me recuerdan cuánto nunca llegó a escribirse. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.route-help / available from start; repeatable without effect | none | This is an inland route from the old-city region toward Cenchreae. The subsequent sea journey stays off-map. Cargo and carriers are tracked separately; neither substitutes for the other. | Es una ruta terrestre desde la región de la ciudad antigua hacia Céncreas. La travesía posterior queda fuera del mapa. Se registran carga y portadores por separado; ninguno sustituye al otro. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.o1-goal / phase-1 active | none | Collect three consignments and assemble all three carriers alive at the east-road yard. | Recoge tres remesas y reúne con vida a los tres portadores en el patio del camino oriental. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.o1-receipt / o1 latched once | none | Three consignments collected and three distinct carriers staged. | Tres remesas recogidas y tres portadores distintos preparados. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.o1-reaction / after o1 receipt | miriam-archive | They are invented carriers, not historical people borrowed to fill a unit list. | Son portadores inventados, no personas históricas prestadas para llenar una lista de unidades. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.o2-goal / phase-2 active | none | Deliver all three consignments to the staging yard and pay 240 food and 60 wood once for onward provisioning. | Entrega las tres remesas en el patio de preparación y paga una sola vez 240 de alimento y 60 de madera para provisiones de salida. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.o2-receipt / o2 latched once | none | Three original consignment arrivals and one exact provisioning receipt recorded. | Tres llegadas de remesas originales y un recibo exacto de provisión registrados. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.o2-reaction / after o2 receipt | miriam-archive | A promise of passage is not yet an arrival. Keep the difference clear. | Una promesa de paso aún no es una llegada. Conserva clara la diferencia. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.o3-goal / phase-3 active | none | Bring the same three staged carriers, the three consignments and both local journey notes to the inland Cenchreae departure yard. | Lleva los mismos tres portadores preparados, las tres remesas y ambas notas locales de viaje al patio interior de salida de Céncreas. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.o3-receipt / o3 latched once | none | The same carriers, original consignments and two notes reached the local departure district. | Los mismos portadores, las remesas originales y dos notas han llegado al barrio local de salida. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.o3-reaction / after o3 receipt | miriam-archive | The horizon is not a receipt for a voyage we have not shown. | El horizonte no es un recibo de una travesía que no hemos mostrado. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-1-goal / optional list from start | none | Escort the local guide of eastern road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía del camino oriental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-1-complete / side-1 completed | none | Eastern road guide completed. Its stated benefit has been granted once. | Guía del camino oriental: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-1-lost / side-1 failed-optional | none | Eastern road guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del camino oriental: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-2-goal / optional list from start | none | Escort the trader of port provision seller to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de vendedor de provisiones portuarias hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-2-complete / side-2 completed | none | Port provision seller completed. Its stated benefit has been granted once. | Vendedor de provisiones portuarias: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-2-lost / side-2 failed-optional | none | Port provision seller is unavailable after the loss of its unique participant or object. The main mission continues. | Vendedor de provisiones portuarias: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-3-goal / optional list from start | none | Recover both separate copies from hospitality slips and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de notas de hospitalidad y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-3-complete / side-3 completed | none | Hospitality slips completed. Its stated benefit has been granted once. | Notas de hospitalidad: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-3-lost / side-3 failed-optional | none | Hospitality slips is unavailable after the loss of its unique participant or object. The main mission continues. | Notas de hospitalidad: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-4-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at roadside port households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del camino portuario. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-4-complete / side-4 completed | none | Roadside port households completed. Its stated benefit has been granted once. | Hogares del camino portuario: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-4-lost / side-4 failed-optional | none | Roadside port households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares del camino portuario: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-5-goal / optional list from start | none | Bring both voluntary evacuee groups from independent departure families to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de familias independientes de salida al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-5-complete / side-5 completed | none | Independent departure families completed. Its stated benefit has been granted once. | Familias independientes de salida: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-5-lost / side-5 failed-optional | none | Independent departure families is unavailable after the loss of its unique participant or object. The main mission continues. | Familias independientes de salida: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-6-goal / optional list from start | none | Pay 50 wood and restore the damaged store of inland port store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén portuario interior. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-6-complete / side-6 completed | none | Inland port store completed. Its stated benefit has been granted once. | Almacén portuario interior: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.side-6-lost / side-6 failed-optional | none | Inland port store is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén portuario interior: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.fact-outro / victory first | collection-narrator | The local consignment ends at the Cenchreae approach. Rome and Jerusalem remain off-map. This fictional departure neither proves Phoebe carried Romans nor establishes an ancient ship or writing address. | La remesa local termina en el acceso a Céncreas. Roma y Jerusalén quedan fuera del mapa. Esta salida ficticia no demuestra que Febe transportara Romanos ni identifica una nave o dirección de escritura antiguas. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.persona-outro / after fact-outro | miriam-archive | I can name the destination in a letter without claiming I stood upon its quay. Let that modest distance remain between my voice and the lives I inherited. | Puedo nombrar el destino de una carta sin afirmar que estuve en su muelle. Conservemos esa distancia modesta entre mi voz y las vidas que heredé. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.13-consignment-and-correspondence-corinth.odyssey.next-episode / after persona-outro | none | Continue with The Appeal Beside the Sea. This episode does not complete the campaign. | Continúa con La apelación junto al mar. Este episodio no termina la campaña. |

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
      "same original carriers must reach departure",
      "cargo without carriers or carriers without cargo cannot win",
      "no inventory attachment claim until capability implemented",
      "journey notes fictional, not Romans autograph",
      "departureyard must be land northwest of shore",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
