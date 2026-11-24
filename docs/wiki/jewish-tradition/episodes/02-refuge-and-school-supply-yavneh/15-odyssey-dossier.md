# 2. A School without Walls

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. Historical, geographic, native and game review remain pending; this typed projection is not an implemented map or played route.

CDF-C02 · `02-refuge-and-school-supply-yavneh` · c.70–80 CE · 400×400

## Historical frame and source record

EN: Yavneh, c.70–80 CE. After the Temple’s destruction, later Jewish sources associate Yavneh with legal teaching and remembered changes in practice. They do not give us the plan of an academy.

ES: Yavneh, hacia 70–80 d. C. Tras la destrucción del Templo, fuentes judías posteriores asocian Yavneh con enseñanza legal y cambios recordados en la práctica. No nos ofrecen el plano de una academia.

EN: The three invented local services are complete for their original recipients. This result does not date an academy’s foundation, settle disputed traditions or reverse the destruction of Jerusalem.

ES: Los tres servicios locales inventados están completos para sus destinatarios originales. Este resultado no fecha la fundación de una academia, resuelve tradiciones discutidas ni revierte la destrucción de Jerusalén.

EN: All local workers, recipients, supplies, records, rooms and errands are invented. No rabbinic autograph, exact academy parcel, contemporary negotiation or canon-closing event is represented. Judith’s account is fictional received memory; gameplay neither proves belief nor reverses Jerusalem’s destruction.

ES: Todos los trabajadores, destinatarios, suministros, anotaciones, estancias y encargos locales son inventados. No se representan un autógrafo rabínico, una parcela exacta de academia, una negociación contemporánea ni un cierre del canon. El relato de Judith es memoria recibida ficticia; el juego no acredita creencias ni revierte la destrucción de Jerusalén.

```json
{
  "sourcePassages": [
    {
      "corpusEventId": 63,
      "sourceUrl": "https://www.jewishvirtuallibrary.org/yavneh",
      "passage": "Fuentes rabínicas compiladas después; overview",
      "qualification": "No presentar como concilio que cerró canon o expulsó cristianos.",
      "candidateEvent": "Yohanan ben Zakkai y estudiosos se asocian con actividad rabínica en Yavneh.",
      "approval": "research source checked with qualifications; architect dossier and independent approval pending",
      "researchAudit": {
        "eventId": 63,
        "campaigns": [
          "jewish-tradition"
        ],
        "originalUrl": "https://www.jewishvirtuallibrary.org/yavneh",
        "correctUrlConsulted": "https://cojs.org/tannaitic_literature_-circa_70-3rd_century_ce/",
        "passage": "COJS, Tannaitic Literature, lines 23–30: after temple destruction tannaitic activity is associated with Yavneh, Usha, Beth Shearim, Sepphoris; later tradition ties Akiva to Yavneh.",
        "supportedClaim": "Según el resumen/localizador actualmente atribuido en corpus: Yohanan ben Zakkai y estudiosos se asocian con actividad rabínica en Yavneh.",
        "problems": "The source supports Yavneh as one center of post-destruction transmission, not a dated 70–80 meeting/academy narrative for named Yohanan ben Zakkai. The original Jewish Virtual Library page consulted is an Encyclopaedia Judaica-derived town entry and does not document the academy claim. Avoid implying a formal academy’s exact founding/date.",
        "coverageRead": "COJS extract lines 19–30 read; JVL Yavneh entry lines 23–30 read. Neither full book nor underlying rabbinic sources read.",
        "auditStatus": "reviewed_with_correction_or_caveat"
      }
    }
  ],
  "knowledgeBasis": {
    "speaker": "judith-copyist",
    "mode": "inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports",
    "noOmniscience": true
  }
}
```

## Shared objective and typed profile

### attend-neighbors-table / phase-1

EN: Bring the original provisions recipient alive to the Neighbors’ Table. This records attendance only. It does not pay for, produce or complete any selected service. That recipient must be present there again at the final confirmation.

ES: Lleva al destinatario original de provisiones con vida hasta la mesa de los vecinos. Esto registra únicamente su asistencia. No paga, produce ni completa ningún servicio elegido. Ese destinatario deberá estar presente allí de nuevo en la confirmación final.

```json
{
  "operator": "all",
  "operation": "attend-neighbors-table",
  "requiredCount": 1,
  "defeatBelowRemaining": null,
  "resourceAmounts": {},
  "phaseGated": true,
  "neverUseTimerInstead": true,
  "requirements": [
    {
      "id": "provisions-arrival",
      "kind": "entity-state",
      "state": "arrived",
      "entities": [
        "jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-provisions"
      ],
      "requiredCount": 1,
      "oncePerEntity": true,
      "destinations": {
        "jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-provisions": "jewish-tradition.02-refuge-and-school-supply-yavneh.meal-court.zone"
      }
    },
    {
      "id": "provisions-current",
      "kind": "current-entity-presence",
      "entities": [
        "jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-provisions"
      ],
      "destinations": {
        "jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-provisions": "jewish-tradition.02-refuge-and-school-supply-yavneh.meal-court.zone"
      },
      "requiredCount": 1
    }
  ],
  "requiredLedgers": [
    "provisions-arrival",
    "provisions-current"
  ],
  "allRequired": true
}
```

## Alternative services

A selection is one authored recipe per service. Costs are alternatives and are never lowered to simultaneous fixed-payment predicates.

### provisions

Goal screen: `main-provisions` · completion screen: `service-complete`

#### local-meal — At the Local Hearth

EN: At the Local Hearth

ES: En el fogón local

Work point `hearth-work` → reception point `meal-court`; worker `jewish-tradition.02-refuge-and-school-supply-yavneh.worker-provisions`; output `jewish-tradition.02-refuge-and-school-supply-yavneh.output-local-meal`; recipients: `jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-provisions`.

Cost: `{"food": 120, "gold": 0, "stone": 0, "wood": 20}`.

#### purchased-consignment — The Western Consignment

EN: The Western Consignment

ES: La remesa occidental

Work point `merchant-work` → reception point `meal-court`; worker `jewish-tradition.02-refuge-and-school-supply-yavneh.worker-provisions`; output `jewish-tradition.02-refuge-and-school-supply-yavneh.output-purchased-consignment`; recipients: `jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-provisions`.

Cost: `{"food": 30, "gold": 70, "stone": 0, "wood": 0}`.

### meeting

Goal screen: `main-meeting` · completion screen: `service-complete`

#### assembled-shelter — A Shelter Prepared Together

EN: A Shelter Prepared Together

ES: Un refugio preparado entre todos

Work point `timber-work` → reception point `built-meeting-court`; worker `jewish-tradition.02-refuge-and-school-supply-yavneh.worker-meeting`; output `jewish-tradition.02-refuge-and-school-supply-yavneh.output-assembled-shelter`; recipients: `jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-meeting`.

Cost: `{"food": 20, "gold": 0, "stone": 0, "wood": 100}`.

#### offered-room — The Door Offered Freely

EN: The Door Offered Freely

ES: La puerta que se ofrece

Work point `host-work` → reception point `host-meeting-court`; worker `jewish-tradition.02-refuge-and-school-supply-yavneh.worker-meeting`; output `jewish-tradition.02-refuge-and-school-supply-yavneh.output-offered-room`; recipients: `jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-meeting`.

Cost: `{"food": 0, "gold": 70, "stone": 0, "wood": 20}`.

### materials

Goal screen: `main-materials` · completion screen: `service-complete`

#### local-working-materials — Materials Put to Use

EN: Materials Put to Use

ES: Materiales que sirven

Work point `materials-work` → reception point `reader-court`; worker `jewish-tradition.02-refuge-and-school-supply-yavneh.worker-materials`; output `jewish-tradition.02-refuge-and-school-supply-yavneh.output-local-working-materials`; recipients: `jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-materials`.

Cost: `{"food": 20, "gold": 0, "stone": 0, "wood": 40}`.

#### purchased-working-materials — The Prepared Bundle

EN: The Prepared Bundle

ES: El fardo preparado

Work point `merchant-work` → reception point `reader-court`; worker `jewish-tradition.02-refuge-and-school-supply-yavneh.worker-materials`; output `jewish-tradition.02-refuge-and-school-supply-yavneh.output-purchased-working-materials`; recipients: `jewish-tradition.02-refuge-and-school-supply-yavneh.recipient-materials`.

Cost: `{"food": 0, "gold": 60, "stone": 0, "wood": 10}`.

## Difficulty accounting

Finite selection arithmetic only; it is not resource gathering, a schedule or a playthrough.

### easy

Accounts:

```json
{
  "spendable": {
    "food": 180,
    "wood": 180,
    "gold": 210,
    "stone": 0
  },
  "protectedRecovery": {
    "food": 0,
    "wood": 0,
    "gold": 0,
    "stone": 0
  },
  "optionalReserve": {
    "food": 70,
    "wood": 60,
    "gold": 30,
    "stone": 0
  }
}
```

Before main funding: 128 of 128 optional subsets are reachable from initial spendable stock; all optional tasks are reachable in that prefix: True. This prefix does not include a service selection.

After main funding: 8 of 8 recipe selections are affordable from initial spendable stock; 8 affordable selections permit all optional tasks in an affordable prefix. Unaffordable selections have no after-funding witness. These are finite accounting cases and assume spatial predicates and actor availability succeed.

