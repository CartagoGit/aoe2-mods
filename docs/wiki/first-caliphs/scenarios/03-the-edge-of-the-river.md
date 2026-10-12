# The Edge of the River / Al borde del río

`first-caliphs/03-the-edge-of-the-river` · 636 CE · combined-arms-battle

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/first-caliphs/03-the-edge-of-the-river.svg)

## Historical frame and outcome

The battle of Yarmuk in 636 ended in defeat for the Byzantine army. Late accounts do not establish precise numbers or every tactical detail.

Victoria árabe ante fuerzas romano-orientales en Yarmuk. Despliegues, efectivos y cadenas de soldados del relato tardío no se toman como precisión.

Resultado militar histórico; no exterminio obligatorio ni cifras de fuente convertidas a spawns.

- [Al-Baladhuri, The Battle of Yarmuk](https://sourcebooks.web.fordham.edu/source/yarmuk.asp): Descripción y episodios posteriores. Autor del siglo IX; enormes efectivos y discursos no son datos seguros.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

From the supply line I saw dust before I saw standards. Later I heard tidy accounts of the battle. My own account begins with the men returning thirsty.

Desde la línea de suministro vi polvo antes que estandartes. Después oí relatos ordenados. El mío comienza con hombres que regresaban sedientos.

## Geography and map construction

Yarmuk and Golan approaches — 400 × 400 tiles; north-up design controls [35.7, 32.63, 36.15, 33.02].

Llanuras/mesetas al norte de cañones; vegetación mediterránea discontinua.

Yarmuk fluye hacia oeste y Jordán; barrancos al sur y oeste del campo esquemático.

Escarpes de cauce y Golan al norte; no cruzables por cualquier unidad.

Aproximaciones por meseta noreste; pasos al suroeste, despliegue exacto reconstruido.

Exclude: Sin puente ferroviario moderno ni oleadas equivalentes a cifras de crónica.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Regional plateau, not exact camp | [35.96, 32.85] | [226.37, 176.66] |
| Yarmuk gorge corridor | [35.91, 32.7] | [187.99, 313.68] |
| Western ravine approach | [35.79, 32.77] | [95.87, 249.74] |

```json
{
  "bbox": [
    35.7,
    32.63,
    36.15,
    33.02
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Regional plateau, not exact camp",
      "lonLat": [
        35.96,
        32.85
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        226.37,
        176.66
      ]
    },
    {
      "id": "anchor-2",
      "name": "Yarmuk gorge corridor",
      "lonLat": [
        35.91,
        32.7
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        187.99,
        313.68
      ]
    },
    {
      "id": "anchor-3",
      "name": "Western ravine approach",
      "lonLat": [
        35.79,
        32.77
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        95.87,
        249.74
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-1",
      "centre": [
        226.37,
        176.66
      ],
      "purpose": {
        "en": "Secure the northern supply point and the two flank paths.",
        "es-ES": "Asegura el punto de suministro norte y los dos caminos de flanco."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-3",
      "centre": [
        95.87,
        249.74
      ],
      "purpose": {
        "en": "Break the two field commands while keeping the protected supply stock at the nearby receiving point.",
        "es-ES": "Rompe los dos mandos de campaña manteniendo la reserva de suministros en el punto de recepción cercano."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-1",
      "centre": [
        226.37,
        176.66
      ],
      "purpose": {
        "en": "Hold the rally plateau and reopen the road for the supply train.",
        "es-ES": "Conserva la meseta de reunión y reabre el camino al tren de víveres."
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
          226.37,
          176.66
        ],
        [
          95.87,
          249.74
        ],
        [
          226.37,
          176.66
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          226.37,
          176.66
        ],
        [
          169.12,
          221.2
        ],
        [
          95.87,
          249.74
        ],
        [
          226.37,
          176.66
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        36.15,
        32.72
      ],
      [
        36.03,
        32.71
      ],
      [
        35.95,
        32.7
      ],
      [
        35.9,
        32.71
      ],
      [
        35.82,
        32.7
      ],
      [
        35.77,
        32.65
      ],
      [
        35.72,
        32.645
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "yarmuk",
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
  "asset": "docs/design/maps/first-caliphs/03-the-edge-of-the-river.svg",
  "mainRouteLengthStraightTiles": 291.86,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        77.87,
        261.74
      ],
      [
        113.87,
        261.74
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
          107.73,
          107.73
        ],
        "radiusTiles": 30,
        "title": {
          "en": "The caravan’s lookout — 1",
          "es-ES": "El vigía de la caravana — 1"
        },
        "task": "reveal-reserve-approach",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {},
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": "wave-2 approach",
        "onceFlag": "03-the-edge-of-the-river.optional-1.claimed",
        "mandatory": false,
        "narrator": "salim-caravan-scribe",
        "response": {
          "en": "A ledger of wells is useful only if the road between them is known.",
          "es-ES": "Un registro de pozos solo sirve si conocemos el camino que los une."
        }
      },
      {
        "id": "optional-2",
        "centreTiles": [
          291.27,
          107.73
        ],
        "radiusTiles": 30,
        "title": {
          "en": "The caravan’s lookout — 2",
          "es-ES": "El vigía de la caravana — 2"
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
        "onceFlag": "03-the-edge-of-the-river.optional-2.claimed",
        "mandatory": false,
        "narrator": "salim-caravan-scribe",
        "response": {
          "en": "A ledger of wells is useful only if the road between them is known.",
          "es-ES": "Un registro de pozos solo sirve si conocemos el camino que los une."
        }
      },
      {
        "id": "optional-3",
        "centreTiles": [
          107.73,
          291.27
        ],
        "radiusTiles": 30,
        "title": {
          "en": "The caravan’s lookout — 3",
          "es-ES": "El vigía de la caravana — 3"
        },
        "task": "reveal-relief-corridor",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {},
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": "relief corridor",
        "onceFlag": "03-the-edge-of-the-river.optional-3.claimed",
        "mandatory": false,
        "narrator": "salim-caravan-scribe",
        "response": {
          "en": "A ledger of wells is useful only if the road between them is known.",
          "es-ES": "Un registro de pozos solo sirve si conocemos el camino que los une."
        }
      },
      {
        "id": "optional-4",
        "centreTiles": [
          291.27,
          291.27
        ],
        "radiusTiles": 30,
        "title": {
          "en": "The caravan’s lookout — 4",
          "es-ES": "El vigía de la caravana — 4"
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
        "onceFlag": "03-the-edge-of-the-river.optional-4.claimed",
        "mandatory": false,
        "narrator": "salim-caravan-scribe",
        "response": {
          "en": "A ledger of wells is useful only if the road between them is known.",
          "es-ES": "Un registro de pozos solo sirve si conocemos el camino que los une."
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
        "en": "Secure the northern supply point and the two flank paths.",
        "es-ES": "Asegura el punto de suministro norte y los dos caminos de flanco."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "03-the-edge-of-the-river.o1",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "secure-corridor",
      "threshold": 2,
      "entities": [
        {
          "id": "03-the-edge-of-the-river.northern-point-blocker.1",
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
          "id": "03-the-edge-of-the-river.o1.main-access-blocker.1",
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
          "id": "03-the-edge-of-the-river.o1.main-access-blocker.2",
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
          "id": "03-the-edge-of-the-river.two-flanks-blocker.1",
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
          "id": "03-the-edge-of-the-river.two-flanks-blocker.2",
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
        "operation": "secure-corridor",
        "requiredCount": 2,
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
              "03-the-edge-of-the-river.o1.main-access.1",
              "03-the-edge-of-the-river.o1.main-access.2"
            ],
            "blockingEnemies": [
              "03-the-edge-of-the-river.o1.main-access-blocker.1",
              "03-the-edge-of-the-river.o1.main-access-blocker.2"
            ],
            "requiredCount": 2,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          },
          {
            "id": "northern-point",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "03-the-edge-of-the-river.northern-point.1"
            ],
            "blockingEnemies": [
              "03-the-edge-of-the-river.northern-point-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          },
          {
            "id": "two-flanks",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "03-the-edge-of-the-river.two-flanks.1",
              "03-the-edge-of-the-river.two-flanks.2"
            ],
            "blockingEnemies": [
              "03-the-edge-of-the-river.two-flanks-blocker.1",
              "03-the-edge-of-the-river.two-flanks-blocker.2"
            ],
            "requiredCount": 2,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          }
        ],
        "requiredLedgers": [
          "main-access",
          "northern-point",
          "two-flanks"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Break the two field commands while keeping the protected supply stock at the nearby receiving point.",
        "es-ES": "Rompe los dos mandos de campaña manteniendo la reserva de suministros en el punto de recepción cercano."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "03-the-edge-of-the-river.o2",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "destroy-military-post",
      "threshold": 2,
      "entities": [
        {
          "id": "03-the-edge-of-the-river.o2-post.1",
          "role": "military-post",
          "initialHub": "hub-2",
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
          "atHub": "hub-2"
        },
        {
          "id": "03-the-edge-of-the-river.o2-post.2",
          "role": "military-post",
          "initialHub": "hub-2",
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
          "atHub": "hub-2"
        },
        {
          "id": "03-the-edge-of-the-river.protected-supply-stock",
          "role": "protected-stock-wagon",
          "initialHub": "hub-2",
          "offsetTiles": [
            -8,
            8
          ],
          "finite": true,
          "initiallyDelivered": false,
          "identity": "fictional local supply reserve",
          "replacement": "protected recovery stock already budgeted; never adds resources",
          "countedOnce": true,
          "atHub": "hub-2"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "destroy-military-post",
        "requiredCount": 2,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "defeated-posts",
            "kind": "entity-state",
            "state": "destroyed",
            "entities": [
              "03-the-edge-of-the-river.o2-post.1",
              "03-the-edge-of-the-river.o2-post.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true
          },
          {
            "id": "reserve-in-reach",
            "kind": "minimum-stock",
            "account": "protected-recovery",
            "amounts": {
              "food": 300,
              "wood": 200,
              "gold": 100,
              "stone": 0
            },
            "evaluate": "at completion; separately reserved, cannot fund mandatory transactions",
            "atHub": "hub-2",
            "maximumNavigableDistanceTiles": 36,
            "accountEntityIds": [
              "03-the-edge-of-the-river.protected-supply-stock"
            ]
          }
        ],
        "requiredLedgers": [
          "defeated-posts",
          "reserve-in-reach"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Hold the rally plateau and reopen the road for the supply train.",
        "es-ES": "Conserva la meseta de reunión y reabre el camino al tren de víveres."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "03-the-edge-of-the-river.o3",
        "oncePerEntity": true,
        "required": 1
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "secure-rally",
      "threshold": 1,
      "entities": [
        {
          "id": "03-the-edge-of-the-river.o3.main-access-blocker.1",
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
          "id": "03-the-edge-of-the-river.train-road-blocker.1",
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
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "secure-rally",
        "requiredCount": 1,
        "destination": "hub-3",
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
              "03-the-edge-of-the-river.o3.main-access.1"
            ],
            "blockingEnemies": [
              "03-the-edge-of-the-river.o3.main-access-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          },
          {
            "id": "train-road",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "03-the-edge-of-the-river.train-road.1"
            ],
            "blockingEnemies": [
              "03-the-edge-of-the-river.train-road-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          }
        ],
        "requiredLedgers": [
          "main-access",
          "train-road"
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
        "id": "03-the-edge-of-the-river.northern-point-blocker.1",
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
        "id": "03-the-edge-of-the-river.two-flanks-blocker.1",
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
        "id": "03-the-edge-of-the-river.two-flanks-blocker.2",
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
        "id": "03-the-edge-of-the-river.o2-post.1",
        "role": "military-post",
        "initialHub": "hub-2",
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
        "id": "03-the-edge-of-the-river.o2-post.2",
        "role": "military-post",
        "initialHub": "hub-2",
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
        "id": "03-the-edge-of-the-river.train-road-blocker.1",
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
        "id": "03-the-edge-of-the-river.protected-supply-stock",
        "role": "protected-stock-wagon",
        "initialHub": "hub-2",
        "offsetTiles": [
          -8,
          8
        ],
        "finite": true,
        "initiallyDelivered": false,
        "identity": "fictional local supply reserve",
        "replacement": "protected recovery stock already budgeted; never adds resources"
      },
      {
        "id": "03-the-edge-of-the-river.o1.main-access-blocker.1",
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
        "id": "03-the-edge-of-the-river.o1.main-access-blocker.2",
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
        "id": "03-the-edge-of-the-river.o3.main-access-blocker.1",
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
      }
    ],
    "zones": [
      {
        "id": "03-the-edge-of-the-river.northern-point.1",
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
        "id": "03-the-edge-of-the-river.two-flanks.1",
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
        "id": "03-the-edge-of-the-river.two-flanks.2",
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
        "id": "03-the-edge-of-the-river.train-road.1",
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
        "id": "03-the-edge-of-the-river.o1.main-access.1",
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
        "id": "03-the-edge-of-the-river.o1.main-access.2",
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
        "id": "03-the-edge-of-the-river.o3.main-access.1",
        "hub": "hub-3",
        "offsetTiles": [
          -8,
          -4
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
      "fixedEnemyPosts": 2,
      "preplacedBatteringRams": 2
    },
    "enemyCiv": "Byzantines",
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
| easy | 1125/875/500/250 | 2355/1125/1420/550 | 28 | 36 + 36 + 36 + 36 = 144 | 120 / 474 |
| standard | 900/700/400/200 | 2340/1200/1360/600 | 24 | 48 + 48 + 48 + 48 = 192 | 90 / 370 |
| hard | 765/595/340/170 | 2235/1205/1260/630 | 20 | 57 + 57 + 57 + 59 = 230 | 75 / 296 |

```json
{
  "profiles": {
    "easy": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 1125,
        "wood": 875,
        "gold": 500,
        "stone": 250
      },
      "gatherableBank": {
        "food": 2355,
        "wood": 1125,
        "gold": 1420,
        "stone": 550
      },
      "mandatoryDeliveries": {
        "food": 0,
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
      "maxVillagers": 24,
      "startingEscortCount": 28,
      "playerPopulationCap": 140,
      "enemyTotalCap": 144,
      "initialEnemy": 36,
      "waves": [
        {
          "id": "wave-1",
          "count": 36,
          "composition": {
            "militia": 12,
            "spearman": 9,
            "archer": 9,
            "scoutCavalry": 6
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 474,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 36,
          "composition": {
            "militia": 12,
            "spearman": 9,
            "archer": 9,
            "scoutCavalry": 6
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 948,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 36,
          "composition": {
            "militia": 12,
            "spearman": 9,
            "archer": 9,
            "scoutCavalry": 6
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1422,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 12,
        "spearman": 9,
        "archer": 9,
        "scoutCavalry": 6
      },
      "enemyNominalResourceCost": {
        "food": 6060,
        "wood": 1800,
        "gold": 2580,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 2280,
        "wood": 1300,
        "gold": 1320,
        "stone": 300
      },
      "roughDurationMinutes": [
        30,
        60
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
        "militia": 14,
        "spearman": 7,
        "archer": 7
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts."
    },
    "standard": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 900,
        "wood": 700,
        "gold": 400,
        "stone": 200
      },
      "gatherableBank": {
        "food": 2340,
        "wood": 1200,
        "gold": 1360,
        "stone": 600
      },
      "mandatoryDeliveries": {
        "food": 0,
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
      "maxVillagers": 24,
      "startingEscortCount": 24,
      "playerPopulationCap": 140,
      "enemyTotalCap": 192,
      "initialEnemy": 48,
      "waves": [
        {
          "id": "wave-1",
          "count": 48,
          "composition": {
            "militia": 16,
            "spearman": 12,
            "archer": 12,
            "scoutCavalry": 8
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 370,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 48,
          "composition": {
            "militia": 16,
            "spearman": 12,
            "archer": 12,
            "scoutCavalry": 8
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 740,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 48,
          "composition": {
            "militia": 16,
            "spearman": 12,
            "archer": 12,
            "scoutCavalry": 8
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1110,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 16,
        "spearman": 12,
        "archer": 12,
        "scoutCavalry": 8
      },
      "enemyNominalResourceCost": {
        "food": 8080,
        "wood": 2400,
        "gold": 3440,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 2040,
        "wood": 1200,
        "gold": 1160,
        "stone": 300
      },
      "roughDurationMinutes": [
        30,
        60
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
        "militia": 12,
        "spearman": 6,
        "archer": 6
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts."
    },
    "hard": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 765,
        "wood": 595,
        "gold": 340,
        "stone": 170
      },
      "gatherableBank": {
        "food": 2235,
        "wood": 1205,
        "gold": 1260,
        "stone": 630
      },
      "mandatoryDeliveries": {
        "food": 0,
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
      "maxVillagers": 24,
      "startingEscortCount": 20,
      "playerPopulationCap": 140,
      "enemyTotalCap": 230,
      "initialEnemy": 57,
      "waves": [
        {
          "id": "wave-1",
          "count": 57,
          "composition": {
            "militia": 20,
            "spearman": 14,
            "archer": 14,
            "scoutCavalry": 9
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 296,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 57,
          "composition": {
            "militia": 20,
            "spearman": 14,
            "archer": 14,
            "scoutCavalry": 9
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 592,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 59,
          "composition": {
            "militia": 22,
            "spearman": 14,
            "archer": 14,
            "scoutCavalry": 9
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 888,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 20,
        "spearman": 14,
        "archer": 14,
        "scoutCavalry": 9
      },
      "enemyNominalResourceCost": {
        "food": 9760,
        "wood": 2800,
        "gold": 4160,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 1800,
        "wood": 1100,
        "gold": 1000,
        "stone": 300
      },
      "roughDurationMinutes": [
        30,
        60
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
        "militia": 10,
        "spearman": 5,
        "archer": 5
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts."
    }
  },
  "analysis": {
    "classification": "feasibility envelope, not a combat simulation or proof of balance",
    "startingWorkers": 12,
    "plannedPeakWorkers": 24,
    "effectiveGatherRatePerWorkerResourcePerSecondAssumption": 0.24,
    "walkingAndIdleIncluded": "Assumed rate discounts native gathering for travel/idle; measure actual efficiency in game.",
    "worstDeliveryFood": 0,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Phase waves use the separate local phase-two supply circuit, not the whole-map journey. Two round trips +90s loading/reaction fit the floor. Validate actual nav-path/speed and recompute before game approval.",
    "minimumWaveGapSecondsFromProposedGeometry": 296,
    "wholeJourneyDistanceTiles": 299.14,
    "wholeJourneyOneWaySecondsEstimate": 428,
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

Cañón no fuerza suicidio; dos pasos señalados. Dos mandos destruidos temprano cuentan; unidades atrapadas pueden salir por meseta este.

{
  "plan": "Cañón no fuerza suicidio; dos pasos señalados. Dos mandos destruidos temprano cuentan; unidades atrapadas pueden salir por meseta este.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.first-caliphs.03-the-edge-of-the-river.title` / always | none → next | The Edge of the River | Al borde del río |
| `scenario.first-caliphs.03-the-edge-of-the-river.fact-intro` / intro first | collection-narrator → next | The battle of Yarmuk in 636 ended in defeat for the Byzantine army. Late accounts do not establish precise numbers or every tactical detail. | Victoria árabe ante fuerzas romano-orientales en Yarmuk. Despliegues, efectivos y cadenas de soldados del relato tardío no se toman como precisión. |
| `scenario.first-caliphs.03-the-edge-of-the-river.personal-intro` / after fact-intro | salim-caravan-scribe → next | From the supply line I saw dust before I saw standards. Later I heard tidy accounts of the battle. My own account begins with the men returning thirsty. | Desde la línea de suministro vi polvo antes que estandartes. Después oí relatos ordenados. El mío comienza con hombres que regresaban sedientos. |
| `scenario.first-caliphs.03-the-edge-of-the-river.objective-1` / phase-1 active | none → hub-1 | Secure the northern supply point and the two flank paths. | Asegura el punto de suministro norte y los dos caminos de flanco. |
| `scenario.first-caliphs.03-the-edge-of-the-river.objective-2` / phase-2 active | none → hub-2 | Break the two field commands while keeping the protected supply stock at the nearby receiving point. | Rompe los dos mandos de campaña manteniendo la reserva de suministros en el punto de recepción cercano. |
| `scenario.first-caliphs.03-the-edge-of-the-river.objective-3` / phase-3 active | none → hub-3 | Hold the rally plateau and reopen the road for the supply train. | Conserva la meseta de reunión y reabre el camino al tren de víveres. |
| `scenario.first-caliphs.03-the-edge-of-the-river.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.first-caliphs.03-the-edge-of-the-river.scouts` / scouts panel | none → next | Regional setting: Yarmuk and Golan approaches. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Yarmuk and Golan approaches. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.first-caliphs.03-the-edge-of-the-river.history` / history panel | none → next | The battle of Yarmuk in 636 ended in defeat for the Byzantine army. Late accounts do not establish precise numbers or every tactical detail. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Victoria árabe ante fuerzas romano-orientales en Yarmuk. Despliegues, efectivos y cadenas de soldados del relato tardío no se toman como precisión. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.first-caliphs.03-the-edge-of-the-river.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.first-caliphs.03-the-edge-of-the-river.event-phase-1-complete` / o1 first becomes true | salim-caravan-scribe → next | The first store is accounted for. Leave enough water for the return. | La primera reserva está registrada. Deja agua suficiente para la vuelta. |
| `scenario.first-caliphs.03-the-edge-of-the-river.event-phase-2-complete` / o2 first becomes true | salim-caravan-scribe → next | A road on my ledger is a journey for someone else. Keep the escort close. | Un camino en mi registro es el viaje de otra persona. Mantén cerca la escolta. |
| `scenario.first-caliphs.03-the-edge-of-the-river.event-phase-3-complete` / o3 first becomes true | salim-caravan-scribe → next | I have counted the arriving loads. I will not pretend that a ledger counts every loss. | He contado las cargas que llegan. No fingiré que un registro cuenta todas las pérdidas. |
| `scenario.first-caliphs.03-the-edge-of-the-river.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | salim-caravan-scribe → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.first-caliphs.03-the-edge-of-the-river.victory-fact` / victory latch first | collection-narrator → next | The battle of Yarmuk in 636 ended in defeat for the Byzantine army. Late accounts do not establish precise numbers or every tactical detail. Your mission task is complete; this outcome does not change the documented events. | Resultado militar histórico; no exterminio obligatorio ni cifras de fuente convertidas a spawns. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.first-caliphs.03-the-edge-of-the-river.victory-personal` / after victory-fact | salim-caravan-scribe → 04-fields-of-the-sawad | I have counted the arriving loads. I will not pretend that a ledger counts every loss. | He contado las cargas que llegan. No fingiré que un registro cuenta todas las pérdidas. |
| `scenario.first-caliphs.03-the-edge-of-the-river.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.first-caliphs.03-the-edge-of-the-river.recovery` / 6 minutes without objective progress | salim-caravan-scribe → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.first-caliphs.03-the-edge-of-the-river.optional-1` / optional sector observed/cache claimed; once, independent of main phase | salim-caravan-scribe → return-to-game | The caravan’s lookout — 1: The hidden reserve approach is now marked. A ledger of wells is useful only if the road between them is known. | El vigía de la caravana — 1: La aproximación de la reserva está señalada. Un registro de pozos solo sirve si conocemos el camino que los une. |
| `scenario.first-caliphs.03-the-edge-of-the-river.optional-2` / optional sector observed/cache claimed; once, independent of main phase | salim-caravan-scribe → return-to-game | The caravan’s lookout — 2: One cache: 300 food, 150 wood and 75 gold. It can be claimed once. A ledger of wells is useful only if the road between them is known. | El vigía de la caravana — 2: Un depósito: 300 de alimento, 150 de madera y 75 de oro. Solo se puede reclamar una vez. Un registro de pozos solo sirve si conocemos el camino que los une. |
| `scenario.first-caliphs.03-the-edge-of-the-river.optional-3` / optional sector observed/cache claimed; once, independent of main phase | salim-caravan-scribe → return-to-game | The caravan’s lookout — 3: The relief route is now marked. A ledger of wells is useful only if the road between them is known. | El vigía de la caravana — 3: La ruta alternativa está señalada. Un registro de pozos solo sirve si conocemos el camino que los une. |
| `scenario.first-caliphs.03-the-edge-of-the-river.optional-4` / optional sector observed/cache claimed; once, independent of main phase | salim-caravan-scribe → return-to-game | The caravan’s lookout — 4: One cache: 300 food, 150 wood and 75 gold. It can be claimed once. A ledger of wells is useful only if the road between them is known. | El vigía de la caravana — 4: Un depósito: 300 de alimento, 150 de madera y 75 de oro. Solo se puede reclamar una vez. Un registro de pozos solo sirve si conocemos el camino que los une. |

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
