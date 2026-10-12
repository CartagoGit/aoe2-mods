# 3. A Table in Jerusalem

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `03-shared-provision-jerusalem` · c. 30–40 CE · 320×320

## Historical frame and fixed outcome

EN: Acts portrays teaching, meals and sharing within the early Jerusalem community. This is the book’s account, not an independent census or proof that every household lived alike.

ES: Hechos describe enseñanza, comidas y bienes compartidos en la primera comunidad de Jerusalén. Es el relato del libro, no un censo independiente ni una prueba de que todos los hogares vivieran igual.

EN: The scenario illustrates the communal practices described in Acts. Its two kitchens, quantities and delivery rounds are playable reconstruction.

ES: El escenario ilustra las prácticas comunitarias que describe Hechos. Sus dos cocinas, cantidades y rondas de entrega son una reconstrucción jugable.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "episodeId": "03-shared-provision-jerusalem",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Acts+2%3A42-47&version=NRSVUE",
      "passage": "Acts 2:42–47; communal meals and distribution as portrayed by Acts",
      "supportedClaim": {
        "en": "Acts portrays teaching, meals and sharing within the early Jerusalem community. This is the book’s account, not an independent census or proof that every household lived alike.",
        "es-ES": "Hechos describe enseñanza, comidas y bienes compartidos en la primera comunidad de Jerusalén. Es el relato del libro, no un censo independiente ni una prueba de que todos los hogares vivieran igual."
      },
      "limitations": "Relato literario cristiano; no censo, cantidades ni uniformidad social comprobados. Las tareas domésticas del mapa son ficticias.",
      "consultationDate": "2026-10-12",
      "status": "consulted by gpt-6; independent approval pending"
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

EN: Collect four separately marked meal baskets at the market court.

ES: Recoge cuatro cestas de comida con marcas distintas en el patio del mercado.

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
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-1",
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-2",
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-3",
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-4"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All four basket identities are recorded.

ES: Las cuatro identidades de las cestas están registradas.

EN: A shared table still has separate journeys behind it.

ES: Tras una mesa compartida siguen existiendo viajes distintos.

### o2 / phase-2

EN: Deliver all four baskets to the kitchen district and pay 160 food for one communal provision.

