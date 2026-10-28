# 2. Promises in the Winter Court

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `02-bounded-negotiation-milan` · 313 CE · 400×400

## Historical frame and fixed outcome

EN: Lactantius reports a meeting of Constantine and Licinius at Milan in 313. The letter he transmits later refers to their agreement on religious choice and restoration of Christian communal property. It is not a transcript of their conversation. Our local dispatch work is fictional; the later publication at Nicomedia is a separate episode. Christianity is not made the state religion by this letter.

ES: Lactancio relata una reunión de Constantino y Licinio en Milán en 313. La carta que transmite después se refiere a su acuerdo sobre elección religiosa y restitución de bienes comunitarios cristianos. No transcribe su conversación. Nuestro trabajo local de despachos es ficticio; la publicación posterior en Nicomedia es un episodio separado. Esta carta no convierte el cristianismo en religión estatal.

EN: A fictional local working register reached a northern receiving court, and its courier returned after an observed departure. This circuit records no private negotiation, original imperial instrument or historical delivery. The agreement reported by Lactantius leads into the distinct account of publication at Nicomedia.

ES: Un registro ficticio local de trabajo llegó a un patio receptor norteño y su correo regresó tras una salida observada. Este circuito no acredita negociación privada, documento imperial original ni entrega histórica. El acuerdo relatado por Lactancio da paso al relato distinto de la publicación en Nicomedia.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "Lactantius 48 transmits a letter referring to the Milan agreement on religious choice and Christian communal-property restitution; its preface reports publication at Nicomedia on 13 June 313.",
        "es-ES": "Lactancio 48 transmite una carta que alude al acuerdo de Milán sobre elección religiosa y restitución de bienes comunitarios cristianos; su preámbulo relata publicación en Nicomedia el13de junio de313."
      },
      "architectCorrection": {
        "reason": "Use directly read Latin DMP48 to attribute meeting and publication; do not treat collector’s conflation with Eusebius/Fordham as exact source lineage. Nicomedia uses the existing Bithynia regional profile.",
        "date": "2026-10-13"
      }
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/200110.htm",
      "passage": "Eusebius HE X.5 / Fordham translation of rescript; checked editorial note describing Milan meeting.",
      "limitations": "The “negotiation” phrasing is an inference; surviving text is later rescript, not minutes of a conversation. Lactantius page URL in dossier was not opened.",
      "status": "consulted",
      "supportedClaim": "Supports a policy agreement attributed to the rulers at Milan, followed by a rescript granting religious freedom. / Apoya un acuerdo político atribuido a los gobernantes en Milán, seguido de un rescripto de libertad religiosa.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "Fordham note and translated rescript; Eusebius HE X.5 checked.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://bkv.unifr.ch/en/works/cpl-91/compare/von-den-todesarten-der-verfolger-bkv/49/de-mortibus-persecutorum",
      "passage": "DMP48.1–13 complete Latin text, root read2026-10-13",
      "limitations": "Milan agreement versus Nicomedia publication; transmitted legal text, no minutes of a negotiation or proven local property delivery.",
      "consultationDate": "2026-10-13",
      "status": "architect read; independent historical approval pending"
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

EN: Collect three northern and three eastern ordinary requests and deliver all six to the western preparation yard.