| Recipe selection | Total cost | Main affordable | Spendable stock after main selection | Reachable optional subsets after funding | All optional tasks affordable after funding |
|---|---|---:|---|---:|---|
| `local-meal`, `assembled-shelter`, `local-working-materials` | `{"food": 160, "gold": 0, "stone": 0, "wood": 160}` | True | `{"food": 20, "gold": 210, "stone": 0, "wood": 20}` | 96 | True |
| `local-meal`, `assembled-shelter`, `purchased-working-materials` | `{"food": 140, "gold": 60, "stone": 0, "wood": 130}` | True | `{"food": 40, "gold": 150, "stone": 0, "wood": 50}` | 128 | True |
| `local-meal`, `offered-room`, `local-working-materials` | `{"food": 140, "gold": 70, "stone": 0, "wood": 80}` | True | `{"food": 40, "gold": 140, "stone": 0, "wood": 100}` | 128 | True |
| `local-meal`, `offered-room`, `purchased-working-materials` | `{"food": 120, "gold": 130, "stone": 0, "wood": 50}` | True | `{"food": 60, "gold": 80, "stone": 0, "wood": 130}` | 128 | True |
| `purchased-consignment`, `assembled-shelter`, `local-working-materials` | `{"food": 70, "gold": 70, "stone": 0, "wood": 140}` | True | `{"food": 110, "gold": 140, "stone": 0, "wood": 40}` | 128 | True |
| `purchased-consignment`, `assembled-shelter`, `purchased-working-materials` | `{"food": 50, "gold": 130, "stone": 0, "wood": 110}` | True | `{"food": 130, "gold": 80, "stone": 0, "wood": 70}` | 128 | True |
| `purchased-consignment`, `offered-room`, `local-working-materials` | `{"food": 50, "gold": 140, "stone": 0, "wood": 60}` | True | `{"food": 130, "gold": 70, "stone": 0, "wood": 120}` | 128 | True |
| `purchased-consignment`, `offered-room`, `purchased-working-materials` | `{"food": 30, "gold": 200, "stone": 0, "wood": 30}` | True | `{"food": 150, "gold": 10, "stone": 0, "wood": 150}` | 96 | True |

### standard

Accounts:

```json
{
  "spendable": {
    "food": 150,
    "wood": 130,
    "gold": 140,
    "stone": 0
  },
  "protectedRecovery": {
    "food": 0,
    "wood": 0,
    "gold": 0,
    "stone": 0
  },
  "optionalReserve": {
    "food": 70,
    "wood": 60,
    "gold": 30,
    "stone": 0
  }
}
```

Before main funding: 128 of 128 optional subsets are reachable from initial spendable stock; all optional tasks are reachable in that prefix: True. This prefix does not include a service selection.

After main funding: 5 of 8 recipe selections are affordable from initial spendable stock; 5 affordable selections permit all optional tasks in an affordable prefix. Unaffordable selections have no after-funding witness. These are finite accounting cases and assume spatial predicates and actor availability succeed.

| Recipe selection | Total cost | Main affordable | Spendable stock after main selection | Reachable optional subsets after funding | All optional tasks affordable after funding |
|---|---|---:|---|---:|---|
| `local-meal`, `assembled-shelter`, `local-working-materials` | `{"food": 160, "gold": 0, "stone": 0, "wood": 160}` | False | `—` | — | — |
| `local-meal`, `assembled-shelter`, `purchased-working-materials` | `{"food": 140, "gold": 60, "stone": 0, "wood": 130}` | True | `{"food": 10, "gold": 80, "stone": 0, "wood": 0}` | 88 | True |
| `local-meal`, `offered-room`, `local-working-materials` | `{"food": 140, "gold": 70, "stone": 0, "wood": 80}` | True | `{"food": 10, "gold": 70, "stone": 0, "wood": 50}` | 112 | True |
| `local-meal`, `offered-room`, `purchased-working-materials` | `{"food": 120, "gold": 130, "stone": 0, "wood": 50}` | True | `{"food": 30, "gold": 10, "stone": 0, "wood": 80}` | 96 | True |
| `purchased-consignment`, `assembled-shelter`, `local-working-materials` | `{"food": 70, "gold": 70, "stone": 0, "wood": 140}` | False | `—` | — | — |
| `purchased-consignment`, `assembled-shelter`, `purchased-working-materials` | `{"food": 50, "gold": 130, "stone": 0, "wood": 110}` | True | `{"food": 100, "gold": 10, "stone": 0, "wood": 20}` | 80 | True |
| `purchased-consignment`, `offered-room`, `local-working-materials` | `{"food": 50, "gold": 140, "stone": 0, "wood": 60}` | True | `{"food": 100, "gold": 0, "stone": 0, "wood": 70}` | 96 | True |
| `purchased-consignment`, `offered-room`, `purchased-working-materials` | `{"food": 30, "gold": 200, "stone": 0, "wood": 30}` | False | `—` | — | — |

### hard

Accounts:

```json
{
  "spendable": {
    "food": 130,
    "wood": 110,
    "gold": 140,
    "stone": 0
  },
  "protectedRecovery": {
    "food": 0,
    "wood": 0,
    "gold": 0,
    "stone": 0
  },
  "optionalReserve": {
    "food": 70,
    "wood": 60,
    "gold": 30,
    "stone": 0
  }
}
```

Before main funding: 128 of 128 optional subsets are reachable from initial spendable stock; all optional tasks are reachable in that prefix: True. This prefix does not include a service selection.

After main funding: 3 of 8 recipe selections are affordable from initial spendable stock; 3 affordable selections permit all optional tasks in an affordable prefix. Unaffordable selections have no after-funding witness. These are finite accounting cases and assume spatial predicates and actor availability succeed.

| Recipe selection | Total cost | Main affordable | Spendable stock after main selection | Reachable optional subsets after funding | All optional tasks affordable after funding |
|---|---|---:|---|---:|---|
| `local-meal`, `assembled-shelter`, `local-working-materials` | `{"food": 160, "gold": 0, "stone": 0, "wood": 160}` | False | `—` | — | — |
| `local-meal`, `assembled-shelter`, `purchased-working-materials` | `{"food": 140, "gold": 60, "stone": 0, "wood": 130}` | False | `—` | — | — |
| `local-meal`, `offered-room`, `local-working-materials` | `{"food": 140, "gold": 70, "stone": 0, "wood": 80}` | False | `—` | — | — |
| `local-meal`, `offered-room`, `purchased-working-materials` | `{"food": 120, "gold": 130, "stone": 0, "wood": 50}` | True | `{"food": 10, "gold": 10, "stone": 0, "wood": 60}` | 80 | True |
| `purchased-consignment`, `assembled-shelter`, `local-working-materials` | `{"food": 70, "gold": 70, "stone": 0, "wood": 140}` | False | `—` | — | — |
| `purchased-consignment`, `assembled-shelter`, `purchased-working-materials` | `{"food": 50, "gold": 130, "stone": 0, "wood": 110}` | True | `{"food": 80, "gold": 10, "stone": 0, "wood": 0}` | 80 | True |
| `purchased-consignment`, `offered-room`, `local-working-materials` | `{"food": 50, "gold": 140, "stone": 0, "wood": 60}` | True | `{"food": 80, "gold": 0, "stone": 0, "wood": 50}` | 96 | True |
| `purchased-consignment`, `offered-room`, `purchased-working-materials` | `{"food": 30, "gold": 200, "stone": 0, "wood": 30}` | False | `—` | — | — |

## Optional objectives

The exact authored v3 contracts follow; their presence does not establish task reachability in the game.

