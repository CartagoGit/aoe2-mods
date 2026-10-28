# The Shattered Oath / El juramento quebrado

Identity: `first-fitna` / CDF-I01 / `CDF_FirstFitna`. Source locale `en`. Period 656–661 CE.

Guerra civil y autoridad en disputa; las tradiciones posteriores no son dos bloques ya acabados en 656.

This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.

[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)

## Arc, inflection points and ending

661: muerte de Ali y acuerdo posterior de Hasan con Muawiya; eventos separados. Perspectivas a I02/I03, no finales que cambien quién gobierna.

Recommended order is narrative, not always chronological: the successor may overlap or revisit earlier events; announce its own date.

The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.

| Scenario | Event / dramatic task | Map |
|---|---|---|
| [News from Medina](scenarios/01-news-from-medina.md) | 656 CE / documented-crisis-escort | 320 × 320 / medina |
| [Between the Camps](scenarios/02-between-the-camps.md) | 656 CE / battlefield-evacuation | 360 × 360 / basra |
| [Water and Words](scenarios/03-water-and-words.md) | 657 CE / water-logistics-and-truce | 400 × 400 / siffin |
| [The Canal Road](scenarios/04-the-canal-road.md) | 658 CE / limited-withdrawal | 360 × 360 / nahrawan |
| [Two Archives, One Past](scenarios/05-two-archives.md) | 661 CE / settlement-and-perspective | 320 × 320 / kufa |

## Engine representation

{
  "playerCivilization": "Saracens",
  "rationale": "Engine proxy for available period-neutral gameplay, never identity of a religion or claim of authentic material culture. Resolve numeric IDs from the pinned parser catalogue.",
  "dlc": "Base DE proxies only; do not require Romans/RoR/DLC or silently use a different game mode.",
  "technology": "Feudal maximum by default; no gunpowder, modern fortifications, monks converting faith, unique units, trebuchets or late plate-armoured knights. Battering ram is an explicit visual/technology proxy where military outposts must fall."
}

## Art assignments

{
  "medium": "Painted historical illustration, map first; contemporary reference photos are for research only.",
  "cover": "The Shattered Oath: Yathrib / Medina oasis, 656 CE; foreground Auxiliar de enfermería militar y escriba de listas de bajas; no modern skyline or invented sacred portrait.",
  "portrait": "Fictional Farid, the Field Medic, occupational props, plain clothing without fabricated uniform; expression follows temperament. Label composite fictional narrator in credits.",
  "assets": [
    "dura-plan",
    "damascus-mosque"
  ],
  "delivery": "One cover, one narrator portrait, one context map per scenario; licensed or original PNG; no paid batch authorized."
}

## Predecessors and campaign screens

