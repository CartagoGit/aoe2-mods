# Keepers of the Unbroken Word / Guardianes de la palabra viva

Identity: `jewish-tradition` / CDF-C02 / `CDF_JewishTradition`. Source locale `en`. Period 70–c. 425 CE.

Continuidad, estudio y diversidad de comunidades judías tras 70; jamás una rama que nazca al abandonar el cristianismo.

This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.

[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)

## Arc, inflection points and ending

c. 425: cierre editorial del volumen, no desaparición de comunidades ni fecha segura de cierre del Talmud.

Recommended order is narrative, not always chronological: the successor may overlap or revisit earlier events; announce its own date.

The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.

| Scenario | Event / dramatic task | Map |
|---|---|---|
| [A City of Names](scenarios/01-a-city-of-names.md) | 70 CE / rescue-and-records | 320 × 320 / jerusalem |
| [The Hill and the School](scenarios/02-the-hill-and-the-school.md) | c. 200 CE / archive-economy | 320 × 320 / galilee |
| [The River Quarter](scenarios/03-the-river-quarter.md) | c. 244 CE / district-trade | 320 × 320 / dura |
| [The Living Margin](scenarios/04-the-living-margin.md) | c. 400–425 CE / distributed-preservation | 360 × 360 / galilee |

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
  "cover": "Keepers of the Unbroken Word: Jerusalem and approaches, 70 CE; foreground Copista de cartas de familias y cuentas de viajeros; no modern skyline or invented sacred portrait.",
  "portrait": "Fictional Judith of Tiberias, occupational props, plain clothing without fabricated uniform; expression follows temperament. Label composite fictional narrator in credits.",
  "assets": [
    "dura-synagogue",
    "dura-plan"
  ],
  "delivery": "One cover, one narrator portrait, one context map per scenario; licensed or original PNG; no paid batch authorized."
}

## Predecessors and campaign screens