```json
[
  {
    "id": "side-1",
    "kind": "aid",
    "title": {
      "en": "A Share for the Northern Hearth",
      "es-ES": "Una parte para el fogón del norte"
    },
    "subject": {
      "en": "The Northern Household",
      "es-ES": "El hogar del norte"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Independent fictional voluntary local task; fixed original identities and actual authored pickup/destination, never a historical person or authentic ancient record.",
      "es-ES": "Tarea local voluntaria ficticia e independiente; identidades originales fijas y origen/destino escritos, sin representar a una persona histórica ni un documento antiguo auténtico."
    },
    "text": {
      "en": "Bring both marked original aid carriers to their distinct assigned northern household collection circles. Reward once:40 food,40 wood,20 gold, drawn from the separate finite reserve.",
      "es-ES": "Lleva los dos portadores originales señalados de ayuda a sus respectivos círculos de recogida del hogar del norte. Recompensa única:40 de alimento,40 de madera y 20 de oro, de la reserva finita separada."
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
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.entity-1",
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.entity-2"
          ],
          "destinations": {
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.entity-1": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.zone-1",
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.entity-2": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.zone-2"
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
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.entity-1",
          "role": "aid",
          "initialHub": "aid-pickup",
          "offsetTiles": [
            -4,
            -5
          ],
          "identity": "Fictional stable optional identity: jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.entity-1; invented ordinary civilian or cargo carrier; native type still to bind",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        },
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.entity-2",
          "role": "aid",
          "initialHub": "aid-pickup",
          "offsetTiles": [
            4,
            -5
          ],
          "identity": "Fictional stable optional identity: jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.entity-2; invented ordinary civilian or cargo carrier; native type still to bind",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.zone-1",
          "hub": "aid-court",
          "offsetTiles": [
            -8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        },
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.zone-2",
          "hub": "aid-court",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "finite-supply-withdrawal",
        "target": "optional supply stock",
        "resources": {
          "food": 40,
          "wood": 40,
          "gold": 20
        },
        "onceFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false
      }
    ],
    "completionFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-1.completed",
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
    "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart. loss of its own original or irreversible invalidation marks this optional unavailable only; no main defeat, reward, replacement or reserve withdrawal",
    "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
    "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
    "reachability": {
      "originHub": "aid-pickup",
      "receivingHub": "aid-court",
      "corridorIds": [
        "path-aid-pickup-to-northern-junction",
        "path-repair-yard-to-northern-junction",
        "path-aid-court-to-repair-yard"
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
    "kind": "copy",
    "title": {
      "en": "The Room Left in the Margin",
      "es-ES": "El sitio que queda en el margen"
    },
    "subject": {
      "en": "The Reading Cloth",
      "es-ES": "El paño de lectura"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Independent fictional voluntary local task; fixed original identities and actual authored pickup/destination, never a historical person or authentic ancient record.",
      "es-ES": "Tarea local voluntaria ficticia e independiente; identidades originales fijas y origen/destino escritos, sin representar a una persona histórica ni un documento antiguo auténtico."
    },
    "text": {
      "en": "Bring the marked original western working-record carrier to the Reading Cloth. Benefit: an attributed note on remembered practice and the selected-court reminder. No resource reward.",
      "es-ES": "Lleva al portador original señalado de la anotación occidental al paño de lectura. Ventaja: una nota atribuida sobre prácticas recordadas y el recordatorio de patios seleccionados. Sin recompensa de recursos."
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
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-2.entity-1"
          ],
          "destinations": {
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-2.entity-1": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-2.zone-1"
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
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-2.entity-1",
          "role": "copy",
          "initialHub": "record-west",
          "offsetTiles": [
            0,
            -5
          ],
          "identity": "Fictional stable optional identity: jewish-tradition.02-refuge-and-school-supply-yavneh.side-2.entity-1; invented ordinary civilian or cargo carrier; native type still to bind",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-2.zone-1",
          "hub": "reader-court",
          "offsetTiles": [
            0,
            8
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "unlock-context-and-hint",
        "target": "attributed source note and selected-court reminder",
        "resources": {},
        "onceFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-2.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false,
        "sourceIds": [
          "odyssey-source.jewish-tradition.02-refuge-and-school-supply-yavneh"
        ],
        "historicalNote": {
          "en": "Mishnah Rosh Hashanah 4:1–3 preserves post-destruction rules and disagreement about their scope. This later compiled legal memory is not a transcript of our fictional gathering.",
          "es-ES": "Mishná Rosh Hashaná4:1–3 conserva normas posteriores a la destrucción y desacuerdos sobre su alcance. Esta memoria legal compilada después no es una transcripción de nuestra reunión ficticia."
        },
        "hint": {
          "en": "Provisions go to the Neighbors’ Table; working materials go to the Reading Cloth. For A Shelter Prepared Together, use the Prepared Meeting Court. For The Door Offered Freely, use the Offered Room. The selected results and original recipients must still be present at the end.",
          "es-ES": "Las provisiones van a la mesa de los vecinos; los materiales, al paño de lectura. Para Un refugio preparado entre todos, usa el patio preparado para reunirse. Para La puerta que se ofrece, usa la estancia ofrecida. Los resultados seleccionados y destinatarios originales deben seguir presentes al terminar."
        }
      }
    ],
    "completionFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-2.completed",
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
    "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart. Loss of the western original record-west-carrier or irreversible invalidation marks this optional unavailable only; no main defeat, reward, replacement or reserve withdrawal.",
    "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
    "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
    "reachability": {
      "originHub": "record-west",
      "receivingHub": "reader-court",
      "corridorIds": [
        "path-record-west-to-merchant-work",
        "path-merchant-work-to-western-junction",
        "path-timber-work-to-western-junction",
        "path-built-meeting-court-to-timber-work",
        "path-reader-court-to-built-meeting-court"
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
    "kind": "copy",
    "title": {
      "en": "A Tale Carried Further",
      "es-ES": "Un relato que sigue su camino"
    },
    "subject": {
      "en": "The Reading Cloth",
      "es-ES": "El paño de lectura"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Independent fictional voluntary local task; fixed original identities and actual authored pickup/destination, never a historical person or authentic ancient record.",
      "es-ES": "Tarea local voluntaria ficticia e independiente; identidades originales fijas y origen/destino escritos, sin representar a una persona histórica ni un documento antiguo auténtico."
    },
    "text": {
      "en": "Bring the marked original northern working-record carrier to the Reading Cloth. Benefit: an attributed later-tradition note and a reminder that originals cannot be replaced. This task is independent of the western note and gives no resources.",
      "es-ES": "Lleva al portador original señalado de la anotación del norte al paño de lectura. Ventaja: una nota atribuida de tradición posterior y un recordatorio de que los originales no se sustituyen. Esta tarea es independiente de la anotación occidental y no da recursos."
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
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-3.entity-1"
          ],
          "destinations": {
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-3.entity-1": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-3.zone-1"
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
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-3.entity-1",
          "role": "copy",
          "initialHub": "record-north",
          "offsetTiles": [
            0,
            -5
          ],
          "identity": "Fictional stable optional identity: jewish-tradition.02-refuge-and-school-supply-yavneh.side-3.entity-1; invented ordinary civilian or cargo carrier; native type still to bind",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-3.zone-1",
          "hub": "reader-court",
          "offsetTiles": [
            0,
            8
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "unlock-context-and-hint",
        "target": "attributed source note and selected-court reminder",
        "resources": {},
        "onceFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-3.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false,
        "sourceIds": [
          "odyssey-source.jewish-tradition.02-refuge-and-school-supply-yavneh"
        ],
        "historicalNote": {
          "en": "The later Gittin 56a–b narrative associates Yavneh with a request during the siege; it is not a contemporary transcript. Our working record and carrier are fictional. A spare carrier cannot replace this original, or the original assigned to the separate western note.",
          "es-ES": "El relato posterior de Guitín 56a–b asocia Yavneh con una petición durante el asedio; no es una transcripción contemporánea. Nuestra anotación de trabajo y su portador son ficticios. Un portador de repuesto no sustituye a este original ni al asignado a la anotación occidental independiente."
        },
        "hint": {
          "en": "A spare carrier cannot replace this original, or the original assigned to the separate western note.",
          "es-ES": "Un portador de repuesto no sustituye a este original ni al asignado a la anotación occidental independiente."
        }
      }
    ],
    "completionFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-3.completed",
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
    "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart. Loss of the northern original record-north-carrier or irreversible invalidation marks this optional unavailable only; no main defeat, reward, replacement or reserve withdrawal.",
    "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
    "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
    "reachability": {
      "originHub": "record-north",
      "receivingHub": "reader-court",
      "corridorIds": [
        "path-northern-junction-to-record-north",
        "path-northern-junction-to-timber-work",
        "path-built-meeting-court-to-timber-work",
        "path-reader-court-to-built-meeting-court"
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
    "kind": "repair",
    "title": {
      "en": "A Roof for What Remains",
      "es-ES": "Un techo para lo que queda"
    },
    "subject": {
      "en": "The Damaged Store",
      "es-ES": "El almacén dañado"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Independent fictional voluntary local task; fixed original identities and actual authored pickup/destination, never a historical person or authentic ancient record.",
      "es-ES": "Tarea local voluntaria ficticia e independiente; identidades originales fijas y origen/destino escritos, sin representar a una persona histórica ni un documento antiguo auténtico."
    },
    "text": {
      "en": "Use the damaged store’s single repair action: pay 30 wood to restore that original store fully, then receive 20 wood once from reserve. Paying without restoration gives no reward.",
      "es-ES": "Usa la acción única de reparación del almacén dañado: paga 30 de madera para restaurar por completo ese almacén original y recibe después 20 de madera de la reserva una sola vez. Pagar sin restaurarlo no da recompensa."
    },
    "mandatory": false,
    "activation": "available from scenario start; known requirement and benefit shown in optional goals",
    "dependencies": [],
    "predicate": {
      "operator": "all",
      "requirements": [
        {
          "kind": "entity-health",
          "entity": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-4.entity-1",
          "health": "full",
          "paymentReceipt": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-4.payment",
          "restoration": "atomic authored-cost repair transaction restores full health; no additional engine repair charge"
        },
        {
          "kind": "atomic-payment",
          "resources": {
            "wood": 30
          },
          "receipt": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-4.payment",
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
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-4.entity-1",
          "role": "repair",
          "initialHub": "repair-yard",
          "offsetTiles": [
            6,
            0
          ],
          "identity": "Fictional stable optional identity: jewish-tradition.02-refuge-and-school-supply-yavneh.side-4.entity-1; invented ordinary store; native footprint/health action still to bind",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed restoration, payment or delivery.",
          "playerControllable": false,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-4.zone-1",
          "hub": "repair-yard",
          "offsetTiles": [
            0,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "finite-supply-withdrawal",
        "target": "optional supply stock",
        "resources": {
          "wood": 20
        },
        "onceFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-4.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false
      }
    ],
    "completionFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-4.completed",
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
    "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart. loss of its own original or irreversible invalidation marks this optional unavailable only; no main defeat, reward, replacement or reserve withdrawal",
    "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
    "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
    "reachability": {
      "originHub": "repair-yard",
      "receivingHub": "repair-yard",
      "corridorIds": [
        "path-starting-court-to-hearth-work",
        "path-hearth-work-to-meal-court",
        "path-meal-court-to-reader-court",
        "path-reader-court-to-built-meeting-court",
        "path-aid-court-to-built-meeting-court",
        "path-aid-court-to-repair-yard"
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
    "kind": "trade",
    "title": {
      "en": "A Fair Exchange at the Southern Yard",
      "es-ES": "Un intercambio justo en el patio del sur"
    },
    "subject": {
      "en": "The Southern Receiving Yard",
      "es-ES": "El patio receptor del sur"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Independent fictional voluntary local task; fixed original identities and actual authored pickup/destination, never a historical person or authentic ancient record.",
      "es-ES": "Tarea local voluntaria ficticia e independiente; identidades originales fijas y origen/destino escritos, sin representar a una persona histórica ni un documento antiguo auténtico."
    },
    "text": {
      "en": "Escort the marked original trader to the southern receiving yard. Pay 20 gold there, then receive 20 food and 10 gold once from reserve. Its own reward cannot pay its cost.",
      "es-ES": "Escolta al comerciante original señalado hasta el patio receptor del sur. Paga allí20 de oro y recibe después 20 de alimento y 10 de oro de la reserva una sola vez. Su propia recompensa no puede pagar su coste."
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
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-5.entity-1"
          ],
          "destinations": {
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-5.entity-1": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-5.zone-1"
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
            "gold": 20
          },
          "receipt": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-5.payment",
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
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-5.entity-1",
          "role": "trade",
          "initialHub": "trade-pickup",
          "offsetTiles": [
            0,
            -5
          ],
          "identity": "Fictional stable optional identity: jewish-tradition.02-refuge-and-school-supply-yavneh.side-5.entity-1; invented ordinary civilian or cargo carrier; native type still to bind",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-5.zone-1",
          "hub": "trade-court",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "finite-supply-withdrawal",
        "target": "optional supply stock",
        "resources": {
          "food": 20,
          "gold": 10
        },
        "onceFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-5.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false
      }
    ],
    "completionFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-5.completed",
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
    "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart. loss of its own original or irreversible invalidation marks this optional unavailable only; no main defeat, reward, replacement or reserve withdrawal",
    "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
    "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
    "reachability": {
      "originHub": "trade-pickup",
      "receivingHub": "trade-court",
      "corridorIds": [
        "path-merchant-work-to-trade-pickup",
        "path-merchant-work-to-western-junction",
        "path-western-junction-to-starting-court",
        "path-starting-court-to-host-work",
        "path-host-work-to-host-meeting-court",
        "path-host-meeting-court-to-trade-court"
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
    "kind": "guide",
    "title": {
      "en": "The Turn We Had Overlooked",
      "es-ES": "El recodo que no habíamos visto"
    },
    "subject": {
      "en": "The Western Junction",
      "es-ES": "El cruce occidental"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Independent fictional voluntary local task; fixed original identities and actual authored pickup/destination, never a historical person or authentic ancient record.",
      "es-ES": "Tarea local voluntaria ficticia e independiente; identidades originales fijas y origen/destino escritos, sin representar a una persona histórica ni un documento antiguo auténtico."
    },
    "text": {
      "en": "Bring the original local guide to the western junction. Benefit: mark the existing northern approach through the Timber Bench to the Northern Turn. The task creates no road or change in terrain.",
      "es-ES": "Lleva al guía local original al cruce occidental. Ventaja: señala la aproximación norte existente por el banco de madera hasta el recodo del norte. La tarea no crea un camino ni cambia el terreno."
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
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-6.entity-1"
          ],
          "destinations": {
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-6.entity-1": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-6.zone-1"
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
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-6.entity-1",
          "role": "guide",
          "initialHub": "guide-pickup",
          "offsetTiles": [
            0,
            -5
          ],
          "identity": "Fictional stable optional identity: jewish-tradition.02-refuge-and-school-supply-yavneh.side-6.entity-1; invented ordinary civilian or cargo carrier; native type still to bind",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-6.zone-1",
          "hub": "western-junction",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "mark-alternative-route",
        "target": "existing northern approach through the Timber Bench to the Northern Turn",
        "resources": {},
        "onceFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-6.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false,
        "corridorId": "northern-approach"
      }
    ],
    "completionFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-6.completed",
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
    "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart. loss of its own original or irreversible invalidation marks this optional unavailable only; no main defeat, reward, replacement or reserve withdrawal",
    "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
    "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
    "reachability": {
      "originHub": "guide-pickup",
      "receivingHub": "western-junction",
      "corridorIds": [
        "path-guide-pickup-to-record-west",
        "path-record-west-to-merchant-work",
        "path-merchant-work-to-western-junction"
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
    "id": "side-7",
    "kind": "extract",
    "title": {
      "en": "Room at Another Hearth",
      "es-ES": "Sitio junto a otro fogón"
    },
    "subject": {
      "en": "The Additional Hearth",
      "es-ES": "El fogón adicional"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Independent fictional voluntary local task; fixed original identities and actual authored pickup/destination, never a historical person or authentic ancient record.",
      "es-ES": "Tarea local voluntaria ficticia e independiente; identidades originales fijas y origen/destino escritos, sin representar a una persona histórica ni un documento antiguo auténtico."
    },
    "text": {
      "en": "Bring both marked original voluntary guests to the additional hearth alive. Pay 20 food for hospitality, then receive 10 food once from reserve. These guests are optional and cannot replace a main recipient.",
      "es-ES": "Lleva con vida a los dos invitados voluntarios originales señalados hasta el fogón adicional. Paga 20 de alimento por la hospitalidad y recibe después 10 de alimento de la reserva una sola vez. Estos invitados son opcionales y no sustituyen a ningún destinatario principal."
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
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.entity-1",
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.entity-2"
          ],
          "destinations": {
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.entity-1": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.zone-1",
            "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.entity-2": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.zone-1"
          },
          "requiredCount": 2,
          "aliveAtDelivery": true,
          "oncePerEntity": true,
          "noSubstitutes": true,
          "initialPlacementDoesNotCount": true
        },
        {
          "kind": "atomic-payment",
          "resources": {
            "food": 20
          },
          "receipt": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.payment",
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
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.entity-1",
          "role": "extract",
          "initialHub": "guest-pickup",
          "offsetTiles": [
            -4,
            -5
          ],
          "identity": "Fictional stable optional identity: jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.entity-1; invented ordinary civilian or cargo carrier; native type still to bind",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        },
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.entity-2",
          "role": "extract",
          "initialHub": "guest-pickup",
          "offsetTiles": [
            4,
            -5
          ],
          "identity": "Fictional stable optional identity: jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.entity-2; invented ordinary civilian or cargo carrier; native type still to bind",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.zone-1",
          "hub": "guest-court",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "finite-supply-withdrawal",
        "target": "optional supply stock",
        "resources": {
          "food": 10
        },
        "onceFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false
      }
    ],
    "completionFlag": "jewish-tradition.02-refuge-and-school-supply-yavneh.side-7.completed",
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
    "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart. loss of its own original or irreversible invalidation marks this optional unavailable only; no main defeat, reward, replacement or reserve withdrawal",
    "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
    "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
    "reachability": {
      "originHub": "guest-pickup",
      "receivingHub": "guest-court",
      "corridorIds": [
        "path-record-north-to-guest-pickup",
        "path-northern-junction-to-record-north",
        "path-northern-junction-to-timber-work",
        "path-timber-work-to-western-junction",
        "path-western-junction-to-starting-court",
        "path-starting-court-to-host-work",
        "path-host-work-to-guest-court"
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
]
```

