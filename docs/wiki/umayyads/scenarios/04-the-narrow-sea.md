# The Narrow Sea / El mar estrecho

`umayyads/04-the-narrow-sea` · 711 CE · amphibious-supply

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/umayyads/04-the-narrow-sea.svg)

## Historical frame and outcome

Tariq’s forces crossed the strait in 711. This map represents the landing region, not a securely located battlefield of Guadalete.

Entrada de fuerzas en Iberia desde el norte de África. El desembarco es reconstrucción; no afirmar sitio exacto de Guadalete ni episodio de barcos quemados como certeza.

711 desembarco local; Al-Ándalus756+ será volumen distinto, no todo el territorio en una isla.

- [The Met, Art of the Umayyad Period](https://www.metmuseum.org/essays/the-art-of-the-umayyad-period-661-750): Dinastía y arquitectura. Referencia material; una construcción no mide la fe de sus habitantes.
- [Ibn Abd al-Hakam, Conquest of Spain](https://sourcebooks.web.fordham.edu/source/conqspain.asp): Strait crossing, late account. Ninth-century testimony; editorial introduction erroneously places Muslim expansion in sixth century. No hostage legend or exact army numbers reused.
- [José Beneroso Santos, dissertation (UNED, 2023)](https://portalcientifico.uned.es/documentos/647a293431258e1eec95307e): Accessible abstract: geography and proposed reinterpretation. Abstract only; proposed battle placement is not consensus and is not used as a surveyed battlefield.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

I was a child when those reports arrived. Years later I met men who disagreed about the landing. I kept their uncertainty beside the goods.

Era un niño cuando llegaron aquellas noticias. Años después conocí hombres que discrepaban sobre el desembarco. Guardé su incertidumbre junto a las mercancías.

## Geography and map construction

Strait of Gibraltar / landing corridor — 400 × 400 tiles; north-up design controls [-5.7, 35.894999999999996, -5.25, 36.25].

Costa rocosa, ensenadas y colinas del estrecho.

África al sur, Iberia al norte; tramo de mar separa ambos.

Peñón/sierras al norte; ruta costera oeste y paso interior.

Desembarco junto a costa, no representar toda conquista peninsular en un mapa.

Exclude: No fuerte moderno; ubicación exacta de Guadalete no se afirma ni se traslada al estrecho.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| North landing region | [-5.36, 36.11] | [290.54, 162.77] |
| Rock geographic control | [-5.344, 36.14] | [303.21, 133.39] |
| African coast control | [-5.45, 35.91] | [219.29, 358.66] |

```json
{
  "bbox": [
    -5.7,
    35.894999999999996,
    -5.25,
    36.25
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "North landing region",
      "lonLat": [
        -5.36,
        36.11
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        290.54,
        162.77
      ]
    },
    {
      "id": "anchor-2",
      "name": "Rock geographic control",
      "lonLat": [
        -5.344,
        36.14
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        303.21,
        133.39
      ]
    },
    {
      "id": "anchor-3",
      "name": "African coast control",
      "lonLat": [
        -5.45,
        35.91
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        219.29,
        358.66
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        219.29,
        358.66
      ],
      "purpose": {
        "en": "Scout the north-shore landing and the inland pass.",
        "es-ES": "Explora el desembarco de la costa norte y el paso interior."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        290.54,
        162.77
      ],
      "purpose": {
        "en": "Land three supply parties and establish the beach store.",
        "es-ES": "Desembarca tres grupos de suministro y establece el almacén de playa."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        303.21,
        133.39
      ],
      "purpose": {
        "en": "Escort the inland convoy without abandoning the shore recovery stock.",
        "es-ES": "Escolta el convoy interior sin abandonar la reserva de recuperación costera."
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
          219.29,
          358.66
        ],
        [
          290.54,
          162.77
        ],
        [
          303.21,
          133.39
        ]
      ],
      "widthTiles": 10,
      "mode": "transport"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          219.29,
          358.66
        ],
        [
          238.91500000000002,
          244.71500000000003
        ],
        [
          290.54,
          162.77
        ],
        [
          303.21,
          133.39
        ]
      ],
      "widthTiles": 6,
      "mode": "transport-then-land"
    }
  ],
  "controlLine": {
    "coordinates": [],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "gibraltar",
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
  "asset": "docs/design/maps/umayyads/04-the-narrow-sea.svg",
  "mainRouteLengthStraightTiles": 240.44
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
        "en": "Scout the north-shore landing and the inland pass.",
        "es-ES": "Explora el desembarco de la costa norte y el paso interior."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-1",
        "oncePerEntity": true,
        "required": "Scout the north-shore landing and the inland pass."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "scout-corridor",
      "threshold": 2,
      "entities": [
        {
          "id": "04-the-narrow-sea-o1-entity-1",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "scout-corridor",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-narrow-sea-o1-entity-2",
          "atHub": "hub-1",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "scout-corridor",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "scout-corridor",
        "requiredCount": 2,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Scout the north-shore landing and the inland pass.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Land three supply parties and establish the beach store.",
        "es-ES": "Desembarca tres grupos de suministro y establece el almacén de playa."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-2",
        "oncePerEntity": true,
        "required": "Land three supply parties and establish the beach store."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "land-supply-party",
      "threshold": 3,
      "entities": [
        {
          "id": "04-the-narrow-sea-o2-entity-1",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "land-supply-party",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-narrow-sea-o2-entity-2",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "land-supply-party",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-narrow-sea-o2-entity-3",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -2
          ],
          "role": "land-supply-party",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "land-supply-party",
        "requiredCount": 3,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Land three supply parties and establish the beach store.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Escort the inland convoy without abandoning the shore recovery stock.",
        "es-ES": "Escolta el convoy interior sin abandonar la reserva de recuperación costera."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-3",
        "oncePerEntity": true,
        "required": "Escort the inland convoy without abandoning the shore recovery stock."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "escort-caravan",
      "threshold": 1,
      "entities": [
        {
          "id": "04-the-narrow-sea-o3-entity-1",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "escort-caravan",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "escort-caravan",
        "requiredCount": 1,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Escort the inland convoy without abandoning the shore recovery stock.",
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
| easy | 1125/875/500/250 | 2355/1125/1420/550 | 28 | 24 + 24 + 24 + 27 = 99 | 120 / 777 |
| standard | 900/700/400/200 | 2340/1200/1360/600 | 24 | 33 + 33 + 33 + 33 = 132 | 90 / 777 |
| hard | 765/595/340/170 | 2235/1205/1260/630 | 20 | 39 + 39 + 39 + 41 = 158 | 75 / 777 |

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
      "enemyTotalCap": 99,
      "initialEnemy": 24,
      "waves": [
        {
          "id": "wave-1",
          "count": 24,
          "composition": {
            "militia": 8,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 777,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 24,
          "composition": {
            "militia": 8,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1554,
          "warningSeconds": 120,
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
          "offsetSeconds": 2331,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 8,
        "spearman": 6,
        "archer": 6,
        "scoutCavalry": 4
      },
      "enemyNominalResourceCost": {
        "food": 4220,
        "wood": 1200,
        "gold": 1780,
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
        "militia": 14,
        "spearman": 7,
        "archer": 7
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
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
      "enemyTotalCap": 132,
      "initialEnemy": 33,
      "waves": [
        {
          "id": "wave-1",
          "count": 33,
          "composition": {
            "militia": 12,
            "spearman": 8,
            "archer": 8,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 777,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 33,
          "composition": {
            "militia": 12,
            "spearman": 8,
            "archer": 8,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1554,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 33,
          "composition": {
            "militia": 12,
            "spearman": 8,
            "archer": 8,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 2331,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 12,
        "spearman": 8,
        "archer": 8,
        "scoutCavalry": 5
      },
      "enemyNominalResourceCost": {
        "food": 5600,
        "wood": 1600,
        "gold": 2400,
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
        "militia": 12,
        "spearman": 6,
        "archer": 6
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
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
      "enemyTotalCap": 158,
      "initialEnemy": 39,
      "waves": [
        {
          "id": "wave-1",
          "count": 39,
          "composition": {
            "militia": 15,
            "spearman": 9,
            "archer": 9,
            "scoutCavalry": 6
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 777,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 39,
          "composition": {
            "militia": 15,
            "spearman": 9,
            "archer": 9,
            "scoutCavalry": 6
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1554,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 41,
          "composition": {
            "militia": 15,
            "spearman": 10,
            "archer": 10,
            "scoutCavalry": 6
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 2331,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 15,
        "spearman": 9,
        "archer": 9,
        "scoutCavalry": 6
      },
      "enemyNominalResourceCost": {
        "food": 6815,
        "wood": 1850,
        "gold": 2865,
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
        "militia": 10,
        "spearman": 5,
        "archer": 5
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
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
    "travelTime": "Measure nav-path length in tiles / actual convoy speed plus loading/unloading; two round trips must fit between phase waves. If not, adjust announced gap or move receiving point within same documented district; architect approval for footprint drift.",
    "minimumWaveGapSecondsFromProposedGeometry": 777
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Cuatro transportes iniciales más uno reservado; dos playas transitables. Nunca quemar automáticamente todos los barcos ni exigir transporte ya destruido.

{
  "plan": "Cuatro transportes iniciales más uno reservado; dos playas transitables. Nunca quemar automáticamente todos los barcos ni exigir transporte ya destruido.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.umayyads.04-the-narrow-sea.title` / always | none → next | The Narrow Sea | El mar estrecho |
| `scenario.umayyads.04-the-narrow-sea.fact-intro` / intro first | collection-narrator → next | Tariq’s forces crossed the strait in 711. This map represents the landing region, not a securely located battlefield of Guadalete. | Entrada de fuerzas en Iberia desde el norte de África. El desembarco es reconstrucción; no afirmar sitio exacto de Guadalete ni episodio de barcos quemados como certeza. |
| `scenario.umayyads.04-the-narrow-sea.personal-intro` / after fact-intro | yasir-cloth-merchant → next | I was a child when those reports arrived. Years later I met men who disagreed about the landing. I kept their uncertainty beside the goods. | Era un niño cuando llegaron aquellas noticias. Años después conocí hombres que discrepaban sobre el desembarco. Guardé su incertidumbre junto a las mercancías. |
| `scenario.umayyads.04-the-narrow-sea.objective-1` / phase-1 active | none → hub-1 | Scout the north-shore landing and the inland pass. | Explora el desembarco de la costa norte y el paso interior. |
| `scenario.umayyads.04-the-narrow-sea.objective-2` / phase-2 active | none → hub-2 | Land three supply parties and establish the beach store. | Desembarca tres grupos de suministro y establece el almacén de playa. |
| `scenario.umayyads.04-the-narrow-sea.objective-3` / phase-3 active | none → hub-3 | Escort the inland convoy without abandoning the shore recovery stock. | Escolta el convoy interior sin abandonar la reserva de recuperación costera. |
| `scenario.umayyads.04-the-narrow-sea.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.umayyads.04-the-narrow-sea.scouts` / scouts panel | none → next | Regional setting: Strait of Gibraltar / landing corridor. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Strait of Gibraltar / landing corridor. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.umayyads.04-the-narrow-sea.history` / history panel | none → next | Tariq’s forces crossed the strait in 711. This map represents the landing region, not a securely located battlefield of Guadalete. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Entrada de fuerzas en Iberia desde el norte de África. El desembarco es reconstrucción; no afirmar sitio exacto de Guadalete ni episodio de barcos quemados como certeza. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.umayyads.04-the-narrow-sea.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.umayyads.04-the-narrow-sea.event-phase-1-complete` / o1 first becomes true | yasir-cloth-merchant → next | The first load arrived. My family’s old accounts rarely mention the people who carried it. | La primera carga ha llegado. Las cuentas antiguas de mi familia apenas nombran a quienes la llevaron. |
| `scenario.umayyads.04-the-narrow-sea.event-phase-2-complete` / o2 first becomes true | yasir-cloth-merchant → next | Keep the shore store supplied. An ambitious road still needs somewhere to return. | Mantén abastecido el almacén de la costa. Hasta un camino ambicioso necesita un lugar al que volver. |
| `scenario.umayyads.04-the-narrow-sea.event-phase-3-complete` / o3 first becomes true | yasir-cloth-merchant → next | The ledger survived. That is less than victory, and more than nothing. | El registro sobrevivió. Es menos que una victoria y más que nada. |
| `scenario.umayyads.04-the-narrow-sea.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | yasir-cloth-merchant → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.umayyads.04-the-narrow-sea.victory-fact` / victory latch first | collection-narrator → next | Tariq’s forces crossed the strait in 711. This map represents the landing region, not a securely located battlefield of Guadalete. Your mission task is complete; this outcome does not change the documented events. | 711 desembarco local; Al-Ándalus756+ será volumen distinto, no todo el territorio en una isla. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.umayyads.04-the-narrow-sea.victory-personal` / after victory-fact | yasir-cloth-merchant → 05-the-last-crossing | The ledger survived. That is less than victory, and more than nothing. | El registro sobrevivió. Es menos que una victoria y más que nada. |
| `scenario.umayyads.04-the-narrow-sea.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.umayyads.04-the-narrow-sea.recovery` / 6 minutes without objective progress | yasir-cloth-merchant → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |

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
