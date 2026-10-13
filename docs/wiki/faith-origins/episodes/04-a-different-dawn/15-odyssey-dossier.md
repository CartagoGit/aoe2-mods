# 30. A Different Dawn

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `04-a-different-dawn` · 303–313 CE; Milan local archive is dramatization, persecution and restitution vary regionally · 400×400

## Historical frame and fixed outcome

EN: Eusebius reports measures against churches and Christian texts from 303, with a Christian interpretation and selective coverage. Lactantius transmits a 313 letter concerning religious freedom and restoration of Christian communal property, reporting agreement at Milan and publication at Nicomedia on 13 June. These sources do not establish uniform enforcement or a particular restored Milan archive. Our local work scene is fictional.

ES: Eusebio informa de medidas contra iglesias y textos cristianos desde 303, con interpretación cristiana y cobertura selectiva. Lactancio transmite una carta de 313 sobre libertad religiosa y restitución de propiedades comunitarias cristianas; relata un acuerdo en Milán y su publicación en Nicomedia el 13 de junio. Estas fuentes no acreditan aplicación uniforme ni un archivo concreto restituido en Milán. Nuestra escena local de trabajo es ficticia.

EN: The fictional archive’s two inventory registers and six neighbor care deliveries are complete. Neither register demonstrates a historical property transfer. The reported 313 agreement and letter do not erase previous violence or establish the later outcomes of imperial Christianity or Jewish communities. Those histories continue in separate campaigns with overlapping dates and different perspectives.