## Geography and map controls

[Proposed map](../../../../design/maps/jewish-tradition/odyssey/02-refuge-and-school-supply-yavneh.svg)

```json
{
  "bbox": [
    34.714,
    31.846,
    34.755,
    31.884
  ],
  "terrainProfile": "yavneh",
  "orientation": "north-up; real inland Yavneh region, fictional local activity sites; no claim to an academy address",
  "projection": "existing geographic_frame.helper.py; cosine-corrected longitude and padded square, north-up",
  "hubs": [
    {
      "id": "starting-court",
      "centre": [
        211.44,
        255.75
      ],
      "lonLat": [
        34.736,
        31.859
      ],
      "name": {
        "en": "The Shared Ledger",
        "es-ES": "El registro compartido"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "hearth-work",
      "centre": [
        235.33,
        237.0
      ],
      "lonLat": [
        34.739,
        31.861
      ],
      "name": {
        "en": "The Local Hearth",
        "es-ES": "El fogón local"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "meal-court",
      "centre": [
        251.25,
        213.56
      ],
      "lonLat": [
        34.741,
        31.8635
      ],
      "name": {
        "en": "The Neighbors’ Table",
        "es-ES": "La mesa de los vecinos"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "timber-work",
      "centre": [
        179.59,
        185.44
      ],
      "lonLat": [
        34.732,
        31.8665
      ],
      "name": {
        "en": "The Timber Bench",
        "es-ES": "El banco de madera"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "built-meeting-court",
      "centre": [
        227.37,
        162.0
      ],
      "lonLat": [
        34.738,
        31.869
      ],
      "name": {
        "en": "The Prepared Meeting Court",
        "es-ES": "El patio preparado para reunirse"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "host-work",
      "centre": [
        163.67,
        293.25
      ],
      "lonLat": [
        34.73,
        31.855
      ],
      "name": {
        "en": "The Host’s Preparation Yard",
        "es-ES": "El patio de preparación del anfitrión"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "host-meeting-court",
      "centre": [
        187.56,
        312.0
      ],
      "lonLat": [
        34.733,
        31.853
      ],
      "name": {
        "en": "The Offered Room",
        "es-ES": "La estancia ofrecida"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "materials-work",
      "centre": [
        251.25,
        265.13
      ],
      "lonLat": [
        34.741,
        31.858
      ],
      "name": {
        "en": "The Local Working Bench",
        "es-ES": "La mesa de trabajo local"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "reader-court",
      "centre": [
        263.2,
        192.94
      ],
      "lonLat": [
        34.7425,
        31.8657
      ],
      "name": {
        "en": "The Reading Cloth",
        "es-ES": "El paño de lectura"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "merchant-work",
      "centre": [
        88.03,
        227.63
      ],
      "lonLat": [
        34.7205,
        31.862
      ],
      "name": {
        "en": "The Western Trader",
        "es-ES": "El comerciante occidental"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "western-junction",
      "centre": [
        131.82,
        227.63
      ],
      "lonLat": [
        34.726,
        31.862
      ],
      "name": {
        "en": "The Western Junction",
        "es-ES": "El cruce occidental"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "northern-junction",
      "centre": [
        171.63,
        143.25
      ],
      "lonLat": [
        34.731,
        31.871
      ],
      "name": {
        "en": "The Northern Turn",
        "es-ES": "El recodo del norte"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "aid-pickup",
      "centre": [
        107.94,
        143.25
      ],
      "lonLat": [
        34.723,
        31.871
      ],
      "name": {
        "en": "The Waiting Aid",
        "es-ES": "La ayuda que espera"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "aid-court",
      "centre": [
        227.37,
        105.75
      ],
      "lonLat": [
        34.738,
        31.875
      ],
      "name": {
        "en": "The Northern Household",
        "es-ES": "El hogar del norte"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "record-west",
      "centre": [
        68.12,
        283.88
      ],
      "lonLat": [
        34.718,
        31.856
      ],
      "name": {
        "en": "The Western Working Record",
        "es-ES": "La anotación de trabajo occidental"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "record-north",
      "centre": [
        131.82,
        68.25
      ],
      "lonLat": [
        34.726,
        31.879
      ],
      "name": {
        "en": "The Northern Working Record",
        "es-ES": "La anotación de trabajo del norte"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "repair-yard",
      "centre": [
        195.52,
        96.38
      ],
      "lonLat": [
        34.734,
        31.876
      ],
      "name": {
        "en": "The Damaged Store",
        "es-ES": "El almacén dañado"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "trade-pickup",
      "centre": [
        56.18,
        171.38
      ],
      "lonLat": [
        34.7165,
        31.868
      ],
      "name": {
        "en": "The Visiting Trader",
        "es-ES": "El comerciante visitante"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "trade-court",
      "centre": [
        211.44,
        340.13
      ],
      "lonLat": [
        34.736,
        31.85
      ],
      "name": {
        "en": "The Southern Receiving Yard",
        "es-ES": "El patio receptor del sur"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "guide-pickup",
      "centre": [
        99.97,
        321.38
      ],
      "lonLat": [
        34.722,
        31.852
      ],
      "name": {
        "en": "The Waiting Guide",
        "es-ES": "El guía que espera"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "guest-pickup",
      "centre": [
        76.09,
        49.5
      ],
      "lonLat": [
        34.719,
        31.881
      ],
      "name": {
        "en": "The Guest Household",
        "es-ES": "El hogar invitado"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    },
    {
      "id": "guest-court",
      "centre": [
        147.75,
        358.88
      ],
      "lonLat": [
        34.728,
        31.848
      ],
      "name": {
        "en": "The Additional Hearth",
        "es-ES": "El fogón adicional"
      },
      "radiusTiles": 12,
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain; radius12 is a proposed gameplay activity envelope, not an ancient parcel"
    }
  ],
  "points": [
    {
      "id": "starting-court",
      "lonLat": [
        34.736,
        31.859
      ],
      "tile": [
        211.44,
        255.75
      ],
      "name": {
        "en": "The Shared Ledger",
        "es-ES": "El registro compartido"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "hearth-work",
      "lonLat": [
        34.739,
        31.861
      ],
      "tile": [
        235.33,
        237.0
      ],
      "name": {
        "en": "The Local Hearth",
        "es-ES": "El fogón local"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "meal-court",
      "lonLat": [
        34.741,
        31.8635
      ],
      "tile": [
        251.25,
        213.56
      ],
      "name": {
        "en": "The Neighbors’ Table",
        "es-ES": "La mesa de los vecinos"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "timber-work",
      "lonLat": [
        34.732,
        31.8665
      ],
      "tile": [
        179.59,
        185.44
      ],
      "name": {
        "en": "The Timber Bench",
        "es-ES": "El banco de madera"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "built-meeting-court",
      "lonLat": [
        34.738,
        31.869
      ],
      "tile": [
        227.37,
        162.0
      ],
      "name": {
        "en": "The Prepared Meeting Court",
        "es-ES": "El patio preparado para reunirse"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "host-work",
      "lonLat": [
        34.73,
        31.855
      ],
      "tile": [
        163.67,
        293.25
      ],
      "name": {
        "en": "The Host’s Preparation Yard",
        "es-ES": "El patio de preparación del anfitrión"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "host-meeting-court",
      "lonLat": [
        34.733,
        31.853
      ],
      "tile": [
        187.56,
        312.0
      ],
      "name": {
        "en": "The Offered Room",
        "es-ES": "La estancia ofrecida"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "materials-work",
      "lonLat": [
        34.741,
        31.858
      ],
      "tile": [
        251.25,
        265.13
      ],
      "name": {
        "en": "The Local Working Bench",
        "es-ES": "La mesa de trabajo local"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "reader-court",
      "lonLat": [
        34.7425,
        31.8657
      ],
      "tile": [
        263.2,
        192.94
      ],
      "name": {
        "en": "The Reading Cloth",
        "es-ES": "El paño de lectura"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "merchant-work",
      "lonLat": [
        34.7205,
        31.862
      ],
      "tile": [
        88.03,
        227.63
      ],
      "name": {
        "en": "The Western Trader",
        "es-ES": "El comerciante occidental"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "western-junction",
      "lonLat": [
        34.726,
        31.862
      ],
      "tile": [
        131.82,
        227.63
      ],
      "name": {
        "en": "The Western Junction",
        "es-ES": "El cruce occidental"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "northern-junction",
      "lonLat": [
        34.731,
        31.871
      ],
      "tile": [
        171.63,
        143.25
      ],
      "name": {
        "en": "The Northern Turn",
        "es-ES": "El recodo del norte"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "aid-pickup",
      "lonLat": [
        34.723,
        31.871
      ],
      "tile": [
        107.94,
        143.25
      ],
      "name": {
        "en": "The Waiting Aid",
        "es-ES": "La ayuda que espera"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "aid-court",
      "lonLat": [
        34.738,
        31.875
      ],
      "tile": [
        227.37,
        105.75
      ],
      "name": {
        "en": "The Northern Household",
        "es-ES": "El hogar del norte"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "record-west",
      "lonLat": [
        34.718,
        31.856
      ],
      "tile": [
        68.12,
        283.88
      ],
      "name": {
        "en": "The Western Working Record",
        "es-ES": "La anotación de trabajo occidental"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "record-north",
      "lonLat": [
        34.726,
        31.879
      ],
      "tile": [
        131.82,
        68.25
      ],
      "name": {
        "en": "The Northern Working Record",
        "es-ES": "La anotación de trabajo del norte"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "repair-yard",
      "lonLat": [
        34.734,
        31.876
      ],
      "tile": [
        195.52,
        96.38
      ],
      "name": {
        "en": "The Damaged Store",
        "es-ES": "El almacén dañado"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "trade-pickup",
      "lonLat": [
        34.7165,
        31.868
      ],
      "tile": [
        56.18,
        171.38
      ],
      "name": {
        "en": "The Visiting Trader",
        "es-ES": "El comerciante visitante"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "trade-court",
      "lonLat": [
        34.736,
        31.85
      ],
      "tile": [
        211.44,
        340.13
      ],
      "name": {
        "en": "The Southern Receiving Yard",
        "es-ES": "El patio receptor del sur"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "guide-pickup",
      "lonLat": [
        34.722,
        31.852
      ],
      "tile": [
        99.97,
        321.38
      ],
      "name": {
        "en": "The Waiting Guide",
        "es-ES": "El guía que espera"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "guest-pickup",
      "lonLat": [
        34.719,
        31.881
      ],
      "tile": [
        76.09,
        49.5
      ],
      "name": {
        "en": "The Guest Household",
        "es-ES": "El hogar invitado"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    },
    {
      "id": "guest-court",
      "lonLat": [
        34.728,
        31.848
      ],
      "tile": [
        147.75,
        358.88
      ],
      "name": {
        "en": "The Additional Hearth",
        "es-ES": "El fogón adicional"
      },
      "certainty": "fictional activity-site candidate; no excavated parcel or approved native terrain"
    }
  ],
  "corridors": [
    {
      "id": "path-starting-court-to-hearth-work",
      "hubOrder": [
        "starting-court",
        "hearth-work"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-hearth-work-to-meal-court",
      "hubOrder": [
        "hearth-work",
        "meal-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-meal-court-to-reader-court",
      "hubOrder": [
        "meal-court",
        "reader-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-reader-court-to-built-meeting-court",
      "hubOrder": [
        "reader-court",
        "built-meeting-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-built-meeting-court-to-timber-work",
      "hubOrder": [
        "built-meeting-court",
        "timber-work"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-timber-work-to-western-junction",
      "hubOrder": [
        "timber-work",
        "western-junction"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-western-junction-to-starting-court",
      "hubOrder": [
        "western-junction",
        "starting-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-starting-court-to-materials-work",
      "hubOrder": [
        "starting-court",
        "materials-work"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-materials-work-to-reader-court",
      "hubOrder": [
        "materials-work",
        "reader-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-starting-court-to-host-work",
      "hubOrder": [
        "starting-court",
        "host-work"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-host-work-to-host-meeting-court",
      "hubOrder": [
        "host-work",
        "host-meeting-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-host-meeting-court-to-trade-court",
      "hubOrder": [
        "host-meeting-court",
        "trade-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-host-work-to-guest-court",
      "hubOrder": [
        "host-work",
        "guest-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-guest-court-to-guide-pickup",
      "hubOrder": [
        "guest-court",
        "guide-pickup"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-guide-pickup-to-record-west",
      "hubOrder": [
        "guide-pickup",
        "record-west"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-record-west-to-merchant-work",
      "hubOrder": [
        "record-west",
        "merchant-work"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-merchant-work-to-western-junction",
      "hubOrder": [
        "merchant-work",
        "western-junction"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-merchant-work-to-trade-pickup",
      "hubOrder": [
        "merchant-work",
        "trade-pickup"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-trade-pickup-to-aid-pickup",
      "hubOrder": [
        "trade-pickup",
        "aid-pickup"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-aid-pickup-to-northern-junction",
      "hubOrder": [
        "aid-pickup",
        "northern-junction"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-northern-junction-to-timber-work",
      "hubOrder": [
        "northern-junction",
        "timber-work"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-northern-junction-to-record-north",
      "hubOrder": [
        "northern-junction",
        "record-north"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-record-north-to-guest-pickup",
      "hubOrder": [
        "record-north",
        "guest-pickup"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-guest-pickup-to-aid-court",
      "hubOrder": [
        "guest-pickup",
        "aid-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-aid-court-to-repair-yard",
      "hubOrder": [
        "aid-court",
        "repair-yard"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-repair-yard-to-northern-junction",
      "hubOrder": [
        "repair-yard",
        "northern-junction"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "path-aid-court-to-built-meeting-court",
      "hubOrder": [
        "aid-court",
        "built-meeting-court"
      ],
      "mode": "land",
      "widthTiles": 4
    },
    {
      "id": "northern-approach",
      "hubOrder": [
        "western-junction",
        "timber-work",
        "northern-junction"
      ],
      "mode": "land",
      "widthTiles": 4
    }
  ],
  "terrainInstructions": "No approved ancient land/elevation/watercourse or native passability. Preserve the27physical links and20documented local approaches, including actual offset circles, only as proposed geometry. The28th corridor is a two-link information alias and creates no road. No modern Soreq course, invented bridge or large flattened courtyard is approved.",
  "geographicLayers": [],
  "geometryStatus": "candidate only; historical land, all full-width paths, footprints, native spawning and gameplay unapproved",
  "asset": "docs/design/maps/jewish-tradition/odyssey/02-refuge-and-school-supply-yavneh.svg",
  "activeAreaPolicy": "22candidate activity areas and their proposed connections; keep native whole-frame geography/density/performance as an acceptance target, never a measured usable-land claim",
  "schematicWaterControl": {
    "coordinates": [],
    "certainty": "first-century course unresolved; empty coordinates do not certify land",
    "renderAs": "unresolved-reference"
  },
  "sourceBindings": {
    "sourceIds": [
      "odyssey-source.jewish-tradition.02-refuge-and-school-supply-yavneh"
    ],
    "citations": [
      {
        "url": "https://hadashot.iaa.org.il/Report_Detail_Eng.aspx?id=25883",
        "passage": "Introduction and figures1–2, Tel Yavne Area A",
        "qualification": "Modern tell/drainage and printed grid extents; no academy parcel or first-century watercourse"
      },
      {
        "url": "https://hadashot.iaa.org.il/Guidelines_eng.aspx",
        "passage": "Map References, New Israel Grid convention",
        "qualification": "CRS identification only; printed map uncertainty remains"
      }
    ]
  }
}
```