ES: Recoge tres solicitudes ordinarias norteñas y tres orientales y entrega las seis en el patio occidental.

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
        "imperial-church.02-bounded-negotiation-milan.north-requests-1",
        "imperial-church.02-bounded-negotiation-milan.north-requests-2",
        "imperial-church.02-bounded-negotiation-milan.north-requests-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.02-bounded-negotiation-milan.north-requests-1",
        "imperial-church.02-bounded-negotiation-milan.north-requests-2",
        "imperial-church.02-bounded-negotiation-milan.north-requests-3"
      ],
      "destinations": {
        "imperial-church.02-bounded-negotiation-milan.north-requests-1": "imperial-church.02-bounded-negotiation-milan.destination-2",
        "imperial-church.02-bounded-negotiation-milan.north-requests-2": "imperial-church.02-bounded-negotiation-milan.destination-2",
        "imperial-church.02-bounded-negotiation-milan.north-requests-3": "imperial-church.02-bounded-negotiation-milan.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.02-bounded-negotiation-milan.east-requests-1",
        "imperial-church.02-bounded-negotiation-milan.east-requests-2",
        "imperial-church.02-bounded-negotiation-milan.east-requests-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "imperial-church.02-bounded-negotiation-milan.east-requests-1",
        "imperial-church.02-bounded-negotiation-milan.east-requests-2",
        "imperial-church.02-bounded-negotiation-milan.east-requests-3"
      ],
      "destinations": {
        "imperial-church.02-bounded-negotiation-milan.east-requests-1": "imperial-church.02-bounded-negotiation-milan.destination-2",
        "imperial-church.02-bounded-negotiation-milan.east-requests-2": "imperial-church.02-bounded-negotiation-milan.destination-2",
        "imperial-church.02-bounded-negotiation-milan.east-requests-3": "imperial-church.02-bounded-negotiation-milan.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Six distinct local request identities reached preparation.

ES: Seis identidades distintas de solicitudes locales llegaron a preparación.

EN: Ordinary paperwork has ordinary authors; none of these notes is an emperor speaking.

ES: Los papeles ordinarios tienen autores ordinarios; ninguna de estas notas es un emperador que habla.

### o2 / phase-2

EN: Pay 80 wood and 30 gold once and prepare one labelled working register from the six collected requests.

ES: Paga una vez 80 de madera y 30 de oro y prepara un registro etiquetado a partir de las seis solicitudes recogidas.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 80,
        "gold": 30
      },
      "id": "req-1",
      "receivingZones": [
        "imperial-church.02-bounded-negotiation-milan.destination-2"
      ],
      "allocations": {
        "imperial-church.02-bounded-negotiation-milan.destination-2": {
          "wood": 80,
          "gold": 30
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.02-bounded-negotiation-milan.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "imperial-church.02-bounded-negotiation-milan.north-requests-1",
        "imperial-church.02-bounded-negotiation-milan.north-requests-2",
        "imperial-church.02-bounded-negotiation-milan.north-requests-3",
        "imperial-church.02-bounded-negotiation-milan.east-requests-1",
        "imperial-church.02-bounded-negotiation-milan.east-requests-2",
        "imperial-church.02-bounded-negotiation-milan.east-requests-3"
      ],
      "outputEntities": [
        "imperial-church.02-bounded-negotiation-milan.working-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.02-bounded-negotiation-milan.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 80,
            "gold": 30
          },
          "newDebit": false
        }
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The working register has one exact active payment receipt.

ES: El registro de trabajo tiene un recibo exacto de pago activo.

EN: One label is sufficient for our fiction; it is not a seal of imperial authenticity.

ES: Una etiqueta basta para nuestra ficción; no es un sello de autenticidad imperial.

### o3 / phase-3

EN: Deliver the one working register and its original assigned courier to the northern local court.