ES: Se han completado los dos registros de inventario del archivo ficticio y seis entregas de cuidados a vecinos. Ningún registro demuestra una transferencia histórica de propiedad. El acuerdo y la carta relatados de 313 no borran la violencia anterior ni determinan los desenlaces posteriores del cristianismo imperial o de las comunidades judías. Esas historias continúan en campañas separadas, con fechas solapadas y perspectivas diferentes.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 23,
      "episodeId": "04-a-different-dawn",
      "order": 30,
      "selectedSourceUrl": "https://www.newadvent.org/fathers/250108.htm",
      "consultedUrl": "https://www.newadvent.org/fathers/250108.htm",
      "passage": "Eusebius, Ecclesiastical History 8.2–3 and 8.5: orders against churches/scriptures and subsequent punishments, with Eusebius' explicitly Christian narrative frame.",
      "supportedClaim": {
        "en": "Eusebius records the Great Persecution's measures against churches and Christian texts and reports punishments in several provinces.",
        "es-ES": "Eusebio registra medidas de la Gran Persecución contra iglesias y textos cristianos, e informa de castigos en varias provincias."
      },
      "limitations": "Eusebius is a Christian historian and his rhetoric interprets events providentially; implementation differed by region and date. This source does not document a specific Milan archive or single uniform local event, nor all the 303–313 range.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/250108.htm",
      "passage": "HEVIII2–3and5",
      "limitations": "Christian interpretation and selective testimony; no uniform303–313Milan persecution or particular restored archive.",
      "consultationDate": "2026-10-13",
      "status": "architect read specified passages; independent approval pending"
    },
    {
      "consultedUrl": "https://bkv.unifr.ch/en/works/cpl-91/compare/von-den-todesarten-der-verfolger-bkv/49/de-mortibus-persecutorum",
      "passage": "De mortibus persecutorum48.1–13, root read complete Latin edition",
      "limitations": "Milan agreement versus Nicomedia publication13June313; transmitted legal text not specific Milan property delivery. No wholesale modern translation reproduced.",
      "consultationDate": "2026-10-13",
      "status": "architect read specified passages; independent approval pending"
    }
  ],
  "knowledgeBasis": {
    "speaker": "miriam-archive",
    "mode": "fictional personal local experience plus sourced reports from other regions",
    "noOmniscience": true
  }
}
```

## Main objectives and individual contracts

### o1 / phase-1

EN: Collect both northern and both eastern inventory requests and deliver all four to the western work yard.

ES: Recoge ambas solicitudes de inventario norteñas y ambas orientales y entrega las cuatro en el patio occidental.

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
        "faith-origins.04-a-different-dawn.north-inventory-requests-1",
        "faith-origins.04-a-different-dawn.north-inventory-requests-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.04-a-different-dawn.north-inventory-requests-1",
        "faith-origins.04-a-different-dawn.north-inventory-requests-2"
      ],
      "destinations": {
        "faith-origins.04-a-different-dawn.north-inventory-requests-1": "faith-origins.04-a-different-dawn.destination-2",
        "faith-origins.04-a-different-dawn.north-inventory-requests-2": "faith-origins.04-a-different-dawn.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "faith-origins.04-a-different-dawn.east-inventory-requests-1",
        "faith-origins.04-a-different-dawn.east-inventory-requests-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "faith-origins.04-a-different-dawn.east-inventory-requests-1",
        "faith-origins.04-a-different-dawn.east-inventory-requests-2"
      ],
      "destinations": {
        "faith-origins.04-a-different-dawn.east-inventory-requests-1": "faith-origins.04-a-different-dawn.destination-2",
        "faith-origins.04-a-different-dawn.east-inventory-requests-2": "faith-origins.04-a-different-dawn.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Four original local inventory requests reached the work yard.

ES: Cuatro solicitudes originales de inventario local llegaron al patio de trabajo.

EN: A request can name a hope; it cannot prove that hope was granted in history.

ES: Una solicitud puede nombrar una esperanza; no prueba que la historia la concediera.

### o2 / phase-2

EN: Pay 60 wood and 20 gold for each distinct register, then prepare both from their own collected requests.

ES: Paga 60 de madera y 20 de oro por cada registro distinto y prepara ambos a partir de sus propias solicitudes recogidas.

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
        "faith-origins.04-a-different-dawn.destination-2"
      ],
      "allocations": {
        "faith-origins.04-a-different-dawn.destination-2": {
          "wood": 60,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.04-a-different-dawn.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 60,
        "gold": 20
      },
      "id": "req-2",
      "receivingZones": [
        "faith-origins.04-a-different-dawn.destination-2"
      ],
      "allocations": {
        "faith-origins.04-a-different-dawn.destination-2": {
          "wood": 60,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.04-a-different-dawn.o2.req-2.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-3",
      "inputEntities": [
        "faith-origins.04-a-different-dawn.north-inventory-requests-1",
        "faith-origins.04-a-different-dawn.north-inventory-requests-2"
      ],
      "outputEntities": [
        "faith-origins.04-a-different-dawn.north-inventory-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.04-a-different-dawn.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 60,
            "gold": 20
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-4",
      "inputEntities": [
        "faith-origins.04-a-different-dawn.east-inventory-requests-1",
        "faith-origins.04-a-different-dawn.east-inventory-requests-2"
      ],
      "outputEntities": [
        "faith-origins.04-a-different-dawn.east-inventory-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.04-a-different-dawn.o2.req-2.paid",
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

EN: Both registers have their own exact funding receipt; 120 wood and 40 gold paid in total.

ES: Ambos registros tienen su recibo exacto propio; se pagaron en total 120 de madera y 40 de oro.

EN: Our two small accounts are not the emperor’s letter, nor evidence of a real property transfer.

ES: Nuestras dos cuentas pequeñas no son la carta del emperador ni pruebas de una transferencia real de propiedad.

### o3 / phase-3

EN: Deliver each register to its own northern/eastern court, and bring three assigned fictional neighbors alive to each.

ES: Entrega cada registro en su propio patio norte u oriental y lleva con vida tres vecinos ficticios asignados a cada uno.

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
        "faith-origins.04-a-different-dawn.north-inventory-register-1"
      ],
      "destinations": {
        "faith-origins.04-a-different-dawn.north-inventory-register-1": "faith-origins.04-a-different-dawn.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.04-a-different-dawn.east-inventory-register-1"
      ],
      "destinations": {
        "faith-origins.04-a-different-dawn.east-inventory-register-1": "faith-origins.04-a-different-dawn.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "state": "arrived",
      "requiredCount": 6,
      "id": "req-3",
      "entities": [
        "faith-origins.04-a-different-dawn.receiving-neighbors-1",
        "faith-origins.04-a-different-dawn.receiving-neighbors-2",
        "faith-origins.04-a-different-dawn.receiving-neighbors-3",
        "faith-origins.04-a-different-dawn.receiving-neighbors-4",
        "faith-origins.04-a-different-dawn.receiving-neighbors-5",
        "faith-origins.04-a-different-dawn.receiving-neighbors-6"
      ],
      "destinations": {
        "faith-origins.04-a-different-dawn.receiving-neighbors-1": "faith-origins.04-a-different-dawn.destination-3",
        "faith-origins.04-a-different-dawn.receiving-neighbors-2": "faith-origins.04-a-different-dawn.destination-3",
        "faith-origins.04-a-different-dawn.receiving-neighbors-3": "faith-origins.04-a-different-dawn.destination-3",
        "faith-origins.04-a-different-dawn.receiving-neighbors-4": "faith-origins.04-a-different-dawn.destination-4",
        "faith-origins.04-a-different-dawn.receiving-neighbors-5": "faith-origins.04-a-different-dawn.destination-4",
        "faith-origins.04-a-different-dawn.receiving-neighbors-6": "faith-origins.04-a-different-dawn.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both distinct registers and all six assigned neighbors reached the local receiving courts.

ES: Ambos registros distintos y los seis vecinos asignados llegaron a los patios receptores locales.

EN: I can close this invented account. The lives beyond it do not become settled because our ledger is complete.

ES: Puedo cerrar esta cuenta inventada. Las vidas que quedan fuera no se resuelven porque nuestro registro esté completo.

## Campaign finale and optional successor recommendations

Design-only continuity contract. Native variable writes, menu rendering and save/load behavior remain unverified.

```json
{
  "classification": "design-only; native variable/menu adapter and game QA pending",
  "selectionState": "route-selection",
  "choicePrompt": {
    "en": "The main work is complete. Choose which historical perspective to follow next. This choice is saved only with victory and recommends a campaign; earlier completed perspectives remain recorded.",
    "es-ES": "El trabajo principal está completo. Elige qué perspectiva histórica seguir. La elección se guarda solo con la victoria y recomienda una campaña; se conservan las perspectivas completadas anteriormente."
  },
  "completionMessage": {
    "en": "Embers of the Covenant is complete. Your chosen perspective recommends the following independent campaign. You may return to the campaign menu and choose another perspective on a later playthrough.",
    "es-ES": "Has completado Las brasas de la alianza. Tu perspectiva elegida recomienda la siguiente campaña independiente. Puedes volver al menú de campañas y elegir otra perspectiva en una partida posterior."
  },
  "routeChoices": [
    {
      "id": "christian-perspective",
      "progressKey": "progress.faith-origins.christian-perspective",
      "choiceLabel": {
        "en": "Follow imperial Christianity: The Eagle and the Cross.",
        "es-ES": "Sigue el cristianismo imperial: El águila y la cruz."
      },
      "chronologyWarning": {
        "en": "Recommended next for your Christian perspective. Its opening returns to 312 and overlaps this ending; it then follows a different narrator and later imperial debates. Embers of the Covenant is recommended background, not a requirement. Choose it from the campaign menu when ready.",
        "es-ES": "Siguiente recomendada para tu perspectiva cristiana. Su inicio vuelve a 312 y se solapa con este final; sigue después a otro narrador y a debates imperiales posteriores. Las brasas de la alianza es un antecedente recomendado, no obligatorio. Elígela en el menú cuando quieras."
      },
      "successor": {
        "campaignId": "imperial-church",
        "publicId": "CDF-C01",
        "title": {
          "en": "The Eagle and the Cross",
          "es-ES": "El águila y la cruz"
        }
      }
    },
    {
      "id": "jewish-perspective",
      "progressKey": "progress.faith-origins.jewish-perspective",
      "choiceLabel": {
        "en": "Follow Jewish traditions: Keepers of the Unbroken Word.",
        "es-ES": "Sigue las tradiciones judías: Guardianes de la palabra viva."
      },
      "chronologyWarning": {
        "en": "Recommended next for your Jewish perspective. Its opening returns to 70 and reexamines earlier events from another community’s perspective before continuing forward. Embers of the Covenant is recommended background, not a requirement. Choose it from the campaign menu when ready.",
        "es-ES": "Siguiente recomendada para tu perspectiva judía. Su inicio vuelve a 70 y reexamina sucesos anteriores desde la perspectiva de otra comunidad antes de avanzar. Las brasas de la alianza es un antecedente recomendado, no obligatorio. Elígela en el menú cuando quieras."
      },
      "successor": {
        "campaignId": "jewish-tradition",
        "publicId": "CDF-C02",
        "title": {
          "en": "Keepers of the Unbroken Word",
          "es-ES": "Guardianes de la palabra viva"
        }
      }
    }
  ],
  "selectionPolicy": {
    "requiredCount": 1,
    "allowPreviouslyCompletedRoute": true,
    "onCancel": "remain in route-selection; no progress write",
    "writesProgress": false,
    "closeSideRewardsOnEntry": true
  },
  "victoryCommit": {
    "on": "victory terminal latch after all mandatory objectives and one valid selected route",
    "write": "selected route progressKey = 1",
    "oncePerRun": true,
    "preserveOtherKeys": true,
    "resetOtherKeys": false,
    "onDefeat": "no progress write",
    "onSaveLoad": "restore pending choice or committed latch; never debit or write twice"
  },
  "recommendationPolicy": {
    "primary": "route selected in this victory",
    "otherCompletedRoutes": "show every accumulated completed route as an additional recommendation",
    "withoutCurrentChoice": "show all accumulated routes; never guess a selected route",
    "autoLaunch": false,
    "enforcePrerequisite": false,
    "successorEntry": "show recommended predecessor and recap; allow starting without predecessor"
  }
}
```

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/04-a-different-dawn.svg)

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
        "en": "Fictional local archive court",
        "es-ES": "Patio ficticio del archivo local"
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
        "en": "Western inventory work yard",
        "es-ES": "Patio occidental de inventario"
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
        "en": "Northern receiving court",
        "es-ES": "Patio receptor septentrional"
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
        "en": "Eastern receiving court",
        "es-ES": "Patio receptor oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-records",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-care",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "outer-inventory",
      "hubOrder": [
        "hub-3",
        "hub-4",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "inland plain circuits; exact Roman street/wall alignment pending"
    }
  ],
  "terrainInstructions": "Local inland Mediolanum frame in the Po plain. Four fictional record/receiving courts represent a dramatized local archive scene around 313, not the emperor’s palace or a proven restituted church property. The decade 303–313 is sourced context, not a uniformly persecuted Milan decade. Do not require a Po crossing, mountaintop fortress or sea voyage. Ancient walls, road entrances and minor watercourses need separately dated footprints; no Gothic Duomo, medieval Navigli, modern railway or present-day street grid. The meeting at Milan and the publication reported at Nicomedia are distinct places. Restitution law does not prove delivery of a particular Milan property. Terrain and real pathfinding remain pending.",
  "corridorStraightLengthsTiles": {
    "north-records": 271.35,
    "east-care": 332.07,
    "outer-inventory": 356.63
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
  "asset": "docs/design/maps/faith-origins/odyssey/04-a-different-dawn.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.04-a-different-dawn.north-inventory-requests-1",
      "role": "fictional-neighborhood-inventory-request",
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
      "id": "faith-origins.04-a-different-dawn.north-inventory-requests-2",
      "role": "fictional-neighborhood-inventory-request",
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
      "id": "faith-origins.04-a-different-dawn.east-inventory-requests-1",
      "role": "fictional-neighborhood-inventory-request",
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
      "id": "faith-origins.04-a-different-dawn.east-inventory-requests-2",
      "role": "fictional-neighborhood-inventory-request",
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
      "id": "faith-origins.04-a-different-dawn.north-inventory-register-1",
      "role": "fictional-local-inventory-register",
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
      "id": "faith-origins.04-a-different-dawn.east-inventory-register-1",
      "role": "fictional-local-inventory-register",
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
      "id": "faith-origins.04-a-different-dawn.receiving-neighbors-1",
      "role": "fictional-voluntary-neighbor",
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
      "id": "faith-origins.04-a-different-dawn.receiving-neighbors-2",
      "role": "fictional-voluntary-neighbor",
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
      "id": "faith-origins.04-a-different-dawn.receiving-neighbors-3",
      "role": "fictional-voluntary-neighbor",
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
      "id": "faith-origins.04-a-different-dawn.receiving-neighbors-4",
      "role": "fictional-voluntary-neighbor",
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
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.04-a-different-dawn.receiving-neighbors-5",
      "role": "fictional-voluntary-neighbor",
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
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.04-a-different-dawn.receiving-neighbors-6",
      "role": "fictional-voluntary-neighbor",
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
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.04-a-different-dawn.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.04-a-different-dawn.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.04-a-different-dawn.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.04-a-different-dawn.destination-4",
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
    "north-inventory-requests": [
      "faith-origins.04-a-different-dawn.north-inventory-requests-1",
      "faith-origins.04-a-different-dawn.north-inventory-requests-2"
    ],
    "east-inventory-requests": [
      "faith-origins.04-a-different-dawn.east-inventory-requests-1",
      "faith-origins.04-a-different-dawn.east-inventory-requests-2"
    ],
    "north-inventory-register": [
      "faith-origins.04-a-different-dawn.north-inventory-register-1"
    ],
    "east-inventory-register": [
      "faith-origins.04-a-different-dawn.east-inventory-register-1"
    ],
    "receiving-neighbors": [
      "faith-origins.04-a-different-dawn.receiving-neighbors-1",
      "faith-origins.04-a-different-dawn.receiving-neighbors-2",
      "faith-origins.04-a-different-dawn.receiving-neighbors-3",
      "faith-origins.04-a-different-dawn.receiving-neighbors-4",
      "faith-origins.04-a-different-dawn.receiving-neighbors-5",
      "faith-origins.04-a-different-dawn.receiving-neighbors-6"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.04-a-different-dawn.receiving-neighbors-1",
        "faith-origins.04-a-different-dawn.receiving-neighbors-2",
        "faith-origins.04-a-different-dawn.receiving-neighbors-3",
        "faith-origins.04-a-different-dawn.receiving-neighbors-4",
        "faith-origins.04-a-different-dawn.receiving-neighbors-5",
        "faith-origins.04-a-different-dawn.receiving-neighbors-6"
      ],
      "minimumAliveOrAlreadySafe": 6
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### The agreement and the published letter / El acuerdo y la carta publicada

EN: Recover both separate copies from the agreement and the published letter and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de el acuerdo y la carta publicada y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Keep fictional context labels distinct: Milan meeting versus Nicomedia publication; no invented imperial autograph.

ES: Separa etiquetas ficticias de contexto: reunión en Milán frente a publicación en Nicomedia; no inventes autógrafos imperiales.

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
          "04-a-different-dawn.side-1.entity-1",
          "04-a-different-dawn.side-1.entity-2"
        ],
        "destinations": {
          "04-a-different-dawn.side-1.entity-1": "04-a-different-dawn.side-1.zone-1",
          "04-a-different-dawn.side-1.entity-2": "04-a-different-dawn.side-1.zone-1"
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
        "id": "04-a-different-dawn.side-1.entity-1",
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
        "id": "04-a-different-dawn.side-1.entity-2",
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
        "id": "04-a-different-dawn.side-1.zone-1",
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
      "onceFlag": "04-a-different-dawn.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.04-a-different-dawn"
      ],
      "historicalNote": {
        "en": "Eusebius reports measures against churches and Christian texts from 303, with a Christian interpretation and selective coverage. Lactantius transmits a 313 letter concerning religious freedom and restoration of Christian communal property, reporting agreement at Milan and publication at Nicomedia on 13 June. These sources do not establish uniform enforcement or a particular restored Milan archive. Our local work scene is fictional.",
        "es-ES": "Eusebio informa de medidas contra iglesias y textos cristianos desde 303, con interpretación cristiana y cobertura selectiva. Lactancio transmite una carta de 313 sobre libertad religiosa y restitución de propiedades comunitarias cristianas; relata un acuerdo en Milán y su publicación en Nicomedia el 13 de junio. Estas fuentes no acreditan aplicación uniforme ni un archivo concreto restituido en Milán. Nuestra escena local de trabajo es ficticia."
      },
      "hint": {
        "en": "Collect both northern and both eastern inventory requests and deliver all four to the western work yard.",
        "es-ES": "Recoge ambas solicitudes de inventario norteñas y ambas orientales y entrega las cuatro en el patio occidental."
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
      "north-records",
      "east-care",
      "outer-inventory"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Neighbors outside the inventory / Vecinos fuera del inventario

EN: Bring each of the two aid crates to its assigned household at neighbors outside the inventory. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en vecinos fuera del inventario. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid separate fictional households irrespective of belief; no property-right or conversion reward.

ES: Ayuda a hogares ficticios separados sin distinción de creencia; no otorga derechos de propiedad ni conversiones.

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
          "04-a-different-dawn.side-2.entity-1",
          "04-a-different-dawn.side-2.entity-2"
        ],
        "destinations": {
          "04-a-different-dawn.side-2.entity-1": "04-a-different-dawn.side-2.zone-1",
          "04-a-different-dawn.side-2.entity-2": "04-a-different-dawn.side-2.zone-2"
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
        "id": "04-a-different-dawn.side-2.entity-1",
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
        "id": "04-a-different-dawn.side-2.entity-2",
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
        "id": "04-a-different-dawn.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "04-a-different-dawn.side-2.zone-2",
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
      "onceFlag": "04-a-different-dawn.side-2.rewarded",
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
      "north-records",
      "east-care",
      "outer-inventory"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### An ordinary archive shelter / Un cobertizo ordinario de archivo

EN: Pay 50 wood and restore the damaged store of an ordinary archive shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de un cobertizo ordinario de archivo. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Finite repair does not reconstruct a documented destroyed church or guarantee ancient restitution.

ES: Una reparación finita no reconstruye una iglesia destruida documentada ni garantiza restituciones antiguas.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "04-a-different-dawn.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "04-a-different-dawn.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "04-a-different-dawn.side-3.payment",
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
        "id": "04-a-different-dawn.side-3.entity-1",
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
        "id": "04-a-different-dawn.side-3.zone-1",
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
      "onceFlag": "04-a-different-dawn.side-3.rewarded",
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
      "north-records",
      "east-care",
      "outer-inventory"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The local archive supply exchange / El intercambio local de provisiones del archivo

EN: Escort the trader of the local archive supply exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de el intercambio local de provisiones del archivo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One bounded supply exchange cannot fund both exact mandatory receipts twice or purchase ownership.

ES: Un intercambio limitado no financia dos veces ambos recibos principales ni compra propiedades.

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
          "04-a-different-dawn.side-4.entity-1"
        ],
        "destinations": {
          "04-a-different-dawn.side-4.entity-1": "04-a-different-dawn.side-4.zone-1"
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
        "receipt": "04-a-different-dawn.side-4.payment",
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
        "id": "04-a-different-dawn.side-4.entity-1",
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
        "id": "04-a-different-dawn.side-4.zone-1",
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
      "onceFlag": "04-a-different-dawn.side-4.rewarded",
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
      "north-records",
      "east-care",
      "outer-inventory"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Northern plain approaches / Accesos septentrionales de la llanura

EN: Scout both marked viewpoints of northern plain approaches. Benefit: Mark the surveyed north-records land circuit once. Every main receiver is already disclosed.

ES: Explora los dos miradores señalados de accesos septentrionales de la llanura. Ventaja: Señala una vez el circuito terrestre reconocido north-records. Todos los receptores principales están ya indicados.

EN: Survey the authored local north route; do not invent exact Roman gates or a battlefield.

ES: Reconoce la ruta norte local diseñada; no inventes puertas romanas exactas ni campos de batalla.

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
          "04-a-different-dawn.side-5.zone-1",
          "04-a-different-dawn.side-5.zone-2"
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
        "id": "04-a-different-dawn.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "04-a-different-dawn.side-5.zone-2",
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
      "target": "north-records local land circuit",
      "resources": {},
      "onceFlag": "04-a-different-dawn.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "north-records"
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
      "north-records",
      "east-care",
      "outer-inventory"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The outer inventory circuit / El circuito exterior de inventario

EN: Escort the local guide of the outer inventory circuit to the marked road junction. Benefit: Mark the surveyed outer-inventory land circuit once. Every main receiver is already disclosed.

ES: Escolta al guía local de el circuito exterior de inventario hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre reconocido outer-inventory. Todos los receptores principales están ya indicados.

EN: Mark the disclosed inland circuit between separate receiving courts; never auto-launch another campaign.

ES: Señala el circuito interior indicado entre patios receptores separados; nunca inicia otra campaña automáticamente.

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
          "04-a-different-dawn.side-6.entity-1"
        ],
        "destinations": {
          "04-a-different-dawn.side-6.entity-1": "04-a-different-dawn.side-6.zone-1"
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
        "id": "04-a-different-dawn.side-6.entity-1",
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
        "id": "04-a-different-dawn.side-6.zone-1",
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
      "target": "outer-inventory local land circuit",
      "resources": {},
      "onceFlag": "04-a-different-dawn.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "outer-inventory"
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
      "north-records",
      "east-care",
      "outer-inventory"
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
      "id": "split-register-crews",
      "optionalObjectives": [
        "side-4",
        "side-5"
      ],
      "costOfOpportunity": "Separate north/east input crews and receipt funding; keep 120 wood/40 gold mandatory reserve.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "context-before-restitution",
      "optionalObjectives": [
        "side-1",
        "side-3"
      ],
      "costOfOpportunity": "Preserve legal provenance and repair the separate shelter without treating gameplay as proof of restitution.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "care-before-archive",
      "optionalObjectives": [
        "side-2",
        "side-6"
      ],
      "costOfOpportunity": "Move separate optional recipients while main neighbors and registers remain assigned to their own destinations.",
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
      "wood": 828,
      "gold": 244,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 120,
      "gold": 40,
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
      "wood": 800,
      "gold": 330,
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
      "wood": 850,
      "gold": 255,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 120,
      "gold": 40,
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
      "wood": 800,
      "gold": 330,
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
      "wood": 873,
      "gold": 267,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 120,
      "gold": 40,
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
      "wood": 800,
      "gold": 330,
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
| scenario.faith-origins.04-a-different-dawn.odyssey.title / always | none | A Different Dawn | Un alba distinta |
| scenario.faith-origins.04-a-different-dawn.odyssey.fact-intro / intro first | collection-narrator | Eusebius reports measures against churches and Christian texts from 303, with a Christian interpretation and selective coverage. Lactantius transmits a 313 letter concerning religious freedom and restoration of Christian communal property, reporting agreement at Milan and publication at Nicomedia on 13 June. These sources do not establish uniform enforcement or a particular restored Milan archive. Our local work scene is fictional. | Eusebio informa de medidas contra iglesias y textos cristianos desde 303, con interpretación cristiana y cobertura selectiva. Lactancio transmite una carta de 313 sobre libertad religiosa y restitución de propiedades comunitarias cristianas; relata un acuerdo en Milán y su publicación en Nicomedia el 13 de junio. Estas fuentes no acreditan aplicación uniforme ni un archivo concreto restituido en Milán. Nuestra escena local de trabajo es ficticia. |
| scenario.faith-origins.04-a-different-dawn.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.04-a-different-dawn.odyssey.persona-intro / after handover | miriam-archive | In our fiction I am in a Milan work yard around 313, sorting ordinary notes. I know the earlier measures through inherited and arriving reports, not by standing in every province. I want a dawn that answers every loss. The records give me an order for restitution, and leave many individual answers unwritten. | En nuestra ficción estoy en un patio de trabajo de Milán hacia 313, ordenando notas ordinarias. Conozco las medidas anteriores por relatos heredados y recibidos, no por haber estado en todas las provincias. Quiero un alba que responda a cada pérdida. Los documentos me dan una orden de restitución y dejan muchas respuestas individuales sin escribir. |
| scenario.faith-origins.04-a-different-dawn.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.04-a-different-dawn.odyssey.route-help / available from start; repeatable without effect | none | Bring two northern inventory requests and two eastern inventory requests to the western yard. Fund each register separately with 60 wood and 20 gold. Deliver the northern register to the north court and the eastern register to the east court, with three assigned fictional neighbors at each. After all main goals, choose a historical perspective to complete this campaign; the choice recommends the next campaign and changes no historical outcome. | Lleva dos solicitudes de inventario norteñas y dos orientales al patio occidental. Financia cada registro por separado con 60 de madera y 20 de oro. Entrega el registro norteño en el patio norte y el oriental en el oriental, con tres vecinos ficticios asignados a cada uno. Tras todos los objetivos principales, elige una perspectiva histórica para completar esta campaña; la elección recomienda la siguiente y no cambia desenlaces históricos. |
| scenario.faith-origins.04-a-different-dawn.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.o1-goal / phase-1 active | none | Collect both northern and both eastern inventory requests and deliver all four to the western work yard. | Recoge ambas solicitudes de inventario norteñas y ambas orientales y entrega las cuatro en el patio occidental. |
| scenario.faith-origins.04-a-different-dawn.odyssey.o1-receipt / o1 latched once | none | Four original local inventory requests reached the work yard. | Cuatro solicitudes originales de inventario local llegaron al patio de trabajo. |
| scenario.faith-origins.04-a-different-dawn.odyssey.o1-reaction / after o1 receipt | miriam-archive | A request can name a hope; it cannot prove that hope was granted in history. | Una solicitud puede nombrar una esperanza; no prueba que la historia la concediera. |
| scenario.faith-origins.04-a-different-dawn.odyssey.o2-goal / phase-2 active | none | Pay 60 wood and 20 gold for each distinct register, then prepare both from their own collected requests. | Paga 60 de madera y 20 de oro por cada registro distinto y prepara ambos a partir de sus propias solicitudes recogidas. |
| scenario.faith-origins.04-a-different-dawn.odyssey.o2-receipt / o2 latched once | none | Both registers have their own exact funding receipt; 120 wood and 40 gold paid in total. | Ambos registros tienen su recibo exacto propio; se pagaron en total 120 de madera y 40 de oro. |
| scenario.faith-origins.04-a-different-dawn.odyssey.o2-reaction / after o2 receipt | miriam-archive | Our two small accounts are not the emperor’s letter, nor evidence of a real property transfer. | Nuestras dos cuentas pequeñas no son la carta del emperador ni pruebas de una transferencia real de propiedad. |
| scenario.faith-origins.04-a-different-dawn.odyssey.o3-goal / phase-3 active | none | Deliver each register to its own northern/eastern court, and bring three assigned fictional neighbors alive to each. | Entrega cada registro en su propio patio norte u oriental y lleva con vida tres vecinos ficticios asignados a cada uno. |
| scenario.faith-origins.04-a-different-dawn.odyssey.o3-receipt / o3 latched once | none | Both distinct registers and all six assigned neighbors reached the local receiving courts. | Ambos registros distintos y los seis vecinos asignados llegaron a los patios receptores locales. |
| scenario.faith-origins.04-a-different-dawn.odyssey.o3-reaction / after o3 receipt | miriam-archive | I can close this invented account. The lives beyond it do not become settled because our ledger is complete. | Puedo cerrar esta cuenta inventada. Las vidas que quedan fuera no se resuelven porque nuestro registro esté completo. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from the agreement and the published letter and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de el acuerdo y la carta publicada y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-1-complete / side-1 completed | none | The agreement and the published letter completed. Its stated benefit has been granted once. | El acuerdo y la carta publicada: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-1-lost / side-1 failed-optional | none | The agreement and the published letter is unavailable after the loss of its unique participant or object. The main mission continues. | El acuerdo y la carta publicada: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at neighbors outside the inventory. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en vecinos fuera del inventario. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-2-complete / side-2 completed | none | Neighbors outside the inventory completed. Its stated benefit has been granted once. | Vecinos fuera del inventario: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-2-lost / side-2 failed-optional | none | Neighbors outside the inventory is unavailable after the loss of its unique participant or object. The main mission continues. | Vecinos fuera del inventario: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of an ordinary archive shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de un cobertizo ordinario de archivo. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-3-complete / side-3 completed | none | An ordinary archive shelter completed. Its stated benefit has been granted once. | Un cobertizo ordinario de archivo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-3-lost / side-3 failed-optional | none | An ordinary archive shelter is unavailable after the loss of its unique participant or object. The main mission continues. | Un cobertizo ordinario de archivo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-4-goal / optional list from start | none | Escort the trader of the local archive supply exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de el intercambio local de provisiones del archivo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-4-complete / side-4 completed | none | The local archive supply exchange completed. Its stated benefit has been granted once. | El intercambio local de provisiones del archivo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-4-lost / side-4 failed-optional | none | The local archive supply exchange is unavailable after the loss of its unique participant or object. The main mission continues. | El intercambio local de provisiones del archivo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of northern plain approaches. Benefit: Mark the surveyed north-records land circuit once. Every main receiver is already disclosed. | Explora los dos miradores señalados de accesos septentrionales de la llanura. Ventaja: Señala una vez el circuito terrestre reconocido north-records. Todos los receptores principales están ya indicados. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-5-complete / side-5 completed | none | Northern plain approaches completed. Its stated benefit has been granted once. | Accesos septentrionales de la llanura: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-5-lost / side-5 failed-optional | none | Northern plain approaches is unavailable after the loss of its unique participant or object. The main mission continues. | Accesos septentrionales de la llanura: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the outer inventory circuit to the marked road junction. Benefit: Mark the surveyed outer-inventory land circuit once. Every main receiver is already disclosed. | Escolta al guía local de el circuito exterior de inventario hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre reconocido outer-inventory. Todos los receptores principales están ya indicados. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-6-complete / side-6 completed | none | The outer inventory circuit completed. Its stated benefit has been granted once. | El circuito exterior de inventario: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.04-a-different-dawn.odyssey.side-6-lost / side-6 failed-optional | none | The outer inventory circuit is unavailable after the loss of its unique participant or object. The main mission continues. | El circuito exterior de inventario: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.04-a-different-dawn.odyssey.fact-outro / victory first | collection-narrator | The fictional archive’s two inventory registers and six neighbor care deliveries are complete. Neither register demonstrates a historical property transfer. The reported 313 agreement and letter do not erase previous violence or establish the later outcomes of imperial Christianity or Jewish communities. Those histories continue in separate campaigns with overlapping dates and different perspectives. | Se han completado los dos registros de inventario del archivo ficticio y seis entregas de cuidados a vecinos. Ningún registro demuestra una transferencia histórica de propiedad. El acuerdo y la carta relatados de 313 no borran la violencia anterior ni determinan los desenlaces posteriores del cristianismo imperial o de las comunidades judías. Esas historias continúan en campañas separadas, con fechas solapadas y perspectivas diferentes. |
| scenario.faith-origins.04-a-different-dawn.odyssey.persona-outro / after fact-outro | miriam-archive | My shelves will not hold every life. I have learned to name what they hold, and what they do not. If you follow the eagle and the cross, another voice will meet you. If you turn toward the keepers of the word, leave my certainties at their door and listen. | Mis estantes no contendrán todas las vidas. He aprendido a nombrar lo que guardan y lo que no. Si sigues al águila y la cruz, te recibirá otra voz. Si te vuelves hacia quienes guardan la palabra, deja mis certezas a su puerta y escucha. |
| scenario.faith-origins.04-a-different-dawn.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.04-a-different-dawn.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.04-a-different-dawn.odyssey.route-choice / route-selection active; no progress write | none | The main work is complete. Choose which historical perspective to follow next. This choice is saved only with victory and recommends a campaign; earlier completed perspectives remain recorded. | El trabajo principal está completo. Elige qué perspectiva histórica seguir. La elección se guarda solo con la victoria y recomienda una campaña; se conservan las perspectivas completadas anteriormente. |
| scenario.faith-origins.04-a-different-dawn.odyssey.campaign-complete / after persona-outro | none | Embers of the Covenant is complete. Your chosen perspective recommends the following independent campaign. You may return to the campaign menu and choose another perspective on a later playthrough. | Has completado Las brasas de la alianza. Tu perspectiva elegida recomienda la siguiente campaña independiente. Puedes volver al menú de campañas y elegir otra perspectiva en una partida posterior. |
| scenario.faith-origins.04-a-different-dawn.odyssey.choose-christian-perspective / route-selection active; selectable without prior completion | none | Follow imperial Christianity: The Eagle and the Cross. | Sigue el cristianismo imperial: El águila y la cruz. |
| scenario.faith-origins.04-a-different-dawn.odyssey.next-campaign-christian-perspective / after campaign-complete; selected or accumulated route christian-perspective | none | The Eagle and the Cross (CDF-C01). Recommended next for your Christian perspective. Its opening returns to 312 and overlaps this ending; it then follows a different narrator and later imperial debates. Embers of the Covenant is recommended background, not a requirement. Choose it from the campaign menu when ready. | El águila y la cruz (CDF-C01). Siguiente recomendada para tu perspectiva cristiana. Su inicio vuelve a 312 y se solapa con este final; sigue después a otro narrador y a debates imperiales posteriores. Las brasas de la alianza es un antecedente recomendado, no obligatorio. Elígela en el menú cuando quieras. |
| scenario.faith-origins.04-a-different-dawn.odyssey.choose-jewish-perspective / route-selection active; selectable without prior completion | none | Follow Jewish traditions: Keepers of the Unbroken Word. | Sigue las tradiciones judías: Guardianes de la palabra viva. |
| scenario.faith-origins.04-a-different-dawn.odyssey.next-campaign-jewish-perspective / after campaign-complete; selected or accumulated route jewish-perspective | none | Keepers of the Unbroken Word (CDF-C02). Recommended next for your Jewish perspective. Its opening returns to 70 and reexamines earlier events from another community’s perspective before continuing forward. Embers of the Covenant is recommended background, not a requirement. Choose it from the campaign menu when ready. | Guardianes de la palabra viva (CDF-C02). Siguiente recomendada para tu perspectiva judía. Su inicio vuelve a 70 y reexamina sucesos anteriores desde la perspectiva de otra comunidad antes de avanzar. Las brasas de la alianza es un antecedente recomendado, no obligatorio. Elígela en el menú cuando quieras. |

## Production, recovery and verification

```json
{
  "stateMachine": {
    "states": [
      "briefing",
      "phase-1",
      "phase-2",
      "phase-3",
      "route-selection",
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
        "to": "route-selection",
        "on": "objective-latched",
        "objectiveId": "o3"
      },
      {
        "from": "route-selection",
        "to": "victory",
        "on": "valid-route-selected"
      }
    ],
    "terminalPriority": "defeat first; close side rewards; one terminal latch",
    "saveLoad": "persist object identities, arrivals, collected facts, receipts, phase elapsed time and side reward balances",
    "campaignProgressWrite": true
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
      "id": "accumulative-finale-menu",
      "status": "design-only canonical route contract; native choice, victory variable writes, retained keys and save/load QA pending"
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
      "final display order 30 retains semantic ID 04-a-different-dawn",
      "north receipt cannot fund eastern register",
      "loss of main identity before route choice defeats with zero progress writes",
      "cancel route choice keeps pending state and writes nothing",
      "choose Christian then replay Jewish: both progress keys stay 1",
      "save/load before choice and after victory cannot write/debit twice",
      "recommend selected route and show other accumulated routes",
      "next titles and public IDs come from canonical catalogue",
      "no auto-launch or predecessor lock; warn chronological overlap in EN/es-ES",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