## Authored presentation

### title (title)

EN: A School without Walls

ES: Una escuela sin murallas

Condition: campaign menu episode entry, before intro-fact · narrator: none · native surface: pending certified SequenceItems/message adapter.

### intro-fact (factualIntro)

EN: Yavneh, c.70–80 CE. After the Temple’s destruction, later Jewish sources associate Yavneh with legal teaching and remembered changes in practice. They do not give us the plan of an academy.

ES: Yavneh, hacia 70–80 d. C. Tras la destrucción del Templo, fuentes judías posteriores asocian Yavneh con enseñanza legal y cambios recordados en la práctica. No nos ofrecen el plano de una academia.

Condition: after title, before intro-handover · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### intro-handover (handover)

EN: These households, supplies and local errands are invented. Judith of Tiberias speaks centuries later, from received accounts. Their success will not found an institution or settle a canon.

ES: Estos hogares, suministros y encargos locales son inventados. Judith de Tiberíades habla siglos después, a partir de relatos recibidos. Su éxito no fundará una institución ni fijará un canon.

Condition: after intro-fact, before intro-personal · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### intro-personal (personalIntro)

EN: I was taught to leave a margin for the next question. The names of Yavneh reached me through other voices. I cannot recover their rooms; I can refuse to mistake a roof for an answer.

