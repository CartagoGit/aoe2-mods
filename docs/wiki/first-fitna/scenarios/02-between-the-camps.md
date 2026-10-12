# Between the Camps / Entre los campamentos

`first-fitna/02-between-the-camps` · 656 CE · battlefield-evacuation

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/first-fitna/02-between-the-camps.svg)

## Historical frame and outcome

The Battle of the Camel took place near Basra in 656. The evacuation in this scenario is fictional and does not settle the competing claims.

Batalla del Camello junto a Basora; disputa de autoridad/lealtad no combate de religiones modernas.

Victoria del bando de Ali se contextualiza fuera del rescate; no matar figuras veneradas como objetivo de bonus.

- [Ismail K. Poonawala, Ali: Life](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Secciones califato, Camello, Siffin y muerte. Distinguir la reconstrucción histórica de las interpretaciones comunitarias.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

Neither side called its own dead a mistake. I had no room for either banner on the wagon; the bandages filled it.

Ningún bando llamaba error a sus propios muertos. No tenía espacio para estandartes en el carro: lo llenaban las vendas.

## Geography and map construction

Early Basra and marsh edge — 360 × 360 tiles; north-up design controls [47.35, 30.15, 47.9, 30.75].

Asentamiento temprano al borde árido oeste de zonas irrigadas/pantanosas.

Canales al este; Shatt al-Arab referencia regional, curso antiguo incierto.

Llano con islas secas; no montaña arbitraria.

Ruta hacia campamentos al oeste y embarcaderos al este.

Exclude: Basora temprana no se coloca en pleno casco moderno como certeza arqueológica.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Early Basra Az Zubayr region | [47.7, 30.38] | [214.04, 216.9] |
| Dry western approach | [47.58, 30.39] | [158.78, 211.55] |
| Irrigated eastern margin | [47.81, 30.45] | [264.7, 179.5] |

```json
{
  "bbox": [
    47.35,
    30.15,
    47.9,
    30.75
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Early Basra Az Zubayr region",
      "lonLat": [
        47.7,
        30.38
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        214.04,
        216.9
      ]
    },
    {
      "id": "anchor-2",
      "name": "Dry western approach",
      "lonLat": [
        47.58,
        30.39
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        158.78,
        211.55
      ]
    },
    {
      "id": "anchor-3",
      "name": "Irrigated eastern margin",
      "lonLat": [
        47.81,
        30.45
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        264.7,
        179.5
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        264.7,
        179.5
      ],
      "purpose": {
        "en": "Open the dry corridor west of the irrigated quarter.",
        "es-ES": "Abre el corredor seco al oeste del barrio irrigado."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        214.04,
        216.9
      ],
      "purpose": {
        "en": "Recover six of eight civilian parties and two aid wagons.",
        "es-ES": "Recupera seis de ocho grupos civiles y dos carros de auxilio."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        158.78,
        211.55
      ],
      "purpose": {
        "en": "Withdraw before the two military camps converge on the corridor.",
        "es-ES": "Retírate antes de que los dos campamentos militares converjan sobre el corredor."
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
          264.7,
          179.5
        ],
        [
          214.04,
          216.9
        ],
        [
          158.78,
          211.55
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          264.7,
          179.5
        ],
        [
          223.37,
          182.2
        ],
        [
          214.04,
          216.9
        ],
        [
          158.78,
          211.55
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
  "terrainProfile": "basra",
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
  "asset": "docs/design/maps/first-fitna/02-between-the-camps.svg",
  "mainRouteLengthStraightTiles": 118.49
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
        "en": "Open the dry corridor west of the irrigated quarter.",
        "es-ES": "Abre el corredor seco al oeste del barrio irrigado."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-1",
        "oncePerEntity": true,
        "required": "Open the dry corridor west of the irrigated quarter."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "secure-corridor",
      "threshold": 1,
      "entities": [
        {
          "id": "02-between-the-camps-o1-entity-1",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "secure-corridor",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "secure-corridor",
        "requiredCount": 1,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Open the dry corridor west of the irrigated quarter.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Recover six of eight civilian parties and two aid wagons.",
        "es-ES": "Recupera seis de ocho grupos civiles y dos carros de auxilio."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-2",
        "oncePerEntity": true,
        "required": "Recover six of eight civilian parties and two aid wagons."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "evacuate-family",
      "threshold": 6,
      "entities": [
        {
          "id": "02-between-the-camps-o2-entity-1",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "02-between-the-camps-o2-entity-2",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "02-between-the-camps-o2-entity-3",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "02-between-the-camps-o2-entity-4",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "02-between-the-camps-o2-entity-5",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "02-between-the-camps-o2-entity-6",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "02-between-the-camps-o2-entity-7",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "02-between-the-camps-o2-entity-8",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "evacuate-family",
        "requiredCount": 6,
        "destination": "hub-2",
        "defeatBelowRemaining": 6,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Recover six of eight civilian parties and two aid wagons.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Withdraw before the two military camps converge on the corridor.",
        "es-ES": "Retírate antes de que los dos campamentos militares converjan sobre el corredor."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-3",
        "oncePerEntity": true,
        "required": "Withdraw before the two military camps converge on the corridor."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "withdraw-escort",
      "threshold": 1,
      "entities": [
        {
          "id": "02-between-the-camps-o3-entity-1",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "withdraw-escort",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "withdraw-escort",
        "requiredCount": 1,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Withdraw before the two military camps converge on the corridor.",
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
| easy | 875/625/312/250 | 1885/1075/1128/550 | 16 | 20 + 20 + 20 + 21 = 81 | 120 / 429 |
| standard | 700/500/250/200 | 1820/1100/1030/600 | 12 | 27 + 27 + 27 + 27 = 108 | 90 / 429 |
| hard | 595/425/212/170 | 1805/1125/988/630 | 10 | 32 + 32 + 32 + 34 = 130 | 75 / 429 |

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
      "enemyTotalCap": 81,
      "initialEnemy": 20,
      "waves": [
        {
          "id": "wave-1",
          "count": 20,
          "composition": {
            "militia": 7,
            "spearman": 5,
            "archer": 5,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 429,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 20,
          "composition": {
            "militia": 7,
            "spearman": 5,
            "archer": 5,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 858,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 21,
          "composition": {
            "militia": 8,
            "spearman": 5,
            "archer": 5,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1287,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 7,
        "spearman": 5,
        "archer": 5,
        "scoutCavalry": 3
      },
      "enemyNominalResourceCost": {
        "food": 3400,
        "wood": 1000,
        "gold": 1480,
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
      "enemyTotalCap": 108,
      "initialEnemy": 27,
      "waves": [
        {
          "id": "wave-1",
          "count": 27,
          "composition": {
            "militia": 11,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 429,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 27,
          "composition": {
            "militia": 11,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 858,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 27,
          "composition": {
            "militia": 11,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1287,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 11,
        "spearman": 6,
        "archer": 6,
        "scoutCavalry": 4
      },
      "enemyNominalResourceCost": {
        "food": 4760,
        "wood": 1200,
        "gold": 1960,
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
      "enemyTotalCap": 130,
      "initialEnemy": 32,
      "waves": [
        {
          "id": "wave-1",
          "count": 32,
          "composition": {
            "militia": 11,
            "spearman": 8,
            "archer": 8,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 429,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 32,
          "composition": {
            "militia": 11,
            "spearman": 8,
            "archer": 8,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 858,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 34,
          "composition": {
            "militia": 13,
            "spearman": 8,
            "archer": 8,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1287,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 11,
        "spearman": 8,
        "archer": 8,
        "scoutCavalry": 5
      },
      "enemyNominalResourceCost": {
        "food": 5480,
        "wood": 1600,
        "gold": 2360,
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
    "minimumWaveGapSecondsFromProposedGeometry": 429
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Ruta seca oeste y ruta de diques al este. Civiles rescatados no vuelven a contarse; retirar a tiempo permite completar tras pérdida de un carro.

{
  "plan": "Ruta seca oeste y ruta de diques al este. Civiles rescatados no vuelven a contarse; retirar a tiempo permite completar tras pérdida de un carro.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.first-fitna.02-between-the-camps.title` / always | none → next | Between the Camps | Entre los campamentos |
| `scenario.first-fitna.02-between-the-camps.fact-intro` / intro first | collection-narrator → next | The Battle of the Camel took place near Basra in 656. The evacuation in this scenario is fictional and does not settle the competing claims. | Batalla del Camello junto a Basora; disputa de autoridad/lealtad no combate de religiones modernas. |
| `scenario.first-fitna.02-between-the-camps.personal-intro` / after fact-intro | farid-field-medic → next | Neither side called its own dead a mistake. I had no room for either banner on the wagon; the bandages filled it. | Ningún bando llamaba error a sus propios muertos. No tenía espacio para estandartes en el carro: lo llenaban las vendas. |
| `scenario.first-fitna.02-between-the-camps.objective-1` / phase-1 active | none → hub-1 | Open the dry corridor west of the irrigated quarter. | Abre el corredor seco al oeste del barrio irrigado. |
| `scenario.first-fitna.02-between-the-camps.objective-2` / phase-2 active | none → hub-2 | Recover six of eight civilian parties and two aid wagons. | Recupera seis de ocho grupos civiles y dos carros de auxilio. |
| `scenario.first-fitna.02-between-the-camps.objective-3` / phase-3 active | none → hub-3 | Withdraw before the two military camps converge on the corridor. | Retírate antes de que los dos campamentos militares converjan sobre el corredor. |
| `scenario.first-fitna.02-between-the-camps.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.first-fitna.02-between-the-camps.scouts` / scouts panel | none → next | Regional setting: Early Basra and marsh edge. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Early Basra and marsh edge. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.first-fitna.02-between-the-camps.history` / history panel | none → next | The Battle of the Camel took place near Basra in 656. The evacuation in this scenario is fictional and does not settle the competing claims. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Batalla del Camello junto a Basora; disputa de autoridad/lealtad no combate de religiones modernas. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.first-fitna.02-between-the-camps.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.first-fitna.02-between-the-camps.event-phase-1-complete` / o1 first becomes true | farid-field-medic → next | The first party is safe. Ask whose hands need tending before asking whose banner they followed. | El primer grupo está a salvo. Pregunta qué manos necesitan ayuda antes de preguntar qué estandarte siguieron. |
| `scenario.first-fitna.02-between-the-camps.event-phase-2-complete` / o2 first becomes true | farid-field-medic → next | The message is sealed. Do not let a wounded man become its price. | El mensaje está sellado. No dejes que un herido sea su precio. |
| `scenario.first-fitna.02-between-the-camps.event-phase-3-complete` / o3 first becomes true | farid-field-medic → next | I will keep both names in the record. Care does not settle the quarrel. | Guardaré ambos nombres en el registro. Cuidar no resuelve la disputa. |
| `scenario.first-fitna.02-between-the-camps.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | farid-field-medic → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.first-fitna.02-between-the-camps.victory-fact` / victory latch first | collection-narrator → next | The Battle of the Camel took place near Basra in 656. The evacuation in this scenario is fictional and does not settle the competing claims. Your mission task is complete; this outcome does not change the documented events. | Victoria del bando de Ali se contextualiza fuera del rescate; no matar figuras veneradas como objetivo de bonus. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.first-fitna.02-between-the-camps.victory-personal` / after victory-fact | farid-field-medic → 03-water-and-words | I will keep both names in the record. Care does not settle the quarrel. | Guardaré ambos nombres en el registro. Cuidar no resuelve la disputa. |
| `scenario.first-fitna.02-between-the-camps.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.first-fitna.02-between-the-camps.recovery` / 6 minutes without objective progress | farid-field-medic → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |

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
