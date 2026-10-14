# Beyond the Golden Gate / Más allá de la Puerta Dorada

Identity: `new-rome` / CDF-C04 / `CDF_NewRome`. Source locale `en`. Period 337–843 CE; missions 451–787.

Instituciones, ciudad y memoria del Imperio romano oriental; no una ortodoxia moderna fabricada en 325.

This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.

[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)

## Arc, inflection points and ending

843: restauración de imágenes como epílogo posterior a la misión de 787; etapas separadas 815/843 explícitas.

Recommended order is narrative, not always chronological: the successor may overlap or revisit earlier events; announce its own date.

The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.

| Scenario | Event / dramatic task | Map |
|---|---|---|
| [Across the Strait](scenarios/01-across-the-strait.md) | 451 CE / transported-delegations | 320 × 320 / chalcedon |
| [The City in Ashes](scenarios/02-the-city-in-ashes.md) | January 532 / urban-evacuation | 360 × 360 / constantinople |
| [The Empty Granary](scenarios/03-the-empty-granary.md) | 542 CE / crisis-logistics | 320 × 320 / constantinople |
| [Winter at the Walls](scenarios/04-winter-at-the-walls.md) | 717–718 CE / siege-and-supply | 400 × 400 / constantinople |
| [Pieces of a Memory](scenarios/05-pieces-of-a-memory.md) | 787 CE; interludes 815 and 843 / artifact-and-record-escort | 320 × 320 / nicaea |

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
  "cover": "Beyond the Golden Gate: Chalcedon and Bosporus, 451 CE; foreground Artesana de mosaicos y custodio de cuadernos de taller; no modern skyline or invented sacred portrait.",
  "portrait": "Fictional Anna, the Mosaic Restorer, occupational props, plain clothing without fabricated uniform; expression follows temperament. Label composite fictional narrator in credits.",
  "assets": [
    "theodosian-walls",
    "hagia-sophia",
    "iznik-lake"
  ],
  "delivery": "One cover, one narrator portrait, one context map per scenario; licensed or original PNG; no paid batch authorized."
}

## Predecessors and campaign screens