ES: Me enseñaron a dejar margen para la siguiente pregunta. Los nombres de Yavneh me llegaron por otras voces. No puedo recuperar sus habitaciones; puedo negarme a confundir un techo con una respuesta.

Condition: after intro-handover, before any player resource action · narrator: judith-copyist · native surface: pending certified SequenceItems/message adapter.

### recommended-previous (unassigned authored screen)

EN: Recommended first: Names beyond the Fallen House, episode 1 of Keepers of the Unbroken Word. This episode can be played independently. The local characters do not certify a household’s journey from Jerusalem.

ES: Se recomienda empezar por Nombres más allá de la casa caída, episodio 1 de Guardianes de la palabra viva. Este episodio puede jugarse por separado. Los personajes locales no acreditan el viaje de un hogar desde Jerusalén.

Condition: entry recommendation, nonblocking and skippable; never read a missing save as permission · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### plan-preview (unassigned authored screen)

EN: Choose one method for each of three services: provisions, meeting space and working materials. Preview is free. Each method shows its own worker, work site, result, receiving court and original recipient.

ES: Elige un método para cada uno de tres servicios: provisiones, lugar de reunión y materiales de trabajo. Consultar es gratis. Cada método muestra su trabajador, lugar de trabajo, resultado, patio receptor y destinatario original.

Condition: opening plan panel or changing complete candidate selection; free · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### reserve (unassigned authored screen)

EN: Reserve the complete affordable selection once. All three costs enter escrow together. You may cancel and recover that escrow before committing; optional rewards remain separate.

ES: Reserva una vez la selección completa que puedas pagar. Los tres costes pasan juntos a depósito. Puedes cancelar y recuperar ese depósito antes de comprometerte; las recompensas opcionales siguen separadas.

Condition: successful atomic reservation, once per attempt · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### unaffordable (unassigned authored screen)

EN: This complete selection exceeds at least one spendable resource. Nothing has been reserved. Compare another method or complete an available optional task; the displayed reward reserve is not your spending stock.

ES: Esta selección completa supera al menos un recurso disponible. No se ha reservado nada. Compara otro método o cumple un secundario disponible; la reserva de recompensas mostrada no forma parte de tus existencias para gastar.

Condition: rejected unaffordable reservation; no mutation · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### cancel (unassigned authored screen)

EN: Reservation cancelled once. Its escrow has returned to spendable stock. Completed optional tasks and their receipts remain recorded.

ES: Reserva cancelada una vez. Su depósito vuelve a los recursos disponibles. Los secundarios completados y sus recibos siguen registrados.

Condition: successful precommit cancellation; refund once · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### commit (unassigned authored screen)

EN: Begin the selected plan. Its methods and costs are now committed. Take each original worker to the selected work circle, then deliver that method’s resulting bundle to its own receiving court.

ES: Comienza el plan elegido. Sus métodos y costes quedan comprometidos. Lleva cada trabajador original al círculo de trabajo seleccionado y entrega después el fardo resultante de ese método en su propio patio receptor.

Condition: successful irreversible commit; announce selected methods · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### main-provisions (unassigned authored screen)

EN: Complete the selected provisions method. Deliver its own result to the Neighbors’ Table with the original provisions recipient alive and present. Payment alone does not serve a meal.

ES: Completa el método elegido de provisiones. Entrega su propio resultado en la mesa de los vecinos con el destinatario original de provisiones vivo y presente. El pago por sí solo no sirve una comida.

Condition: active main service goal; selected recipe only · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### main-meeting (unassigned authored screen)

EN: Complete the selected meeting method. The original meeting recipient must attend its selected receiving court: the prepared court for A Shelter Prepared Together, or the offered room for The Door Offered Freely.

ES: Completa el método elegido de reunión. El destinatario original de reunión debe acudir al patio receptor seleccionado: el patio preparado para Un refugio preparado entre todos o la estancia ofrecida para La puerta que se ofrece.

Condition: active main service goal; selected recipe only · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### main-materials (unassigned authored screen)

EN: Complete the selected working-materials method. Deliver its own result to the Reading Cloth with the original materials recipient alive and present. These are ordinary working supplies, not a recovered sacred original.

ES: Completa el método elegido de materiales de trabajo. Entrega su propio resultado en el paño de lectura con el destinatario original de materiales vivo y presente. Son suministros corrientes de trabajo, no un original sagrado recuperado.

Condition: active main service goal; selected recipe only · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### service-complete (unassigned authored screen)

EN: One task has a destination now, and someone there to receive it. Leave its name beside its receipt; a total without a name tells too easy a story.

ES: Una tarea ya tiene destino y alguien que la reciba. Deja su nombre junto al recibo; un total sin nombre cuenta una historia demasiado fácil.

Condition: one notification for each service original selected output reception receipt; bind service ID explicitly, maximum3 · narrator: judith-copyist · native surface: pending certified SequenceItems/message adapter.

### aid-offer (unassigned authored screen)

EN: Bring both marked original aid carriers to their distinct assigned northern household collection circles. Reward once:40 food,40 wood,20 gold, drawn from the separate finite reserve.