Static advice always appears in the description and intro. Conditional variants depend on verified SequenceItems conditions and profile persistence; unknown progress never blocks play. Selected routes set only their own progress key to 1. No cross-mod launch button is promised: show title and public identity, then return to the engine menu.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.jewish-tradition.title` / always | none → next | Keepers of the Unbroken Word | Guardianes de la palabra viva |
| `campaign.jewish-tradition.description` / always | none → next | 70–c. 425 CE. Follow Judith of Tiberias through 4 scenarios. Each begins with a factual account, then a personal recollection. All campaigns can be played independently. | 70–c. 425 CE. Sigue a Judith of Tiberias en 4 escenarios. Cada uno comienza con un relato de los hechos y después una memoria personal. Todas las campañas se pueden jugar de forma independiente. |
| `campaign.jewish-tradition.voice-contract` / first intro | collection-narrator → next | The shared narrator gives the historical frame. The campaign narrator is a fictional person whose memories, songs and inherited accounts offer a situated perspective. Invented dialogue is never a historical quotation. | El narrador común presenta el marco histórico. El narrador de campaña es un personaje ficticio cuya memoria, cantares y relatos heredados ofrecen una perspectiva situada. Los diálogos inventados nunca son citas históricas. |
| `campaign.jewish-tradition.personal-introduction` / after factual frame | judith-copyist → next | A damaged line is still a line. I copy it with the gap intact, so that no one mistakes my guess for another person’s word. | Una línea dañada sigue siendo una línea. La copio con su hueco, para que nadie confunda mi suposición con palabras ajenas. |
| `campaign.jewish-tradition.predecessor-advice` / always in mod description and opening; never a permission check | collection-narrator → next | Recommended first: Embers of the Covenant (CDF-C00), jewish-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 70 CE, and may revisit an overlapping period. | Se recomienda jugar antes Las brasas de la alianza (CDF-C00), ruta jewish-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 70 CE y puede volver a un período solapado. |
| `campaign.jewish-tradition.predecessor-missing` / required route progress.faith-origins.jewish-perspective is not >0, if native condition verified; otherwise static advice | collection-narrator → next | Recommended first: Embers of the Covenant (CDF-C00), jewish-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 70 CE, and may revisit an overlapping period. | Se recomienda jugar antes Las brasas de la alianza (CDF-C00), ruta jewish-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 70 CE y puede volver a un período solapado. |
| `campaign.jewish-tradition.predecessor-present` / progress.faith-origins.jewish-perspective>0 only when profile persistence verified | collection-narrator → next | Your earlier route in Embers of the Covenant is remembered. Here we follow a new narrator and the documented events of 70–c. 425 CE. | Se recuerda tu ruta anterior en Las brasas de la alianza. Aquí seguimos a otro narrador y los hechos documentados de 70–c. 425 CE. |
| `campaign.jewish-tradition.predecessor-other-route` / other route >0 and required route not >0; conditional encoding must be certified | collection-narrator → next | Recommended first: Embers of the Covenant (CDF-C00), jewish-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 70 CE, and may revisit an overlapping period. | Se recomienda jugar antes Las brasas de la alianza (CDF-C00), ruta jewish-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 70 CE y puede volver a un período solapado. |
| `campaign.jewish-tradition.predecessor-unknown` / progress unavailable, mod absent, profile reset or layout not certified | collection-narrator → next | Recommended first: Embers of the Covenant (CDF-C00), jewish-perspective. It explains the earlier setting. You can continue now; a recap follows. This campaign begins in 70 CE, and may revisit an overlapping period. | Se recomienda jugar antes Las brasas de la alianza (CDF-C00), ruta jewish-perspective. Explica los antecedentes. Puedes continuar ahora; verás una recapitulación. Esta campaña comienza en 70 CE y puede volver a un período solapado. |
| `campaign.jewish-tradition.continue-completed` / victory selected completed; write only progress.jewish-tradition.completed=1 | collection-narrator → collection catalogue | This campaign is complete. Your completed perspective is remembered. Recommended next: the parallel stories in the collection. There is no designated direct sequel in this catalogue. You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva completed. Continúa con los relatos paralelos de la colección. Este catálogo no incluye una continuación directa designada. También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.jewish-tradition.predecessor-recap` / always before first scenario, skippable; same sufficient recap regardless of stored progress | collection-narrator → personal-introduction | The earlier Jewish perspective introduces continuity within diverse imperial communities. This campaign returns to70 and follows transmission in Galilee and Dura; it does not place the origin of Judaism in that year. | La perspectiva judía anterior introduce continuidad entre comunidades diversas del imperio. Esta campaña vuelve a70 y sigue la transmisión en Galilea y Dura; no sitúa el origen del judaísmo en ese año. |

## Historical source ledger

- [Eusebius, Church History III](https://www.newadvent.org/fathers/250103.htm): III.5: tradición de Pella; testimonio posterior. La narración de la huida a Pella no acredita la ruta ni a todos los habitantes.
- [UNESCO, Necropolis of Bet Shearim](https://whc.unesco.org/en/list/1471/): Contexto de renovación judía y Judá el Príncipe. Necrópolis y transmisión cultural, no prueba de una aventura del protagonista.
- [Jewish Encyclopedia, Judah I](https://jewishencyclopedia.com/articles/8963-judah-i): Redaction and limits of attribution. Older scholarship; redactor rather than sole author. The precise form and moment of redaction remain qualified.
- [Encyclopaedia Iranica, Dura Europos](https://www.iranicaonline.org/articles/dura-europos/): Emplazamiento y arqueología. Ciudad en margen derecha del Éufrates; no proyectar la ciudad contemporánea.
- [UNESCO, Mari & Europos-Dura](https://whc.unesco.org/en/tentativelists/5702/): Emplazamiento y edificios de cultos. Es lista indicativa, no inscripción de Patrimonio Mundial.
- [Wilhelm Bacher, Talmud (Jewish Encyclopedia)](https://www.jewishencyclopedia.com/articles/14213-talmud): Palestinian Talmud and Date of Redaction sections. Older synthesis; competing stages/redactions must not become an exact universally agreed closing date.
