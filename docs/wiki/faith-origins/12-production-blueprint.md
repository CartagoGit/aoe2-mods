# Embers of the Covenant / Las brasas de la alianza

Identity: `faith-origins` / CDF-C00 / `CDF_FaithOrigins`. Source locale `en`. Period c. 50–313 CE.

Redes de comunidades judías y cristianas dentro del Imperio; el judaísmo posee una historia muy anterior al primer escenario.

This blueprint supersedes earlier provisional story briefs where they differ. Earlier compatibility/approval evidence remains historical evidence, not proof that these new missions are implemented.

[Narrator bible](13-narrator-bible.md) · [shared design rules](../../design/production-contract.md) · [catalogue](../../design/README.md) · [handoff](../../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md)

## Arc, inflection points and ending

313: el cambio jurídico abre una etapa imperial; no acaba toda violencia ni comienza el judaísmo.

Recommended order is narrative, not always chronological: the successor may overlap or revisit earlier events; announce its own date.

The factual collection voice opens every scenario and every documented ending, then explicitly yields to the same campaign narrator. Changes of century are title-card interludes, not travel time on one map.

| Scenario | Event / dramatic task | Map |
|---|---|---|
| [Letters on the Orontes](scenarios/01-roads-of-antioch.md) | c. 50 CE / network-escort | 320 × 320 / antioch |
| [A Road Beyond the Walls](scenarios/02-after-the-siege.md) | 70 CE / civilian-evacuation | 320 × 320 / jerusalem |
| [The Governor’s Question](scenarios/03-the-governors-question.md) | c. 112 CE / administrative-intrigue | 300 × 300 / bithynia |
| [A Different Dawn](scenarios/04-a-different-dawn.md) | 303–313 CE / supply-and-testimony | 320 × 320 / milan |

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
  "cover": "Embers of the Covenant: Antioch and Orontes, c. 50 CE; foreground Copista y administradora de un archivo familiar; no modern skyline or invented sacred portrait.",
  "portrait": "Fictional Miriam of Caesarea, occupational props, plain clothing without fabricated uniform; expression follows temperament. Label composite fictional narrator in credits.",
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
| `campaign.faith-origins.title` / always | none → next | Embers of the Covenant | Las brasas de la alianza |
| `campaign.faith-origins.description` / always | none → next | c. 50–313 CE. Follow Miriam of Caesarea through 4 scenarios. Each begins with a factual account, then a personal recollection. All campaigns can be played independently. | c. 50–313 CE. Sigue a Miriam of Caesarea en 4 escenarios. Cada uno comienza con un relato de los hechos y después una memoria personal. Todas las campañas se pueden jugar de forma independiente. |
| `campaign.faith-origins.voice-contract` / first intro | collection-narrator → next | The shared narrator gives the historical frame. The campaign narrator is a fictional person whose memories, songs and inherited accounts offer a situated perspective. Invented dialogue is never a historical quotation. | El narrador común presenta el marco histórico. El narrador de campaña es un personaje ficticio cuya memoria, cantares y relatos heredados ofrecen una perspectiva situada. Los diálogos inventados nunca son citas históricas. |
| `campaign.faith-origins.personal-introduction` / after factual frame | miriam-archive → next | My grandmother kept letters, not armies. I learned to read the gaps between them. | Mi abuela guardaba cartas, no ejércitos. Aprendí a leer los huecos entre ellas. |
| `campaign.faith-origins.independent-entry` / always | collection-narrator → next | You may begin here. Dates on each scenario distinguish events from later memories. No earlier campaign is required. | Puedes empezar aquí. Las fechas de cada escenario distinguen los hechos de las memorias posteriores. No necesitas una campaña anterior. |
| `campaign.faith-origins.continue-christian-perspective` / victory selected christian-perspective; write only progress.faith-origins.christian-perspective=1 | collection-narrator → imperial-church | This campaign is complete. Your christian-perspective perspective is remembered. Recommended next: The Eagle and the Cross (CDF-C01; begins 28 October 312). You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva christian-perspective. Continúa con El águila y la cruz (CDF-C01; comienza en 28 October 312). También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |
| `campaign.faith-origins.continue-jewish-perspective` / victory selected jewish-perspective; write only progress.faith-origins.jewish-perspective=1 | collection-narrator → jewish-tradition | This campaign is complete. Your jewish-perspective perspective is remembered. Recommended next: Keepers of the Unbroken Word (CDF-C02; begins 70 CE). You can also replay another perspective; previous choices remain recorded. | Esta campaña ha terminado. Se recuerda tu perspectiva jewish-perspective. Continúa con Guardianes de la palabra viva (CDF-C02; comienza en 70 CE). También puedes rejugar otra perspectiva; se conservan las elecciones anteriores. |

## Historical source ledger

- [Eusebius, Church History III](https://www.newadvent.org/fathers/250103.htm): III.5: tradición de Pella; testimonio posterior. La narración de la huida a Pella no acredita la ruta ni a todos los habitantes.
- [Acts 11, consulted multilingual text](https://www.newadvent.org/bible/act011.htm): 11.19–30: Antioch community and aid narrative. Religious literary testimony, not proof of our courier names, exact date or route.
- [Pliny and Trajan, Letters 10.96–97](https://sourcebooks.web.fordham.edu/ancient/pliny-trajan1.asp): Preguntas del gobernador y respuesta imperial. Dos cartas no prueban una persecución uniforme durante tres siglos.
- [Eusebius, Church History VIII](https://www.newadvent.org/fathers/250108.htm): VIII.2: persecución; contextualización situada. Autor cristiano; no generalizar experiencia local a todas las provincias.
- [Lactantius, On the Deaths of the Persecutors](https://www.newadvent.org/fathers/0705.htm): 44: Milvio; 48: disposiciones de 313. El sueño es testimonio religioso; no convertirlo en buff sobrenatural.