ES: Lleva los dos portadores originales señalados de ayuda a sus respectivos círculos de recogida del hogar del norte. Recompensa única:40 de alimento,40 de madera y 20 de oro, de la reserva finita separada.

Condition: optional panel from start and reread while nonterminal; exact cost/benefit before acceptance · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### aid-complete (unassigned authored screen)

EN: A share arrived before anyone could turn generosity into a heading. I would leave the recipient’s place in the account.

ES: Llegó una parte antes de que nadie convirtiera la generosidad en un encabezamiento. Yo dejaría sitio para su destinatario en la cuenta.

Condition: after atomic once completion and own reserve debit/reward; bind this optional ID only · narrator: judith-copyist · native surface: pending certified SequenceItems/message adapter.

### copy-offer (unassigned authored screen)

EN: Bring the marked original western working-record carrier to the Reading Cloth. Benefit: an attributed note on remembered practice and the selected-court reminder. No resource reward.

ES: Lleva al portador original señalado de la anotación occidental al paño de lectura. Ventaja: una nota atribuida sobre prácticas recordadas y el recordatorio de patios seleccionados. Sin recompensa de recursos.

Condition: side-2 western original copy offer, independent from side-3 · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### copy-hint (unassigned authored screen)

EN: Provisions go to the Neighbors’ Table; working materials go to the Reading Cloth. For A Shelter Prepared Together, use the Prepared Meeting Court. For The Door Offered Freely, use the Offered Room. The selected results and original recipients must still be present at the end.

ES: Las provisiones van a la mesa de los vecinos; los materiales, al paño de lectura. Para Un refugio preparado entre todos, usa el patio preparado para reunirse. Para La puerta que se ofrece, usa la estancia ofrecida. Los resultados seleccionados y destinatarios originales deben seguir presentes al terminar.

Condition: after side-2 copy-complete once; independent from side-3 · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### copy-complete (unassigned authored screen)

EN: Mishnah Rosh Hashanah 4:1–3 preserves post-destruction rules and disagreement about their scope. This later compiled legal memory is not a transcript of our fictional gathering.

ES: Mishná Rosh Hashaná4:1–3 conserva normas posteriores a la destrucción y desacuerdos sobre su alcance. Esta memoria legal compilada después no es una transcripción de nuestra reunión ficticia.

Condition: earned side-2 western original arrival once; source note then copy-hint · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### repair-offer (unassigned authored screen)

EN: Use the damaged store’s single repair action: pay 30 wood to restore that original store fully, then receive 20 wood once from reserve. Paying without restoration gives no reward.

ES: Usa la acción única de reparación del almacén dañado: paga 30 de madera para restaurar por completo ese almacén original y recibe después 20 de madera de la reserva una sola vez. Pagar sin restaurarlo no da recompensa.

Condition: optional panel from start and reread while nonterminal; exact cost/benefit before acceptance · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### repair-complete (unassigned authored screen)

EN: The roof has a use again. That is a smaller claim than rebuilding a lost world, and one I can write without borrowing another person’s grief.

ES: El techo vuelve a tener uso. Es una afirmación más pequeña que reconstruir un mundo perdido y puedo escribirla sin tomar prestado el dolor de otra persona.

Condition: after atomic once completion and own reserve debit/reward; bind this optional ID only · narrator: judith-copyist · native surface: pending certified SequenceItems/message adapter.

### trade-offer (unassigned authored screen)

EN: Escort the marked original trader to the southern receiving yard. Pay 20 gold there, then receive 20 food and 10 gold once from reserve. Its own reward cannot pay its cost.

ES: Escolta al comerciante original señalado hasta el patio receptor del sur. Paga allí20 de oro y recibe después 20 de alimento y 10 de oro de la reserva una sola vez. Su propia recompensa no puede pagar su coste.

Condition: optional panel from start and reread while nonterminal; exact cost/benefit before acceptance · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### trade-complete (unassigned authored screen)

EN: The exchange closes one account and opens a place at the table. Neither line says what another household must believe.

ES: El intercambio cierra una cuenta y abre un sitio en la mesa. Ninguna línea dice lo que otro hogar debe creer.

Condition: after atomic once completion and own reserve debit/reward; bind this optional ID only · narrator: judith-copyist · native surface: pending certified SequenceItems/message adapter.

### guide-offer (unassigned authored screen)

EN: Bring the original local guide to the western junction. Benefit: mark the existing northern approach through the Timber Bench to the Northern Turn. The task creates no road or change in terrain.

ES: Lleva al guía local original al cruce occidental. Ventaja: señala la aproximación norte existente por el banco de madera hasta el recodo del norte. La tarea no crea un camino ni cambia el terreno.

Condition: side-6 original guide offer; mark existing northern-approach only · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### guide-complete (unassigned authored screen)

EN: A turn can be missed without being secret. I prefer a clear direction to a tale in which the ground itself rewards us.

ES: Un recodo puede pasar inadvertido sin ser secreto. Prefiero una indicación clara a un relato en el que el propio suelo nos recompensa.

Condition: after atomic once completion and own reserve debit/reward; bind this optional ID only · narrator: judith-copyist · native surface: pending certified SequenceItems/message adapter.

### guest-offer (unassigned authored screen)

EN: Bring both marked original voluntary guests to the additional hearth alive. Pay 20 food for hospitality, then receive 10 food once from reserve. These guests are optional and cannot replace a main recipient.

ES: Lleva con vida a los dos invitados voluntarios originales señalados hasta el fogón adicional. Paga 20 de alimento por la hospitalidad y recibe después 10 de alimento de la reserva una sola vez. Estos invitados son opcionales y no sustituyen a ningún destinatario principal.

Condition: optional panel from start and reread while nonterminal; exact cost/benefit before acceptance · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### guest-complete (unassigned authored screen)

EN: There was room beyond the three promises in the ledger. I would not call that room a proof; I would keep it open.

ES: Había sitio más allá de las tres promesas del registro. Yo no llamaría prueba a ese sitio; lo dejaría abierto.

Condition: after atomic once completion and own reserve debit/reward; bind this optional ID only · narrator: judith-copyist · native surface: pending certified SequenceItems/message adapter.

### optional-unavailable (unassigned authored screen)

EN: This optional task can no longer be completed with its original actor or object. It gives no reward and does not defeat the main plan. Already earned receipts remain; replacements cannot complete it.

ES: Este secundario ya no puede completarse con su actor u objeto original. No da recompensa ni causa la derrota del plan principal. Los recibos ya ganados se conservan; los reemplazos no pueden completarlo.

Condition: one notification per failed optional ID; never main defeat · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### fresh-reception (unassigned authored screen)

EN: Before finishing, bring all three original main recipients alive into their selected receiving courts, with each selected result there too. Deliveries remain recorded, but past presence cannot replace current presence.

ES: Antes de terminar, lleva a los tres destinatarios originales principales vivos a sus patios receptores seleccionados, con cada resultado elegido también allí. Las entregas quedan registradas, pero la presencia pasada no sustituye a la actual.

Condition: all service receipts complete but fresh current output/recipient presence incomplete · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### defeat (defeat)

EN: A required original recipient, or a selected worker before completing its work, has been lost. A selected result has also become indispensable after commitment. Load an earlier save or restart if the plan cannot be completed.

ES: Se ha perdido un destinatario original obligatorio o un trabajador seleccionado antes de terminar su trabajo. Cada resultado seleccionado también es indispensable tras el compromiso. Carga una partida anterior o reinicia si el plan ya no puede completarse.

Condition: irreversible main failure, suppress victory and later optional mutations · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### source-limit (unassigned authored screen)

EN: The later Gittin 56 a–b account associates Yavneh with a request made during the siege. We preserve its later narrative status; no private negotiation is reenacted here.

ES: El relato posterior de Guitín 56 a–b asocia Yavneh con una petición durante el asedio. Conservamos su carácter narrativo posterior; aquí no se representa ninguna negociación privada.

Condition: optional copy historical note or freely reread historical notebook; never a victory prerequisite · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### victory-fact (factualOutro)

EN: The three invented local services are complete for their original recipients. This result does not date an academy’s foundation, settle disputed traditions or reverse the destruction of Jerusalem.

ES: Los tres servicios locales inventados están completos para sus destinatarios originales. Este resultado no fecha la fundación de una academia, resuelve tradiciones discutidas ni revierte la destrucción de Jerusalén.

Condition: fresh simultaneous selected output/recipient check passes; before victory-personal · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### victory-personal (personalOutro)

EN: I cannot enter their room from my own century. I can leave three names beside three completed tasks, and a margin for the voices that never reached my page.

ES: No puedo entrar en su habitación desde mi propio siglo. Puedo dejar tres nombres junto a tres tareas terminadas y un margen para las voces que nunca llegaron a mi página.

Condition: after victory-fact; before continue-next · narrator: judith-copyist · native surface: pending certified SequenceItems/message adapter.

### continue-next (continuation)

EN: Continue with The Questions We Carried, episode 3 of Keepers of the Unbroken Word, c.80–100 CE. It follows the circulation of learning; this is not the campaign finale.

ES: Continúa con Las preguntas que llevábamos, episodio 3 de Guardianes de la palabra viva, hacia 80–100 d.C. Trata de la circulación del aprendizaje; este no es el final de la campaña.

Condition: after victory-personal, next recommendation only · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### recipe-local-meal (unassigned authored screen)

EN: At the Local Hearth. Cost: 120 food, 20 wood, 0 gold. Work: The Local Hearth. Receive: The Neighbors’ Table.

ES: En el fogón local. Coste: 120 de alimento, 20 de madera, 0 de oro. Trabajo: El fogón local. Recepción: La mesa de los vecinos.

