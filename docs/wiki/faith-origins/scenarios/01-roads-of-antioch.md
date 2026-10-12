# Letters on the Orontes / Cartas sobre el Orontes

`faith-origins/01-roads-of-antioch` · c. 50 CE · network-escort

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/faith-origins/01-roads-of-antioch.svg)

## Historical frame and outcome

First-century communities exchanged travellers and letters across Roman Syria. The couriers in this scenario are fictional.

Reconstrucción de la circulación de comunidades del siglo I; los viajes individuales del jugador son ficticios. No se representa el origen del judaísmo como una decisión cristiana.

Las redes siguen siendo diversas; la misión no produce una conversión automática.

- [Eusebius, Church History III](https://www.newadvent.org/fathers/250103.htm): III.5: tradición de Pella; testimonio posterior. La narración de la huida a Pella no acredita la ruta ni a todos los habitantes.
- [Acts 11, consulted multilingual text](https://www.newadvent.org/bible/act011.htm): 11.19–30: Antioch community and aid narrative. Religious literary testimony, not proof of our courier names, exact date or route.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

These letters were older than my grandmother. I cannot tell you their couriers’ names; I can tell you why a safe road mattered.

Estas cartas eran anteriores a mi abuela. No puedo decirte quién las llevó; sí por qué importaba un camino seguro.

## Geography and map construction

Antioch and Orontes — 320 × 320 tiles; north-up design controls [36.05, 36.1, 36.25, 36.3].

Valle aluvial cultivado; laderas pedregosas al sur/este.

Orontes desde sur hacia norte y giro hacia costa al oeste.

Silpio al sur de la ciudad; no cordillera en medio de la llanura.

Ciudad y puentes junto al Orontes; salida regional hacia Siria/puerto.

Exclude: Sin basílicas del IV, fortalezas cruzadas ni urbanismo moderno.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Orontes city bank | [36.155, 36.203] | [165.25, 155.23] |
| Silpius slope | [36.167, 36.188] | [179.04, 176.59] |
| North valley road | [36.155, 36.25] | [165.25, 88.29] |

```json
{
  "bbox": [
    36.05,
    36.1,
    36.25,
    36.3
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Orontes city bank",
      "lonLat": [
        36.155,
        36.203
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        165.25,
        155.23
      ]
    },
    {
      "id": "anchor-2",
      "name": "Silpius slope",
      "lonLat": [
        36.167,
        36.188
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        179.04,
        176.59
      ]
    },
    {
      "id": "anchor-3",
      "name": "North valley road",
      "lonLat": [
        36.155,
        36.25
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        165.25,
        88.29
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        165.25,
        88.29
      ],
      "purpose": {
        "en": "Deliver three sealed letters along the Orontes roads.",
        "es-ES": "Entrega tres cartas selladas por las rutas del Orontes."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        165.25,
        155.23
      ],
      "purpose": {
        "en": "Secure food for two meeting houses without attacking their neighbours.",
        "es-ES": "Asegura alimento para dos casas de reunión sin atacar a sus vecinos."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        179.04,
        176.59
      ],
      "purpose": {
        "en": "Bring the returning courier safely to the south gate.",
        "es-ES": "Lleva al correo de regreso sano a la puerta sur."
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
          165.25,
          88.29
        ],
        [
          165.25,
          155.23
        ],
        [
          179.04,
          176.59
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          165.25,
          88.29
        ],
        [
          181.25,
          137.76
        ],
        [
          165.25,
          155.23
        ],
        [
          179.04,
          176.59
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        36.17,
        36.1
      ],
      [
        36.16,
        36.19
      ],
      [
        36.155,
        36.205
      ],
      [
        36.135,
        36.25
      ],
      [
        36.07,
        36.29
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "antioch",
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
  "asset": "docs/design/maps/faith-origins/01-roads-of-antioch.svg",
  "mainRouteLengthStraightTiles": 92.36
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
        "en": "Deliver three sealed letters along the Orontes roads.",
        "es-ES": "Entrega tres cartas selladas por las rutas del Orontes."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-1",
        "oncePerEntity": true,
        "required": "Deliver three sealed letters along the Orontes roads."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-record",
      "threshold": 3,
      "entities": [
        {
          "id": "01-roads-of-antioch-o1-entity-1",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "deliver-record",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "01-roads-of-antioch-o1-entity-2",
          "atHub": "hub-1",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "deliver-record",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "01-roads-of-antioch-o1-entity-3",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -2
          ],
          "role": "deliver-record",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "deliver-record",
        "requiredCount": 3,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Deliver three sealed letters along the Orontes roads.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Secure food for two meeting houses without attacking their neighbours.",
        "es-ES": "Asegura alimento para dos casas de reunión sin atacar a sus vecinos."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-2",
        "oncePerEntity": true,
        "required": "Secure food for two meeting houses without attacking their neighbours."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "supply-house",
      "threshold": 2,
      "entities": [
        {
          "id": "01-roads-of-antioch-o2-entity-1",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "supply-house",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "01-roads-of-antioch-o2-entity-2",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "supply-house",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "supply-house",
        "requiredCount": 2,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "food": 600
        },
        "criticalSecondaryRequirements": "Secure food for two meeting houses without attacking their neighbours.",
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "foodPerHouse": 300
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Bring the returning courier safely to the south gate.",
        "es-ES": "Lleva al correo de regreso sano a la puerta sur."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-3",
        "oncePerEntity": true,
        "required": "Bring the returning courier safely to the south gate."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "arrive-courier",
      "threshold": 1,
      "entities": [
        {
          "id": "01-roads-of-antioch-o3-entity-1",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "arrive-courier",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "arrive-courier",
        "requiredCount": 1,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Bring the returning courier safely to the south gate.",
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
| easy | 875/625/312/250 | 2485/1075/1128/550 | 16 | 5 + 5 + 5 + 7 = 22 | 120 / 354 |
| standard | 700/500/250/200 | 2420/1100/1030/600 | 12 | 7 + 7 + 7 + 9 = 30 | 90 / 354 |
| hard | 595/425/212/170 | 2405/1125/988/630 | 10 | 9 + 9 + 9 + 9 = 36 | 75 / 354 |

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
      "enemyTotalCap": 22,
      "initialEnemy": 5,
      "waves": [
        {
          "id": "wave-1",
          "count": 5,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 0
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 354,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 5,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 0
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 708,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 7,
          "composition": {
            "militia": 4,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1062,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 3,
        "spearman": 1,
        "archer": 1,
        "scoutCavalry": 0
      },
      "enemyNominalResourceCost": {
        "food": 1000,
        "wood": 200,
        "gold": 440,
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
      "enemyTotalCap": 30,
      "initialEnemy": 7,
      "waves": [
        {
          "id": "wave-1",
          "count": 7,
          "composition": {
            "militia": 4,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 354,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 7,
          "composition": {
            "militia": 4,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 708,
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
          "offsetSeconds": 1062,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 4,
        "spearman": 1,
        "archer": 1,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1455,
        "wood": 250,
        "gold": 545,
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
          "offsetSeconds": 354,
          "warningSeconds": 75,
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
          "offsetSeconds": 708,
          "warningSeconds": 75,
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
          "offsetSeconds": 1062,
          "warningSeconds": 75,
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
    "worstDeliveryFood": 600,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Measure nav-path length in tiles / actual convoy speed plus loading/unloading; two round trips must fit between phase waves. If not, adjust announced gap or move receiving point within same documented district; architect approval for footprint drift.",
    "minimumWaveGapSecondsFromProposedGeometry": 354
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Correo reemplazable por un único ayudante que recoge copia en archivo; una casa perdida no elimina la segunda vía.

{
  "plan": "Correo reemplazable por un único ayudante que recoge copia en archivo; una casa perdida no elimina la segunda vía.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.faith-origins.01-roads-of-antioch.title` / always | none → next | Letters on the Orontes | Cartas sobre el Orontes |
| `scenario.faith-origins.01-roads-of-antioch.fact-intro` / intro first | collection-narrator → next | First-century communities exchanged travellers and letters across Roman Syria. The couriers in this scenario are fictional. | Reconstrucción de la circulación de comunidades del siglo I; los viajes individuales del jugador son ficticios. No se representa el origen del judaísmo como una decisión cristiana. |
| `scenario.faith-origins.01-roads-of-antioch.personal-intro` / after fact-intro | miriam-archive → next | These letters were older than my grandmother. I cannot tell you their couriers’ names; I can tell you why a safe road mattered. | Estas cartas eran anteriores a mi abuela. No puedo decirte quién las llevó; sí por qué importaba un camino seguro. |
| `scenario.faith-origins.01-roads-of-antioch.objective-1` / phase-1 active | none → hub-1 | Deliver three sealed letters along the Orontes roads. | Entrega tres cartas selladas por las rutas del Orontes. |
| `scenario.faith-origins.01-roads-of-antioch.objective-2` / phase-2 active | none → hub-2 | Secure food for two meeting houses without attacking their neighbours. | Asegura alimento para dos casas de reunión sin atacar a sus vecinos. |
| `scenario.faith-origins.01-roads-of-antioch.objective-3` / phase-3 active | none → hub-3 | Bring the returning courier safely to the south gate. | Lleva al correo de regreso sano a la puerta sur. |
| `scenario.faith-origins.01-roads-of-antioch.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.faith-origins.01-roads-of-antioch.scouts` / scouts panel | none → next | Regional setting: Antioch and Orontes. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Antioch and Orontes. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.faith-origins.01-roads-of-antioch.history` / history panel | none → next | First-century communities exchanged travellers and letters across Roman Syria. The couriers in this scenario are fictional. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Reconstrucción de la circulación de comunidades del siglo I; los viajes individuales del jugador son ficticios. No se representa el origen del judaísmo como una decisión cristiana. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.faith-origins.01-roads-of-antioch.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.faith-origins.01-roads-of-antioch.event-phase-1-complete` / o1 first becomes true | miriam-archive → next | I have found the first safe address. A letter can travel farther than its writer. | He encontrado la primera dirección segura. Una carta puede viajar más lejos que quien la escribe. |
| `scenario.faith-origins.01-roads-of-antioch.event-phase-2-complete` / o2 first becomes true | miriam-archive → next | The second bundle weighs little. Protecting it has cost us more than ink. | El segundo legajo pesa poco. Protegerlo nos ha costado más que tinta. |
| `scenario.faith-origins.01-roads-of-antioch.event-phase-3-complete` / o3 first becomes true | miriam-archive → next | I will record what arrived, and leave a space for what did not. | Registraré lo que llegó y dejaré un espacio para lo que no. |
| `scenario.faith-origins.01-roads-of-antioch.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | miriam-archive → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.faith-origins.01-roads-of-antioch.victory-fact` / victory latch first | collection-narrator → next | First-century communities exchanged travellers and letters across Roman Syria. The couriers in this scenario are fictional. Your mission task is complete; this outcome does not change the documented events. | Las redes siguen siendo diversas; la misión no produce una conversión automática. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.faith-origins.01-roads-of-antioch.victory-personal` / after victory-fact | miriam-archive → 02-after-the-siege | I will record what arrived, and leave a space for what did not. | Registraré lo que llegó y dejaré un espacio para lo que no. |
| `scenario.faith-origins.01-roads-of-antioch.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.faith-origins.01-roads-of-antioch.recovery` / 6 minutes without objective progress | miriam-archive → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |

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
