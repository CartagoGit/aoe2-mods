# 16. A Story in the Shadow of War

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `16-comparative-copying-antioch` · c. 65–70 CE; authorial location not known · 360×360

## Historical frame and fixed outcome

EN: Mark begins with John’s proclamation and presents Jesus’ baptism and ministry. The text does not state its writing place. Its date around 65–70 is an approximate scholarly frame; this Antioch copying scene is fiction, not the author’s desk.

ES: Marcos comienza con la proclamación de Juan y presenta el bautismo y ministerio de Jesús. El texto no indica su lugar de escritura. La fecha hacia 65–70 es un marco académico aproximado; esta escena de copias en Antioquía es ficticia, no la mesa del autor.

EN: The fictional local copying circuit has preserved separate working notes. Its success establishes neither the date and place of Mark’s composition nor the historical truth of every narrated action.

ES: El circuito local ficticio de copias ha conservado notas de trabajo separadas. Su éxito no determina fecha y lugar de composición de Marcos ni la historicidad de todas las acciones narradas.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 9,
      "episodeId": "16-comparative-copying-antioch",
      "order": 16,
      "selectedSourceUrl": "https://academic.oup.com/book/3544",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Mark+1&version=NRSVUE",
      "passage": "Mark 1:1–15 as opening and narrative evidence for the Gospel's representation of Jesus; Oxford title page is metadata/abstract only, not full-text chapter evidence.",
      "supportedClaim": {
        "en": "The Gospel of Mark presents a narrative about Jesus and locates its opening in a Second Temple Jewish setting.",
        "es-ES": "El Evangelio de Marcos presenta un relato sobre Jesús y sitúa su comienzo en el contexto judío del Segundo Templo."
      },
      "limitations": "Mark's date is commonly placed around the Jewish War but debated; text does not identify its author or place of composition. Do not state that this source proves it was written during the war or in Antioch.",
      "consultationDate": "2026-10-12",
      "status": "disputed",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Mark+1&version=NRSVUE",
      "passage": "Mark1; architect read chapter and footnotes",
      "limitations": "Textual opening and attributed ministry narrative; not composition date/place, local Antioch manuscript, or proof of every miracle.",
      "consultationDate": "2026-10-13",
      "status": "architect consulted; independent approval pending"
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

EN: Collect three distinct local working notes and take all three to the copying court.