ES: Entrega las cuatro cestas en el barrio de cocinas y paga 160 de alimento para una sola provisión común.

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
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-1",
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-2",
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-3",
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-4"
      ],
      "destinations": {
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-1": "faith-origins.03-shared-provision-jerusalem.destination-2",
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-2": "faith-origins.03-shared-provision-jerusalem.destination-2",
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-3": "faith-origins.03-shared-provision-jerusalem.destination-2",
        "faith-origins.03-shared-provision-jerusalem.meal-baskets-4": "faith-origins.03-shared-provision-jerusalem.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 160
      },
      "id": "req-2",
      "receivingZones": [
        "faith-origins.03-shared-provision-jerusalem.destination-2"
      ],
      "allocations": {
        "faith-origins.03-shared-provision-jerusalem.destination-2": {
          "food": 160
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.03-shared-provision-jerusalem.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Four baskets and one payment receipt complete the kitchen provision.

ES: Cuatro cestas y un único recibo completan la provisión de las cocinas.

EN: Count both the baskets and the payment; promises cannot feed a household.

ES: Cuenta las cestas y el pago; las promesas no alimentan a un hogar.

### o3 / phase-3

EN: Deliver the two distinct distribution notes to the southern households.

ES: Entrega las dos notas de reparto distintas en los hogares del sur.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "faith-origins.03-shared-provision-jerusalem.distribution-notes-1",
        "faith-origins.03-shared-provision-jerusalem.distribution-notes-2"
      ],
      "destinations": {
        "faith-origins.03-shared-provision-jerusalem.distribution-notes-1": "faith-origins.03-shared-provision-jerusalem.destination-3",
        "faith-origins.03-shared-provision-jerusalem.distribution-notes-2": "faith-origins.03-shared-provision-jerusalem.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both distribution notes have arrived; neither is a claim about the size of the ancient community.

ES: Ambas notas han llegado; ninguna afirma el tamaño de la comunidad antigua.

EN: A margin note can remember a duty after its speaker has gone.

ES: Una nota al margen puede recordar una obligación cuando su voz ya se ha ido.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/03-shared-provision-jerusalem.svg)

```json
{
  "bbox": [
    35.12,
    31.7,
    35.3,
    31.86
  ],
  "terrainProfile": "jerusalem",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        165.55,
        125.68
      ],
      "lonLat": [
        35.214,
        31.799
      ],
      "name": {
        "en": "West market court",
        "es-ES": "Patio del mercado oeste"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        180.69,
        157.72
      ],
      "lonLat": [
        35.224,
        31.781
      ],
      "name": {
        "en": "Domestic kitchen district",
        "es-ES": "Barrio de cocinas domésticas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        186.74,
        204.0
      ],
      "lonLat": [
        35.228,
        31.755
      ],
      "name": {
        "en": "South households",
        "es-ES": "Hogares del sur"
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
  "terrainInstructions": "Domestic activities on the western plateau and southern approaches; Temple referenced in source, not captured by player. No church basilicas of later centuries; terrain remains limestone and ravines.",
  "mainRouteLengthStraightTiles": 82.11,
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
  "asset": "docs/design/maps/faith-origins/odyssey/03-shared-provision-jerusalem.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.03-shared-provision-jerusalem.meal-baskets-1",
      "role": "fictional-food-consignment",
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
      "id": "faith-origins.03-shared-provision-jerusalem.meal-baskets-2",
      "role": "fictional-food-consignment",
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
      "id": "faith-origins.03-shared-provision-jerusalem.meal-baskets-3",
      "role": "fictional-food-consignment",
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
      "id": "faith-origins.03-shared-provision-jerusalem.meal-baskets-4",
      "role": "fictional-food-consignment",
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
      "id": "faith-origins.03-shared-provision-jerusalem.distribution-notes-1",
      "role": "fictional-delivery-note",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.03-shared-provision-jerusalem.distribution-notes-2",
      "role": "fictional-delivery-note",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.03-shared-provision-jerusalem.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.03-shared-provision-jerusalem.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.03-shared-provision-jerusalem.destination-3",
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
    "meal-baskets": [
      "faith-origins.03-shared-provision-jerusalem.meal-baskets-1",
      "faith-origins.03-shared-provision-jerusalem.meal-baskets-2",
      "faith-origins.03-shared-provision-jerusalem.meal-baskets-3",
      "faith-origins.03-shared-provision-jerusalem.meal-baskets-4"
    ],
    "distribution-notes": [
      "faith-origins.03-shared-provision-jerusalem.distribution-notes-1",
      "faith-origins.03-shared-provision-jerusalem.distribution-notes-2"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Market families / Familias del mercado

EN: Bring each of the two aid crates to its assigned household at market families. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en familias del mercado. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Local food aid follows the domestic theme.

ES: El auxilio local sigue la temática doméstica.

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
          "03-shared-provision-jerusalem.side-1.entity-1",
          "03-shared-provision-jerusalem.side-1.entity-2"
        ],
        "destinations": {
          "03-shared-provision-jerusalem.side-1.entity-1": "03-shared-provision-jerusalem.side-1.zone-1",
          "03-shared-provision-jerusalem.side-1.entity-2": "03-shared-provision-jerusalem.side-1.zone-2"
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
        "id": "03-shared-provision-jerusalem.side-1.entity-1",
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
        "id": "03-shared-provision-jerusalem.side-1.entity-2",
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
        "id": "03-shared-provision-jerusalem.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "03-shared-provision-jerusalem.side-1.zone-2",
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
      "onceFlag": "03-shared-provision-jerusalem.side-1.rewarded",
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

### Household lists / Listas domésticas

EN: Recover both separate copies from household lists and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de listas domésticas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Copy two independent fictional lists.

ES: Copia dos listas ficticias independientes.

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
          "03-shared-provision-jerusalem.side-2.entity-1",
          "03-shared-provision-jerusalem.side-2.entity-2"
        ],
        "destinations": {
          "03-shared-provision-jerusalem.side-2.entity-1": "03-shared-provision-jerusalem.side-2.zone-1",
          "03-shared-provision-jerusalem.side-2.entity-2": "03-shared-provision-jerusalem.side-2.zone-1"
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
        "id": "03-shared-provision-jerusalem.side-2.entity-1",
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
        "id": "03-shared-provision-jerusalem.side-2.entity-2",
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
        "id": "03-shared-provision-jerusalem.side-2.zone-1",
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
      "onceFlag": "03-shared-provision-jerusalem.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.03-shared-provision-jerusalem"
      ],
      "historicalNote": {
        "en": "Acts portrays teaching, meals and sharing within the early Jerusalem community. This is the book’s account, not an independent census or proof that every household lived alike.",
        "es-ES": "Hechos describe enseñanza, comidas y bienes compartidos en la primera comunidad de Jerusalén. Es el relato del libro, no un censo independiente ni una prueba de que todos los hogares vivieran igual."
      },
      "hint": {
        "en": "Collect four separately marked meal baskets at the market court.",
        "es-ES": "Recoge cuatro cestas de comida con marcas distintas en el patio del mercado."
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

### Kitchen store / Almacén de la cocina

EN: Pay 50 wood and restore the damaged store of kitchen store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén de la cocina. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A repair buys finite provision stock.

ES: Una reparación obtiene existencias finitas.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "03-shared-provision-jerusalem.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "03-shared-provision-jerusalem.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "03-shared-provision-jerusalem.side-3.payment",
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
        "id": "03-shared-provision-jerusalem.side-3.entity-1",
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
        "id": "03-shared-provision-jerusalem.side-3.zone-1",
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
      "onceFlag": "03-shared-provision-jerusalem.side-3.rewarded",
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

### Grain carrier / Portador de grano

EN: Escort the trader of grain carrier to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de portador de grano hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Trade requires arrival before payment.

ES: El intercambio requiere llegada antes del pago.

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
          "03-shared-provision-jerusalem.side-4.entity-1"
        ],
        "destinations": {
          "03-shared-provision-jerusalem.side-4.entity-1": "03-shared-provision-jerusalem.side-4.zone-1"
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
        "receipt": "03-shared-provision-jerusalem.side-4.payment",
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
        "id": "03-shared-provision-jerusalem.side-4.entity-1",
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
        "id": "03-shared-provision-jerusalem.side-4.zone-1",
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
      "onceFlag": "03-shared-provision-jerusalem.side-4.rewarded",
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

### Western footpath / Sendero occidental

EN: Escort the local guide of western footpath to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de sendero occidental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: A guide marks an existing footpath.

ES: Un guía señala un sendero existente.

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
          "03-shared-provision-jerusalem.side-5.entity-1"
        ],
        "destinations": {
          "03-shared-provision-jerusalem.side-5.entity-1": "03-shared-provision-jerusalem.side-5.zone-1"
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
        "id": "03-shared-provision-jerusalem.side-5.entity-1",
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
        "id": "03-shared-provision-jerusalem.side-5.zone-1",
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
      "onceFlag": "03-shared-provision-jerusalem.side-5.rewarded",
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

### Guests seeking lodging / Huéspedes que buscan alojamiento

EN: Bring both voluntary evacuee groups from guests seeking lodging to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de huéspedes que buscan alojamiento al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Hospitality is voluntary and distinct from conversion.

ES: La hospitalidad es voluntaria e independiente de la conversión.

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
          "03-shared-provision-jerusalem.side-6.entity-1",
          "03-shared-provision-jerusalem.side-6.entity-2"
        ],
        "destinations": {
          "03-shared-provision-jerusalem.side-6.entity-1": "03-shared-provision-jerusalem.side-6.zone-1",
          "03-shared-provision-jerusalem.side-6.entity-2": "03-shared-provision-jerusalem.side-6.zone-1"
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
        "id": "03-shared-provision-jerusalem.side-6.entity-1",
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
        "id": "03-shared-provision-jerusalem.side-6.entity-2",
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
        "id": "03-shared-provision-jerusalem.side-6.zone-1",
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
      "onceFlag": "03-shared-provision-jerusalem.side-6.rewarded",
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
      "food": 1378,
      "wood": 708,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 160,
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
      "food": 1230,
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
      "food": 1430,
      "wood": 730,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 160,
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
      "food": 1230,
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
      "food": 1483,
      "wood": 753,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 160,
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
      "food": 1230,
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
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.title / always | none | A Table in Jerusalem | Una mesa en Jerusalén |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.fact-intro / intro first | collection-narrator | Acts portrays teaching, meals and sharing within the early Jerusalem community. This is the book’s account, not an independent census or proof that every household lived alike. | Hechos describe enseñanza, comidas y bienes compartidos en la primera comunidad de Jerusalén. Es el relato del libro, no un censo independiente ni una prueba de que todos los hogares vivieran igual. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.persona-intro / after handover | miriam-archive | My grandmother marked the meals in the margins. I used to read only the speeches. She knew a community also had to set a table. | Mi abuela señalaba las comidas en los márgenes. Yo antes solo leía los discursos. Ella sabía que una comunidad también tenía que poner la mesa. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.route-help / available from start; repeatable without effect | none | Keep the market, kitchen and delivery notes separate. The marked western path avoids the steep eastern valley. | Distingue el mercado, las cocinas y las notas de reparto. El camino occidental señalado evita el valle escarpado del este. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.o1-goal / phase-1 active | none | Collect four separately marked meal baskets at the market court. | Recoge cuatro cestas de comida con marcas distintas en el patio del mercado. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.o1-receipt / o1 latched once | none | All four basket identities are recorded. | Las cuatro identidades de las cestas están registradas. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.o1-reaction / after o1 receipt | miriam-archive | A shared table still has separate journeys behind it. | Tras una mesa compartida siguen existiendo viajes distintos. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.o2-goal / phase-2 active | none | Deliver all four baskets to the kitchen district and pay 160 food for one communal provision. | Entrega las cuatro cestas en el barrio de cocinas y paga 160 de alimento para una sola provisión común. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.o2-receipt / o2 latched once | none | Four baskets and one payment receipt complete the kitchen provision. | Cuatro cestas y un único recibo completan la provisión de las cocinas. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.o2-reaction / after o2 receipt | miriam-archive | Count both the baskets and the payment; promises cannot feed a household. | Cuenta las cestas y el pago; las promesas no alimentan a un hogar. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.o3-goal / phase-3 active | none | Deliver the two distinct distribution notes to the southern households. | Entrega las dos notas de reparto distintas en los hogares del sur. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.o3-receipt / o3 latched once | none | Both distribution notes have arrived; neither is a claim about the size of the ancient community. | Ambas notas han llegado; ninguna afirma el tamaño de la comunidad antigua. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.o3-reaction / after o3 receipt | miriam-archive | A margin note can remember a duty after its speaker has gone. | Una nota al margen puede recordar una obligación cuando su voz ya se ha ido. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at market families. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en familias del mercado. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-1-complete / side-1 completed | none | Market families completed. Its stated benefit has been granted once. | Familias del mercado: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-1-lost / side-1 failed-optional | none | Market families is unavailable after the loss of its unique participant or object. The main mission continues. | Familias del mercado: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from household lists and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de listas domésticas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-2-complete / side-2 completed | none | Household lists completed. Its stated benefit has been granted once. | Listas domésticas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-2-lost / side-2 failed-optional | none | Household lists is unavailable after the loss of its unique participant or object. The main mission continues. | Listas domésticas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of kitchen store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén de la cocina. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-3-complete / side-3 completed | none | Kitchen store completed. Its stated benefit has been granted once. | Almacén de la cocina: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-3-lost / side-3 failed-optional | none | Kitchen store is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén de la cocina: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-4-goal / optional list from start | none | Escort the trader of grain carrier to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de portador de grano hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-4-complete / side-4 completed | none | Grain carrier completed. Its stated benefit has been granted once. | Portador de grano: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-4-lost / side-4 failed-optional | none | Grain carrier is unavailable after the loss of its unique participant or object. The main mission continues. | Portador de grano: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-5-goal / optional list from start | none | Escort the local guide of western footpath to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de sendero occidental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-5-complete / side-5 completed | none | Western footpath completed. Its stated benefit has been granted once. | Sendero occidental: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-5-lost / side-5 failed-optional | none | Western footpath is unavailable after the loss of its unique participant or object. The main mission continues. | Sendero occidental: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from guests seeking lodging to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de huéspedes que buscan alojamiento al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-6-complete / side-6 completed | none | Guests seeking lodging completed. Its stated benefit has been granted once. | Huéspedes que buscan alojamiento: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.side-6-lost / side-6 failed-optional | none | Guests seeking lodging is unavailable after the loss of its unique participant or object. The main mission continues. | Huéspedes que buscan alojamiento: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.fact-outro / victory first | collection-narrator | The scenario illustrates the communal practices described in Acts. Its two kitchens, quantities and delivery rounds are playable reconstruction. | El escenario ilustra las prácticas comunitarias que describe Hechos. Sus dos cocinas, cantidades y rondas de entrega son una reconstrucción jugable. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.persona-outro / after fact-outro | miriam-archive | Sharing begins with attention to what each house needs. It does not make every disagreement disappear. | Compartir empieza por atender a lo que necesita cada casa. No hace desaparecer todos los desacuerdos. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.03-shared-provision-jerusalem.odyssey.next-episode / after persona-outro | none | Continue with The Road He Remembered. This episode does not complete the campaign. | Continúa con El camino que recordaba. Este episodio no termina la campaña. |

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
      "four distinct baskets, not four visits",
      "notes cannot finish the kitchen phase",
      "payment without baskets is incomplete",
      "no religious conversion or conquest objective",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
