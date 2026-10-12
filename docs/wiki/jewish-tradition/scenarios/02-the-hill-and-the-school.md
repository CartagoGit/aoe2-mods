# The Hill and the School / La colina y la escuela

`jewish-tradition/02-the-hill-and-the-school` · c. 200 CE · archive-economy

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/jewish-tradition/02-the-hill-and-the-school.svg)

## Historical frame and outcome

Around the beginning of the third century, Judah the Prince was associated with the redaction of the Mishnah. Its transmission was a collective process.

Tradición de compilación de la Mishná y contexto de Judá el Príncipe; localización/fecha exacta de cada acto de escritura no se afirma.

Los contadores representan logística, no una puntuación de ortodoxia religiosa.

- [UNESCO, Necropolis of Bet Shearim](https://whc.unesco.org/en/list/1471/): Contexto de renovación judía y Judá el Príncipe. Necrópolis y transmisión cultural, no prueba de una aventura del protagonista.
- [Jewish Encyclopedia, Judah I](https://jewishencyclopedia.com/articles/8963-judah-i): Redaction and limits of attribution. Older scholarship; redactor rather than sole author. The precise form and moment of redaction remain qualified.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

My teachers described those older debates without putting a torch to one another’s books. I gave that inherited disagreement its own column.

Mis maestros describían aquellos debates antiguos sin quemar los libros de los demás. Dediqué una columna a esa discrepancia heredada.

## Geography and map construction

Galilee, Sepphoris and Tiberias — 320 × 320 tiles; north-up design controls [35.113, 32.6, 35.65, 32.95].

Galilea con colinas cultivadas y asentamientos; costa del lago interior.

Mar de Galilea al este; Jordán sale hacia sur, no al Mediterráneo.

Seforis al oeste elevada; Tiberíades en costa occidental del lago.

Camino de mesetas hacia Tiberíades y eje de poblados.

Exclude: No mezclar aldeas separadas 30 km como barrio continuo; escala regional comprimida.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Tiberias west shore | [35.531, 32.79] | [238.79, 150.04] |
| Bet Shearim | [35.128, 32.703] | [25.05, 204.92] |
| Sepphoris area | [35.279, 32.754] | [105.13, 172.75] |

```json
{
  "bbox": [
    35.113,
    32.6,
    35.65,
    32.95
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Tiberias west shore",
      "lonLat": [
        35.531,
        32.79
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        238.79,
        150.04
      ]
    },
    {
      "id": "anchor-2",
      "name": "Bet Shearim",
      "lonLat": [
        35.128,
        32.703
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        25.05,
        204.92
      ]
    },
    {
      "id": "anchor-3",
      "name": "Sepphoris area",
      "lonLat": [
        35.279,
        32.754
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        105.13,
        172.75
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        105.13,
        172.75
      ],
      "purpose": {
        "en": "Link three settlements to the western archive.",
        "es-ES": "Conecta tres asentamientos con el archivo occidental."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        238.79,
        150.04
      ],
      "purpose": {
        "en": "Fund copying with 800 food and 400 gold while keeping village reserves.",
        "es-ES": "Financia la copia con 800 de alimento y 400 de oro conservando reservas aldeanas."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        25.05,
        204.92
      ],
      "purpose": {
        "en": "Deliver two completed copies to separate custodians.",
        "es-ES": "Entrega dos copias completas a custodios distintos."
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
          105.13,
          172.75
        ],
        [
          238.79,
          150.04
        ],
        [
          25.05,
          204.92
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          105.13,
          172.75
        ],
        [
          155.95999999999998,
          145.39499999999998
        ],
        [
          238.79,
          150.04
        ],
        [
          25.05,
          204.92
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        35.55,
        32.85
      ],
      [
        35.58,
        32.83
      ],
      [
        35.59,
        32.77
      ],
      [
        35.56,
        32.72
      ],
      [
        35.54,
        32.73
      ],
      [
        35.53,
        32.8
      ],
      [
        35.55,
        32.85
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "lake-outline"
  },
  "terrainProfile": "galilee",
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
  "asset": "docs/design/maps/jewish-tradition/02-the-hill-and-the-school.svg",
  "mainRouteLengthStraightTiles": 356.25
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
        "en": "Link three settlements to the western archive.",
        "es-ES": "Conecta tres asentamientos con el archivo occidental."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-1",
        "oncePerEntity": true,
        "required": "Link three settlements to the western archive."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "connect-settlement",
      "threshold": 3,
      "entities": [
        {
          "id": "02-the-hill-and-the-school-o1-entity-1",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "connect-settlement",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "02-the-hill-and-the-school-o1-entity-2",
          "atHub": "hub-1",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "connect-settlement",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "02-the-hill-and-the-school-o1-entity-3",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -2
          ],
          "role": "connect-settlement",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "connect-settlement",
        "requiredCount": 3,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Link three settlements to the western archive.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Fund copying with 800 food and 400 gold while keeping village reserves.",
        "es-ES": "Financia la copia con 800 de alimento y 400 de oro conservando reservas aldeanas."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-2",
        "oncePerEntity": true,
        "required": "Fund copying with 800 food and 400 gold while keeping village reserves."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "resource-delivery",
      "threshold": 1200,
      "entities": [
        {
          "id": "02-the-hill-and-the-school-o2-entity-1",
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
          "id": "02-the-hill-and-the-school-o2-entity-2",
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
          "id": "02-the-hill-and-the-school-o2-entity-3",
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
        "requiredCount": 1200,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "food": 800,
          "wood": 0,
          "gold": 400,
          "stone": 0
        },
        "criticalSecondaryRequirements": "Fund copying with 800 food and 400 gold while keeping village reserves.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Deliver two completed copies to separate custodians.",
        "es-ES": "Entrega dos copias completas a custodios distintos."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-3",
        "oncePerEntity": true,
        "required": "Deliver two completed copies to separate custodians."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-copy",
      "threshold": 2,
      "entities": [
        {
          "id": "02-the-hill-and-the-school-o3-entity-1",
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
          "id": "02-the-hill-and-the-school-o3-entity-2",
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
        "criticalSecondaryRequirements": "Deliver two completed copies to separate custodians.",
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
| easy | 875/625/312/250 | 2685/1075/1528/550 | 16 | 4 + 4 + 4 + 6 = 18 | 120 / 1108 |
| standard | 700/500/250/200 | 2620/1100/1430/600 | 12 | 6 + 6 + 6 + 6 = 24 | 90 / 1108 |
| hard | 595/425/212/170 | 2605/1125/1388/630 | 10 | 7 + 7 + 7 + 8 = 29 | 75 / 1108 |

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
        "food": 2685,
        "wood": 1075,
        "gold": 1528,
        "stone": 550
      },
      "mandatoryDeliveries": {
        "food": 800,
        "wood": 0,
        "gold": 400,
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
      "enemyTotalCap": 18,
      "initialEnemy": 4,
      "waves": [
        {
          "id": "wave-1",
          "count": 4,
          "composition": {
            "militia": 2,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 0
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1108,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 4,
          "composition": {
            "militia": 2,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 0
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 2216,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 6,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 3324,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 2,
        "spearman": 1,
        "archer": 1,
        "scoutCavalry": 0
      },
      "enemyNominalResourceCost": {
        "food": 760,
        "wood": 200,
        "gold": 360,
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
        "food": 2620,
        "wood": 1100,
        "gold": 1430,
        "stone": 600
      },
      "mandatoryDeliveries": {
        "food": 800,
        "wood": 0,
        "gold": 400,
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
      "enemyTotalCap": 24,
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
          "offsetSeconds": 1108,
          "warningSeconds": 90,
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
          "offsetSeconds": 2216,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 6,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 3324,
          "warningSeconds": 90,
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
        "food": 1180,
        "wood": 200,
        "gold": 420,
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
        "food": 2605,
        "wood": 1125,
        "gold": 1388,
        "stone": 630
      },
      "mandatoryDeliveries": {
        "food": 800,
        "wood": 0,
        "gold": 400,
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
      "enemyTotalCap": 29,
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
          "offsetSeconds": 1108,
          "warningSeconds": 75,
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
          "offsetSeconds": 2216,
          "warningSeconds": 75,
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
          "offsetSeconds": 3324,
          "warningSeconds": 75,
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
        "food": 1395,
        "wood": 250,
        "gold": 525,
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
    "worstDeliveryFood": 800,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Measure nav-path length in tiles / actual convoy speed plus loading/unloading; two round trips must fit between phase waves. If not, adjust announced gap or move receiving point within same documented district; architect approval for footprint drift.",
    "minimumWaveGapSecondsFromProposedGeometry": 1108
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Dos talleres; perder uno aumenta recorrido y coste limitado. Reservar 400 de alimento para recovery; no convertir al rival como condición.

{
  "plan": "Dos talleres; perder uno aumenta recorrido y coste limitado. Reservar 400 de alimento para recovery; no convertir al rival como condición.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.jewish-tradition.02-the-hill-and-the-school.title` / always | none → next | The Hill and the School | La colina y la escuela |
| `scenario.jewish-tradition.02-the-hill-and-the-school.fact-intro` / intro first | collection-narrator → next | Around the beginning of the third century, Judah the Prince was associated with the redaction of the Mishnah. Its transmission was a collective process. | Tradición de compilación de la Mishná y contexto de Judá el Príncipe; localización/fecha exacta de cada acto de escritura no se afirma. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.personal-intro` / after fact-intro | judith-copyist → next | My teachers described those older debates without putting a torch to one another’s books. I gave that inherited disagreement its own column. | Mis maestros describían aquellos debates antiguos sin quemar los libros de los demás. Dediqué una columna a esa discrepancia heredada. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.objective-1` / phase-1 active | none → hub-1 | Link three settlements to the western archive. | Conecta tres asentamientos con el archivo occidental. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.objective-2` / phase-2 active | none → hub-2 | Fund copying with 800 food and 400 gold while keeping village reserves. | Financia la copia con 800 de alimento y 400 de oro conservando reservas aldeanas. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.objective-3` / phase-3 active | none → hub-3 | Deliver two completed copies to separate custodians. | Entrega dos copias completas a custodios distintos. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.scouts` / scouts panel | none → next | Regional setting: Galilee, Sepphoris and Tiberias. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Galilee, Sepphoris and Tiberias. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.history` / history panel | none → next | Around the beginning of the third century, Judah the Prince was associated with the redaction of the Mishnah. Its transmission was a collective process. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Tradición de compilación de la Mishná y contexto de Judá el Príncipe; localización/fecha exacta de cada acto de escritura no se afirma. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.event-phase-1-complete` / o1 first becomes true | judith-copyist → next | One copy is safe. I prefer a second before congratulating anyone. | Una copia está a salvo. Prefiero una segunda antes de felicitar a nadie. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.event-phase-2-complete` / o2 first becomes true | judith-copyist → next | A margin is not wasted space. Sometimes it holds the disagreement we must keep. | Un margen no es espacio perdido. A veces guarda la discrepancia que debemos conservar. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.event-phase-3-complete` / o3 first becomes true | judith-copyist → next | Send them by separate roads. A living tradition needs more than one keeper. | Envíalas por caminos separados. Una tradición viva necesita más de un guardián. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | judith-copyist → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.victory-fact` / victory latch first | collection-narrator → next | Around the beginning of the third century, Judah the Prince was associated with the redaction of the Mishnah. Its transmission was a collective process. Your mission task is complete; this outcome does not change the documented events. | Los contadores representan logística, no una puntuación de ortodoxia religiosa. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.victory-personal` / after victory-fact | judith-copyist → 03-the-river-quarter | Send them by separate roads. A living tradition needs more than one keeper. | Envíalas por caminos separados. Una tradición viva necesita más de un guardián. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.recovery` / 6 minutes without objective progress | judith-copyist → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |

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
