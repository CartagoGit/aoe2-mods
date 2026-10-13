# 18. Two Voices, Unfinished Margins

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `18-parallel-archive-logistics-antioch` · c. 80–90 CE; location is fictional local circulation, not authorial provenance · 380×380

## Historical frame and fixed outcome

EN: Matthew and Luke preserve different genealogies: Matthew traces through Solomon, while Luke names Nathan. Their writing places and the precise dates proposed here remain debated. The two local archive chains in Antioch are fictional and cannot resolve those questions.

ES: Mateo y Lucas conservan genealogías diferentes: Mateo sigue a Salomón, mientras Lucas nombra a Natán. Sus lugares de escritura y las fechas precisas aquí propuestas siguen discutidos. Las dos cadenas locales de archivo en Antioquía son ficticias y no resuelven esas cuestiones.

EN: Two fictional local note collections remain distinct after delivery. They illustrate preserving different accounts; neither collection is a canonical autograph or evidence for a particular ancient audience in Antioch.

ES: Dos colecciones locales ficticias de notas permanecen distintas tras su entrega. Ilustran la conservación de relatos diferentes; ninguna es un autógrafo canónico ni prueba de un público antiguo concreto en Antioquía.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 11,
      "episodeId": "18-parallel-archive-logistics-antioch",
      "order": 18,
      "selectedSourceUrl": "https://academic.oup.com/book/3544",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Matthew+1&version=NRSVUE",
      "passage": "Matthew 1 and Luke 1 as distinct narrative openings; Oxford resource supplied only as abstract/metadata, not evidence for audience reconstruction.",
      "supportedClaim": {
        "en": "Matthew and Luke preserve distinct narrative presentations of Jesus; their texts can be compared for differing genealogies and infancy narratives.",
        "es-ES": "Mateo y Lucas conservan presentaciones narrativas distintas de Jesús; sus textos permiten comparar genealogías y relatos de infancia diferentes."
      },
      "limitations": "The claim that they were tailored for distinct communities is scholarly inference; neither texts nor Oxford abstract consulted here proves specific communities or provenance in Antioch.",
      "consultationDate": "2026-10-12",
      "status": "disputed",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Matthew+1&version=NRSVUE",
      "passage": "Matthew1; architect read genealogy and birth narrative",
      "limitations": "Different textual genealogy; not proof of a specific Antioch audience or authorial location.",
      "consultationDate": "2026-10-13",
      "status": "architect consulted; independent approval pending"
    },
    {
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Luke+3:23-38&version=NRSVUE",
      "passage": "Luke3:23–38; architect read displayed genealogy and footnotes",
      "limitations": "Genealogy differs fromMatthew1; no harmonization, audience/place inference or use of modern translation as physical ancient object.",
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

EN: Collect both northern and both southern working notes; deliver the northern pair to the north yard and the southern pair to the south yard.

ES: Recoge las dos notas de la cadena norte y las dos de la sur; entrega cada pareja en su patio correspondiente.

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
        "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-1",
        "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-1",
        "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-1",
        "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-2"
      ],
      "destinations": {
        "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-1": "faith-origins.18-parallel-archive-logistics-antioch.destination-2",
        "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-2": "faith-origins.18-parallel-archive-logistics-antioch.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-1",
        "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-2"
      ],
      "destinations": {
        "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-1": "faith-origins.18-parallel-archive-logistics-antioch.destination-3",
        "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-2": "faith-origins.18-parallel-archive-logistics-antioch.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Two distinct note pairs reached their assigned independent copy yards.

ES: Dos parejas distintas de notas han llegado a sus patios independientes asignados.

EN: The sum cannot tell me whether each voice reached the right table.

ES: La suma no me dice si cada voz llegó a la mesa correcta.

### o2 / phase-2

EN: Pay 40 wood at each copy yard, then derive one register from each yard’s own two notes.

ES: Paga 40 de madera en cada patio de copias y después elabora un registro con las dos notas propias de cada cadena.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 80
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.18-parallel-archive-logistics-antioch.destination-2",
        "faith-origins.18-parallel-archive-logistics-antioch.destination-3"
      ],
      "allocations": {
        "faith-origins.18-parallel-archive-logistics-antioch.destination-2": {
          "wood": 40
        },
        "faith-origins.18-parallel-archive-logistics-antioch.destination-3": {
          "wood": 40
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.18-parallel-archive-logistics-antioch.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-1",
        "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-2"
      ],
      "outputEntities": [
        "faith-origins.18-parallel-archive-logistics-antioch.north-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.18-parallel-archive-logistics-antioch.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 80
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
        "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-1",
        "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-2"
      ],
      "outputEntities": [
        "faith-origins.18-parallel-archive-logistics-antioch.south-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.18-parallel-archive-logistics-antioch.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 80
          },
          "newDebit": false
        }
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Two paid receiving shares and two independent derived registers are recorded.