Condition: preview selected method; no debit · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### recipe-purchased-consignment (unassigned authored screen)

EN: The Western Consignment. Cost: 30 food, 0 wood, 70 gold. Work: The Western Trader. Receive: The Neighbors’ Table.

ES: La remesa occidental. Coste: 30 de alimento, 0 de madera, 70 de oro. Trabajo: El comerciante occidental. Recepción: La mesa de los vecinos.

Condition: preview selected method; no debit · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### recipe-assembled-shelter (unassigned authored screen)

EN: A Shelter Prepared Together. Cost: 20 food, 100 wood, 0 gold. Work: The Timber Bench. Receive: The Prepared Meeting Court.

ES: Un refugio preparado entre todos. Coste: 20 de alimento, 100 de madera, 0 de oro. Trabajo: El banco de madera. Recepción: El patio preparado para reunirse.

Condition: preview selected method; no debit · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### recipe-offered-room (unassigned authored screen)

EN: The Door Offered Freely. Cost: 0 food, 20 wood, 70 gold. Work: The Host’s Preparation Yard. Receive: The Offered Room.

ES: La puerta que se ofrece. Coste: 0 de alimento, 20 de madera, 70 de oro. Trabajo: El patio de preparación del anfitrión. Recepción: La estancia ofrecida.

Condition: preview selected method; no debit · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### recipe-local-working-materials (unassigned authored screen)

EN: Materials Put to Use. Cost: 20 food, 40 wood, 0 gold. Work: The Local Working Bench. Receive: The Reading Cloth.

ES: Materiales que sirven. Coste: 20 de alimento, 40 de madera, 0 de oro. Trabajo: La mesa de trabajo local. Recepción: El paño de lectura.

Condition: preview selected method; no debit · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### recipe-purchased-working-materials (unassigned authored screen)

EN: The Prepared Bundle. Cost: 0 food, 10 wood, 60 gold. Work: The Western Trader. Receive: The Reading Cloth.

ES: El fardo preparado. Coste: 0 de alimento, 10 de madera, 60 de oro. Trabajo: El comerciante occidental. Recepción: El paño de lectura.

Condition: preview selected method; no debit · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### shared-attendance-goal (unassigned authored screen)

EN: Bring the original provisions recipient alive to the Neighbors’ Table. This records attendance only. It does not pay for, produce or complete any selected service. That recipient must be present there again at the final confirmation.

ES: Lleva al destinatario original de provisiones con vida hasta la mesa de los vecinos. Esto registra únicamente su asistencia. No paga, produce ni completa ningún servicio elegido. Ese destinatario deberá estar presente allí de nuevo en la confirmación final.

Condition: phase-1 shared objective; current presence and original arrival; no service receipt · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### plan-complete (unassigned authored screen)

EN: The three selected services have their own work and reception receipts. Finish only with each selected result and each original recipient alive at its selected court. A past receipt cannot supply someone who is absent now.

ES: Los tres servicios elegidos tienen sus propios recibos de trabajo y recepción. Termina únicamente con cada resultado elegido y destinatario original vivos en su patio seleccionado. Un recibo pasado no aporta a quien ahora está ausente.

Condition: selected services complete; documentary plan confirmation, never a terminal fact before the fresh final gate · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### copy-north-offer (unassigned authored screen)

EN: Bring the marked original northern working-record carrier to the Reading Cloth. Benefit: an attributed later-tradition note and a reminder that originals cannot be replaced. This task is independent of the western note and gives no resources.

ES: Lleva al portador original señalado de la anotación del norte al paño de lectura. Ventaja: una nota atribuida de tradición posterior y un recordatorio de que los originales no se sustituyen. Esta tarea es independiente de la anotación occidental y no da recursos.

Condition: side-3 offered from start, independent of side-2 and main goals; reread while available · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### copy-north-complete (unassigned authored screen)

EN: The later Gittin 56a–b narrative associates Yavneh with a request during the siege; it is not a contemporary transcript. Our working record and carrier are fictional. A spare carrier cannot replace this original, or the original assigned to the separate western note.

ES: El relato posterior de Guitín 56a–b asocia Yavneh con una petición durante el asedio; no es una transcripción contemporánea. Nuestra anotación de trabajo y su portador son ficticios. Un portador de repuesto no sustituye a este original ni al asignado a la anotación occidental independiente.

Condition: earned side-3 original arrival once; independent failure/receipt; contextual note and identity hint · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

## QA and capability limits

```json
{
  "qa": {
    "staticStatus": "typed v3 profile and dossier bindings checked",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "Enumerate all24 direct financial choices and preserve8/5/3; existing optional-prefix BFS gives8/7/6, never promise hard ACE/BDF.",
      "Exercise all nine style/difficulty prefixes with actual identities and travel; financial evidence alone is not a played style.",
      "Attendance alone must neither reserve resources nor create work/output/service receipts or victory.",
      "For each of six methods, reserve/cancel/refund once before commit and reject stale, partial or unaffordable choice without debit.",
      "After commit, each exact original worker departs and performs its own selected work; another service worker or unselected method cannot qualify.",
      "Only genuinely generated selected output can arrive; reject preplaced, wrong-recipe, duplicate and substitute results.",
      "Meeting C and D require distinct actual receiving courts, both for the selected output and the unchanged original recipient.",
      "All selected results and three original recipients require fresh alive presence at their selected courts at final; historical receipt or attendance is insufficient.",
      "Loss of required recipient/indispensable selected result defeats before simultaneous victory; worker loss after completed work does not undo it.",
      "Repair30W, trade20G and guests20F charge before reserve rewards. Require two aid originals and two guests, with no replacement or reward for optional loss.",
      "Save/load at reservation, cancellation, commitment, work/generation, every reception/reward and final arbitration; rotate observation epoch and reject queued stale actions.",
      "Verify all22 sites/27 interhub links/20 local approaches against approved terrain and actual circles/footprints; no modern river course or empty waterline certifies land.",
      "Check all44 EN/es-ES screen texts, role order, source cautions, cost/work/court display, contextual service completion and the real next episode03.",
      "Native v3 and multi-origin modes remain rejected until their explicit real adapters and engine QA exist; no fallback to old conjunctive payments.",
      "Revised design: west and north copy each has exactly one original, its own true origin/route, scoped receipt/effect and independent failure. Opposite or spare carrier cannot complete it.",
      "Seven-task BFS24rows preserve8/5/3 and8/7/6; all directly affordable main choices also have all-seven witnesses after immediate funding.",
      "The compound guide information corridor is exactly the two existing links through Timber Bench; no extra road, new terrain or duplicate physical route is created."
    ]
  },
  "requiredCapabilities": [
    {
      "id": "alternative-fulfillment-v3",
      "status": "actual reference model available; native selection/escrow/work/output/reception pending i00007/S3"
    },
    {
      "id": "current-original-presence",
      "status": "reference checks available; native terminal scheduling/save-load QA pending"
    },
    {
      "id": "single-origin-independent-secondary",
      "status": "one original per copy is legal in current complete-profile v3; actual typed full candidate still must be executed and reviewed"
    },
    {
      "id": "authored-secondary-costs",
      "status": "reference projection integrated b4bdc4ee; native extract arrival-plus-payment unsupported"
    },
    {
      "id": "historical-terrain-and-footprints",
      "status": "candidate frame and local paths authored; ancient land, slope, watercourse, footprints and native navigation unapproved"
    },
    {
      "id": "ordered-two-narrator-captions",
      "status": "EN/es-ES source44 screens specified; editorial/native/audio acceptance pending"
    }
  ],
  "continuation": {
    "nextEpisodeId": "03-distributed-study-network-yavneh",
    "campaignComplete": false,
    "sourceScreenId": "continue-next"
  },
  "gameplayIdentity": {
    "problem": "Keep three distinct voluntary local promises with exclusive methods, original workers/results/recipients and finite joint resources",
    "decision": "Compare resource mixture, different work/reception circuits and optional aid/context before irreversible commitment; three candidate styles are financially feasible in each difficulty",
    "density": "22 activity sites,27 physical interhub links,20 local approaches, six methods and7 independent secondary tasks; the guide information alias adds no physical road",
    "replay": "Historical outcome stays fixed; replay changes ADF/BCF/BDE or other affordable methods, independent note completion and optional order",
    "pacing": "Reflective civilian recovery episode after destruction, not another six-of-eight rescue, fake siege or deadline; challenge and travel remain uncalibrated",
    "limits": "No game-verified difficulty or duration; an interesting RTS experience is an acceptance obligation, not an assertion from menus and graphs"
  },
  "failureRecovery": {
    "beforeCommit": "Free preview; reject unaffordable input without debit; exact joint escrow refund once before irreversible commitment",
    "afterCommit": "Keep selected identities/costs; wrong destination or absent recipient yields no receipt, use the same originals at correct court; no timer or substitute work",
    "mainIdentityLoss": "Existing reference rules: original required recipient or indispensable generated selected result loss defeats first; selected worker loss before work defeats, loss after recorded work does not undo its result",
    "optionalIdentityLoss": "Each independent side task fails only on its own lost original or object; west/north copies fail independently; no reward/resurrection/main defeat",
    "resources": "Main all-skip8/5/3 choices; finite70F60W30G reward account separate from operating stock; no gathering, production, regeneration or replacement budget",
    "nativeStatus": "Reference recovery descriptions require actual native composition/input/save-load/engine evidence"
  }
}
```

A reference-profile projection is not native support. Native rendering, actual UI, audio, world footprints, pathfinding, difficulty, engine behavior and historical approval remain separate gates.