ES: Recoge tres notas locales distintas y lleva las tres al patio de copias.

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
        "faith-origins.16-comparative-copying-antioch.local-working-notes-1",
        "faith-origins.16-comparative-copying-antioch.local-working-notes-2",
        "faith-origins.16-comparative-copying-antioch.local-working-notes-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.16-comparative-copying-antioch.local-working-notes-1",
        "faith-origins.16-comparative-copying-antioch.local-working-notes-2",
        "faith-origins.16-comparative-copying-antioch.local-working-notes-3"
      ],
      "destinations": {
        "faith-origins.16-comparative-copying-antioch.local-working-notes-1": "faith-origins.16-comparative-copying-antioch.destination-2",
        "faith-origins.16-comparative-copying-antioch.local-working-notes-2": "faith-origins.16-comparative-copying-antioch.destination-2",
        "faith-origins.16-comparative-copying-antioch.local-working-notes-3": "faith-origins.16-comparative-copying-antioch.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three original working identities are at the copying court.

ES: Tres identidades originales de trabajo están en el patio de copias.

EN: Their existence belongs to our fiction; their labels cannot prove where Mark wrote.

ES: Su existencia pertenece a nuestra ficción; sus etiquetas no prueban dónde escribió Marcos.

### o2 / phase-2

EN: Pay 60 wood and 20 gold once, then create two labelled copies from the three collected notes.

ES: Paga una vez 60 de madera y 20 de oro y después crea dos copias etiquetadas a partir de las tres notas recogidas.

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
        "faith-origins.16-comparative-copying-antioch.destination-2"
      ],
      "allocations": {
        "faith-origins.16-comparative-copying-antioch.destination-2": {
          "wood": 60,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.16-comparative-copying-antioch.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "faith-origins.16-comparative-copying-antioch.local-working-notes-1",
        "faith-origins.16-comparative-copying-antioch.local-working-notes-2",
        "faith-origins.16-comparative-copying-antioch.local-working-notes-3"
      ],
      "outputEntities": [
        "faith-origins.16-comparative-copying-antioch.labelled-copies-1",
        "faith-origins.16-comparative-copying-antioch.labelled-copies-2"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.16-comparative-copying-antioch.o2.req-1.paid",
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

EN: An exact payment receipt precedes both derived copy identities.

ES: Un recibo exacto de pago precede a ambas identidades derivadas.

EN: A second copy is not a second independent ancient source.

ES: Una segunda copia no es una segunda fuente antigua independiente.

### o3 / phase-3

EN: Deliver both labelled copies to the northern preservation court.

ES: Entrega ambas copias etiquetadas al patio septentrional de conservación.

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
        "faith-origins.16-comparative-copying-antioch.labelled-copies-1",
        "faith-origins.16-comparative-copying-antioch.labelled-copies-2"
      ],
      "destinations": {
        "faith-origins.16-comparative-copying-antioch.labelled-copies-1": "faith-origins.16-comparative-copying-antioch.destination-3",
        "faith-origins.16-comparative-copying-antioch.labelled-copies-2": "faith-origins.16-comparative-copying-antioch.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both distinct copies arrived, with their local provenance unchanged.

ES: Ambas copias distintas han llegado conservando su procedencia local.

EN: I will leave the unknown place in the margin. It is not mine to invent as history.

ES: Dejaré el lugar desconocido en el margen. No me corresponde inventarlo como historia.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/16-comparative-copying-antioch.svg)

```json
{
  "bbox": [
    36.14,
    36.18,
    36.205,
    36.245
  ],
  "terrainProfile": "antioch",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        209.34,
        191.83
      ],
      "lonLat": [
        36.18,
        36.21
      ],
      "name": {
        "en": "Eastern local receiving yard",
        "es-ES": "Patio receptor local oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        229.23,
        290.45
      ],
      "lonLat": [
        36.185,
        36.19
      ],
      "name": {
        "en": "Southern copying court",
        "es-ES": "Patio de copias meridional"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        201.38,
        68.55
      ],
      "lonLat": [
        36.178,
        36.235
      ],
      "name": {
        "en": "Northern preservation court",
        "es-ES": "Patio septentrional de conservación"
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
  "terrainInstructions": "Local Antioch districts east of the schematic Orontes city reach, below or north of Silpius slopes as appropriate. No invented crossing, modern Antakya street grid, fourth-century basilica or later fortress. Exact terrain elevation, ancient banks and footprint checks pending. All local activities are fictional; long-distance journeys remain off-map.",
  "mainRouteLengthStraightTiles": 324.25,
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
        36.17,
        36.1
      ],
      [
        36.16,
        36.19
      ],
      [
        36.155,
        36.205
      ],
      [
        36.135,
        36.25
      ],
      [
        36.07,
        36.29
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
  "asset": "docs/design/maps/faith-origins/odyssey/16-comparative-copying-antioch.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.16-comparative-copying-antioch.local-working-notes-1",
      "role": "fictional-local-circulation-note",
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
      "id": "faith-origins.16-comparative-copying-antioch.local-working-notes-2",
      "role": "fictional-local-circulation-note",
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
      "id": "faith-origins.16-comparative-copying-antioch.local-working-notes-3",
      "role": "fictional-local-circulation-note",
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
      "id": "faith-origins.16-comparative-copying-antioch.labelled-copies-1",
      "role": "fictional-labelled-working-copy",
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
      "id": "faith-origins.16-comparative-copying-antioch.labelled-copies-2",
      "role": "fictional-labelled-working-copy",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.16-comparative-copying-antioch.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.16-comparative-copying-antioch.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.16-comparative-copying-antioch.destination-3",
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
    "local-working-notes": [
      "faith-origins.16-comparative-copying-antioch.local-working-notes-1",
      "faith-origins.16-comparative-copying-antioch.local-working-notes-2",
      "faith-origins.16-comparative-copying-antioch.local-working-notes-3"
    ],
    "labelled-copies": [
      "faith-origins.16-comparative-copying-antioch.labelled-copies-1",
      "faith-origins.16-comparative-copying-antioch.labelled-copies-2"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Northern storage survey / Reconocimiento del depósito norte

EN: Scout both marked viewpoints of northern storage survey. Benefit: reveal the second reserve approach.

ES: Explora los dos miradores señalados de reconocimiento del depósito norte. Ventaja: revela la aproximación de la segunda reserva.

EN: Survey two real land approaches before dispatch; no authorial birthplace is revealed.

ES: Reconoce dos accesos terrestres antes del envío; no se revela un lugar de nacimiento autoral.

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
          "16-comparative-copying-antioch.side-1.zone-1",
          "16-comparative-copying-antioch.side-1.zone-2"
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
        "id": "16-comparative-copying-antioch.side-1.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "16-comparative-copying-antioch.side-1.zone-2",
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
      "kind": "reveal-enemy-approach",
      "target": "wave-2 approach",
      "resources": {},
      "onceFlag": "16-comparative-copying-antioch.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "rosterIds": [
        "wave-2"
      ],
      "alreadyReleasedPolicy": "reveal current surviving members, never spawn a replacement"
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
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Independent labels / Etiquetas independientes

EN: Recover both separate copies from independent labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de etiquetas independientes y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Optional local notes preserve attribution without supplying mandatory notes.

ES: Las notas locales opcionales conservan atribución sin suplir las principales.

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
          "16-comparative-copying-antioch.side-2.entity-1",
          "16-comparative-copying-antioch.side-2.entity-2"
        ],
        "destinations": {
          "16-comparative-copying-antioch.side-2.entity-1": "16-comparative-copying-antioch.side-2.zone-1",
          "16-comparative-copying-antioch.side-2.entity-2": "16-comparative-copying-antioch.side-2.zone-1"
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
        "id": "16-comparative-copying-antioch.side-2.entity-1",
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
        "id": "16-comparative-copying-antioch.side-2.entity-2",
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
        "id": "16-comparative-copying-antioch.side-2.zone-1",
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
      "onceFlag": "16-comparative-copying-antioch.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.16-comparative-copying-antioch"
      ],
      "historicalNote": {
        "en": "Mark begins with John’s proclamation and presents Jesus’ baptism and ministry. The text does not state its writing place. Its date around 65–70 is an approximate scholarly frame; this Antioch copying scene is fiction, not the author’s desk.",
        "es-ES": "Marcos comienza con la proclamación de Juan y presenta el bautismo y ministerio de Jesús. El texto no indica su lugar de escritura. La fecha hacia 65–70 es un marco académico aproximado; esta escena de copias en Antioquía es ficticia, no la mesa del autor."
      },
      "hint": {
        "en": "Collect three distinct local working notes and take all three to the copying court.",
        "es-ES": "Recoge tres notas locales distintas y lleva las tres al patio de copias."
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

### Copying shelter / Cobertizo de copias

EN: Pay 50 wood and restore the damaged store of copying shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de cobertizo de copias. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Separate roof repair releases bounded work stock.

ES: La reparación separada del tejado libera existencias limitadas.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "16-comparative-copying-antioch.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "16-comparative-copying-antioch.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "16-comparative-copying-antioch.side-3.payment",
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
        "id": "16-comparative-copying-antioch.side-3.entity-1",
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
        "id": "16-comparative-copying-antioch.side-3.zone-1",
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
      "onceFlag": "16-comparative-copying-antioch.side-3.rewarded",
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

### Local paper consignment / Remesa local de material de escritura

EN: Escort the trader of local paper consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de remesa local de material de escritura hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One fictional exchange funds a detour, not a purchase of canonical authority.

ES: Un intercambio ficticio apoya un desvío, no compra autoridad canónica.

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
          "16-comparative-copying-antioch.side-4.entity-1"
        ],
        "destinations": {
          "16-comparative-copying-antioch.side-4.entity-1": "16-comparative-copying-antioch.side-4.zone-1"
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
        "receipt": "16-comparative-copying-antioch.side-4.payment",
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
        "id": "16-comparative-copying-antioch.side-4.entity-1",
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
        "id": "16-comparative-copying-antioch.side-4.zone-1",
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
      "onceFlag": "16-comparative-copying-antioch.side-4.rewarded",
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

### Roadside working households / Hogares trabajadores del camino

EN: Bring each of the two aid crates to its assigned household at roadside working households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares trabajadores del camino. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid is independent from the copying contract.

ES: La ayuda es independiente del contrato de copias.

```json
{
  "id": "side-5",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "16-comparative-copying-antioch.side-5.entity-1",
          "16-comparative-copying-antioch.side-5.entity-2"
        ],
        "destinations": {
          "16-comparative-copying-antioch.side-5.entity-1": "16-comparative-copying-antioch.side-5.zone-1",
          "16-comparative-copying-antioch.side-5.entity-2": "16-comparative-copying-antioch.side-5.zone-2"
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
        "id": "16-comparative-copying-antioch.side-5.entity-1",
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
        "id": "16-comparative-copying-antioch.side-5.entity-2",
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
        "id": "16-comparative-copying-antioch.side-5.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "16-comparative-copying-antioch.side-5.zone-2",
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
      "onceFlag": "16-comparative-copying-antioch.side-5.rewarded",
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

### Valley-side guide / Guía del lado del valle

EN: Escort the local guide of valley-side guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía del lado del valle hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: A guide marks surveyed land access; never an unverified Orontes bridge.

ES: Un guía señala un acceso terrestre comprobado; nunca un puente del Orontes sin verificar.

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
          "16-comparative-copying-antioch.side-6.entity-1"
        ],
        "destinations": {
          "16-comparative-copying-antioch.side-6.entity-1": "16-comparative-copying-antioch.side-6.zone-1"
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
        "id": "16-comparative-copying-antioch.side-6.entity-1",
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
        "id": "16-comparative-copying-antioch.side-6.zone-1",
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
      "onceFlag": "16-comparative-copying-antioch.side-6.rewarded",
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
      "id": "provenance-first",
      "optionalObjectives": [
        "side-1",
        "side-2"
      ],
      "costOfOpportunity": "Survey and label first; do not confuse optional knowledge with required sources.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "copying-investment",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Reserve main 60 wood/20 gold before optional 50 wood/50 gold investments.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "care-and-navigation",
      "optionalObjectives": [
        "side-5",
        "side-6"
      ],
      "costOfOpportunity": "A separate team supports households and route guidance while notes are copied.",
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
      "wood": 768,
      "gold": 224,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 60,
      "gold": 20,
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
      "wood": 740,
      "gold": 310,
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
    "difficultyLevers": "12 workers; all main origins and receivers disclosed, separate labels and route markers.",
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
      "wood": 790,
      "gold": 235,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 60,
      "gold": 20,
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
      "wood": 740,
      "gold": 310,
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
    "difficultyLevers": "9 workers; split collection, gathering and dispatch teams under local fog.",
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
      "wood": 813,
      "gold": 247,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 60,
      "gold": 20,
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
      "wood": 740,
      "gold": 310,
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
    "difficultyLevers": "6 workers, lower finite starting stock; parallel teams and optional opportunity costs. No hidden recipient, forced secret deadline or invented army.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.title / always | none | A Story in the Shadow of War | Un relato a la sombra de la guerra |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.fact-intro / intro first | collection-narrator | Mark begins with John’s proclamation and presents Jesus’ baptism and ministry. The text does not state its writing place. Its date around 65–70 is an approximate scholarly frame; this Antioch copying scene is fiction, not the author’s desk. | Marcos comienza con la proclamación de Juan y presenta el bautismo y ministerio de Jesús. El texto no indica su lugar de escritura. La fecha hacia 65–70 es un marco académico aproximado; esta escena de copias en Antioquía es ficticia, no la mesa del autor. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.persona-intro / after handover | miriam-archive | A blank place on a label used to irritate me. I wanted to fill it. These inherited accounts taught me that leaving a place unknown can be more faithful than giving it a confident address. | Antes me irritaba un espacio vacío en una etiqueta. Quería llenarlo. Estos relatos heredados me enseñaron que dejar un lugar desconocido puede ser más fiel que darle una dirección demasiado segura. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.route-help / available from start; repeatable without effect | none | This is a local Antioch scene, not proof of where a text was composed. Keep the proposed routes on the city-side land bank; no required river crossing. | Es una escena local de Antioquía, no una prueba del lugar donde se compuso un texto. Mantén las rutas propuestas en tierra del lado urbano; no es necesario cruzar el río. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.o1-goal / phase-1 active | none | Collect three distinct local working notes and take all three to the copying court. | Recoge tres notas locales distintas y lleva las tres al patio de copias. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.o1-receipt / o1 latched once | none | Three original working identities are at the copying court. | Tres identidades originales de trabajo están en el patio de copias. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.o1-reaction / after o1 receipt | miriam-archive | Their existence belongs to our fiction; their labels cannot prove where Mark wrote. | Su existencia pertenece a nuestra ficción; sus etiquetas no prueban dónde escribió Marcos. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.o2-goal / phase-2 active | none | Pay 60 wood and 20 gold once, then create two labelled copies from the three collected notes. | Paga una vez 60 de madera y 20 de oro y después crea dos copias etiquetadas a partir de las tres notas recogidas. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.o2-receipt / o2 latched once | none | An exact payment receipt precedes both derived copy identities. | Un recibo exacto de pago precede a ambas identidades derivadas. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.o2-reaction / after o2 receipt | miriam-archive | A second copy is not a second independent ancient source. | Una segunda copia no es una segunda fuente antigua independiente. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.o3-goal / phase-3 active | none | Deliver both labelled copies to the northern preservation court. | Entrega ambas copias etiquetadas al patio septentrional de conservación. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.o3-receipt / o3 latched once | none | Both distinct copies arrived, with their local provenance unchanged. | Ambas copias distintas han llegado conservando su procedencia local. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.o3-reaction / after o3 receipt | miriam-archive | I will leave the unknown place in the margin. It is not mine to invent as history. | Dejaré el lugar desconocido en el margen. No me corresponde inventarlo como historia. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of northern storage survey. Benefit: reveal the second reserve approach. | Explora los dos miradores señalados de reconocimiento del depósito norte. Ventaja: revela la aproximación de la segunda reserva. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-1-complete / side-1 completed | none | Northern storage survey completed. Its stated benefit has been granted once. | Reconocimiento del depósito norte: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-1-lost / side-1 failed-optional | none | Northern storage survey is unavailable after the loss of its unique participant or object. The main mission continues. | Reconocimiento del depósito norte: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from independent labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de etiquetas independientes y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-2-complete / side-2 completed | none | Independent labels completed. Its stated benefit has been granted once. | Etiquetas independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-2-lost / side-2 failed-optional | none | Independent labels is unavailable after the loss of its unique participant or object. The main mission continues. | Etiquetas independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of copying shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de cobertizo de copias. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-3-complete / side-3 completed | none | Copying shelter completed. Its stated benefit has been granted once. | Cobertizo de copias: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-3-lost / side-3 failed-optional | none | Copying shelter is unavailable after the loss of its unique participant or object. The main mission continues. | Cobertizo de copias: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-4-goal / optional list from start | none | Escort the trader of local paper consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de remesa local de material de escritura hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-4-complete / side-4 completed | none | Local paper consignment completed. Its stated benefit has been granted once. | Remesa local de material de escritura: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-4-lost / side-4 failed-optional | none | Local paper consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Remesa local de material de escritura: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-5-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at roadside working households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares trabajadores del camino. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-5-complete / side-5 completed | none | Roadside working households completed. Its stated benefit has been granted once. | Hogares trabajadores del camino: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-5-lost / side-5 failed-optional | none | Roadside working households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares trabajadores del camino: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-6-goal / optional list from start | none | Escort the local guide of valley-side guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía del lado del valle hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-6-complete / side-6 completed | none | Valley-side guide completed. Its stated benefit has been granted once. | Guía del lado del valle: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.side-6-lost / side-6 failed-optional | none | Valley-side guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del lado del valle: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.fact-outro / victory first | collection-narrator | The fictional local copying circuit has preserved separate working notes. Its success establishes neither the date and place of Mark’s composition nor the historical truth of every narrated action. | El circuito local ficticio de copias ha conservado notas de trabajo separadas. Su éxito no determina fecha y lugar de composición de Marcos ni la historicidad de todas las acciones narradas. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.persona-outro / after fact-outro | miriam-archive | I kept the labels separate. I did not solve the century. A careful copyist must know which of those two tasks belongs to her. | Conservé separadas las etiquetas. No resolví el siglo. Una copista cuidadosa debe saber cuál de esas tareas le corresponde. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.16-comparative-copying-antioch.odyssey.next-episode / after persona-outro | none | Continue with The Names Beyond the Siege. This episode does not complete the campaign. | Continúa con Los nombres más allá del asedio. Este episodio no termina la campaña. |

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
      "all three original notes must arrive before objective1 latch",
      "copies cannot spawn before exact payment",
      "optional labels cannot supply main notes",
      "Antioch is not declared Mark’s composition site",
      "no first-century actor handles a modern critical edition",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
