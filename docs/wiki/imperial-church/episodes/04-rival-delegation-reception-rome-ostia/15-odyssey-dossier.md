# 4. The African Petition

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `04-rival-delegation-reception-rome-ostia` · 313–314 CE; Roman hearing focus · 400×400

## Historical frame and fixed outcome

EN: Eusebius preserves a letter directing an African ecclesiastical dispute to a hearing at Rome. Optatus later describes a Roman hearing under Miltiades and a decision favoring Caecilian; his account is polemical and its date wording needs comparison. The bishop of Ostia appears among participants, not as evidence for a hearing in Ostia. Our two local delegation groups and their work records are fictional. The player does not decide the historical judgment.

ES: Eusebio conserva una carta que remite una disputa eclesiástica africana a una audiencia en Roma. Optato describe después una audiencia romana bajo Milcíades y una decisión favorable a Ceciliano; su relato es polémico y la datación requiere contraste. El obispo de Ostia aparece entre los participantes, no como prueba de una audiencia en Ostia. Nuestros dos grupos locales de delegados y sus registros son ficticios. El jugador no decide el juicio histórico.

EN: Two fictional working registers reached one local reception court; both original delegation groups then returned after their own observed receipt-backed departures. That administrative circuit establishes neither a fair trial nor the truth of either historical party’s case. The transmitted Roman decision remains attributed, and the controversy continues toward Arles.

ES: Dos registros ficticios llegaron a un patio local común de recepción; ambos grupos originales regresaron después de sus propias salidas observadas y respaldadas por recibo. Ese circuito administrativo no acredita juicio justo ni verdad de ninguna posición histórica. La decisión romana transmitida sigue atribuida y la controversia continúa hacia Arlés.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "The transmitted letter directs the African dispute to Rome; Optatus later gives a Roman hearing and decision for Caecilian. Ostia is an attendee’s see, not an attested hearing venue. Polemical framing, consular wording and party identity require comparison.",
        "es-ES": "La carta transmitida remite la disputa africana a Roma; Optato relata después una audiencia romana y decisión favorable a Ceciliano. Ostia es sede de un participante, no sede documentada de audiencia. El marco polémico, la fórmula consular y la identidad de la parte requieren contraste."
      },
      "architectCorrection": {
        "date": "2026-10-13",
        "author": "gpt-6",
        "approval": "independent historical review pending",
        "reason": "Direct primary passages replace candidate conflations; all gameplay participants and work outputs remain explicit fiction."
      }
    },
    {
      "consultedUrl": null,
      "passage": "No exact passage directly consulted for the dossier’s Rome/Ostia hearings; Eusebius HE X.5 mentions a Roman decision only indirectly in the contextual tradition.",
      "limitations": "Dossier URLs (Fourth Century/Optatus) not opened in this pass; Rome/Ostia may conflate distinct hearings. Needs primary passage before treating as established.",
      "status": "unavailable",
      "supportedClaim": "A Donatist dispute and episcopal/imperial adjudication are broadly attested by later sources, but this particular source audit does not verify the proposed hearings or location. / Las fuentes posteriores atestiguan en términos generales la disputa donatista y su arbitraje episcopal/imperial, pero esta auditoría no verifica las audiencias ni el lugar propuestos.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "No qualifying exact passage consulted.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/250110.htm",
      "passage": "Eusebius HE X.5.18–20",
      "coverageActuallyRead": "Complete displayed imperial summons to Miltiades/Marcus, including Africa parties and Rome destination.",
      "limitations": "Transmitted legal invitation, not private deliberation or proof of fairness.",
      "consultationDate": "2026-10-13",
      "approval": "architect interpretation; independent approval pending"
    },
    {
      "consultedUrl": "https://www.tertullian.org/fathers/optatus_01_book1.htm",
      "passage": "Optatus I.22–25 and edition notes188–192",
      "coverageActuallyRead": "Read petition, appointed Roman judges, decision/appeal and notes on party naming, date and Donatus identity.",
      "limitations": "Retrospective polemic; note190 contrasts consular wording with Augustine. No Ostia hearing or exact playable room follows.",
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

EN: Collect three requests from each visitor court and deliver each set to its own north/south preparation yard.

ES: Recoge tres solicitudes de cada patio de visitantes y entrega cada conjunto en su propio patio de preparación norte/sur.

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
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-2",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-2",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-3"
      ],
      "destinations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-1": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-3",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-2": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-3",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-3": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-2",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-2",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-3"
      ],
      "destinations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-1": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-4",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-2": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-4",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-3": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both original three-request chains reached their own preparation yards.

