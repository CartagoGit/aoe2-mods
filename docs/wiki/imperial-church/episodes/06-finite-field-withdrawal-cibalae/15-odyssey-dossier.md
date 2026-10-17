# 6. The Field between Two Eagles

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `06-finite-field-withdrawal-cibalae` · 314 or 316 CE; dating disputed · 400×400

## Historical frame and fixed outcome

EN: Zosimus recounts a battle near Cibalae between Constantine and Licinius, followed by Licinius’ retreat toward Sirmium. His later account is hostile to Constantine and does not settle the disputed dating to 314 or 316. Modern Vinkovci occupies the Cibalae area beside the Bosut in a lowland region; the exact battlefield has not been established here. Our small auxiliary withdrawal is fiction within the fixed historical defeat of Licinius.

ES: Zósimo relata una batalla junto a Cibalae entre Constantino y Licinio, seguida por la retirada de Licinio hacia Sirmio. Su relato tardío es hostil a Constantino y no resuelve la datación discutida en 314 o 316. La actual Vinkovci ocupa la zona de Cibalae junto al Bosut, en una región de tierras bajas; aquí no se ha establecido el campo de batalla exacto. Nuestra pequeña retirada auxiliar es ficticia dentro de la derrota histórica fija de Licinio.

EN: At least eight auxiliaries who actually staged at the provision yard reached the northern local assembly, together with four original supply chests. This fictional local success reverses no historical battle. Zosimus places Licinius’ later withdrawal toward Sirmium; that longer itinerary is off-map and is not represented by our northward local route. The battle date and tactical footprint remain qualified.

