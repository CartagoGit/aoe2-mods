# Pieces of a Memory / Piezas de una memoria

`new-rome/05-pieces-of-a-memory` · 787 CE; interludes 815 and 843 · artifact-and-record-escort

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/new-rome/05-pieces-of-a-memory.svg)

## Historical frame and outcome

The council at Nicaea in 787 restored the veneration of images. Renewed iconoclasm in 815 and its ending in 843 belong to separate dated epilogues.

Nicea II condena la iconoclasia en 787; esta vuelve en 815 y es condenada en 843. No existe final lineal ininterrumpido desde 787.

787 misión; Anna anciana relata 843. Recomendaciones a C03 e I02 son perspectivas paralelas; 1054 requiere nueva campaña.

- [The Met, Iconoclasm](https://www.metmuseum.org/exhibitions/listings/2012/byzantium-and-islam/blog/topical-essays/posts/iconoclasm): Hieria 754, Nicea 787, reanudación 815, condena 843. Política y experiencia local no uniformes; no homogeneizar comunidades.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

I was old enough to work in 787, and old enough to doubt my first certainty when the policy changed again. A restored image does not restore a lost life.

Ya podía trabajar en 787, y pude dudar de mi primera certeza cuando cambió de nuevo la política. Restaurar una imagen no devuelve una vida perdida.

## Geography and map construction

Nicaea and Ascanian Lake — 320 × 320 tiles; north-up design controls [29.6, 40.34, 29.88, 40.53].

Llanura oriental del lago con cultivos; colinas periféricas.

Lago Ascanio/Iznik al oeste de la ciudad; salida por costa occidental.

Montañas norte/sur fuera del centro; pendientes transitables.

Ciudad junto a orilla este; camino de Nicomedia desde noroeste y ramal sur.

Exclude: No representar el concilio en Constantinopla ni inventar catedral gótica.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Nicaea civic core | [29.72, 40.429] | [139.16, 167.52] |
| Lake east shore | [29.71, 40.43] | [128.98, 166.18] |
| North gate approach | [29.72, 40.46] | [139.16, 126.09] |

```json
{
  "bbox": [
    29.6,
    40.34,
    29.88,
    40.53
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Nicaea civic core",
      "lonLat": [
        29.72,
        40.429
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        139.16,
        167.52
      ]
    },
    {
      "id": "anchor-2",
      "name": "Lake east shore",
      "lonLat": [
        29.71,
        40.43
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        128.98,
        166.18
      ]
    },
    {
      "id": "anchor-3",
      "name": "North gate approach",
      "lonLat": [
        29.72,
        40.46
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        139.16,
        126.09
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        139.16,
        126.09
      ],
      "purpose": {
        "en": "Gather the three workshop records without destroying opposing archives.",
        "es-ES": "Reúne los tres registros de taller sin destruir archivos contrarios."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        139.16,
        167.52
      ],
      "purpose": {
        "en": "Escort the record keepers through the north road and lakeside path.",
        "es-ES": "Escolta a los custodios por el camino norte y la senda del lago."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        128.98,
        166.18
      ],
      "purpose": {
        "en": "Deposit two copies and preserve one inventory for the future.",
        "es-ES": "Deposita dos copias y conserva un inventario para el futuro."
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
          139.16,
          126.09
        ],
        [
          139.16,
          167.52
        ],
        [
          128.98,
          166.18
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          139.16,
          126.09
        ],
        [
          155.16,
          162.805
        ],
        [
          139.16,
          167.52
        ],
        [
          128.98,
          166.18
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        29.6,
        40.43
      ],
      [
        29.65,
        40.445
      ],
      [
        29.7,
        40.44
      ],
      [
        29.712,
        40.425
      ],
      [
        29.695,
        40.4
      ],
      [
        29.63,
        40.39
      ],
      [
        29.6,
        40.41
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "lake-outline"
  },
  "terrainProfile": "nicaea",
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
  "asset": "docs/design/maps/new-rome/05-pieces-of-a-memory.svg",
  "mainRouteLengthStraightTiles": 51.7
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
        "en": "Gather the three workshop records without destroying opposing archives.",
        "es-ES": "Reúne los tres registros de taller sin destruir archivos contrarios."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-1",
        "oncePerEntity": true,
        "required": "Gather the three workshop records without destroying opposing archives."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "collect-record",
      "threshold": 3,
      "entities": [
        {
          "id": "05-pieces-of-a-memory-o1-entity-1",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "collect-record",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-pieces-of-a-memory-o1-entity-2",
          "atHub": "hub-1",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "collect-record",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-pieces-of-a-memory-o1-entity-3",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -2
          ],
          "role": "collect-record",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "collect-record",
        "requiredCount": 3,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Gather the three workshop records without destroying opposing archives.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Escort the record keepers through the north road and lakeside path.",
        "es-ES": "Escolta a los custodios por el camino norte y la senda del lago."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-2",
        "oncePerEntity": true,
        "required": "Escort the record keepers through the north road and lakeside path."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "escort-custodian",
      "threshold": 2,
      "entities": [
        {
          "id": "05-pieces-of-a-memory-o2-entity-1",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "escort-custodian",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-pieces-of-a-memory-o2-entity-2",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "escort-custodian",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "escort-custodian",
        "requiredCount": 2,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Escort the record keepers through the north road and lakeside path.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Deposit two copies and preserve one inventory for the future.",
        "es-ES": "Deposita dos copias y conserva un inventario para el futuro."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-3",
        "oncePerEntity": true,
        "required": "Deposit two copies and preserve one inventory for the future."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-copy",
      "threshold": 2,
      "entities": [
        {
          "id": "05-pieces-of-a-memory-o3-entity-1",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "deliver-copy",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-pieces-of-a-memory-o3-entity-2",
          "atHub": "hub-3",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "deliver-copy",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "deliver-copy",
        "requiredCount": 2,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Deposit two copies and preserve one inventory for the future.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    }
  ],
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
| easy | 875/625/312/250 | 1885/1075/1128/550 | 16 | 8 + 8 + 8 + 8 = 32 | 120 / 240 |
| standard | 700/500/250/200 | 1820/1100/1030/600 | 12 | 10 + 10 + 10 + 12 = 42 | 90 / 238 |
| hard | 595/425/212/170 | 1805/1125/988/630 | 10 | 12 + 12 + 12 + 14 = 50 | 75 / 238 |

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
        "food": 1885,
        "wood": 1075,
        "gold": 1128,
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
      "maxVillagers": 18,
      "startingEscortCount": 16,
      "playerPopulationCap": 90,
      "enemyTotalCap": 32,
      "initialEnemy": 8,
      "waves": [
        {
          "id": "wave-1",
          "count": 8,
          "composition": {
            "militia": 3,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 240,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 8,
          "composition": {
            "militia": 3,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 480,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 8,
          "composition": {
            "militia": 3,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 720,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 3,
        "spearman": 2,
        "archer": 2,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1320,
        "wood": 400,
        "gold": 600,
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
        45
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
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
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
        "food": 1820,
        "wood": 1100,
        "gold": 1030,
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
      "maxVillagers": 18,
      "startingEscortCount": 12,
      "playerPopulationCap": 90,
      "enemyTotalCap": 42,
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
          "offsetSeconds": 238,
          "warningSeconds": 90,
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
          "offsetSeconds": 476,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 12,
          "composition": {
            "militia": 4,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 714,
          "warningSeconds": 90,
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
        "food": 1855,
        "wood": 450,
        "gold": 785,
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
        45
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
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
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
        "food": 1805,
        "wood": 1125,
        "gold": 988,
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
      "maxVillagers": 18,
      "startingEscortCount": 10,
      "playerPopulationCap": 90,
      "enemyTotalCap": 50,
      "initialEnemy": 12,
      "waves": [
        {
          "id": "wave-1",
          "count": 12,
          "composition": {
            "militia": 4,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 238,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 12,
          "composition": {
            "militia": 4,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 476,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 14,
          "composition": {
            "militia": 6,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 714,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 4,
        "spearman": 3,
        "archer": 3,
        "scoutCavalry": 2
      },
      "enemyNominalResourceCost": {
        "food": 2140,
        "wood": 600,
        "gold": 900,
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
        45
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
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
    }
  },
  "analysis": {
    "classification": "feasibility envelope, not a combat simulation or proof of balance",
    "startingWorkers": 12,
    "plannedPeakWorkers": 18,
    "effectiveGatherRatePerWorkerResourcePerSecondAssumption": 0.24,
    "walkingAndIdleIncluded": "Assumed rate discounts native gathering for travel/idle; measure actual efficiency in game.",
    "worstDeliveryFood": 0,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Measure nav-path length in tiles / actual convoy speed plus loading/unloading; two round trips must fit between phase waves. If not, adjust announced gap or move receiving point within same documented district; architect approval for footprint drift.",
    "minimumWaveGapSecondsFromProposedGeometry": 238
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Dos custodios de reemplazo con documentos duplicados; ninguna eliminación doctrinal de rivales. No cambiar mapa de Nicea a Constantinopla por un timer.

{
  "plan": "Dos custodios de reemplazo con documentos duplicados; ninguna eliminación doctrinal de rivales. No cambiar mapa de Nicea a Constantinopla por un timer.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.new-rome.05-pieces-of-a-memory.title` / always | none → next | Pieces of a Memory | Piezas de una memoria |
| `scenario.new-rome.05-pieces-of-a-memory.fact-intro` / intro first | collection-narrator → next | The council at Nicaea in 787 restored the veneration of images. Renewed iconoclasm in 815 and its ending in 843 belong to separate dated epilogues. | Nicea II condena la iconoclasia en 787; esta vuelve en 815 y es condenada en 843. No existe final lineal ininterrumpido desde 787. |
| `scenario.new-rome.05-pieces-of-a-memory.personal-intro` / after fact-intro | anna-mosaicist → next | I was old enough to work in 787, and old enough to doubt my first certainty when the policy changed again. A restored image does not restore a lost life. | Ya podía trabajar en 787, y pude dudar de mi primera certeza cuando cambió de nuevo la política. Restaurar una imagen no devuelve una vida perdida. |
| `scenario.new-rome.05-pieces-of-a-memory.objective-1` / phase-1 active | none → hub-1 | Gather the three workshop records without destroying opposing archives. | Reúne los tres registros de taller sin destruir archivos contrarios. |
| `scenario.new-rome.05-pieces-of-a-memory.objective-2` / phase-2 active | none → hub-2 | Escort the record keepers through the north road and lakeside path. | Escolta a los custodios por el camino norte y la senda del lago. |
| `scenario.new-rome.05-pieces-of-a-memory.objective-3` / phase-3 active | none → hub-3 | Deposit two copies and preserve one inventory for the future. | Deposita dos copias y conserva un inventario para el futuro. |
| `scenario.new-rome.05-pieces-of-a-memory.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.new-rome.05-pieces-of-a-memory.scouts` / scouts panel | none → next | Regional setting: Nicaea and Ascanian Lake. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Nicaea and Ascanian Lake. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.new-rome.05-pieces-of-a-memory.history` / history panel | none → next | The council at Nicaea in 787 restored the veneration of images. Renewed iconoclasm in 815 and its ending in 843 belong to separate dated epilogues. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Nicea II condena la iconoclasia en 787; esta vuelve en 815 y es condenada en 843. No existe final lineal ininterrumpido desde 787. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.new-rome.05-pieces-of-a-memory.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.new-rome.05-pieces-of-a-memory.event-phase-1-complete` / o1 first becomes true | anna-mosaicist → next | The first piece is in place. A city is harder to mend than a mosaic. | La primera pieza está en su sitio. Una ciudad es más difícil de reparar que un mosaico. |
| `scenario.new-rome.05-pieces-of-a-memory.event-phase-2-complete` / o2 first becomes true | anna-mosaicist → next | I used to notice only the broken images. Now I notice who carries them. | Antes solo veía las imágenes rotas. Ahora veo quién las lleva. |
| `scenario.new-rome.05-pieces-of-a-memory.event-phase-3-complete` / o3 first becomes true | anna-mosaicist → next | Keep the inventory beside the pieces. Memory should not become another excuse to destroy. | Guarda el inventario junto a las piezas. La memoria no debe ser otra excusa para destruir. |
| `scenario.new-rome.05-pieces-of-a-memory.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | anna-mosaicist → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.new-rome.05-pieces-of-a-memory.victory-fact` / victory latch first | collection-narrator → next | The council at Nicaea in 787 restored the veneration of images. Renewed iconoclasm in 815 and its ending in 843 belong to separate dated epilogues. Your mission task is complete; this outcome does not change the documented events. | 787 misión; Anna anciana relata 843. Recomendaciones a C03 e I02 son perspectivas paralelas; 1054 requiere nueva campaña. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.new-rome.05-pieces-of-a-memory.victory-personal` / after victory-fact | anna-mosaicist → campaign ending | Keep the inventory beside the pieces. Memory should not become another excuse to destroy. | Guarda el inventario junto a las piezas. La memoria no debe ser otra excusa para destruir. |
| `scenario.new-rome.05-pieces-of-a-memory.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.new-rome.05-pieces-of-a-memory.recovery` / 6 minutes without objective progress | anna-mosaicist → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |

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