ES: Ambas cadenas originales de tres solicitudes llegaron a sus propios patios.

EN: Two labels protect the distinction; neither label makes its owner right.

ES: Dos etiquetas protegen la distinción; ninguna da razón a su propietario.

### o2 / phase-2

EN: Pay each yard 50 wood and 20 gold once, then create its own working register from that yard’s three collected requests.

ES: Paga una vez 50 de madera y 20 de oro a cada patio y crea su registro con las tres solicitudes recogidas de ese patio.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 50,
        "gold": 20
      },
      "id": "req-1",
      "receivingZones": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.destination-3"
      ],
      "allocations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.destination-3": {
          "wood": 50,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.04-rival-delegation-reception-rome-ostia.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 50,
        "gold": 20
      },
      "id": "req-2",
      "receivingZones": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.destination-4"
      ],
      "allocations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.destination-4": {
          "wood": 50,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.04-rival-delegation-reception-rome-ostia.o2.req-2.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-3",
      "inputEntities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-2",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-3"
      ],
      "outputEntities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.04-rival-delegation-reception-rome-ostia.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 50,
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
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-2",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-3"
      ],
      "outputEntities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.04-rival-delegation-reception-rome-ostia.o2.req-2.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 50,
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

EN: Two separate derived registers each have their own exact funded receipt.

ES: Dos registros derivados separados tienen cada uno su recibo exacto de financiación.

EN: I have funded two working tables, not bought two versions of truth.

ES: He financiado dos mesas de trabajo, no comprado dos versiones de la verdad.

### o3 / phase-3

EN: Deliver both labelled registers and both groups of two original fictional delegates to common eastern reception.

ES: Entrega ambos registros etiquetados y ambos grupos de dos delegados ficticios originales en la recepción común oriental.

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
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-register-1"
      ],
      "destinations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-register-1": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-register-1"
      ],
      "destinations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-register-1": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-2"
      ],
      "destinations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-1": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-5",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-2": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-2"
      ],
      "destinations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-1": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-5",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-2": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-5"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both distinct registers and all four original fictional delegates reached common reception.

ES: Ambos registros distintos y los cuatro delegados ficticios originales llegaron a recepción.

EN: Being admitted together is a local act of hospitality, not evidence of historical reconciliation.

ES: Recibirlos juntos es hospitalidad local, no prueba de reconciliación histórica.

### o4 / phase-4

EN: After each group’s reception, depart its original members and return each group to its own preparation yard.

ES: Tras la recepción de cada grupo, da salida a sus miembros originales y devuelve cada grupo a su propio patio de preparación.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "ordered-departure",
      "receiptObjective": "o3",
      "receiptRequirement": "req-3",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-1",
      "departingEntities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-2"
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
      "id": "req-2",
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-2"
      ],
      "destinations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-1": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-3",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-2": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "ordered-departure",
      "receiptObjective": "o3",
      "receiptRequirement": "req-4",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-3",
      "departingEntities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-2"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-3"
      },
      "id": "req-4",
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-2"
      ],
      "destinations": {
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-1": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-4",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-2": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Each returning group used its own arrival receipt and observed departure.

ES: Cada grupo que regresa utilizó su propio recibo de llegada y salida observada.

EN: The visitors can leave our yard without leaving their dispute behind.

ES: Los visitantes pueden salir de nuestro patio sin dejar atrás su disputa.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/04-rival-delegation-reception-rome-ostia.svg)

