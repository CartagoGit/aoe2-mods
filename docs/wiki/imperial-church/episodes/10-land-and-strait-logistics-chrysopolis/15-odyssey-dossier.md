# 9. Across the Bright Shore

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `10-land-and-strait-logistics-chrysopolis` · 18 September 324 CE, conventional · 400×400

## Historical frame and fixed outcome

EN: The final campaign against Licinius reached the Asian side of the Bosphorus after the fighting around Byzantium and the Hellespont. The usual chronology places the victory at Chrysopolis on 18 September 324. Zosimus describes crossings near a northern sacred promontory and fighting between it and Chalcedon; that narrative does not fix our local landing. The player operates a fictional two-shore supply service, not the emperor’s fleet or a theological war.

ES: La campaña final contra Licinio llegó a la orilla asiática del Bósforo tras los combates en torno a Bizancio y el Helesponto. La cronología habitual sitúa la victoria de Crisópolis el 18 de septiembre de 324. Zósimo describe cruces junto a un promontorio sagrado norteño y combates entre este y Calcedonia; ese relato no fija nuestro desembarque local. El jugador dirige un servicio ficticio de provisiones entre dos orillas, no la flota imperial ni una guerra teológica.

EN: The fictional two-shore service delivered its original people and four assigned loads. Historical accounts place Licinius’ defeat and later surrender in the final 324 sequence; neither the service nor a clerk’s paperwork caused sole imperial rule. Church disputes did not end with the battle.

