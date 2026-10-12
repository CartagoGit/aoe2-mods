# Where Two Seas Meet / Donde se encuentran dos mares

`imperial-church/03-new-capital` · 330 CE; epilogue to 337 · urban-logistics

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/imperial-church/03-new-capital.svg)

## Historical frame and outcome

Constantinople was inaugurated in 330. Constantine died in 337; imperial and church institutions continued to change.

Constantinopla inaugura una nueva etapa en 330. El diseño de construcción comprime abastecimiento y trabajo; los barrios exactos son reconstrucción.

330 concluye obra jugable; 337 se relata fuera del mapa. Final ofrece C03 o C04 según perspectiva.

- [The Met, Byzantium (ca. 330–1453)](https://www.metmuseum.org/essays/byzantium-ca-330-1453): Períodos y cultura material. Ensayo de museo de síntesis, no plano arqueológico ni cronología militar completa.
- [UNESCO, Historic Areas of Istanbul](https://whc.unesco.org/en/list/356/): Península, murallas y monumentos. Paisaje de varias épocas: filtrar fecha de cada edificio.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

I had thought Rome was the centre of every road. Here I found two seas, another ledger, and the limits of that certainty.

Había creído que Roma era el centro de todos los caminos. Aquí encontré dos mares, otro registro y los límites de aquella certeza.

## Geography and map construction

Byzantion / Constantinople peninsula — 360 × 360 tiles; north-up design controls [28.88, 40.96, 29.04, 41.07].

Península urbana y huertas de Tracia al oeste.

Cuerno de Oro al norte; Bósforo al este; Propóntide al sur.

Lomas de península, sin montañas interiores.

Accesos terrestres desde oeste; puertos al sur/norte.

Exclude: Antes 413 no muralla teodosiana; antes 537 no Hagia Sophia actual; sin minaretes ni puente moderno del Bósforo.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Historic peninsula core | [28.978, 41.009] | [215.56, 195.43] |
| Land wall corridor | [28.925, 41.025] | [109.38, 152.95] |
| Golden Horn quay | [28.965, 41.024] | [189.52, 155.6] |

```json
{
  "bbox": [
    28.88,
    40.96,
    29.04,
    41.07
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Historic peninsula core",
      "lonLat": [
        28.978,
        41.009
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        215.56,
        195.43
      ]
    },
    {
      "id": "anchor-2",
      "name": "Land wall corridor",
      "lonLat": [
        28.925,
        41.025
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        109.38,
        152.95
      ]
    },
    {
      "id": "anchor-3",
      "name": "Golden Horn quay",
      "lonLat": [
        28.965,
        41.024
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        189.52,
        155.6
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        189.52,
        155.6
      ],
      "purpose": {
        "en": "Restore the western road and two harbour depots.",
        "es-ES": "Restablece el camino occidental y dos depósitos portuarios."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        215.56,
        195.43
      ],
      "purpose": {
        "en": "Deliver 1800 food, 1200 wood and 600 stone to the civic works.",
        "es-ES": "Entrega 1800 de alimento, 1200 de madera y 600 de piedra a las obras civiles."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        109.38,
        152.95
      ],
      "purpose": {
        "en": "Complete the civic record and select the western or eastern archive.",
        "es-ES": "Completa el registro civil y selecciona el archivo occidental u oriental."
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
          189.52,
          155.6
        ],
        [
          215.56,
          195.43
        ],
        [
          109.38,
          152.95
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          189.52,
          155.6
        ],
        [
          218.54000000000002,
          191.515
        ],
        [
          215.56,
          195.43
        ],
        [
          109.38,
          152.95
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "constantinople",
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
  "asset": "docs/design/maps/imperial-church/03-new-capital.svg",
  "mainRouteLengthStraightTiles": 161.95
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
        "en": "Restore the western road and two harbour depots.",
        "es-ES": "Restablece el camino occidental y dos depósitos portuarios."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-1",
        "oncePerEntity": true,
        "required": "Restore the western road and two harbour depots."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "restore-depot",
      "threshold": 2,
      "entities": [
        {
          "id": "03-new-capital-o1-entity-1",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "restore-depot",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "03-new-capital-o1-entity-2",
          "atHub": "hub-1",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "restore-depot",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "restore-depot",
        "requiredCount": 2,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Restore the western road and two harbour depots.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Deliver 1800 food, 1200 wood and 600 stone to the civic works.",
        "es-ES": "Entrega 1800 de alimento, 1200 de madera y 600 de piedra a las obras civiles."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-2",
        "oncePerEntity": true,
        "required": "Deliver 1800 food, 1200 wood and 600 stone to the civic works."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "resource-delivery",
      "threshold": 3600,
      "entities": [
        {
          "id": "03-new-capital-o2-entity-1",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "resource-delivery",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "03-new-capital-o2-entity-2",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "resource-delivery",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "03-new-capital-o2-entity-3",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -2
          ],
          "role": "resource-delivery",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "resource-delivery",
        "requiredCount": 3600,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "food": 1800,
          "wood": 1200,
          "gold": 0,
          "stone": 600
        },
        "criticalSecondaryRequirements": "Deliver 1800 food, 1200 wood and 600 stone to the civic works.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Complete the civic record and select the western or eastern archive.",
        "es-ES": "Completa el registro civil y selecciona el archivo occidental u oriental."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-3",
        "oncePerEntity": true,
        "required": "Complete the civic record and select the western or eastern archive."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "perspective-choice",
      "threshold": 1,
      "entities": [
        {
          "id": "03-new-capital-o3-entity-1",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "perspective-choice",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "perspective-choice",
        "requiredCount": 1,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Complete the civic record and select the western or eastern archive.",
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "routes": [
          {
            "id": "western-perspective",
            "progressKey": "progress.imperial-church.western-perspective",
            "value": 1,
            "resetOtherKeys": false
          },
          {
            "id": "eastern-perspective",
            "progressKey": "progress.imperial-church.eastern-perspective",
            "value": 1,
            "resetOtherKeys": false
          }
        ]
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
| easy | 875/625/312/250 | 3685/2275/1128/1150 | 16 | 11 + 11 + 11 + 12 = 45 | 120 / 553 |
| standard | 700/500/250/200 | 3620/2300/1030/1200 | 12 | 15 + 15 + 15 + 15 = 60 | 90 / 553 |
| hard | 595/425/212/170 | 3605/2325/988/1230 | 10 | 18 + 18 + 18 + 18 = 72 | 75 / 553 |

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
        "food": 3685,
        "wood": 2275,
        "gold": 1128,
        "stone": 1150
      },
      "mandatoryDeliveries": {
        "food": 1800,
        "wood": 1200,
        "gold": 0,
        "stone": 600
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
      "enemyTotalCap": 45,
      "initialEnemy": 11,
      "waves": [
        {
          "id": "wave-1",
          "count": 11,
          "composition": {
            "militia": 6,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 553,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 11,
          "composition": {
            "militia": 6,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1106,
          "warningSeconds": 120,
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
          "offsetSeconds": 1659,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 6,
        "spearman": 2,
        "archer": 2,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 2035,
        "wood": 450,
        "gold": 845,
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
        "food": 3620,
        "wood": 2300,
        "gold": 1030,
        "stone": 1200
      },
      "mandatoryDeliveries": {
        "food": 1800,
        "wood": 1200,
        "gold": 0,
        "stone": 600
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
      "enemyTotalCap": 60,
      "initialEnemy": 15,
      "waves": [
        {
          "id": "wave-1",
          "count": 15,
          "composition": {
            "militia": 7,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 553,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 15,
          "composition": {
            "militia": 7,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1106,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 15,
          "composition": {
            "militia": 7,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1659,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 7,
        "spearman": 3,
        "archer": 3,
        "scoutCavalry": 2
      },
      "enemyNominalResourceCost": {
        "food": 2740,
        "wood": 600,
        "gold": 1100,
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
        "food": 3605,
        "wood": 2325,
        "gold": 988,
        "stone": 1230
      },
      "mandatoryDeliveries": {
        "food": 1800,
        "wood": 1200,
        "gold": 0,
        "stone": 600
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
      "enemyTotalCap": 72,
      "initialEnemy": 18,
      "waves": [
        {
          "id": "wave-1",
          "count": 18,
          "composition": {
            "militia": 7,
            "spearman": 4,
            "archer": 4,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 553,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 18,
          "composition": {
            "militia": 7,
            "spearman": 4,
            "archer": 4,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1106,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 18,
          "composition": {
            "militia": 7,
            "spearman": 4,
            "archer": 4,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1659,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 7,
        "spearman": 4,
        "archer": 4,
        "scoutCavalry": 3
      },
      "enemyNominalResourceCost": {
        "food": 3200,
        "wood": 800,
        "gold": 1280,
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
    "worstDeliveryFood": 1800,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Measure nav-path length in tiles / actual convoy speed plus loading/unloading; two round trips must fit between phase waves. If not, adjust announced gap or move receiving point within same documented district; architect approval for footprint drift.",
    "minimumWaveGapSecondsFromProposedGeometry": 553
  }
}
```

## Choice, failure and recovery

Enviar copias a Roma (western) o Nueva Roma (eastern); no borrar la otra clave. Ningún edificio de 413/537 aparece en 330.

Entrega en lotes con recibos únicos; recursos reservados para recuperar depósito; no exigir saldo final después de consumir el tributo.

{
  "plan": "Entrega en lotes con recibos únicos; recursos reservados para recuperar depósito; no exigir saldo final después de consumir el tributo.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.imperial-church.03-new-capital.title` / always | none → next | Where Two Seas Meet | Donde se encuentran dos mares |
| `scenario.imperial-church.03-new-capital.fact-intro` / intro first | collection-narrator → next | Constantinople was inaugurated in 330. Constantine died in 337; imperial and church institutions continued to change. | Constantinopla inaugura una nueva etapa en 330. El diseño de construcción comprime abastecimiento y trabajo; los barrios exactos son reconstrucción. |
| `scenario.imperial-church.03-new-capital.personal-intro` / after fact-intro | imperial-clerk → next | I had thought Rome was the centre of every road. Here I found two seas, another ledger, and the limits of that certainty. | Había creído que Roma era el centro de todos los caminos. Aquí encontré dos mares, otro registro y los límites de aquella certeza. |
| `scenario.imperial-church.03-new-capital.objective-1` / phase-1 active | none → hub-1 | Restore the western road and two harbour depots. | Restablece el camino occidental y dos depósitos portuarios. |
| `scenario.imperial-church.03-new-capital.objective-2` / phase-2 active | none → hub-2 | Deliver 1800 food, 1200 wood and 600 stone to the civic works. | Entrega 1800 de alimento, 1200 de madera y 600 de piedra a las obras civiles. |
| `scenario.imperial-church.03-new-capital.objective-3` / phase-3 active | none → hub-3 | Complete the civic record and select the western or eastern archive. | Completa el registro civil y selecciona el archivo occidental u oriental. |
| `scenario.imperial-church.03-new-capital.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.imperial-church.03-new-capital.scouts` / scouts panel | none → next | Regional setting: Byzantion / Constantinople peninsula. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Byzantion / Constantinople peninsula. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.imperial-church.03-new-capital.history` / history panel | none → next | Constantinople was inaugurated in 330. Constantine died in 337; imperial and church institutions continued to change. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Constantinopla inaugura una nueva etapa en 330. El diseño de construcción comprime abastecimiento y trabajo; los barrios exactos son reconstrucción. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.imperial-church.03-new-capital.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.imperial-church.03-new-capital.event-phase-1-complete` / o1 first becomes true | imperial-clerk → next | The first account is settled. Keep the road open; promises do not haul supplies. | La primera cuenta está saldada. Mantén el camino abierto: las promesas no transportan provisiones. |
| `scenario.imperial-church.03-new-capital.event-phase-2-complete` / o2 first becomes true | imperial-clerk → next | We have what we came for. Now comes the part the clerks forget: getting it home. | Tenemos lo que vinimos a buscar. Ahora viene lo que olvidan los escribanos: llevarlo a casa. |
| `scenario.imperial-church.03-new-capital.event-phase-3-complete` / o3 first becomes true | imperial-clerk → next | I can sign this ledger. I cannot sign for every story told about it. | Puedo firmar este registro. No todas las historias que se cuentan sobre él. |
| `scenario.imperial-church.03-new-capital.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | imperial-clerk → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.imperial-church.03-new-capital.victory-fact` / victory latch first | collection-narrator → next | Constantinople was inaugurated in 330. Constantine died in 337; imperial and church institutions continued to change. Your mission task is complete; this outcome does not change the documented events. | 330 concluye obra jugable; 337 se relata fuera del mapa. Final ofrece C03 o C04 según perspectiva. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.imperial-church.03-new-capital.victory-personal` / after victory-fact | imperial-clerk → campaign ending | I can sign this ledger. I cannot sign for every story told about it. | Puedo firmar este registro. No todas las historias que se cuentan sobre él. |
| `scenario.imperial-church.03-new-capital.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.imperial-church.03-new-capital.recovery` / 6 minutes without objective progress | imperial-clerk → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |

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
