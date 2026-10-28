# 3. The Doors Returned

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `03-property-and-record-restoration-nicomedia` · 13 June 313 CE · 400×400

## Historical frame and fixed outcome

EN: Lactantius reports Licinius publishing a letter at Nicomedia on 13 June 313. The transmitted text grants religious choice and orders restoration of Christian communal property, distinguishing communal from individual ownership and allowing indemnity requests. A legal order does not prove every local restoration. Our two receiving yards and their working records are fictional.

ES: Lactancio relata la publicación por Licinio de una carta en Nicomedia el 13 de junio de 313. El texto transmitido concede elección religiosa y ordena restituir bienes comunitarios cristianos; distingue la propiedad comunitaria de la individual y permite solicitar indemnizaciones. Una orden jurídica no prueba todas las restituciones locales. Nuestros dos patios receptores y sus documentos de trabajo son ficticios.

EN: Two fictional yards were observed as controlled and passable, funded separately and given their own working registers and assigned neighbors. This models local administrative work, not a documented Christian property transfer. The letter’s legal terms remain distinct from their uneven and partly unrecorded implementation.

ES: Dos patios ficticios se observaron bajo control y transitables, se financiaron por separado y recibieron sus propios registros de trabajo y vecinos asignados. Esto representa trabajo administrativo local, no una transferencia documentada de propiedad cristiana. Los términos jurídicos de la carta permanecen distintos de su aplicación desigual y parcialmente no registrada.

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
      "consultedUrl": "https://sourcebooks.fordham.edu/source/edict-milan.asp",
      "passage": "Eusebius HE X.5 as reproduced in Fordham; lines on Nicomedia and restitution.",
      "limitations": "The text is not the original Milan instrument; legal order is not proof of uniform practical restitution.",
      "status": "consulted",
      "supportedClaim": "Supports Licinius’ Nicomedian publication of a rescript ordering freedom of worship and restoration of communal property. / Apoya la publicación nicomediense de un rescripto de Licinio que ordena libertad de culto y restitución de bienes comunitarios.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "Fordham editorial note and rescript translation; Eusebius HE X.5 checked.",
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

EN: Collect four original ordinary inventory notes and deliver all four to the western local inventory yard.