ES: El servicio ficticio entre dos orillas entregó a sus personas originales y cuatro cargas asignadas. Los relatos históricos sitúan la derrota de Licinio y su posterior rendición en la secuencia final de 324; ni el servicio ni los papeles de un funcionario causaron el gobierno imperial único. Las disputas eclesiales no terminaron con la batalla.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "The final324 military sequence includes the Asian-shore victory conventionally dated18September atChrysopolis and Licinius’ subsequent surrender. Zosimus’ northern crossing narrative does not survey this local supply route.",
        "es-ES": "La secuencia militar final de324 incluye la victoria asiática fechada convencionalmente el18de septiembre enCrisópolis y la rendición posterior deLicinio. El relato de cruce norteño deZósimo no prospecta esta ruta local de provisiones."
      },
      "architectCorrection": {
        "date": "2026-10-13",
        "author": "gpt-6",
        "approval": "independent historical review pending",
        "reason": "Separated direct Zosimus military sequence, conventional scholarly dates and archaeological place controls; fictional supply crossing is not an imperial tactical footprint."
      }
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/25022.htm",
      "passage": "No precise battle passage opened; Eusebius VC II checked generally, Britannica not consulted.",
      "limitations": "Do not merge both battles as one event; precise conventional dates need source support.",
      "status": "unavailable",
      "supportedClaim": "The checked material does not independently verify the 18 September date or Chrysopolis location. / El material consultado no verifica independientemente la fecha del 18 de septiembre ni el lugar de Crisópolis.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "No exact battle locator found.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.tertullian.org/fathers/zosimus02_book2.htm",
      "passage": "New History II; printed49–50 Asian shore and battle/surrender sequence",
      "coverageActuallyRead": "Architect directly read the displayed military narrative; no modern numbered subsection displayed in the1814 translation.",
      "limitations": "Later hostile account; not a precise calendar date, GPS crossing/battlefield, neutral casualty total or private dialogue.",
      "consultationDate": "2026-10-13",
      "approval": "architect interpretation; independent approval pending"
    },
    {
      "consultedUrl": "https://roman-emperors.sites.luc.edu/licinius.htm",
      "passage": "Michael DiMaio, Second Civil War and Death paragraphs",
      "coverageActuallyRead": "Architect directly read conventional3July/18September324 dates and the separate military sequence.",
      "limitations": "Modern scholarly reference updated1997, not a primary ancient date attestation; summary and interpretive dates retain review gate.",
      "consultationDate": "2026-10-13",
      "approval": "architect interpretation; independent approval pending"
    },
    {
      "consultedUrl": "https://www.ancientportsantiques.com/wp-content/uploads/Documents/PLACES/Bosphorus-BlackSea/Chalcedon-Belke2021.pdf",
      "passage": "Belke2021 chapter pp223–224 and227–228; map figure pp226",
      "coverageActuallyRead": "Architect read preliminary/geographic remarks and Chrysopolis harbor/sedimentation sections; inspected figure1.",
      "limitations": "Only selected chapter passages, not full73-page offprint; multi-era coast and later Skutarion ruins not324 quay. Official Propylaeum access denied; mirrored scholarly PDF consulted.",
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

EN: Stage eight original auxiliaries and all four distinct assigned loads at European embarkation; pay the two150/100 and100/80 food/wood consignments once.

ES: Prepara ocho auxiliares originales y las cuatro cargas asignadas distintas en el embarque europeo; paga una vez las dos remesas de150/100 y100/80 de alimento/madera.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 8,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-3",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-5",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-6",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-7",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-8",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-9",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-10"
      ],
      "destinations": {
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-1": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-2": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-3": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-4": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-5": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-6": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-7": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-8": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-9": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-10": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-2"
      ],
      "destinations": {
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-1": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-2": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-4",
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-5",
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-2"
      ],
      "destinations": {
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-1": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-2": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 150,
        "wood": 100
      },
      "id": "req-6",
      "receivingZones": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2"
      ],
      "allocations": {
        "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2": {
          "food": 150,
          "wood": 100
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.10-land-and-strait-logistics-chrysopolis.o1.req-6.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 100,
        "wood": 80
      },
      "id": "req-7",
      "receivingZones": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2"
      ],
      "allocations": {
        "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2": {
          "food": 100,
          "wood": 80
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.10-land-and-strait-logistics-chrysopolis.o1.req-7.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Distinct original shore identities and separately labelled funded consignments are ready.

ES: Las identidades originales distintas de la orilla y las remesas financiadas con etiquetas separadas están preparadas.

EN: Two labels are worth more than an impressive total that tells no receiver what belongs to it.

ES: Dos etiquetas valen más que un total impresionante que no dice a cada receptor qué le corresponde.

### o2 / phase-2

EN: Cross eight actually staged auxiliaries and both pairs of assigned original loads by manifest-backed ferry journeys to the Asian landing.

ES: Cruza con ocho auxiliares realmente preparados y ambos pares de cargas originales asignadas mediante viajes en embarcación respaldados por manifiesto hasta el desembarque asiático.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "transport-journey",
      "requiredCount": 8,
      "allowedCorridorIds": [
        "local-strait-passage",
        "northern-local-water-loop"
      ],
      "readyReceipt": {
        "objective": "o1",
        "requirement": "req-1"
      },
      "eventOrder": [
        "ready-receipt",
        "board",
        "depart-origin",
        "water-transit",
        "arrive-destination",
        "disembark"
      ],
      "proofPolicy": {
        "samePassengerIdentity": true,
        "sameCarrierWithinJourney": true,
        "observedPositions": true,
        "sharedCapacityReservation": true,
        "persistentScopedReceipts": true,
        "arrivalAloneInsufficient": true,
        "noTimerSubstitution": true,
        "idempotentCompletion": true,
        "sourceObjectiveLatched": true
      },
      "passengerSlotsEach": 1,
      "id": "req-1",
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-3",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-5",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-6",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-7",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-8",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-9",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-10"
      ],
      "carriers": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-2"
      ],
      "originZone": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
      "destinationZone": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-3"
    },
    {
      "kind": "transport-journey",
      "requiredCount": 2,
      "allowedCorridorIds": [
        "local-strait-passage",
        "northern-local-water-loop"
      ],
      "readyReceipt": {
        "objective": "o1",
        "requirement": "req-3"
      },
      "eventOrder": [
        "ready-receipt",
        "board",
        "depart-origin",
        "water-transit",
        "arrive-destination",
        "disembark"
      ],
      "proofPolicy": {
        "samePassengerIdentity": true,
        "sameCarrierWithinJourney": true,
        "observedPositions": true,
        "sharedCapacityReservation": true,
        "persistentScopedReceipts": true,
        "arrivalAloneInsufficient": true,
        "noTimerSubstitution": true,
        "idempotentCompletion": true,
        "sourceObjectiveLatched": true
      },
      "passengerSlotsEach": 1,
      "id": "req-2",
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-2"
      ],
      "carriers": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-2"
      ],
      "originZone": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
      "destinationZone": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-3"
    },
    {
      "kind": "transport-journey",
      "requiredCount": 2,
      "allowedCorridorIds": [
        "local-strait-passage",
        "northern-local-water-loop"
      ],
      "readyReceipt": {
        "objective": "o1",
        "requirement": "req-5"
      },
      "eventOrder": [
        "ready-receipt",
        "board",
        "depart-origin",
        "water-transit",
        "arrive-destination",
        "disembark"
      ],
      "proofPolicy": {
        "samePassengerIdentity": true,
        "sameCarrierWithinJourney": true,
        "observedPositions": true,
        "sharedCapacityReservation": true,
        "persistentScopedReceipts": true,
        "arrivalAloneInsufficient": true,
        "noTimerSubstitution": true,
        "idempotentCompletion": true,
        "sourceObjectiveLatched": true
      },
      "passengerSlotsEach": 1,
      "id": "req-3",
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-2"
      ],
      "carriers": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-2"
      ],
      "originZone": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
      "destinationZone": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-3"
    }
  ],
  "neverUseTimerInstead": true,
  "exportedLedgers": [
    {
      "id": "auxiliaries-crossed",
      "fromRequirements": [
        "req-1"
      ],
      "minimumCount": 8,
      "snapshot": "exact original identities with completed scoped water journeys at o2 latch; immutable after export",
      "operator": "intersection"
    }
  ]
}
```

EN: Original boarded and unloaded identities have their own completed Asian-shore journey records.

ES: Las identidades originales embarcadas y desembarcadas tienen sus propios registros completos de viaje a la orilla asiática.

EN: The ink line took one stroke. The ferry took several trips. I shall charge the ledger to reality.

ES: La línea de tinta necesitó un trazo. La embarcación necesitó varios viajes. Ajustaré el registro a la realidad.

### o3 / phase-3

EN: Deliver both original north loads and eight actually crossed original auxiliaries to the northeastern inland court.

ES: Entrega ambas cargas norteñas originales y ocho auxiliares originales realmente cruzados en el patio interior nororiental.

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
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-2"
      ],
      "destinations": {
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-1": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-2": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 8,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o2",
        "ledger": "auxiliaries-crossed"
      },
      "id": "req-2",
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-3",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-5",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-6",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-7",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-8",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-9",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-10"
      ],
      "destinations": {
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-1": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-2": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-3": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-4": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-5": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-6": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-7": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-8": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-9": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-10": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The north court has its own assigned pair and original auxiliary support.

ES: El patio norteño tiene su propio par asignado y apoyo auxiliar original.

EN: One book is complete. That is no excuse to close the other one.

ES: Un libro está completo. Eso no justifica cerrar el otro.

### o4 / phase-4

EN: Deliver both original south loads to their southeastern inland receiver.

ES: Entrega ambas cargas sureñas originales en su receptor interior suroriental.

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
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-2"
      ],
      "destinations": {
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-1": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-5",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-2": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-5"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The separate south consignment reached its own receiver, without replacement by northern deliveries.

ES: La remesa sureña separada llegó a su propio receptor, sin sustituirla por entregas norteñas.

EN: I can finish this column. I cannot finish a city’s argument with it.

ES: Puedo terminar esta columna. No puedo terminar con ella la disputa de una ciudad.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/10-land-and-strait-logistics-chrysopolis.svg)

```json
{
  "bbox": [
    28.975,
    40.998,
    29.06,
    41.065
  ],
  "terrainProfile": "chrysopolis",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        101.23,
        127.72
      ],
      "lonLat": [
        28.993,
        41.045
      ],
      "name": {
        "en": "Fictional European preparation court north of the Golden Horn",
        "es-ES": "Patio ficticio europeo de preparación al norte del Cuerno de Oro"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        89.2,
        180.89
      ],
      "lonLat": [
        28.99,
        41.035
      ],
      "name": {
        "en": "Proposed European embarkation sector",
        "es-ES": "Sector europeo propuesto de embarque"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        185.46,
        212.79
      ],
      "lonLat": [
        29.014,
        41.029
      ],
      "name": {
        "en": "Proposed Chrysopolis landing sector",
        "es-ES": "Sector propuesto de desembarque en Crisópolis"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        309.8,
        148.99
      ],
      "lonLat": [
        29.045,
        41.041
      ],
      "name": {
        "en": "Fictional northeastern inland receiver",
        "es-ES": "Receptor ficticio interior nororiental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        281.73,
        313.82
      ],
      "lonLat": [
        29.038,
        41.01
      ],
      "name": {
        "en": "Fictional southeastern inland receiver",
        "es-ES": "Receptor ficticio interior suroriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-6",
      "centre": [
        261.67,
        95.82
      ],
      "lonLat": [
        29.033,
        41.051
      ],
      "name": {
        "en": "Northern open-water approach control",
        "es-ES": "Control de acceso norteño en aguas abiertas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-7",
      "centre": [
        69.14,
        117.08
      ],
      "lonLat": [
        28.985,
        41.047
      ],
      "name": {
        "en": "Ordinary European hillside support",
        "es-ES": "Apoyo ordinario en ladera europea"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "west-support",
      "hubOrder": [
        "hub-1",
        "hub-7",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "local-strait-passage",
      "hubOrder": [
        "hub-2",
        "hub-3"
      ],
      "mode": "water",
      "widthTiles": 14
    },
    {
      "id": "northern-local-water-loop",
      "hubOrder": [
        "hub-2",
        "hub-6",
        "hub-3"
      ],
      "mode": "water",
      "widthTiles": 12
    },
    {
      "id": "east-north-receiving",
      "hubOrder": [
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-south-receiving",
      "hubOrder": [
        "hub-3",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-inland-link",
      "hubOrder": [
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 8
    }
  ],
  "terrainInstructions": "One continuous Bosphorus frame: European courts north of the Golden Horn west, Chrysopolis/modernUskudar landing and inland districts east. The strait is an actual impassable land barrier; no land bridge, teleport or decorative substitute. Modern Natural Earth coastline is only a regional control. Belke identifies silting, Roman jetties and much later Skutarion structures: reconstruct dated 324 shore/harbor extent before placement, especially the proposed landing whose modern point is not an ancient quay. No Ottoman mosque, modern quay/sea wall, Bosphorus bridge, railway tunnel, Justinianic harbor or later palace imported into 324. Local water paths are fictional logistics alternatives, not Zosimus’s northern military crossing; Sacred Promontory and full Chalcedon battlefield remain outside this local tactical footprint. Actual current-aware navigation, landing pockets, elevation and path lengths need native QA.",
  "corridorStraightLengthsTiles": {
    "west-support": 100.7,
    "local-strait-passage": 101.41,
    "northern-local-water-loop": 331.92,
    "east-north-receiving": 139.75,
    "east-south-receiving": 139.55,
    "east-inland-link": 167.2
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
  "asset": "docs/design/maps/imperial-church/odyssey/10-land-and-strait-logistics-chrysopolis.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-1",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -14,
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-2",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -12,
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-3",
      "role": "fictional-original-auxiliary",
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-4",
      "role": "fictional-original-auxiliary",
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-5",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -14,
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-6",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -12,
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-7",
      "role": "fictional-original-auxiliary",
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-8",
      "role": "fictional-original-auxiliary",
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
    },
    {
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-9",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -14,
        12
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-10",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -12,
        12
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-1",
      "role": "fictional-north-assigned-loadable-proxy",
      "initialHub": "hub-1",
      "offsetTiles": [
        0,
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-2",
      "role": "fictional-north-assigned-loadable-proxy",
      "initialHub": "hub-1",
      "offsetTiles": [
        2,
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-1",
      "role": "fictional-south-assigned-loadable-proxy",
      "initialHub": "hub-1",
      "offsetTiles": [
        14,
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-2",
      "role": "fictional-south-assigned-loadable-proxy",
      "initialHub": "hub-1",
      "offsetTiles": [
        16,
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-1",
      "role": "fictional-original-water-carrier",
      "initialHub": "hub-2",
      "offsetTiles": [
        -14,
        22
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-2",
      "role": "fictional-original-water-carrier",
      "initialHub": "hub-2",
      "offsetTiles": [
        -12,
        22
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
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-5",
      "hub": "hub-5",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-6",
      "hub": "hub-6",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.10-land-and-strait-logistics-chrysopolis.destination-7",
      "hub": "hub-7",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    }
  ],
  "objectGroups": {
    "auxiliaries": [
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-1",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-2",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-3",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-4",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-5",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-6",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-7",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-8",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-9",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-10"
    ],
    "north-loads": [
      "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-1",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-2"
    ],
    "south-loads": [
      "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-1",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-2"
    ],
    "ferries": [
      "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-1",
      "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-2"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-2",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-3",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-4",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-5",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-6",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-7",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-8",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-9",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.auxiliaries-10"
      ],
      "minimumAliveOrAlreadySafe": 8
    },
    {
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.north-loads-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    },
    {
      "entities": [
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-1",
        "imperial-church.10-land-and-strait-logistics-chrysopolis.south-loads-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Two European viewpoints / Dos miradores europeos

EN: Scout both marked viewpoints of two european viewpoints. Benefit: Mark the disclosed northern-local-water-loop once; neither capacity nor terrain changes.

ES: Explora los dos miradores señalados de dos miradores europeos. Ventaja: Señala una vez northern-local-water-loop ya indicado; no cambia capacidad ni terreno.

EN: Mark the northern fictional water loop without locating the emperor’s actual crossing.

ES: Señala el circuito acuático norteño ficticio sin localizar el cruce real del emperador.

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
          "10-land-and-strait-logistics-chrysopolis.side-1.zone-1",
          "10-land-and-strait-logistics-chrysopolis.side-1.zone-2"
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-1.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "10-land-and-strait-logistics-chrysopolis.side-1.zone-2",
        "hub": "hub-7",
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
      "target": "northern-local-water-loop fictional alternative",
      "resources": {},
      "onceFlag": "10-land-and-strait-logistics-chrysopolis.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "northern-local-water-loop"
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
    "receivingHub": "hub-7",
    "corridorIds": [
      "west-support"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Battle, surrender and church dispute / Batalla, rendición y disputa eclesial

EN: Recover both separate copies from battle, surrender and church dispute and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de batalla, rendición y disputa eclesial y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Optional attributed context separates the military result from agreement between churches.

ES: El contexto opcional atribuido separa el resultado militar del acuerdo entre iglesias.

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
          "10-land-and-strait-logistics-chrysopolis.side-2.entity-1",
          "10-land-and-strait-logistics-chrysopolis.side-2.entity-2"
        ],
        "destinations": {
          "10-land-and-strait-logistics-chrysopolis.side-2.entity-1": "10-land-and-strait-logistics-chrysopolis.side-2.zone-1",
          "10-land-and-strait-logistics-chrysopolis.side-2.entity-2": "10-land-and-strait-logistics-chrysopolis.side-2.zone-1"
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-2.entity-1",
        "role": "copy",
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-2.entity-2",
        "role": "copy",
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-2.zone-1",
        "hub": "hub-7",
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
      "onceFlag": "10-land-and-strait-logistics-chrysopolis.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.10-land-and-strait-logistics-chrysopolis"
      ],
      "historicalNote": {
        "en": "The final campaign against Licinius reached the Asian side of the Bosphorus after the fighting around Byzantium and the Hellespont. The usual chronology places the victory at Chrysopolis on 18 September 324. Zosimus describes crossings near a northern sacred promontory and fighting between it and Chalcedon; that narrative does not fix our local landing. The player operates a fictional two-shore supply service, not the emperor’s fleet or a theological war.",
        "es-ES": "La campaña final contra Licinio llegó a la orilla asiática del Bósforo tras los combates en torno a Bizancio y el Helesponto. La cronología habitual sitúa la victoria de Crisópolis el 18 de septiembre de 324. Zósimo describe cruces junto a un promontorio sagrado norteño y combates entre este y Calcedonia; ese relato no fija nuestro desembarque local. El jugador dirige un servicio ficticio de provisiones entre dos orillas, no la flota imperial ni una guerra teológica."
      },
      "hint": {
        "en": "Stage eight original auxiliaries and all four distinct assigned loads at European embarkation; pay the two150/100 and100/80 food/wood consignments once.",
        "es-ES": "Prepara ocho auxiliares originales y las cuatro cargas asignadas distintas en el embarque europeo; paga una vez las dos remesas de150/100 y100/80 de alimento/madera."
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
    "originHub": "hub-1",
    "receivingHub": "hub-7",
    "corridorIds": [
      "west-support"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### European waiting households / Hogares europeos en espera

EN: Bring each of the two aid crates to its assigned household at european waiting households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares europeos en espera. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Keep voluntary aid on its own bank; no household task consumes a unique main load.

ES: Mantén la ayuda voluntaria en su propia orilla; ninguna tarea doméstica consume una carga principal única.

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
          "10-land-and-strait-logistics-chrysopolis.side-3.entity-1",
          "10-land-and-strait-logistics-chrysopolis.side-3.entity-2"
        ],
        "destinations": {
          "10-land-and-strait-logistics-chrysopolis.side-3.entity-1": "10-land-and-strait-logistics-chrysopolis.side-3.zone-1",
          "10-land-and-strait-logistics-chrysopolis.side-3.entity-2": "10-land-and-strait-logistics-chrysopolis.side-3.zone-2"
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-3.entity-1",
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-3.entity-2",
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-3.zone-1",
        "hub": "hub-7",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "10-land-and-strait-logistics-chrysopolis.side-3.zone-2",
        "hub": "hub-7",
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
      "onceFlag": "10-land-and-strait-logistics-chrysopolis.side-3.rewarded",
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
    "receivingHub": "hub-7",
    "corridorIds": [
      "west-support"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The European supply shelter / El cobertizo europeo de provisiones

EN: Pay 50 wood and restore the damaged store of the european supply shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el cobertizo europeo de provisiones. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Restore a separate store for bounded ordinary stock, not ship resurrection or cargo fabrication.

ES: Restaura un almacén separado para existencias ordinarias limitadas, no para resucitar barcos ni fabricar cargas.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "10-land-and-strait-logistics-chrysopolis.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "10-land-and-strait-logistics-chrysopolis.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "10-land-and-strait-logistics-chrysopolis.side-4.payment",
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-4.entity-1",
        "role": "repair",
        "initialHub": "hub-1",
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-4.zone-1",
        "hub": "hub-7",
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
      "onceFlag": "10-land-and-strait-logistics-chrysopolis.side-4.rewarded",
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
    "receivingHub": "hub-7",
    "corridorIds": [
      "west-support"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### One hillside consignment / Una remesa en la ladera

EN: Escort the trader of one hillside consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de una remesa en la ladera hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Finite exchange remains local and never buys imperial submission or a bishop’s assent.

ES: El intercambio finito permanece local y no compra sumisión imperial ni asentimiento episcopal.

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
          "10-land-and-strait-logistics-chrysopolis.side-5.entity-1"
        ],
        "destinations": {
          "10-land-and-strait-logistics-chrysopolis.side-5.entity-1": "10-land-and-strait-logistics-chrysopolis.side-5.zone-1"
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
        "receipt": "10-land-and-strait-logistics-chrysopolis.side-5.payment",
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-5.entity-1",
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-5.zone-1",
        "hub": "hub-7",
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
      "onceFlag": "10-land-and-strait-logistics-chrysopolis.side-5.rewarded",
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
    "receivingHub": "hub-7",
    "corridorIds": [
      "west-support"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The European staging route / La ruta europea de preparación

EN: Escort the local guide of the european staging route to the marked road junction. Benefit: Mark the disclosed west-support once; neither capacity nor terrain changes.

ES: Escolta al guía local de la ruta europea de preparación hasta el cruce señalado. Ventaja: Señala una vez west-support ya indicado; no cambia capacidad ni terreno.

EN: Disclose the ordinary local preparation path independently of main water capacity.

ES: Señala el acceso ordinario local de preparación con independencia de la capacidad acuática principal.

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
          "10-land-and-strait-logistics-chrysopolis.side-6.entity-1"
        ],
        "destinations": {
          "10-land-and-strait-logistics-chrysopolis.side-6.entity-1": "10-land-and-strait-logistics-chrysopolis.side-6.zone-1"
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-6.entity-1",
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
        "id": "10-land-and-strait-logistics-chrysopolis.side-6.zone-1",
        "hub": "hub-7",
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
      "target": "west-support fictional alternative",
      "resources": {},
      "onceFlag": "10-land-and-strait-logistics-chrysopolis.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "west-support"
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
    "receivingHub": "hub-7",
    "corridorIds": [
      "west-support"
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
      "id": "scheduled-mixed-loads",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Choose water approaches and combine men/cargo within the shared slot cap; no speed or wind buff.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "consignment-first",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Send distinct north/south loads in separate batches while reserving the ordinary restoration budget.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "parallel-west-and-east-teams",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Leave independent west workers on optional aid/trade and stage auxiliaries east; two shores retain separate work allocation.",
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
      "food": 1368,
      "wood": 888,
      "gold": 204,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 250,
      "wood": 180,
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
      "food": 1320,
      "wood": 860,
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
    "difficultyLevers": "12 workers; two original four-slot ferries; both receivers, labels and water paths disclosed. No opponents or hidden deadline.",
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
      "food": 1420,
      "wood": 910,
      "gold": 215,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 250,
      "wood": 180,
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
      "food": 1320,
      "wood": 860,
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
    "difficultyLevers": "9 workers; same ferries, identities and consignment costs; schedule shared loads and inland deliveries.",
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
      "food": 1473,
      "wood": 933,
      "gold": 227,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 250,
      "wood": 180,
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
      "food": 1320,
      "wood": 860,
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
    "difficultyLevers": "6 workers and lower initial stock; same finite ferries, labels and auxiliary loss margin. Worker/ship scheduling and longer routes create opportunity cost; no harder invented war.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.title / always | none | Across the Bright Shore | Al otro lado de la costa luminosa |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.fact-intro / intro first | collection-narrator | The final campaign against Licinius reached the Asian side of the Bosphorus after the fighting around Byzantium and the Hellespont. The usual chronology places the victory at Chrysopolis on 18 September 324. Zosimus describes crossings near a northern sacred promontory and fighting between it and Chalcedon; that narrative does not fix our local landing. The player operates a fictional two-shore supply service, not the emperor’s fleet or a theological war. | La campaña final contra Licinio llegó a la orilla asiática del Bósforo tras los combates en torno a Bizancio y el Helesponto. La cronología habitual sitúa la victoria de Crisópolis el 18 de septiembre de 324. Zósimo describe cruces junto a un promontorio sagrado norteño y combates entre este y Calcedonia; ese relato no fija nuestro desembarque local. El jugador dirige un servicio ficticio de provisiones entre dos orillas, no la flota imperial ni una guerra teológica. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.persona-intro / after handover | imperial-clerk | On a page the two shores almost touch. I once drew a straight line and called it dispatch. A boatman asked whether my ink could row against the current. I inherited these earlier papers, but that question is mine. We will keep the shore receipts separate. | En una página las dos orillas casi se tocan. Una vez tracé una línea recta y la llamé despacho. Un barquero preguntó si mi tinta sabía remar contra la corriente. Estos papeles anteriores son heredados, pero esa pregunta es mía. Mantendremos separados los recibos de las orillas. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.route-help / available from start; repeatable without effect | none | Stage eight of ten original auxiliaries and all four original assigned supply loads at the European shore; pay 250 food and 180 wood, split into two labelled consignments of 150/100 and 100/80. The labels account for funding; load proxies do not claim a real carried resource inventory. Two original ferries share four slots each. Observe each original passenger’s crossing and unloading in the Asian landing sector. Then send the two north loads to the north receiver and the two south loads to the south receiver; eight actually crossed auxiliaries support the north court. Either local water path is available from the start. No hostile navy, invisible deadline or side reward is required. Stage all ten auxiliaries before the final readiness payment to allow two later auxiliary losses; if only eight are receipted, every one of those eight must survive. Crossing proofs start only after the complete readiness objective latches. | Prepara ocho de diez auxiliares originales y las cuatro cargas originales asignadas en la orilla europea; paga 250 de alimento y 180 de madera, divididos en dos remesas rotuladas de 150/100 y 100/80. Las etiquetas contabilizan financiación; las cargas representadas no afirman un inventario físico de recursos transportados. Dos embarcaciones originales comparten cuatro plazas cada una. Observa el cruce y desembarque de cada pasajero original en el sector asiático. Envía después las dos cargas norteñas al receptor norte y las dos sureñas al receptor sur; ocho auxiliares realmente cruzados apoyan el patio norteño. Ambas rutas acuáticas locales están disponibles desde el inicio. No necesitas enfrentarte a una armada hostil, plazo invisible ni recompensa secundaria. Prepara los diez auxiliares antes del último pago de preparación para permitir dos pérdidas auxiliares posteriores; si el recibo recoge solo ocho, deben sobrevivir los ocho. Las pruebas de cruce empiezan solo tras fijarse el objetivo completo de preparación. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o1-goal / phase-1 active | none | Stage eight original auxiliaries and all four distinct assigned loads at European embarkation; pay the two150/100 and100/80 food/wood consignments once. | Prepara ocho auxiliares originales y las cuatro cargas asignadas distintas en el embarque europeo; paga una vez las dos remesas de150/100 y100/80 de alimento/madera. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o1-receipt / o1 latched once | none | Distinct original shore identities and separately labelled funded consignments are ready. | Las identidades originales distintas de la orilla y las remesas financiadas con etiquetas separadas están preparadas. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o1-reaction / after o1 receipt | imperial-clerk | Two labels are worth more than an impressive total that tells no receiver what belongs to it. | Dos etiquetas valen más que un total impresionante que no dice a cada receptor qué le corresponde. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o2-goal / phase-2 active | none | Cross eight actually staged auxiliaries and both pairs of assigned original loads by manifest-backed ferry journeys to the Asian landing. | Cruza con ocho auxiliares realmente preparados y ambos pares de cargas originales asignadas mediante viajes en embarcación respaldados por manifiesto hasta el desembarque asiático. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o2-receipt / o2 latched once | none | Original boarded and unloaded identities have their own completed Asian-shore journey records. | Las identidades originales embarcadas y desembarcadas tienen sus propios registros completos de viaje a la orilla asiática. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o2-reaction / after o2 receipt | imperial-clerk | The ink line took one stroke. The ferry took several trips. I shall charge the ledger to reality. | La línea de tinta necesitó un trazo. La embarcación necesitó varios viajes. Ajustaré el registro a la realidad. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o3-goal / phase-3 active | none | Deliver both original north loads and eight actually crossed original auxiliaries to the northeastern inland court. | Entrega ambas cargas norteñas originales y ocho auxiliares originales realmente cruzados en el patio interior nororiental. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o3-receipt / o3 latched once | none | The north court has its own assigned pair and original auxiliary support. | El patio norteño tiene su propio par asignado y apoyo auxiliar original. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o3-reaction / after o3 receipt | imperial-clerk | One book is complete. That is no excuse to close the other one. | Un libro está completo. Eso no justifica cerrar el otro. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o4-goal / phase-4 active | none | Deliver both original south loads to their southeastern inland receiver. | Entrega ambas cargas sureñas originales en su receptor interior suroriental. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o4-receipt / o4 latched once | none | The separate south consignment reached its own receiver, without replacement by northern deliveries. | La remesa sureña separada llegó a su propio receptor, sin sustituirla por entregas norteñas. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.o4-reaction / after o4 receipt | imperial-clerk | I can finish this column. I cannot finish a city’s argument with it. | Puedo terminar esta columna. No puedo terminar con ella la disputa de una ciudad. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of two european viewpoints. Benefit: Mark the disclosed northern-local-water-loop once; neither capacity nor terrain changes. | Explora los dos miradores señalados de dos miradores europeos. Ventaja: Señala una vez northern-local-water-loop ya indicado; no cambia capacidad ni terreno. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-1-complete / side-1 completed | none | Two European viewpoints completed. Its stated benefit has been granted once. | Dos miradores europeos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-1-lost / side-1 failed-optional | none | Two European viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Dos miradores europeos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from battle, surrender and church dispute and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de batalla, rendición y disputa eclesial y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-2-complete / side-2 completed | none | Battle, surrender and church dispute completed. Its stated benefit has been granted once. | Batalla, rendición y disputa eclesial: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-2-lost / side-2 failed-optional | none | Battle, surrender and church dispute is unavailable after the loss of its unique participant or object. The main mission continues. | Batalla, rendición y disputa eclesial: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at european waiting households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares europeos en espera. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-3-complete / side-3 completed | none | European waiting households completed. Its stated benefit has been granted once. | Hogares europeos en espera: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-3-lost / side-3 failed-optional | none | European waiting households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares europeos en espera: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the european supply shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el cobertizo europeo de provisiones. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-4-complete / side-4 completed | none | The European supply shelter completed. Its stated benefit has been granted once. | El cobertizo europeo de provisiones: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-4-lost / side-4 failed-optional | none | The European supply shelter is unavailable after the loss of its unique participant or object. The main mission continues. | El cobertizo europeo de provisiones: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-5-goal / optional list from start | none | Escort the trader of one hillside consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de una remesa en la ladera hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-5-complete / side-5 completed | none | One hillside consignment completed. Its stated benefit has been granted once. | Una remesa en la ladera: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-5-lost / side-5 failed-optional | none | One hillside consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Una remesa en la ladera: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the european staging route to the marked road junction. Benefit: Mark the disclosed west-support once; neither capacity nor terrain changes. | Escolta al guía local de la ruta europea de preparación hasta el cruce señalado. Ventaja: Señala una vez west-support ya indicado; no cambia capacidad ni terreno. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-6-complete / side-6 completed | none | The European staging route completed. Its stated benefit has been granted once. | La ruta europea de preparación: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.side-6-lost / side-6 failed-optional | none | The European staging route is unavailable after the loss of its unique participant or object. The main mission continues. | La ruta europea de preparación: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.fact-outro / victory first | collection-narrator | The fictional two-shore service delivered its original people and four assigned loads. Historical accounts place Licinius’ defeat and later surrender in the final 324 sequence; neither the service nor a clerk’s paperwork caused sole imperial rule. Church disputes did not end with the battle. | El servicio ficticio entre dos orillas entregó a sus personas originales y cuatro cargas asignadas. Los relatos históricos sitúan la derrota de Licinio y su posterior rendición en la secuencia final de 324; ni el servicio ni los papeles de un funcionario causaron el gobierno imperial único. Las disputas eclesiales no terminaron con la batalla. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.persona-outro / after fact-outro | imperial-clerk | Two receiving books, four loads, no shore rubbed out to make the arithmetic easier. The next papers ask for concord. I know how to send a notice across water; I have never found agreement waiting in the hold. | Dos libros de recepción, cuatro cargas, ninguna orilla borrada para facilitar la cuenta. Los papeles siguientes piden concordia. Sé enviar un aviso a través del agua; nunca he encontrado acuerdo esperando en la bodega. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.defeat / main defeat; close side rewards first | none | The required number of actually ready or actually crossed original auxiliaries is no longer available, an indispensable original load is lost, or both original ferries are lost before every required crossing finishes. Boarded passengers are lost with their destroyed carrier; disembarked passengers survive independently. Optional losses alone never defeat the main mission. | Ya no queda el número requerido de auxiliares originales realmente preparados o realmente cruzados, se pierde una carga original indispensable, o se pierden ambas embarcaciones originales antes de terminar todos los cruces requeridos. Los pasajeros embarcados se pierden con su embarcación destruida; quienes desembarcaron sobreviven por separado. Las pérdidas opcionales por sí solas nunca derrotan la misión principal. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.10-land-and-strait-logistics-chrysopolis.odyssey.next-episode / after persona-outro | none | Continue with Words over Alexandria. This episode does not complete the campaign. | Continúa con Palabras sobre Alejandría. Este episodio no termina la campaña. |

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
    "recoveryImplementation": "inventory/replacement capability pending; reserved resources alone cannot resurrect an identity",
    "transportLoss": "destroyed carrier loses every currently boarded passenger; disembarked passengers survive independently",
    "carrierLoss": "one remaining original ferry can complete every main trip without optional goals; loss of both before all main crossings finish defeats the mission",
    "eligibleAuxiliaryLoss": "after readiness latch, fewer than required actually receipted auxiliaries alive or already completed causes defeat; after crossing latch use the actual crossed ledger; unstaged or uncrossed originals never fill an eligibility deficit"
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
    },
    {
      "id": "manifest-backed-water-journeys",
      "status": "design-only-unimplemented; typed reference, shared manifests, physical observers and native save/load QA pending"
    }
  ],
  "transportPlan": {
    "implementationStatus": "design-only-unimplemented",
    "sharedManifestAuthority": true,
    "cargoPolicy": "identified loadable proxies; no resource inventory claim",
    "lossPolicy": "destroyed carrier loses every currently boarded passenger; disembarked passengers survive independently",
    "placementGate": "real water-spawn and shore boarding/disembark zones require dated-bank, DEM and in-game pathfinding certification; district centres are not native boat coordinates",
    "operatingPolicy": "two original carriers share one capacity ledger, four passenger slots each; repeated trips allowed; a passenger reserves one slot until disembark or loss; no teleport, free replacement, timer completion or paid-resource inventory inside a chest",
    "emptyCarrierLoss": "one remaining original ferry can complete every main trip without optional goals; loss of both before all main crossings finish defeats the mission",
    "concurrency": "boarding, departure, arrival, unloading and loss are atomic per carrier; requirements share manifests rather than separately granting capacity",
    "eligibilityLossPolicy": "after readiness latch, fewer than required actually receipted auxiliaries alive or already completed causes defeat; after crossing latch use the actual crossed ledger; unstaged or uncrossed originals never fill an eligibility deficit",
    "capacityByCarrier": {
      "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-1": 4,
      "imperial-church.10-land-and-strait-logistics-chrysopolis.ferries-2": 4
    }
  },
  "artDirection": {
    "style": "restrained late Roman riverbank or strait logistics, readable shore labels and ordinary people",
    "historicalControls": "no surveyed tactical crossing, modern bridge, Ottoman mosque or later harbor/palace; local boats and load quantities are dramatization",
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "north and south consignments have distinct original load IDs and funding receipts",
      "a north delivery cannot satisfy a south receiver or duplicate its payment",
      "all passenger requirements share the same two-carrier capacity authority",
      "a geometric shore arrival or timer does not fulfill a water journey",
      "actual observed readiness limits every counted passenger, with per-identity save receipts",
      "one remaining original ferry can finish without optional aid after the other is lost empty",
      "all optional tasks remain on the European bank; no default land route crosses the Bosphorus",
      "no local crossing portrayed as Zosimus’s northern military itinerary",
      "no modern filled harbor or medieval palace accepted as324 terrain",
      "readiness payment last: stage all10 before latch permits2 auxiliary losses; stage only8 means no receipted auxiliary loss can be absorbed",
      "a live but unreceipted original never replaces a dead staged passenger; defeat is raised when the eligible threshold becomes irrecoverable",
      "boarding/proof cannot precede complete readiness objective latch including all funded receipts",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
