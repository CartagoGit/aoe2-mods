# From Damascus to the Far Horizon / De Damasco al último horizonte

Identity: `umayyads` / CDF-I02 / `CDF_Umayyads`. Source locale `en`. Period 661–750 CE.

Administración, obras y expansión de un imperio diverso; el final omeya de 750 no acaba su linaje ni inaugura homogeneidad social.

This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.

[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)

## Arc, inflection points and ending

750: caída del poder omeya de Damasco; epílogo a 756 menciona continuidad andalusí sin campaña inventada ya disponible.

Recommended order is narrative, not always chronological: the successor may overlap or revisit earlier events; announce its own date.

The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.

| Scenario | Event / dramatic task | Map |
|---|---|---|
| [Ledgers of Damascus](scenarios/01-ledgers-of-damascus.md) | 661 CE / administration-and-supply | 360 × 360 / damascus |
| [Stone and Memory](scenarios/02-stone-and-memory.md) | 691/692 CE / civic-construction | 320 × 320 / jerusalem |
| [The Western Shore](scenarios/03-the-western-shore.md) | 698 CE / port-withdrawal | 400 × 400 / carthage |
| [The Narrow Sea](scenarios/04-the-narrow-sea.md) | 711 CE / amphibious-supply | 400 × 400 / gibraltar |
| [The Last Crossing](scenarios/05-the-last-crossing.md) | 750 CE / army-withdrawal | 400 × 400 / zab |

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
  "cover": "From Damascus to the Far Horizon: Damascus / Ghouta, 661 CE; foreground Mercader de tejidos y portador de cuentas entre talleres; no modern skyline or invented sacred portrait.",
  "portrait": "Fictional Yasir, the Cloth Merchant, occupational props, plain clothing without fabricated uniform; expression follows temperament. Label composite fictional narrator in credits.",
  "assets": [
    "damascus-mosque",
    "dome-rock",
    "yarmuk-valley"
  ],
  "delivery": "One cover, one narrator portrait, one context map per scenario; licensed or original PNG; no paid batch authorized."
}

## Predecessors and campaign screens

