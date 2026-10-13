# 8. The Maritsa Crossing

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `09-crossing-and-supply-adrianople` · 3 July 324 CE, conventional · 400×400

## Historical frame and fixed outcome

EN: Constantine defeated Licinius near Adrianople in the Hebrus region in 324. The usual date is 3 July. Zosimus gives a later, hostile account of a river crossing and retreat; it does not locate a surveyed ford. Our smaller auxiliary ferry convoy is fiction beside that campaign. It does not command the imperial battle or turn the later Bithynian victory into this one.

ES: Constantino derrotó a Licinio junto a Adriánopolis, en la región del Hebro, en 324. La fecha habitual es el 3 de julio. Zósimo ofrece un relato tardío y hostil de un cruce y una retirada; no identifica un vado prospectado. Nuestro pequeño convoy auxiliar en embarcaciones es ficticio y se sitúa junto a esa campaña. No dirige la batalla imperial ni la confunde con la victoria posterior en Bitinia.

EN: The fictional convoy crossed with observed manifests and reached its local inland assembly. The reported imperial victory remains historical context; this small success neither measures the ancient armies nor identifies Constantine’s crossing. The operations toward Byzantium and the Asian shore follow separately.

ES: El convoy ficticio cruzó con manifiestos observados y alcanzó su punto local de reunión interior. La victoria imperial referida sigue siendo contexto histórico; este pequeño éxito no mide los ejércitos antiguos ni identifica el paso de Constantino. Las operaciones hacia Bizancio y la orilla asiática continúan por separado.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "Constantine defeated Licinius in the Adrianople/Hebrus region before the later Bithynian operations;3July324 is conventional chronology, not dated in the displayed Zosimus account.",
        "es-ES": "Constantino derrotó a Licinio en la región de Adriánopolis/Hebro antes de las operaciones bitinias posteriores; el3de julio de324 es cronología convencional, no fecha indicada en el relato mostrado de Zósimo."
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
      "limitations": "Date and military detail remain unverified in this audit; should retain as conventional only with a better source.",
      "status": "unavailable",
      "supportedClaim": "The checked material does not establish Adrianople on 3 July or distinguish this battle from Chrysopolis. / El material consultado no establece Adrianópolis el 3 de julio ni separa esa batalla de Crisópolis.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "No exact battle locator found.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.tertullian.org/fathers/zosimus02_book2.htm",
      "passage": "New History II; printed47–48 Adrianople/Hebrus crossing and retreat",
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
      "consultedUrl": "https://dergipark.org.tr/en/download/article-file/6126842",
      "passage": "Yildirim2015; abstract and opening pp181–183; regional map figure1 onPDFpage2",
      "coverageActuallyRead": "Architect read English/Turkish abstract and opening regional/river discussion, inspected the reproduced historical-map figure.",
      "limitations": "Not full24-page archaeological analysis read; medieval/modern city plans elsewhere not adopted as324 footprint. Exact ford and ancient channels unverified.",
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

EN: Stage eight original auxiliaries and all four collected original chests at lower embarkation; pay 300 food and 120 wood once.

