# 10. Words over Alexandria

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `08-disputed-correspondence-alexandria` · 324–325 CE · 400×400

## Historical frame and fixed outcome

EN: Eusebius describes disputes in the Alexandrian church and transmits an imperial letter to Alexander and Arius urging concord. His narrative frames the letter after Constantine’s decisive victory and a Nicomedia visit, but gives no exact date. It also says the dispute continued. The author’s religious explanation and the letter’s dismissal of the controversy as minor are attributed positions. Our local working notice and courier are fiction, not the original imperial letter.

ES: Eusebio describe disputas en la iglesia alejandrina y transmite una carta imperial a Alejandro y Arrio que insta a la concordia. Su relato sitúa la carta tras la victoria decisiva de Constantino y una visita a Nicomedia, sin fecha exacta. También indica que la disputa continuó. La explicación religiosa del autor y la minimización de la controversia en la carta son posiciones atribuidas. Nuestro aviso local y mensajero son ficticios, no la carta imperial original.

EN: One fictional working notice reached both local receiving courts with the same courier, using observed departures after the first receipts. Two deliveries do not establish agreement. Eusebius reports the controversy continuing despite the transmitted imperial appeal; its exact date and reception beyond that account remain qualified.

ES: Un aviso ficticio de trabajo llegó a ambos patios receptores locales con el mismo mensajero, mediante salidas observadas tras los primeros recibos. Dos entregas no acreditan acuerdo. Eusebio refiere que la controversia continuó pese a la exhortación imperial transmitida; su fecha exacta y la recepción más allá de ese relato mantienen sus cautelas.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "consultedUrl": "https://www.newadvent.org/fathers/25022.htm",
      "passage": "Eusebius VC II.61–64 checked for dispute background and imperial intervention.",
      "limitations": "Eusebius’ account is selective and pro-Constantinian; date range 324–325 and the phrase “networks” are editorial synthesis, not an exact dated event.",
      "status": "consulted",
      "supportedClaim": "Supports a dispute involving Arius and Alexander that drew imperial correspondence and wider church attention in Eusebius’ narrative. / Apoya que la disputa entre Arrio y Alejandro atrajo correspondencia imperial y atención eclesiástica más amplia en el relato de Eusebio.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "VC II.61–64 checked; whole book not read.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/25022.htm",
      "passage": "VC II.61–73, especiallyII.67 andII.72 post-victory/Nicomedia framing andII.73 continued dispute",
      "coverageActuallyRead": "Architect read the displayed narrative, transmitted letter and continuation. II.69 includes apparent editorial/markup corruption; no corrupted wording is adopted or quoted.",
      "limitations": "Richardson1890 translation revised onNewAdvent; noGreek critical apparatus or exactletterdate. Eusebius is panegyrical; imperial characterization of the dispute as minor remains attributed, never the agnostic narrator’s verdict.",
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

EN: Collect both distinct original receiving-court context notes and deliver both to common dispatch.