ES: Al menos ocho auxiliares que realmente pasaron por el patio de provisiones llegaron al punto local norteño de reunión, junto con cuatro cofres originales. Este éxito local ficticio no revierte ninguna batalla histórica. Zósimo sitúa la retirada posterior de Licinio hacia Sirmio; ese itinerario más largo queda fuera del mapa y no lo representa nuestra ruta local hacia el norte. La fecha de batalla y la huella táctica mantienen sus cautelas.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "Zosimus narrates Constantine’s victory near Cibalae and Licinius’ subsequent withdrawal toward Sirmium. The exact year314/316 and battlefield footprint remain disputed or unverified; the local auxiliary convoy does not represent the emperor’s entire retreat.",
        "es-ES": "Zósimo narra la victoria de Constantino junto a Cibalae y la retirada posterior de Licinio hacia Sirmio. El año exacto314/316 y la huella del campo siguen discutidos o sin verificar; el convoy auxiliar local no representa toda la retirada del emperador."
      },
      "architectCorrection": {
        "date": "2026-10-13",
        "author": "gpt-6",
        "approval": "independent historical review pending",
        "reason": "Direct primary passages and geographical controls replace candidate conflations; local participants and outputs remain fiction."
      }
    },
    {
      "consultedUrl": null,
      "passage": "No accessible primary/academic passage opened for Cibalae in this pass; dossier relies on Britannica.",
      "limitations": "Dating 314 vs 316 is disputed; Britannica URL not consulted. Do not present either year as settled here.",
      "status": "unavailable",
      "supportedClaim": "The claimed battle and 317 settlement were not verified in consulted material. / La batalla y el acuerdo de 317 no se verificaron en material consultado.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "No qualifying passage consulted.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.tertullian.org/fathers/zosimus02_book2.htm",
      "passage": "Zosimus New History II, displayed Cibalis battle/retreat paragraphs (II.18–20 locator to compare)",
      "coverageActuallyRead": "Read quarrel, town/road/marsh/hill description, battle outcome, retreat toward Sirmium and later settlement sequence.",
      "limitations": "Later hostile narrative; displayed passage does not settle314/316 or exact317 settlement date. No modern battlefield coordinate or high mountain inferred.",
      "consultationDate": "2026-10-13",
      "approval": "architect interpretation; independent approval pending"
    },
    {
      "consultedUrl": "https://grad-vinkovci.hr/geoprometni-polozaj",
      "passage": "Municipal geography/elevation paragraph",
      "coverageActuallyRead": "Read Bosut setting between Danube and Sava and modern78–125m elevation range.",
      "limitations": "Modern regional control only, not ancient wetlands, road or battlefield survey.",
      "consultationDate": "2026-10-13",
      "approval": "architect interpretation; independent approval pending"
    },
    {
      "consultedUrl": "https://grad-vinkovci.hr/povijest-grada",
      "passage": "Municipal history, Roman Cibalae paragraph",
      "coverageActuallyRead": "Read modern city identification with Roman Cibalae and municipal314 battle date.",
      "limitations": "Official municipal summary does not resolve scholarly314/316 dispute; unrelated later monastery chronology not adopted.",
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

EN: Stage at least eight of the ten original auxiliaries and all four original supply chests at the provision yard.

ES: Prepara al menos ocho de los diez auxiliares originales y los cuatro cofres originales en el patio de provisiones.

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
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-4",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-6",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-7",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-8",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-9",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-10"
      ],
      "destinations": {
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-1": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-2": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-3": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-4": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-5": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-6": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-7": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-8": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-9": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-10": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-4"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-4"
      ],
      "destinations": {
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-1": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-2": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-3": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-4": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true,
  "exportedLedgers": [
    {
      "id": "auxiliaries-staged",
      "fromRequirements": [
        "req-1"
      ],
      "minimumCount": 8,
      "snapshot": "exact entities with observed arrival at o1 latch; immutable after export",
      "operator": "intersection"
    }
  ]
}
```

EN: The observed staging ledger contains at least eight original auxiliaries and four original chests.

ES: El registro observado de preparación contiene al menos ocho auxiliares originales y cuatro cofres originales.

EN: A name outside the yard cannot be counted merely because I hope it will arrive.

ES: No puedo contar un nombre que está fuera del patio solo porque espero que llegue.

### o2 / phase-2

EN: Pay 300 food and 100 wood once; visit and verify passage through at least one of the east-field or west-detour approaches.

ES: Paga una vez 300 de alimento y 100 de madera; visita y verifica el paso por al menos uno de los accesos de campo oriental o desvío occidental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 300,
        "wood": 100
      },
      "id": "req-1",
      "receivingZones": [
        "imperial-church.06-finite-field-withdrawal-cibalae.destination-2"
      ],
      "allocations": {
        "imperial-church.06-finite-field-withdrawal-cibalae.destination-2": {
          "food": 300,
          "wood": 100
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.06-finite-field-withdrawal-cibalae.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "area-state",
      "requiredCount": 1,
      "state": "visited-and-passable",
      "blockingEnemies": [],
      "id": "req-2",
      "zones": [
        "imperial-church.06-finite-field-withdrawal-cibalae.destination-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.destination-4"
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: One conserved supply payment and at least one actually visited passable branch are recorded.

ES: Se registran un pago conservado de provisiones y al menos una rama realmente visitada y transitable.

EN: The wider circuit spends distance; the shorter circuit may spend lives. Neither is the emperor’s complete retreat.

ES: El circuito amplio gasta distancia; el corto puede gastar vidas. Ninguno es la retirada completa del emperador.

### o3 / phase-3

EN: Bring at least eight auxiliaries from the actual staging ledger and all four original chests to northern local assembly.

ES: Lleva al menos ocho auxiliares del registro real de preparación y los cuatro cofres originales a la reunión local norteña.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 8,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o1",
        "ledger": "auxiliaries-staged"
      },
      "id": "req-1",
      "entities": [
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-4",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-6",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-7",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-8",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-9",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-10"
      ],
      "destinations": {
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-1": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-2": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-3": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-4": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-5": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-6": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-7": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-8": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-9": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-10": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-4"
      ],
      "destinations": {
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-1": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-2": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-3": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-4": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Eight or more actually staged original auxiliaries and all four chests reached local assembly.

ES: Ocho o más auxiliares originales realmente preparados y los cuatro cofres llegaron a la reunión local.

EN: This entry saves our invented local count. It does not change the name on the historical victory line.

ES: Esta anotación salva nuestra cuenta local inventada. No cambia el nombre de la línea de victoria histórica.

## Finite opposition and authored engagement constraints

```json
{
  "historicalPolicy": "fictional finite east-field pocket, not actual battle deployment or army size",
  "worldSelectionPolicy": "only selected initial identities instantiate; unselected maximum members absent, not hidden reserves",
  "engagementPolicy": "All selected opponents are confined to the east-field pocket aroundhub3. The west land detour, staging yard, assembly and independent civilian branches are outside their leash. No global hunt, scripted pursuit, production or timed wave. Exact leash polygon, native proxies and combat calibration must be measured; proposed non-combat viability is not claimed as tested.",
  "byDifficulty": {
    "easy": {
      "productionEnabled": false,
      "mobilizations": [],
      "initialEntityIds": [
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-4",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-6",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-7",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-8",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-9",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-10",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-11",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-12",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-4",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-6"
      ]
    },
    "standard": {
      "productionEnabled": false,
      "mobilizations": [],
      "initialEntityIds": [
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-4",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-6",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-7",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-8",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-9",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-10",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-11",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-12",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-13",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-14",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-15",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-16",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-17",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-18",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-4",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-6",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-7",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-8",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-9",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-10"
      ]
    },
    "hard": {
      "productionEnabled": false,
      "mobilizations": [],
      "initialEntityIds": [
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-4",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-6",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-7",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-8",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-9",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-10",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-11",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-12",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-13",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-14",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-15",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-16",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-17",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-18",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-19",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-20",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-21",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-22",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-23",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-24",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-4",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-6",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-7",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-8",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-9",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-10",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-11",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-12",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-13",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-14",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-15",
        "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-16"
      ]
    }
  }
}
```

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/06-finite-field-withdrawal-cibalae.svg)

```json
{
  "bbox": [
    18.747,
    45.277,
    18.847,
    45.332
  ],
  "terrainProfile": "cibalae",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        192.38,
        252.68
      ],
      "lonLat": [
        18.795,
        45.294
      ],
      "name": {
        "en": "Fictional auxiliary starting pocket",
        "es-ES": "Punto inicial ficticio de auxiliares"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        188.81,
        196.97
      ],
      "lonLat": [
        18.794,
        45.305
      ],
      "name": {
        "en": "Northern provision and staging yard",
        "es-ES": "Patio norteño de provisiones y preparación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        281.44,
        196.97
      ],
      "lonLat": [
        18.82,
        45.305
      ],
      "name": {
        "en": "Eastern shorter field approach",
        "es-ES": "Acceso oriental de campo más corto"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        81.94,
        141.25
      ],
      "lonLat": [
        18.764,
        45.316
      ],
      "name": {
        "en": "Western lowland detour",
        "es-ES": "Desvío occidental de tierras bajas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        203.06,
        100.73
      ],
      "lonLat": [
        18.798,
        45.324
      ],
      "name": {
        "en": "Northern local assembly",
        "es-ES": "Reunión local norteña"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "eastern-field-road",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-3",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "western-lowland-detour",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "northern-relief",
      "hubOrder": [
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 6
    }
  ],
  "terrainInstructions": "Local lowland crop north of a schematic Bosut channel around the real Cibalae/Vinkovci region. Five openly fictional supply, field, detour and assembly pockets remain on the north bank. No required Bosut crossing and no invented high mountain or cliff borrowed literally from Zosimus. His marsh/hill/road description needs critical topographic comparison; municipal modern elevation 78–125 m does not reconstruct ancient waterlogging. Main northern detour and shorter eastern field road are local assembly choices, not the full historical withdrawal toward Sirmium. Avoid modern railways, canalization, later church façades and a surveyed battlefield claim. Exact ancient banks, DEM, soft ground and troop deployment pending.",
  "corridorStraightLengthsTiles": {
    "eastern-field-road": 272.57,
    "western-lowland-detour": 304.07,
    "northern-relief": 127.72
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
        18.747,
        45.285
      ],
      [
        18.774,
        45.28
      ],
      [
        18.8,
        45.284
      ],
      [
        18.825,
        45.283
      ],
      [
        18.847,
        45.278
      ]
    ],
    "certainty": "architect schematic Bosut regional control; not measured ancient banks, marshes or battle footprint",
    "renderAs": "river-line"
  },
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/imperial-church/odyssey/06-finite-field-withdrawal-cibalae.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-1",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-2",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-3",
      "role": "fictional-original-auxiliary",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-4",
      "role": "fictional-original-auxiliary",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-5",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-6",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-7",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -6,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-8",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -4,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-9",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-10",
      "role": "fictional-original-auxiliary",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-1",
      "role": "fictional-original-local-supply-chest",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-2",
      "role": "fictional-original-local-supply-chest",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-3",
      "role": "fictional-original-local-supply-chest",
      "initialHub": "hub-1",
      "offsetTiles": [
        -6,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-4",
      "role": "fictional-original-local-supply-chest",
      "initialHub": "hub-1",
      "offsetTiles": [
        -4,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-1",
      "role": "fictional-friendly-field-screen",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-2",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-3",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        12,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-4",
      "role": "fictional-friendly-field-screen",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-5",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        8,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-6",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-7",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        12,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-8",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        14,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-9",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        8,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-10",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-11",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        12,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-12",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        14,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-13",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        8,
        14
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-14",
      "role": "fictional-friendly-field-screen",
      "initialHub": "hub-1",
      "offsetTiles": [
        10,
        14
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-1",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-2",
      "role": "fictional-hostile-patrol",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-3",
      "role": "fictional-hostile-patrol",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-4",
      "role": "fictional-hostile-patrol",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-5",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-6",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-7",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-8",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -6,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-9",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-10",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-11",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -8,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-12",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -6,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-13",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -12,
        14
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-14",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -10,
        14
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-15",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -8,
        14
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-16",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -6,
        14
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-17",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -12,
        16
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-18",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -10,
        16
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-19",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -8,
        16
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-20",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -6,
        16
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-21",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -12,
        18
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-22",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -10,
        18
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-23",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -8,
        18
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-24",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        -6,
        18
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-1",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        8,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-2",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-3",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        12,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-4",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        14,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-5",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        8,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-6",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-7",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        12,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-8",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        14,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-9",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        8,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-10",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-11",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        12,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-12",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        14,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-13",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        8,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-14",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        10,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-15",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        12,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-16",
      "role": "fictional-hostile-patrol",
      "initialHub": "hub-3",
      "offsetTiles": [
        14,
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
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.06-finite-field-withdrawal-cibalae.destination-5",
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
    "withdrawal-auxiliaries": [
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-1",
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-2",
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-3",
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-4",
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-5",
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-6",
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-7",
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-8",
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-9",
      "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-10"
    ],
    "supply-chests": [
      "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-1",
      "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-2",
      "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-3",
      "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-4"
    ],
    "friendly-screen": [
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-1",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-2",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-3",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-4",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-5",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-6",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-7",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-8",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-9",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-10",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-11",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-12",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-13",
      "imperial-church.06-finite-field-withdrawal-cibalae.friendly-screen-14"
    ],
    "field-patrol": [
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-1",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-2",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-3",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-4",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-5",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-6",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-7",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-8",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-9",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-10",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-11",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-12",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-13",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-14",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-15",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-16",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-17",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-18",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-19",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-20",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-21",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-22",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-23",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-patrol-24"
    ],
    "field-ranged": [
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-1",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-2",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-3",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-4",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-5",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-6",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-7",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-8",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-9",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-10",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-11",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-12",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-13",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-14",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-15",
      "imperial-church.06-finite-field-withdrawal-cibalae.field-ranged-16"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-4",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-5",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-6",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-7",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-8",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-9",
        "imperial-church.06-finite-field-withdrawal-cibalae.withdrawal-auxiliaries-10"
      ],
      "minimumAliveOrAlreadySafe": 8
    },
    {
      "entities": [
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-1",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-2",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-3",
        "imperial-church.06-finite-field-withdrawal-cibalae.supply-chests-4"
      ],
      "minimumAliveOrAlreadySafe": 4
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### The wider Bosut-side circuit / El circuito amplio junto al Bosut

EN: Scout both marked viewpoints of the wider bosut-side circuit. Benefit: Mark the proposed western-lowland-detour local land circuit once. All mandatory receivers are already disclosed.

ES: Explora los dos miradores señalados de el circuito amplio junto al bosut. Ventaja: Señala una vez el circuito terrestre local propuesto western-lowland-detour. Todos los receptores obligatorios ya se indican.

EN: Mark a proposed north-bank detour without certifying ancient marsh edges or unlocking a mandatory route.

ES: Señala un desvío propuesto de la ribera norte sin certificar márgenes antiguos de marisma ni desbloquear una ruta obligatoria.

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
          "06-finite-field-withdrawal-cibalae.side-1.zone-1",
          "06-finite-field-withdrawal-cibalae.side-1.zone-2"
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
        "id": "06-finite-field-withdrawal-cibalae.side-1.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "06-finite-field-withdrawal-cibalae.side-1.zone-2",
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
      "target": "western-lowland-detour proposed local land approach",
      "resources": {},
      "onceFlag": "06-finite-field-withdrawal-cibalae.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "western-lowland-detour"
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
      "eastern-field-road",
      "western-lowland-detour",
      "northern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Households beyond the field pocket / Hogares fuera del área de combate

EN: Bring each of the two aid crates to its assigned household at households beyond the field pocket. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares fuera del área de combate. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Independent civilian help remains outside enemy leashes; it never substitutes a main auxiliary.

ES: La ayuda civil independiente queda fuera de los límites enemigos; nunca sustituye a un auxiliar principal.

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
          "06-finite-field-withdrawal-cibalae.side-2.entity-1",
          "06-finite-field-withdrawal-cibalae.side-2.entity-2"
        ],
        "destinations": {
          "06-finite-field-withdrawal-cibalae.side-2.entity-1": "06-finite-field-withdrawal-cibalae.side-2.zone-1",
          "06-finite-field-withdrawal-cibalae.side-2.entity-2": "06-finite-field-withdrawal-cibalae.side-2.zone-2"
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
        "id": "06-finite-field-withdrawal-cibalae.side-2.entity-1",
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
        "id": "06-finite-field-withdrawal-cibalae.side-2.entity-2",
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
        "id": "06-finite-field-withdrawal-cibalae.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "06-finite-field-withdrawal-cibalae.side-2.zone-2",
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
      "onceFlag": "06-finite-field-withdrawal-cibalae.side-2.rewarded",
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
      "eastern-field-road",
      "western-lowland-detour",
      "northern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A shelter for the staging yard / Un cobertizo para el patio de preparación

EN: Pay 50 wood and restore the damaged store of a shelter for the staging yard to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de un cobertizo para el patio de preparación. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Separate shelter repair grants bounded ordinary stock, not resurrection or free reinforcements.

ES: La reparación separada concede existencias ordinarias limitadas, no resurrección ni refuerzos gratis.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "06-finite-field-withdrawal-cibalae.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "06-finite-field-withdrawal-cibalae.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "06-finite-field-withdrawal-cibalae.side-3.payment",
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
        "id": "06-finite-field-withdrawal-cibalae.side-3.entity-1",
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
        "id": "06-finite-field-withdrawal-cibalae.side-3.zone-1",
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
      "onceFlag": "06-finite-field-withdrawal-cibalae.side-3.rewarded",
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
      "eastern-field-road",
      "western-lowland-detour",
      "northern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### One finite replacement consignment / Una remesa finita de reposición

EN: Escort the trader of one finite replacement consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de una remesa finita de reposición hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A finite resource exchange supports a future certified paid replacement capability; the exchange itself creates no soldiers.

ES: Un intercambio finito apoya una futura capacidad certificada de reposición pagada; el intercambio no crea soldados.

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
          "06-finite-field-withdrawal-cibalae.side-4.entity-1"
        ],
        "destinations": {
          "06-finite-field-withdrawal-cibalae.side-4.entity-1": "06-finite-field-withdrawal-cibalae.side-4.zone-1"
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
        "receipt": "06-finite-field-withdrawal-cibalae.side-4.payment",
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
        "id": "06-finite-field-withdrawal-cibalae.side-4.entity-1",
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
        "id": "06-finite-field-withdrawal-cibalae.side-4.zone-1",
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
      "onceFlag": "06-finite-field-withdrawal-cibalae.side-4.rewarded",
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
      "eastern-field-road",
      "western-lowland-detour",
      "northern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A separate local convoy / Un convoy local separado

EN: Bring both voluntary evacuee groups from a separate local convoy to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de un convoy local separado al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Optional transport uses distinct identities and cannot fill the mandatory staging ledger.

ES: El transporte opcional usa identidades distintas y no rellena el registro obligatorio.

```json
{
  "id": "side-5",
  "kind": "extract",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "06-finite-field-withdrawal-cibalae.side-5.entity-1",
          "06-finite-field-withdrawal-cibalae.side-5.entity-2"
        ],
        "destinations": {
          "06-finite-field-withdrawal-cibalae.side-5.entity-1": "06-finite-field-withdrawal-cibalae.side-5.zone-1",
          "06-finite-field-withdrawal-cibalae.side-5.entity-2": "06-finite-field-withdrawal-cibalae.side-5.zone-1"
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
        "id": "06-finite-field-withdrawal-cibalae.side-5.entity-1",
        "role": "extract",
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
        "id": "06-finite-field-withdrawal-cibalae.side-5.entity-2",
        "role": "extract",
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
        "id": "06-finite-field-withdrawal-cibalae.side-5.zone-1",
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
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 100,
        "gold": 25
      },
      "onceFlag": "06-finite-field-withdrawal-cibalae.side-5.rewarded",
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
    "originHub": "hub-3",
    "receivingHub": "hub-1",
    "corridorIds": [
      "eastern-field-road",
      "western-lowland-detour",
      "northern-relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The last northern approach / El último acceso norteño

EN: Escort the local guide of the last northern approach to the marked road junction. Benefit: Mark the proposed northern-relief local land circuit once. All mandatory receivers are already disclosed.

ES: Escolta al guía local de el último acceso norteño hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local propuesto northern-relief. Todos los receptores obligatorios ya se indican.

EN: Mark the northern local land approach, never a complete Sirmium itinerary or a safe enemy-bypass guarantee without native testing.

ES: Señala el acceso terrestre local norteño, nunca un itinerario completo a Sirmio ni una garantía de evitar enemigos sin pruebas nativas.

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
          "06-finite-field-withdrawal-cibalae.side-6.entity-1"
        ],
        "destinations": {
          "06-finite-field-withdrawal-cibalae.side-6.entity-1": "06-finite-field-withdrawal-cibalae.side-6.zone-1"
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
        "id": "06-finite-field-withdrawal-cibalae.side-6.entity-1",
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
        "id": "06-finite-field-withdrawal-cibalae.side-6.zone-1",
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
      "target": "northern-relief proposed local land approach",
      "resources": {},
      "onceFlag": "06-finite-field-withdrawal-cibalae.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "northern-relief"
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
      "eastern-field-road",
      "western-lowland-detour",
      "northern-relief"
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
      "food": 550,
      "wood": 200,
      "gold": 25,
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
      "id": "distance-before-combat",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Use the longer proposed west detour, keep all original identities together and invest in route information.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "screen-and-short-route",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Use the friendly screen against the finite east pocket, reserve supply payment and accept tactical exposure instead of a compulsory kill objective.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "parallel-local-care",
      "optionalObjectives": [
        "side-2",
        "side-5"
      ],
      "costOfOpportunity": "Route the main convoy west while a separate team supports civilian work outside the enemy pocket.",
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
      "food": 2225,
      "wood": 1113,
      "gold": 653,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 100,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 400,
      "wood": 250,
      "gold": 200,
      "stone": 0
    },
    "replacementBudget": {
      "food": 900,
      "wood": 450,
      "gold": 450,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 2250,
      "wood": 1200,
      "gold": 800,
      "stone": 100
    },
    "maxVillagers": 12,
    "enemyTotalCap": 18,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      30,
      55
    ],
    "difficultyLevers": "12 workers;18 finite east opponents,14 friendly screen; west detour disclosed and mandatory transport loss margin 2.",
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
      "food": 2300,
      "wood": 1150,
      "gold": 675,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 100,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 400,
      "wood": 250,
      "gold": 200,
      "stone": 0
    },
    "replacementBudget": {
      "food": 900,
      "wood": 450,
      "gold": 450,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 2250,
      "wood": 1200,
      "gold": 800,
      "stone": 100
    },
    "maxVillagers": 9,
    "enemyTotalCap": 28,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      35,
      65
    ],
    "difficultyLevers": "9 workers;28 finite east opponents, same 14 screen; decide longer transport route or concentrated local combat.",
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
      "food": 2375,
      "wood": 1188,
      "gold": 698,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 100,
      "gold": 0,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 400,
      "wood": 250,
      "gold": 200,
      "stone": 0
    },
    "replacementBudget": {
      "food": 900,
      "wood": 450,
      "gold": 450,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 2250,
      "wood": 1200,
      "gold": 800,
      "stone": 100
    },
    "maxVillagers": 6,
    "enemyTotalCap": 40,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      40,
      75
    ],
    "difficultyLevers": "6 workers;40 finite east opponents, same 14 screen and lower start stock; viable west detour must survive native leash/path audit, not forced combat.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.title / always | none | The Field between Two Eagles | El campo entre dos águilas |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.fact-intro / intro first | collection-narrator | Zosimus recounts a battle near Cibalae between Constantine and Licinius, followed by Licinius’ retreat toward Sirmium. His later account is hostile to Constantine and does not settle the disputed dating to 314 or 316. Modern Vinkovci occupies the Cibalae area beside the Bosut in a lowland region; the exact battlefield has not been established here. Our small auxiliary withdrawal is fiction within the fixed historical defeat of Licinius. | Zósimo relata una batalla junto a Cibalae entre Constantino y Licinio, seguida por la retirada de Licinio hacia Sirmio. Su relato tardío es hostil a Constantino y no resuelve la datación discutida en 314 o 316. La actual Vinkovci ocupa la zona de Cibalae junto al Bosut, en una región de tierras bajas; aquí no se ha establecido el campo de batalla exacto. Nuestra pequeña retirada auxiliar es ficticia dentro de la derrota histórica fija de Licinio. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.persona-intro / after handover | imperial-clerk | The inherited military account wants a line for victory and a line for defeat. I understand that habit: a clerk can make a loss disappear by choosing a convenient heading. Our imagined ten auxiliaries deserve a different count. I was not at Cibalae, and neither these names nor this northern assembly yard are an ancient witness. | El relato militar heredado quiere una línea para la victoria y otra para la derrota. Entiendo esa costumbre: un funcionario puede hacer desaparecer una pérdida eligiendo un encabezamiento conveniente. Nuestros diez auxiliares imaginados merecen otra cuenta. No estuve en Cibalae, y ni estos nombres ni este patio norteño son un testimonio antiguo. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.route-help / available from start; repeatable without effect | none | Bring at least eight of the ten original auxiliaries to the provision yard and stage all four original chests there. Pay 300 food and 100 wood once. Visit and verify either the eastern field approach or the longer western detour. Then take at least eight of the auxiliaries actually recorded at staging, and all four chests, to northern local assembly. The eastern field pocket has finite disclosed opponents; the western route is designed to avoid that pocket and remain viable without optional tasks. More than two auxiliary losses or any chest loss causes main defeat. | Lleva al menos ocho de los diez auxiliares originales al patio de provisiones y prepara allí los cuatro cofres originales. Paga una vez 300 de alimento y 100 de madera. Visita y verifica el acceso oriental de campo o el desvío occidental más largo. Después lleva al menos ocho auxiliares realmente registrados en la preparación y los cuatro cofres a la reunión local norteña. El área oriental tiene oponentes finitos indicados; la ruta occidental se diseña para evitarla y seguir siendo viable sin objetivos opcionales. Perder más de dos auxiliares o cualquier cofre causa derrota principal. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.o1-goal / phase-1 active | none | Stage at least eight of the ten original auxiliaries and all four original supply chests at the provision yard. | Prepara al menos ocho de los diez auxiliares originales y los cuatro cofres originales en el patio de provisiones. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.o1-receipt / o1 latched once | none | The observed staging ledger contains at least eight original auxiliaries and four original chests. | El registro observado de preparación contiene al menos ocho auxiliares originales y cuatro cofres originales. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.o1-reaction / after o1 receipt | imperial-clerk | A name outside the yard cannot be counted merely because I hope it will arrive. | No puedo contar un nombre que está fuera del patio solo porque espero que llegue. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.o2-goal / phase-2 active | none | Pay 300 food and 100 wood once; visit and verify passage through at least one of the east-field or west-detour approaches. | Paga una vez 300 de alimento y 100 de madera; visita y verifica el paso por al menos uno de los accesos de campo oriental o desvío occidental. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.o2-receipt / o2 latched once | none | One conserved supply payment and at least one actually visited passable branch are recorded. | Se registran un pago conservado de provisiones y al menos una rama realmente visitada y transitable. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.o2-reaction / after o2 receipt | imperial-clerk | The wider circuit spends distance; the shorter circuit may spend lives. Neither is the emperor’s complete retreat. | El circuito amplio gasta distancia; el corto puede gastar vidas. Ninguno es la retirada completa del emperador. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.o3-goal / phase-3 active | none | Bring at least eight auxiliaries from the actual staging ledger and all four original chests to northern local assembly. | Lleva al menos ocho auxiliares del registro real de preparación y los cuatro cofres originales a la reunión local norteña. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.o3-receipt / o3 latched once | none | Eight or more actually staged original auxiliaries and all four chests reached local assembly. | Ocho o más auxiliares originales realmente preparados y los cuatro cofres llegaron a la reunión local. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.o3-reaction / after o3 receipt | imperial-clerk | This entry saves our invented local count. It does not change the name on the historical victory line. | Esta anotación salva nuestra cuenta local inventada. No cambia el nombre de la línea de victoria histórica. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of the wider bosut-side circuit. Benefit: Mark the proposed western-lowland-detour local land circuit once. All mandatory receivers are already disclosed. | Explora los dos miradores señalados de el circuito amplio junto al bosut. Ventaja: Señala una vez el circuito terrestre local propuesto western-lowland-detour. Todos los receptores obligatorios ya se indican. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-1-complete / side-1 completed | none | The wider Bosut-side circuit completed. Its stated benefit has been granted once. | El circuito amplio junto al Bosut: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-1-lost / side-1 failed-optional | none | The wider Bosut-side circuit is unavailable after the loss of its unique participant or object. The main mission continues. | El circuito amplio junto al Bosut: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at households beyond the field pocket. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares fuera del área de combate. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-2-complete / side-2 completed | none | Households beyond the field pocket completed. Its stated benefit has been granted once. | Hogares fuera del área de combate: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-2-lost / side-2 failed-optional | none | Households beyond the field pocket is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares fuera del área de combate: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of a shelter for the staging yard to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de un cobertizo para el patio de preparación. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-3-complete / side-3 completed | none | A shelter for the staging yard completed. Its stated benefit has been granted once. | Un cobertizo para el patio de preparación: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-3-lost / side-3 failed-optional | none | A shelter for the staging yard is unavailable after the loss of its unique participant or object. The main mission continues. | Un cobertizo para el patio de preparación: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-4-goal / optional list from start | none | Escort the trader of one finite replacement consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de una remesa finita de reposición hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-4-complete / side-4 completed | none | One finite replacement consignment completed. Its stated benefit has been granted once. | Una remesa finita de reposición: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-4-lost / side-4 failed-optional | none | One finite replacement consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Una remesa finita de reposición: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-5-goal / optional list from start | none | Bring both voluntary evacuee groups from a separate local convoy to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de un convoy local separado al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-5-complete / side-5 completed | none | A separate local convoy completed. Its stated benefit has been granted once. | Un convoy local separado: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-5-lost / side-5 failed-optional | none | A separate local convoy is unavailable after the loss of its unique participant or object. The main mission continues. | Un convoy local separado: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the last northern approach to the marked road junction. Benefit: Mark the proposed northern-relief local land circuit once. All mandatory receivers are already disclosed. | Escolta al guía local de el último acceso norteño hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local propuesto northern-relief. Todos los receptores obligatorios ya se indican. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-6-complete / side-6 completed | none | The last northern approach completed. Its stated benefit has been granted once. | El último acceso norteño: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.side-6-lost / side-6 failed-optional | none | The last northern approach is unavailable after the loss of its unique participant or object. The main mission continues. | El último acceso norteño: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.fact-outro / victory first | collection-narrator | At least eight auxiliaries who actually staged at the provision yard reached the northern local assembly, together with four original supply chests. This fictional local success reverses no historical battle. Zosimus places Licinius’ later withdrawal toward Sirmium; that longer itinerary is off-map and is not represented by our northward local route. The battle date and tactical footprint remain qualified. | Al menos ocho auxiliares que realmente pasaron por el patio de provisiones llegaron al punto local norteño de reunión, junto con cuatro cofres originales. Este éxito local ficticio no revierte ninguna batalla histórica. Zósimo sitúa la retirada posterior de Licinio hacia Sirmio; ese itinerario más largo queda fuera del mapa y no lo representa nuestra ruta local hacia el norte. La fecha de batalla y la huella táctica mantienen sus cautelas. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.persona-outro / after fact-outro | imperial-clerk | I can record who reached our yard without turning them into the emperor’s saved army. The smaller entry is the honest one. Beyond it, the inherited account goes on to another field and another settlement; I will not supply a date it has not given me. | Puedo registrar quién llegó a nuestro patio sin convertirlo en el ejército salvado del emperador. La anotación menor es la honesta. Más allá, el relato heredado continúa hacia otro campo y otro acuerdo; no le proporcionaré una fecha que no me ha dado. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.defeat / main defeat; close side rewards first | none | Fewer than eight original auxiliaries remain alive or already safe, or an original supply chest was irrecoverably lost. The fictional local withdrawal fails; the historical battle result remains unchanged. Optional losses alone never cause main defeat. | Quedan menos de ocho auxiliares originales vivos o ya a salvo, o se perdió un cofre original de forma irrecuperable. Fracasa la retirada local ficticia; el resultado histórico permanece. Las pérdidas opcionales por sí solas nunca causan derrota principal. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.next-episode / after persona-outro | none | Continue with A Day beneath the Law. This episode does not complete the campaign. | Continúa con Un día bajo la ley. Este episodio no termina la campaña. |
| scenario.imperial-church.06-finite-field-withdrawal-cibalae.odyssey.act-turning-point / after next-episode | collection-narrator | The first act ends with imperial rivalry still distinct from theological agreement. The next act begins in 321 with transmitted legal rules and their exceptions, then correspondence, war and council logistics. Neither the agreements of 313 nor success in this invented withdrawal made Christianity the state religion. | El primer acto termina con la rivalidad imperial todavía distinta del acuerdo teológico. El siguiente empieza en 321 con normas legales transmitidas y sus excepciones, y continúa con correspondencia, guerra y logística conciliar. Ni los acuerdos de 313 ni el éxito de esta retirada inventada hicieron del cristianismo la religión del Estado. |

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
      "status": "reference implemented; native arrival/departure/ledger save/load QA pending"
    },
    {
      "id": "finite-local-combat-rosters",
      "status": "authored selected identities; native catalogue, leash and combat calibration pending"
    },
    {
      "id": "paid-finite-troop-replacement",
      "status": "architecture/native implementation and game QA required; stock alone is not implementation"
    },
    {
      "id": "geographic-land-corridors",
      "status": "plan authored; ancient banks, DEM and pathfinding pending"
    },
    {
      "id": "two-narrator-sequence",
      "status": "text authored; native sequence adapter and localization QA pending"
    }
  ],
  "artDirection": {
    "style": "sober late Roman local work and land routes",
    "historicalControls": "fictional courts and field pockets; no exact emperor deployment, legal autograph or modern monument",
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "o1 ledger exports exactly observed arrived identities, never the complete ten-person roster",
      "only actually staged survivors can satisfy o3; eight unstaged arrivals fail",
      "any chest loss or fewer than eight original auxiliaries alive/safe causes defeat",
      "optional convoy identities never replace main ledger members",
      "west no-combat route remains viable with no optional goals on every difficulty; verify leash and path width in game",
      "east patrol may expose main convoy but may not roam to west support hubs or optional civilians",
      "no army production or invisible reserves",
      "no claim that a northward local assembly is the historical Sirmium retreat",
      "no giant mountain inferred from a disputed literary description",
      "fixed historical outcome and year uncertainty survive victory/defeat",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
