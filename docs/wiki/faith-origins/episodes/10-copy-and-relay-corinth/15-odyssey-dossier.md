# 10. Before the First Letter Faded

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `10-copy-and-relay-corinth` · c. 50–51 CE · 360×360

## Historical frame and fixed outcome

EN: First Thessalonians names Paul, Silvanus and Timothy and describes news from Thessalonica. Its writing place is not stated. The Corinth setting and date around 50–51 are a reconstruction, and the relay participants here are fictional.

ES: Primera a los Tesalonicenses nombra a Pablo, Silvano y Timoteo y describe noticias de Tesalónica. No indica dónde se escribió. La ambientación en Corinto y la fecha hacia 50–51 son una reconstrucción; los participantes del relevo son ficticios.

EN: The letter preserves a network of correspondence and concern. This reconstructed local relay does not prove a Corinthian writing address or make its fictional notes part of the surviving letter.

ES: La carta conserva una red de correspondencia y preocupación. Este relevo local reconstruido no demuestra una dirección de escritura en Corinto ni incorpora sus notas ficticias a la carta conservada.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 2,
      "episodeId": "10-copy-and-relay-corinth",
      "order": 10,
      "selectedSourceUrl": "https://academic.oup.com/book/3544",
      "consultedUrl": "https://citer.ucp.pt/sites/default/files/2024-03/citer-catedra-abravanel-de-gois-amy-jill-levine-and-marc-zvi-brettler-the-jewish-annotated-new-testament.pdf",
      "passage": "Jewish Annotated New Testament introduction to 1 Thessalonians: dates ca. 50 CE and calls it earliest extant Pauline writing; contrast primary letter itself.",
      "supportedClaim": {
        "en": "1 Thessalonians is commonly dated around 50 CE and is the earliest surviving Pauline letter.",
        "es-ES": "1 Tesalonicenses suele fecharse hacia el año 50 y es la carta paulina conservada más antigua."
      },
      "limitations": "The source is scholarly commentary; this supports conventional date/order, not that the letter was written in Corinth. The dossier's OUP source was only an abstract and should not be represented as full-book consultation.",
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

EN: Collect two separate local news notes and take both to the copy yard.

