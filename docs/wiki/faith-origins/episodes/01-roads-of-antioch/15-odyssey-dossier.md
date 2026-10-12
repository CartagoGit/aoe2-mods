# 6. Letters on the Orontes

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `01-roads-of-antioch` · c. 40–49 CE; conventional early-network reconstruction · 340×340

## Historical frame and fixed outcome

EN: Acts describes a community at Antioch and an aid shipment to Judea. Its travelers and charitable network provide the narrative context; this local courier circuit is fictional and its conventional dating is reconstructed.

ES: Hechos describe una comunidad en Antioquía y una remesa de ayuda a Judea. Sus viajeros y su red de auxilio aportan el contexto narrativo; el circuito local de correos es ficticio y su fecha convencional se reconstruye.

EN: The local circuit changes no documented historical outcome. Acts and Paul’s later account of disagreement remain separately attributed sources; deliveries do not establish uniform beliefs.

ES: El circuito local no cambia ningún desenlace histórico documentado. Hechos y el relato paulino posterior de desacuerdo siguen atribuidos por separado; las entregas no prueban creencias uniformes.

EN: The named gameplay workers, objects, quantities and routes are fictional local reconstruction. Historical persons remain in the attributed narration.

ES: Los trabajadores, objetos, cantidades y rutas jugables son una reconstrucción local ficticia. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "episodeId": "01-roads-of-antioch",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Acts+11%3A19-30&version=NRSVUE",
      "passage": "Acts 11:19–30; Antioch community and narrated aid to Judea",
      "supportedClaim": {
        "en": "Acts describes a community at Antioch and an aid shipment to Judea. Its travelers and charitable network provide the narrative context; this local courier circuit is fictional and its conventional dating is reconstructed.",
        "es-ES": "Hechos describe una comunidad en Antioquía y una remesa de ayuda a Judea. Sus viajeros y su red de auxilio aportan el contexto narrativo; el circuito local de correos es ficticio y su fecha convencional se reconstruye."
      },
      "limitations": "Relato literario cristiano; fechas y cifras no se fijan en el pasaje. Gal2:11–14 se conserva como contexto posterior de disenso, no se sitúa antes de su relato de visita a Jerusalén.",
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

EN: Bring all three sealed letters to the eastern city receiving court.