ES: Recoge ambas notas originales distintas de contexto de los patios receptores y entrega ambas al despacho común.

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
        "imperial-church.08-disputed-correspondence-alexandria.north-context-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.08-disputed-correspondence-alexandria.north-context-note-1"
      ],
      "destinations": {
        "imperial-church.08-disputed-correspondence-alexandria.north-context-note-1": "imperial-church.08-disputed-correspondence-alexandria.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.08-disputed-correspondence-alexandria.east-context-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "imperial-church.08-disputed-correspondence-alexandria.east-context-note-1"
      ],
      "destinations": {
        "imperial-church.08-disputed-correspondence-alexandria.east-context-note-1": "imperial-church.08-disputed-correspondence-alexandria.destination-1"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both distinct original local context notes reached common dispatch.

ES: Ambas notas originales distintas de contexto local llegaron al despacho común.

EN: Two notes, two labels. My old title must wait for the particulars.

ES: Dos notas, dos etiquetas. Mi antiguo título tendrá que esperar a los detalles.

### o2 / phase-2

EN: Pay 80 wood and 20 gold once, then make one local working notice from both collected original notes.

ES: Paga una vez 80 de madera y 20 de oro, y prepara un aviso local de trabajo con ambas notas originales recogidas.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 80,
        "gold": 20
      },
      "id": "req-1",
      "receivingZones": [
        "imperial-church.08-disputed-correspondence-alexandria.destination-1"
      ],
      "allocations": {
        "imperial-church.08-disputed-correspondence-alexandria.destination-1": {
          "wood": 80,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.08-disputed-correspondence-alexandria.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "imperial-church.08-disputed-correspondence-alexandria.north-context-note-1",
        "imperial-church.08-disputed-correspondence-alexandria.east-context-note-1"
      ],
      "outputEntities": [
        "imperial-church.08-disputed-correspondence-alexandria.working-notice-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.08-disputed-correspondence-alexandria.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 80,
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

EN: One original derived local notice has its own exact funded receipt.

ES: Un aviso local derivado original tiene su recibo exacto de financiación.

EN: The workshop can make a notice. Agreement is not in its stock ledger.

ES: El taller puede hacer un aviso. El acuerdo no figura en su registro de existencias.

### o3 / phase-3

EN: Deliver the same original courier and the original working notice to the northern receiving court.

ES: Entrega el mismo mensajero original y el aviso original de trabajo en el patio receptor norteño.

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
        "imperial-church.08-disputed-correspondence-alexandria.original-courier-1"
      ],
      "destinations": {
        "imperial-church.08-disputed-correspondence-alexandria.original-courier-1": "imperial-church.08-disputed-correspondence-alexandria.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.08-disputed-correspondence-alexandria.working-notice-1"
      ],
      "destinations": {
        "imperial-church.08-disputed-correspondence-alexandria.working-notice-1": "imperial-church.08-disputed-correspondence-alexandria.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The original courier and original derived notice each have a northern arrival receipt.

ES: El mensajero original y el aviso derivado original tienen cada uno un recibo de llegada norteña.

EN: They opened the receiving door. I must not add a reconciled city to that small fact.

ES: Abrieron la puerta receptora. No debo añadir una ciudad reconciliada a ese pequeño hecho.

### o4 / phase-4

EN: After each identity’s own northern receipt, depart the original courier and original notice and deliver both to the eastern receiving court.

ES: Tras el recibo norteño propio de cada identidad, da salida al mensajero original y al aviso original, y entrega ambos en el patio receptor oriental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "ordered-departure",
      "receiptObjective": "o3",
      "receiptRequirement": "req-1",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-1",
      "departingEntities": [
        "imperial-church.08-disputed-correspondence-alexandria.original-courier-1"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-1"
      },
      "id": "req-2",
      "entities": [
        "imperial-church.08-disputed-correspondence-alexandria.original-courier-1"
      ],
      "destinations": {
        "imperial-church.08-disputed-correspondence-alexandria.original-courier-1": "imperial-church.08-disputed-correspondence-alexandria.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "ordered-departure",
      "receiptObjective": "o3",
      "receiptRequirement": "req-2",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-3",
      "departingEntities": [
        "imperial-church.08-disputed-correspondence-alexandria.working-notice-1"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-3"
      },
      "id": "req-4",
      "entities": [
        "imperial-church.08-disputed-correspondence-alexandria.working-notice-1"
      ],
      "destinations": {
        "imperial-church.08-disputed-correspondence-alexandria.working-notice-1": "imperial-church.08-disputed-correspondence-alexandria.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both same original identities arrived east after their own observed receipt-backed departures.

ES: Ambas mismas identidades originales llegaron al este tras sus propias salidas observadas respaldadas por recibo.

EN: Delivered twice is still a delivery account. The reply deserves its own line.

ES: Entregado dos veces sigue siendo una cuenta de entregas. La respuesta merece su propia línea.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/08-disputed-correspondence-alexandria.svg)

```json
{
  "bbox": [
    29.915,
    31.173,
    29.976,
    31.215
  ],
  "terrainProfile": "alexandria",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        120.66,
        213.15
      ],
      "lonLat": [
        29.932,
        31.192
      ],
      "name": {
        "en": "Common local work dispatch",
        "es-ES": "Despacho común local de trabajo"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        161.54,
        131.23
      ],
      "lonLat": [
        29.939,
        31.204
      ],
      "name": {
        "en": "Northern fictional receiving court",
        "es-ES": "Patio receptor ficticio norteño"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        307.54,
        138.05
      ],
      "lonLat": [
        29.964,
        31.203
      ],
      "name": {
        "en": "Eastern fictional receiving court",
        "es-ES": "Patio receptor ficticio oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        196.58,
        274.6
      ],
      "lonLat": [
        29.945,
        31.183
      ],
      "name": {
        "en": "Southern ordinary support court",
        "es-ES": "Patio sureño ordinario de apoyo"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-notice-chain",
      "hubOrder": [
        "hub-1",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-onward-chain",
      "hubOrder": [
        "hub-2",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "southern-support-circuit",
      "hubOrder": [
        "hub-1",
        "hub-4",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 8
    }
  ],
  "terrainInstructions": "Local mainland Alexandrian city band between the Mediterranean harbors to the north and the Lake Mareotis system farther south. Four fictional working/receiving courts remain on mainland land and do not identify an actual Alexander/Arius house, episcopal chamber or imperial messenger itinerary. No compulsory Heptastadion/Pharos crossing, harbor voyage or lake crossing. Ancient coastline subsidence, canal alignments, street phases and exact parcel elevations need archaeological/geological review; the CEAlex reconstructions span multiple periods. Do not import a Ptolemaic 300–100 BCE community map as the 324 street plan. Exclude Qaitbay fort, modern corniche, modern canals, railways and a modern excavated block as an intact ancient façade.",
  "corridorStraightLengthsTiles": {
    "north-notice-chain": 91.55,
    "east-onward-chain": 146.16,
    "southern-support-circuit": 273.62
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
  "asset": "docs/design/maps/imperial-church/odyssey/08-disputed-correspondence-alexandria.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.08-disputed-correspondence-alexandria.north-context-note-1",
      "role": "fictional-local-context-note",
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
      "id": "imperial-church.08-disputed-correspondence-alexandria.east-context-note-1",
      "role": "fictional-local-context-note",
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
      "id": "imperial-church.08-disputed-correspondence-alexandria.working-notice-1",
      "role": "fictional-local-working-notice",
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
      "id": "imperial-church.08-disputed-correspondence-alexandria.original-courier-1",
      "role": "fictional-original-local-courier",
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
    }
  ],
  "zones": [
    {
      "id": "imperial-church.08-disputed-correspondence-alexandria.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.08-disputed-correspondence-alexandria.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.08-disputed-correspondence-alexandria.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.08-disputed-correspondence-alexandria.destination-4",
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
    "north-context-note": [
      "imperial-church.08-disputed-correspondence-alexandria.north-context-note-1"
    ],
    "east-context-note": [
      "imperial-church.08-disputed-correspondence-alexandria.east-context-note-1"
    ],
    "working-notice": [
      "imperial-church.08-disputed-correspondence-alexandria.working-notice-1"
    ],
    "original-courier": [
      "imperial-church.08-disputed-correspondence-alexandria.original-courier-1"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.08-disputed-correspondence-alexandria.original-courier-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### The southern mainland circuit / El circuito continental sureño

EN: Scout both marked viewpoints of the southern mainland circuit. Benefit: Mark the proposed southern-support-circuit circuit once; all main receivers are already disclosed.

ES: Explora los dos miradores señalados de el circuito continental sureño. Ventaja: Señala una vez el circuito propuesto southern-support-circuit; todos los receptores principales ya se indican.

EN: Mark a proposed mainland alternative without identifying an actual imperial messenger route.

ES: Señala una alternativa continental propuesta sin identificar una ruta real del mensajero imperial.

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
          "08-disputed-correspondence-alexandria.side-1.zone-1",
          "08-disputed-correspondence-alexandria.side-1.zone-2"
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
        "id": "08-disputed-correspondence-alexandria.side-1.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "08-disputed-correspondence-alexandria.side-1.zone-2",
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
      "target": "southern-support-circuit proposed local mainland approach",
      "resources": {},
      "onceFlag": "08-disputed-correspondence-alexandria.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "southern-support-circuit"
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
      "north-notice-chain",
      "east-onward-chain",
      "southern-support-circuit"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### An appeal beside its reception / Una exhortación junto a su recepción

EN: Recover both separate copies from an appeal beside its reception and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de una exhortación junto a su recepción y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Optional context places the reported continuing dispute beside the transmitted appeal, not inside a contemporary copy of Eusebius.

ES: El contexto opcional pone la continuidad referida de la disputa junto a la exhortación transmitida, no en una copia contemporánea de Eusebio.

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
          "08-disputed-correspondence-alexandria.side-2.entity-1",
          "08-disputed-correspondence-alexandria.side-2.entity-2"
        ],
        "destinations": {
          "08-disputed-correspondence-alexandria.side-2.entity-1": "08-disputed-correspondence-alexandria.side-2.zone-1",
          "08-disputed-correspondence-alexandria.side-2.entity-2": "08-disputed-correspondence-alexandria.side-2.zone-1"
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
        "id": "08-disputed-correspondence-alexandria.side-2.entity-1",
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
        "id": "08-disputed-correspondence-alexandria.side-2.entity-2",
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
        "id": "08-disputed-correspondence-alexandria.side-2.zone-1",
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
      "onceFlag": "08-disputed-correspondence-alexandria.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.08-disputed-correspondence-alexandria"
      ],
      "historicalNote": {
        "en": "Eusebius describes disputes in the Alexandrian church and transmits an imperial letter to Alexander and Arius urging concord. His narrative frames the letter after Constantine’s decisive victory and a Nicomedia visit, but gives no exact date. It also says the dispute continued. The author’s religious explanation and the letter’s dismissal of the controversy as minor are attributed positions. Our local working notice and courier are fiction, not the original imperial letter.",
        "es-ES": "Eusebio describe disputas en la iglesia alejandrina y transmite una carta imperial a Alejandro y Arrio que insta a la concordia. Su relato sitúa la carta tras la victoria decisiva de Constantino y una visita a Nicomedia, sin fecha exacta. También indica que la disputa continuó. La explicación religiosa del autor y la minimización de la controversia en la carta son posiciones atribuidas. Nuestro aviso local y mensajero son ficticios, no la carta imperial original."
      },
      "hint": {
        "en": "Collect both distinct original receiving-court context notes and deliver both to common dispatch.",
        "es-ES": "Recoge ambas notas originales distintas de contexto de los patios receptores y entrega ambas al despacho común."
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
      "north-notice-chain",
      "east-onward-chain",
      "southern-support-circuit"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Neighbors between the doors / Vecinos entre las puertas

EN: Bring each of the two aid crates to its assigned household at neighbors between the doors. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en vecinos entre las puertas. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Voluntary ordinary aid accepts neither a theological verdict nor a faction score as payment.

ES: La ayuda ordinaria voluntaria no acepta un veredicto teológico ni puntuación de facción como pago.

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
          "08-disputed-correspondence-alexandria.side-3.entity-1",
          "08-disputed-correspondence-alexandria.side-3.entity-2"
        ],
        "destinations": {
          "08-disputed-correspondence-alexandria.side-3.entity-1": "08-disputed-correspondence-alexandria.side-3.zone-1",
          "08-disputed-correspondence-alexandria.side-3.entity-2": "08-disputed-correspondence-alexandria.side-3.zone-2"
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
        "id": "08-disputed-correspondence-alexandria.side-3.entity-1",
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
        "id": "08-disputed-correspondence-alexandria.side-3.entity-2",
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
        "id": "08-disputed-correspondence-alexandria.side-3.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "08-disputed-correspondence-alexandria.side-3.zone-2",
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
      "onceFlag": "08-disputed-correspondence-alexandria.side-3.rewarded",
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
      "north-notice-chain",
      "east-onward-chain",
      "southern-support-circuit"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The southern work shelter / El cobertizo sureño de trabajo

EN: Pay 50 wood and restore the damaged store of the southern work shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el cobertizo sureño de trabajo. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Separate shelter repair releases bounded ordinary stock without replacing the unique courier.

ES: La reparación separada libera existencias limitadas sin sustituir al mensajero único.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "08-disputed-correspondence-alexandria.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "08-disputed-correspondence-alexandria.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "08-disputed-correspondence-alexandria.side-4.payment",
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
        "id": "08-disputed-correspondence-alexandria.side-4.entity-1",
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
        "id": "08-disputed-correspondence-alexandria.side-4.zone-1",
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
      "onceFlag": "08-disputed-correspondence-alexandria.side-4.rewarded",
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
      "north-notice-chain",
      "east-onward-chain",
      "southern-support-circuit"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A finite writing-material consignment / Una remesa finita de material de escritura

EN: Escort the trader of a finite writing-material consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de una remesa finita de material de escritura hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One exchange supports ordinary work; no conversion, bishop influence or communal assent is purchased.

ES: Un intercambio apoya trabajo ordinario; no compra conversión, influencia episcopal ni asentimiento comunitario.

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
          "08-disputed-correspondence-alexandria.side-5.entity-1"
        ],
        "destinations": {
          "08-disputed-correspondence-alexandria.side-5.entity-1": "08-disputed-correspondence-alexandria.side-5.zone-1"
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
        "receipt": "08-disputed-correspondence-alexandria.side-5.payment",
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
        "id": "08-disputed-correspondence-alexandria.side-5.entity-1",
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
        "id": "08-disputed-correspondence-alexandria.side-5.zone-1",
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
      "onceFlag": "08-disputed-correspondence-alexandria.side-5.rewarded",
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
      "north-notice-chain",
      "east-onward-chain",
      "southern-support-circuit"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### From the first door to the second / De la primera puerta a la segunda

EN: Escort the local guide of from the first door to the second to the marked road junction. Benefit: Mark the proposed east-onward-chain circuit once; all main receivers are already disclosed.

ES: Escolta al guía local de de la primera puerta a la segunda hasta el cruce señalado. Ventaja: Señala una vez el circuito propuesto east-onward-chain; todos los receptores principales ya se indican.

EN: Mark the disclosed eastward local land approach; neither an imperial path reconstruction nor a theological solution.

ES: Señala el acceso terrestre local oriental indicado; no reconstruye un trayecto imperial ni resuelve teología.

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
          "08-disputed-correspondence-alexandria.side-6.entity-1"
        ],
        "destinations": {
          "08-disputed-correspondence-alexandria.side-6.entity-1": "08-disputed-correspondence-alexandria.side-6.zone-1"
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
        "id": "08-disputed-correspondence-alexandria.side-6.entity-1",
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
        "id": "08-disputed-correspondence-alexandria.side-6.zone-1",
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
      "target": "east-onward-chain proposed local mainland approach",
      "resources": {},
      "onceFlag": "08-disputed-correspondence-alexandria.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "east-onward-chain"
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
      "north-notice-chain",
      "east-onward-chain",
      "southern-support-circuit"
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
      "id": "direct-two-door-dispatch",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Collect from both courts, fund the notice and run the guarded north-then-east courier chain using route information.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "workshop-and-context",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Read reception limits and support the separate workshop while reserving80wood/20gold main funding.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "neighbors-and-materials",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Use a separate support team for households/trade while the unique courier carries the original notice.",
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
      "wood": 788,
      "gold": 224,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
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
      "wood": 760,
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
      "wood": 810,
      "gold": 235,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
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
      "wood": 760,
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
      "wood": 833,
      "gold": 247,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
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
      "wood": 760,
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
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.title / always | none | Words over Alexandria | Palabras sobre Alejandría |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.fact-intro / intro first | collection-narrator | Eusebius describes disputes in the Alexandrian church and transmits an imperial letter to Alexander and Arius urging concord. His narrative frames the letter after Constantine’s decisive victory and a Nicomedia visit, but gives no exact date. It also says the dispute continued. The author’s religious explanation and the letter’s dismissal of the controversy as minor are attributed positions. Our local working notice and courier are fiction, not the original imperial letter. | Eusebio describe disputas en la iglesia alejandrina y transmite una carta imperial a Alejandro y Arrio que insta a la concordia. Su relato sitúa la carta tras la victoria decisiva de Constantino y una visita a Nicomedia, sin fecha exacta. También indica que la disputa continuó. La explicación religiosa del autor y la minimización de la controversia en la carta son posiciones atribuidas. Nuestro aviso local y mensajero son ficticios, no la carta imperial original. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.persona-intro / after handover | imperial-clerk | In Milan I once copied a fine title and thought I had settled an argument. The next official changed the title; the argument kept its chair. These inherited Alexandrian pages trouble that younger clerk in me. An order may travel splendidly and arrive quite unable to do what its heading promises. Let us at least get our small notice to both doors. | En Milán copié una vez un título magnífico y creí haber resuelto una disputa. El siguiente funcionario cambió el título; la disputa conservó su silla. Estas páginas alejandrinas heredadas incomodan al joven escribiente que todavía llevo dentro. Una orden puede viajar espléndidamente y llegar incapaz de hacer lo que promete su encabezamiento. Llevemos al menos nuestro pequeño aviso a ambas puertas. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.route-help / available from start; repeatable without effect | none | Collect one original note from each of the two receiving courts and deliver both to common work dispatch. Pay 80 wood and 20 gold once to prepare one local working notice from those two notes. Bring that same notice and the original courier to the north receiving court. After each identity’s own north-arrival receipt, observe its departure, then deliver both original identities to the eastern court. An early eastern visit or a different courier cannot replace those guarded arrivals. Receiving the notice does not make either court agree. | Recoge una nota original de cada uno de los dos patios receptores y entrega ambas en el despacho común. Paga una vez 80 de madera y 20 de oro para preparar un aviso local con esas dos notas. Lleva ese mismo aviso y el mensajero original al patio receptor norteño. Tras el recibo de llegada norteña propio de cada identidad, observa su salida y entrega ambas identidades originales en el patio oriental. Una visita oriental temprana o un mensajero distinto no sustituye esas llegadas condicionadas. Recibir el aviso no hace que ningún patio esté de acuerdo. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o1-goal / phase-1 active | none | Collect both distinct original receiving-court context notes and deliver both to common dispatch. | Recoge ambas notas originales distintas de contexto de los patios receptores y entrega ambas al despacho común. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o1-receipt / o1 latched once | none | Both distinct original local context notes reached common dispatch. | Ambas notas originales distintas de contexto local llegaron al despacho común. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o1-reaction / after o1 receipt | imperial-clerk | Two notes, two labels. My old title must wait for the particulars. | Dos notas, dos etiquetas. Mi antiguo título tendrá que esperar a los detalles. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o2-goal / phase-2 active | none | Pay 80 wood and 20 gold once, then make one local working notice from both collected original notes. | Paga una vez 80 de madera y 20 de oro, y prepara un aviso local de trabajo con ambas notas originales recogidas. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o2-receipt / o2 latched once | none | One original derived local notice has its own exact funded receipt. | Un aviso local derivado original tiene su recibo exacto de financiación. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o2-reaction / after o2 receipt | imperial-clerk | The workshop can make a notice. Agreement is not in its stock ledger. | El taller puede hacer un aviso. El acuerdo no figura en su registro de existencias. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o3-goal / phase-3 active | none | Deliver the same original courier and the original working notice to the northern receiving court. | Entrega el mismo mensajero original y el aviso original de trabajo en el patio receptor norteño. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o3-receipt / o3 latched once | none | The original courier and original derived notice each have a northern arrival receipt. | El mensajero original y el aviso derivado original tienen cada uno un recibo de llegada norteña. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o3-reaction / after o3 receipt | imperial-clerk | They opened the receiving door. I must not add a reconciled city to that small fact. | Abrieron la puerta receptora. No debo añadir una ciudad reconciliada a ese pequeño hecho. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o4-goal / phase-4 active | none | After each identity’s own northern receipt, depart the original courier and original notice and deliver both to the eastern receiving court. | Tras el recibo norteño propio de cada identidad, da salida al mensajero original y al aviso original, y entrega ambos en el patio receptor oriental. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o4-receipt / o4 latched once | none | Both same original identities arrived east after their own observed receipt-backed departures. | Ambas mismas identidades originales llegaron al este tras sus propias salidas observadas respaldadas por recibo. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.o4-reaction / after o4 receipt | imperial-clerk | Delivered twice is still a delivery account. The reply deserves its own line. | Entregado dos veces sigue siendo una cuenta de entregas. La respuesta merece su propia línea. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of the southern mainland circuit. Benefit: Mark the proposed southern-support-circuit circuit once; all main receivers are already disclosed. | Explora los dos miradores señalados de el circuito continental sureño. Ventaja: Señala una vez el circuito propuesto southern-support-circuit; todos los receptores principales ya se indican. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-1-complete / side-1 completed | none | The southern mainland circuit completed. Its stated benefit has been granted once. | El circuito continental sureño: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-1-lost / side-1 failed-optional | none | The southern mainland circuit is unavailable after the loss of its unique participant or object. The main mission continues. | El circuito continental sureño: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from an appeal beside its reception and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de una exhortación junto a su recepción y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-2-complete / side-2 completed | none | An appeal beside its reception completed. Its stated benefit has been granted once. | Una exhortación junto a su recepción: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-2-lost / side-2 failed-optional | none | An appeal beside its reception is unavailable after the loss of its unique participant or object. The main mission continues. | Una exhortación junto a su recepción: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at neighbors between the doors. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en vecinos entre las puertas. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-3-complete / side-3 completed | none | Neighbors between the doors completed. Its stated benefit has been granted once. | Vecinos entre las puertas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-3-lost / side-3 failed-optional | none | Neighbors between the doors is unavailable after the loss of its unique participant or object. The main mission continues. | Vecinos entre las puertas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the southern work shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el cobertizo sureño de trabajo. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-4-complete / side-4 completed | none | The southern work shelter completed. Its stated benefit has been granted once. | El cobertizo sureño de trabajo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-4-lost / side-4 failed-optional | none | The southern work shelter is unavailable after the loss of its unique participant or object. The main mission continues. | El cobertizo sureño de trabajo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-5-goal / optional list from start | none | Escort the trader of a finite writing-material consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de una remesa finita de material de escritura hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-5-complete / side-5 completed | none | A finite writing-material consignment completed. Its stated benefit has been granted once. | Una remesa finita de material de escritura: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-5-lost / side-5 failed-optional | none | A finite writing-material consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Una remesa finita de material de escritura: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-6-goal / optional list from start | none | Escort the local guide of from the first door to the second to the marked road junction. Benefit: Mark the proposed east-onward-chain circuit once; all main receivers are already disclosed. | Escolta al guía local de de la primera puerta a la segunda hasta el cruce señalado. Ventaja: Señala una vez el circuito propuesto east-onward-chain; todos los receptores principales ya se indican. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-6-complete / side-6 completed | none | From the first door to the second completed. Its stated benefit has been granted once. | De la primera puerta a la segunda: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.side-6-lost / side-6 failed-optional | none | From the first door to the second is unavailable after the loss of its unique participant or object. The main mission continues. | De la primera puerta a la segunda: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.fact-outro / victory first | collection-narrator | One fictional working notice reached both local receiving courts with the same courier, using observed departures after the first receipts. Two deliveries do not establish agreement. Eusebius reports the controversy continuing despite the transmitted imperial appeal; its exact date and reception beyond that account remain qualified. | Un aviso ficticio de trabajo llegó a ambos patios receptores locales con el mismo mensajero, mediante salidas observadas tras los primeros recibos. Dos entregas no acreditan acuerdo. Eusebio refiere que la controversia continuó pese a la exhortación imperial transmitida; su fecha exacta y la recepción más allá de ese relato mantienen sus cautelas. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.persona-outro / after fact-outro | imperial-clerk | Both doors received our notice. Neither owes me harmony for the trouble. I will write “delivered” and leave room beside it. That room is for the answer a clerk cannot stamp into existence. | Ambas puertas recibieron nuestro aviso. Ninguna me debe armonía por el esfuerzo. Escribiré «entregado» y dejaré espacio a su lado. Ese espacio es para la respuesta que un funcionario no puede hacer existir con un sello. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.08-disputed-correspondence-alexandria.odyssey.next-episode / after persona-outro | none | Continue with Before the Lakeside Council. This episode does not complete the campaign. | Continúa con Antes del concilio junto al lago. Este episodio no termina la campaña. |

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
    "style": "sober Alexandrian mainland work courts, restrained Mediterranean light and ordinary civic life",
    "historicalControls": "no imperial autograph, exact private episcopal room, Qaitbay fort, later mosque or modern corniche; no Ptolemaic plan promoted as324 geometry",
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "two notes are distinct original identities; optional context cannot substitute",
      "notice generation requires its own exacto2 funded receipt and both collected inputs",
      "north receipt for courier cannot authorize notice departure or the reverse",
      "both guarded east arrivals require their own correcto4 departure evidence; an early visit fails",
      "a different courier or a second fabricated notice cannot satisfy the original identities",
      "save/load preserves each scoped departure and arrival without duplicating payments or production",
      "no historical Alexander/Arius units or imperial messenger identity is inferred from local court labels",
      "no ecclesiastical consensus, conversion or correct-theology meter",
      "letter stays after324 military sequence and its precise date remains qualified",
      "all mandatory and optional land paths require ancient-bank/parcel and in-game navigation audit",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