ES: Entrega el único registro de trabajo y su correo original asignado en el patio local norteño.

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
        "imperial-church.02-bounded-negotiation-milan.working-register-1"
      ],
      "destinations": {
        "imperial-church.02-bounded-negotiation-milan.working-register-1": "imperial-church.02-bounded-negotiation-milan.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.02-bounded-negotiation-milan.local-courier-1"
      ],
      "destinations": {
        "imperial-church.02-bounded-negotiation-milan.local-courier-1": "imperial-church.02-bounded-negotiation-milan.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The original courier and the labelled local register reached northern reception.

ES: El correo original y el registro local etiquetado llegaron a recepción norteña.

EN: We have reached a fictional work court, not the inside of an imperial agreement.

ES: Hemos llegado a un patio ficticio de trabajo, no al interior de un acuerdo imperial.

### o4 / phase-4

EN: After northern reception, depart the same courier and bring him back to the western preparation yard.

ES: Tras la recepción norteña, da salida al mismo correo y hazlo regresar al patio occidental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "ordered-departure",
      "receiptObjective": "o3",
      "receiptRequirement": "req-2",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-1",
      "departingEntities": [
        "imperial-church.02-bounded-negotiation-milan.local-courier-1"
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
        "imperial-church.02-bounded-negotiation-milan.local-courier-1"
      ],
      "destinations": {
        "imperial-church.02-bounded-negotiation-milan.local-courier-1": "imperial-church.02-bounded-negotiation-milan.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The return arrived only after its own receipt-backed departure.

ES: El regreso llegó solo después de su propia salida respaldada por recibo.

EN: The courier’s first visit is not his return. Even a heading must respect that much time.

ES: La primera visita del correo no es su regreso. Hasta un encabezamiento debe respetar ese poco de tiempo.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/02-bounded-negotiation-milan.svg)

```json
{
  "bbox": [
    9.15,
    45.445,
    9.22,
    45.49
  ],
  "terrainProfile": "milan",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        174.05,
        232.16
      ],
      "lonLat": [
        9.18,
        45.463
      ],
      "name": {
        "en": "Fictional ordinary receiving court",
        "es-ES": "Patio receptor ordinario ficticio"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        77.36,
        239.41
      ],
      "lonLat": [
        9.161,
        45.462
      ],
      "name": {
        "en": "Western dispatch preparation yard",
        "es-ES": "Patio occidental de preparación de despachos"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        174.05,
        94.28
      ],
      "lonLat": [
        9.18,
        45.482
      ],
      "name": {
        "en": "Northern local request court",
        "es-ES": "Patio local norteño de solicitudes"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        311.46,
        261.18
      ],
      "lonLat": [
        9.207,
        45.459
      ],
      "name": {
        "en": "Eastern local request court",
        "es-ES": "Patio local oriental de solicitudes"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-dispatch",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-requests",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "outer-yard",
      "hubOrder": [
        "hub-3",
        "hub-4",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 6
    }
  ],
  "terrainInstructions": "Local inland Mediolanum in the Po plain, same regional crop as the preceding campaign’s final local archive but a distinct fictional work scene. Four invented request/dispatch courts, not actual palace rooms or an emperor’s meeting place. No Gothic Duomo, medieval Navigli or modern railways; minor ancient watercourses, gates, wall phases and exact Roman streets need dated footprints. The community map combines centuries III–V and cannot date every basilica to 313. No Po crossing or naval travel is mandatory. All logistics are local; Milan-to-Nicomedia publication remains off this map.",
  "corridorStraightLengthsTiles": {
    "north-dispatch": 271.35,
    "east-requests": 332.07,
    "outer-yard": 356.63
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
    "coordinates": [],
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
  "asset": "docs/design/maps/imperial-church/odyssey/02-bounded-negotiation-milan.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.02-bounded-negotiation-milan.north-requests-1",
      "role": "fictional-local-work-request",
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
      "id": "imperial-church.02-bounded-negotiation-milan.north-requests-2",
      "role": "fictional-local-work-request",
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
      "id": "imperial-church.02-bounded-negotiation-milan.north-requests-3",
      "role": "fictional-local-work-request",
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
      "id": "imperial-church.02-bounded-negotiation-milan.east-requests-1",
      "role": "fictional-local-work-request",
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
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "imperial-church.02-bounded-negotiation-milan.east-requests-2",
      "role": "fictional-local-work-request",
      "initialHub": "hub-4",
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
      "id": "imperial-church.02-bounded-negotiation-milan.east-requests-3",
      "role": "fictional-local-work-request",
      "initialHub": "hub-4",
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
      "id": "imperial-church.02-bounded-negotiation-milan.working-register-1",
      "role": "fictional-labelled-local-register",
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
      "id": "imperial-church.02-bounded-negotiation-milan.local-courier-1",
      "role": "fictional-dispatch-courier",
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
    }
  ],
  "zones": [
    {
      "id": "imperial-church.02-bounded-negotiation-milan.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.02-bounded-negotiation-milan.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.02-bounded-negotiation-milan.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.02-bounded-negotiation-milan.destination-4",
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
    "north-requests": [
      "imperial-church.02-bounded-negotiation-milan.north-requests-1",
      "imperial-church.02-bounded-negotiation-milan.north-requests-2",
      "imperial-church.02-bounded-negotiation-milan.north-requests-3"
    ],
    "east-requests": [
      "imperial-church.02-bounded-negotiation-milan.east-requests-1",
      "imperial-church.02-bounded-negotiation-milan.east-requests-2",
      "imperial-church.02-bounded-negotiation-milan.east-requests-3"
    ],
    "working-register": [
      "imperial-church.02-bounded-negotiation-milan.working-register-1"
    ],
    "local-courier": [
      "imperial-church.02-bounded-negotiation-milan.local-courier-1"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.02-bounded-negotiation-milan.local-courier-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Meeting and letter on separate labels / Reunión y carta en etiquetas separadas

EN: Recover both separate copies from meeting and letter on separate labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de reunión y carta en etiquetas separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Qualified local context distinguishes Lactantius’ meeting report from the later transmitted letter.

ES: El contexto local distingue el relato de la reunión de Lactancio de la carta transmitida después.

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
          "02-bounded-negotiation-milan.side-1.entity-1",
          "02-bounded-negotiation-milan.side-1.entity-2"
        ],
        "destinations": {
          "02-bounded-negotiation-milan.side-1.entity-1": "02-bounded-negotiation-milan.side-1.zone-1",
          "02-bounded-negotiation-milan.side-1.entity-2": "02-bounded-negotiation-milan.side-1.zone-1"
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
        "id": "02-bounded-negotiation-milan.side-1.entity-1",
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
        "id": "02-bounded-negotiation-milan.side-1.entity-2",
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
        "id": "02-bounded-negotiation-milan.side-1.zone-1",
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
      "onceFlag": "02-bounded-negotiation-milan.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.02-bounded-negotiation-milan"
      ],
      "historicalNote": {
        "en": "Lactantius reports a meeting of Constantine and Licinius at Milan in 313. The letter he transmits later refers to their agreement on religious choice and restoration of Christian communal property. It is not a transcript of their conversation. Our local dispatch work is fictional; the later publication at Nicomedia is a separate episode. Christianity is not made the state religion by this letter.",
        "es-ES": "Lactancio relata una reunión de Constantino y Licinio en Milán en 313. La carta que transmite después se refiere a su acuerdo sobre elección religiosa y restitución de bienes comunitarios cristianos. No transcribe su conversación. Nuestro trabajo local de despachos es ficticio; la publicación posterior en Nicomedia es un episodio separado. Esta carta no convierte el cristianismo en religión estatal."
      },
      "hint": {
        "en": "Collect three northern and three eastern ordinary requests and deliver all six to the western preparation yard.",
        "es-ES": "Recoge tres solicitudes ordinarias norteñas y tres orientales y entrega las seis en el patio occidental."
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
      "north-dispatch",
      "east-requests",
      "outer-yard"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The ordinary yard households / Los hogares ordinarios del patio

EN: Bring each of the two aid crates to its assigned household at the ordinary yard households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares ordinarios del patio. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Independent household aid has no emperor’s favor, conversion or religious-test requirement.

ES: La ayuda a hogares independientes no exige favor imperial, conversión ni examen religioso.

```json
{
  "id": "side-2",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "02-bounded-negotiation-milan.side-2.entity-1",
          "02-bounded-negotiation-milan.side-2.entity-2"
        ],
        "destinations": {
          "02-bounded-negotiation-milan.side-2.entity-1": "02-bounded-negotiation-milan.side-2.zone-1",
          "02-bounded-negotiation-milan.side-2.entity-2": "02-bounded-negotiation-milan.side-2.zone-2"
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
        "id": "02-bounded-negotiation-milan.side-2.entity-1",
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
        "id": "02-bounded-negotiation-milan.side-2.entity-2",
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
        "id": "02-bounded-negotiation-milan.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "02-bounded-negotiation-milan.side-2.zone-2",
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
      "onceFlag": "02-bounded-negotiation-milan.side-2.rewarded",
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
      "north-dispatch",
      "east-requests",
      "outer-yard"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The dispatch roof / El tejado de despachos

EN: Pay 50 wood and restore the damaged store of the dispatch roof to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el tejado de despachos. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A finite ordinary shelter repair cannot restore a historically documented Christian property.

ES: Reparar un cobertizo ordinario finito no restituye una propiedad cristiana históricamente documentada.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "02-bounded-negotiation-milan.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "02-bounded-negotiation-milan.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "02-bounded-negotiation-milan.side-3.payment",
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
        "id": "02-bounded-negotiation-milan.side-3.entity-1",
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
        "id": "02-bounded-negotiation-milan.side-3.zone-1",
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
      "onceFlag": "02-bounded-negotiation-milan.side-3.rewarded",
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
      "north-dispatch",
      "east-requests",
      "outer-yard"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### An independent consignment / Una remesa independiente

EN: Escort the trader of an independent consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de una remesa independiente hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Bounded trade supports a local detour, never an imperial audience or historic diplomatic success.

ES: El comercio limitado apoya un desvío local, nunca una audiencia imperial ni un éxito diplomático histórico.

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
          "02-bounded-negotiation-milan.side-4.entity-1"
        ],
        "destinations": {
          "02-bounded-negotiation-milan.side-4.entity-1": "02-bounded-negotiation-milan.side-4.zone-1"
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
        "receipt": "02-bounded-negotiation-milan.side-4.payment",
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
        "id": "02-bounded-negotiation-milan.side-4.entity-1",
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
        "id": "02-bounded-negotiation-milan.side-4.zone-1",
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
      "onceFlag": "02-bounded-negotiation-milan.side-4.rewarded",
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
      "north-dispatch",
      "east-requests",
      "outer-yard"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The northern return road / El camino de regreso norteño

EN: Scout both marked viewpoints of the northern return road. Benefit: Mark the surveyed north-dispatch local land circuit once; every main receiver is disclosed without this task.

ES: Explora los dos miradores señalados de el camino de regreso norteño. Ventaja: Señala una vez el circuito terrestre local reconocido north-dispatch; todos los receptores principales se indican sin esta tarea.

EN: Survey the real proposed northern courier circuit; no secret palace access.

ES: Reconoce el circuito norteño propuesto del correo; no revela acceso secreto al palacio.

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
          "02-bounded-negotiation-milan.side-5.zone-1",
          "02-bounded-negotiation-milan.side-5.zone-2"
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
        "id": "02-bounded-negotiation-milan.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "02-bounded-negotiation-milan.side-5.zone-2",
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
      "target": "north-dispatch local disclosed circuit",
      "resources": {},
      "onceFlag": "02-bounded-negotiation-milan.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "north-dispatch"
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
      "north-dispatch",
      "east-requests",
      "outer-yard"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A guide around the work yards / Un guía entre los patios de trabajo

EN: Escort the local guide of a guide around the work yards to the marked road junction. Benefit: Mark the surveyed outer-yard local land circuit once; every main receiver is disclosed without this task.

ES: Escolta al guía local de un guía entre los patios de trabajo hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local reconocido outer-yard; todos los receptores principales se indican sin esta tarea.

EN: Marks the outer local land route without implying a journey to Nicomedia.

ES: Señala la ruta terrestre local exterior sin simular un viaje a Nicomedia.

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
          "02-bounded-negotiation-milan.side-6.entity-1"
        ],
        "destinations": {
          "02-bounded-negotiation-milan.side-6.entity-1": "02-bounded-negotiation-milan.side-6.zone-1"
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
        "id": "02-bounded-negotiation-milan.side-6.entity-1",
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
        "id": "02-bounded-negotiation-milan.side-6.zone-1",
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
      "target": "outer-yard local disclosed circuit",
      "resources": {},
      "onceFlag": "02-bounded-negotiation-milan.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "outer-yard"
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
      "north-dispatch",
      "east-requests",
      "outer-yard"
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
      "id": "split-request-crews",
      "optionalObjectives": [
        "side-4",
        "side-5"
      ],
      "costOfOpportunity": "Split northern/eastern collection while reserving the 80 wood/30 gold mandatory payment.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "context-and-shelter",
      "optionalObjectives": [
        "side-1",
        "side-3"
      ],
      "costOfOpportunity": "Separate provenance labels and optional shelter work before preparing the local register.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "households-and-return",
      "optionalObjectives": [
        "side-2",
        "side-6"
      ],
      "costOfOpportunity": "Run independent care while the original courier completes an observed outward/return journey.",
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
      "gold": 234,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
      "gold": 30,
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
      "gold": 320,
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
      "gold": 245,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
      "gold": 30,
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
      "gold": 320,
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
      "gold": 257,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
      "gold": 30,
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
      "gold": 320,
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
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.title / always | none | Promises in the Winter Court | Promesas en la corte de invierno |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.fact-intro / intro first | collection-narrator | Lactantius reports a meeting of Constantine and Licinius at Milan in 313. The letter he transmits later refers to their agreement on religious choice and restoration of Christian communal property. It is not a transcript of their conversation. Our local dispatch work is fictional; the later publication at Nicomedia is a separate episode. Christianity is not made the state religion by this letter. | Lactancio relata una reunión de Constantino y Licinio en Milán en 313. La carta que transmite después se refiere a su acuerdo sobre elección religiosa y restitución de bienes comunitarios cristianos. No transcribe su conversación. Nuestro trabajo local de despachos es ficticio; la publicación posterior en Nicomedia es un episodio separado. Esta carta no convierte el cristianismo en religión estatal. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.persona-intro / after handover | imperial-clerk | My family papers give this meeting a remarkably tidy heading. I was not yet born, which helped the heading remain tidy. Years of clerical work have made me curious about the people and delays it leaves out. I can imagine a dispatch yard; I cannot put my ear behind the emperors’ door. | Los papeles de mi familia dan a esta reunión un encabezamiento admirablemente ordenado. Yo aún no había nacido, lo que ayudó al encabezamiento a seguir ordenado. Los años de escribiente me hicieron sentir curiosidad por las personas y demoras que omite. Puedo imaginar un patio de despachos; no poner la oreja tras la puerta de los emperadores. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.route-help / available from start; repeatable without effect | none | Collect three local northern requests and three eastern requests and bring all six to the western preparation yard. Pay 80 wood and 30 gold there once to prepare one labelled working register. Deliver that register and its assigned original courier to the northern court. Only then depart that courier and return him to the western yard. The last arrival must follow the receipt-backed departure; no imperial audience or historical autograph is involved. | Recoge tres solicitudes locales norteñas y tres orientales y lleva las seis al patio occidental de preparación. Paga allí una vez 80 de madera y 30 de oro para preparar un registro de trabajo etiquetado. Entrega el registro y su correo original asignado en el patio norte. Solo entonces da salida a ese correo y hazlo regresar al patio occidental. La última llegada debe seguir a la salida respaldada por recibo; no interviene audiencia imperial ni autógrafo histórico. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o1-goal / phase-1 active | none | Collect three northern and three eastern ordinary requests and deliver all six to the western preparation yard. | Recoge tres solicitudes ordinarias norteñas y tres orientales y entrega las seis en el patio occidental. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o1-receipt / o1 latched once | none | Six distinct local request identities reached preparation. | Seis identidades distintas de solicitudes locales llegaron a preparación. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o1-reaction / after o1 receipt | imperial-clerk | Ordinary paperwork has ordinary authors; none of these notes is an emperor speaking. | Los papeles ordinarios tienen autores ordinarios; ninguna de estas notas es un emperador que habla. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o2-goal / phase-2 active | none | Pay 80 wood and 30 gold once and prepare one labelled working register from the six collected requests. | Paga una vez 80 de madera y 30 de oro y prepara un registro etiquetado a partir de las seis solicitudes recogidas. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o2-receipt / o2 latched once | none | The working register has one exact active payment receipt. | El registro de trabajo tiene un recibo exacto de pago activo. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o2-reaction / after o2 receipt | imperial-clerk | One label is sufficient for our fiction; it is not a seal of imperial authenticity. | Una etiqueta basta para nuestra ficción; no es un sello de autenticidad imperial. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o3-goal / phase-3 active | none | Deliver the one working register and its original assigned courier to the northern local court. | Entrega el único registro de trabajo y su correo original asignado en el patio local norteño. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o3-receipt / o3 latched once | none | The original courier and the labelled local register reached northern reception. | El correo original y el registro local etiquetado llegaron a recepción norteña. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o3-reaction / after o3 receipt | imperial-clerk | We have reached a fictional work court, not the inside of an imperial agreement. | Hemos llegado a un patio ficticio de trabajo, no al interior de un acuerdo imperial. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o4-goal / phase-4 active | none | After northern reception, depart the same courier and bring him back to the western preparation yard. | Tras la recepción norteña, da salida al mismo correo y hazlo regresar al patio occidental. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o4-receipt / o4 latched once | none | The return arrived only after its own receipt-backed departure. | El regreso llegó solo después de su propia salida respaldada por recibo. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.o4-reaction / after o4 receipt | imperial-clerk | The courier’s first visit is not his return. Even a heading must respect that much time. | La primera visita del correo no es su regreso. Hasta un encabezamiento debe respetar ese poco de tiempo. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from meeting and letter on separate labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de reunión y carta en etiquetas separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-1-complete / side-1 completed | none | Meeting and letter on separate labels completed. Its stated benefit has been granted once. | Reunión y carta en etiquetas separadas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-1-lost / side-1 failed-optional | none | Meeting and letter on separate labels is unavailable after the loss of its unique participant or object. The main mission continues. | Reunión y carta en etiquetas separadas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at the ordinary yard households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares ordinarios del patio. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-2-complete / side-2 completed | none | The ordinary yard households completed. Its stated benefit has been granted once. | Los hogares ordinarios del patio: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-2-lost / side-2 failed-optional | none | The ordinary yard households is unavailable after the loss of its unique participant or object. The main mission continues. | Los hogares ordinarios del patio: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the dispatch roof to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el tejado de despachos. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-3-complete / side-3 completed | none | The dispatch roof completed. Its stated benefit has been granted once. | El tejado de despachos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-3-lost / side-3 failed-optional | none | The dispatch roof is unavailable after the loss of its unique participant or object. The main mission continues. | El tejado de despachos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-4-goal / optional list from start | none | Escort the trader of an independent consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de una remesa independiente hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-4-complete / side-4 completed | none | An independent consignment completed. Its stated benefit has been granted once. | Una remesa independiente: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-4-lost / side-4 failed-optional | none | An independent consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Una remesa independiente: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of the northern return road. Benefit: Mark the surveyed north-dispatch local land circuit once; every main receiver is disclosed without this task. | Explora los dos miradores señalados de el camino de regreso norteño. Ventaja: Señala una vez el circuito terrestre local reconocido north-dispatch; todos los receptores principales se indican sin esta tarea. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-5-complete / side-5 completed | none | The northern return road completed. Its stated benefit has been granted once. | El camino de regreso norteño: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-5-lost / side-5 failed-optional | none | The northern return road is unavailable after the loss of its unique participant or object. The main mission continues. | El camino de regreso norteño: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-6-goal / optional list from start | none | Escort the local guide of a guide around the work yards to the marked road junction. Benefit: Mark the surveyed outer-yard local land circuit once; every main receiver is disclosed without this task. | Escolta al guía local de un guía entre los patios de trabajo hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local reconocido outer-yard; todos los receptores principales se indican sin esta tarea. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-6-complete / side-6 completed | none | A guide around the work yards completed. Its stated benefit has been granted once. | Un guía entre los patios de trabajo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.side-6-lost / side-6 failed-optional | none | A guide around the work yards is unavailable after the loss of its unique participant or object. The main mission continues. | Un guía entre los patios de trabajo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.fact-outro / victory first | collection-narrator | A fictional local working register reached a northern receiving court, and its courier returned after an observed departure. This circuit records no private negotiation, original imperial instrument or historical delivery. The agreement reported by Lactantius leads into the distinct account of publication at Nicomedia. | Un registro ficticio local de trabajo llegó a un patio receptor norteño y su correo regresó tras una salida observada. Este circuito no acredita negociación privada, documento imperial original ni entrega histórica. El acuerdo relatado por Lactancio da paso al relato distinto de la publicación en Nicomedia. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.persona-outro / after fact-outro | imperial-clerk | I like a returned courier. He gives my fictional ledger an ending I can count. The heading about the emperors remains less obedient: it names an agreement, not every consequence that followed. | Me gusta un correo que regresa. Da a mi registro ficticio un final que puedo contar. El encabezamiento sobre los emperadores es menos obediente: nombra un acuerdo, no todas las consecuencias posteriores. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.02-bounded-negotiation-milan.odyssey.next-episode / after persona-outro | none | Continue with The Doors Returned. This episode does not complete the campaign. | Continúa con Las puertas restituidas. Este episodio no termina la campaña. |

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
    "style": "sober Roman provincial plain, invented local work scene",
    "historicalControls": "no actual palace room, later basilica or modern city grid as evidence for 313",
    "referenceAssets": [
      "milan-circus-remains",
      "mediolanum-multiphase-plan"
    ],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "all six original requests required",
      "register never generated before exact payment",
      "courier cannot be replaced by an optional guide",
      "initial western-yard visit cannot count as return",
      "same courier must reach northern court before departure enables",
      "no 313 first-person Marcus memory",
      "no actual emperor conversation or forced religion choice",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