ES: Lleva las tres cartas selladas al patio receptor oriental de la ciudad.

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
        "faith-origins.01-roads-of-antioch.sealed-letters-1",
        "faith-origins.01-roads-of-antioch.sealed-letters-2",
        "faith-origins.01-roads-of-antioch.sealed-letters-3"
      ],
      "destinations": {
        "faith-origins.01-roads-of-antioch.sealed-letters-1": "faith-origins.01-roads-of-antioch.destination-2",
        "faith-origins.01-roads-of-antioch.sealed-letters-2": "faith-origins.01-roads-of-antioch.destination-2",
        "faith-origins.01-roads-of-antioch.sealed-letters-3": "faith-origins.01-roads-of-antioch.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three unique letter deliveries are registered.

ES: Tres entregas de cartas únicas están registradas.

EN: Keep their seals distinct; agreement is not required for safe delivery.

ES: Conserva sus sellos distintos; una entrega segura no exige acuerdo.

### o2 / phase-2

EN: Pay a single total of 200 food to provision the receiving households.

ES: Paga un único total de 200 de alimento para abastecer los hogares receptores.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 200
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.01-roads-of-antioch.destination-2"
      ],
      "allocations": {
        "faith-origins.01-roads-of-antioch.destination-2": {
          "food": 200
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.01-roads-of-antioch.o2.req-1.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Provision is recorded once without attacking neighboring households.

ES: La provisión se registra una vez sin atacar a los hogares vecinos.

EN: A household should not have to agree with its courier to receive bread.

ES: Un hogar no debería tener que dar la razón a su correo para recibir pan.

### o3 / phase-3

EN: Bring the returning courier alive to the gate beside Silpius.

ES: Lleva con vida al correo de regreso a la puerta junto al Silpio.

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
        "faith-origins.01-roads-of-antioch.returning-courier-1"
      ],
      "destinations": {
        "faith-origins.01-roads-of-antioch.returning-courier-1": "faith-origins.01-roads-of-antioch.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The distinct returning courier has reached the receiving gate.

ES: El correo de regreso distinto ha llegado a la puerta receptora.

EN: Let him carry a reply; do not make it say what the archive cannot know.

ES: Deja que lleve una respuesta; no le hagas decir lo que el archivo desconoce.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/01-roads-of-antioch.svg)

```json
{
  "bbox": [
    36.05,
    36.1,
    36.25,
    36.3
  ],
  "terrainProfile": "antioch",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        181.71,
        93.83
      ],
      "lonLat": [
        36.16,
        36.25
      ],
      "name": {
        "en": "North valley dispatch",
        "es-ES": "Envío del valle norte"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        182.93,
        160.42
      ],
      "lonLat": [
        36.161,
        36.206
      ],
      "name": {
        "en": "Eastern city receiving court",
        "es-ES": "Patio receptor urbano oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        200.03,
        184.63
      ],
      "lonLat": [
        36.175,
        36.19
      ],
      "name": {
        "en": "Silpius-side return gate",
        "es-ES": "Puerta de regreso junto al Silpio"
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
  "terrainInstructions": "All three main districts lie on the city/Silpius side of the Orontes. River remains real west of this itinerary; no fictional bridge for the alternative path. Slopes east/south, no later basilicas.",
  "mainRouteLengthStraightTiles": 96.24,
  "interestSpacingTiles": [
    25,
    55
  ],
  "minimumUsableAreaFraction": 0.45,
  "activeAreaPolicy": "main districts, finite supply hinterland and six optional circuits; survey usable terrain, not rectangle area",
  "geometryStatus": "georeferenced proposal; neither raster/DEM nor native footprint/pathfinding certified",
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/01-roads-of-antioch.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.01-roads-of-antioch.sealed-letters-1",
      "role": "fictional-community-letter",
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
      "generationPolicy": "preplaced and available"
    },
    {
      "id": "faith-origins.01-roads-of-antioch.sealed-letters-2",
      "role": "fictional-community-letter",
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
      "generationPolicy": "preplaced and available"
    },
    {
      "id": "faith-origins.01-roads-of-antioch.sealed-letters-3",
      "role": "fictional-community-letter",
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
      "generationPolicy": "preplaced and available"
    },
    {
      "id": "faith-origins.01-roads-of-antioch.returning-courier-1",
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
      "generationPolicy": "preplaced and available"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.01-roads-of-antioch.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.01-roads-of-antioch.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.01-roads-of-antioch.destination-3",
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
    "sealed-letters": [
      "faith-origins.01-roads-of-antioch.sealed-letters-1",
      "faith-origins.01-roads-of-antioch.sealed-letters-2",
      "faith-origins.01-roads-of-antioch.sealed-letters-3"
    ],
    "returning-courier": [
      "faith-origins.01-roads-of-antioch.returning-courier-1"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Six optional tasks and three combinable playstyles

### Riverside households / Hogares junto al río

EN: Bring each of the two aid crates to its assigned household at riverside households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares junto al río. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid is independent of disputed table fellowship.

ES: El auxilio es independiente de la disputa sobre comidas.

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
          "01-roads-of-antioch.side-1.entity-1",
          "01-roads-of-antioch.side-1.entity-2"
        ],
        "destinations": {
          "01-roads-of-antioch.side-1.entity-1": "01-roads-of-antioch.side-1.zone-1",
          "01-roads-of-antioch.side-1.entity-2": "01-roads-of-antioch.side-1.zone-2"
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
        "id": "01-roads-of-antioch.side-1.entity-1",
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
        "id": "01-roads-of-antioch.side-1.entity-2",
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
        "id": "01-roads-of-antioch.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "01-roads-of-antioch.side-1.zone-2",
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
      "onceFlag": "01-roads-of-antioch.side-1.rewarded",
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

### Distinct letter labels / Etiquetas de cartas distintas

EN: Recover both separate copies from distinct letter labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de etiquetas de cartas distintas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Two copies preserve attributed disagreement.

ES: Dos copias conservan el desacuerdo atribuido.

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
          "01-roads-of-antioch.side-2.entity-1",
          "01-roads-of-antioch.side-2.entity-2"
        ],
        "destinations": {
          "01-roads-of-antioch.side-2.entity-1": "01-roads-of-antioch.side-2.zone-1",
          "01-roads-of-antioch.side-2.entity-2": "01-roads-of-antioch.side-2.zone-1"
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
        "id": "01-roads-of-antioch.side-2.entity-1",
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
        "id": "01-roads-of-antioch.side-2.entity-2",
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
        "id": "01-roads-of-antioch.side-2.zone-1",
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
      "onceFlag": "01-roads-of-antioch.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.01-roads-of-antioch"
      ],
      "historicalNote": {
        "en": "Acts describes a community at Antioch and an aid shipment to Judea. Its travelers and charitable network provide the narrative context; this local courier circuit is fictional and its conventional dating is reconstructed.",
        "es-ES": "Hechos describe una comunidad en Antioquía y una remesa de ayuda a Judea. Sus viajeros y su red de auxilio aportan el contexto narrativo; el circuito local de correos es ficticio y su fecha convencional se reconstruye."
      },
      "hint": {
        "en": "Bring all three sealed letters to the eastern city receiving court.",
        "es-ES": "Lleva las tres cartas selladas al patio receptor oriental de la ciudad."
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

### Road storehouse / Almacén del camino

EN: Pay 50 wood and restore the damaged store of road storehouse to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén del camino. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repairs improve finite provision.

ES: Las reparaciones mejoran suministros finitos.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "01-roads-of-antioch.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "01-roads-of-antioch.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "01-roads-of-antioch.side-3.payment",
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
        "id": "01-roads-of-antioch.side-3.entity-1",
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
        "id": "01-roads-of-antioch.side-3.zone-1",
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
      "onceFlag": "01-roads-of-antioch.side-3.rewarded",
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

### Valley grain trader / Comerciante de grano del valle

EN: Escort the trader of valley grain trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de comerciante de grano del valle hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Local trade avoids inventing an army.

ES: El intercambio local evita inventar un ejército.

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
          "01-roads-of-antioch.side-4.entity-1"
        ],
        "destinations": {
          "01-roads-of-antioch.side-4.entity-1": "01-roads-of-antioch.side-4.zone-1"
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
        "receipt": "01-roads-of-antioch.side-4.payment",
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
        "id": "01-roads-of-antioch.side-4.entity-1",
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
        "id": "01-roads-of-antioch.side-4.zone-1",
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
      "onceFlag": "01-roads-of-antioch.side-4.rewarded",
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

### Silpius road guide / Guía del camino del Silpio

EN: Escort the local guide of silpius road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía del camino del silpio hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: Alternative route stays east of the river.

ES: La ruta alternativa permanece al este del río.

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
          "01-roads-of-antioch.side-5.entity-1"
        ],
        "destinations": {
          "01-roads-of-antioch.side-5.entity-1": "01-roads-of-antioch.side-5.zone-1"
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
        "id": "01-roads-of-antioch.side-5.entity-1",
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
        "id": "01-roads-of-antioch.side-5.zone-1",
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
      "onceFlag": "01-roads-of-antioch.side-5.rewarded",
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

### Visiting households / Hogares visitantes

EN: Bring both voluntary evacuee groups from visiting households to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de hogares visitantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Voluntary lodging does not resolve doctrine.

ES: El alojamiento voluntario no resuelve doctrinas.

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
          "01-roads-of-antioch.side-6.entity-1",
          "01-roads-of-antioch.side-6.entity-2"
        ],
        "destinations": {
          "01-roads-of-antioch.side-6.entity-1": "01-roads-of-antioch.side-6.zone-1",
          "01-roads-of-antioch.side-6.entity-2": "01-roads-of-antioch.side-6.zone-1"
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
        "id": "01-roads-of-antioch.side-6.entity-1",
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
        "id": "01-roads-of-antioch.side-6.entity-2",
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
        "id": "01-roads-of-antioch.side-6.zone-1",
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
      "onceFlag": "01-roads-of-antioch.side-6.rewarded",
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
      "food": 1418,
      "wood": 708,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 200,
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
      "food": 1270,
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
      "food": 1470,
      "wood": 730,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 200,
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
      "food": 1270,
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
      "food": 1523,
      "wood": 753,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 200,
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
      "food": 1270,
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
| scenario.faith-origins.01-roads-of-antioch.odyssey.title / always | none | Letters on the Orontes | Cartas sobre el Orontes |
| scenario.faith-origins.01-roads-of-antioch.odyssey.fact-intro / intro first | collection-narrator | Acts describes a community at Antioch and an aid shipment to Judea. Its travelers and charitable network provide the narrative context; this local courier circuit is fictional and its conventional dating is reconstructed. | Hechos describe una comunidad en Antioquía y una remesa de ayuda a Judea. Sus viajeros y su red de auxilio aportan el contexto narrativo; el circuito local de correos es ficticio y su fecha convencional se reconstruye. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.persona-intro / after handover | miriam-archive | My grandmother kept letters that disagreed. She would not let me scrape away the difficult lines just to make the shelf look peaceful. | Mi abuela conservaba cartas que discrepaban. No me dejaba raspar las líneas difíciles para que el estante pareciera pacífico. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.historical-license / after persona-intro | none | The named gameplay workers, objects, quantities and routes are fictional local reconstruction. Historical persons remain in the attributed narration. | Los trabajadores, objetos, cantidades y rutas jugables son una reconstrucción local ficticia. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.route-help / available from start; repeatable without effect | none | Use the city-side roads between the valley, receiving court and Silpius gate. The alternative path stays on the same river bank. | Usa los caminos del lado de la ciudad entre el valle, el patio y la puerta del Silpio. El sendero alternativo permanece en la misma orilla. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.o1-goal / phase-1 active | none | Bring all three sealed letters to the eastern city receiving court. | Lleva las tres cartas selladas al patio receptor oriental de la ciudad. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.o1-receipt / o1 latched once | none | Three unique letter deliveries are registered. | Tres entregas de cartas únicas están registradas. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.o1-reaction / after o1 receipt | miriam-archive | Keep their seals distinct; agreement is not required for safe delivery. | Conserva sus sellos distintos; una entrega segura no exige acuerdo. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.o2-goal / phase-2 active | none | Pay a single total of 200 food to provision the receiving households. | Paga un único total de 200 de alimento para abastecer los hogares receptores. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.o2-receipt / o2 latched once | none | Provision is recorded once without attacking neighboring households. | La provisión se registra una vez sin atacar a los hogares vecinos. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.o2-reaction / after o2 receipt | miriam-archive | A household should not have to agree with its courier to receive bread. | Un hogar no debería tener que dar la razón a su correo para recibir pan. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.o3-goal / phase-3 active | none | Bring the returning courier alive to the gate beside Silpius. | Lleva con vida al correo de regreso a la puerta junto al Silpio. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.o3-receipt / o3 latched once | none | The distinct returning courier has reached the receiving gate. | El correo de regreso distinto ha llegado a la puerta receptora. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.o3-reaction / after o3 receipt | miriam-archive | Let him carry a reply; do not make it say what the archive cannot know. | Deja que lleve una respuesta; no le hagas decir lo que el archivo desconoce. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at riverside households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares junto al río. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-1-complete / side-1 completed | none | Riverside households completed. Its stated benefit has been granted once. | Hogares junto al río: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-1-lost / side-1 failed-optional | none | Riverside households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares junto al río: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from distinct letter labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de etiquetas de cartas distintas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-2-complete / side-2 completed | none | Distinct letter labels completed. Its stated benefit has been granted once. | Etiquetas de cartas distintas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-2-lost / side-2 failed-optional | none | Distinct letter labels is unavailable after the loss of its unique participant or object. The main mission continues. | Etiquetas de cartas distintas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of road storehouse to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén del camino. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-3-complete / side-3 completed | none | Road storehouse completed. Its stated benefit has been granted once. | Almacén del camino: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-3-lost / side-3 failed-optional | none | Road storehouse is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén del camino: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-4-goal / optional list from start | none | Escort the trader of valley grain trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de comerciante de grano del valle hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-4-complete / side-4 completed | none | Valley grain trader completed. Its stated benefit has been granted once. | Comerciante de grano del valle: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-4-lost / side-4 failed-optional | none | Valley grain trader is unavailable after the loss of its unique participant or object. The main mission continues. | Comerciante de grano del valle: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-5-goal / optional list from start | none | Escort the local guide of silpius road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía del camino del silpio hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-5-complete / side-5 completed | none | Silpius road guide completed. Its stated benefit has been granted once. | Guía del camino del Silpio: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-5-lost / side-5 failed-optional | none | Silpius road guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del camino del Silpio: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from visiting households to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de hogares visitantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-6-complete / side-6 completed | none | Visiting households completed. Its stated benefit has been granted once. | Hogares visitantes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.side-6-lost / side-6 failed-optional | none | Visiting households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares visitantes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.fact-outro / victory first | collection-narrator | The local circuit changes no documented historical outcome. Acts and Paul’s later account of disagreement remain separately attributed sources; deliveries do not establish uniform beliefs. | El circuito local no cambia ningún desenlace histórico documentado. Hechos y el relato paulino posterior de desacuerdo siguen atribuidos por separado; las entregas no prueban creencias uniformes. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.persona-outro / after fact-outro | miriam-archive | A road may be safe while the words carried along it remain difficult. We need to preserve both truths. | Un camino puede ser seguro aunque las palabras que viajan por él sigan siendo difíciles. Debemos conservar ambas cosas. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.01-roads-of-antioch.odyssey.next-episode / after persona-outro | none | Continue with The Doors That Closed. This episode does not complete the campaign. | Continúa con Las puertas que se cerraron. Este episodio no termina la campaña. |

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
      "same letter cannot fill two identities",
      "no army generated to dramatize theological disagreement",
      "baseline semantic ID remains unchanged",
      "alternative road does not cross the river",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