ES: Recoge cuatro notas originales ordinarias de inventario y entrega las cuatro en el patio occidental.

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
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-1",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-2",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-3",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-4"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-1",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-2",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-3",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-4"
      ],
      "destinations": {
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-1": "imperial-church.03-property-and-record-restoration-nicomedia.destination-2",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-2": "imperial-church.03-property-and-record-restoration-nicomedia.destination-2",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-3": "imperial-church.03-property-and-record-restoration-nicomedia.destination-2",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-4": "imperial-church.03-property-and-record-restoration-nicomedia.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All four distinct working identities reached the inventory yard.

ES: Las cuatro identidades distintas de trabajo llegaron al patio de inventario.

EN: A local list of imagined goods cannot become an imperial property roll by being complete.

ES: Una lista local de bienes imaginados no se convierte en registro imperial de propiedades por estar completa.

### o2 / phase-2

EN: Observe both receiving yards controlled and passable; pay each its own 60 wood and 20 gold once.

ES: Observa ambos patios receptores bajo control y transitables; paga a cada uno una vez sus propios 60 de madera y 20 de oro.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "area-state",
      "requiredCount": 2,
      "state": "controlled-and-passable",
      "blockingEnemies": [],
      "observationPolicy": "actual separate access/control observations; not visibility, elapsed time, property ownership proof or reconstructed ancient church repair",
      "id": "req-1",
      "zones": [
        "imperial-church.03-property-and-record-restoration-nicomedia.destination-3",
        "imperial-church.03-property-and-record-restoration-nicomedia.destination-4"
      ]
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 60,
        "gold": 20
      },
      "id": "req-2",
      "receivingZones": [
        "imperial-church.03-property-and-record-restoration-nicomedia.destination-3"
      ],
      "allocations": {
        "imperial-church.03-property-and-record-restoration-nicomedia.destination-3": {
          "wood": 60,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.03-property-and-record-restoration-nicomedia.o2.req-2.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 60,
        "gold": 20
      },
      "id": "req-3",
      "receivingZones": [
        "imperial-church.03-property-and-record-restoration-nicomedia.destination-4"
      ],
      "allocations": {
        "imperial-church.03-property-and-record-restoration-nicomedia.destination-4": {
          "wood": 60,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.03-property-and-record-restoration-nicomedia.o2.req-3.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both separate yards are observed usable and have separate preparation payments.

ES: Ambos patios separados se observan utilizables y tienen pagos separados de preparación.

EN: Access and payment are the limits of our small task. Neither certifies historical ownership.

ES: Acceso y pago son los límites de nuestra pequeña tarea. Ninguno certifica propiedades históricas.

### o3 / phase-3

EN: Prepare two distinct yard registers, each from the collected notes and its own yard’s exact payment receipt.

ES: Prepara dos registros de patio distintos, cada uno con las notas recogidas y el recibo exacto de su propio patio.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-1",
      "inputEntities": [
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-1",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-2",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-3",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-4"
      ],
      "outputEntities": [
        "imperial-church.03-property-and-record-restoration-nicomedia.north-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.03-property-and-record-restoration-nicomedia.o2.req-2.paid",
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
      "id": "req-2",
      "inputEntities": [
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-1",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-2",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-3",
        "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-4"
      ],
      "outputEntities": [
        "imperial-church.03-property-and-record-restoration-nicomedia.east-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.03-property-and-record-restoration-nicomedia.o2.req-3.paid",
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

EN: Each fictional register cites its own funded yard without another debit.

ES: Cada registro ficticio cita su propio patio financiado sin otro cobro.

EN: Two registers do not prove two restorations. I will keep those verbs apart.

ES: Dos registros no prueban dos restituciones. Mantendré separados esos verbos.

### o4 / phase-4

EN: Deliver each register and its two assigned original neighbors to the matching northern/eastern yard.

ES: Entrega cada registro y sus dos vecinos originales asignados en el patio norteño u oriental correspondiente.

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
        "imperial-church.03-property-and-record-restoration-nicomedia.north-register-1"
      ],
      "destinations": {
        "imperial-church.03-property-and-record-restoration-nicomedia.north-register-1": "imperial-church.03-property-and-record-restoration-nicomedia.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.03-property-and-record-restoration-nicomedia.east-register-1"
      ],
      "destinations": {
        "imperial-church.03-property-and-record-restoration-nicomedia.east-register-1": "imperial-church.03-property-and-record-restoration-nicomedia.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "state": "arrived",
      "requiredCount": 4,
      "id": "req-3",
      "entities": [
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-1",
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-2",
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-3",
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-4"
      ],
      "destinations": {
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-1": "imperial-church.03-property-and-record-restoration-nicomedia.destination-3",
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-2": "imperial-church.03-property-and-record-restoration-nicomedia.destination-3",
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-3": "imperial-church.03-property-and-record-restoration-nicomedia.destination-4",
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-4": "imperial-church.03-property-and-record-restoration-nicomedia.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both registers and all four assigned neighbors reached their own local yards.

ES: Ambos registros y los cuatro vecinos asignados llegaron a sus patios locales propios.

EN: The people in our fiction reached a yard. The people outside our records deserve more than an automatic conclusion.

ES: Las personas de nuestra ficción llegaron a un patio. Las que quedan fuera de nuestros documentos merecen más que una conclusión automática.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/03-property-and-record-restoration-nicomedia.svg)

```json
{
  "bbox": [
    29.905,
    40.758,
    29.995,
    40.822
  ],
  "terrainProfile": "bithynia",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        120.33,
        267.47
      ],
      "lonLat": [
        29.93,
        40.777
      ],
      "name": {
        "en": "Local inland pickup court",
        "es-ES": "Patio interior local de recogida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        60.96,
        298.84
      ],
      "lonLat": [
        29.915,
        40.771
      ],
      "name": {
        "en": "Western local inventory yard",
        "es-ES": "Patio occidental de inventario local"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        159.92,
        84.48
      ],
      "lonLat": [
        29.94,
        40.812
      ],
      "name": {
        "en": "Northern fictional receiving yard",
        "es-ES": "Patio receptor ficticio norteño"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        318.25,
        236.1
      ],
      "lonLat": [
        29.98,
        40.783
      ],
      "name": {
        "en": "Eastern fictional receiving yard",
        "es-ES": "Patio receptor ficticio oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-access",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-access",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "inland-link",
      "hubOrder": [
        "hub-3",
        "hub-4",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 6
    }
  ],
  "terrainInstructions": "Nicomedia local inland north side of the gulf head, within the existing Bithynia profile. All four invented working courts remain on the northern land approach; coastal water stays south/west outside main routes. Northern hills require graded land access, not cliff ramps or a giant invented river. No modern Izmit docks/refineries, freeway, Ottoman defenses or later basilica. Two usable yards are fictional, not excavated restituted churches. Publication point, palace and Christian property boundaries are not identified. Ancient shore, grades, exact workplaces and native footprints need dated audit.",
  "corridorStraightLengthsTiles": {
    "north-access": 303.25,
    "east-access": 331.98,
    "inland-link": 419.61
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
  "asset": "docs/design/maps/imperial-church/odyssey/03-property-and-record-restoration-nicomedia.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-1",
      "role": "fictional-local-inventory-note",
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
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-2",
      "role": "fictional-local-inventory-note",
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
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-3",
      "role": "fictional-local-inventory-note",
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
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-4",
      "role": "fictional-local-inventory-note",
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
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.north-register-1",
      "role": "fictional-local-yard-register",
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
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.east-register-1",
      "role": "fictional-local-yard-register",
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
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-1",
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
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-2",
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
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-3",
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
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-4",
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
    }
  ],
  "zones": [
    {
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.03-property-and-record-restoration-nicomedia.destination-4",
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
    "inventory-notes": [
      "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-1",
      "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-2",
      "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-3",
      "imperial-church.03-property-and-record-restoration-nicomedia.inventory-notes-4"
    ],
    "north-register": [
      "imperial-church.03-property-and-record-restoration-nicomedia.north-register-1"
    ],
    "east-register": [
      "imperial-church.03-property-and-record-restoration-nicomedia.east-register-1"
    ],
    "yard-neighbors": [
      "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-1",
      "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-2",
      "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-3",
      "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-4"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-1",
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-2",
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-3",
        "imperial-church.03-property-and-record-restoration-nicomedia.yard-neighbors-4"
      ],
      "minimumAliveOrAlreadySafe": 4
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Communal and private property labels / Etiquetas de propiedad comunitaria y privada

EN: Recover both separate copies from communal and private property labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de etiquetas de propiedad comunitaria y privada y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Sourced legal context separates the letter’s categories without assigning a historical property to a fictional yard.

ES: El contexto jurídico distingue categorías de la carta sin asignar propiedades históricas a patios ficticios.

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
          "03-property-and-record-restoration-nicomedia.side-1.entity-1",
          "03-property-and-record-restoration-nicomedia.side-1.entity-2"
        ],
        "destinations": {
          "03-property-and-record-restoration-nicomedia.side-1.entity-1": "03-property-and-record-restoration-nicomedia.side-1.zone-1",
          "03-property-and-record-restoration-nicomedia.side-1.entity-2": "03-property-and-record-restoration-nicomedia.side-1.zone-1"
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
        "id": "03-property-and-record-restoration-nicomedia.side-1.entity-1",
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
        "id": "03-property-and-record-restoration-nicomedia.side-1.entity-2",
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
        "id": "03-property-and-record-restoration-nicomedia.side-1.zone-1",
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
      "onceFlag": "03-property-and-record-restoration-nicomedia.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.03-property-and-record-restoration-nicomedia"
      ],
      "historicalNote": {
        "en": "Lactantius reports Licinius publishing a letter at Nicomedia on 13 June 313. The transmitted text grants religious choice and orders restoration of Christian communal property, distinguishing communal from individual ownership and allowing indemnity requests. A legal order does not prove every local restoration. Our two receiving yards and their working records are fictional.",
        "es-ES": "Lactancio relata la publicación por Licinio de una carta en Nicomedia el 13 de junio de 313. El texto transmitido concede elección religiosa y ordena restituir bienes comunitarios cristianos; distingue la propiedad comunitaria de la individual y permite solicitar indemnizaciones. Una orden jurídica no prueba todas las restituciones locales. Nuestros dos patios receptores y sus documentos de trabajo son ficticios."
      },
      "hint": {
        "en": "Collect four original ordinary inventory notes and deliver all four to the western local inventory yard.",
        "es-ES": "Recoge cuatro notas originales ordinarias de inventario y entrega las cuatro en el patio occidental."
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
      "north-access",
      "east-access",
      "inland-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Independent gulf-side households / Hogares independientes próximos al golfo

EN: Bring each of the two aid crates to its assigned household at independent gulf-side households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes próximos al golfo. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid fictional households on land; no particular historic congregation or religious status required.

ES: Ayuda a hogares ficticios en tierra; no exige congregación histórica concreta ni condición religiosa.

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
          "03-property-and-record-restoration-nicomedia.side-2.entity-1",
          "03-property-and-record-restoration-nicomedia.side-2.entity-2"
        ],
        "destinations": {
          "03-property-and-record-restoration-nicomedia.side-2.entity-1": "03-property-and-record-restoration-nicomedia.side-2.zone-1",
          "03-property-and-record-restoration-nicomedia.side-2.entity-2": "03-property-and-record-restoration-nicomedia.side-2.zone-2"
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
        "id": "03-property-and-record-restoration-nicomedia.side-2.entity-1",
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
        "id": "03-property-and-record-restoration-nicomedia.side-2.entity-2",
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
        "id": "03-property-and-record-restoration-nicomedia.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "03-property-and-record-restoration-nicomedia.side-2.zone-2",
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
      "onceFlag": "03-property-and-record-restoration-nicomedia.side-2.rewarded",
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
      "north-access",
      "east-access",
      "inland-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A separate ordinary store roof / El tejado separado de un almacén ordinario

EN: Pay 50 wood and restore the damaged store of a separate ordinary store roof to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el tejado separado de un almacén ordinario. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Optional finite repair is identity-disjoint from both main receiving yards; it cannot certify their historical reconstruction.

ES: La reparación opcional finita tiene identidad distinta de ambos patios principales; no certifica reconstrucciones históricas.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "03-property-and-record-restoration-nicomedia.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "03-property-and-record-restoration-nicomedia.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "03-property-and-record-restoration-nicomedia.side-3.payment",
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
        "id": "03-property-and-record-restoration-nicomedia.side-3.entity-1",
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
        "id": "03-property-and-record-restoration-nicomedia.side-3.zone-1",
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
      "onceFlag": "03-property-and-record-restoration-nicomedia.side-3.rewarded",
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
      "north-access",
      "east-access",
      "inland-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### An ordinary inland supply exchange / Un intercambio ordinario interior

EN: Escort the trader of an ordinary inland supply exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de un intercambio ordinario interior hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Finite trade is independent from both main payment receipts and cannot buy ownership or compensation under the letter.

ES: El comercio finito es independiente de ambos recibos principales y no compra propiedad ni indemnizaciones jurídicas.

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
          "03-property-and-record-restoration-nicomedia.side-4.entity-1"
        ],
        "destinations": {
          "03-property-and-record-restoration-nicomedia.side-4.entity-1": "03-property-and-record-restoration-nicomedia.side-4.zone-1"
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
        "receipt": "03-property-and-record-restoration-nicomedia.side-4.payment",
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
        "id": "03-property-and-record-restoration-nicomedia.side-4.entity-1",
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
        "id": "03-property-and-record-restoration-nicomedia.side-4.zone-1",
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
      "onceFlag": "03-property-and-record-restoration-nicomedia.side-4.rewarded",
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
      "north-access",
      "east-access",
      "inland-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Northern yard approaches / Accesos al patio norteño

EN: Scout both marked viewpoints of northern yard approaches. Benefit: Mark the surveyed north-access local land circuit once; every main receiver is disclosed without this task.

ES: Explora los dos miradores señalados de accesos al patio norteño. Ventaja: Señala una vez el circuito terrestre local reconocido north-access; todos los receptores principales se indican sin esta tarea.

EN: Survey the proposed north land access without implying a palace or publication address.

ES: Reconoce el acceso terrestre norte propuesto sin identificar palacio ni dirección de publicación.

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
          "03-property-and-record-restoration-nicomedia.side-5.zone-1",
          "03-property-and-record-restoration-nicomedia.side-5.zone-2"
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
        "id": "03-property-and-record-restoration-nicomedia.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "03-property-and-record-restoration-nicomedia.side-5.zone-2",
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
      "target": "north-access local disclosed circuit",
      "resources": {},
      "onceFlag": "03-property-and-record-restoration-nicomedia.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "north-access"
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
      "north-access",
      "east-access",
      "inland-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The inland receiving-yard link / El enlace interior entre patios receptores

EN: Escort the local guide of the inland receiving-yard link to the marked road junction. Benefit: Mark the surveyed inland-link local land circuit once; every main receiver is disclosed without this task.

ES: Escolta al guía local de el enlace interior entre patios receptores hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local reconocido inland-link; todos los receptores principales se indican sin esta tarea.

EN: Marks the actual proposed land link; no mandatory gulf crossing or invented river.

ES: Señala el enlace terrestre real propuesto; no exige cruzar el golfo ni un río inventado.

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
          "03-property-and-record-restoration-nicomedia.side-6.entity-1"
        ],
        "destinations": {
          "03-property-and-record-restoration-nicomedia.side-6.entity-1": "03-property-and-record-restoration-nicomedia.side-6.zone-1"
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
        "id": "03-property-and-record-restoration-nicomedia.side-6.entity-1",
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
        "id": "03-property-and-record-restoration-nicomedia.side-6.zone-1",
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
      "target": "inland-link local disclosed circuit",
      "resources": {},
      "onceFlag": "03-property-and-record-restoration-nicomedia.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "inland-link"
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
      "north-access",
      "east-access",
      "inland-link"
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
      "id": "survey-and-register",
      "optionalObjectives": [
        "side-1",
        "side-5"
      ],
      "costOfOpportunity": "Check yard access and documentary categories before dispatch, preserving separate receipts.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "split-yard-teams",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Gather in parallel and pay each yard exactly; optional trade never covers mandatory solvency assumptions.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "neighbors-and-inland-link",
      "optionalObjectives": [
        "side-2",
        "side-6"
      ],
      "costOfOpportunity": "Split two neighbors per destination while a separate team handles independent care and route guidance.",
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
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.title / always | none | The Doors Returned | Las puertas restituidas |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.fact-intro / intro first | collection-narrator | Lactantius reports Licinius publishing a letter at Nicomedia on 13 June 313. The transmitted text grants religious choice and orders restoration of Christian communal property, distinguishing communal from individual ownership and allowing indemnity requests. A legal order does not prove every local restoration. Our two receiving yards and their working records are fictional. | Lactancio relata la publicación por Licinio de una carta en Nicomedia el 13 de junio de 313. El texto transmitido concede elección religiosa y ordena restituir bienes comunitarios cristianos; distingue la propiedad comunitaria de la individual y permite solicitar indemnizaciones. Una orden jurídica no prueba todas las restituciones locales. Nuestros dos patios receptores y sus documentos de trabajo son ficticios. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.persona-intro / after handover | imperial-clerk | A door returned: the phrase fits neatly in a register. It says less about what stood behind the door, or who could use it. I inherited this earlier paperwork; I did not see Licinius post the letter. In our smaller fiction I can account for two yards without claiming to account for a province. | Una puerta devuelta: la frase cabe ordenadamente en un registro. Dice menos de lo que había tras la puerta o de quién podía utilizarla. Heredé estos papeles anteriores; no vi a Licinio publicar la carta. En nuestra ficción menor puedo dar cuenta de dos patios sin afirmar que doy cuenta de una provincia. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.route-help / available from start; repeatable without effect | none | Collect four ordinary inventory notes and bring them to the western work yard. Observe both northern/eastern receiving yards controlled and passable, and fund each with its own 60 wood and 20 gold payment. Prepare one working register per yard from collected notes and that yard’s exact receipt. Deliver each register and two assigned original neighbors to its own yard. Access observations cannot be replaced by a timer or mere map visibility. | Recoge cuatro notas ordinarias de inventario y llévalas al patio occidental de trabajo. Observa ambos patios receptores norte/este bajo control y transitables y financia cada uno con su propio pago de 60 de madera y 20 de oro. Prepara un registro por patio a partir de las notas recogidas y del recibo exacto de ese patio. Entrega cada registro y dos vecinos originales asignados en su propio patio. Un temporizador o la mera visibilidad no sustituyen las observaciones de acceso. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o1-goal / phase-1 active | none | Collect four original ordinary inventory notes and deliver all four to the western local inventory yard. | Recoge cuatro notas originales ordinarias de inventario y entrega las cuatro en el patio occidental. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o1-receipt / o1 latched once | none | All four distinct working identities reached the inventory yard. | Las cuatro identidades distintas de trabajo llegaron al patio de inventario. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o1-reaction / after o1 receipt | imperial-clerk | A local list of imagined goods cannot become an imperial property roll by being complete. | Una lista local de bienes imaginados no se convierte en registro imperial de propiedades por estar completa. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o2-goal / phase-2 active | none | Observe both receiving yards controlled and passable; pay each its own 60 wood and 20 gold once. | Observa ambos patios receptores bajo control y transitables; paga a cada uno una vez sus propios 60 de madera y 20 de oro. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o2-receipt / o2 latched once | none | Both separate yards are observed usable and have separate preparation payments. | Ambos patios separados se observan utilizables y tienen pagos separados de preparación. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o2-reaction / after o2 receipt | imperial-clerk | Access and payment are the limits of our small task. Neither certifies historical ownership. | Acceso y pago son los límites de nuestra pequeña tarea. Ninguno certifica propiedades históricas. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o3-goal / phase-3 active | none | Prepare two distinct yard registers, each from the collected notes and its own yard’s exact payment receipt. | Prepara dos registros de patio distintos, cada uno con las notas recogidas y el recibo exacto de su propio patio. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o3-receipt / o3 latched once | none | Each fictional register cites its own funded yard without another debit. | Cada registro ficticio cita su propio patio financiado sin otro cobro. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o3-reaction / after o3 receipt | imperial-clerk | Two registers do not prove two restorations. I will keep those verbs apart. | Dos registros no prueban dos restituciones. Mantendré separados esos verbos. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o4-goal / phase-4 active | none | Deliver each register and its two assigned original neighbors to the matching northern/eastern yard. | Entrega cada registro y sus dos vecinos originales asignados en el patio norteño u oriental correspondiente. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o4-receipt / o4 latched once | none | Both registers and all four assigned neighbors reached their own local yards. | Ambos registros y los cuatro vecinos asignados llegaron a sus patios locales propios. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.o4-reaction / after o4 receipt | imperial-clerk | The people in our fiction reached a yard. The people outside our records deserve more than an automatic conclusion. | Las personas de nuestra ficción llegaron a un patio. Las que quedan fuera de nuestros documentos merecen más que una conclusión automática. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from communal and private property labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de etiquetas de propiedad comunitaria y privada y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-1-complete / side-1 completed | none | Communal and private property labels completed. Its stated benefit has been granted once. | Etiquetas de propiedad comunitaria y privada: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-1-lost / side-1 failed-optional | none | Communal and private property labels is unavailable after the loss of its unique participant or object. The main mission continues. | Etiquetas de propiedad comunitaria y privada: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at independent gulf-side households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes próximos al golfo. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-2-complete / side-2 completed | none | Independent gulf-side households completed. Its stated benefit has been granted once. | Hogares independientes próximos al golfo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-2-lost / side-2 failed-optional | none | Independent gulf-side households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares independientes próximos al golfo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of a separate ordinary store roof to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el tejado separado de un almacén ordinario. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-3-complete / side-3 completed | none | A separate ordinary store roof completed. Its stated benefit has been granted once. | El tejado separado de un almacén ordinario: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-3-lost / side-3 failed-optional | none | A separate ordinary store roof is unavailable after the loss of its unique participant or object. The main mission continues. | El tejado separado de un almacén ordinario: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-4-goal / optional list from start | none | Escort the trader of an ordinary inland supply exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de un intercambio ordinario interior hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-4-complete / side-4 completed | none | An ordinary inland supply exchange completed. Its stated benefit has been granted once. | Un intercambio ordinario interior: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-4-lost / side-4 failed-optional | none | An ordinary inland supply exchange is unavailable after the loss of its unique participant or object. The main mission continues. | Un intercambio ordinario interior: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of northern yard approaches. Benefit: Mark the surveyed north-access local land circuit once; every main receiver is disclosed without this task. | Explora los dos miradores señalados de accesos al patio norteño. Ventaja: Señala una vez el circuito terrestre local reconocido north-access; todos los receptores principales se indican sin esta tarea. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-5-complete / side-5 completed | none | Northern yard approaches completed. Its stated benefit has been granted once. | Accesos al patio norteño: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-5-lost / side-5 failed-optional | none | Northern yard approaches is unavailable after the loss of its unique participant or object. The main mission continues. | Accesos al patio norteño: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the inland receiving-yard link to the marked road junction. Benefit: Mark the surveyed inland-link local land circuit once; every main receiver is disclosed without this task. | Escolta al guía local de el enlace interior entre patios receptores hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local reconocido inland-link; todos los receptores principales se indican sin esta tarea. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-6-complete / side-6 completed | none | The inland receiving-yard link completed. Its stated benefit has been granted once. | El enlace interior entre patios receptores: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.side-6-lost / side-6 failed-optional | none | The inland receiving-yard link is unavailable after the loss of its unique participant or object. The main mission continues. | El enlace interior entre patios receptores: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.fact-outro / victory first | collection-narrator | Two fictional yards were observed as controlled and passable, funded separately and given their own working registers and assigned neighbors. This models local administrative work, not a documented Christian property transfer. The letter’s legal terms remain distinct from their uneven and partly unrecorded implementation. | Dos patios ficticios se observaron bajo control y transitables, se financiaron por separado y recibieron sus propios registros de trabajo y vecinos asignados. Esto representa trabajo administrativo local, no una transferencia documentada de propiedad cristiana. Los términos jurídicos de la carta permanecen distintos de su aplicación desigual y parcialmente no registrada. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.persona-outro / after fact-outro | imperial-clerk | Both columns are filled. I used to think that meant the matter was settled. Here I have written what our imagined workers did, and left the larger order on another sheet. The ink can bear the separation. | Ambas columnas están llenas. Antes creía que eso significaba asunto resuelto. Aquí he escrito lo que hicieron nuestros trabajadores imaginados y he dejado la orden mayor en otra hoja. La tinta puede soportar la separación. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.03-property-and-record-restoration-nicomedia.odyssey.next-episode / after persona-outro | none | Continue with The African Petition. This episode does not complete the campaign. | Continúa con La petición africana. Este episodio no termina la campaña. |

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
      "id": "controlled-and-passable-yard-observation",
      "status": "reference area-state exists; native control and path/footprint observations pending"
    }
  ],
  "artDirection": {
    "style": "sober Bithynian coastal hinterland; local work yards north of gulf",
    "historicalControls": "no proven restored church, palace interior or modernindustrialcoast",
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "one usable receiving yard cannot satisfy both",
      "visibility or a timer cannot substitute for controlled/passable observation",
      "northern receipt cannot generate eastern register",
      "each register requires its exact receipt and same four collected input identities",
      "two northern neighbors cannot satisfy eastern neighbors",
      "no property deed, actual restituted church or exactpublicationaddress invented",
      "Marcus cannot be a313eyewitness",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
