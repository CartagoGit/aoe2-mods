# The Eagle and the Cross / El águila y la cruz

Identity: `imperial-church` / CDF-C01 / `CDF_ImperialChurch`. Source locale `en`. Period 312–337 CE.

Poder imperial, cristianismo e instituciones; 312/325/330 conservan los tres escenarios existentes.

This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.

[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)

## Arc, inflection points and ending

337: muerte de Constantino; se abre la historia regional de Roma y Nueva Roma, todavía sin cisma de iglesias actuales.

Recommended order is narrative, not always chronological: the successor may overlap or revisit earlier events; announce its own date.

The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.

| Scenario | Event / dramatic task | Map |
|---|---|---|
| [The Last Bridge to Rome](scenarios/01-milvian-bridge.md) | 28 October 312 / river-battle | 360 × 360 / milvio |
| [Voices Beside the Lake](scenarios/02-nicaea.md) | 325 CE / delegate-logistics | 320 × 320 / nicaea |
| [Where Two Seas Meet](scenarios/03-new-capital.md) | 330 CE; epilogue to 337 / urban-logistics | 360 × 360 / constantinople |

## Engine representation

{
  "playerCivilization": "Byzantines",
  "rationale": "Engine proxy for available period-neutral gameplay, never identity of a religion or claim of authentic material culture. Resolve numeric IDs from the pinned parser catalogue.",
  "dlc": "Base DE proxies only; do not require Romans/RoR/DLC or silently use a different game mode.",
  "technology": "Feudal maximum by default; no gunpowder, modern fortifications, monks converting faith, unique units, trebuchets or late plate-armoured knights. Battering ram is an explicit visual/technology proxy where military outposts must fall."
}

## Art assignments

{
  "medium": "Painted historical illustration, map first; contemporary reference photos are for research only.",
  "cover": "The Eagle and the Cross: Pons Mulvius and northern Rome, 28 October 312; foreground Antiguo auxiliar de intendencia y copista de expedientes; no modern skyline or invented sacred portrait.",
  "portrait": "Fictional Marcus, the Imperial Clerk, occupational props, plain clothing without fabricated uniform; expression follows temperament. Label composite fictional narrator in credits.",
  "assets": [
    "ponte-milvio",
    "iznik-lake",
    "theodosian-walls"
  ],
  "delivery": "One cover, one narrator portrait, one context map per scenario; licensed or original PNG; no paid batch authorized."
}

## Predecessors and campaign screens