ES: Se registran dos partes receptoras pagadas y dos registros derivados independientes.

EN: Do not borrow a page from the other pile just to make the count convenient.

ES: No tomes una página de la otra pila para facilitar el recuento.

### o3 / phase-3

EN: Bring both independent registers to the eastern archive; retain their separate labels.

ES: Lleva ambos registros independientes al archivo oriental conservando sus etiquetas separadas.

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
        "faith-origins.18-parallel-archive-logistics-antioch.north-register-1"
      ],
      "destinations": {
        "faith-origins.18-parallel-archive-logistics-antioch.north-register-1": "faith-origins.18-parallel-archive-logistics-antioch.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.18-parallel-archive-logistics-antioch.south-register-1"
      ],
      "destinations": {
        "faith-origins.18-parallel-archive-logistics-antioch.south-register-1": "faith-origins.18-parallel-archive-logistics-antioch.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both original derived register identities arrived without being merged.

ES: Ambas identidades originales de registros derivados han llegado sin fusionarse.

EN: A tidy shelf need not mean a single story.

ES: Una estantería ordenada no implica un solo relato.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/18-parallel-archive-logistics-antioch.svg)

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
        229.4,
        197.31
      ],
      "lonLat": [
        36.182,
        36.211
      ],
      "name": {
        "en": "Shared local collection court",
        "es-ES": "Patio local común de recogida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        183.2,
        87.98
      ],
      "lonLat": [
        36.171,
        36.232
      ],
      "name": {
        "en": "Northern independent copy yard",
        "es-ES": "Patio independiente de copias norte"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        263.01,
        306.64
      ],
      "lonLat": [
        36.19,
        36.19
      ],
      "name": {
        "en": "Southern independent copy yard",
        "es-ES": "Patio independiente de copias sur"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        296.61,
        160.87
      ],
      "lonLat": [
        36.198,
        36.218
      ],
      "name": {
        "en": "Eastern two-label archive",
        "es-ES": "Archivo oriental de dos etiquetas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-chain",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "south-chain",
      "hubOrder": [
        "hub-1",
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "relief",
      "hubOrder": [
        "hub-2",
        "hub-1",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "survey alternative land branch; no invented river crossing"
    }
  ],
  "terrainInstructions": "Local Antioch districts east of the schematic Orontes city reach, below or north of Silpius slopes as appropriate. No invented crossing, modern Antakya street grid, fourth-century basilica or later fortress. Exact terrain elevation, ancient banks and footprint checks pending. All local activities are fictional; long-distance journeys remain off-map.",
  "mainRouteLengthStraightTiles": 501.05,
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
  "asset": "docs/design/maps/faith-origins/odyssey/18-parallel-archive-logistics-antioch.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-1",
      "role": "fictional-independent-north-note",
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
      "id": "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-2",
      "role": "fictional-independent-north-note",
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
      "id": "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-1",
      "role": "fictional-independent-south-note",
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
      "id": "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-2",
      "role": "fictional-independent-south-note",
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
      "id": "faith-origins.18-parallel-archive-logistics-antioch.north-register-1",
      "role": "fictional-north-copy-register",
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
      "id": "faith-origins.18-parallel-archive-logistics-antioch.south-register-1",
      "role": "fictional-south-copy-register",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.18-parallel-archive-logistics-antioch.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.18-parallel-archive-logistics-antioch.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.18-parallel-archive-logistics-antioch.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.18-parallel-archive-logistics-antioch.destination-4",
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
    "north-working-notes": [
      "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-1",
      "faith-origins.18-parallel-archive-logistics-antioch.north-working-notes-2"
    ],
    "south-working-notes": [
      "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-1",
      "faith-origins.18-parallel-archive-logistics-antioch.south-working-notes-2"
    ],
    "north-register": [
      "faith-origins.18-parallel-archive-logistics-antioch.north-register-1"
    ],
    "south-register": [
      "faith-origins.18-parallel-archive-logistics-antioch.south-register-1"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Two independent annotations / Dos anotaciones independientes

EN: Recover both separate copies from two independent annotations and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de dos anotaciones independientes y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Optional notes explain attribution rather than reconcile the source genealogies.

ES: Las notas opcionales explican atribución sin reconciliar las genealogías.

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
          "18-parallel-archive-logistics-antioch.side-1.entity-1",
          "18-parallel-archive-logistics-antioch.side-1.entity-2"
        ],
        "destinations": {
          "18-parallel-archive-logistics-antioch.side-1.entity-1": "18-parallel-archive-logistics-antioch.side-1.zone-1",
          "18-parallel-archive-logistics-antioch.side-1.entity-2": "18-parallel-archive-logistics-antioch.side-1.zone-1"
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
        "id": "18-parallel-archive-logistics-antioch.side-1.entity-1",
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
        "id": "18-parallel-archive-logistics-antioch.side-1.entity-2",
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
        "id": "18-parallel-archive-logistics-antioch.side-1.zone-1",
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
      "onceFlag": "18-parallel-archive-logistics-antioch.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.18-parallel-archive-logistics-antioch"
      ],
      "historicalNote": {
        "en": "Matthew and Luke preserve different genealogies: Matthew traces through Solomon, while Luke names Nathan. Their writing places and the precise dates proposed here remain debated. The two local archive chains in Antioch are fictional and cannot resolve those questions.",
        "es-ES": "Mateo y Lucas conservan genealogías diferentes: Mateo sigue a Salomón, mientras Lucas nombra a Natán. Sus lugares de escritura y las fechas precisas aquí propuestas siguen discutidos. Las dos cadenas locales de archivo en Antioquía son ficticias y no resuelven esas cuestiones."
      },
      "hint": {
        "en": "Collect both northern and both southern working notes; deliver the northern pair to the north yard and the southern pair to the south yard.",
        "es-ES": "Recoge las dos notas de la cadena norte y las dos de la sur; entrega cada pareja en su patio correspondiente."
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

### Copy-yard approaches / Accesos a los patios de copias

EN: Scout both marked viewpoints of copy-yard approaches. Benefit: reveal the second reserve approach.

ES: Explora los dos miradores señalados de accesos a los patios de copias. Ventaja: revela la aproximación de la segunda reserva.

EN: Survey the north and south circuits; no choice removes a required archive chain.

ES: Reconoce los circuitos norte y sur; ninguna elección elimina una cadena principal.

```json
{
  "id": "side-2",
  "kind": "scout",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "visit-zones",
        "zones": [
          "18-parallel-archive-logistics-antioch.side-2.zone-1",
          "18-parallel-archive-logistics-antioch.side-2.zone-2"
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
        "id": "18-parallel-archive-logistics-antioch.side-2.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "18-parallel-archive-logistics-antioch.side-2.zone-2",
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
      "onceFlag": "18-parallel-archive-logistics-antioch.side-2.rewarded",
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

### Separate writing stock / Existencias separadas de escritura

EN: Escort the trader of separate writing stock to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de existencias separadas de escritura hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A bounded exchange supports simultaneous teams.

ES: Un intercambio limitado apoya equipos simultáneos.

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
          "18-parallel-archive-logistics-antioch.side-3.entity-1"
        ],
        "destinations": {
          "18-parallel-archive-logistics-antioch.side-3.entity-1": "18-parallel-archive-logistics-antioch.side-3.zone-1"
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
        "receipt": "18-parallel-archive-logistics-antioch.side-3.payment",
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
        "id": "18-parallel-archive-logistics-antioch.side-3.entity-1",
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
        "id": "18-parallel-archive-logistics-antioch.side-3.zone-1",
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
      "onceFlag": "18-parallel-archive-logistics-antioch.side-3.rewarded",
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

### Independent storage shelter / Cobertizo independiente de custodia

EN: Pay 50 wood and restore the damaged store of independent storage shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de cobertizo independiente de custodia. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: The repair releases finite stock without merging registers.

ES: La reparación libera existencias finitas sin fusionar registros.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "18-parallel-archive-logistics-antioch.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "18-parallel-archive-logistics-antioch.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "18-parallel-archive-logistics-antioch.side-4.payment",
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
        "id": "18-parallel-archive-logistics-antioch.side-4.entity-1",
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
        "id": "18-parallel-archive-logistics-antioch.side-4.zone-1",
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
      "onceFlag": "18-parallel-archive-logistics-antioch.side-4.rewarded",
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

### East-archive guide / Guía del archivo oriental

EN: Escort the local guide of east-archive guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía del archivo oriental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: Marks a land route for both finished registers.

ES: Señala una ruta terrestre para ambos registros terminados.

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
          "18-parallel-archive-logistics-antioch.side-5.entity-1"
        ],
        "destinations": {
          "18-parallel-archive-logistics-antioch.side-5.entity-1": "18-parallel-archive-logistics-antioch.side-5.zone-1"
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
        "id": "18-parallel-archive-logistics-antioch.side-5.entity-1",
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
        "id": "18-parallel-archive-logistics-antioch.side-5.zone-1",
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
      "onceFlag": "18-parallel-archive-logistics-antioch.side-5.rewarded",
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

### Copy-workers households / Hogares de trabajadores de copias

EN: Bring each of the two aid crates to its assigned household at copy-workers households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de trabajadores de copias. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Optional support is independent of the two main note sets.

ES: El auxilio opcional es independiente de los dos juegos principales de notas.

```json
{
  "id": "side-6",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "18-parallel-archive-logistics-antioch.side-6.entity-1",
          "18-parallel-archive-logistics-antioch.side-6.entity-2"
        ],
        "destinations": {
          "18-parallel-archive-logistics-antioch.side-6.entity-1": "18-parallel-archive-logistics-antioch.side-6.zone-1",
          "18-parallel-archive-logistics-antioch.side-6.entity-2": "18-parallel-archive-logistics-antioch.side-6.zone-2"
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
        "id": "18-parallel-archive-logistics-antioch.side-6.entity-1",
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
        "id": "18-parallel-archive-logistics-antioch.side-6.entity-2",
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
        "id": "18-parallel-archive-logistics-antioch.side-6.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "18-parallel-archive-logistics-antioch.side-6.zone-2",
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
      "onceFlag": "18-parallel-archive-logistics-antioch.side-6.rewarded",
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
      "id": "parallel-preservation",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Run two courier teams with bounded supply investment; the 80 wood main debit remains reserved.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "context-and-survey",
      "optionalObjectives": [
        "side-1",
        "side-2"
      ],
      "costOfOpportunity": "Read attributed differences and survey branches before committing both chains.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "community-and-guide",
      "optionalObjectives": [
        "side-5",
        "side-6"
      ],
      "costOfOpportunity": "Support households and onward guidance while independent copies are prepared.",
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
      "gold": 204,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
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
      "wood": 760,
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
      "wood": 810,
      "gold": 215,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
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
      "wood": 760,
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
      "wood": 833,
      "gold": 227,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
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
      "wood": 760,
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
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.title / always | none | Two Voices, Unfinished Margins | Dos voces, márgenes sin terminar |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.fact-intro / intro first | collection-narrator | Matthew and Luke preserve different genealogies: Matthew traces through Solomon, while Luke names Nathan. Their writing places and the precise dates proposed here remain debated. The two local archive chains in Antioch are fictional and cannot resolve those questions. | Mateo y Lucas conservan genealogías diferentes: Mateo sigue a Salomón, mientras Lucas nombra a Natán. Sus lugares de escritura y las fechas precisas aquí propuestas siguen discutidos. Las dos cadenas locales de archivo en Antioquía son ficticias y no resuelven esas cuestiones. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.persona-intro / after handover | miriam-archive | Once I tidied two disagreeing lists until they looked like one. I remember how pleased I was, and how much I had erased. Here I will carry two voices without smoothing their edges. | Una vez ordené dos listas discrepantes hasta que parecieron una. Recuerdo lo satisfecha que quedé y cuánto había borrado. Aquí llevaré dos voces sin alisar sus bordes. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.route-help / available from start; repeatable without effect | none | This is a local Antioch scene, not proof of where a text was composed. Keep the proposed routes on the city-side land bank; no required river crossing. | Es una escena local de Antioquía, no una prueba del lugar donde se compuso un texto. Mantén las rutas propuestas en tierra del lado urbano; no es necesario cruzar el río. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.o1-goal / phase-1 active | none | Collect both northern and both southern working notes; deliver the northern pair to the north yard and the southern pair to the south yard. | Recoge las dos notas de la cadena norte y las dos de la sur; entrega cada pareja en su patio correspondiente. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.o1-receipt / o1 latched once | none | Two distinct note pairs reached their assigned independent copy yards. | Dos parejas distintas de notas han llegado a sus patios independientes asignados. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.o1-reaction / after o1 receipt | miriam-archive | The sum cannot tell me whether each voice reached the right table. | La suma no me dice si cada voz llegó a la mesa correcta. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.o2-goal / phase-2 active | none | Pay 40 wood at each copy yard, then derive one register from each yard’s own two notes. | Paga 40 de madera en cada patio de copias y después elabora un registro con las dos notas propias de cada cadena. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.o2-receipt / o2 latched once | none | Two paid receiving shares and two independent derived registers are recorded. | Se registran dos partes receptoras pagadas y dos registros derivados independientes. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.o2-reaction / after o2 receipt | miriam-archive | Do not borrow a page from the other pile just to make the count convenient. | No tomes una página de la otra pila para facilitar el recuento. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.o3-goal / phase-3 active | none | Bring both independent registers to the eastern archive; retain their separate labels. | Lleva ambos registros independientes al archivo oriental conservando sus etiquetas separadas. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.o3-receipt / o3 latched once | none | Both original derived register identities arrived without being merged. | Ambas identidades originales de registros derivados han llegado sin fusionarse. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.o3-reaction / after o3 receipt | miriam-archive | A tidy shelf need not mean a single story. | Una estantería ordenada no implica un solo relato. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from two independent annotations and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de dos anotaciones independientes y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-1-complete / side-1 completed | none | Two independent annotations completed. Its stated benefit has been granted once. | Dos anotaciones independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-1-lost / side-1 failed-optional | none | Two independent annotations is unavailable after the loss of its unique participant or object. The main mission continues. | Dos anotaciones independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-2-goal / optional list from start | none | Scout both marked viewpoints of copy-yard approaches. Benefit: reveal the second reserve approach. | Explora los dos miradores señalados de accesos a los patios de copias. Ventaja: revela la aproximación de la segunda reserva. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-2-complete / side-2 completed | none | Copy-yard approaches completed. Its stated benefit has been granted once. | Accesos a los patios de copias: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-2-lost / side-2 failed-optional | none | Copy-yard approaches is unavailable after the loss of its unique participant or object. The main mission continues. | Accesos a los patios de copias: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-3-goal / optional list from start | none | Escort the trader of separate writing stock to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de existencias separadas de escritura hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-3-complete / side-3 completed | none | Separate writing stock completed. Its stated benefit has been granted once. | Existencias separadas de escritura: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-3-lost / side-3 failed-optional | none | Separate writing stock is unavailable after the loss of its unique participant or object. The main mission continues. | Existencias separadas de escritura: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of independent storage shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de cobertizo independiente de custodia. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-4-complete / side-4 completed | none | Independent storage shelter completed. Its stated benefit has been granted once. | Cobertizo independiente de custodia: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-4-lost / side-4 failed-optional | none | Independent storage shelter is unavailable after the loss of its unique participant or object. The main mission continues. | Cobertizo independiente de custodia: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-5-goal / optional list from start | none | Escort the local guide of east-archive guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía del archivo oriental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-5-complete / side-5 completed | none | East-archive guide completed. Its stated benefit has been granted once. | Guía del archivo oriental: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-5-lost / side-5 failed-optional | none | East-archive guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del archivo oriental: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-6-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at copy-workers households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de trabajadores de copias. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-6-complete / side-6 completed | none | Copy-workers households completed. Its stated benefit has been granted once. | Hogares de trabajadores de copias: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.side-6-lost / side-6 failed-optional | none | Copy-workers households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares de trabajadores de copias: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.fact-outro / victory first | collection-narrator | Two fictional local note collections remain distinct after delivery. They illustrate preserving different accounts; neither collection is a canonical autograph or evidence for a particular ancient audience in Antioch. | Dos colecciones locales ficticias de notas permanecen distintas tras su entrega. Ilustran la conservación de relatos diferentes; ninguna es un autógrafo canónico ni prueba de un público antiguo concreto en Antioquía. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.persona-outro / after fact-outro | miriam-archive | The shelves hold both labels. I do not have to make one silence the other to keep the archive in order. | Las estanterías conservan ambas etiquetas. No necesito silenciar una para mantener ordenado el archivo. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.18-parallel-archive-logistics-antioch.odyssey.next-episode / after persona-outro | none | Continue with The House Before the Road. This episode does not complete the campaign. | Continúa con La casa antes del camino. Este episodio no termina la campaña. |

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
      "two northern notes cannot satisfy southern pair",
      "one register cannot count as both voices",
      "40 wood north and40south must remain exact",
      "both distinct derived IDs must arrive",
      "no canonical autograph or settled Antioch provenance",
      "fourth receiving district cannot be replaced with third",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