Static advice always appears in the description and intro. Conditional variants depend on verified SequenceItems conditions and profile persistence; unknown progress never blocks play. Selected routes set only their own progress key to 1. No cross-mod launch button is promised: show title and public identity, then return to the engine menu.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.umayyads.title` / always | none → next | From Damascus to the Far Horizon | De Damasco al último horizonte |
| `campaign.umayyads.description` / always | none → next | 661–750 CE. Follow Yasir, the Cloth Merchant through 5 scenarios. Each begins with a factual account, then a personal recollection. All campaigns can be played independently. | 661–750 CE. Sigue a Yasir, the Cloth Merchant en 5 escenarios. Cada uno comienza con un relato de los hechos y después una memoria personal. Todas las campañas se pueden jugar de forma independiente. |
| `campaign.umayyads.voice-contract` / first intro | collection-narrator → next | The shared narrator gives the historical frame. The campaign narrator is a fictional person whose memories, songs and inherited accounts offer a situated perspective. Invented dialogue is never a historical quotation. | El narrador común presenta el marco histórico. El narrador de campaña es un personaje ficticio cuya memoria, cantares y relatos heredados ofrecen una perspectiva situada. Los diálogos inventados nunca son citas históricas. |
| `campaign.umayyads.personal-introduction` / after factual frame | yasir-cloth-merchant → next | My first map was a list of debts. The empire looked boundless until I learned how far a promise could travel before it broke. | Mi primer mapa era una lista de deudas. El imperio parecía no tener límite hasta que aprendí cuán lejos podía viajar una promesa antes de romperse. |
| `campaign.umayyads.predecessor-advice` / always in mod description and opening; never a permission check | collection-narrator → next | Recommended first: The Shattered Oath (CDF-I01), muawiya-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 661 CE, and may revisit an overlapping period. | Se recomienda jugar antes El juramento quebrado (CDF-I01), ruta muawiya-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 661 CE y puede volver a un período solapado. |
| `campaign.umayyads.predecessor-missing` / required route progress.first-fitna.muawiya-perspective is not >0, if native condition verified; otherwise static advice | collection-narrator → next | Recommended first: The Shattered Oath (CDF-I01), muawiya-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 661 CE, and may revisit an overlapping period. | Se recomienda jugar antes El juramento quebrado (CDF-I01), ruta muawiya-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 661 CE y puede volver a un período solapado. |
| `campaign.umayyads.predecessor-present` / progress.first-fitna.muawiya-perspective>0 only when profile persistence verified | collection-narrator → next | Your earlier route in The Shattered Oath is remembered. Here we follow a new narrator and the documented events of 661–750 CE. | Se recuerda tu ruta anterior en El juramento quebrado. Aquí seguimos a otro narrador y los hechos documentados de 661–750 CE. |
| `campaign.umayyads.predecessor-other-route` / other route >0 and required route not >0; conditional encoding must be certified | collection-narrator → next | Recommended first: The Shattered Oath (CDF-I01), muawiya-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 661 CE, and may revisit an overlapping period. | Se recomienda jugar antes El juramento quebrado (CDF-I01), ruta muawiya-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 661 CE y puede volver a un período solapado. |
| `campaign.umayyads.predecessor-unknown` / progress unavailable, mod absent, profile reset or layout not certified | collection-narrator → next | Recommended first: The Shattered Oath (CDF-I01), muawiya-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 661 CE, and may revisit an overlapping period. | Se recomienda jugar antes El juramento quebrado (CDF-I01), ruta muawiya-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 661 CE y puede volver a un período solapado. |
| `campaign.umayyads.continue-completed` / victory selected completed; write only progress.umayyads.completed=1 | collection-narrator → collection catalogue | This campaign is complete. Your completed perspective is remembered. Recommended next: the parallel stories in the collection. There is no designated direct sequel in this catalogue. You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva completed. Continúa con los relatos paralelos de la colección. Este catálogo no incluye una continuación directa designada. También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.umayyads.predecessor-recap` / always before first scenario, skippable; same sufficient recap regardless of stored progress | collection-narrator → personal-introduction | The earlier conflict led to the settlement of661. Following the Syrian archive now traces Umayyad government, construction, expansion and the eastern dynasty’s ending in750. The personal voice is a later family merchant, not a witness to every reign. | El conflicto anterior llevó al acuerdo de661. El archivo sirio sigue gobierno, construcción, expansión y el final oriental de la dinastía en750. La voz personal es un mercader familiar posterior, no testigo de todos los reinados. |

## Historical source ledger

- [The Met, Art of the Umayyad Period](https://www.metmuseum.org/essays/the-art-of-the-umayyad-period-661-750): Dinastía y arquitectura. Referencia material; una construcción no mide la fe de sus habitantes.
- [The Met, Byzantium and Islam](https://www.metmuseum.org/exhibitions/listings/2012/byzantium-and-islam): Transformaciones regionales siglos VII–IX. Panorama y objetos; evitar presentarlo como explicación causal exhaustiva.
- [The Cambridge Medieval History II (1913), p. 370](https://en.wikisource.org/wiki/Page:Bury_J_B_The_Cambridge_Medieval_History_Vol_2_1913.djvu/398): Carthage naval reversal in 698. Older scholarship: use narrow chronology only; reject its colonial generalisations and ethnic causal claims.
- [Ibn Abd al-Hakam, Conquest of Spain](https://sourcebooks.web.fordham.edu/source/conqspain.asp): Strait crossing, late account. Ninth-century testimony; editorial introduction erroneously places Muslim expansion in sixth century. No hostage legend or exact army numbers reused.
- [José Beneroso Santos, dissertation (UNED, 2023)](https://portalcientifico.uned.es/documentos/647a293431258e1eec95307e): Accessible abstract: geography and proposed reinterpretation. Abstract only; proposed battle placement is not consensus and is not used as a surveyed battlefield.
- [C. E. Bosworth, Abbasid Caliphate](https://www.iranicaonline.org/articles/abbasid-caliphate/): Establishment in 750. Supports dynastic transition; does not authenticate our tactical retreat, camp coordinates or unit counts.
- [El-Hussein A. Y. Aly, The Graeco-Arabic Translation Movement, publisher excerpt](https://assets.cambridge.org/97810093/85602/excerpt/9781009385602_excerpt.pdf): Introduction, historical Umayyad context: Great Zab750. Accessible publisher excerpt downloaded temporarily and read, not whole monograph. Narrow chronology only; deployments remain fictional.