Static advice always appears in the description and intro. Conditional variants depend on verified SequenceItems conditions and profile persistence; unknown progress never blocks play. Selected routes set only their own progress key to 1. No cross-mod launch button is promised: show title and public identity, then return to the engine menu.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.new-rome.title` / always | none → next | Beyond the Golden Gate | Más allá de la Puerta Dorada |
| `campaign.new-rome.description` / always | none → next | 337–843 CE; missions 451–787. Follow Anna, the Mosaic Restorer through 5 scenarios. Each begins with a factual account, then a personal recollection. All campaigns can be played independently. | 337–843 CE; missions 451–787. Sigue a Anna, the Mosaic Restorer en 5 escenarios. Cada uno comienza con un relato de los hechos y después una memoria personal. Todas las campañas se pueden jugar de forma independiente. |
| `campaign.new-rome.voice-contract` / first intro | collection-narrator → next | The shared narrator gives the historical frame. The campaign narrator is a fictional person whose memories, songs and inherited accounts offer a situated perspective. Invented dialogue is never a historical quotation. | El narrador común presenta el marco histórico. El narrador de campaña es un personaje ficticio cuya memoria, cantares y relatos heredados ofrecen una perspectiva situada. Los diálogos inventados nunca son citas históricas. |
| `campaign.new-rome.personal-introduction` / after factual frame | anna-mosaicist → next | A wall keeps more than stones. Every repair tells me what someone before us chose to keep—or to erase. | Un muro conserva algo más que piedras. Cada reparación cuenta qué quiso alguien conservar, o borrar. |
| `campaign.new-rome.predecessor-advice` / always in mod description and opening; never a permission check | collection-narrator → next | Recommended first: The Eagle and the Cross (CDF-C01), eastern-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 451 CE, and may revisit an overlapping period. | Se recomienda jugar antes El águila y la cruz (CDF-C01), ruta eastern-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 451 CE y puede volver a un período solapado. |
| `campaign.new-rome.predecessor-missing` / required route progress.imperial-church.eastern-perspective is not >0, if native condition verified; otherwise static advice | collection-narrator → next | Recommended first: The Eagle and the Cross (CDF-C01), eastern-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 451 CE, and may revisit an overlapping period. | Se recomienda jugar antes El águila y la cruz (CDF-C01), ruta eastern-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 451 CE y puede volver a un período solapado. |
| `campaign.new-rome.predecessor-present` / progress.imperial-church.eastern-perspective>0 only when profile persistence verified | collection-narrator → next | Your earlier route in The Eagle and the Cross is remembered. Here we follow a new narrator and the documented events of 337–843 CE; missions 451–787. | Se recuerda tu ruta anterior en El águila y la cruz. Aquí seguimos a otro narrador y los hechos documentados de 337–843 CE; missions 451–787. |
| `campaign.new-rome.predecessor-other-route` / other route >0 and required route not >0; conditional encoding must be certified | collection-narrator → next | Recommended first: The Eagle and the Cross (CDF-C01), eastern-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 451 CE, and may revisit an overlapping period. | Se recomienda jugar antes El águila y la cruz (CDF-C01), ruta eastern-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 451 CE y puede volver a un período solapado. |
| `campaign.new-rome.predecessor-unknown` / progress unavailable, mod absent, profile reset or layout not certified | collection-narrator → next | Recommended first: The Eagle and the Cross (CDF-C01), eastern-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 451 CE, and may revisit an overlapping period. | Se recomienda jugar antes El águila y la cruz (CDF-C01), ruta eastern-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 451 CE y puede volver a un período solapado. |
| `campaign.new-rome.continue-completed` / victory selected completed; write only progress.new-rome.completed=1 | collection-narrator → collection catalogue | This campaign is complete. Your completed perspective is remembered. Recommended next: the parallel stories in the collection. There is no designated direct sequel in this catalogue. You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva completed. Continúa con los relatos paralelos de la colección. Este catálogo no incluye una continuación directa designada. También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.new-rome.predecessor-recap` / always before first scenario, skippable; same sufficient recap regardless of stored progress | collection-narrator → personal-introduction | The imperial story closed in337. We now follow the eastern capital and its region, beginning at Chalcedon in451 and ending in843. The narrator draws earlier episodes from records and later ones from her life. | La historia imperial cerró en337. Seguimos la capital oriental y su región, desde Calcedonia en451 hasta843. La narradora conoce los primeros episodios por registros y los últimos por su vida. |

## Historical source ledger

- [Council of Chalcedon](https://sourcebooks.web.fordham.edu/basis/chalcedon.asp): Definición y canon 28. Distinguir texto conciliar de comentario confesional del editor.
- [Procopius, Wars I.24](https://sourcebooks.web.fordham.edu/source/procop-wars1.asp): Insurrección Nika de 532. No tomar cifras de muertos como conteo moderno ni hacer la matanza un objetivo.
- [The Met, Byzantium (ca. 330–1453)](https://www.metmuseum.org/essays/byzantium-ca-330-1453): Períodos y cultura material. Ensayo de museo de síntesis, no plano arqueológico ni cronología militar completa.
- [Procopius, Wars II.22–23](https://sourcebooks.web.fordham.edu/source/542procopius-plague.asp): Constantinople in 542. Literary testimony; do not convert rhetorical mortality into a numerical simulation.
- [Harvard SoHP, Selected Draft Translations](https://sohp.fas.harvard.edu/selected-draft-translations): Procopius commentary. Consulted commentary; draft translations are not copied into this repository.
- [UNESCO, Historic Areas of Istanbul](https://whc.unesco.org/en/list/356/): Península, murallas y monumentos. Paisaje de varias épocas: filtrar fecha de cada edificio.
- [E. W. Brooks, The Campaign of 716–718, from Arabic Sources (1899)](https://www.cambridge.org/core/journals/journal-of-hellenic-studies/article/abs/campaign-of-716718-from-arabic-sources/7FA64C84BFD76CECFF0AB6C528D6C854): Published extract and source discussion. Only the accessible extract was consulted, not the paywalled full paper.
- [The Met, Iconoclasm](https://www.metmuseum.org/exhibitions/listings/2012/byzantium-and-islam/blog/topical-essays/posts/iconoclasm): Hieria 754, Nicea 787, reanudación 815, condena 843. Política y experiencia local no uniformes; no homogeneizar comunidades.