Static advice always appears in the description and intro. Conditional variants depend on verified SequenceItems conditions and profile persistence; unknown progress never blocks play. Selected routes set only their own progress key to 1. No cross-mod launch button is promised: show title and public identity, then return to the engine menu.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.first-fitna.title` / always | none → next | The Shattered Oath | El juramento quebrado |
| `campaign.first-fitna.description` / always | none → next | 656–661 CE. Follow Farid, the Field Medic through 5 scenarios. Each begins with a factual account, then a personal recollection. All campaigns can be played independently. | 656–661 CE. Sigue a Farid, the Field Medic en 5 escenarios. Cada uno comienza con un relato de los hechos y después una memoria personal. Todas las campañas se pueden jugar de forma independiente. |
| `campaign.first-fitna.voice-contract` / first intro | collection-narrator → next | The shared narrator gives the historical frame. The campaign narrator is a fictional person whose memories, songs and inherited accounts offer a situated perspective. Invented dialogue is never a historical quotation. | El narrador común presenta el marco histórico. El narrador de campaña es un personaje ficticio cuya memoria, cantares y relatos heredados ofrecen una perspectiva situada. Los diálogos inventados nunca son citas históricas. |
| `campaign.first-fitna.personal-introduction` / after factual frame | farid-field-medic → next | I learned which camp a man came from after I had bound the wound. Before that, I knew only that he needed help. | Aprendía de qué campamento venía un hombre después de vendarle la herida. Antes solo sabía que necesitaba ayuda. |
| `campaign.first-fitna.predecessor-advice` / always in mod description and opening; never a permission check | collection-narrator → next | Recommended first: Beneath the Desert Stars (CDF-I00), completed. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 656 CE, and may revisit an overlapping period. | Se recomienda jugar antes Bajo las estrellas del desierto (CDF-I00), ruta completed. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 656 CE y puede volver a un período solapado. |
| `campaign.first-fitna.predecessor-missing` / required route progress.first-caliphs.completed is not >0, if native condition verified; otherwise static advice | collection-narrator → next | Recommended first: Beneath the Desert Stars (CDF-I00), completed. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 656 CE, and may revisit an overlapping period. | Se recomienda jugar antes Bajo las estrellas del desierto (CDF-I00), ruta completed. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 656 CE y puede volver a un período solapado. |
| `campaign.first-fitna.predecessor-present` / progress.first-caliphs.completed>0 only when profile persistence verified | collection-narrator → next | Your earlier route in Beneath the Desert Stars is remembered. Here we follow a new narrator and the documented events of 656–661 CE. | Se recuerda tu ruta anterior en Bajo las estrellas del desierto. Aquí seguimos a otro narrador y los hechos documentados de 656–661 CE. |
| `campaign.first-fitna.predecessor-other-route` / other route >0 and required route not >0; conditional encoding must be certified | collection-narrator → next | Recommended first: Beneath the Desert Stars (CDF-I00), completed. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 656 CE, and may revisit an overlapping period. | Se recomienda jugar antes Bajo las estrellas del desierto (CDF-I00), ruta completed. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 656 CE y puede volver a un período solapado. |
| `campaign.first-fitna.predecessor-unknown` / progress unavailable, mod absent, profile reset or layout not certified | collection-narrator → next | Recommended first: Beneath the Desert Stars (CDF-I00), completed. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 656 CE, and may revisit an overlapping period. | Se recomienda jugar antes Bajo las estrellas del desierto (CDF-I00), ruta completed. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 656 CE y puede volver a un período solapado. |
| `campaign.first-fitna.continue-muawiya-perspective` / victory selected muawiya-perspective; write only progress.first-fitna.muawiya-perspective=1 | collection-narrator → umayyads | This campaign is complete. Your muawiya-perspective perspective is remembered. Recommended next: From Damascus to the Far Horizon (CDF-I02; begins 661 CE). You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva muawiya-perspective. Continúa con De Damasco al último horizonte (CDF-I02; comienza en 661 CE). También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.first-fitna.continue-ali-perspective` / victory selected ali-perspective; write only progress.first-fitna.ali-perspective=1 | collection-narrator → house-of-ali | This campaign is complete. Your ali-perspective perspective is remembered. Recommended next: The River Remembers (CDF-I03; begins 656 CE). You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva ali-perspective. Continúa con El río recuerda (CDF-I03; comienza en 656 CE). También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.first-fitna.predecessor-recap` / always before first scenario, skippable; same sufficient recap regardless of stored progress | collection-narrator → personal-introduction | The earlier campaign followed migration and conquests to the crisis of656. Uthman’s death opens this arc; rival claims, negotiations and subsequent events lead to a choice of archives in661. | La campaña anterior siguió migración y conquistas hasta la crisis de656. La muerte de Uthman abre este arco; reclamaciones rivales, negociaciones y hechos posteriores llevan a elegir archivo en661. |

## Historical source ledger

- [Ismail K. Poonawala, Ali: Life](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Secciones califato, Camello, Siffin y muerte. Distinguir la reconstrucción histórica de las interpretaciones comunitarias.
- [Wilferd Madelung, Hasan b. Ali](https://www.iranicaonline.org/articles/hasan-b-ali/): Negociaciones y renuncia en 661. La conversión 660 de la muerte de Ali en esta página entra en conflicto con su entrada Ali: se registra errata y se usa 661 con contraste.