Static advice always appears in the description and intro. Conditional variants depend on verified SequenceItems conditions and profile persistence; unknown progress never blocks play. Selected routes set only their own progress key to 1. No cross-mod launch button is promised: show title and public identity, then return to the engine menu.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.imperial-church.title` / always | none → next | The Eagle and the Cross | El águila y la cruz |
| `campaign.imperial-church.description` / always | none → next | 312–337 CE. Follow Marcus, the Imperial Clerk through 3 scenarios. Each begins with a factual account, then a personal recollection. All campaigns can be played independently. | 312–337 CE. Sigue a Marcus, the Imperial Clerk en 3 escenarios. Cada uno comienza con un relato de los hechos y después una memoria personal. Todas las campañas se pueden jugar de forma independiente. |
| `campaign.imperial-church.voice-contract` / first intro | collection-narrator → next | The shared narrator gives the historical frame. The campaign narrator is a fictional person whose memories, songs and inherited accounts offer a situated perspective. Invented dialogue is never a historical quotation. | El narrador común presenta el marco histórico. El narrador de campaña es un personaje ficticio cuya memoria, cantares y relatos heredados ofrecen una perspectiva situada. Los diálogos inventados nunca son citas históricas. |
| `campaign.imperial-church.personal-introduction` / after factual frame | imperial-clerk → next | An eagle can be stitched onto a banner. Feeding the men beneath it is harder. That was my trade. | Un águila se puede coser a una bandera. Dar de comer a los hombres que marchan debajo cuesta más. Ese era mi oficio. |
| `campaign.imperial-church.predecessor-advice` / always in mod description and opening; never a permission check | collection-narrator → next | Recommended first: Embers of the Covenant (CDF-C00), christian-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 28 October 312, and may revisit an overlapping period. | Se recomienda jugar antes Las brasas de la alianza (CDF-C00), ruta christian-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 28 October 312 y puede volver a un período solapado. |
| `campaign.imperial-church.predecessor-missing` / required route progress.faith-origins.christian-perspective is not >0, if native condition verified; otherwise static advice | collection-narrator → next | Recommended first: Embers of the Covenant (CDF-C00), christian-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 28 October 312, and may revisit an overlapping period. | Se recomienda jugar antes Las brasas de la alianza (CDF-C00), ruta christian-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 28 October 312 y puede volver a un período solapado. |
| `campaign.imperial-church.predecessor-present` / progress.faith-origins.christian-perspective>0 only when profile persistence verified | collection-narrator → next | Your earlier route in Embers of the Covenant is remembered. Here we follow a new narrator and the documented events of 312–337 CE. | Se recuerda tu ruta anterior en Las brasas de la alianza. Aquí seguimos a otro narrador y los hechos documentados de 312–337 CE. |
| `campaign.imperial-church.predecessor-other-route` / other route >0 and required route not >0; conditional encoding must be certified | collection-narrator → next | Recommended first: Embers of the Covenant (CDF-C00), christian-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 28 October 312, and may revisit an overlapping period. | Se recomienda jugar antes Las brasas de la alianza (CDF-C00), ruta christian-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 28 October 312 y puede volver a un período solapado. |
| `campaign.imperial-church.predecessor-unknown` / progress unavailable, mod absent, profile reset or layout not certified | collection-narrator → next | Recommended first: Embers of the Covenant (CDF-C00), christian-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 28 October 312, and may revisit an overlapping period. | Se recomienda jugar antes Las brasas de la alianza (CDF-C00), ruta christian-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 28 October 312 y puede volver a un período solapado. |
| `campaign.imperial-church.continue-western-perspective` / victory selected western-perspective; write only progress.imperial-church.western-perspective=1 | collection-narrator → church-of-rome | This campaign is complete. Your western-perspective perspective is remembered. Recommended next: The Keys of the Eternal City (CDF-C03; begins 410 CE). You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva western-perspective. Continúa con Las llaves de la Ciudad Eterna (CDF-C03; comienza en 410 CE). También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.imperial-church.continue-eastern-perspective` / victory selected eastern-perspective; write only progress.imperial-church.eastern-perspective=1 | collection-narrator → new-rome | This campaign is complete. Your eastern-perspective perspective is remembered. Recommended next: Beyond the Golden Gate (CDF-C04; begins 451 CE). You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva eastern-perspective. Continúa con Más allá de la Puerta Dorada (CDF-C04; comienza en 451 CE). También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.imperial-church.predecessor-recap` / always before first scenario, skippable; same sufficient recap regardless of stored progress | collection-narrator → personal-introduction | The earlier archive follows communities through persecution and the legal changes of 313. This campaign revisits 312 before moving to Nicaea and Constantinople; institutional histories overlap. | El archivo anterior sigue comunidades durante las persecuciones y los cambios legales de313. Esta campaña vuelve a312 antes de pasar a Nicea y Constantinopla; las historias institucionales se solapan. |

## Historical source ledger

- [Eusebius, Church History IX](https://www.newadvent.org/fathers/250109.htm): IX.9: victoria ante Majencio. Perspectiva favorable a Constantino, no parte militar neutral.
- [Lactantius, On the Deaths of the Persecutors](https://www.newadvent.org/fathers/0705.htm): 44: Milvio; 48: disposiciones de 313. El sueño es testimonio religioso; no convertirlo en buff sobrenatural.
- [First Council of Nicaea, Creed and Canons](https://www.newadvent.org/fathers/3801.htm): Credo y cánones 4–7. No es el origen inmediato de católicos/ortodoxos modernos.
- [The Met, Byzantium (ca. 330–1453)](https://www.metmuseum.org/essays/byzantium-ca-330-1453): Períodos y cultura material. Ensayo de museo de síntesis, no plano arqueológico ni cronología militar completa.
- [UNESCO, Historic Areas of Istanbul](https://whc.unesco.org/en/list/356/): Península, murallas y monumentos. Paisaje de varias épocas: filtrar fecha de cada edificio.
