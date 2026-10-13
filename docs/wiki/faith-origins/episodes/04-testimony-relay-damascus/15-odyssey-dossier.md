# 4. The Road He Remembered

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `04-testimony-relay-damascus` · c. 33–36 CE · 340×340

## Historical frame and fixed outcome

EN: Paul describes his change of allegiance as a revelation and commission. His letter mentions Arabia and Damascus without a complete itinerary or exact year. The revelation is attributed to his account.

ES: Pablo describe su cambio como una revelación y un encargo. Su carta menciona Arabia y Damasco sin un itinerario completo ni un año exacto. La revelación se atribuye a su relato.

EN: The local relay preserves a representation of Paul’s testimony. Its couriers do not establish his route through Arabia or recreate a supernatural event.

ES: El relevo local conserva una representación del testimonio de Pablo. Sus correos no acreditan su ruta por Arabia ni recrean un hecho sobrenatural.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 27,
      "episodeId": "04-testimony-relay-damascus",
      "order": 4,
      "selectedSourceUrl": "https://www.biblegateway.com/passage/?search=Galatians+1&version=NIV",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Galatians+1%3A13-17&version=NRSVUE",
      "passage": "Galatians 1:13–17: Paul recalls persecution, a divine revelation/commission, Arabia, and return to Damascus.",
      "supportedClaim": {
        "en": "Paul says he persecuted the assembly of God and describes his change as a revelation and commission; he names Arabia and Damascus but gives no complete itinerary or exact year.",
        "es-ES": "Pablo dice que persiguió a la asamblea de Dios y describe su cambio como revelación y encargo; nombra Arabia y Damasco, pero no ofrece itinerario completo ni año exacto."
      },
      "limitations": "The revelation is Paul's theological account, not an independently verifiable supernatural event. Year range c.33–36 is reconstructed; do not stage an unreported journey.",
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

EN: Collect the fictional local message at the western oasis post. It is not a copy of Galatians.

ES: Recoge el mensaje local ficticio en el puesto del oasis occidental. No es una copia de Gálatas.

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
        "faith-origins.04-testimony-relay-damascus.testimony-copy-1"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: One fictional local message is registered; it does not add a historical witness.

ES: Se registra un mensaje local ficticio; no añade un testigo histórico.

EN: His account is not mine to improve.

ES: No me corresponde mejorar su relato.

### o2 / phase-2

EN: Deliver that copy to the city relay and fund its local reception with 120 food.

