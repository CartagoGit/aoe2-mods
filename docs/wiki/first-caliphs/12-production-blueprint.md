# Beneath the Desert Stars / Bajo las estrellas del desierto

Identity: `first-caliphs` / CDF-I00 / `CDF_FirstCaliphs`. Source locale `en`. Period 622–656 CE.

Asentamientos, expansión y gobiernos de la comunidad; conquistas militares no significan conversiones instantáneas.

This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.

[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)

## Arc, inflection points and ending

656: muerte de Uthman y crisis de gobierno, narradas fuera de la victoria militar final; enlaza I01.

Recommended order is narrative, not always chronological: the successor may overlap or revisit earlier events; announce its own date.

The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.

| Scenario | Event / dramatic task | Map |
|---|---|---|
| [The Oasis Road](scenarios/01-the-oasis-road.md) | 622 CE / settlement-logistics | 360 × 360 / medina |
| [The Roads of Yamama](scenarios/02-the-roads-of-yamama.md) | 632–633 CE / finite-campaign-escort | 360 × 360 / yamama |
| [The Edge of the River](scenarios/03-the-edge-of-the-river.md) | 636 CE / combined-arms-battle | 400 × 400 / yarmuk |
| [Fields of the Sawad](scenarios/04-fields-of-the-sawad.md) | mid-630s; conventional 636/637 / irrigation-front-battle | 360 × 360 / qadisiyya |
| [A Camp Beside the Nile](scenarios/05-a-camp-beside-the-nile.md) | 641–642 CE; epilogue to 656 / river-port-logistics | 400 × 400 / fustat |

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
  "cover": "Beneath the Desert Stars: Yathrib / Medina oasis, 622 CE; foreground Administrador de caravanas y suministros; no modern skyline or invented sacred portrait.",
  "portrait": "Fictional Salim, the Caravan Scribe, occupational props, plain clothing without fabricated uniform; expression follows temperament. Label composite fictional narrator in credits.",
  "assets": [
    "yarmuk-valley",
    "dura-plan"
  ],
  "delivery": "One cover, one narrator portrait, one context map per scenario; licensed or original PNG; no paid batch authorized."
}

## Predecessors and campaign screens

Static advice always appears in the description and intro. Conditional variants depend on verified SequenceItems conditions and profile persistence; unknown progress never blocks play. Selected routes set only their own progress key to 1. No cross-mod launch button is promised: show title and public identity, then return to the engine menu.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.first-caliphs.title` / always | none → next | Beneath the Desert Stars | Bajo las estrellas del desierto |
| `campaign.first-caliphs.description` / always | none → next | 622–656 CE. Follow Salim, the Caravan Scribe through 5 scenarios. Each begins with a factual account, then a personal recollection. All campaigns can be played independently. | 622–656 CE. Sigue a Salim, the Caravan Scribe en 5 escenarios. Cada uno comienza con un relato de los hechos y después una memoria personal. Todas las campañas se pueden jugar de forma independiente. |
| `campaign.first-caliphs.voice-contract` / first intro | collection-narrator → next | The shared narrator gives the historical frame. The campaign narrator is a fictional person whose memories, songs and inherited accounts offer a situated perspective. Invented dialogue is never a historical quotation. | El narrador común presenta el marco histórico. El narrador de campaña es un personaje ficticio cuya memoria, cantares y relatos heredados ofrecen una perspectiva situada. Los diálogos inventados nunca son citas históricas. |
| `campaign.first-caliphs.personal-introduction` / after factual frame | salim-caravan-scribe → next | I knew the sky by its stars and a road by its wells. Then the roads began to lead farther than any ledger I had carried. | Conocía el cielo por sus estrellas y el camino por sus pozos. Después los caminos llegaron más lejos que cualquier registro que había llevado. |
| `campaign.first-caliphs.independent-entry` / always | collection-narrator → next | You may begin here. Dates on each scenario distinguish events from later memories. No earlier campaign is required. | Puedes empezar aquí. Las fechas de cada escenario distinguen los hechos de las memorias posteriores. No necesitas una campaña anterior. |
| `campaign.first-caliphs.continue-completed` / victory selected completed; write only progress.first-caliphs.completed=1 | collection-narrator → first-fitna | This campaign is complete. Your completed perspective is remembered. Recommended next: The Shattered Oath (CDF-I01; begins 656 CE). You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva completed. Continúa con El juramento quebrado (CDF-I01; comienza en 656 CE). También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |

## Historical source ledger

- [Fred M. Donner, The Early Islamic Conquests (extract)](https://sourcebooks.web.fordham.edu/med/donner.asp): Estratos y organización de la comunidad. Extracto consultado; no lectura del libro completo.
- [The Met, Byzantium and Islam](https://www.metmuseum.org/exhibitions/listings/2012/byzantium-and-islam): Transformaciones regionales siglos VII–IX. Panorama y objetos; evitar presentarlo como explicación causal exhaustiva.
- [Al-Baladhuri, The Battle of Yarmuk](https://sourcebooks.web.fordham.edu/source/yarmuk.asp): Descripción y episodios posteriores. Autor del siglo IX; enormes efectivos y discursos no son datos seguros.
- [D. Gershon Lewental, Qadesiya, Battle of](https://www.iranicaonline.org/articles/qadesiya-battle/): Cronología, lugar y discusión de las fuentes. 636/637 es la banda convencional; hay propuestas 634/635. Posición del campo y cifras no se fijan como certeza.
- [Accounts of the Arab Conquest of Egypt](https://sourcebooks.web.fordham.edu/source/642Egypt-conq2.asp): Patriarcas de Alejandría y al-Baladhuri, secciones de fortaleza y capitulación. Relatos tardíos con cronologías/tendencias distintas; contrastar, no fundirlos.