ES: Recoge dos notas locales distintas y lleva ambas al patio de copias.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-1",
      "entities": [
        "faith-origins.10-copy-and-relay-corinth.local-news-notes-1",
        "faith-origins.10-copy-and-relay-corinth.local-news-notes-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.10-copy-and-relay-corinth.local-news-notes-1",
        "faith-origins.10-copy-and-relay-corinth.local-news-notes-2"
      ],
      "destinations": {
        "faith-origins.10-copy-and-relay-corinth.local-news-notes-1": "faith-origins.10-copy-and-relay-corinth.destination-2",
        "faith-origins.10-copy-and-relay-corinth.local-news-notes-2": "faith-origins.10-copy-and-relay-corinth.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both original notes arrived at the copy yard.

ES: Ambas notas originales han llegado al patio de copias.

EN: One account is never two just because we read it twice.

ES: Un relato nunca son dos porque lo leamos dos veces.

### o2 / phase-2

EN: Pay 40 wood for one fictional dispatch notice derived from both collected notes.

ES: Paga 40 de madera por un aviso ficticio de salida elaborado a partir de las dos notas recogidas.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 40
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.10-copy-and-relay-corinth.destination-2"
      ],
      "allocations": {
        "faith-origins.10-copy-and-relay-corinth.destination-2": {
          "wood": 40
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.10-copy-and-relay-corinth.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "requiresInputsCollected": true,
      "id": "req-2",
      "inputEntities": [
        "faith-origins.10-copy-and-relay-corinth.local-news-notes-1",
        "faith-origins.10-copy-and-relay-corinth.local-news-notes-2"
      ],
      "outputEntities": [
        "faith-origins.10-copy-and-relay-corinth.dispatch-notice-1"
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: One paid notice is ready.

ES: Un único aviso pagado está listo.

EN: This is a working note in our invented relay, not the first Thessalonian autograph.

ES: Es una nota de trabajo de nuestro relevo inventado, no el autógrafo de Primera a los Tesalonicenses.

### o3 / phase-3

EN: Bring the notice and both independent carriers to the east-road post alive.

ES: Lleva con vida el aviso y los dos portadores independientes al puesto oriental.

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
        "faith-origins.10-copy-and-relay-corinth.dispatch-notice-1"
      ],
      "destinations": {
        "faith-origins.10-copy-and-relay-corinth.dispatch-notice-1": "faith-origins.10-copy-and-relay-corinth.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.10-copy-and-relay-corinth.relay-carriers-1",
        "faith-origins.10-copy-and-relay-corinth.relay-carriers-2"
      ],
      "destinations": {
        "faith-origins.10-copy-and-relay-corinth.relay-carriers-1": "faith-origins.10-copy-and-relay-corinth.destination-3",
        "faith-origins.10-copy-and-relay-corinth.relay-carriers-2": "faith-origins.10-copy-and-relay-corinth.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: One notice and two named gameplay identities reached onward departure.

ES: Un aviso y dos identidades jugables concretas han alcanzado la salida.

EN: Their next journey lies beyond our map. We cannot claim to have watched it.

ES: Su siguiente viaje queda fuera del mapa. No podemos afirmar que lo hemos visto.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/10-copy-and-relay-corinth.svg)

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
        128.35,
        158.75
      ],
      "lonLat": [
        22.91,
        37.937
      ],
      "name": {
        "en": "North-road arrival court",
        "es-ES": "Patio de llegada del camino norte"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        101.07,
        205.44
      ],
      "lonLat": [
        22.89,
        37.91
      ],
      "name": {
        "en": "Inland relay copy yard",
        "es-ES": "Patio interior de copias para el relevo"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        226.56,
        207.17
      ],
      "lonLat": [
        22.982,
        37.909
      ],
      "name": {
        "en": "East-road onward post",
        "es-ES": "Puesto de continuación del camino oriental"
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
  "terrainInstructions": "North road arrival and inland city court connect toward eastern inland post. Do not place Thessalonica or Macedonia inside Corinth bbox. Long-distance correspondence is off-map; harbor basin/movement needs native footprint audit.",
  "mainRouteLengthStraightTiles": 179.58,
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
  "asset": "docs/design/maps/faith-origins/odyssey/10-copy-and-relay-corinth.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.10-copy-and-relay-corinth.local-news-notes-1",
      "role": "fictional-local-news-note",
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
      "id": "faith-origins.10-copy-and-relay-corinth.local-news-notes-2",
      "role": "fictional-local-news-note",
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
      "id": "faith-origins.10-copy-and-relay-corinth.dispatch-notice-1",
      "role": "fictional-local-dispatch-notice",
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
      "id": "faith-origins.10-copy-and-relay-corinth.relay-carriers-1",
      "role": "fictional-independent-relay-carrier",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.10-copy-and-relay-corinth.relay-carriers-2",
      "role": "fictional-independent-relay-carrier",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.10-copy-and-relay-corinth.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.10-copy-and-relay-corinth.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.10-copy-and-relay-corinth.destination-3",
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
    "local-news-notes": [
      "faith-origins.10-copy-and-relay-corinth.local-news-notes-1",
      "faith-origins.10-copy-and-relay-corinth.local-news-notes-2"
    ],
    "dispatch-notice": [
      "faith-origins.10-copy-and-relay-corinth.dispatch-notice-1"
    ],
    "relay-carriers": [
      "faith-origins.10-copy-and-relay-corinth.relay-carriers-1",
      "faith-origins.10-copy-and-relay-corinth.relay-carriers-2"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Local hospitality notes / Notas locales de hospitalidad

EN: Recover both separate copies from local hospitality notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de notas locales de hospitalidad y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Separate fictitious notes unlock attributed context without becoming the letter itself.

ES: Notas ficticias separadas desbloquean contexto atribuido sin convertirse en la carta.

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
          "10-copy-and-relay-corinth.side-1.entity-1",
          "10-copy-and-relay-corinth.side-1.entity-2"
        ],
        "destinations": {
          "10-copy-and-relay-corinth.side-1.entity-1": "10-copy-and-relay-corinth.side-1.zone-1",
          "10-copy-and-relay-corinth.side-1.entity-2": "10-copy-and-relay-corinth.side-1.zone-1"
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
        "id": "10-copy-and-relay-corinth.side-1.entity-1",
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
        "id": "10-copy-and-relay-corinth.side-1.entity-2",
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
        "id": "10-copy-and-relay-corinth.side-1.zone-1",
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
      "onceFlag": "10-copy-and-relay-corinth.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.10-copy-and-relay-corinth"
      ],
      "historicalNote": {
        "en": "First Thessalonians names Paul, Silvanus and Timothy and describes news from Thessalonica. Its writing place is not stated. The Corinth setting and date around 50–51 are a reconstruction, and the relay participants here are fictional.",
        "es-ES": "Primera a los Tesalonicenses nombra a Pablo, Silvano y Timoteo y describe noticias de Tesalónica. No indica dónde se escribió. La ambientación en Corinto y la fecha hacia 50–51 son una reconstrucción; los participantes del relevo son ficticios."
      },
      "hint": {
        "en": "Collect two separate local news notes and take both to the copy yard.",
        "es-ES": "Recoge dos notas locales distintas y lleva ambas al patio de copias."
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

### Inland junction guide / Guía del cruce interior

EN: Escort the local guide of inland junction guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía del cruce interior hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: Marks a parallel land route between relay courts.

ES: Señala un camino terrestre paralelo entre los patios del relevo.

```json
{
  "id": "side-2",
  "kind": "guide",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "10-copy-and-relay-corinth.side-2.entity-1"
        ],
        "destinations": {
          "10-copy-and-relay-corinth.side-2.entity-1": "10-copy-and-relay-corinth.side-2.zone-1"
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
        "id": "10-copy-and-relay-corinth.side-2.entity-1",
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
        "id": "10-copy-and-relay-corinth.side-2.zone-1",
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
      "onceFlag": "10-copy-and-relay-corinth.side-2.rewarded",
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

### Courier provisions / Provisiones de correo

EN: Escort the trader of courier provisions to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de provisiones de correo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One bounded consignment supports longer optional detours.

ES: Una remesa limitada apoya los desvíos opcionales largos.

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
          "10-copy-and-relay-corinth.side-3.entity-1"
        ],
        "destinations": {
          "10-copy-and-relay-corinth.side-3.entity-1": "10-copy-and-relay-corinth.side-3.zone-1"
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
        "receipt": "10-copy-and-relay-corinth.side-3.payment",
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
        "id": "10-copy-and-relay-corinth.side-3.entity-1",
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
        "id": "10-copy-and-relay-corinth.side-3.zone-1",
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
      "onceFlag": "10-copy-and-relay-corinth.side-3.rewarded",
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

### Relay households / Hogares del relevo

EN: Bring each of the two aid crates to its assigned household at relay households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del relevo. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid belongs to independent fictional recipients.

ES: La ayuda corresponde a receptores ficticios independientes.

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
          "10-copy-and-relay-corinth.side-4.entity-1",
          "10-copy-and-relay-corinth.side-4.entity-2"
        ],
        "destinations": {
          "10-copy-and-relay-corinth.side-4.entity-1": "10-copy-and-relay-corinth.side-4.zone-1",
          "10-copy-and-relay-corinth.side-4.entity-2": "10-copy-and-relay-corinth.side-4.zone-2"
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
        "id": "10-copy-and-relay-corinth.side-4.entity-1",
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
        "id": "10-copy-and-relay-corinth.side-4.entity-2",
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
        "id": "10-copy-and-relay-corinth.side-4.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "10-copy-and-relay-corinth.side-4.zone-2",
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
      "onceFlag": "10-copy-and-relay-corinth.side-4.rewarded",
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

### Roadside store / Almacén del camino

EN: Pay 50 wood and restore the damaged store of roadside store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén del camino. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A repaired local store releases finite supplies once.

ES: Un almacén local reparado entrega suministros finitos una vez.

```json
{
  "id": "side-5",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "10-copy-and-relay-corinth.side-5.entity-1",
        "health": "full",
        "paymentReceipt": "10-copy-and-relay-corinth.side-5.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "10-copy-and-relay-corinth.side-5.payment",
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
        "id": "10-copy-and-relay-corinth.side-5.entity-1",
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
        "id": "10-copy-and-relay-corinth.side-5.zone-1",
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
      "onceFlag": "10-copy-and-relay-corinth.side-5.rewarded",
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

### Independent return travelers / Viajeros de regreso independientes

EN: Bring both voluntary evacuee groups from independent return travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de viajeros de regreso independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Optional arrivals do not fulfill the main two-carrier count.

ES: Las llegadas opcionales no completan el recuento de los dos portadores principales.

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
          "10-copy-and-relay-corinth.side-6.entity-1",
          "10-copy-and-relay-corinth.side-6.entity-2"
        ],
        "destinations": {
          "10-copy-and-relay-corinth.side-6.entity-1": "10-copy-and-relay-corinth.side-6.zone-1",
          "10-copy-and-relay-corinth.side-6.entity-2": "10-copy-and-relay-corinth.side-6.zone-1"
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
        "id": "10-copy-and-relay-corinth.side-6.entity-1",
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
        "id": "10-copy-and-relay-corinth.side-6.entity-2",
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
        "id": "10-copy-and-relay-corinth.side-6.zone-1",
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
      "onceFlag": "10-copy-and-relay-corinth.side-6.rewarded",
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
      "id": "information-first",
      "optionalObjectives": [
        "side-1",
        "side-2"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Survey the inland dispatch route before committing the two carriers."
    },
    {
      "id": "supply-parallelism",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Separate optional trader/repair team consumes50gold/50wood without touching protected recovery."
    },
    {
      "id": "hospitality-chain",
      "optionalObjectives": [
        "side-4",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Help distinct households while the notice is prepared; optional travel cannot delay main terminal state."
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
      "food": 1218,
      "wood": 748,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
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
      "food": 1070,
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
      "food": 1270,
      "wood": 770,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
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
      "food": 1070,
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
      "food": 1323,
      "wood": 793,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
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
      "food": 1070,
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
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.title / always | none | Before the First Letter Faded | Antes de que se borrase la primera carta |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.fact-intro / intro first | collection-narrator | First Thessalonians names Paul, Silvanus and Timothy and describes news from Thessalonica. Its writing place is not stated. The Corinth setting and date around 50–51 are a reconstruction, and the relay participants here are fictional. | Primera a los Tesalonicenses nombra a Pablo, Silvano y Timoteo y describe noticias de Tesalónica. No indica dónde se escribió. La ambientación en Corinto y la fecha hacia 50–51 son una reconstrucción; los participantes del relevo son ficticios. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.persona-intro / after handover | miriam-archive | When news reached my own table, I learned to ask who brought it and what had been left unsaid. I ask the same of these inherited letters. | Cuando llegaban noticias a mi mesa, aprendí a preguntar quién las traía y qué se había callado. Hago la misma pregunta a estas cartas heredadas. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.route-help / available from start; repeatable without effect | none | The scene covers only a local Corinthian relay. Keep inland; its onward destination is off-map, not a road across the gulf. | La escena abarca solo un relevo local corintio. Sigue por tierra; el destino posterior está fuera del mapa, no al otro lado de un camino sobre el golfo. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.o1-goal / phase-1 active | none | Collect two separate local news notes and take both to the copy yard. | Recoge dos notas locales distintas y lleva ambas al patio de copias. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.o1-receipt / o1 latched once | none | Both original notes arrived at the copy yard. | Ambas notas originales han llegado al patio de copias. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.o1-reaction / after o1 receipt | miriam-archive | One account is never two just because we read it twice. | Un relato nunca son dos porque lo leamos dos veces. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.o2-goal / phase-2 active | none | Pay 40 wood for one fictional dispatch notice derived from both collected notes. | Paga 40 de madera por un aviso ficticio de salida elaborado a partir de las dos notas recogidas. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.o2-receipt / o2 latched once | none | One paid notice is ready. | Un único aviso pagado está listo. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.o2-reaction / after o2 receipt | miriam-archive | This is a working note in our invented relay, not the first Thessalonian autograph. | Es una nota de trabajo de nuestro relevo inventado, no el autógrafo de Primera a los Tesalonicenses. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.o3-goal / phase-3 active | none | Bring the notice and both independent carriers to the east-road post alive. | Lleva con vida el aviso y los dos portadores independientes al puesto oriental. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.o3-receipt / o3 latched once | none | One notice and two named gameplay identities reached onward departure. | Un aviso y dos identidades jugables concretas han alcanzado la salida. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.o3-reaction / after o3 receipt | miriam-archive | Their next journey lies beyond our map. We cannot claim to have watched it. | Su siguiente viaje queda fuera del mapa. No podemos afirmar que lo hemos visto. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from local hospitality notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de notas locales de hospitalidad y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-1-complete / side-1 completed | none | Local hospitality notes completed. Its stated benefit has been granted once. | Notas locales de hospitalidad: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-1-lost / side-1 failed-optional | none | Local hospitality notes is unavailable after the loss of its unique participant or object. The main mission continues. | Notas locales de hospitalidad: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-2-goal / optional list from start | none | Escort the local guide of inland junction guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía del cruce interior hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-2-complete / side-2 completed | none | Inland junction guide completed. Its stated benefit has been granted once. | Guía del cruce interior: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-2-lost / side-2 failed-optional | none | Inland junction guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del cruce interior: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-3-goal / optional list from start | none | Escort the trader of courier provisions to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de provisiones de correo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-3-complete / side-3 completed | none | Courier provisions completed. Its stated benefit has been granted once. | Provisiones de correo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-3-lost / side-3 failed-optional | none | Courier provisions is unavailable after the loss of its unique participant or object. The main mission continues. | Provisiones de correo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-4-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at relay households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del relevo. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-4-complete / side-4 completed | none | Relay households completed. Its stated benefit has been granted once. | Hogares del relevo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-4-lost / side-4 failed-optional | none | Relay households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares del relevo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-5-goal / optional list from start | none | Pay 50 wood and restore the damaged store of roadside store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén del camino. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-5-complete / side-5 completed | none | Roadside store completed. Its stated benefit has been granted once. | Almacén del camino: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-5-lost / side-5 failed-optional | none | Roadside store is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén del camino: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from independent return travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de viajeros de regreso independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-6-complete / side-6 completed | none | Independent return travelers completed. Its stated benefit has been granted once. | Viajeros de regreso independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.side-6-lost / side-6 failed-optional | none | Independent return travelers is unavailable after the loss of its unique participant or object. The main mission continues. | Viajeros de regreso independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.fact-outro / victory first | collection-narrator | The letter preserves a network of correspondence and concern. This reconstructed local relay does not prove a Corinthian writing address or make its fictional notes part of the surviving letter. | La carta conserva una red de correspondencia y preocupación. Este relevo local reconstruido no demuestra una dirección de escritura en Corinto ni incorpora sus notas ficticias a la carta conservada. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.persona-outro / after fact-outro | miriam-archive | A message can travel farther than its bearer. My duty is to keep the uncertainty with it, instead of losing that uncertainty on the road. | Un mensaje puede viajar más lejos que quien lo lleva. Mi deber es conservar también la incertidumbre, en lugar de perderla por el camino. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.10-copy-and-relay-corinth.odyssey.next-episode / after persona-outro | none | Continue with The Argument Across the Water. This episode does not complete the campaign. | Continúa con La disputa al otro lado del agua. Este episodio no termina la campaña. |

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
      "one note cannot stand for two",
      "notice cannot exist before derivation",
      "optional travelers cannot replace two main carriers",
      "Thessalonica never placed in Corinth map",
      "Corinth composition remains qualified in all captions",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