ES: Entrega esa copia en el relevo urbano y financia su recepción local con 120 de alimento.

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
        "faith-origins.04-testimony-relay-damascus.testimony-copy-1"
      ],
      "destinations": {
        "faith-origins.04-testimony-relay-damascus.testimony-copy-1": "faith-origins.04-testimony-relay-damascus.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 120
      },
      "id": "req-2",
      "receivingZones": [
        "faith-origins.04-testimony-relay-damascus.destination-2"
      ],
      "allocations": {
        "faith-origins.04-testimony-relay-damascus.destination-2": {
          "food": 120
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.04-testimony-relay-damascus.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The copy and reception payment are recorded once.

ES: La copia y el pago de recepción quedan registrados una vez.

EN: This is a short relay in an oasis, not a map of every journey.

ES: Este es un relevo breve en un oasis, no un mapa de todos los viajes.

### o3 / phase-3

EN: Bring the distinct local messenger alive to the eastern orchard station.

ES: Lleva con vida al correo local distinto a la estación de huertos oriental.

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
        "faith-origins.04-testimony-relay-damascus.relay-messenger-1"
      ],
      "destinations": {
        "faith-origins.04-testimony-relay-damascus.relay-messenger-1": "faith-origins.04-testimony-relay-damascus.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The local messenger has reached the eastern receiving station.

ES: El correo local ha llegado a la estación receptora oriental.

EN: A messenger carries a local message. The later account belongs to another part of my archive.

ES: Un mensajero lleva un mensaje local. El relato posterior pertenece a otra parte de mi archivo.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/04-testimony-relay-damascus.svg)

```json
{
  "bbox": [
    36.25,
    33.47,
    36.355,
    33.535
  ],
  "terrainProfile": "damascus",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        61.4,
        150.49
      ],
      "lonLat": [
        36.265,
        33.508
      ],
      "name": {
        "en": "Western oasis post",
        "es-ES": "Puesto del oasis occidental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        168.06,
        171.23
      ],
      "lonLat": [
        36.302,
        33.502
      ],
      "name": {
        "en": "Southern city relay court",
        "es-ES": "Patio de relevo del sector urbano sur"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        277.6,
        178.14
      ],
      "lonLat": [
        36.34,
        33.5
      ],
      "name": {
        "en": "Eastern orchard station",
        "es-ES": "Estación de huertos oriental"
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
      "routePolicy": "Same-bank southern local circuit; diagram centreline only. Parallel path offsets, canal avoidance and traversable full width require native verification."
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
      "routePolicy": "Same-bank southern local circuit; diagram centreline only. Parallel path offsets, canal avoidance and traversable full width require native verification."
    }
  ],
  "terrainInstructions": "Local southern Damascus oasis frame; all fictional courts and both proposed land corridors stay south of the schematic Barada control. Western/northwestern uplands are mostly off-frame; eastern orchards remain lowland. Ancient branches, canal alignments and footprints remain unverified. No assumed ford, bridge, Umayyad mosque before 706, or guessed Arabia leg.",
  "corridorStraightLengthsTiles": {
    "main": 218.42,
    "relief": 218.42
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
        36.12,
        33.61
      ],
      [
        36.23,
        33.54
      ],
      [
        36.3,
        33.52
      ],
      [
        36.34,
        33.515
      ],
      [
        36.45,
        33.5
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
  "asset": "docs/design/maps/faith-origins/odyssey/04-testimony-relay-damascus.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.04-testimony-relay-damascus.testimony-copy-1",
      "role": "fictional-contemporary-local-message",
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
      "id": "faith-origins.04-testimony-relay-damascus.relay-messenger-1",
      "role": "fictional-local-courier",
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
    }
  ],
  "zones": [
    {
      "id": "faith-origins.04-testimony-relay-damascus.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.04-testimony-relay-damascus.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.04-testimony-relay-damascus.destination-3",
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
    "testimony-copy": [
      "faith-origins.04-testimony-relay-damascus.testimony-copy-1"
    ],
    "relay-messenger": [
      "faith-origins.04-testimony-relay-damascus.relay-messenger-1"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Orchard workers / Trabajadores de los huertos

EN: Bring each of the two aid crates to its assigned household at orchard workers. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en trabajadores de los huertos. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid reflects an oasis district.

ES: El auxilio corresponde a un ámbito de oasis.

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
          "04-testimony-relay-damascus.side-1.entity-1",
          "04-testimony-relay-damascus.side-1.entity-2"
        ],
        "destinations": {
          "04-testimony-relay-damascus.side-1.entity-1": "04-testimony-relay-damascus.side-1.zone-1",
          "04-testimony-relay-damascus.side-1.entity-2": "04-testimony-relay-damascus.side-1.zone-2"
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
        "id": "04-testimony-relay-damascus.side-1.entity-1",
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
        "id": "04-testimony-relay-damascus.side-1.entity-2",
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
        "id": "04-testimony-relay-damascus.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "04-testimony-relay-damascus.side-1.zone-2",
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
      "onceFlag": "04-testimony-relay-damascus.side-1.rewarded",
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

### Relay duplicates / Duplicados del relevo

EN: Recover both separate copies from relay duplicates and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de duplicados del relevo y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Independent copies preserve testimony.

ES: Las copias independientes conservan el testimonio.

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
          "04-testimony-relay-damascus.side-2.entity-1",
          "04-testimony-relay-damascus.side-2.entity-2"
        ],
        "destinations": {
          "04-testimony-relay-damascus.side-2.entity-1": "04-testimony-relay-damascus.side-2.zone-1",
          "04-testimony-relay-damascus.side-2.entity-2": "04-testimony-relay-damascus.side-2.zone-1"
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
        "id": "04-testimony-relay-damascus.side-2.entity-1",
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
        "id": "04-testimony-relay-damascus.side-2.entity-2",
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
        "id": "04-testimony-relay-damascus.side-2.zone-1",
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
      "onceFlag": "04-testimony-relay-damascus.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.04-testimony-relay-damascus"
      ],
      "historicalNote": {
        "en": "Paul describes his change of allegiance as a revelation and commission. His letter mentions Arabia and Damascus without a complete itinerary or exact year. The revelation is attributed to his account.",
        "es-ES": "Pablo describe su cambio como una revelación y un encargo. Su carta menciona Arabia y Damasco sin un itinerario completo ni un año exacto. La revelación se atribuye a su relato."
      },
      "hint": {
        "en": "Collect the fictional local message at the western oasis post. It is not a copy of Galatians.",
        "es-ES": "Recoge el mensaje local ficticio en el puesto del oasis occidental. No es una copia de Gálatas."
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

### Canal-side store / Almacén junto al canal

EN: Pay 50 wood and restore the damaged store of canal-side store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén junto al canal. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair does not alter river geography.

ES: La reparación no altera la geografía fluvial.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "04-testimony-relay-damascus.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "04-testimony-relay-damascus.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "04-testimony-relay-damascus.side-3.payment",
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
        "id": "04-testimony-relay-damascus.side-3.entity-1",
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
        "id": "04-testimony-relay-damascus.side-3.zone-1",
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
      "onceFlag": "04-testimony-relay-damascus.side-3.rewarded",
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

### Oasis consignment / Remesa del oasis

EN: Escort the trader of oasis consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de remesa del oasis hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Finite supplies travel locally.

ES: Los suministros finitos viajan de forma local.

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
          "04-testimony-relay-damascus.side-4.entity-1"
        ],
        "destinations": {
          "04-testimony-relay-damascus.side-4.entity-1": "04-testimony-relay-damascus.side-4.zone-1"
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
        "receipt": "04-testimony-relay-damascus.side-4.payment",
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
        "id": "04-testimony-relay-damascus.side-4.entity-1",
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
        "id": "04-testimony-relay-damascus.side-4.zone-1",
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
      "onceFlag": "04-testimony-relay-damascus.side-4.rewarded",
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

### Orchard path guide / Guía del sendero de huertos

EN: Escort the local guide of orchard path guide to the marked road junction. Benefit: Mark the proposed southern relief circuit once. This supplies route information; no verified bridge, terrain change or exclusive main access.

ES: Escolta al guía local de guía del sendero de huertos hasta el cruce señalado. Ventaja: Señala una vez el circuito meridional de auxilio propuesto. Aporta información de ruta; no acredita un puente ni cambia el terreno ni da acceso principal exclusivo.

EN: Marks the narrower southern land alternative; no surveyed crossing is claimed.

ES: Señala la alternativa terrestre meridional más estrecha; no acredita ningún cruce topográfico.

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
          "04-testimony-relay-damascus.side-5.entity-1"
        ],
        "destinations": {
          "04-testimony-relay-damascus.side-5.entity-1": "04-testimony-relay-damascus.side-5.zone-1"
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
        "id": "04-testimony-relay-damascus.side-5.entity-1",
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
        "id": "04-testimony-relay-damascus.side-5.zone-1",
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
      "target": "relief proposed southern land corridor",
      "resources": {},
      "onceFlag": "04-testimony-relay-damascus.side-5.rewarded",
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

### Visiting caravan families / Familias de caravanas visitantes

EN: Bring both voluntary evacuee groups from visiting caravan families to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de familias de caravanas visitantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Voluntary lodging, not a recorded Pauline itinerary.

ES: Alojamiento voluntario, no itinerario paulino documentado.

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
          "04-testimony-relay-damascus.side-6.entity-1",
          "04-testimony-relay-damascus.side-6.entity-2"
        ],
        "destinations": {
          "04-testimony-relay-damascus.side-6.entity-1": "04-testimony-relay-damascus.side-6.zone-1",
          "04-testimony-relay-damascus.side-6.entity-2": "04-testimony-relay-damascus.side-6.zone-1"
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
        "id": "04-testimony-relay-damascus.side-6.entity-1",
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
        "id": "04-testimony-relay-damascus.side-6.entity-2",
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
        "id": "04-testimony-relay-damascus.side-6.zone-1",
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
      "onceFlag": "04-testimony-relay-damascus.side-6.rewarded",
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
      "food": 1338,
      "wood": 708,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 120,
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
      "food": 1190,
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
      "food": 1390,
      "wood": 730,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 120,
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
      "food": 1190,
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
      "food": 1443,
      "wood": 753,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 120,
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
      "food": 1190,
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
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.title / always | none | The Road He Remembered | El camino que recordaba |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.fact-intro / intro first | collection-narrator | Paul describes his change of allegiance as a revelation and commission. His letter mentions Arabia and Damascus without a complete itinerary or exact year. The revelation is attributed to his account. | Pablo describe su cambio como una revelación y un encargo. Su carta menciona Arabia y Damasco sin un itinerario completo ni un año exacto. La revelación se atribuye a su relato. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.persona-intro / after handover | miriam-archive | He gives a reason for his journey. I keep his reason beside his name. I cannot use it to supply roads he never described. | Él da una razón para su viaje. Conservo esa razón junto a su nombre. No puedo usarla para añadir caminos que nunca describió. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.route-help / available from start; repeatable without effect | none | Follow the southern oasis land circuit between the three disclosed courts. No river crossing is required or assumed. The narrower parallel relief path needs terrain and footprint verification; Arabia remains off-map. | Sigue el circuito terrestre del oasis sur entre los tres patios señalados. No exige ni presupone cruzar el río. El sendero paralelo de auxilio requiere verificar terreno y parcelas; Arabia queda fuera del mapa. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.o1-goal / phase-1 active | none | Collect the fictional local message at the western oasis post. It is not a copy of Galatians. | Recoge el mensaje local ficticio en el puesto del oasis occidental. No es una copia de Gálatas. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.o1-receipt / o1 latched once | none | One fictional local message is registered; it does not add a historical witness. | Se registra un mensaje local ficticio; no añade un testigo histórico. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.o1-reaction / after o1 receipt | miriam-archive | His account is not mine to improve. | No me corresponde mejorar su relato. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.o2-goal / phase-2 active | none | Deliver that copy to the city relay and fund its local reception with 120 food. | Entrega esa copia en el relevo urbano y financia su recepción local con 120 de alimento. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.o2-receipt / o2 latched once | none | The copy and reception payment are recorded once. | La copia y el pago de recepción quedan registrados una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.o2-reaction / after o2 receipt | miriam-archive | This is a short relay in an oasis, not a map of every journey. | Este es un relevo breve en un oasis, no un mapa de todos los viajes. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.o3-goal / phase-3 active | none | Bring the distinct local messenger alive to the eastern orchard station. | Lleva con vida al correo local distinto a la estación de huertos oriental. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.o3-receipt / o3 latched once | none | The local messenger has reached the eastern receiving station. | El correo local ha llegado a la estación receptora oriental. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.o3-reaction / after o3 receipt | miriam-archive | A messenger carries a local message. The later account belongs to another part of my archive. | Un mensajero lleva un mensaje local. El relato posterior pertenece a otra parte de mi archivo. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at orchard workers. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en trabajadores de los huertos. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-1-complete / side-1 completed | none | Orchard workers completed. Its stated benefit has been granted once. | Trabajadores de los huertos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-1-lost / side-1 failed-optional | none | Orchard workers is unavailable after the loss of its unique participant or object. The main mission continues. | Trabajadores de los huertos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from relay duplicates and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de duplicados del relevo y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-2-complete / side-2 completed | none | Relay duplicates completed. Its stated benefit has been granted once. | Duplicados del relevo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-2-lost / side-2 failed-optional | none | Relay duplicates is unavailable after the loss of its unique participant or object. The main mission continues. | Duplicados del relevo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of canal-side store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén junto al canal. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-3-complete / side-3 completed | none | Canal-side store completed. Its stated benefit has been granted once. | Almacén junto al canal: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-3-lost / side-3 failed-optional | none | Canal-side store is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén junto al canal: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-4-goal / optional list from start | none | Escort the trader of oasis consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de remesa del oasis hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-4-complete / side-4 completed | none | Oasis consignment completed. Its stated benefit has been granted once. | Remesa del oasis: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-4-lost / side-4 failed-optional | none | Oasis consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Remesa del oasis: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-5-goal / optional list from start | none | Escort the local guide of orchard path guide to the marked road junction. Benefit: Mark the proposed southern relief circuit once. This supplies route information; no verified bridge, terrain change or exclusive main access. | Escolta al guía local de guía del sendero de huertos hasta el cruce señalado. Ventaja: Señala una vez el circuito meridional de auxilio propuesto. Aporta información de ruta; no acredita un puente ni cambia el terreno ni da acceso principal exclusivo. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-5-complete / side-5 completed | none | Orchard path guide completed. Its stated benefit has been granted once. | Guía del sendero de huertos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-5-lost / side-5 failed-optional | none | Orchard path guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del sendero de huertos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from visiting caravan families to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de familias de caravanas visitantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-6-complete / side-6 completed | none | Visiting caravan families completed. Its stated benefit has been granted once. | Familias de caravanas visitantes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.side-6-lost / side-6 failed-optional | none | Visiting caravan families is unavailable after the loss of its unique participant or object. The main mission continues. | Familias de caravanas visitantes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.fact-outro / victory first | collection-narrator | The local relay preserves a representation of Paul’s testimony. Its couriers do not establish his route through Arabia or recreate a supernatural event. | El relevo local conserva una representación del testimonio de Pablo. Sus correos no acreditan su ruta por Arabia ni recrean un hecho sobrenatural. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.persona-outro / after fact-outro | miriam-archive | An honest copy leaves the speaker’s voice intact and the copier’s inventions outside the page. | Una copia honrada conserva la voz de quien habla y deja fuera de la página las invenciones del copista. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.04-testimony-relay-damascus.odyssey.next-episode / after persona-outro | none | Continue with Fifteen Days, Many Voices. This episode does not complete the campaign. | Continúa con Quince días, muchas voces. Este episodio no termina la campaña. |

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
      "courier and testimony token remain distinct",
      "no guessed itinerary across Arabia",
      "canal path cannot be rasterized as continuous land",
      "All three receiver radii and both full-width corridors must remain on the southern bank of the schematic control; unresolved native canals block promotion, not trigger an invented bridge.",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