```json
{
  "bbox": [
    12.478,
    41.875,
    12.53,
    41.915
  ],
  "terrainProfile": "rome-ostia",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        172.98,
        74.81
      ],
      "lonLat": [
        12.5,
        41.909
      ],
      "name": {
        "en": "Northern fictional visitor court",
        "es-ES": "Patio ficticio norteño de visitantes"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        146.46,
        315.28
      ],
      "lonLat": [
        12.496,
        41.882
      ],
      "name": {
        "en": "Southern fictional visitor court",
        "es-ES": "Patio ficticio sureño de visitantes"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        80.17,
        154.97
      ],
      "lonLat": [
        12.486,
        41.9
      ],
      "name": {
        "en": "Northern separate preparation yard",
        "es-ES": "Patio separado norteño de preparación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        226.02,
        315.28
      ],
      "lonLat": [
        12.508,
        41.882
      ],
      "name": {
        "en": "Southern separate preparation yard",
        "es-ES": "Patio separado sureño de preparación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        325.46,
        190.59
      ],
      "lonLat": [
        12.523,
        41.896
      ],
      "name": {
        "en": "Eastern fictional common reception",
        "es-ES": "Recepción común ficticia oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-reception-chain",
      "hubOrder": [
        "hub-1",
        "hub-3",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "south-reception-chain",
      "hubOrder": [
        "hub-2",
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "working-yard-link",
      "hubOrder": [
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 6
    }
  ],
  "terrainInstructions": "Local eastern Roman urban/hinterland crop east of the schematic Tiber. Fictional north/south visitor courts, separate preparation yards and one eastern receiving court; the historical Lateran venue named by Optatus is context, not an excavated house/room footprint or a playable modern basilica. No journey from Africa or obligatory lower-Tiber/Ostia crossing. No hearing in Ostia inferred from an attendee’s episcopal see. Avoid Renaissance/Baroque Lateran, modern railways and modern archaeological boundary walls. Ancient road gradients and dated urban parcels require review; the five working courts are openly invented local placements.",
  "corridorStraightLengthsTiles": {
    "north-reception-chain": 370.5,
    "south-reception-chain": 239.05,
    "working-yard-link": 216.73
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
        12.477,
        41.95
      ],
      [
        12.47,
        41.925
      ],
      [
        12.47,
        41.9
      ],
      [
        12.475,
        41.87
      ],
      [
        12.42,
        41.85
      ],
      [
        12.4,
        41.8
      ],
      [
        12.28,
        41.76
      ],
      [
        12.23,
        41.73
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
  "asset": "docs/design/maps/imperial-church/odyssey/04-rival-delegation-reception-rome-ostia.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-1",
      "role": "fictional-local-work-request",
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
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-2",
      "role": "fictional-local-work-request",
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
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-3",
      "role": "fictional-local-work-request",
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
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-1",
      "role": "fictional-local-work-request",
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
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-2",
      "role": "fictional-local-work-request",
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
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-3",
      "role": "fictional-local-work-request",
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
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.north-register-1",
      "role": "fictional-labelled-delegation-register",
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
    },
    {
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.south-register-1",
      "role": "fictional-labelled-delegation-register",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-1",
      "role": "fictional-local-delegation-member",
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
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-2",
      "role": "fictional-local-delegation-member",
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
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-1",
      "role": "fictional-local-delegation-member",
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
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-2",
      "role": "fictional-local-delegation-member",
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
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.04-rival-delegation-reception-rome-ostia.destination-5",
      "hub": "hub-5",
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
      "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-1",
      "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-2",
      "imperial-church.04-rival-delegation-reception-rome-ostia.north-requests-3"
    ],
    "south-requests": [
      "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-1",
      "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-2",
      "imperial-church.04-rival-delegation-reception-rome-ostia.south-requests-3"
    ],
    "north-register": [
      "imperial-church.04-rival-delegation-reception-rome-ostia.north-register-1"
    ],
    "south-register": [
      "imperial-church.04-rival-delegation-reception-rome-ostia.south-register-1"
    ],
    "north-delegates": [
      "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-1",
      "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-2"
    ],
    "south-delegates": [
      "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-1",
      "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-2"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.north-delegates-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    },
    {
      "entities": [
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-1",
        "imperial-church.04-rival-delegation-reception-rome-ostia.south-delegates-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Labels without a verdict / Etiquetas sin veredicto

EN: Recover both separate copies from labels without a verdict and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de etiquetas sin veredicto y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Separate optional context does not authenticate a petition or award doctrinal victory.

ES: El contexto opcional separado no autentica una petición ni otorga victoria doctrinal.

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
          "04-rival-delegation-reception-rome-ostia.side-1.entity-1",
          "04-rival-delegation-reception-rome-ostia.side-1.entity-2"
        ],
        "destinations": {
          "04-rival-delegation-reception-rome-ostia.side-1.entity-1": "04-rival-delegation-reception-rome-ostia.side-1.zone-1",
          "04-rival-delegation-reception-rome-ostia.side-1.entity-2": "04-rival-delegation-reception-rome-ostia.side-1.zone-1"
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
        "id": "04-rival-delegation-reception-rome-ostia.side-1.entity-1",
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
        "id": "04-rival-delegation-reception-rome-ostia.side-1.entity-2",
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
        "id": "04-rival-delegation-reception-rome-ostia.side-1.zone-1",
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
      "onceFlag": "04-rival-delegation-reception-rome-ostia.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.04-rival-delegation-reception-rome-ostia"
      ],
      "historicalNote": {
        "en": "Eusebius preserves a letter directing an African ecclesiastical dispute to a hearing at Rome. Optatus later describes a Roman hearing under Miltiades and a decision favoring Caecilian; his account is polemical and its date wording needs comparison. The bishop of Ostia appears among participants, not as evidence for a hearing in Ostia. Our two local delegation groups and their work records are fictional. The player does not decide the historical judgment.",
        "es-ES": "Eusebio conserva una carta que remite una disputa eclesiástica africana a una audiencia en Roma. Optato describe después una audiencia romana bajo Milcíades y una decisión favorable a Ceciliano; su relato es polémico y la datación requiere contraste. El obispo de Ostia aparece entre los participantes, no como prueba de una audiencia en Ostia. Nuestros dos grupos locales de delegados y sus registros son ficticios. El jugador no decide el juicio histórico."
      },
      "hint": {
        "en": "Collect three requests from each visitor court and deliver each set to its own north/south preparation yard.",
        "es-ES": "Recoge tres solicitudes de cada patio de visitantes y entrega cada conjunto en su propio patio de preparación norte/sur."
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
      "north-reception-chain",
      "south-reception-chain",
      "working-yard-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Shared ordinary hospitality / Hospitalidad ordinaria compartida

EN: Bring each of the two aid crates to its assigned household at shared ordinary hospitality. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hospitalidad ordinaria compartida. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Independent aid accepts fictional neighbors without testing their faction or creed.

ES: La ayuda independiente recibe a vecinos ficticios sin examinar facción ni credo.

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
          "04-rival-delegation-reception-rome-ostia.side-2.entity-1",
          "04-rival-delegation-reception-rome-ostia.side-2.entity-2"
        ],
        "destinations": {
          "04-rival-delegation-reception-rome-ostia.side-2.entity-1": "04-rival-delegation-reception-rome-ostia.side-2.zone-1",
          "04-rival-delegation-reception-rome-ostia.side-2.entity-2": "04-rival-delegation-reception-rome-ostia.side-2.zone-2"
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
        "id": "04-rival-delegation-reception-rome-ostia.side-2.entity-1",
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
        "id": "04-rival-delegation-reception-rome-ostia.side-2.entity-2",
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
        "id": "04-rival-delegation-reception-rome-ostia.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "04-rival-delegation-reception-rome-ostia.side-2.zone-2",
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
      "onceFlag": "04-rival-delegation-reception-rome-ostia.side-2.rewarded",
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
      "north-reception-chain",
      "south-reception-chain",
      "working-yard-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Two tables under a roof / Dos mesas bajo un tejado

EN: Pay 50 wood and restore the damaged store of two tables under a roof to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de dos mesas bajo un tejado. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair an ordinary independent work shelter, not the actual House of Fausta.

ES: Repara un cobertizo independiente ordinario, no la casa real de Fausta.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "04-rival-delegation-reception-rome-ostia.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "04-rival-delegation-reception-rome-ostia.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "04-rival-delegation-reception-rome-ostia.side-3.payment",
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
        "id": "04-rival-delegation-reception-rome-ostia.side-3.entity-1",
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
        "id": "04-rival-delegation-reception-rome-ostia.side-3.zone-1",
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
      "onceFlag": "04-rival-delegation-reception-rome-ostia.side-3.rewarded",
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
      "north-reception-chain",
      "south-reception-chain",
      "working-yard-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Supplies beyond the hearing / Suministros fuera de la audiencia

EN: Escort the trader of supplies beyond the hearing to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de suministros fuera de la audiencia hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Bounded local exchange cannot purchase a bishop’s vote or alter the decision.

ES: El intercambio local limitado no compra el voto de un obispo ni cambia la decisión.

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
          "04-rival-delegation-reception-rome-ostia.side-4.entity-1"
        ],
        "destinations": {
          "04-rival-delegation-reception-rome-ostia.side-4.entity-1": "04-rival-delegation-reception-rome-ostia.side-4.zone-1"
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
        "receipt": "04-rival-delegation-reception-rome-ostia.side-4.payment",
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
        "id": "04-rival-delegation-reception-rome-ostia.side-4.entity-1",
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
        "id": "04-rival-delegation-reception-rome-ostia.side-4.zone-1",
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
      "onceFlag": "04-rival-delegation-reception-rome-ostia.side-4.rewarded",
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
      "north-reception-chain",
      "south-reception-chain",
      "working-yard-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The northern visitors’ approach / El acceso de los visitantes norteños

EN: Scout both marked viewpoints of the northern visitors’ approach. Benefit: Mark the proposed north-reception-chain local land circuit once. All mandatory receivers are already disclosed.

ES: Explora los dos miradores señalados de el acceso de los visitantes norteños. Ventaja: Señala una vez el circuito terrestre local propuesto north-reception-chain. Todos los receptores obligatorios ya se indican.

EN: Mark the proposed local north circuit, never a discovered authentic travel itinerary.

ES: Señala el circuito local norteño propuesto, nunca un itinerario histórico descubierto.

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
          "04-rival-delegation-reception-rome-ostia.side-5.zone-1",
          "04-rival-delegation-reception-rome-ostia.side-5.zone-2"
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
        "id": "04-rival-delegation-reception-rome-ostia.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "04-rival-delegation-reception-rome-ostia.side-5.zone-2",
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
      "target": "north-reception-chain proposed local land approach",
      "resources": {},
      "onceFlag": "04-rival-delegation-reception-rome-ostia.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "north-reception-chain"
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
      "north-reception-chain",
      "south-reception-chain",
      "working-yard-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Between the working yards / Entre los patios de trabajo

EN: Escort the local guide of between the working yards to the marked road junction. Benefit: Mark the proposed working-yard-link local land circuit once. All mandatory receivers are already disclosed.

ES: Escolta al guía local de entre los patios de trabajo hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local propuesto working-yard-link. Todos los receptores obligatorios ya se indican.

EN: Mark a local land link that remains independent of both delegation identities.

ES: Señala una unión terrestre local independiente de ambas identidades de delegación.

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
          "04-rival-delegation-reception-rome-ostia.side-6.entity-1"
        ],
        "destinations": {
          "04-rival-delegation-reception-rome-ostia.side-6.entity-1": "04-rival-delegation-reception-rome-ostia.side-6.zone-1"
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
        "id": "04-rival-delegation-reception-rome-ostia.side-6.entity-1",
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
        "id": "04-rival-delegation-reception-rome-ostia.side-6.zone-1",
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
      "target": "working-yard-link proposed local land approach",
      "resources": {},
      "onceFlag": "04-rival-delegation-reception-rome-ostia.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "working-yard-link"
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
      "north-reception-chain",
      "south-reception-chain",
      "working-yard-link"
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
      "id": "parallel-reception",
      "optionalObjectives": [
        "side-5",
        "side-6"
      ],
      "costOfOpportunity": "Survey two local circuits and split preparation/escort teams; preserve separate payments and groups.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "separate-record-work",
      "optionalObjectives": [
        "side-1",
        "side-3"
      ],
      "costOfOpportunity": "Invest in labels and shelter while reserving both mandatory register payments.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "hospitality-and-supply",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Run independent shared care and bounded trade alongside both mandatory visitor chains.",
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
      "wood": 808,
      "gold": 244,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 100,
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
      "wood": 780,
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
      "wood": 830,
      "gold": 255,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 100,
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
      "wood": 780,
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
      "wood": 853,
      "gold": 267,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 100,
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
      "wood": 780,
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
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.title / always | none | The African Petition | La petición africana |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.fact-intro / intro first | collection-narrator | Eusebius preserves a letter directing an African ecclesiastical dispute to a hearing at Rome. Optatus later describes a Roman hearing under Miltiades and a decision favoring Caecilian; his account is polemical and its date wording needs comparison. The bishop of Ostia appears among participants, not as evidence for a hearing in Ostia. Our two local delegation groups and their work records are fictional. The player does not decide the historical judgment. | Eusebio conserva una carta que remite una disputa eclesiástica africana a una audiencia en Roma. Optato describe después una audiencia romana bajo Milcíades y una decisión favorable a Ceciliano; su relato es polémico y la datación requiere contraste. El obispo de Ostia aparece entre los participantes, no como prueba de una audiencia en Ostia. Nuestros dos grupos locales de delegados y sus registros son ficticios. El jugador no decide el juicio histórico. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.persona-intro / after handover | imperial-clerk | Two parties, two bundles. My old desk would have asked for one neat conclusion. The inherited dossier refuses to oblige: its author has already chosen a side. I can prepare separate labels for our imagined visitors and still hear the temptation to make orderly paperwork stand for justice. I was not in that Roman room. | Dos partes, dos paquetes. Mi antigua mesa habría pedido una conclusión ordenada. El expediente heredado se resiste: su autor ya ha elegido un bando. Puedo preparar etiquetas separadas para nuestros visitantes imaginados y aun sentir la tentación de hacer pasar papeles ordenados por justicia. No estuve en aquella sala romana. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.route-help / available from start; repeatable without effect | none | Keep the two chains separate. Collect three ordinary requests from each visitor court and deliver each set to its own preparation yard. Pay 50 wood and 20 gold at each yard once and make that chain’s working register from its own three inputs and receipt. Bring both registers and both groups of two original fictional delegates to eastern reception. Then depart each group only after its own reception receipt and return it to its assigned preparation yard. Neither group is an enemy army or a historical named bishop. | Mantén separadas las dos cadenas. Recoge tres solicitudes ordinarias de cada patio de visitantes y lleva cada conjunto a su propio patio de preparación. Paga una vez 50 de madera y 20 de oro en cada patio y prepara el registro de esa cadena con sus tres entradas y recibo propios. Lleva ambos registros y ambos grupos de dos delegados ficticios originales a la recepción oriental. Después da salida a cada grupo solo tras su propio recibo de recepción y devuélvelo a su patio asignado. Ningún grupo es ejército enemigo ni obispo histórico con nombre. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o1-goal / phase-1 active | none | Collect three requests from each visitor court and deliver each set to its own north/south preparation yard. | Recoge tres solicitudes de cada patio de visitantes y entrega cada conjunto en su propio patio de preparación norte/sur. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o1-receipt / o1 latched once | none | Both original three-request chains reached their own preparation yards. | Ambas cadenas originales de tres solicitudes llegaron a sus propios patios. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o1-reaction / after o1 receipt | imperial-clerk | Two labels protect the distinction; neither label makes its owner right. | Dos etiquetas protegen la distinción; ninguna da razón a su propietario. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o2-goal / phase-2 active | none | Pay each yard 50 wood and 20 gold once, then create its own working register from that yard’s three collected requests. | Paga una vez 50 de madera y 20 de oro a cada patio y crea su registro con las tres solicitudes recogidas de ese patio. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o2-receipt / o2 latched once | none | Two separate derived registers each have their own exact funded receipt. | Dos registros derivados separados tienen cada uno su recibo exacto de financiación. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o2-reaction / after o2 receipt | imperial-clerk | I have funded two working tables, not bought two versions of truth. | He financiado dos mesas de trabajo, no comprado dos versiones de la verdad. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o3-goal / phase-3 active | none | Deliver both labelled registers and both groups of two original fictional delegates to common eastern reception. | Entrega ambos registros etiquetados y ambos grupos de dos delegados ficticios originales en la recepción común oriental. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o3-receipt / o3 latched once | none | Both distinct registers and all four original fictional delegates reached common reception. | Ambos registros distintos y los cuatro delegados ficticios originales llegaron a recepción. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o3-reaction / after o3 receipt | imperial-clerk | Being admitted together is a local act of hospitality, not evidence of historical reconciliation. | Recibirlos juntos es hospitalidad local, no prueba de reconciliación histórica. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o4-goal / phase-4 active | none | After each group’s reception, depart its original members and return each group to its own preparation yard. | Tras la recepción de cada grupo, da salida a sus miembros originales y devuelve cada grupo a su propio patio de preparación. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o4-receipt / o4 latched once | none | Each returning group used its own arrival receipt and observed departure. | Cada grupo que regresa utilizó su propio recibo de llegada y salida observada. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.o4-reaction / after o4 receipt | imperial-clerk | The visitors can leave our yard without leaving their dispute behind. | Los visitantes pueden salir de nuestro patio sin dejar atrás su disputa. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from labels without a verdict and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de etiquetas sin veredicto y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-1-complete / side-1 completed | none | Labels without a verdict completed. Its stated benefit has been granted once. | Etiquetas sin veredicto: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-1-lost / side-1 failed-optional | none | Labels without a verdict is unavailable after the loss of its unique participant or object. The main mission continues. | Etiquetas sin veredicto: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at shared ordinary hospitality. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hospitalidad ordinaria compartida. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-2-complete / side-2 completed | none | Shared ordinary hospitality completed. Its stated benefit has been granted once. | Hospitalidad ordinaria compartida: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-2-lost / side-2 failed-optional | none | Shared ordinary hospitality is unavailable after the loss of its unique participant or object. The main mission continues. | Hospitalidad ordinaria compartida: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of two tables under a roof to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de dos mesas bajo un tejado. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-3-complete / side-3 completed | none | Two tables under a roof completed. Its stated benefit has been granted once. | Dos mesas bajo un tejado: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-3-lost / side-3 failed-optional | none | Two tables under a roof is unavailable after the loss of its unique participant or object. The main mission continues. | Dos mesas bajo un tejado: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-4-goal / optional list from start | none | Escort the trader of supplies beyond the hearing to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de suministros fuera de la audiencia hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-4-complete / side-4 completed | none | Supplies beyond the hearing completed. Its stated benefit has been granted once. | Suministros fuera de la audiencia: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-4-lost / side-4 failed-optional | none | Supplies beyond the hearing is unavailable after the loss of its unique participant or object. The main mission continues. | Suministros fuera de la audiencia: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of the northern visitors’ approach. Benefit: Mark the proposed north-reception-chain local land circuit once. All mandatory receivers are already disclosed. | Explora los dos miradores señalados de el acceso de los visitantes norteños. Ventaja: Señala una vez el circuito terrestre local propuesto north-reception-chain. Todos los receptores obligatorios ya se indican. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-5-complete / side-5 completed | none | The northern visitors’ approach completed. Its stated benefit has been granted once. | El acceso de los visitantes norteños: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-5-lost / side-5 failed-optional | none | The northern visitors’ approach is unavailable after the loss of its unique participant or object. The main mission continues. | El acceso de los visitantes norteños: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-6-goal / optional list from start | none | Escort the local guide of between the working yards to the marked road junction. Benefit: Mark the proposed working-yard-link local land circuit once. All mandatory receivers are already disclosed. | Escolta al guía local de entre los patios de trabajo hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local propuesto working-yard-link. Todos los receptores obligatorios ya se indican. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-6-complete / side-6 completed | none | Between the working yards completed. Its stated benefit has been granted once. | Entre los patios de trabajo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.side-6-lost / side-6 failed-optional | none | Between the working yards is unavailable after the loss of its unique participant or object. The main mission continues. | Entre los patios de trabajo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.fact-outro / victory first | collection-narrator | Two fictional working registers reached one local reception court; both original delegation groups then returned after their own observed receipt-backed departures. That administrative circuit establishes neither a fair trial nor the truth of either historical party’s case. The transmitted Roman decision remains attributed, and the controversy continues toward Arles. | Dos registros ficticios llegaron a un patio local común de recepción; ambos grupos originales regresaron después de sus propias salidas observadas y respaldadas por recibo. Ese circuito administrativo no acredita juicio justo ni verdad de ninguna posición histórica. La decisión romana transmitida sigue atribuida y la controversia continúa hacia Arlés. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.persona-outro / after fact-outro | imperial-clerk | Every visitor has a return line. I am pleased with the accounting and less pleased with how easily that pleasure can become a verdict. Let the two labels remain. We have done the work outside a hearing, not earned the right to speak for everyone within it. | Cada visitante tiene una línea de regreso. Me satisface la cuenta y me satisface menos lo fácilmente que ese placer puede volverse veredicto. Que permanezcan las dos etiquetas. Hemos trabajado fuera de una audiencia, no ganado derecho a hablar por todos los presentes. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.04-rival-delegation-reception-rome-ostia.odyssey.next-episode / after persona-outro | none | Continue with The Road to Arles. This episode does not complete the campaign. | Continúa con El camino hacia Arlés. Este episodio no termina la campaña. |

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
    "style": "sober late Roman local working districts and ordinary hospitality",
    "historicalControls": "fictional work courts, not a reconstructed hearing room or council basilica",
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "all three requests in each distinct chain required",
      "north receipt cannot fund south derived register or vice versa",
      "one arriving delegation cannot satisfy the other reception or departure receipt",
      "early visits to either preparation yard cannot count as final guarded return",
      "no hostile faction, bishop capture or doctrine meter",
      "no Ostia hearing invented",
      "no precise October day asserted from conflicting Optatus consular wording",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