ES: Prepara ocho auxiliares originales y los cuatro cofres originales recogidos en el embarque inferior; paga una vez 300 de alimento y 120 de madera.

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
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-1",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-3",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-5",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-6",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-7",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-8",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-9",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-10"
      ],
      "destinations": {
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-1": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-2": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-3": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-4": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-5": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-6": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-7": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-8": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-9": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-10": "imperial-church.09-crossing-and-supply-adrianople.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-1",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-2",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-3",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-4"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-1",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-2",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-3",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-4"
      ],
      "destinations": {
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-1": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-2": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-3": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-4": "imperial-church.09-crossing-and-supply-adrianople.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 300,
        "wood": 120
      },
      "id": "req-4",
      "receivingZones": [
        "imperial-church.09-crossing-and-supply-adrianople.destination-2"
      ],
      "allocations": {
        "imperial-church.09-crossing-and-supply-adrianople.destination-2": {
          "food": 300,
          "wood": 120
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.09-crossing-and-supply-adrianople.o1.req-4.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Readiness records identify the actual originals staged at the southwest shore.

ES: Los recibos de preparación identifican los originales realmente preparados en la orilla suroccidental.

EN: There is no passenger yet in the crossing column. A supply payment is not a ferry trip.

ES: Aún no hay pasajeros en la columna de cruces. Pagar provisiones no es viajar en embarcación.

### o2 / phase-2

EN: Use the two original four-slot ferries to cross eight actually staged auxiliaries and all four chests, with individual manifest-backed unloading at the opposite landing.

ES: Usa las dos embarcaciones originales de cuatro plazas para cruzar con ocho auxiliares realmente preparados y los cuatro cofres, con desembarque individual respaldado por manifiesto.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "transport-journey",
      "requiredCount": 8,
      "allowedCorridorIds": [
        "lower-ferry",
        "upper-water-detour"
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
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-1",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-3",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-5",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-6",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-7",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-8",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-9",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-10"
      ],
      "carriers": [
        "imperial-church.09-crossing-and-supply-adrianople.ferries-1",
        "imperial-church.09-crossing-and-supply-adrianople.ferries-2"
      ],
      "originZone": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
      "destinationZone": "imperial-church.09-crossing-and-supply-adrianople.destination-3"
    },
    {
      "kind": "transport-journey",
      "requiredCount": 4,
      "allowedCorridorIds": [
        "lower-ferry",
        "upper-water-detour"
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
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-1",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-2",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-3",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-4"
      ],
      "carriers": [
        "imperial-church.09-crossing-and-supply-adrianople.ferries-1",
        "imperial-church.09-crossing-and-supply-adrianople.ferries-2"
      ],
      "originZone": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
      "destinationZone": "imperial-church.09-crossing-and-supply-adrianople.destination-3"
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

EN: Original passenger journeys are complete; every counted identity boarded and disembarked through its own scoped manifest.

ES: Los viajes originales están completos; cada identidad contada embarcó y desembarcó mediante su propio manifiesto específico.

EN: A boat can carry four passengers. Two clerks cannot give it eight by keeping separate books.

ES: Una embarcación lleva cuatro pasajeros. Dos escribientes no pueden darle ocho llevando libros separados.

### o3 / phase-3

EN: Bring at least eight actually crossed original auxiliaries and all four original chests to the local inland assembly.

ES: Lleva al menos ocho auxiliares originales realmente cruzados y los cuatro cofres originales a la reunión local interior.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 8,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o2",
        "ledger": "auxiliaries-crossed"
      },
      "id": "req-1",
      "entities": [
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-1",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-3",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-5",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-6",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-7",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-8",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-9",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-10"
      ],
      "destinations": {
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-1": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-2": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-3": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-4": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-5": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-6": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-7": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-8": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-9": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-10": "imperial-church.09-crossing-and-supply-adrianople.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-1",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-2",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-3",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-4"
      ],
      "destinations": {
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-1": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-2": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-3": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-4": "imperial-church.09-crossing-and-supply-adrianople.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The surviving original convoy reached inland assembly after its observed water crossings.

ES: El convoy original superviviente llegó a la reunión interior tras sus cruces de agua observados.

EN: That longer path may save a shorter list of condolences. I will leave the choice to the escort.

ES: Ese camino más largo puede ahorrar una lista más corta de pésames. Dejaré la elección a la escolta.

## Finite opposition and authored engagement constraints

```json
{
  "historicalPolicy": "fictional local screen and skirmish pocket, not a mapped ancient battlefield or army strengths",
  "worldSelectionPolicy": "only selected initial identities exist; maximum unused group identities are absent",
  "engagementPolicy": "all selected opponents confined to a narrow disclosed short east-approach pocket near the inland assembly, outside the receiving zone itself; longer east detour, landing, river and all western optional branches remain outside leashes. Exact footprints and combat calibration pending; no navy, waves, production or roaming attack on the only boat.",
  "byDifficulty": {
    "easy": {
      "productionEnabled": false,
      "mobilizations": [],
      "initialEntityIds": [
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-1",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-2",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-3",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-4",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-5",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-6",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-7",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-8",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-9",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-10",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-11",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-12"
      ]
    },
    "standard": {
      "productionEnabled": false,
      "mobilizations": [],
      "initialEntityIds": [
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-1",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-2",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-3",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-4",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-5",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-6",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-7",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-8",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-9",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-10",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-11",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-12",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-13",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-14",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-15",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-16",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-17",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-18",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-19",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-20"
      ]
    },
    "hard": {
      "productionEnabled": false,
      "mobilizations": [],
      "initialEntityIds": [
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-1",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-2",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-3",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-4",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-5",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-6",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-7",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-8",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-9",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-10",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-11",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-12",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-13",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-14",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-15",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-16",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-17",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-18",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-19",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-20",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-21",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-22",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-23",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-24",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-25",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-26",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-27",
        "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-28"
      ]
    }
  }
}
```

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/09-crossing-and-supply-adrianople.svg)

```json
{
  "bbox": [
    26.5,
    41.6,
    26.645,
    41.685
  ],
  "terrainProfile": "adrianople",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        95.08,
        260.32
      ],
      "lonLat": [
        26.53,
        41.624
      ],
      "name": {
        "en": "Southwestern fictional convoy work court",
        "es-ES": "Patio ficticio suroccidental del convoy"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        232.67,
        263.61
      ],
      "lonLat": [
        26.586,
        41.623
      ],
      "name": {
        "en": "Lower southwest-bank embarkation district",
        "es-ES": "Sector de embarque inferior en la orilla suroccidental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        286.72,
        230.73
      ],
      "lonLat": [
        26.608,
        41.633
      ],
      "name": {
        "en": "Lower northeast-bank landing district",
        "es-ES": "Sector de desembarque inferior en la orilla nororiental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        328.49,
        132.1
      ],
      "lonLat": [
        26.625,
        41.663
      ],
      "name": {
        "en": "Northeastern local inland assembly",
        "es-ES": "Reunión local interior nororiental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        178.62,
        230.73
      ],
      "lonLat": [
        26.564,
        41.633
      ],
      "name": {
        "en": "Upper southwest-bank approach district",
        "es-ES": "Sector superior de acceso suroccidental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-6",
      "centre": [
        222.84,
        158.4
      ],
      "lonLat": [
        26.582,
        41.655
      ],
      "name": {
        "en": "Upper northeast-bank approach district",
        "es-ES": "Sector superior de acceso nororiental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "west-preparation",
      "hubOrder": [
        "hub-1",
        "hub-5",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "lower-ferry",
      "hubOrder": [
        "hub-2",
        "hub-3"
      ],
      "mode": "water",
      "widthTiles": 12
    },
    {
      "id": "upper-water-detour",
      "hubOrder": [
        "hub-2",
        "hub-5",
        "hub-6",
        "hub-3"
      ],
      "mode": "water",
      "widthTiles": 10
    },
    {
      "id": "east-short-assembly",
      "hubOrder": [
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-land-detour",
      "hubOrder": [
        "hub-3",
        "hub-6",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 8
    }
  ],
  "terrainInstructions": "Adrianople/Hadrianopolis lowland and the Hebrus/Maritsa/Meric reach downstream of the tributary convergence. Southwest-bank preparation and northeast-bank receiving circuits are fictional and are not Licinius/Constantine deployments. The modern generalized Evros river line is downloaded Natural Earth data, not the 324 channel. Tunca and Arda minor reaches are not resolved in that layer: obtain dated confluence/bank evidence before native placement; do not invent straight water barriers or identify a modern bridge as the ford. Proposed ferries are local dramatization, not Zosimus’s reported tactical crossing. No Selimiye mosque, Ottoman bridges, railway or literal modern road grid; no 378 Valens battle. Actual shores, crossing length, floodplain relief and enemy leash footprints remain unapproved.",
  "corridorStraightLengthsTiles": {
    "west-preparation": 151.89,
    "lower-ferry": 63.27,
    "upper-water-detour": 244.54,
    "east-short-assembly": 107.11,
    "east-land-detour": 205.37
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
        26.459972,
        41.679023
      ],
      [
        26.475678,
        41.675971
      ],
      [
        26.491954,
        41.681016
      ],
      [
        26.491466,
        41.674018
      ],
      [
        26.493663,
        41.670844
      ],
      [
        26.497081,
        41.669379
      ],
      [
        26.499441,
        41.667344
      ],
      [
        26.534272,
        41.666571
      ],
      [
        26.560802,
        41.654812
      ],
      [
        26.580496,
        41.635688
      ],
      [
        26.5949,
        41.612738
      ],
      [
        26.594737,
        41.605251
      ],
      [
        26.595795,
        41.597846
      ],
      [
        26.598155,
        41.591091
      ]
    ],
    "certainty": "modern generalizedEvros/Maritsa line selected without editing vertices from downloadedNaturalEarth10m snapshot; no324 channel or ford inferred",
    "renderAs": "modern-river-line"
  },
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/imperial-church/odyssey/09-crossing-and-supply-adrianople.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-1",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-2",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-3",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-4",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-5",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-6",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-7",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-8",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-9",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-10",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.supply-chests-1",
      "role": "fictional-loadable-chest-proxy",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.supply-chests-2",
      "role": "fictional-loadable-chest-proxy",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.supply-chests-3",
      "role": "fictional-loadable-chest-proxy",
      "initialHub": "hub-1",
      "offsetTiles": [
        4,
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.supply-chests-4",
      "role": "fictional-loadable-chest-proxy",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ferries-1",
      "role": "fictional-original-water-carrier",
      "initialHub": "hub-2",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ferries-2",
      "role": "fictional-original-water-carrier",
      "initialHub": "hub-2",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-1",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-2",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
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
    },
    {
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-3",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -10,
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-4",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -8,
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-5",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -14,
        24
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-6",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -12,
        24
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-7",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -10,
        24
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-8",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -8,
        24
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-9",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -14,
        26
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-10",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -12,
        26
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-11",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -10,
        26
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-12",
      "role": "fictional-ordinary-friendly-screen",
      "initialHub": "hub-3",
      "offsetTiles": [
        -8,
        26
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-1",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -26,
        -16
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-2",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -24,
        -16
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-3",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -22,
        -16
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-4",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -20,
        -16
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-5",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -26,
        -14
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-6",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -24,
        -14
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-7",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -22,
        -14
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-8",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -20,
        -14
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-9",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -26,
        -12
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-10",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -24,
        -12
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-11",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -22,
        -12
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-12",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -20,
        -12
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-13",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -26,
        -10
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-14",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -24,
        -10
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-15",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -22,
        -10
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-16",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -20,
        -10
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-17",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -26,
        -8
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-18",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -24,
        -8
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-19",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -22,
        -8
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-20",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -20,
        -8
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-21",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -26,
        -6
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-22",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -24,
        -6
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-23",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -22,
        -6
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-24",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -20,
        -6
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-25",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -26,
        -4
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-26",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -24,
        -4
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-27",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -22,
        -4
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-28",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-4",
      "offsetTiles": [
        -20,
        -4
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
      "id": "imperial-church.09-crossing-and-supply-adrianople.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.09-crossing-and-supply-adrianople.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.09-crossing-and-supply-adrianople.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.09-crossing-and-supply-adrianople.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.09-crossing-and-supply-adrianople.destination-5",
      "hub": "hub-5",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.09-crossing-and-supply-adrianople.destination-6",
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
    "auxiliaries": [
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-1",
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-2",
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-3",
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-4",
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-5",
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-6",
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-7",
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-8",
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-9",
      "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-10"
    ],
    "supply-chests": [
      "imperial-church.09-crossing-and-supply-adrianople.supply-chests-1",
      "imperial-church.09-crossing-and-supply-adrianople.supply-chests-2",
      "imperial-church.09-crossing-and-supply-adrianople.supply-chests-3",
      "imperial-church.09-crossing-and-supply-adrianople.supply-chests-4"
    ],
    "ferries": [
      "imperial-church.09-crossing-and-supply-adrianople.ferries-1",
      "imperial-church.09-crossing-and-supply-adrianople.ferries-2"
    ],
    "ordinary-screen": [
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-1",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-2",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-3",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-4",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-5",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-6",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-7",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-8",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-9",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-10",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-11",
      "imperial-church.09-crossing-and-supply-adrianople.ordinary-screen-12"
    ],
    "east-hostile-pocket": [
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-1",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-2",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-3",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-4",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-5",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-6",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-7",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-8",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-9",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-10",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-11",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-12",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-13",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-14",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-15",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-16",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-17",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-18",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-19",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-20",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-21",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-22",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-23",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-24",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-25",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-26",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-27",
      "imperial-church.09-crossing-and-supply-adrianople.east-hostile-pocket-28"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-1",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-2",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-3",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-4",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-5",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-6",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-7",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-8",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-9",
        "imperial-church.09-crossing-and-supply-adrianople.auxiliaries-10"
      ],
      "minimumAliveOrAlreadySafe": 8
    },
    {
      "entities": [
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-1",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-2",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-3",
        "imperial-church.09-crossing-and-supply-adrianople.supply-chests-4"
      ],
      "minimumAliveOrAlreadySafe": 4
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Both western approaches / Los dos accesos occidentales

EN: Scout both marked viewpoints of both western approaches. Benefit: Mark the disclosed upper-water-detour once; neither capacity nor terrain changes.

ES: Explora los dos miradores señalados de los dos accesos occidentales. Ventaja: Señala una vez upper-water-detour ya indicado; no cambia capacidad ni terreno.

EN: Mark preparation districts and the proposed river detour without claiming a historical ford.

ES: Señala sectores de preparación y el desvío fluvial propuesto sin afirmar un vado histórico.

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
          "09-crossing-and-supply-adrianople.side-1.zone-1",
          "09-crossing-and-supply-adrianople.side-1.zone-2"
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
        "id": "09-crossing-and-supply-adrianople.side-1.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "09-crossing-and-supply-adrianople.side-1.zone-2",
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
      "target": "upper-water-detour fictional alternative",
      "resources": {},
      "onceFlag": "09-crossing-and-supply-adrianople.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "upper-water-detour"
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
      "west-preparation"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A crossing without a surveyed ford / Un cruce sin vado prospectado

EN: Recover both separate copies from a crossing without a surveyed ford and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de un cruce sin vado prospectado y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Keep the later literary narrative separate from the fictional ferry ledger.

ES: Separa el relato literario tardío del registro ficticio de embarcaciones.

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
          "09-crossing-and-supply-adrianople.side-2.entity-1",
          "09-crossing-and-supply-adrianople.side-2.entity-2"
        ],
        "destinations": {
          "09-crossing-and-supply-adrianople.side-2.entity-1": "09-crossing-and-supply-adrianople.side-2.zone-1",
          "09-crossing-and-supply-adrianople.side-2.entity-2": "09-crossing-and-supply-adrianople.side-2.zone-1"
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
        "id": "09-crossing-and-supply-adrianople.side-2.entity-1",
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
        "id": "09-crossing-and-supply-adrianople.side-2.entity-2",
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
        "id": "09-crossing-and-supply-adrianople.side-2.zone-1",
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
      "kind": "unlock-context-and-hint",
      "target": "documented context and a main-goal hint",
      "resources": {},
      "onceFlag": "09-crossing-and-supply-adrianople.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.09-crossing-and-supply-adrianople"
      ],
      "historicalNote": {
        "en": "Constantine defeated Licinius near Adrianople in the Hebrus region in 324. The usual date is 3 July. Zosimus gives a later, hostile account of a river crossing and retreat; it does not locate a surveyed ford. Our smaller auxiliary ferry convoy is fiction beside that campaign. It does not command the imperial battle or turn the later Bithynian victory into this one.",
        "es-ES": "Constantino derrotó a Licinio junto a Adriánopolis, en la región del Hebro, en 324. La fecha habitual es el 3 de julio. Zósimo ofrece un relato tardío y hostil de un cruce y una retirada; no identifica un vado prospectado. Nuestro pequeño convoy auxiliar en embarcaciones es ficticio y se sitúa junto a esa campaña. No dirige la batalla imperial ni la confunde con la victoria posterior en Bitinia."
      },
      "hint": {
        "en": "Stage eight original auxiliaries and all four collected original chests at lower embarkation; pay 300 food and 120 wood once.",
        "es-ES": "Prepara ocho auxiliares originales y los cuatro cofres originales recogidos en el embarque inferior; paga una vez 300 de alimento y 120 de madera."
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
    "receivingHub": "hub-5",
    "corridorIds": [
      "west-preparation"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Households on the waiting bank / Hogares en la orilla de espera

EN: Bring each of the two aid crates to its assigned household at households on the waiting bank. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares en la orilla de espera. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Independent voluntary aid remains on the southwest bank and does not replace mandatory chests.

ES: La ayuda voluntaria independiente permanece en la orilla suroccidental y no sustituye cofres obligatorios.

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
          "09-crossing-and-supply-adrianople.side-3.entity-1",
          "09-crossing-and-supply-adrianople.side-3.entity-2"
        ],
        "destinations": {
          "09-crossing-and-supply-adrianople.side-3.entity-1": "09-crossing-and-supply-adrianople.side-3.zone-1",
          "09-crossing-and-supply-adrianople.side-3.entity-2": "09-crossing-and-supply-adrianople.side-3.zone-2"
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
        "id": "09-crossing-and-supply-adrianople.side-3.entity-1",
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
        "id": "09-crossing-and-supply-adrianople.side-3.entity-2",
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
        "id": "09-crossing-and-supply-adrianople.side-3.zone-1",
        "hub": "hub-5",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "09-crossing-and-supply-adrianople.side-3.zone-2",
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
        "food": 100,
        "wood": 50
      },
      "onceFlag": "09-crossing-and-supply-adrianople.side-3.rewarded",
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
    "receivingHub": "hub-5",
    "corridorIds": [
      "west-preparation"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The western loading shelter / El cobertizo occidental de carga

EN: Pay 50 wood and restore the damaged store of the western loading shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el cobertizo occidental de carga. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair a separate store for bounded supplies, never restore a destroyed carrier or boarded passenger.

ES: Repara un almacén separado para provisiones limitadas; no restaura embarcaciones destruidas ni pasajeros embarcados.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "09-crossing-and-supply-adrianople.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "09-crossing-and-supply-adrianople.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "09-crossing-and-supply-adrianople.side-4.payment",
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
        "id": "09-crossing-and-supply-adrianople.side-4.entity-1",
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
        "id": "09-crossing-and-supply-adrianople.side-4.zone-1",
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
        "food": 200,
        "wood": 100
      },
      "onceFlag": "09-crossing-and-supply-adrianople.side-4.rewarded",
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
    "receivingHub": "hub-5",
    "corridorIds": [
      "west-preparation"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### One waiting-bank consignment / Una remesa en la orilla de espera

EN: Escort the trader of one waiting-bank consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de una remesa en la orilla de espera hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Finite ordinary exchange does not buy a new unique boat.

ES: El intercambio ordinario finito no compra una embarcación única nueva.

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
          "09-crossing-and-supply-adrianople.side-5.entity-1"
        ],
        "destinations": {
          "09-crossing-and-supply-adrianople.side-5.entity-1": "09-crossing-and-supply-adrianople.side-5.zone-1"
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
        "receipt": "09-crossing-and-supply-adrianople.side-5.payment",
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
        "id": "09-crossing-and-supply-adrianople.side-5.entity-1",
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
        "id": "09-crossing-and-supply-adrianople.side-5.zone-1",
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
      "onceFlag": "09-crossing-and-supply-adrianople.side-5.rewarded",
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
    "receivingHub": "hub-5",
    "corridorIds": [
      "west-preparation"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The western staging circuit / El circuito occidental de preparación

EN: Escort the local guide of the western staging circuit to the marked road junction. Benefit: Mark the disclosed west-preparation once; neither capacity nor terrain changes.

ES: Escolta al guía local de el circuito occidental de preparación hasta el cruce señalado. Ventaja: Señala una vez west-preparation ya indicado; no cambia capacidad ni terreno.

EN: Mark an ordinary preparation approach; all essential endpoints are disclosed independently.

ES: Señala un acceso ordinario de preparación; todos los extremos esenciales se indican por separado.

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
          "09-crossing-and-supply-adrianople.side-6.entity-1"
        ],
        "destinations": {
          "09-crossing-and-supply-adrianople.side-6.entity-1": "09-crossing-and-supply-adrianople.side-6.zone-1"
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
        "id": "09-crossing-and-supply-adrianople.side-6.entity-1",
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
        "id": "09-crossing-and-supply-adrianople.side-6.zone-1",
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
      "target": "west-preparation fictional alternative",
      "resources": {},
      "onceFlag": "09-crossing-and-supply-adrianople.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "west-preparation"
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
      "west-preparation"
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
      "id": "ferry-first-and-land-detour",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Move chests in protected batches and use the longer northeast-bank land detour; extra sailing is optional.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "concentrated-east-screen",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Use the initial friendly screen on the shorter east approach while preserving ferry passengers; exact combat and leash calibration pending.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "waiting-bank-support",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Keep a separate west-bank aid/trade team while one or both ferries repeat main trips; bounded time and worker opportunity cost.",
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
      "food": 575,
      "wood": 287,
      "gold": 172,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1925,
      "wood": 1133,
      "gold": 528,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 120,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 400,
      "wood": 300,
      "gold": 200,
      "stone": 0
    },
    "replacementBudget": {
      "food": 700,
      "wood": 400,
      "gold": 350,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 2050,
      "wood": 1220,
      "gold": 700,
      "stone": 100
    },
    "maxVillagers": 12,
    "enemyTotalCap": 12,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      30,
      55
    ],
    "difficultyLevers": "12 workers and 12 selected east-land opponents;12 friendly screen, two four-slot ferries and at most2 auxiliary losses if all10 were readied. Main shores and both land choices disclosed.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  },
  "standard": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 500,
      "wood": 250,
      "gold": 150,
      "stone": 0
    },
    "gatherableBank": {
      "food": 2000,
      "wood": 1170,
      "gold": 550,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 120,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 400,
      "wood": 300,
      "gold": 200,
      "stone": 0
    },
    "replacementBudget": {
      "food": 700,
      "wood": 400,
      "gold": 350,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 2050,
      "wood": 1220,
      "gold": 700,
      "stone": 100
    },
    "maxVillagers": 9,
    "enemyTotalCap": 20,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      35,
      65
    ],
    "difficultyLevers": "9 workers and 20 selected east-land opponents; same screen/ferries/loss margin. Divide collection, sailing and optional west work.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  },
  "hard": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 425,
      "wood": 212,
      "gold": 127,
      "stone": 0
    },
    "gatherableBank": {
      "food": 2075,
      "wood": 1208,
      "gold": 573,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 120,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 400,
      "wood": 300,
      "gold": 200,
      "stone": 0
    },
    "replacementBudget": {
      "food": 700,
      "wood": 400,
      "gold": 350,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 2050,
      "wood": 1220,
      "gold": 700,
      "stone": 100
    },
    "maxVillagers": 6,
    "enemyTotalCap": 28,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      40,
      75
    ],
    "difficultyLevers": "6 workers and 28 selected east-land opponents; same finite boats and screen, lower initial stock. East detour must remain viable without combat or side goals after native leash/path audit.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.title / always | none | The Maritsa Crossing | El paso del Maritsa |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.fact-intro / intro first | collection-narrator | Constantine defeated Licinius near Adrianople in the Hebrus region in 324. The usual date is 3 July. Zosimus gives a later, hostile account of a river crossing and retreat; it does not locate a surveyed ford. Our smaller auxiliary ferry convoy is fiction beside that campaign. It does not command the imperial battle or turn the later Bithynian victory into this one. | Constantino derrotó a Licinio junto a Adriánopolis, en la región del Hebro, en 324. La fecha habitual es el 3 de julio. Zósimo ofrece un relato tardío y hostil de un cruce y una retirada; no identifica un vado prospectado. Nuestro pequeño convoy auxiliar en embarcaciones es ficticio y se sitúa junto a esa campaña. No dirige la batalla imperial ni la confunde con la victoria posterior en Bitinia. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.persona-intro / after handover | imperial-clerk | My family papers count men twice: once when they answer, once when they reach the other bank. I used to call that fussy. Then an empty boat came back to my own desk with a full departure list. I have stopped laughing at the second column. | Los papeles familiares cuentan a los hombres dos veces: cuando responden y cuando alcanzan la otra orilla. Antes lo llamaba una manía. Después volvió a mi propia mesa una embarcación vacía con una lista de salida llena. He dejado de reírme de la segunda columna. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.route-help / available from start; repeatable without effect | none | Stage at least eight of ten original auxiliaries and all four original chests at lower embarkation, with 300 food and 120 wood paid once. Two original ferries have four slots each, shared by all passengers. Carry at least eight actually staged auxiliaries and all four chests across; each needs its own observed boarding, journey and unloading. Repeat trips are allowed. Bring eight actually crossed auxiliaries and all chests to inland assembly. The short east land approach has a disclosed finite hostile pocket; a longer east detour is available from the start. Main boats are unopposed. Optional assistance never supplies a main chest or opens the only route. Stage all ten auxiliaries before the final readiness payment to allow two later auxiliary losses; if only eight are receipted, every one of those eight must survive. Crossing proofs start only after the complete readiness objective latches. | Prepara al menos ocho de diez auxiliares originales y los cuatro cofres originales en el embarque inferior; paga una vez 300 de alimento y 120 de madera. Dos embarcaciones originales tienen cuatro plazas cada una, compartidas por todos los pasajeros. Cruza con al menos ocho auxiliares realmente preparados y los cuatro cofres; cada uno necesita embarque, viaje y desembarque observados propios. Puedes repetir viajes. Lleva ocho auxiliares realmente cruzados y todos los cofres a la reunión interior. El acceso terrestre oriental corto tiene una bolsa hostil finita indicada; desde el inicio existe un desvío oriental más largo. Las embarcaciones principales no tienen oposición. La ayuda opcional no proporciona cofres principales ni abre la única ruta. Prepara los diez auxiliares antes del último pago de preparación para permitir dos pérdidas auxiliares posteriores; si el recibo recoge solo ocho, deben sobrevivir los ocho. Las pruebas de cruce empiezan solo tras fijarse el objetivo completo de preparación. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.o1-goal / phase-1 active | none | Stage eight original auxiliaries and all four collected original chests at lower embarkation; pay 300 food and 120 wood once. | Prepara ocho auxiliares originales y los cuatro cofres originales recogidos en el embarque inferior; paga una vez 300 de alimento y 120 de madera. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.o1-receipt / o1 latched once | none | Readiness records identify the actual originals staged at the southwest shore. | Los recibos de preparación identifican los originales realmente preparados en la orilla suroccidental. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.o1-reaction / after o1 receipt | imperial-clerk | There is no passenger yet in the crossing column. A supply payment is not a ferry trip. | Aún no hay pasajeros en la columna de cruces. Pagar provisiones no es viajar en embarcación. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.o2-goal / phase-2 active | none | Use the two original four-slot ferries to cross eight actually staged auxiliaries and all four chests, with individual manifest-backed unloading at the opposite landing. | Usa las dos embarcaciones originales de cuatro plazas para cruzar con ocho auxiliares realmente preparados y los cuatro cofres, con desembarque individual respaldado por manifiesto. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.o2-receipt / o2 latched once | none | Original passenger journeys are complete; every counted identity boarded and disembarked through its own scoped manifest. | Los viajes originales están completos; cada identidad contada embarcó y desembarcó mediante su propio manifiesto específico. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.o2-reaction / after o2 receipt | imperial-clerk | A boat can carry four passengers. Two clerks cannot give it eight by keeping separate books. | Una embarcación lleva cuatro pasajeros. Dos escribientes no pueden darle ocho llevando libros separados. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.o3-goal / phase-3 active | none | Bring at least eight actually crossed original auxiliaries and all four original chests to the local inland assembly. | Lleva al menos ocho auxiliares originales realmente cruzados y los cuatro cofres originales a la reunión local interior. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.o3-receipt / o3 latched once | none | The surviving original convoy reached inland assembly after its observed water crossings. | El convoy original superviviente llegó a la reunión interior tras sus cruces de agua observados. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.o3-reaction / after o3 receipt | imperial-clerk | That longer path may save a shorter list of condolences. I will leave the choice to the escort. | Ese camino más largo puede ahorrar una lista más corta de pésames. Dejaré la elección a la escolta. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of both western approaches. Benefit: Mark the disclosed upper-water-detour once; neither capacity nor terrain changes. | Explora los dos miradores señalados de los dos accesos occidentales. Ventaja: Señala una vez upper-water-detour ya indicado; no cambia capacidad ni terreno. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-1-complete / side-1 completed | none | Both western approaches completed. Its stated benefit has been granted once. | Los dos accesos occidentales: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-1-lost / side-1 failed-optional | none | Both western approaches is unavailable after the loss of its unique participant or object. The main mission continues. | Los dos accesos occidentales: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from a crossing without a surveyed ford and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de un cruce sin vado prospectado y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-2-complete / side-2 completed | none | A crossing without a surveyed ford completed. Its stated benefit has been granted once. | Un cruce sin vado prospectado: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-2-lost / side-2 failed-optional | none | A crossing without a surveyed ford is unavailable after the loss of its unique participant or object. The main mission continues. | Un cruce sin vado prospectado: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at households on the waiting bank. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares en la orilla de espera. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-3-complete / side-3 completed | none | Households on the waiting bank completed. Its stated benefit has been granted once. | Hogares en la orilla de espera: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-3-lost / side-3 failed-optional | none | Households on the waiting bank is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares en la orilla de espera: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the western loading shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el cobertizo occidental de carga. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-4-complete / side-4 completed | none | The western loading shelter completed. Its stated benefit has been granted once. | El cobertizo occidental de carga: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-4-lost / side-4 failed-optional | none | The western loading shelter is unavailable after the loss of its unique participant or object. The main mission continues. | El cobertizo occidental de carga: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-5-goal / optional list from start | none | Escort the trader of one waiting-bank consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de una remesa en la orilla de espera hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-5-complete / side-5 completed | none | One waiting-bank consignment completed. Its stated benefit has been granted once. | Una remesa en la orilla de espera: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-5-lost / side-5 failed-optional | none | One waiting-bank consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Una remesa en la orilla de espera: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the western staging circuit to the marked road junction. Benefit: Mark the disclosed west-preparation once; neither capacity nor terrain changes. | Escolta al guía local de el circuito occidental de preparación hasta el cruce señalado. Ventaja: Señala una vez west-preparation ya indicado; no cambia capacidad ni terreno. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-6-complete / side-6 completed | none | The western staging circuit completed. Its stated benefit has been granted once. | El circuito occidental de preparación: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.side-6-lost / side-6 failed-optional | none | The western staging circuit is unavailable after the loss of its unique participant or object. The main mission continues. | El circuito occidental de preparación: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.fact-outro / victory first | collection-narrator | The fictional convoy crossed with observed manifests and reached its local inland assembly. The reported imperial victory remains historical context; this small success neither measures the ancient armies nor identifies Constantine’s crossing. The operations toward Byzantium and the Asian shore follow separately. | El convoy ficticio cruzó con manifiestos observados y alcanzó su punto local de reunión interior. La victoria imperial referida sigue siendo contexto histórico; este pequeño éxito no mide los ejércitos antiguos ni identifica el paso de Constantino. Las operaciones hacia Bizancio y la orilla asiática continúan por separado. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.persona-outro / after fact-outro | imperial-clerk | Eight names at least, four chests without a twin, and boats that came back for those still waiting. A victory headline would be shorter. My second column takes up more room, and I am keeping it. | Al menos ocho nombres, cuatro cofres sin sustituto y embarcaciones que volvieron por quienes esperaban. Un titular de victoria sería más corto. Mi segunda columna ocupa más espacio, y la conservaré. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.defeat / main defeat; close side rewards first | none | The required number of actually ready or actually crossed original auxiliaries is no longer available, an indispensable original load is lost, or both original ferries are lost before every required crossing finishes. Boarded passengers are lost with their destroyed carrier; disembarked passengers survive independently. Optional losses alone never defeat the main mission. | Ya no queda el número requerido de auxiliares originales realmente preparados o realmente cruzados, se pierde una carga original indispensable, o se pierden ambas embarcaciones originales antes de terminar todos los cruces requeridos. Los pasajeros embarcados se pierden con su embarcación destruida; quienes desembarcaron sobreviven por separado. Las pérdidas opcionales por sí solas nunca derrotan la misión principal. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.09-crossing-and-supply-adrianople.odyssey.next-episode / after persona-outro | none | Continue with Across the Bright Shore. This episode does not complete the campaign. | Continúa con Al otro lado de la costa luminosa. Este episodio no termina la campaña. |

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
    },
    {
      "id": "finite-local-combat-rosters",
      "status": "native leashes, unit proxies and real combat calibration pending"
    },
    {
      "id": "paid-finite-troop-replacement",
      "status": "architecture/native implementation pending; original cargo/auxiliaries/carriers never replaced"
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
      "imperial-church.09-crossing-and-supply-adrianople.ferries-1": 4,
      "imperial-church.09-crossing-and-supply-adrianople.ferries-2": 4
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
      "a fifth simultaneous passenger cannot board a four-slot carrier, even through another main requirement",
      "an arrival at the opposite bank without boarding/water transit/disembark receipts cannot count",
      "never count a passenger absent from its own actual readiness receipt",
      "empty ferry return and repeated event never duplicate a passenger journey",
      "destroying an occupied ferry loses its manifest passengers, not already disembarked ones",
      "one original ferry can complete all required crossings after the other is lost empty",
      "eight final auxiliaries must belong to the actual completed-journey ledger",
      "long east route remains viable without main combat or optional reward in all difficulties",
      "no implied historical ford or Ottoman bridge; tributary/ancient channel controls must be independently certified",
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
