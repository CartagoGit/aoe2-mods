# The River Remembers / El río recuerda

Identity: `house-of-ali` / CDF-I03 / `CDF_HouseOfAli`. Source locale `en`. Period 656–680 CE.

Red familiar y memoria de Ali, Hasan y Husayn; perspectivas y tradiciones comunitarias se atribuyen, nunca se representan como verdades ganadas con armas.

This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.

[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)

## Arc, inflection points and ending

680: muerte de Husayn en Karbala y consecuencias narradas con contención; no ofrecer una victoria que evite ese hecho en campaña histórica.

Recommended order is narrative, not always chronological: the successor may overlap or revisit earlier events; announce its own date.

The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.

| Scenario | Event / dramatic task | Map |
|---|---|---|
| [The Kufan Hearth](scenarios/01-the-kufan-hearth.md) | 656 CE / district-recovery | 320 × 320 / kufa |
| [A Cup at Siffin](scenarios/02-a-cup-at-siffin.md) | 657 CE / aid-corridor | 360 × 360 / siffin |
| [The Sealed Copy](scenarios/03-the-sealed-copy.md) | 661 CE / archive-evacuation | 320 × 320 / kufa |
| [The Water That Remains](scenarios/04-the-water-that-remains.md) | 680 CE / civilian-witness-withdrawal | 360 × 360 / karbala |

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
  "cover": "The River Remembers: Kufa and Euphrates margin, 656 CE; foreground Alfarera y proveedora de vasijas para familias viajeras; no modern skyline or invented sacred portrait.",
  "portrait": "Fictional Dina of the Riverbank, occupational props, plain clothing without fabricated uniform; expression follows temperament. Label composite fictional narrator in credits.",
  "assets": [
    "dura-plan"
  ],
  "delivery": "One cover, one narrator portrait, one context map per scenario; licensed or original PNG; no paid batch authorized."
}

## Predecessors and campaign screens

Static advice always appears in the description and intro. Conditional variants depend on verified SequenceItems conditions and profile persistence; unknown progress never blocks play. Selected routes set only their own progress key to 1. No cross-mod launch button is promised: show title and public identity, then return to the engine menu.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.house-of-ali.title` / always | none → next | The River Remembers | El río recuerda |
| `campaign.house-of-ali.description` / always | none → next | 656–680 CE. Follow Dina of the Riverbank through 4 scenarios. Each begins with a factual account, then a personal recollection. All campaigns can be played independently. | 656–680 CE. Sigue a Dina of the Riverbank en 4 escenarios. Cada uno comienza con un relato de los hechos y después una memoria personal. Todas las campañas se pueden jugar de forma independiente. |
| `campaign.house-of-ali.voice-contract` / first intro | collection-narrator → next | The shared narrator gives the historical frame. The campaign narrator is a fictional person whose memories, songs and inherited accounts offer a situated perspective. Invented dialogue is never a historical quotation. | El narrador común presenta el marco histórico. El narrador de campaña es un personaje ficticio cuya memoria, cantares y relatos heredados ofrecen una perspectiva situada. Los diálogos inventados nunca son citas históricas. |
| `campaign.house-of-ali.personal-introduction` / after factual frame | dina-potter → next | A jar remembers the hand that shaped it. A family remembers more, and not always in the same way. I will tell you which memories are mine. | Una vasija conserva la mano que le dio forma. Una familia guarda más, y no siempre de la misma manera. Te diré qué recuerdos son míos. |
| `campaign.house-of-ali.predecessor-advice` / always in mod description and opening; never a permission check | collection-narrator → next | Recommended first: The Shattered Oath (CDF-I01), ali-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 656 CE, and may revisit an overlapping period. | Se recomienda jugar antes El juramento quebrado (CDF-I01), ruta ali-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 656 CE y puede volver a un período solapado. |
| `campaign.house-of-ali.predecessor-missing` / required route progress.first-fitna.ali-perspective is not >0, if native condition verified; otherwise static advice | collection-narrator → next | Recommended first: The Shattered Oath (CDF-I01), ali-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 656 CE, and may revisit an overlapping period. | Se recomienda jugar antes El juramento quebrado (CDF-I01), ruta ali-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 656 CE y puede volver a un período solapado. |
| `campaign.house-of-ali.predecessor-present` / progress.first-fitna.ali-perspective>0 only when profile persistence verified | collection-narrator → next | Your earlier route in The Shattered Oath is remembered. Here we follow a new narrator and the documented events of 656–680 CE. | Se recuerda tu ruta anterior en El juramento quebrado. Aquí seguimos a otro narrador y los hechos documentados de 656–680 CE. |
| `campaign.house-of-ali.predecessor-other-route` / other route >0 and required route not >0; conditional encoding must be certified | collection-narrator → next | Recommended first: The Shattered Oath (CDF-I01), ali-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 656 CE, and may revisit an overlapping period. | Se recomienda jugar antes El juramento quebrado (CDF-I01), ruta ali-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 656 CE y puede volver a un período solapado. |
| `campaign.house-of-ali.predecessor-unknown` / progress unavailable, mod absent, profile reset or layout not certified | collection-narrator → next | Recommended first: The Shattered Oath (CDF-I01), ali-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 656 CE, and may revisit an overlapping period. | Se recomienda jugar antes El juramento quebrado (CDF-I01), ruta ali-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 656 CE y puede volver a un período solapado. |
| `campaign.house-of-ali.continue-completed` / victory selected completed; write only progress.house-of-ali.completed=1 | collection-narrator → collection catalogue | This campaign is complete. Your completed perspective is remembered. Recommended next: the parallel stories in the collection. There is no designated direct sequel in this catalogue. You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva completed. Continúa con los relatos paralelos de la colección. Este catálogo no incluye una continuación directa designada. También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.house-of-ali.predecessor-recap` / always before first scenario, skippable; same sufficient recap regardless of stored progress | collection-narrator → personal-introduction | The family archive offers another perspective on the same years. This campaign returns to656, distinguishes Ali’s death from Hasan’s agreement in661, and follows memory and civilian experience to Karbala in680. | El archivo familiar ofrece otra perspectiva de los mismos años. Esta campaña vuelve a656, distingue la muerte de Alí del acuerdo de Hasan en661 y sigue memoria y experiencia civil hasta Karbala en680. |

## Historical source ledger

- [Ismail K. Poonawala, Ali: Life](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Secciones califato, Camello, Siffin y muerte. Distinguir la reconstrucción histórica de las interpretaciones comunitarias.
- [Wilferd Madelung, Hasan b. Ali](https://www.iranicaonline.org/articles/hasan-b-ali/): Negociaciones y renuncia en 661. La conversión 660 de la muerte de Ali en esta página entra en conflicto con su entrada Ali: se registra errata y se usa 661 con contraste.
- [Wilferd Madelung, Husayn: Life and Significance](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Viaje y muerte en Karbala. Las escenas domésticas del narrador son ficticias, no citas de Husayn.
- [Encyclopaedia Iranica, Karbala](https://www.iranicaonline.org/articles/karbala/): Memoria, enterramiento y visitas posteriores. El santuario moderno no pertenece al paisaje de 680.
