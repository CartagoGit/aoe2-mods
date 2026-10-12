# Ledgers of Damascus / Los registros de Damasco

`umayyads/01-ledgers-of-damascus` · 661 CE · administration-and-supply

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/umayyads/01-ledgers-of-damascus.svg)

## Historical frame and outcome

Muawiya’s rule after 661 began the Umayyad dynastic period. Damascus’s later monumental mosque did not yet exist in this form.

Muawiya establece gobierno omeya con centro en Damasco. Identidad lingüística/religiosa de provincias no se homogeneiza en ese año.

La gran mezquita de al-Walid no existe aún en mapa de 661. Representar administración, no victoria sobre edificios religiosos.

- [The Met, Art of the Umayyad Period](https://www.metmuseum.org/essays/the-art-of-the-umayyad-period-661-750): Dinastía y arquitectura. Referencia material; una construcción no mide la fe de sus habitantes.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

This account predates my mother. I know the sum because she preserved it; I do not know whether the clerk smiled when he wrote it.

Esta cuenta es anterior a mi madre. Conozco la suma porque la conservó; no sé si sonreía el escribiente que la anotó.

## Geography and map construction

Damascus / Ghouta — 360 × 360 tiles; north-up design controls [36.12, 33.4, 36.48, 33.65].

Oasis Ghouta, campos y huertas junto a núcleo urbano.

Barada entra desde noroeste y se dispersa hacia oasis oriental.

Qasioun al norte/noroeste; desierto al este, no Mediterráneo.

Caminos regionales a Palestina/sur y Iraq/este.

Exclude: No gran mezquita omeya monumental en 661: fase de al-Walid posterior.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Damascus old city | [36.306, 33.512] | [184.84, 193.38] |
| Qasioun slope | [36.28, 33.56] | [161.69, 142.12] |
| Eastern Ghouta | [36.39, 33.51] | [259.63, 195.52] |

```json
{
  "bbox": [
    36.12,
    33.4,
    36.48,
    33.65
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Damascus old city",
      "lonLat": [
        36.306,
        33.512
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        184.84,
        193.38
      ]
    },
    {
      "id": "anchor-2",
      "name": "Qasioun slope",
      "lonLat": [
        36.28,
        33.56
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        161.69,
        142.12
      ]
    },
    {
      "id": "anchor-3",
      "name": "Eastern Ghouta",
      "lonLat": [
        36.39,
        33.51
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        259.63,
        195.52
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        259.63,
        195.52
      ],
      "purpose": {
        "en": "Reconnect three stores in the Ghouta to the civic road.",
        "es-ES": "Reconecta tres almacenes de la Ghouta con el camino cívico."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        184.84,
        193.38
      ],
      "purpose": {
        "en": "Deliver two district inventories and provisions without seizing the workshops.",
        "es-ES": "Entrega dos inventarios de barrio y víveres sin tomar los talleres."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-3",
      "centre": [
        259.63,
        195.52
      ],
      "purpose": {
        "en": "Open the eastern caravan route and register its first shipment.",
        "es-ES": "Abre la ruta oriental de caravanas y registra su primer envío."
      },
      "radiusTiles": 14,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    }
  ],
  "corridors": [
    {
      "id": "main",
      "waypoints": [
        [
          259.63,
          195.52
        ],
        [
          184.84,
          193.38
        ],
        [
          259.63,
          195.52
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          259.63,
          195.52
        ],
        [
          230.24,
          202.45
        ],
        [
          184.84,
          193.38
        ],
        [
          259.63,
          195.52
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        36.12,
        33.61
      ],
      [
        36.23,
        33.54
      ],
      [
        36.3,
        33.52
      ],
      [
        36.34,
        33.515
      ],
      [
        36.45,
        33.5
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "damascus",
  "minimumUsableAreaFraction": 0.45,
  "interestSpacingTiles": [
    25,
    55
  ],
  "areaPolicy": "Active core + supply hinterland + optional scouting loops. Place a rest/supply point every 25–55 navigable tiles; rest cannot spawn infinite resources. Bodies of water/steep ground count as geography, not empty playable space.",
  "reliefLevels": {
    "plain": 0,
    "terrace": 1,
    "hill": 3,
    "ridge": 5,
    "cliff": 7
  },
  "rasterisation": "Contemporary coastline and schematic minor-river controls are separate layers. Ancient coast/canal uncertainty is labelled. No automatic land corridor across water; designate an evidenced fixed crossing or a transport segment and require naval capability.",
  "geometryStatus": "georeferenced design controls; corridor traversability not yet game-tested",
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmark": "20-minute crowded corridor replay, 3 passes on documented target PC; simulation slowdown <10% vs reference, measured not presumed"
  },
  "asset": "docs/design/maps/umayyads/01-ledgers-of-damascus.svg",
  "mainRouteLengthStraightTiles": 131.07,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        166.84,
        205.38
      ],
      [
        202.84,
        205.38
      ]
    ],
    "widthTiles": 6,
    "distanceTiles": 36.0,
    "placement": "fictional local supply circuit on SAME bank/plateau in receiving district; validate terrain and footprints, no invented river crossing",
    "twoRoundTripFormula": "4 * measured one-way navigable distance / measured convoy speed + loading/reaction allowance"
  },
  "explorationPlan": {
    "classification": "regional sectors for fictional optional activity; not ancient sites or surveyed routes",
    "sectors": [
      {
        "id": "optional-1",
        "centreTiles": [
          96.93,
          96.93
        ],
        "radiusTiles": 30,
        "title": {
          "en": "A merchant’s side account — 1",
          "es-ES": "La cuenta lateral de un mercader — 1"
        },
        "task": "reveal-reserve-approach",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {},
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": "wave-2 approach",
        "onceFlag": "01-ledgers-of-damascus.optional-1.claimed",
        "mandatory": false,
        "narrator": "yasir-cloth-merchant",
        "response": {
          "en": "Count the return journey before praising the distance.",
          "es-ES": "Cuenta el viaje de regreso antes de elogiar la distancia."
        }
      },
      {
        "id": "optional-2",
        "centreTiles": [
          262.07,
          96.93
        ],
        "radiusTiles": 30,
        "title": {
          "en": "A merchant’s side account — 2",
          "es-ES": "La cuenta lateral de un mercader — 2"
        },
        "task": "collect-finite-cache",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {
          "food": 300,
          "wood": 150,
          "gold": 75,
          "stone": 0
        },
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": null,
        "onceFlag": "01-ledgers-of-damascus.optional-2.claimed",
        "mandatory": false,
        "narrator": "yasir-cloth-merchant",
        "response": {
          "en": "Count the return journey before praising the distance.",
          "es-ES": "Cuenta el viaje de regreso antes de elogiar la distancia."
        }
      },
      {
        "id": "optional-3",
        "centreTiles": [
          96.93,
          262.07
        ],
        "radiusTiles": 30,
        "title": {
          "en": "A merchant’s side account — 3",
          "es-ES": "La cuenta lateral de un mercader — 3"
        },
        "task": "reveal-relief-corridor",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {},
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": "relief corridor",
        "onceFlag": "01-ledgers-of-damascus.optional-3.claimed",
        "mandatory": false,
        "narrator": "yasir-cloth-merchant",
        "response": {
          "en": "Count the return journey before praising the distance.",
          "es-ES": "Cuenta el viaje de regreso antes de elogiar la distancia."
        }
      },
      {
        "id": "optional-4",
        "centreTiles": [
          262.07,
          262.07
        ],
        "radiusTiles": 30,
        "title": {
          "en": "A merchant’s side account — 4",
          "es-ES": "La cuenta lateral de un mercader — 4"
        },
        "task": "collect-finite-cache",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {
          "food": 300,
          "wood": 150,
          "gold": 75,
          "stone": 0
        },
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": null,
        "onceFlag": "01-ledgers-of-damascus.optional-4.claimed",
        "mandatory": false,
        "narrator": "yasir-cloth-merchant",
        "response": {
          "en": "Count the return journey before praising the distance.",
          "es-ES": "Cuenta el viaje de regreso antes de elogiar la distancia."
        }
      }
    ],
    "connectingTrails": "four optional scouting sectors link to main/relief corridors by paths following real terrain. Rest/lookout every25–55 navigable tiles; do not turn the full map into a forced perimeter march.",
    "qualityGate": "architect certifies each sector location against raster terrain, coast and relief; no new historical claim or geography deformation to make a cache reachable"
  }
}
```

## Objectives, entity ledgers and state machine

Every predicate requires the actual world-state operation, not a timer approximating success. Coordinates below specify district plus local offset; validate actual footprint and terrain before assigning engine IDs.

```json
{
  "objectives": [
    {
      "id": "o1",
      "text": {
        "en": "Reconnect three stores in the Ghouta to the civic road.",
        "es-ES": "Reconecta tres almacenes de la Ghouta con el camino cívico."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "01-ledgers-of-damascus.o1",
        "oncePerEntity": true,
        "required": 3
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "connect-settlement",
      "threshold": 3,
      "entities": [
        {
          "id": "01-ledgers-of-damascus.o1.main-access-blocker.1",
          "role": "military-guard",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "01-ledgers-of-damascus.o1.main-access-blocker.2",
          "role": "military-guard",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "01-ledgers-of-damascus.o1.main-access-blocker.3",
          "role": "military-guard",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top",
          "countedOnce": true,
          "atHub": "hub-1"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "connect-settlement",
        "requiredCount": 3,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "main-access",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "01-ledgers-of-damascus.o1.main-access.1",
              "01-ledgers-of-damascus.o1.main-access.2",
              "01-ledgers-of-damascus.o1.main-access.3"
            ],
            "blockingEnemies": [
              "01-ledgers-of-damascus.o1.main-access-blocker.1",
              "01-ledgers-of-damascus.o1.main-access-blocker.2",
              "01-ledgers-of-damascus.o1.main-access-blocker.3"
            ],
            "requiredCount": 3,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          }
        ],
        "requiredLedgers": [
          "main-access"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Deliver two district inventories and provisions without seizing the workshops.",
        "es-ES": "Entrega dos inventarios de barrio y víveres sin tomar los talleres."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "01-ledgers-of-damascus.o2",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "collect-inventory",
      "threshold": 2,
      "entities": [
        {
          "id": "01-ledgers-of-damascus.o2.main-entities.1",
          "role": "record-token",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "01-ledgers-of-damascus.o2.main-entities.2",
          "role": "record-token",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "collect-inventory",
        "requiredCount": 2,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "food": 600
        },
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "main-entities",
            "kind": "entity-state",
            "state": "collected",
            "entities": [
              "01-ledgers-of-damascus.o2.main-entities.1",
              "01-ledgers-of-damascus.o2.main-entities.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true,
            "destinations": {
              "01-ledgers-of-damascus.o2.main-entities.1": "01-ledgers-of-damascus.o2.main-entities.receiving-zone",
              "01-ledgers-of-damascus.o2.main-entities.2": "01-ledgers-of-damascus.o2.main-entities.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "district-provisions",
            "kind": "resource-transaction",
            "amounts": {
              "food": 600
            },
            "receivingZones": [
              "01-ledgers-of-damascus.district-provisions-receiver.1"
            ],
            "allocations": {
              "01-ledgers-of-damascus.district-provisions-receiver.1": {
                "food": 600
              }
            },
            "paidFlag": "01-ledgers-of-damascus.o2.district-provisions.paid",
            "account": "spendable",
            "atomic": true,
            "once": true,
            "commit": "debit resources AND persist receipt in same guarded transition; repeated arrivals/save cannot repay"
          },
          {
            "id": "protect-workshops",
            "kind": "civilian-protection",
            "zones": [
              "01-ledgers-of-damascus.protect-workshops.1",
              "01-ledgers-of-damascus.protect-workshops.2"
            ],
            "rule": "no player damage, seizure or conversion of protected civilian sites",
            "implementation": "neutral diplomacy + disable conversion/capture; illegal player attack order refused; do not fail for AI collateral",
            "activeFrom": "briefing",
            "activeUntil": "victory"
          }
        ],
        "requiredLedgers": [
          "main-entities",
          "district-provisions",
          "protect-workshops"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Open the eastern caravan route and register its first shipment.",
        "es-ES": "Abre la ruta oriental de caravanas y registra su primer envío."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "01-ledgers-of-damascus.o3",
        "oncePerEntity": true,
        "required": 1
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "escort-caravan",
      "threshold": 1,
      "entities": [
        {
          "id": "01-ledgers-of-damascus.eastern-route-blocker.1",
          "role": "military-guard",
          "initialHub": "hub-3",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top",
          "countedOnce": true,
          "atHub": "hub-3"
        },
        {
          "id": "01-ledgers-of-damascus.o3.main-entities.1",
          "role": "caravan",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "escort-caravan",
        "requiredCount": 1,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "main-entities",
            "kind": "entity-state",
            "state": "arrived",
            "entities": [
              "01-ledgers-of-damascus.o3.main-entities.1"
            ],
            "requiredCount": 1,
            "oncePerEntity": true,
            "destinations": {
              "01-ledgers-of-damascus.o3.main-entities.1": "01-ledgers-of-damascus.o3.main-entities.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "eastern-route",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "01-ledgers-of-damascus.eastern-route.1"
            ],
            "blockingEnemies": [
              "01-ledgers-of-damascus.eastern-route-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          }
        ],
        "requiredLedgers": [
          "main-entities",
          "eastern-route"
        ],
        "allRequired": true
      }
    }
  ],
  "worldContract": {
    "version": 1,
    "classification": "authoring specification, not implemented DSL",
    "entities": [
      {
        "id": "01-ledgers-of-damascus.o2.main-entities.1",
        "role": "record-token",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "01-ledgers-of-damascus.o2.main-entities.2",
        "role": "record-token",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "01-ledgers-of-damascus.o3.main-entities.1",
        "role": "caravan",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "01-ledgers-of-damascus.eastern-route-blocker.1",
        "role": "military-guard",
        "initialHub": "hub-3",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
        "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top"
      },
      {
        "id": "01-ledgers-of-damascus.o1.main-access-blocker.1",
        "role": "military-guard",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
        "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top"
      },
      {
        "id": "01-ledgers-of-damascus.o1.main-access-blocker.2",
        "role": "military-guard",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
        "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top"
      },
      {
        "id": "01-ledgers-of-damascus.o1.main-access-blocker.3",
        "role": "military-guard",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
        "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top"
      }
    ],
    "zones": [
      {
        "id": "01-ledgers-of-damascus.district-provisions-receiver.1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "01-ledgers-of-damascus.protect-workshops.1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": true
      },
      {
        "id": "01-ledgers-of-damascus.protect-workshops.2",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": true
      },
      {
        "id": "01-ledgers-of-damascus.eastern-route.1",
        "hub": "hub-3",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "01-ledgers-of-damascus.o2.main-entities.receiving-zone",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid ground within geographic district; receiving zone excludes origins",
        "protectedCivilian": false
      },
      {
        "id": "01-ledgers-of-damascus.o3.main-entities.receiving-zone",
        "hub": "hub-3",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid ground within geographic district; receiving zone excludes origins",
        "protectedCivilian": false
      },
      {
        "id": "01-ledgers-of-damascus.o1.main-access.1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "01-ledgers-of-damascus.o1.main-access.2",
        "hub": "hub-1",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "01-ledgers-of-damascus.o1.main-access.3",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      }
    ],
    "ledgerPolicy": "persist exact object IDs, allocations, receipt flags, pairing and phase. Compound objectives require EVERY listed requirement; shared families/copies retain identity between phases.",
    "resourcePolicy": "protected-recovery is separate from spendable; no double-count in ledgers; no infinite consignment or fifth engine resource",
    "defeatPolicy": "below required possible survivors is unrecoverable; recoverable carriers retain their token via one helper; historical deaths remain narrated, not killable units",
    "earlyDelivery": "Observation is always active. Only phase transition and announced effects are phase-gated. Preserve token origin, owner and already-counted receipt through save/load.",
    "survivorGroups": [],
    "enemyBinding": "Bind every military-guard and military-post entity to a unique initialEnemy roster member. They consume that budget; never add objective guards on top of initial composition."
  },
  "states": {
    "states": [
      "briefing",
      "phase-1",
      "phase-2",
      "phase-3",
      "victory",
      "defeat"
    ],
    "transitions": [
      "briefing → phase-1 after skippable two-voice intro",
      "phase-1 → phase-2 when o1 latched",
      "phase-2 → phase-3 when o2 latched",
      "phase-3 → victory when o3 and all required survivor constraints met",
      "any non-terminal → defeat only on declared unrecoverable constraint"
    ],
    "terminalPriority": "defeat evaluated first; one terminal latch, choice order documented",
    "saveLoad": "Persist phases, delivered entity IDs, paid flags, wave releases, recovered archive flags and terminal latch. Re-entering zone or reloading cannot issue resources twice.",
    "phaseClock": "Relative timer starts on phase entry. Current absolute scenario timers cannot implement this contract; capability proposal required."
  },
  "roster": {
    "player": {
      "fictionalCommander": 0,
      "essentialHeroDefeat": false,
      "escortArchetypes": {
        "militia": 0.5,
        "spearman": 0.25,
        "archer": 0.25
      },
      "villagers": 12,
      "carriers": "one noncombat carrier per task entity, all named fictional",
      "fixedEnemyPosts": 0,
      "preplacedBatteringRams": 0
    },
    "enemyCiv": "Saracens",
    "proxyCautions": "These are engine proxies. No generic religious race, no monks representing forced belief. Enemy units are military/raider gameplay groups, not every neighbouring civilian.",
    "entityRepresentation": {
      "record": "named noncombat carrier with physical copy object/token, no magical relic bonus",
      "wagon": "Trade Cart visual proxy with trading disabled; fixed consignments and no renewable trade gold",
      "family": "named villager groups, no farming/economic AI when representing escorted parties",
      "military-post": "Watch Tower base DE proxy; two objectives have stable unit IDs, unrelated civilians excluded",
      "water": "named noncombat consignment, amount of water is narrative inventory, not an undocumented fifth engine resource",
      "commander": "named fictional Militia proxy, essential only when objective explicitly requires commander; no sacred unit",
      "recovery": "four preplaced guards released once with protected resources, persisting after save/load"
    }
  }
}
```

## Difficulty and finite budget

These are explicit estimates for calibration, not measured wins or evidence of perfect balance. Player starting military is preplaced; enemy initial/waves are one roster with production disabled. Nominal militia/spearman/archer/scout costs audit the plan, not historical army numbers. Resource banks include mandatory delivery, replacement allowance, protected recovery and a surplus.

| Profile | Start F/W/G/S | Gatherable F/W/G/S | Escort | Initial + waves | Warning / gap seconds |
|---|---|---|---:|---|---|
| easy | 875/625/312/250 | 2485/1075/1128/550 | 16 | 6 + 6 + 6 + 9 = 27 | 120 / 474 |
| standard | 700/500/250/200 | 2420/1100/1030/600 | 12 | 9 + 9 + 9 + 9 = 36 | 90 / 370 |
| hard | 595/425/212/170 | 2405/1125/988/630 | 10 | 10 + 10 + 10 + 13 = 43 | 75 / 296 |

```json
{
  "profiles": {
    "easy": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 875,
        "wood": 625,
        "gold": 312,
        "stone": 250
      },
      "gatherableBank": {
        "food": 2485,
        "wood": 1075,
        "gold": 1128,
        "stone": 550
      },
      "mandatoryDeliveries": {
        "food": 600,
        "wood": 0,
        "gold": 0,
        "stone": 0
      },
      "protectedRecoveryStock": {
        "food": 300,
        "wood": 200,
        "gold": 100,
        "stone": 0
      },
      "maxVillagers": 18,
      "startingEscortCount": 16,
      "playerPopulationCap": 90,
      "enemyTotalCap": 27,
      "initialEnemy": 6,
      "waves": [
        {
          "id": "wave-1",
          "count": 6,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 474,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 6,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 948,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 9,
          "composition": {
            "militia": 4,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1422,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 3,
        "spearman": 1,
        "archer": 1,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1275,
        "wood": 250,
        "gold": 485,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 1560,
        "wood": 1000,
        "gold": 840,
        "stone": 300
      },
      "roughDurationMinutes": [
        25,
        55
      ],
      "objectiveThresholds": "Identical in all difficulties; 6/8 civilian tolerance stays 6/8; no harder historical outcome.",
      "tactics": "one approach at a time; show full route",
      "reactionMarginSeconds": 120,
      "movementSpeed": "native unchanged; no difficulty HP, damage or speed cheats",
      "criticalUnitDefeat": "essential fictional commander only if explicitly named in objective; civilians 6/8 threshold on evacuation missions, courier replacement before defeat otherwise",
      "supplyMargins": {
        "food": 900,
        "wood": 500,
        "gold": 500,
        "stone": 500
      },
      "playerStartingMilitary": {
        "militia": 8,
        "spearman": 4,
        "archer": 4
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts."
    },
    "standard": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 700,
        "wood": 500,
        "gold": 250,
        "stone": 200
      },
      "gatherableBank": {
        "food": 2420,
        "wood": 1100,
        "gold": 1030,
        "stone": 600
      },
      "mandatoryDeliveries": {
        "food": 600,
        "wood": 0,
        "gold": 0,
        "stone": 0
      },
      "protectedRecoveryStock": {
        "food": 300,
        "wood": 200,
        "gold": 100,
        "stone": 0
      },
      "maxVillagers": 18,
      "startingEscortCount": 12,
      "playerPopulationCap": 90,
      "enemyTotalCap": 36,
      "initialEnemy": 9,
      "waves": [
        {
          "id": "wave-1",
          "count": 9,
          "composition": {
            "militia": 4,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 370,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 9,
          "composition": {
            "militia": 4,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 740,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 9,
          "composition": {
            "militia": 4,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1110,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 4,
        "spearman": 2,
        "archer": 2,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1560,
        "wood": 400,
        "gold": 680,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 1320,
        "wood": 900,
        "gold": 680,
        "stone": 300
      },
      "roughDurationMinutes": [
        25,
        55
      ],
      "objectiveThresholds": "Identical in all difficulties; 6/8 civilian tolerance stays 6/8; no harder historical outcome.",
      "tactics": "alternate main and flank; show warning + scoutable approach",
      "reactionMarginSeconds": 90,
      "movementSpeed": "native unchanged; no difficulty HP, damage or speed cheats",
      "criticalUnitDefeat": "essential fictional commander only if explicitly named in objective; civilians 6/8 threshold on evacuation missions, courier replacement before defeat otherwise",
      "supplyMargins": {
        "food": 900,
        "wood": 500,
        "gold": 500,
        "stone": 500
      },
      "playerStartingMilitary": {
        "militia": 6,
        "spearman": 3,
        "archer": 3
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts."
    },
    "hard": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 595,
        "wood": 425,
        "gold": 212,
        "stone": 170
      },
      "gatherableBank": {
        "food": 2405,
        "wood": 1125,
        "gold": 988,
        "stone": 630
      },
      "mandatoryDeliveries": {
        "food": 600,
        "wood": 0,
        "gold": 0,
        "stone": 0
      },
      "protectedRecoveryStock": {
        "food": 300,
        "wood": 200,
        "gold": 100,
        "stone": 0
      },
      "maxVillagers": 18,
      "startingEscortCount": 10,
      "playerPopulationCap": 90,
      "enemyTotalCap": 43,
      "initialEnemy": 10,
      "waves": [
        {
          "id": "wave-1",
          "count": 10,
          "composition": {
            "militia": 5,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 296,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 10,
          "composition": {
            "militia": 5,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 592,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 13,
          "composition": {
            "militia": 5,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 888,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 5,
        "spearman": 2,
        "archer": 2,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1915,
        "wood": 450,
        "gold": 805,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 1200,
        "wood": 850,
        "gold": 600,
        "stone": 300
      },
      "roughDurationMinutes": [
        25,
        55
      ],
      "objectiveThresholds": "Identical in all difficulties; 6/8 civilian tolerance stays 6/8; no harder historical outcome.",
      "tactics": "wave 2 two scoutable approaches, waves remain capped; force escort/reserve split without simultaneous blind spawns",
      "reactionMarginSeconds": 75,
      "movementSpeed": "native unchanged; no difficulty HP, damage or speed cheats",
      "criticalUnitDefeat": "essential fictional commander only if explicitly named in objective; civilians 6/8 threshold on evacuation missions, courier replacement before defeat otherwise",
      "supplyMargins": {
        "food": 900,
        "wood": 500,
        "gold": 500,
        "stone": 500
      },
      "playerStartingMilitary": {
        "militia": 5,
        "spearman": 2,
        "archer": 3
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts."
    }
  },
  "analysis": {
    "classification": "feasibility envelope, not a combat simulation or proof of balance",
    "startingWorkers": 12,
    "plannedPeakWorkers": 18,
    "effectiveGatherRatePerWorkerResourcePerSecondAssumption": 0.24,
    "walkingAndIdleIncluded": "Assumed rate discounts native gathering for travel/idle; measure actual efficiency in game.",
    "worstDeliveryFood": 600,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Phase waves use the separate local phase-two supply circuit, not the whole-map journey. Two round trips +90s loading/reaction fit the floor. Validate actual nav-path/speed and recompute before game approval.",
    "minimumWaveGapSecondsFromProposedGeometry": 296,
    "wholeJourneyDistanceTiles": 149.64,
    "wholeJourneyOneWaySecondsEstimate": 214,
    "optionalCacheAllocation": {
      "food": 600,
      "wood": 300,
      "gold": 150,
      "stone": 0
    },
    "solventWithoutOptionalCaches": true
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Dos puentes de Barada/calles alternativas; talleres civiles no convertibles. Inventarios no bloquean por matar administrador ficticio: segundo escribiente.

{
  "plan": "Dos puentes de Barada/calles alternativas; talleres civiles no convertibles. Inventarios no bloquean por matar administrador ficticio: segundo escribiente.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.umayyads.01-ledgers-of-damascus.title` / always | none → next | Ledgers of Damascus | Los registros de Damasco |
| `scenario.umayyads.01-ledgers-of-damascus.fact-intro` / intro first | collection-narrator → next | Muawiya’s rule after 661 began the Umayyad dynastic period. Damascus’s later monumental mosque did not yet exist in this form. | Muawiya establece gobierno omeya con centro en Damasco. Identidad lingüística/religiosa de provincias no se homogeneiza en ese año. |
| `scenario.umayyads.01-ledgers-of-damascus.personal-intro` / after fact-intro | yasir-cloth-merchant → next | This account predates my mother. I know the sum because she preserved it; I do not know whether the clerk smiled when he wrote it. | Esta cuenta es anterior a mi madre. Conozco la suma porque la conservó; no sé si sonreía el escribiente que la anotó. |
| `scenario.umayyads.01-ledgers-of-damascus.objective-1` / phase-1 active | none → hub-1 | Reconnect three stores in the Ghouta to the civic road. | Reconecta tres almacenes de la Ghouta con el camino cívico. |
| `scenario.umayyads.01-ledgers-of-damascus.objective-2` / phase-2 active | none → hub-2 | Deliver two district inventories and provisions without seizing the workshops. | Entrega dos inventarios de barrio y víveres sin tomar los talleres. |
| `scenario.umayyads.01-ledgers-of-damascus.objective-3` / phase-3 active | none → hub-3 | Open the eastern caravan route and register its first shipment. | Abre la ruta oriental de caravanas y registra su primer envío. |
| `scenario.umayyads.01-ledgers-of-damascus.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.umayyads.01-ledgers-of-damascus.scouts` / scouts panel | none → next | Regional setting: Damascus / Ghouta. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Damascus / Ghouta. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.umayyads.01-ledgers-of-damascus.history` / history panel | none → next | Muawiya’s rule after 661 began the Umayyad dynastic period. Damascus’s later monumental mosque did not yet exist in this form. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Muawiya establece gobierno omeya con centro en Damasco. Identidad lingüística/religiosa de provincias no se homogeneiza en ese año. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.umayyads.01-ledgers-of-damascus.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.umayyads.01-ledgers-of-damascus.event-phase-1-complete` / o1 first becomes true | yasir-cloth-merchant → next | The first load arrived. My family’s old accounts rarely mention the people who carried it. | La primera carga ha llegado. Las cuentas antiguas de mi familia apenas nombran a quienes la llevaron. |
| `scenario.umayyads.01-ledgers-of-damascus.event-phase-2-complete` / o2 first becomes true | yasir-cloth-merchant → next | Keep the shore store supplied. An ambitious road still needs somewhere to return. | Mantén abastecido el almacén de la costa. Hasta un camino ambicioso necesita un lugar al que volver. |
| `scenario.umayyads.01-ledgers-of-damascus.event-phase-3-complete` / o3 first becomes true | yasir-cloth-merchant → next | The ledger survived. That is less than victory, and more than nothing. | El registro sobrevivió. Es menos que una victoria y más que nada. |
| `scenario.umayyads.01-ledgers-of-damascus.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | yasir-cloth-merchant → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.umayyads.01-ledgers-of-damascus.victory-fact` / victory latch first | collection-narrator → next | Muawiya’s rule after 661 began the Umayyad dynastic period. Damascus’s later monumental mosque did not yet exist in this form. Your mission task is complete; this outcome does not change the documented events. | La gran mezquita de al-Walid no existe aún en mapa de 661. Representar administración, no victoria sobre edificios religiosos. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.umayyads.01-ledgers-of-damascus.victory-personal` / after victory-fact | yasir-cloth-merchant → 02-stone-and-memory | The ledger survived. That is less than victory, and more than nothing. | El registro sobrevivió. Es menos que una victoria y más que nada. |
| `scenario.umayyads.01-ledgers-of-damascus.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.umayyads.01-ledgers-of-damascus.recovery` / 6 minutes without objective progress | yasir-cloth-merchant → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.umayyads.01-ledgers-of-damascus.optional-1` / optional sector observed/cache claimed; once, independent of main phase | yasir-cloth-merchant → return-to-game | A merchant’s side account — 1: The hidden reserve approach is now marked. Count the return journey before praising the distance. | La cuenta lateral de un mercader — 1: La aproximación de la reserva está señalada. Cuenta el viaje de regreso antes de elogiar la distancia. |
| `scenario.umayyads.01-ledgers-of-damascus.optional-2` / optional sector observed/cache claimed; once, independent of main phase | yasir-cloth-merchant → return-to-game | A merchant’s side account — 2: One cache: 300 food, 150 wood and 75 gold. It can be claimed once. Count the return journey before praising the distance. | La cuenta lateral de un mercader — 2: Un depósito: 300 de alimento, 150 de madera y 75 de oro. Solo se puede reclamar una vez. Cuenta el viaje de regreso antes de elogiar la distancia. |
| `scenario.umayyads.01-ledgers-of-damascus.optional-3` / optional sector observed/cache claimed; once, independent of main phase | yasir-cloth-merchant → return-to-game | A merchant’s side account — 3: The relief route is now marked. Count the return journey before praising the distance. | La cuenta lateral de un mercader — 3: La ruta alternativa está señalada. Cuenta el viaje de regreso antes de elogiar la distancia. |
| `scenario.umayyads.01-ledgers-of-damascus.optional-4` / optional sector observed/cache claimed; once, independent of main phase | yasir-cloth-merchant → return-to-game | A merchant’s side account — 4: One cache: 300 food, 150 wood and 75 gold. It can be claimed once. Count the return journey before praising the distance. | La cuenta lateral de un mercader — 4: Un depósito: 300 de alimento, 150 de madera y 75 de oro. Solo se puede reclamar una vez. Cuenta el viaje de regreso antes de elogiar la distancia. |

## Adversarial QA

- `historical-facts` (pending): All narrator facts link to claim/source; uncertainty spoken when essential; fictional dialogue labelled.
- `map-geography` (pending): Landmark banks and coast orientation match regional controls; no anachronisms listed in profile.
- `footprint-and-transport` (pending): Flood fill with unit footprint, bridge/naval checks; land routes cannot jump water; largest convoy reaches all goals.
- `early-completion` (pending): Targets destroyed/archives saved before activation latch and unlock later objectives.
- `save-load-ledger` (pending): Save before/after every delivery and wave; reload cannot duplicate or lose counts.
- `finite-enemy` (pending): Roster initial plus three waves <= cap in each difficulty; all enemy production off.
- `loss-recovery` (pending): Lose one courier/boat or two families; documented fallback exists without repeating payments.
- `difficulty` (pending): Normal success rates 60–80% familiar AoE2 cohort, easy 80–95% learning cohort, hard 35–60% expert blind cohort: hypotheses, not measurements.
- `narration` (pending): General factual brief then campaign person; no omniscience or lived memory before birth.
- `localization` (pending): All screens EN and es-ES, 17 full destination catalogs reviewed for release; no implicit engine fallback.
- `performance` (pending): Recorded 20min crowded replay below frame/simulation degradation budget.
- `continuity` (pending): Fresh/profile one-route/both/unknown/replay preserve cumulative keys and nonblocking static recommendation.
