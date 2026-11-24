# The Price of Peace / El precio de la paz

`church-of-rome/02-the-price-of-peace` · 593–595 CE · bounded-negotiation

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/church-of-rome/02-the-price-of-peace.svg)

## Historical frame and outcome

Gregory’s correspondence records difficult negotiations involving Lombard leaders and imperial officials in the 590s.

Gregorio negocia paz y arbitraje con poderes lombardos e imperiales; no consenso religioso universal.

La diplomacia local se distingue de dominio territorial y arbitraje imperial.

- [Gregory I, Register V.36](https://www.newadvent.org/fathers/360205036.htm): V.36: arbitraje con Agilulfo y exarca. Las negociaciones no tienen un resultado único impuesto por esta carta.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

A singer prefers a bargain with a tidy ending. Gregory’s letters offer no such comfort. I kept their awkward pauses.

Un cantor prefiere un trato con un final limpio. Las cartas de Gregorio no ofrecen ese consuelo. Conservé sus pausas incómodas.

## Geography and map construction

Rome, Portus and Ostia — 320 × 320 tiles; north-up design controls [12.18, 41.69, 12.56, 41.96].

Corredor entre litoral y Roma, cultivos/colinas y cauce.

Tíber desemboca al suroeste; Portus al norte de desembocadura, Ostia al sur.

Roma elevada respecto al litoral; llano portuario.

Eje fluvial hacia Roma noreste; caminos paralelos a ambas orillas.

Exclude: Litoral antiguo más interior; línea moderna solo orientación, no coste reconstruida. Sin San Pedro renacentista.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Rome civic centre | [12.486, 41.892] | [246.45, 92.11] |
| Ostia harbour region | [12.288, 41.756] | [98.04, 228.9] |
| Lower Tiber road | [12.4, 41.83] | [181.99, 154.47] |

```json
{
  "bbox": [
    12.18,
    41.69,
    12.56,
    41.96
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Rome civic centre",
      "lonLat": [
        12.486,
        41.892
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        246.45,
        92.11
      ]
    },
    {
      "id": "anchor-2",
      "name": "Ostia harbour region",
      "lonLat": [
        12.288,
        41.756
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        98.04,
        228.9
      ]
    },
    {
      "id": "anchor-3",
      "name": "Lower Tiber road",
      "lonLat": [
        12.4,
        41.83
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        181.99,
        154.47
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        181.99,
        154.47
      ],
      "purpose": {
        "en": "Escort the two envoys through distinct guarded roads.",
        "es-ES": "Escolta a los dos enviados por caminos vigilados distintos."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        246.45,
        92.11
      ],
      "purpose": {
        "en": "Fund one negotiated passage and deliver its sealed agreement.",
        "es-ES": "Financia un paso negociado y entrega su acuerdo sellado."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        98.04,
        228.9
      ],
      "purpose": {
        "en": "Supply Rome without renewing an already paid levy.",
        "es-ES": "Abastece Roma sin volver a pagar un peaje ya satisfecho."
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
          181.99,
          154.47
        ],
        [
          246.45,
          92.11
        ],
        [
          98.04,
          228.9
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          181.99,
          154.47
        ],
        [
          222.22,
          131.29
        ],
        [
          246.45,
          92.11
        ],
        [
          98.04,
          228.9
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        12.477,
        41.95
      ],
      [
        12.47,
        41.925
      ],
      [
        12.47,
        41.9
      ],
      [
        12.475,
        41.87
      ],
      [
        12.42,
        41.85
      ],
      [
        12.4,
        41.8
      ],
      [
        12.28,
        41.76
      ],
      [
        12.23,
        41.73
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "rome-ostia",
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
  "asset": "docs/design/maps/church-of-rome/02-the-price-of-peace.svg",
  "mainRouteLengthStraightTiles": 291.52,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        228.45,
        104.11
      ],
      [
        264.45,
        104.11
      ]
    ],
    "widthTiles": 6,
    "distanceTiles": 36.0,
    "placement": "fictional local supply circuit on SAME bank/plateau in receiving district; validate terrain and footprints, no invented river crossing",
    "twoRoundTripFormula": "4 * measured one-way navigable distance / measured convoy speed + loading/reaction allowance"
  },
  "explorationPlan": {
    "classification": "optional fictional tasks within dated geographic districts; not surveyed ancient locations",
    "sectors": [],
    "secondaryObjectiveIds": [
      "side-1",
      "side-2",
      "side-3",
      "side-4",
      "side-5",
      "side-6"
    ],
    "connectingTrails": "use main/relief corridors to the task districts; optional travel must not create an extra mandatory crossing",
    "qualityGate": "certify each task path, safe delivery zone and footprint at all difficulties; geography remains authoritative"
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
        "en": "Escort the two envoys through distinct guarded roads.",
        "es-ES": "Escolta a los dos enviados por caminos vigilados distintos."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-the-price-of-peace.o1",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "escort-envoy",
      "threshold": 2,
      "entities": [
        {
          "id": "02-the-price-of-peace.o1.main-entities.1",
          "role": "envoy",
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
          "id": "02-the-price-of-peace.o1.main-entities.2",
          "role": "envoy",
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
        "operation": "escort-envoy",
        "requiredCount": 2,
        "destination": "hub-1",
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
              "02-the-price-of-peace.o1.main-entities.1",
              "02-the-price-of-peace.o1.main-entities.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true,
            "destinations": {
              "02-the-price-of-peace.o1.main-entities.1": "02-the-price-of-peace.distinct-envoy-roads.1",
              "02-the-price-of-peace.o1.main-entities.2": "02-the-price-of-peace.distinct-envoy-roads.2"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          }
        ],
        "requiredLedgers": [
          "main-entities"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Fund one negotiated passage and deliver its sealed agreement.",
        "es-ES": "Financia un paso negociado y entrega su acuerdo sellado."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-the-price-of-peace.o2",
        "oncePerEntity": true,
        "required": 1
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "pay-once-and-deliver",
      "threshold": 1,
      "entities": [
        {
          "id": "02-the-price-of-peace.o2.sealed-agreement.1",
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
        "operation": "pay-once-and-deliver",
        "requiredCount": 1,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "gold": 400
        },
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "paymentGold": 400,
        "requirements": [
          {
            "id": "audited-delivery",
            "kind": "resource-transaction",
            "amounts": {
              "gold": 400
            },
            "receivingZones": [
              "02-the-price-of-peace.o2-supply-district.1"
            ],
            "allocations": {
              "02-the-price-of-peace.o2-supply-district.1": {
                "gold": 400
              }
            },
            "paidFlag": "02-the-price-of-peace.o2.audited-delivery.paid",
            "account": "spendable",
            "atomic": true,
            "once": true,
            "commit": "debit resources AND persist receipt in same guarded transition; repeated arrivals/save cannot repay"
          },
          {
            "id": "sealed-agreement",
            "kind": "entity-state",
            "state": "arrived",
            "entities": [
              "02-the-price-of-peace.o2.sealed-agreement.1"
            ],
            "requiredCount": 1,
            "oncePerEntity": true,
            "destinations": {
              "02-the-price-of-peace.o2.sealed-agreement.1": "02-the-price-of-peace.o2.sealed-agreement.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          }
        ],
        "requiredLedgers": [
          "audited-delivery",
          "sealed-agreement"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Supply Rome without renewing an already paid levy.",
        "es-ES": "Abastece Roma sin volver a pagar un peaje ya satisfecho."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-the-price-of-peace.o3",
        "oncePerEntity": true,
        "required": 1200
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "resource-delivery",
      "threshold": 1200,
      "entities": [],
      "predicate": {
        "operator": "all",
        "operation": "resource-delivery",
        "requiredCount": 1200,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "food": 1200
        },
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "audited-delivery",
            "kind": "resource-transaction",
            "amounts": {
              "food": 1200
            },
            "receivingZones": [
              "02-the-price-of-peace.o3-supply-district.1"
            ],
            "allocations": {
              "02-the-price-of-peace.o3-supply-district.1": {
                "food": 1200
              }
            },
            "paidFlag": "02-the-price-of-peace.o3.audited-delivery.paid",
            "account": "spendable",
            "atomic": true,
            "once": true,
            "commit": "debit resources AND persist receipt in same guarded transition; repeated arrivals/save cannot repay"
          },
          {
            "id": "no-repeated-levy",
            "kind": "receipt-exists",
            "flag": "02-the-price-of-peace.o2.audited-delivery.paid",
            "fromObjective": "o2",
            "amounts": {
              "gold": 400
            },
            "newDebit": false
          }
        ],
        "requiredLedgers": [
          "audited-delivery",
          "no-repeated-levy"
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
        "id": "02-the-price-of-peace.o1.main-entities.1",
        "role": "envoy",
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
        "id": "02-the-price-of-peace.o1.main-entities.2",
        "role": "envoy",
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
        "id": "02-the-price-of-peace.o2.sealed-agreement.1",
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
      }
    ],
    "zones": [
      {
        "id": "02-the-price-of-peace.distinct-envoy-roads.1",
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
        "id": "02-the-price-of-peace.distinct-envoy-roads.2",
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
        "id": "02-the-price-of-peace.o2-supply-district.1",
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
        "id": "02-the-price-of-peace.o3-supply-district.1",
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
        "id": "02-the-price-of-peace.o2.sealed-agreement.receiving-zone",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid ground within geographic district; receiving zone excludes origins",
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
  },
  "secondaryObjectives": [
    {
      "id": "side-1",
      "kind": "copy",
      "title": {
        "en": "What the Fire Must Not Take — the envoys public copies",
        "es-ES": "Lo que el fuego no debe llevarse — las copias públicas de los enviados"
      },
      "subject": {
        "en": "the envoys public copies",
        "es-ES": "las copias públicas de los enviados"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Price of Peace supports this bounded fictional local task. It concerns the envoys public copies; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El precio de la paz permite esta tarea local ficticia y limitada. Se ocupa de las copias públicas de los enviados; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Recover both separate copies from the envoys public copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.",
        "es-ES": "Recupera las dos copias distintas de las copias públicas de los enviados y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-arrival",
            "entities": [
              "02-the-price-of-peace.side-1.entity-1",
              "02-the-price-of-peace.side-1.entity-2"
            ],
            "destinations": {
              "02-the-price-of-peace.side-1.entity-1": "02-the-price-of-peace.side-1.zone-1",
              "02-the-price-of-peace.side-1.entity-2": "02-the-price-of-peace.side-1.zone-1"
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
            "id": "02-the-price-of-peace.side-1.entity-1",
            "role": "copy",
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
            "id": "02-the-price-of-peace.side-1.entity-2",
            "role": "copy",
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
            "id": "02-the-price-of-peace.side-1.zone-1",
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
          "kind": "unlock-context-and-hint",
          "target": "documented context and a main-goal hint",
          "resources": {},
          "onceFlag": "02-the-price-of-peace.side-1.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "sourceIds": [
            "gregory-peace"
          ],
          "historicalNote": {
            "en": "Gregory’s correspondence records difficult negotiations involving Lombard leaders and imperial officials in the 590s.",
            "es-ES": "Gregorio negocia paz y arbitraje con poderes lombardos e imperiales; no consenso religioso universal."
          },
          "hint": {
            "en": "Escort the two envoys through distinct guarded roads.",
            "es-ES": "Escolta a los dos enviados por caminos vigilados distintos."
          }
        }
      ],
      "completionFlag": "02-the-price-of-peace.side-1.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
      "reachability": {
        "originHub": "hub-3",
        "receivingHub": "hub-1",
        "corridorIds": [
          "main",
          "relief"
        ],
        "maxRequiredRoundTrips": 1,
        "spawnOutsideReceivingZone": true,
        "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-2",
      "kind": "trade",
      "title": {
        "en": "One Honest Consignment — the truce-road post",
        "es-ES": "Una remesa honrada — el puesto del camino de la tregua"
      },
      "subject": {
        "en": "the truce-road post",
        "es-ES": "el puesto del camino de la tregua"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Price of Peace supports this bounded fictional local task. It concerns the truce-road post; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El precio de la paz permite esta tarea local ficticia y limitada. Se ocupa de el puesto del camino de la tregua; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the trader of the truce-road post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.",
        "es-ES": "Escolta al comerciante de el puesto del camino de la tregua hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-arrival",
            "entities": [
              "02-the-price-of-peace.side-2.entity-1"
            ],
            "destinations": {
              "02-the-price-of-peace.side-2.entity-1": "02-the-price-of-peace.side-2.zone-1"
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
            "receipt": "02-the-price-of-peace.side-2.payment",
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
            "id": "02-the-price-of-peace.side-2.entity-1",
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
            "id": "02-the-price-of-peace.side-2.zone-1",
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
          "onceFlag": "02-the-price-of-peace.side-2.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "02-the-price-of-peace.side-2.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
      "reachability": {
        "originHub": "hub-1",
        "receivingHub": "hub-2",
        "corridorIds": [
          "main",
          "relief"
        ],
        "maxRequiredRoundTrips": 1,
        "spawnOutsideReceivingZone": true,
        "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-3",
      "kind": "guide",
      "title": {
        "en": "The Path Between — the second envoy road",
        "es-ES": "El camino entre ambos — el segundo camino de los enviados"
      },
      "subject": {
        "en": "the second envoy road",
        "es-ES": "el segundo camino de los enviados"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Price of Peace supports this bounded fictional local task. It concerns the second envoy road; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El precio de la paz permite esta tarea local ficticia y limitada. Se ocupa de el segundo camino de los enviados; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the local guide of the second envoy road to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.",
        "es-ES": "Escolta al guía local de el segundo camino de los enviados hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-arrival",
            "entities": [
              "02-the-price-of-peace.side-3.entity-1"
            ],
            "destinations": {
              "02-the-price-of-peace.side-3.entity-1": "02-the-price-of-peace.side-3.zone-1"
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
            "id": "02-the-price-of-peace.side-3.entity-1",
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
            "id": "02-the-price-of-peace.side-3.zone-1",
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
          "target": "relief corridor",
          "resources": {},
          "onceFlag": "02-the-price-of-peace.side-3.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "corridorId": "relief"
        }
      ],
      "completionFlag": "02-the-price-of-peace.side-3.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
      "reachability": {
        "originHub": "hub-1",
        "receivingHub": "hub-3",
        "corridorIds": [
          "main",
          "relief"
        ],
        "maxRequiredRoundTrips": 1,
        "spawnOutsideReceivingZone": true,
        "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-4",
      "kind": "aid",
      "title": {
        "en": "A Place at the Hearth — the waiting families",
        "es-ES": "Un lugar junto al hogar — las familias que esperan"
      },
      "subject": {
        "en": "the waiting families",
        "es-ES": "las familias que esperan"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Price of Peace supports this bounded fictional local task. It concerns the waiting families; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El precio de la paz permite esta tarea local ficticia y limitada. Se ocupa de las familias que esperan; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Bring each of the two aid crates to its assigned household at the waiting families. Benefit: 100 food, 50 wood, once.",
        "es-ES": "Lleva cada una de las dos cajas de ayuda a su hogar asignado en las familias que esperan. Ventaja: 100 de alimento, 50 de madera, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-arrival",
            "entities": [
              "02-the-price-of-peace.side-4.entity-1",
              "02-the-price-of-peace.side-4.entity-2"
            ],
            "destinations": {
              "02-the-price-of-peace.side-4.entity-1": "02-the-price-of-peace.side-4.zone-1",
              "02-the-price-of-peace.side-4.entity-2": "02-the-price-of-peace.side-4.zone-2"
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
            "id": "02-the-price-of-peace.side-4.entity-1",
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
            "id": "02-the-price-of-peace.side-4.entity-2",
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
            "id": "02-the-price-of-peace.side-4.zone-1",
            "hub": "hub-2",
            "offsetTiles": [
              -8,
              0
            ],
            "radiusTiles": 3
          },
          {
            "id": "02-the-price-of-peace.side-4.zone-2",
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
          "onceFlag": "02-the-price-of-peace.side-4.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "02-the-price-of-peace.side-4.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
      "reachability": {
        "originHub": "hub-1",
        "receivingHub": "hub-2",
        "corridorIds": [
          "main",
          "relief"
        ],
        "maxRequiredRoundTrips": 1,
        "spawnOutsideReceivingZone": true,
        "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-5",
      "kind": "watch",
      "title": {
        "en": "Eyes Beyond the Gate — the guarded-road approaches",
        "es-ES": "Ojos más allá de la puerta — las aproximaciones a los caminos vigilados"
      },
      "subject": {
        "en": "the guarded-road approaches",
        "es-ES": "las aproximaciones a los caminos vigilados"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Price of Peace supports this bounded fictional local task. It concerns the guarded-road approaches; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El precio de la paz permite esta tarea local ficticia y limitada. Se ocupa de las aproximaciones a los caminos vigilados; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Visit both observation posts overlooking the guarded-road approaches. Benefit: reveal the first and last reserve approaches.",
        "es-ES": "Visita los dos puestos de observación sobre las aproximaciones a los caminos vigilados. Ventaja: revela las aproximaciones de la primera y la última reserva."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "visit-zones",
            "zones": [
              "02-the-price-of-peace.side-5.zone-1",
              "02-the-price-of-peace.side-5.zone-2"
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
            "id": "02-the-price-of-peace.side-5.zone-1",
            "hub": "hub-2",
            "offsetTiles": [
              0,
              -8
            ],
            "radiusTiles": 3
          },
          {
            "id": "02-the-price-of-peace.side-5.zone-2",
            "hub": "hub-3",
            "offsetTiles": [
              0,
              8
            ],
            "radiusTiles": 3
          }
        ]
      },
      "effects": [
        {
          "kind": "reveal-enemy-approach",
          "target": "wave-1 and wave-3 approaches",
          "resources": {},
          "onceFlag": "02-the-price-of-peace.side-5.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "rosterIds": [
            "wave-1",
            "wave-3"
          ],
          "alreadyReleasedPolicy": "reveal current surviving members, never spawn a replacement"
        }
      ],
      "completionFlag": "02-the-price-of-peace.side-5.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
      "reachability": {
        "originHub": "hub-3",
        "receivingHub": "hub-2",
        "corridorIds": [
          "main",
          "relief"
        ],
        "maxRequiredRoundTrips": 1,
        "spawnOutsideReceivingZone": true,
        "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-6",
      "kind": "repair",
      "title": {
        "en": "Raise the Store Again — the reception store",
        "es-ES": "Levantar de nuevo el almacén — el almacén receptor"
      },
      "subject": {
        "en": "the reception store",
        "es-ES": "el almacén receptor"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Price of Peace supports this bounded fictional local task. It concerns the reception store; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El precio de la paz permite esta tarea local ficticia y limitada. Se ocupa de el almacén receptor; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Pay 50 wood and restore the damaged store of the reception store to full health. Benefit: 200 food, 100 wood, once.",
        "es-ES": "Paga 50 de madera y repara por completo el almacén dañado de el almacén receptor. Ventaja: 200 de alimento, 100 de madera, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-health",
            "entity": "02-the-price-of-peace.side-6.entity-1",
            "health": "full",
            "paymentReceipt": "02-the-price-of-peace.side-6.payment",
            "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
          },
          {
            "kind": "atomic-payment",
            "resources": {
              "wood": 50
            },
            "receipt": "02-the-price-of-peace.side-6.payment",
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
            "id": "02-the-price-of-peace.side-6.entity-1",
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
            "id": "02-the-price-of-peace.side-6.zone-1",
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
          "onceFlag": "02-the-price-of-peace.side-6.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "02-the-price-of-peace.side-6.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
      "reachability": {
        "originHub": "hub-2",
        "receivingHub": "hub-2",
        "corridorIds": [
          "main",
          "relief"
        ],
        "maxRequiredRoundTrips": 1,
        "spawnOutsideReceivingZone": true,
        "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    }
  ],
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
    "fundingPolicy": "replace old generic caches, never stack rewards; withdraw once from reserved gatherable stock; all main goals solvent when every optional goal is skipped",
    "nativeStatus": "design-only; requires certified reusable predicates and native QA"
  },
  "playstyles": [
    {
      "id": "careful-supply",
      "optionalObjectives": [
        "side-6",
        "side-2",
        "side-4"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "informed-movement",
      "optionalObjectives": [
        "side-3",
        "side-5",
        "side-1"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "civilian-and-memory",
      "optionalObjectives": [
        "side-4",
        "side-1",
        "side-3"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    }
  ]
}
```

## Difficulty and finite budget

These are explicit estimates for calibration, not measured wins or evidence of perfect balance. Player starting military is preplaced; enemy initial/waves are one roster with production disabled. Nominal militia/spearman/archer/scout costs audit the plan, not historical army numbers. Resource banks include mandatory delivery, replacement allowance, protected recovery and a surplus.

| Profile | Start F/W/G/S | Gatherable F/W/G/S | Escort | Initial + waves | Warning / gap seconds |
|---|---|---|---:|---|---|
| easy | 875/625/312/250 | 3085/1075/1528/550 | 16 | 9 + 9 + 9 + 9 = 36 | 120 / 474 |
| standard | 700/500/250/200 | 3020/1100/1430/600 | 12 | 12 + 12 + 12 + 12 = 48 | 90 / 370 |
| hard | 595/425/212/170 | 3005/1125/1388/630 | 10 | 14 + 14 + 14 + 16 = 58 | 75 / 296 |

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
        "food": 3085,
        "wood": 1075,
        "gold": 1528,
        "stone": 550
      },
      "mandatoryDeliveries": {
        "food": 1200,
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
          "offsetSeconds": 474,
          "warningSeconds": 120,
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
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts.",
      "accessibleWithoutOptionalRewards": {
        "food": 3510,
        "wood": 1500,
        "gold": 1840,
        "stone": 800
      }
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
        "food": 3020,
        "wood": 1100,
        "gold": 1430,
        "stone": 600
      },
      "mandatoryDeliveries": {
        "food": 1200,
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
      "enemyTotalCap": 48,
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
          "offsetSeconds": 370,
          "warningSeconds": 90,
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
          "offsetSeconds": 740,
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
          "offsetSeconds": 1110,
          "warningSeconds": 90,
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
        "food": 2020,
        "wood": 600,
        "gold": 860,
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
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts.",
      "accessibleWithoutOptionalRewards": {
        "food": 3270,
        "wood": 1400,
        "gold": 1680,
        "stone": 800
      }
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
        "food": 3005,
        "wood": 1125,
        "gold": 1388,
        "stone": 630
      },
      "mandatoryDeliveries": {
        "food": 1200,
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
      "enemyTotalCap": 58,
      "initialEnemy": 14,
      "waves": [
        {
          "id": "wave-1",
          "count": 14,
          "composition": {
            "militia": 6,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 296,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 14,
          "composition": {
            "militia": 6,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 592,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 16,
          "composition": {
            "militia": 6,
            "spearman": 4,
            "archer": 4,
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
        "militia": 6,
        "spearman": 3,
        "archer": 3,
        "scoutCavalry": 2
      },
      "enemyNominalResourceCost": {
        "food": 2535,
        "wood": 650,
        "gold": 1065,
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
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts.",
      "accessibleWithoutOptionalRewards": {
        "food": 3150,
        "wood": 1350,
        "gold": 1600,
        "stone": 800
      }
    }
  },
  "analysis": {
    "classification": "feasibility envelope, not a combat simulation or proof of balance",
    "startingWorkers": 12,
    "plannedPeakWorkers": 18,
    "effectiveGatherRatePerWorkerResourcePerSecondAssumption": 0.24,
    "walkingAndIdleIncluded": "Assumed rate discounts native gathering for travel/idle; measure actual efficiency in game.",
    "worstDeliveryFood": 1200,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Phase waves use the separate local phase-two supply circuit, not the whole-map journey. Two round trips +90s loading/reaction fit the floor. Validate actual nav-path/speed and recompute before game approval.",
    "minimumWaveGapSecondsFromProposedGeometry": 296,
    "wholeJourneyDistanceTiles": 291.52,
    "wholeJourneyOneWaySecondsEstimate": 417,
    "optionalCacheAllocation": {
      "food": 600,
      "wood": 300,
      "gold": 150,
      "stone": 0
    },
    "solventWithoutOptionalCaches": true
  },
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
    "fundingPolicy": "replace old generic caches, never stack rewards; withdraw once from reserved gatherable stock; all main goals solvent when every optional goal is skipped",
    "nativeStatus": "design-only; requires certified reusable predicates and native QA"
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Un pago por control; intento fallido no consume ambos presupuestos. Correo reemplazable y ruta de mayor escolta sin peaje.

{
  "plan": "Un pago por control; intento fallido no consume ambos presupuestos. Correo reemplazable y ruta de mayor escolta sin peaje.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.church-of-rome.02-the-price-of-peace.title` / always | none → next | The Price of Peace | El precio de la paz |
| `scenario.church-of-rome.02-the-price-of-peace.fact-intro` / intro first | collection-narrator → next | Gregory’s correspondence records difficult negotiations involving Lombard leaders and imperial officials in the 590s. | Gregorio negocia paz y arbitraje con poderes lombardos e imperiales; no consenso religioso universal. |
| `scenario.church-of-rome.02-the-price-of-peace.personal-intro` / after fact-intro | leo-road-singer → next | A singer prefers a bargain with a tidy ending. Gregory’s letters offer no such comfort. I kept their awkward pauses. | Un cantor prefiere un trato con un final limpio. Las cartas de Gregorio no ofrecen ese consuelo. Conservé sus pausas incómodas. |
| `scenario.church-of-rome.02-the-price-of-peace.objective-1` / phase-1 active | none → hub-1 | Escort the two envoys through distinct guarded roads. | Escolta a los dos enviados por caminos vigilados distintos. |
| `scenario.church-of-rome.02-the-price-of-peace.objective-2` / phase-2 active | none → hub-2 | Fund one negotiated passage and deliver its sealed agreement. | Financia un paso negociado y entrega su acuerdo sellado. |
| `scenario.church-of-rome.02-the-price-of-peace.objective-3` / phase-3 active | none → hub-3 | Supply Rome without renewing an already paid levy. | Abastece Roma sin volver a pagar un peaje ya satisfecho. |
| `scenario.church-of-rome.02-the-price-of-peace.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.church-of-rome.02-the-price-of-peace.scouts` / scouts panel | none → next | Regional setting: Rome, Portus and Ostia. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Rome, Portus and Ostia. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.church-of-rome.02-the-price-of-peace.history` / history panel | none → next | Gregory’s correspondence records difficult negotiations involving Lombard leaders and imperial officials in the 590s. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Gregorio negocia paz y arbitraje con poderes lombardos e imperiales; no consenso religioso universal. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.church-of-rome.02-the-price-of-peace.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.church-of-rome.02-the-price-of-peace.event-phase-1-complete` / o1 first becomes true | leo-road-singer → next | The road has its first verse. Do not mistake a good rhyme for a full granary. | El camino tiene su primer verso. No confundas una buena rima con un granero lleno. |
| `scenario.church-of-rome.02-the-price-of-peace.event-phase-2-complete` / o2 first becomes true | leo-road-singer → next | My song can shorten the journey. Your wagons still have to make it. | Mi cantar puede acortar el viaje. Tus carros aún tienen que recorrerlo. |
| `scenario.church-of-rome.02-the-price-of-peace.event-phase-3-complete` / o3 first becomes true | leo-road-singer → next | That is where I end this verse. The record will tell you what the song leaves out. | Aquí termino este verso. El registro te dirá lo que el cantar deja fuera. |
| `scenario.church-of-rome.02-the-price-of-peace.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | leo-road-singer → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.church-of-rome.02-the-price-of-peace.victory-fact` / victory latch first | collection-narrator → next | Gregory’s correspondence records difficult negotiations involving Lombard leaders and imperial officials in the 590s. Your mission task is complete; this outcome does not change the documented events. | La diplomacia local se distingue de dominio territorial y arbitraje imperial. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.church-of-rome.02-the-price-of-peace.victory-personal` / after victory-fact | leo-road-singer → 03-roads-to-pavia | That is where I end this verse. The record will tell you what the song leaves out. | Aquí termino este verso. El registro te dirá lo que el cantar deja fuera. |
| `scenario.church-of-rome.02-the-price-of-peace.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.church-of-rome.02-the-price-of-peace.recovery` / 6 minutes without objective progress | leo-road-singer → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.church-of-rome.02-the-price-of-peace.side-1-brief` / optional objectives tab, always available | leo-road-singer → return-to-game | Recover both separate copies from the envoys public copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de las copias públicas de los enviados y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| `scenario.church-of-rome.02-the-price-of-peace.side-1-completed` / 02-the-price-of-peace.side-1.completed latched; once | leo-road-singer → return-to-game | Optional task completed: What the Fire Must Not Take — the envoys public copies. Sing of the road, and leave a verse for the hands that kept it open. | Tarea opcional completada: Lo que el fuego no debe llevarse — las copias públicas de los enviados. Canta al camino, y deja un verso para las manos que lo mantuvieron abierto. |
| `scenario.church-of-rome.02-the-price-of-peace.side-1-unavailable` / unique optional entity irrecoverably lost; once | leo-road-singer → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.church-of-rome.02-the-price-of-peace.side-2-brief` / optional objectives tab, always available | leo-road-singer → return-to-game | Escort the trader of the truce-road post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de el puesto del camino de la tregua hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| `scenario.church-of-rome.02-the-price-of-peace.side-2-completed` / 02-the-price-of-peace.side-2.completed latched; once | leo-road-singer → return-to-game | Optional task completed: One Honest Consignment — the truce-road post. Sing of the road, and leave a verse for the hands that kept it open. | Tarea opcional completada: Una remesa honrada — el puesto del camino de la tregua. Canta al camino, y deja un verso para las manos que lo mantuvieron abierto. |
| `scenario.church-of-rome.02-the-price-of-peace.side-2-unavailable` / unique optional entity irrecoverably lost; once | leo-road-singer → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.church-of-rome.02-the-price-of-peace.side-3-brief` / optional objectives tab, always available | leo-road-singer → return-to-game | Escort the local guide of the second envoy road to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de el segundo camino de los enviados hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| `scenario.church-of-rome.02-the-price-of-peace.side-3-completed` / 02-the-price-of-peace.side-3.completed latched; once | leo-road-singer → return-to-game | Optional task completed: The Path Between — the second envoy road. Sing of the road, and leave a verse for the hands that kept it open. | Tarea opcional completada: El camino entre ambos — el segundo camino de los enviados. Canta al camino, y deja un verso para las manos que lo mantuvieron abierto. |
| `scenario.church-of-rome.02-the-price-of-peace.side-3-unavailable` / unique optional entity irrecoverably lost; once | leo-road-singer → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.church-of-rome.02-the-price-of-peace.side-4-brief` / optional objectives tab, always available | leo-road-singer → return-to-game | Bring each of the two aid crates to its assigned household at the waiting families. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en las familias que esperan. Ventaja: 100 de alimento, 50 de madera, una vez. |
| `scenario.church-of-rome.02-the-price-of-peace.side-4-completed` / 02-the-price-of-peace.side-4.completed latched; once | leo-road-singer → return-to-game | Optional task completed: A Place at the Hearth — the waiting families. Sing of the road, and leave a verse for the hands that kept it open. | Tarea opcional completada: Un lugar junto al hogar — las familias que esperan. Canta al camino, y deja un verso para las manos que lo mantuvieron abierto. |
| `scenario.church-of-rome.02-the-price-of-peace.side-4-unavailable` / unique optional entity irrecoverably lost; once | leo-road-singer → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.church-of-rome.02-the-price-of-peace.side-5-brief` / optional objectives tab, always available | leo-road-singer → return-to-game | Visit both observation posts overlooking the guarded-road approaches. Benefit: reveal the first and last reserve approaches. | Visita los dos puestos de observación sobre las aproximaciones a los caminos vigilados. Ventaja: revela las aproximaciones de la primera y la última reserva. |
| `scenario.church-of-rome.02-the-price-of-peace.side-5-completed` / 02-the-price-of-peace.side-5.completed latched; once | leo-road-singer → return-to-game | Optional task completed: Eyes Beyond the Gate — the guarded-road approaches. Sing of the road, and leave a verse for the hands that kept it open. | Tarea opcional completada: Ojos más allá de la puerta — las aproximaciones a los caminos vigilados. Canta al camino, y deja un verso para las manos que lo mantuvieron abierto. |
| `scenario.church-of-rome.02-the-price-of-peace.side-5-unavailable` / unique optional entity irrecoverably lost; once | leo-road-singer → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.church-of-rome.02-the-price-of-peace.side-6-brief` / optional objectives tab, always available | leo-road-singer → return-to-game | Pay 50 wood and restore the damaged store of the reception store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el almacén receptor. Ventaja: 200 de alimento, 100 de madera, una vez. |
| `scenario.church-of-rome.02-the-price-of-peace.side-6-completed` / 02-the-price-of-peace.side-6.completed latched; once | leo-road-singer → return-to-game | Optional task completed: Raise the Store Again — the reception store. Sing of the road, and leave a verse for the hands that kept it open. | Tarea opcional completada: Levantar de nuevo el almacén — el almacén receptor. Canta al camino, y deja un verso para las manos que lo mantuvieron abierto. |
| `scenario.church-of-rome.02-the-price-of-peace.side-6-unavailable` / unique optional entity irrecoverably lost; once | leo-road-singer → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |

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
