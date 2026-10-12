# The Keys of the Eternal City / Las llaves de la Ciudad Eterna

Identity: `church-of-rome` / CDF-C03 / `CDF_ChurchOfRome`. Source locale `en`. Period 337–800 CE; missions 410–800.

Una ciudad, su abastecimiento y sus instituciones entre autoridad imperial, obispos y reyes.

This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.

[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)

## Arc, inflection points and ending

800: coronación de Carlos en Roma; cierre de un arco institucional, no nacimiento instantáneo de una iglesia moderna separada.

Recommended order is narrative, not always chronological: the successor may overlap or revisit earlier events; announce its own date.

The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.

| Scenario | Event / dramatic task | Map |
|---|---|---|
| [Bread Beyond the Gates](scenarios/01-bread-beyond-the-gates.md) | 410 CE / supply-under-collapse | 360 × 360 / rome-ostia |
| [The Price of Peace](scenarios/02-the-price-of-peace.md) | 593–595 CE / bounded-negotiation | 320 × 320 / rome-ostia |
| [Roads to Pavia](scenarios/03-roads-to-pavia.md) | 754–756 CE / campaign-logistics | 360 × 360 / pavia |
| [A Crown at Dawn](scenarios/04-a-crown-at-dawn.md) | 25 December 800 / ceremonial-security | 320 × 320 / rome-ostia |

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
  "cover": "The Keys of the Eternal City: Rome, Portus and Ostia, 410 CE; foreground Cantor itinerante y escribiente ocasional en hospicios; no modern skyline or invented sacred portrait.",
  "portrait": "Fictional Leo of the Roman Roads, occupational props, plain clothing without fabricated uniform; expression follows temperament. Label composite fictional narrator in credits.",
  "assets": [
    "ponte-milvio",
    "ravenna-justinian"
  ],
  "delivery": "One cover, one narrator portrait, one context map per scenario; licensed or original PNG; no paid batch authorized."
}

## Predecessors and campaign screens

Static advice always appears in the description and intro. Conditional variants depend on verified SequenceItems conditions and profile persistence; unknown progress never blocks play. Selected routes set only their own progress key to 1. No cross-mod launch button is promised: show title and public identity, then return to the engine menu.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.church-of-rome.title` / always | none → next | The Keys of the Eternal City | Las llaves de la Ciudad Eterna |
| `campaign.church-of-rome.description` / always | none → next | 337–800 CE; missions 410–800. Follow Leo of the Roman Roads through 4 scenarios. Each begins with a factual account, then a personal recollection. All campaigns can be played independently. | 337–800 CE; missions 410–800. Sigue a Leo of the Roman Roads en 4 escenarios. Cada uno comienza con un relato de los hechos y después una memoria personal. Todas las campañas se pueden jugar de forma independiente. |
| `campaign.church-of-rome.voice-contract` / first intro | collection-narrator → next | The shared narrator gives the historical frame. The campaign narrator is a fictional person whose memories, songs and inherited accounts offer a situated perspective. Invented dialogue is never a historical quotation. | El narrador común presenta el marco histórico. El narrador de campaña es un personaje ficticio cuya memoria, cantares y relatos heredados ofrecen una perspectiva situada. Los diálogos inventados nunca son citas históricas. |
| `campaign.church-of-rome.personal-introduction` / after factual frame | leo-road-singer → next | A road gives a singer a chorus. A city gives him too many verses. Listen for the difference between a song and a record. | Un camino da al cantor un estribillo. Una ciudad le da demasiadas estrofas. Escucha la diferencia entre una canción y un registro. |
| `campaign.church-of-rome.predecessor-advice` / always in mod description and opening; never a permission check | collection-narrator → next | Recommended first: The Eagle and the Cross (CDF-C01), western-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 410 CE, and may revisit an overlapping period. | Se recomienda jugar antes El águila y la cruz (CDF-C01), ruta western-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 410 CE y puede volver a un período solapado. |
| `campaign.church-of-rome.predecessor-missing` / required route progress.imperial-church.western-perspective is not >0, if native condition verified; otherwise static advice | collection-narrator → next | Recommended first: The Eagle and the Cross (CDF-C01), western-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 410 CE, and may revisit an overlapping period. | Se recomienda jugar antes El águila y la cruz (CDF-C01), ruta western-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 410 CE y puede volver a un período solapado. |
| `campaign.church-of-rome.predecessor-present` / progress.imperial-church.western-perspective>0 only when profile persistence verified | collection-narrator → next | Your earlier route in The Eagle and the Cross is remembered. Here we follow a new narrator and the documented events of 337–800 CE; missions 410–800. | Se recuerda tu ruta anterior en El águila y la cruz. Aquí seguimos a otro narrador y los hechos documentados de 337–800 CE; missions 410–800. |
| `campaign.church-of-rome.predecessor-other-route` / other route >0 and required route not >0; conditional encoding must be certified | collection-narrator → next | Recommended first: The Eagle and the Cross (CDF-C01), western-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 410 CE, and may revisit an overlapping period. | Se recomienda jugar antes El águila y la cruz (CDF-C01), ruta western-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 410 CE y puede volver a un período solapado. |
| `campaign.church-of-rome.predecessor-unknown` / progress unavailable, mod absent, profile reset or layout not certified | collection-narrator → next | Recommended first: The Eagle and the Cross (CDF-C01), western-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 410 CE, and may revisit an overlapping period. | Se recomienda jugar antes El águila y la cruz (CDF-C01), ruta western-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 410 CE y puede volver a un período solapado. |
| `campaign.church-of-rome.continue-completed` / victory selected completed; write only progress.church-of-rome.completed=1 | collection-narrator → collection catalogue | This campaign is complete. Your completed perspective is remembered. Recommended next: the parallel stories in the collection. There is no designated direct sequel in this catalogue. You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva completed. Continúa con los relatos paralelos de la colección. Este catálogo no incluye una continuación directa designada. También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.church-of-rome.predecessor-recap` / always before first scenario, skippable; same sufficient recap regardless of stored progress | collection-narrator → personal-introduction | Constantine’s reign ended in337. We now follow later events around Rome, beginning in410, through negotiations and Frankish intervention to800. This regional perspective is not an instant church split in337. | El reinado de Constantino terminó en337. Seguimos hechos posteriores alrededor de Roma, desde410, pasando por negociaciones e intervención franca hasta800. Esta perspectiva regional no es un cisma instantáneo en337. |

## Historical source ledger

- [Augustine, City of God I](https://www.newadvent.org/fathers/120101.htm): I.1: santuarios y saqueo de Roma. Apologética: no usar como registro exhaustivo de protección individual.
- [Gregory I, Register V.36](https://www.newadvent.org/fathers/360205036.htm): V.36: arbitraje con Agilulfo y exarca. Las negociaciones no tienen un resultado único impuesto por esta carta.
- [Einhard, Life of Charlemagne](https://sourcebooks.web.fordham.edu/basis/einhard.asp): 6: campañas italianas; 28: coronación. Autor ligado a la corte; la sorpresa de Carlos es objeto de debate.
- [Fordham introduction to Donation of Constantine](https://sourcebooks.web.fordham.edu/source/donatconst.asp): Editorial historical context of 754/756. The Donation of Constantine itself is a forgery, not evidence for a donation in the fourth century.
