# 18. The Court without Its Emperor

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `18-administrative-transition-nicomedia` · 22 May 337 CE · 400×400

## Historical frame and fixed outcome

EN: Constantine died in 337, conventionally dated 22May. Eusebius places his final baptism in Nicomedia’s suburbs and death at Pentecost, without naming the baptizer. Jerome later names Eusebius of Nicomedia. The exact residence is uncertain. After that news, our fictional local clerks arrange ordinary work handoffs. Resources neither buy the baptism nor avert the emperor’s death.

ES: Constantino murió en 337, convencionalmente el 22de mayo. Eusebio sitúa su último bautismo en los alrededores de Nicomedia y su muerte en Pentecostés, sin nombrar oficiante. Jerónimo nombra después a Eusebio de Nicomedia. La residencia exacta es incierta. Tras esa noticia, nuestros escribientes locales ficticios preparan traspasos ordinarios. Los recursos no compran bautismo ni evitan la muerte del emperador.

EN: Four fictional clerks completed their paid local assignments and causal handoffs. Their two records do not reproduce Constantine’s will, his baptism or a royal burial convoy. Eusebius reports the body’s transfer to Constantinople; it remains off-map. The following episode concerns succession and the 337 killings, whose responsibility is disputed in the sources.

ES: Cuatro escribientes ficticios completaron asignaciones locales financiadas y traspasos causales. Sus dos registros no reproducen testamento de Constantino, bautismo ni cortejo funerario real. Eusebio refiere el traslado del cuerpo a Constantinopla; queda fuera del mapa. El siguiente episodio trata de la sucesión y las matanzas de 337, cuya responsabilidad se discute en las fuentes.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "consultedUrl": "https://www.newadvent.org/fathers/25024.htm",
      "passage": "Eusebius VC IV.61–64 checked for baptism and death at Nicomedia.",
      "limitations": "The narrative is an imperial Christian encomium; day 22 May is not independently verified by the passage checked.",
      "status": "consulted",
      "supportedClaim": "Supports Constantine’s baptism by Eusebius of Nicomedia and death at Nicomedia in 337 in Eusebius’ account. / Respalda el bautismo por Eusebio de Nicomedia y la muerte de Constantino en Nicomedia en 337 según Eusebio.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "VC IV.61–64 checked.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/25024.htm",
      "passage": "VCIV61–66",
      "coverageActuallyRead": "Architect directly read complete displayed span61–66 via ordinary HTML retrieval after browser timeout.",
      "limitations": "Christian imperial encomium; reconstructed speeches not stenography. Nicomedia suburbs and Pentecost named, no exact22May numeral, officiating bishop name or Achyron villa in this span. Body transfer to Constantinople off-map, itinerary not supplied.",
      "consultationDate": "2026-10-14",
      "approval": "independent review pending"
    },
    {
      "consultedUrl": "https://www.tertullian.org/fathers/jerome_chronicle_03_part2.htm",
      "passage": "Chronicle annal337 baptism note and nearby death notice",
      "coverageActuallyRead": "Architect directly read the translated baptism annal and surrounding entries; not entire chronicle.",
      "limitations": "Late-fourth-century chronicle names EusebiusNic and appends doctrinal blame. Nearby death notice lies in a confusing year-column sequence and readsAncyra nearNicomedia; no corrected precise villa coordinate is inferred. Not eyewitness diary.",
      "consultationDate": "2026-10-14",
      "approval": "independent review pending"
    },
    {
      "consultedUrl": "https://bmcr.brynmawr.edu/2006/2006.04.03/",
      "passage": "JanDrijvers2006 review of MarilenaAmerise2005, selected source survey",
      "coverageActuallyRead": "Architect read full displayed short review; Amerise monograph itself not accessed.",
      "limitations": "Corrects initial delegated authorHansPohlsander. Review prints377 in illness sentence, a typo excluded from chronology; its22May337 date is conventional. Achyron probable, not recovered game building. No deliberate omission motive treated as established.",
      "consultationDate": "2026-10-14",
      "approval": "independent review pending"
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

EN: Register both distinct local work ledgers and all four original clerks, two for households and two for service work. These are ordinary fictional lists, never an imperial testament.

ES: Registra los dos libros locales distintos de trabajo y los cuatro escribientes originales, dos de hogares y dos de servicio. Son listas ficticias ordinarias, nunca un testamento imperial.

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
        "imperial-church.18-administrative-transition-nicomedia.household-work-ledger-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-work-ledger-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-4",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-2"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both work chains and four original clerks are registered separately.

ES: Ambas cadenas de trabajo y cuatro escribientes originales quedan registrados separados.

EN: A household list is not a sovereign’s will.

ES: Una lista de hogares no es el testamento de un soberano.

### o2 / phase-2

EN: Send the household ledger and its two clerks south, the service ledger and its two clerks northeast. Pay 120 food/60 wood south and 100 food/40 wood northeast once. Both exact receiving shares are mandatory.

ES: Envía el libro de hogares y sus dos escribientes al sur, el de servicio y sus dos escribientes al nordeste. Paga una vez 120 alimento/60 madera al sur y 100 alimento/40 madera al nordeste. Ambas partes receptoras exactas son obligatorias.

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
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-2"
      ],
      "destinations": {
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-1": "imperial-church.18-administrative-transition-nicomedia.destination-3",
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-2": "imperial-church.18-administrative-transition-nicomedia.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.household-work-ledger-1"
      ],
      "destinations": {
        "imperial-church.18-administrative-transition-nicomedia.household-work-ledger-1": "imperial-church.18-administrative-transition-nicomedia.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-2"
      ],
      "destinations": {
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-1": "imperial-church.18-administrative-transition-nicomedia.destination-4",
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-2": "imperial-church.18-administrative-transition-nicomedia.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-work-ledger-1"
      ],
      "destinations": {
        "imperial-church.18-administrative-transition-nicomedia.service-work-ledger-1": "imperial-church.18-administrative-transition-nicomedia.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 220,
        "wood": 100
      },
      "id": "req-5",
      "receivingZones": [
        "imperial-church.18-administrative-transition-nicomedia.destination-3",
        "imperial-church.18-administrative-transition-nicomedia.destination-4"
      ],
      "allocations": {
        "imperial-church.18-administrative-transition-nicomedia.destination-3": {
          "food": 120,
          "wood": 60
        },
        "imperial-church.18-administrative-transition-nicomedia.destination-4": {
          "food": 100,
          "wood": 40
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.18-administrative-transition-nicomedia.o2.req-5.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both original work chains reached their receivers and exact budgets were paid once.

ES: Ambas cadenas originales llegaron a sus receptores y se pagaron una vez los presupuestos exactos.

EN: Different duties need different shares.

ES: Tareas diferentes necesitan partes diferentes.

### o3 / phase-3

EN: After both work courts have received their assigned teams and budgets, prepare a household handoff from its own ledger and a service handoff from its own ledger. Collect both notices. Their work is covered by the receiving payment; do not pay it again.

ES: Una vez que ambos patios de trabajo reciban sus equipos y presupuestos asignados, prepara un traspaso de hogares de su propio libro y un traspaso de servicio de su propio libro. Recoge los dos avisos. Su trabajo lo cubre el pago receptor; no lo pagues otra vez.

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
        "imperial-church.18-administrative-transition-nicomedia.household-work-ledger-1"
      ],
      "outputEntities": [
        "imperial-church.18-administrative-transition-nicomedia.household-handoff-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.18-administrative-transition-nicomedia.o2.req-5.paid",
          "fromObjective": "o2",
          "amounts": {
            "food": 220,
            "wood": 100
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
        "imperial-church.18-administrative-transition-nicomedia.service-work-ledger-1"
      ],
      "outputEntities": [
        "imperial-church.18-administrative-transition-nicomedia.service-handoff-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.18-administrative-transition-nicomedia.o2.req-5.paid",
          "fromObjective": "o2",
          "amounts": {
            "food": 220,
            "wood": 100
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.household-handoff-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-4",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-handoff-1"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The household and service handoffs are recorded separately, with no repeated receiving charge.

ES: Los traspasos de hogares y servicio quedan registrados separados, sin repetir el cobro receptor.

EN: Do not carry one duty’s title over another.

ES: No pases el título de una tarea a otra.

### o4 / phase-4

EN: After this phase begins, observe each original clerk leave their own received work court and bring all four to personnel accounts. Deliver the household handoff to accounts and the service handoff to the eastern local relay. The original ledgers stay at their work courts.

ES: Al comenzar esta fase, observa cada escribiente original salir de su propio patio de trabajo recibido y lleva los cuatro a cuentas de personal. Entrega el traspaso de hogares a cuentas y el de servicio al relevo oriental local. Los libros originales quedan en sus patios de trabajo.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "ordered-departure",
      "receiptObjective": "o2",
      "receiptRequirement": "req-1",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-1",
      "departingEntities": [
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-2"
      ]
    },
    {
      "kind": "ordered-departure",
      "receiptObjective": "o2",
      "receiptRequirement": "req-3",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-2",
      "departingEntities": [
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-2"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-1"
      },
      "id": "req-3",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-2"
      ],
      "destinations": {
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-1": "imperial-church.18-administrative-transition-nicomedia.destination-5",
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-2": "imperial-church.18-administrative-transition-nicomedia.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-2"
      },
      "id": "req-4",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-2"
      ],
      "destinations": {
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-1": "imperial-church.18-administrative-transition-nicomedia.destination-5",
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-2": "imperial-church.18-administrative-transition-nicomedia.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-5",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.household-handoff-1"
      ],
      "destinations": {
        "imperial-church.18-administrative-transition-nicomedia.household-handoff-1": "imperial-church.18-administrative-transition-nicomedia.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-6",
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-handoff-1"
      ],
      "destinations": {
        "imperial-church.18-administrative-transition-nicomedia.service-handoff-1": "imperial-church.18-administrative-transition-nicomedia.destination-6"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Four exact clerk identities returned causally and two distinct handoffs reached their designated destinations.

ES: Cuatro identidades exactas de escribientes volvieron causalmente y dos traspasos distintos llegaron a sus destinos designados.

EN: The work continues in smaller names.

ES: El trabajo continúa con nombres más pequeños.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/18-administrative-transition-nicomedia.svg)

```json
{
  "bbox": [
    29.915,
    40.767,
    29.99,
    40.812
  ],
  "terrainProfile": "nicomedia",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        59.37,
        215.18
      ],
      "lonLat": [
        29.923,
        40.787
      ],
      "name": {
        "en": "Fictional western household-work origin",
        "es-ES": "Origen ficticio occidental de trabajo doméstico"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        163.87,
        114.8
      ],
      "lonLat": [
        29.945,
        40.803
      ],
      "name": {
        "en": "Fictional northern service-work origin",
        "es-ES": "Origen ficticio septentrional de trabajo de servicio"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        173.37,
        290.47
      ],
      "lonLat": [
        29.947,
        40.775
      ],
      "name": {
        "en": "Fictional southern household receiver",
        "es-ES": "Receptor ficticio meridional de hogares"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        320.63,
        139.9
      ],
      "lonLat": [
        29.978,
        40.799
      ],
      "name": {
        "en": "Fictional northeast service receiver",
        "es-ES": "Receptor ficticio nordeste de servicio"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        216.12,
        208.91
      ],
      "lonLat": [
        29.956,
        40.788
      ],
      "name": {
        "en": "Fictional central personnel-account court",
        "es-ES": "Patio ficticio central de cuentas de personal"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-6",
      "centre": [
        311.12,
        271.65
      ],
      "lonLat": [
        29.976,
        40.778
      ],
      "name": {
        "en": "Fictional eastern local outgoing relay",
        "es-ES": "Relevo ficticio oriental local de salida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "household-work-handoff",
      "hubOrder": [
        "hub-1",
        "hub-3",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "service-work-handoff",
      "hubOrder": [
        "hub-2",
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "local-outgoing-relay",
      "hubOrder": [
        "hub-5",
        "hub-6"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "central-household-alternative",
      "hubOrder": [
        "hub-1",
        "hub-5",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "central-service-alternative",
      "hubOrder": [
        "hub-2",
        "hub-5",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 8
    }
  ],
  "terrainInstructions": "Inland local Nicomedia north of the gulf head, ordinary work gardens and hillside approaches. Every court is fiction after the death news, not an imperial estate, bath, baptism church or certified337 villa. Helenopolis, Constantinople and royal body transport remain off-map; no compressed teleport or player-led coffin convoy. Courts and routes need actual ancient shore, streams, grades and dated road controls. Regional modern locator is research only, and absence of a coast trace cannot certify land. Do not project industrial shoreline/reclamation, Ottoman fabric, modern freeway or358 earthquake destruction into337.",
  "corridorStraightLengthsTiles": {
    "household-work-handoff": 228.7,
    "service-work-handoff": 284.0,
    "local-outgoing-relay": 113.85,
    "central-household-alternative": 248.96,
    "central-service-alternative": 232.88
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
  "asset": "docs/design/maps/imperial-church/odyssey/18-administrative-transition-nicomedia.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.18-administrative-transition-nicomedia.household-work-ledger-1",
      "role": "fictional-local-household-ledger",
      "initialHub": "hub-1",
      "offsetTiles": [
        -18,
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
      "id": "imperial-church.18-administrative-transition-nicomedia.service-work-ledger-1",
      "role": "fictional-local-service-ledger",
      "initialHub": "hub-2",
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
      "id": "imperial-church.18-administrative-transition-nicomedia.household-clerks-1",
      "role": "fictional-local-work-clerk",
      "initialHub": "hub-1",
      "offsetTiles": [
        6,
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
      "id": "imperial-church.18-administrative-transition-nicomedia.household-clerks-2",
      "role": "fictional-local-work-clerk",
      "initialHub": "hub-1",
      "offsetTiles": [
        8,
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
      "id": "imperial-church.18-administrative-transition-nicomedia.service-clerks-1",
      "role": "fictional-local-work-clerk",
      "initialHub": "hub-2",
      "offsetTiles": [
        18,
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
      "id": "imperial-church.18-administrative-transition-nicomedia.service-clerks-2",
      "role": "fictional-local-work-clerk",
      "initialHub": "hub-2",
      "offsetTiles": [
        20,
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
      "id": "imperial-church.18-administrative-transition-nicomedia.household-handoff-1",
      "role": "fictional-local-handoff-note",
      "initialHub": "hub-3",
      "offsetTiles": [
        -18,
        20
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
      "id": "imperial-church.18-administrative-transition-nicomedia.service-handoff-1",
      "role": "fictional-local-handoff-note",
      "initialHub": "hub-4",
      "offsetTiles": [
        -6,
        20
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
      "id": "imperial-church.18-administrative-transition-nicomedia.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.18-administrative-transition-nicomedia.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.18-administrative-transition-nicomedia.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.18-administrative-transition-nicomedia.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.18-administrative-transition-nicomedia.destination-5",
      "hub": "hub-5",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.18-administrative-transition-nicomedia.destination-6",
      "hub": "hub-6",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    }
  ],
  "objectGroups": {
    "household-work-ledger": [
      "imperial-church.18-administrative-transition-nicomedia.household-work-ledger-1"
    ],
    "service-work-ledger": [
      "imperial-church.18-administrative-transition-nicomedia.service-work-ledger-1"
    ],
    "household-clerks": [
      "imperial-church.18-administrative-transition-nicomedia.household-clerks-1",
      "imperial-church.18-administrative-transition-nicomedia.household-clerks-2"
    ],
    "service-clerks": [
      "imperial-church.18-administrative-transition-nicomedia.service-clerks-1",
      "imperial-church.18-administrative-transition-nicomedia.service-clerks-2"
    ],
    "household-handoff": [
      "imperial-church.18-administrative-transition-nicomedia.household-handoff-1"
    ],
    "service-handoff": [
      "imperial-church.18-administrative-transition-nicomedia.service-handoff-1"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.household-work-ledger-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    },
    {
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-work-ledger-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    },
    {
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.household-clerks-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    },
    {
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-1",
        "imperial-church.18-administrative-transition-nicomedia.service-clerks-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    },
    {
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.household-handoff-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    },
    {
      "entities": [
        "imperial-church.18-administrative-transition-nicomedia.service-handoff-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Inland work approaches / Accesos interiores de trabajo

EN: Scout both marked viewpoints of inland work approaches. Benefit: Mark the proposed central-service-alternative once; required destinations remain disclosed even if this optional task is skipped.

ES: Explora los dos miradores señalados de accesos interiores de trabajo. Ventaja: Señala una vez central-service-alternative propuesto; los destinos obligatorios siguen indicados aunque se omita este secundario.

EN: Two ordinary observations mark land circuits, not the imperial deathbed or burial route.

ES: Dos observaciones ordinarias señalan circuitos terrestres, no lecho imperial ni ruta funeraria.

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
          "18-administrative-transition-nicomedia.side-1.zone-1",
          "18-administrative-transition-nicomedia.side-1.zone-2"
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
        "id": "18-administrative-transition-nicomedia.side-1.zone-1",
        "hub": "hub-3",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "18-administrative-transition-nicomedia.side-1.zone-2",
        "hub": "hub-4",
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
      "target": "central-service-alternative",
      "resources": {},
      "onceFlag": "18-administrative-transition-nicomedia.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "central-service-alternative"
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
      "household-work-handoff",
      "service-work-handoff",
      "local-outgoing-relay",
      "central-household-alternative",
      "central-service-alternative"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Separate duties annotation / Anotación de tareas separadas

EN: Recover both separate copies from separate duties annotation and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de anotación de tareas separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: One local copy preserves household/service distinctions and never replaces either original ledger.

ES: Una copia local conserva la distinción hogares/servicio y nunca sustituye libros originales.

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
          "18-administrative-transition-nicomedia.side-2.entity-1",
          "18-administrative-transition-nicomedia.side-2.entity-2"
        ],
        "destinations": {
          "18-administrative-transition-nicomedia.side-2.entity-1": "18-administrative-transition-nicomedia.side-2.zone-1",
          "18-administrative-transition-nicomedia.side-2.entity-2": "18-administrative-transition-nicomedia.side-2.zone-1"
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
        "id": "18-administrative-transition-nicomedia.side-2.entity-1",
        "role": "copy",
        "initialHub": "hub-5",
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
        "id": "18-administrative-transition-nicomedia.side-2.entity-2",
        "role": "copy",
        "initialHub": "hub-5",
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
        "id": "18-administrative-transition-nicomedia.side-2.zone-1",
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
      "onceFlag": "18-administrative-transition-nicomedia.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.18-administrative-transition-nicomedia"
      ],
      "historicalNote": {
        "en": "Constantine died in 337, conventionally dated 22May. Eusebius places his final baptism in Nicomedia’s suburbs and death at Pentecost, without naming the baptizer. Jerome later names Eusebius of Nicomedia. The exact residence is uncertain. After that news, our fictional local clerks arrange ordinary work handoffs. Resources neither buy the baptism nor avert the emperor’s death.",
        "es-ES": "Constantino murió en 337, convencionalmente el 22de mayo. Eusebio sitúa su último bautismo en los alrededores de Nicomedia y su muerte en Pentecostés, sin nombrar oficiante. Jerónimo nombra después a Eusebio de Nicomedia. La residencia exacta es incierta. Tras esa noticia, nuestros escribientes locales ficticios preparan traspasos ordinarios. Los recursos no compran bautismo ni evitan la muerte del emperador."
      },
      "hint": {
        "en": "Register both distinct local work ledgers and all four original clerks, two for households and two for service work. These are ordinary fictional lists, never an imperial testament.",
        "es-ES": "Registra los dos libros locales distintos de trabajo y los cuatro escribientes originales, dos de hogares y dos de servicio. Son listas ficticias ordinarias, nunca un testamento imperial."
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
    "originHub": "hub-5",
    "receivingHub": "hub-1",
    "corridorIds": [
      "household-work-handoff",
      "service-work-handoff",
      "local-outgoing-relay",
      "central-household-alternative",
      "central-service-alternative"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Work-yard households / Hogares de los patios de trabajo

EN: Bring each of the two aid crates to its assigned household at work-yard households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de los patios de trabajo. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Voluntary finite help supports ordinary people after news, not a sacrament or imperial recovery.

ES: Ayuda voluntaria finita apoya personas ordinarias tras la noticia, no sacramento ni recuperación imperial.

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
          "18-administrative-transition-nicomedia.side-3.entity-1",
          "18-administrative-transition-nicomedia.side-3.entity-2"
        ],
        "destinations": {
          "18-administrative-transition-nicomedia.side-3.entity-1": "18-administrative-transition-nicomedia.side-3.zone-1",
          "18-administrative-transition-nicomedia.side-3.entity-2": "18-administrative-transition-nicomedia.side-3.zone-2"
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
        "id": "18-administrative-transition-nicomedia.side-3.entity-1",
        "role": "aid",
        "initialHub": "hub-2",
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
        "id": "18-administrative-transition-nicomedia.side-3.entity-2",
        "role": "aid",
        "initialHub": "hub-2",
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
        "id": "18-administrative-transition-nicomedia.side-3.zone-1",
        "hub": "hub-3",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "18-administrative-transition-nicomedia.side-3.zone-2",
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
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 100,
        "wood": 50
      },
      "onceFlag": "18-administrative-transition-nicomedia.side-3.rewarded",
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
    "receivingHub": "hub-3",
    "corridorIds": [
      "household-work-handoff",
      "service-work-handoff",
      "local-outgoing-relay",
      "central-household-alternative",
      "central-service-alternative"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Account shelter tools / Herramientas del refugio de cuentas

EN: Pay 50 wood and restore the damaged store of account shelter tools to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de herramientas del refugio de cuentas. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A bounded ordinary repair frees stock for labor, without opening a royal crypt or curing a ruler.

ES: Una reparación ordinaria limitada libera existencias para trabajo, sin abrir cripta real ni curar gobernante.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "18-administrative-transition-nicomedia.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "18-administrative-transition-nicomedia.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "18-administrative-transition-nicomedia.side-4.payment",
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
        "id": "18-administrative-transition-nicomedia.side-4.entity-1",
        "role": "repair",
        "initialHub": "hub-5",
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
        "id": "18-administrative-transition-nicomedia.side-4.zone-1",
        "hub": "hub-6",
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
      "onceFlag": "18-administrative-transition-nicomedia.side-4.rewarded",
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
    "originHub": "hub-5",
    "receivingHub": "hub-6",
    "corridorIds": [
      "household-work-handoff",
      "service-work-handoff",
      "local-outgoing-relay",
      "central-household-alternative",
      "central-service-alternative"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Handoff work provisions / Provisiones de trabajo de traspaso

EN: Escort the trader of handoff work provisions to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de provisiones de trabajo de traspaso hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One finite procurement supports the local personnel circuit, not funeral tribute or succession purchase.

ES: Una compra finita apoya el circuito local de personal, no tributo funerario ni compra de sucesión.

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
          "18-administrative-transition-nicomedia.side-5.entity-1"
        ],
        "destinations": {
          "18-administrative-transition-nicomedia.side-5.entity-1": "18-administrative-transition-nicomedia.side-5.zone-1"
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
        "receipt": "18-administrative-transition-nicomedia.side-5.payment",
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
        "id": "18-administrative-transition-nicomedia.side-5.entity-1",
        "role": "trade",
        "initialHub": "hub-4",
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
        "id": "18-administrative-transition-nicomedia.side-5.zone-1",
        "hub": "hub-5",
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
      "onceFlag": "18-administrative-transition-nicomedia.side-5.rewarded",
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
    "originHub": "hub-4",
    "receivingHub": "hub-5",
    "corridorIds": [
      "household-work-handoff",
      "service-work-handoff",
      "local-outgoing-relay",
      "central-household-alternative",
      "central-service-alternative"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Central account guide / Guía central de cuentas

EN: Escort the local guide of central account guide to the marked road junction. Benefit: Mark the proposed central-household-alternative once; required destinations remain disclosed even if this optional task is skipped.

ES: Escolta al guía local de guía central de cuentas hasta el cruce señalado. Ventaja: Señala una vez central-household-alternative propuesto; los destinos obligatorios siguen indicados aunque se omita este secundario.

EN: Marks a local inland alternative, never a shortened Nicomedia–Constantinople journey.

ES: Señala alternativa interior local, nunca un viaje Nicomedia–Constantinopla abreviado.

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
          "18-administrative-transition-nicomedia.side-6.entity-1"
        ],
        "destinations": {
          "18-administrative-transition-nicomedia.side-6.entity-1": "18-administrative-transition-nicomedia.side-6.zone-1"
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
        "id": "18-administrative-transition-nicomedia.side-6.entity-1",
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
        "id": "18-administrative-transition-nicomedia.side-6.zone-1",
        "hub": "hub-5",
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
      "target": "central-household-alternative",
      "resources": {},
      "onceFlag": "18-administrative-transition-nicomedia.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "central-household-alternative"
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
    "receivingHub": "hub-5",
    "corridorIds": [
      "household-work-handoff",
      "service-work-handoff",
      "local-outgoing-relay",
      "central-household-alternative",
      "central-service-alternative"
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
      "id": "parallel-work-teams",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Run two original two-clerk teams and use the central inland alternatives; preserve both separate budgets.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "accounts-and-tools",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Annotate duties and fund finite tool stock while reserving220 food/100 wood for receiving work.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "household-provisions",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Support optional households and ordinary finite procurement before converging personnel at accounts.",
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
      "food": 229,
      "wood": 97,
      "gold": 74,
      "stone": 40
    },
    "gatherableBank": {
      "food": 1461,
      "wood": 853,
      "gold": 186,
      "stone": 120
    },
    "mandatoryDeliveries": {
      "food": 220,
      "wood": 100,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 250,
      "wood": 170,
      "gold": 70,
      "stone": 60
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
      "food": 1240,
      "wood": 750,
      "gold": 260,
      "stone": 160
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
      "food": 200,
      "wood": 85,
      "gold": 65,
      "stone": 35
    },
    "gatherableBank": {
      "food": 1490,
      "wood": 865,
      "gold": 195,
      "stone": 125
    },
    "mandatoryDeliveries": {
      "food": 220,
      "wood": 100,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 250,
      "wood": 170,
      "gold": 70,
      "stone": 60
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
      "food": 1240,
      "wood": 750,
      "gold": 260,
      "stone": 160
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
      "food": 170,
      "wood": 72,
      "gold": 55,
      "stone": 29
    },
    "gatherableBank": {
      "food": 1520,
      "wood": 878,
      "gold": 205,
      "stone": 131
    },
    "mandatoryDeliveries": {
      "food": 220,
      "wood": 100,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 250,
      "wood": 170,
      "gold": 70,
      "stone": 60
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
      "food": 1240,
      "wood": 750,
      "gold": 260,
      "stone": 160
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
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.title / always | none | The Court without Its Emperor | La corte sin su emperador |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.fact-intro / intro first | collection-narrator | Constantine died in 337, conventionally dated 22May. Eusebius places his final baptism in Nicomedia’s suburbs and death at Pentecost, without naming the baptizer. Jerome later names Eusebius of Nicomedia. The exact residence is uncertain. After that news, our fictional local clerks arrange ordinary work handoffs. Resources neither buy the baptism nor avert the emperor’s death. | Constantino murió en 337, convencionalmente el 22de mayo. Eusebio sitúa su último bautismo en los alrededores de Nicomedia y su muerte en Pentecostés, sin nombrar oficiante. Jerónimo nombra después a Eusebio de Nicomedia. La residencia exacta es incierta. Tras esa noticia, nuestros escribientes locales ficticios preparan traspasos ordinarios. Los recursos no compran bautismo ni evitan la muerte del emperador. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.persona-intro / after handover | imperial-clerk | There is no deathbed in my memory that I can honestly call the emperor’s. Father’s lists have quieter names: the people who kept the work moving after the news. Two courtyards needed hands, and somebody had to say which duties were still waiting. A court can lose its master before a household loses its need for bread. | No hay lecho de muerte en mi memoria que pueda llamar honradamente el del emperador. Las listas de mi padre tienen nombres más callados: quienes mantuvieron el trabajo tras la noticia. Dos patios necesitaban manos y alguien debía decir qué tareas seguían esperando. Una corte puede perder a su señor antes de que un hogar deje de necesitar pan. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.route-help / available from start; repeatable without effect | none | Keep the household ledger and its two clerks together at the southern work court; send the service ledger and its two clerks northeast. Fund 120 food/60 wood south and 100 food/40 wood northeast once. Prepare each handoff from its own ledger after funding both courts. During the return task, each original clerk must actually leave their assigned court before going to personnel accounts. Send the household handoff to accounts and the service handoff to the eastern local relay. The two original ledgers remain at their work courts. The emperor’s death and baptism are historical context; neither depends on these payments. | Mantén el libro de hogares y sus dos escribientes en el patio de trabajo sur; envía el de servicio y sus dos escribientes al nordeste. Financia una vez 120 alimento/60 madera al sur y 100 alimento/40 madera al nordeste. Prepara cada traspaso de su propio libro tras financiar ambos patios. Durante la tarea de regreso, cada escribiente original debe salir realmente de su patio asignado antes de ir a cuentas de personal. Envía el traspaso de hogares a cuentas y el de servicio al relevo oriental local. Los dos libros originales quedan en sus patios de trabajo. Muerte y bautismo del emperador son contexto histórico; no dependen de estos pagos. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o1-goal / phase-1 active | none | Register both distinct local work ledgers and all four original clerks, two for households and two for service work. These are ordinary fictional lists, never an imperial testament. | Registra los dos libros locales distintos de trabajo y los cuatro escribientes originales, dos de hogares y dos de servicio. Son listas ficticias ordinarias, nunca un testamento imperial. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o1-receipt / o1 latched once | none | Both work chains and four original clerks are registered separately. | Ambas cadenas de trabajo y cuatro escribientes originales quedan registrados separados. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o1-reaction / after o1 receipt | imperial-clerk | A household list is not a sovereign’s will. | Una lista de hogares no es el testamento de un soberano. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o2-goal / phase-2 active | none | Send the household ledger and its two clerks south, the service ledger and its two clerks northeast. Pay 120 food/60 wood south and 100 food/40 wood northeast once. Both exact receiving shares are mandatory. | Envía el libro de hogares y sus dos escribientes al sur, el de servicio y sus dos escribientes al nordeste. Paga una vez 120 alimento/60 madera al sur y 100 alimento/40 madera al nordeste. Ambas partes receptoras exactas son obligatorias. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o2-receipt / o2 latched once | none | Both original work chains reached their receivers and exact budgets were paid once. | Ambas cadenas originales llegaron a sus receptores y se pagaron una vez los presupuestos exactos. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o2-reaction / after o2 receipt | imperial-clerk | Different duties need different shares. | Tareas diferentes necesitan partes diferentes. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o3-goal / phase-3 active | none | After both work courts have received their assigned teams and budgets, prepare a household handoff from its own ledger and a service handoff from its own ledger. Collect both notices. Their work is covered by the receiving payment; do not pay it again. | Una vez que ambos patios de trabajo reciban sus equipos y presupuestos asignados, prepara un traspaso de hogares de su propio libro y un traspaso de servicio de su propio libro. Recoge los dos avisos. Su trabajo lo cubre el pago receptor; no lo pagues otra vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o3-receipt / o3 latched once | none | The household and service handoffs are recorded separately, with no repeated receiving charge. | Los traspasos de hogares y servicio quedan registrados separados, sin repetir el cobro receptor. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o3-reaction / after o3 receipt | imperial-clerk | Do not carry one duty’s title over another. | No pases el título de una tarea a otra. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o4-goal / phase-4 active | none | After this phase begins, observe each original clerk leave their own received work court and bring all four to personnel accounts. Deliver the household handoff to accounts and the service handoff to the eastern local relay. The original ledgers stay at their work courts. | Al comenzar esta fase, observa cada escribiente original salir de su propio patio de trabajo recibido y lleva los cuatro a cuentas de personal. Entrega el traspaso de hogares a cuentas y el de servicio al relevo oriental local. Los libros originales quedan en sus patios de trabajo. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o4-receipt / o4 latched once | none | Four exact clerk identities returned causally and two distinct handoffs reached their designated destinations. | Cuatro identidades exactas de escribientes volvieron causalmente y dos traspasos distintos llegaron a sus destinos designados. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.o4-reaction / after o4 receipt | imperial-clerk | The work continues in smaller names. | El trabajo continúa con nombres más pequeños. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of inland work approaches. Benefit: Mark the proposed central-service-alternative once; required destinations remain disclosed even if this optional task is skipped. | Explora los dos miradores señalados de accesos interiores de trabajo. Ventaja: Señala una vez central-service-alternative propuesto; los destinos obligatorios siguen indicados aunque se omita este secundario. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-1-complete / side-1 completed | none | Inland work approaches completed. Its stated benefit has been granted once. | Accesos interiores de trabajo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-1-lost / side-1 failed-optional | none | Inland work approaches is unavailable after the loss of its unique participant or object. The main mission continues. | Accesos interiores de trabajo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from separate duties annotation and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de anotación de tareas separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-2-complete / side-2 completed | none | Separate duties annotation completed. Its stated benefit has been granted once. | Anotación de tareas separadas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-2-lost / side-2 failed-optional | none | Separate duties annotation is unavailable after the loss of its unique participant or object. The main mission continues. | Anotación de tareas separadas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at work-yard households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de los patios de trabajo. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-3-complete / side-3 completed | none | Work-yard households completed. Its stated benefit has been granted once. | Hogares de los patios de trabajo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-3-lost / side-3 failed-optional | none | Work-yard households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares de los patios de trabajo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of account shelter tools to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de herramientas del refugio de cuentas. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-4-complete / side-4 completed | none | Account shelter tools completed. Its stated benefit has been granted once. | Herramientas del refugio de cuentas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-4-lost / side-4 failed-optional | none | Account shelter tools is unavailable after the loss of its unique participant or object. The main mission continues. | Herramientas del refugio de cuentas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-5-goal / optional list from start | none | Escort the trader of handoff work provisions to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de provisiones de trabajo de traspaso hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-5-complete / side-5 completed | none | Handoff work provisions completed. Its stated benefit has been granted once. | Provisiones de trabajo de traspaso: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-5-lost / side-5 failed-optional | none | Handoff work provisions is unavailable after the loss of its unique participant or object. The main mission continues. | Provisiones de trabajo de traspaso: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-6-goal / optional list from start | none | Escort the local guide of central account guide to the marked road junction. Benefit: Mark the proposed central-household-alternative once; required destinations remain disclosed even if this optional task is skipped. | Escolta al guía local de guía central de cuentas hasta el cruce señalado. Ventaja: Señala una vez central-household-alternative propuesto; los destinos obligatorios siguen indicados aunque se omita este secundario. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-6-complete / side-6 completed | none | Central account guide completed. Its stated benefit has been granted once. | Guía central de cuentas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.side-6-lost / side-6 failed-optional | none | Central account guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía central de cuentas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.fact-outro / victory first | collection-narrator | Four fictional clerks completed their paid local assignments and causal handoffs. Their two records do not reproduce Constantine’s will, his baptism or a royal burial convoy. Eusebius reports the body’s transfer to Constantinople; it remains off-map. The following episode concerns succession and the 337 killings, whose responsibility is disputed in the sources. | Cuatro escribientes ficticios completaron asignaciones locales financiadas y traspasos causales. Sus dos registros no reproducen testamento de Constantino, bautismo ni cortejo funerario real. Eusebio refiere el traslado del cuerpo a Constantinopla; queda fuera del mapa. El siguiente episodio trata de la sucesión y las matanzas de 337, cuya responsabilidad se discute en las fuentes. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.persona-outro / after fact-outro | imperial-clerk | The two ledgers stayed where the work was done. Four clerks came back to accounts, and two handoff notices went to different tables. The emperor’s name did not make those ordinary lines complete themselves. The next bundle has more seals and less certainty. I will keep the households’ names where I can still read them. | Los dos libros quedaron donde se hizo el trabajo. Cuatro escribientes volvieron a cuentas y dos avisos de traspaso fueron a mesas distintas. El nombre del emperador no completó por sí solo esas líneas ordinarias. El siguiente legajo tiene más sellos y menos certeza. Conservaré los nombres de los hogares donde pueda seguir leyéndolos. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.18-administrative-transition-nicomedia.odyssey.next-episode / after persona-outro | none | Continue with Three Seals, One Inheritance. This episode does not complete the campaign. | Continúa con Tres sellos, una herencia. Este episodio no termina la campaña. |

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
      "status": "caption text authored; certified native Sequence Items pending"
    },
    {
      "id": "receipt-gated-ordered-departure",
      "status": "reference implemented; native observers and real navigation pending"
    }
  ],
  "artDirection": {
    "style": "ordinary hillside work courts and restrained mourning in local households, no imperial deathbed reconstruction",
    "historicalControls": "No Achyron address, authentic will, bishop speech, Sylvester scene or magic cure. Modern locator research only.",
    "referenceAssets": [
      "nicomedia-modern-locator"
    ],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "Two household clerks cannot satisfy the two service identities.",
      "220F100W at one receiver fails120F60W south and100F40W northeast.",
      "Each derived handoff requires its own collected ledger and owno2 req5 receipt, with no additional debit.",
      "Household return uses clerkso2 req1; service return uses clerkso2 req3, never ledger receipts.",
      "Final prior accounts visit is insufficient without phase-active received departure.",
      "Handoff destinations cannot swap, and original ledgers are not required to return.",
      "No emperor health, baptism-purchase, real will, coffin proxy or later Sylvester scene is generated.",
      "All sides can be omitted in every difficulty with finite ordinary gathering; neither optional failure nor grief score defeats main.",
      "Suburban villa coordinates and ancient coast/relief/pathfinding remain pending; no357/358 state imported.",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
