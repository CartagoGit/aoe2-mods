# Beyond the Golden Gate / Más allá de la Puerta Dorada

`new-rome` · CDF-C04 · 32 selected episodes · source locale`en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

```json
{
  "editorial": {
    "campaignTitle": {
      "en": "Beyond the Golden Gate",
      "es-ES": "Más allá de la Puerta Dorada"
    },
    "publicId": "CDF-C04",
    "internalName": "CDF_NewRome",
    "sourceLocale": "en",
    "targetEpisodeCount": 32,
    "narratorId": "anna-mosaicist",
    "personaLens": {
      "en": "Materials, repairs and workshop traditions",
      "es-ES": "Materiales, reparaciones y tradiciones de taller"
    },
    "deliveryTone": {
      "en": "sensory patience, anger held in check",
      "es-ES": "paciencia sensorial, rabia contenida"
    },
    "sequence": [
      {
        "speaker": "collection-narrator",
        "mode": "sober source-qualified historical fact",
        "causePolicy": "attribute motives, miracles and sectarian judgements to their sources; no single moral or theological verdict"
      },
      {
        "speaker": "anna-mosaicist",
        "mode": "fictional personal interpretation with explicit witness basis"
      }
    ],
    "baselineSemanticIdsPreserved": [
      "01-across-the-strait",
      "02-the-city-in-ashes",
      "03-the-empty-granary",
      "04-winter-at-the-walls",
      "05-pieces-of-a-memory"
    ],
    "orderingPolicy": "order is a separate integer; existing semantic IDs and public/progress IDs remain stable",
    "progressPolicy": "only the actual final odyssey episode offers terminal route write; every former last baseline mission becomes nonterminal when followed by new episodes",
    "sourceAuditStatus": "candidate chronologies reviewed for errors; individual episode historical approval pending",
    "coreMechanicPolicy": "at least four mission-core families in each odyssey; no more than two consecutive identical core families without authored reason; side-objective variety does not excuse identical main missions",
    "selectedEpisodeCount": 32,
    "selectionNotes": [
      "Act counts are subordinate to source chronology and are not filler quotas.",
      "Scene location fixes the local player adventure; remote event claims remain explicitly off-map reports.",
      "Repeated core families require episode-specific world layout, counts and choice tradeoffs before authoring assignment.",
      "Archaeology is dated by phases; a modern artifact is not proof of a precise ancient dedication date."
    ]
  },
  "continuity": {
    "recommendedPrevious": [
      {
        "campaignId": "imperial-church",
        "route": "eastern-perspective"
      }
    ],
    "nextRoutes": [
      {
        "id": "completed",
        "key": "progress.new-rome.completed",
        "next": null
      }
    ],
    "chronologyWarning": "Any predecessor-dependent campaign remains independently playable; show recommendation and recap, preserve all route keys, and disclose overlap when changing perspective.",
    "terminalScreenRule": "show successor English/Spanish title plus public ID for the chosen route; no automatic launching and no requirement lock",
    "proceedWithoutPredecessor": true
  }
}
```

Only the final expanded episode may complete this campaign or present the successor recommendation. Former baseline finales become intermediate episodes when later episodes exist. Preserve every existing semantic scenario ID; display order is a separate field.

## act-1: Heirs of the Eastern Gate / Herederos de la puerta oriental

Historical year band: [337, 438]. La capital recibe sucesión y nuevas instituciones;330 es recap contextual, no misión del periodo337–843.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 1 / 01-administrative-transition-constantinople | The Gate after Its Founder / La puerta tras su fundador | 337 CE; Nicomedia death reported | constantinople | administrative-transition |
| 2 / 02-council-and-city-logistics-constantinople | The City's Place in the Canon / El lugar de la ciudad en el canon | 381 CE | constantinople | council-and-city-logistics |
| 3 / 03-competing-dispatches-constantinople | Two Courts beneath One Memory / Dos cortes bajo una memoria | 395 CE; deathMilan off-map | constantinople | competing-dispatches |
| 4 / 04-civilian-refuge-and-dispatch-constantinople | The Bishop Who Was Sent Away / El obispo al que alejaron | 404 CE | constantinople | civilian-refuge-and-dispatch |
| 5 / 05-finite-school-works-constantinople | Rooms for the Written Word / Salas para la palabra escrita | 425 CE; school institution, not modern university | constantinople | finite-school-works |
| 6 / 06-separate-session-logistics-ephesus | Before the Delegates Arrived / Antes de que llegaran los delegados | 431 CE | ephesus | separate-session-logistics |
| 7 / 07-ceremony-and-household-logistics-constantinople | A Return after the Exile / Un regreso después del exilio | 438 CE; relics transfer | constantinople | ceremony-and-household-logistics |
| 8 / 08-distributed-record-collation-constantinople | The Law Gathered into Books / La ley reunida en libros | 438 CE; publication/439effective distinguished | constantinople | distributed-record-collation |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.63,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 0.76,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 0.9,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## act-2: The Council and the City / El concilio y la ciudad

Historical year band: [451, 553]. Calcedonia, cortes, Nika, reconstrucción y peste; la voz objetiva contextualiza los sesgos de las crónicas.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 9 / 01-across-the-strait | Across the Strait / Al otro lado del estrecho | 451 CE | chalcedon | delegate-and-ferry-logistics |
| 10 / 10-ceremony-route-and-provision-constantinople | The Emperor at the City's Edge / El emperador en el límite de la ciudad | 457 CE | constantinople | ceremony-route-and-provision |
| 11 / 11-disputed-correspondence-constantinople | A Letter That Could Not Unite / Una carta que no pudo unir | 482 CE | constantinople | disputed-correspondence |
| 12 / 12-administrative-transition-constantinople | One Seal after Two Emperors / Un sello tras dos emperadores | 1 August527 CE; co-rule sinceApril | constantinople | administrative-transition |
| 13 / 02-the-city-in-ashes | The City in Ashes / La ciudad entre cenizas | January532 CE | constantinople | civilian-evacuation-under-unrest |
| 14 / 14-finite-construction-logistics-constantinople | Stone beneath the Great Dome / Piedra bajo la gran cúpula | 532–537 CE; dedication537 | constantinople | finite-construction-logistics |
| 15 / 15-bounded-civilian-extraction-antioch | The Orontes after the Flames / El Orontes después de las llamas | 540 CE | antioch | bounded-civilian-extraction |
| 16 / 03-the-empty-granary | The Empty Granary / El granero vacío | 542 CE | constantinople | care-and-food-allocation |
| 17 / 17-council-record-comparison-constantinople | The Chapters on the Table / Los capítulos sobre la mesa | 553 CE | constantinople | council-record-comparison |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.71,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 0.82,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 0.95,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## act-3: Grain Beneath the Siege / Grano bajo el asedio

Historical year band: [626, 718]. Asedios y cambios de soberanía regional;674–678 es marco discutido, no certeza táctica año por año.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 18 / 18-finite-siege-and-ferry-supply-constantinople | A City between Two Armies / Una ciudad entre dos ejércitos | 626 CE | constantinople | finite-siege-and-ferry-supply |
| 19 / 19-civilian-record-and-property-logistics-jerusalem | News from the Holy City / Noticias desde la ciudad santa | 637/638 CE; capitulation reports qualified | jerusalem | civilian-record-and-property-logistics |
| 20 / 20-coastal-watch-and-bounded-convoy-constantinople | Ships in the Uncertain Years / Barcos en los años inciertos | c.674–678 CE; continuous siege disputed | constantinople | coastal-watch-and-bounded-convoy |
| 21 / 21-delegation-and-text-comparison-constantinople | Eighteen Sessions by the Palace / Dieciocho sesiones junto al palacio | 680–681 CE | constantinople | delegation-and-text-comparison |
| 22 / 04-winter-at-the-walls | Winter at the Walls / Invierno junto a las murallas | 717–718 CE | constantinople | finite-winter-siege-and-supply |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.79,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 0.88,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 1.0,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## act-4: Images at the Edge / Imágenes en el límite

Historical year band: [726, 787]. Cronología de políticas iconoclastas incierta, posiciones diversas y Nicea787; Anna recuerda su oficio sin hablar por todos.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 23 / 23-artisan-record-and-protection-constantinople | An Image beneath the Orders / Una imagen bajo las órdenes | c.726–730 CE; policy chronology disputed | constantinople | artisan-record-and-protection |
| 24 / 24-council-and-workshop-logistics-chalcedon | The Assembly at Hieria / La asamblea en Hieria | 754 CE; reconstructed from later opposing acts | chalcedon | council-and-workshop-logistics |
| 25 / 05-pieces-of-a-memory | Pieces of a Memory / Fragmentos de una memoria | 787 CE; former843epilogue now separatefinale | nicaea | restoration-and-council-logistics |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.87,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 0.94,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 1.05,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## act-5: The Mosaic Restored / El mosaico restaurado

Historical year band: [797, 843]. Cortes y guerras hasta815y843; noticias de800llegan desde Roma, no son vivencia de Anna allí.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 26 / 26-civilian-supply-and-succession-records-constantinople | The Court under Irene / La corte bajo Irene | 797 CE | constantinople | civilian-supply-and-succession-records |
| 27 / 27-off-map-dispatch-and-comparison-constantinople | A Crown beyond the Western Sea / Una corona más allá del mar occidental | 800 CE; crowningRome off-map | constantinople | off-map-dispatch-and-comparison |
| 28 / 28-administrative-transition-constantinople | The Seal That Changed Hands / El sello que cambió de manos | 802 CE | constantinople | administrative-transition |
| 29 / 29-finite-withdrawal-and-relief-pliska | The Roads below Pliska / Los caminos bajo Pliska | 811 CE; battle-site footprint uncertain | pliska | finite-withdrawal-and-relief |
| 30 / 30-civilian-refuge-and-dispatch-adrianople | A Report from the Thracian Field / Un parte desde el campo tracio | 813 CE; Versinikia regional location uncertain | adrianople | civilian-refuge-and-dispatch |
| 31 / 31-artisan-and-archive-preservation-constantinople | The Covered Workshop / El taller cubierto | 815 CE | constantinople | artisan-and-archive-preservation |
| 32 / 32-restoration-and-final-perspective-constantinople | The Mosaic Returned / El mosaico restituido | 843 CE | constantinople | restoration-and-final-perspective |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.95,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 1.0,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 1.1,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## Episode source and knowledge ledger

### 1. The Gate after Its Founder

[Candidate source](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.64

Research candidate (not yet approved narration): Muerte de Constantino; sus hijos heredan el imperio y la capital oriental.

La capitalidad se consolida gradualmente.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/25024.htm): Eusebius, Vita Constantini IV.64 (cierre de la vida y muerte de Constantino).

Constantino murió en 337 y sus hijos heredaron.

Limit: Pasaje es panegírico y registra muerte; sucesión compartida debe contrastarse con cronología imperial independiente. URL correcta para Book IV.64.

Coverage: Página primaria abrió correctamente; encabezamiento y localizador IV.64 identificados, pero el párrafo exacto no fue extraído en esta pasada.

### 2. The City's Place in the Canon

[Candidate source](https://www.papalencyclicals.net/councils/ecum02.htm): Credo y cánones del Concilio de Constantinopla I; la página señala el problema de la transmisión del credo y el estatus inicialmente limitado del concilio.

Research candidate (not yet approved narration): Un concilio en Constantinopla reafirma la fe nicena, trata controversias sobre el Espíritu y fija en canon 3 la precedencia honorífica del obispo de Constantinopla después de Roma.

El credo conocido como niceno-constantinopolitano se atestigua textualmente en Calcedonia (451); no atribuir sin reservas toda su forma conservada a actas contemporáneas de 381. El canon 3 trata rango, no una división moderna entre católicos y ortodoxos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.papalencyclicals.net/councils/ecum02.htm): Constantinople I: canon 3; creed and canons, but status/transmission caveat

The source text supports a council traditionally dated 381 and canon 3 giving Constantinople honor after Rome because it is New Rome; creed transmission/history is separate from these canons.

Limit: Canon 3 does not establish papal/imperial jurisdiction or later East-West schism. Page is a compiled translation; it acknowledges transmission complexity.

Coverage: Opened council page and checked canon 3 and creed section; not manuscript apparatus.

### 3. Two Courts beneath One Memory

[Candidate source](https://www.britannica.com/biography/Theodosius-I): Chronology and overview

Research candidate (not yet approved narration): Muerte de Teodosio I precede división administrativa duradera entre cortes oriental y occidental.

No hubo división legal absoluta del imperio en ese momento.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 4. The Bishop Who Was Sent Away

[Candidate source](https://www.newadvent.org/fathers/1912.htm): Palladius, Dialogue on the Life of John Chrysostom

Research candidate (not yet approved narration): Juan Crisóstomo es depuesto y exiliado tras conflicto de corte y episcopado.

Fuente pro-Crisóstomo.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.tertullian.org/fathers/palladius_dialogus_02_text.htm): Palladius, Dialogue on the Life of John Chrysostom, chapter/section “Chrysostom’s Second Expulsion” (site text around lines 187–202)

Supports armed force expelling Chrysostom and clergy from Constantinople and putting him on a ship at night; event belongs to 404 chronology.

Limit: Palladius writes a partisan defense of Chrysostom and is not neutral; the passage narrates violence but does not itself provide a precise calendar date. Original New Advent URL was unrelated Chrysostom homily, not Palladius.

Coverage: Opened translation and read expulsion passages around text lines 187–202; limited extract, not the full dialogue.

### 5. Rooms for the Written Word

[Candidate source](https://www.britannica.com/topic/University-of-Constantinople): Codex Theodosianus 14.9.3

Research candidate (not yet approved narration): Teodosio II funda la universidad imperial de Constantinopla, fortaleciendo educación jurídica y literaria.

Las instituciones enseñaban materias variadas, no universidad moderna.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.forum.thelatinlibrary.com/theodosius/theod14.shtml): Codex Theodosianus 14.9.3, praescriptio and main provision (27 Feb 425)

Supports Theodosius II and Valentinian regulating an imperial auditorium at the Capitolium, specifying appointed Latin/Greek rhetors and grammarians plus philosophy and law teachers.

Limit: Does not support a modern “university foundation” claim. Better describe regulation/organization of imperial public teaching. Latin text dates 3 days before Kalends of March, Constantinople, consuls Theodosius XI and Valentinian.

Coverage: Read search-result excerpt of CTh 14.9.3 including staff list/dateline; direct HTML open failed, so accessibility/passages should be rechecked.

### 6. Before the Delegates Arrived

[Candidate source](https://sourcebooks.web.fordham.edu/basis/ephesus.asp): Actas del Concilio de Éfeso, sesión I y documentos asociados; traducción NPNF alojada por Fordham. Para caracterización académica consultada: https://www.cambridge.org/core/books/abs/cambridge-edition-of-early-christian-writings/acts-of-the-council-of-ephesus-juneoctober-431-selected-proceedings/B4E8190281A0B2F93C0B80DCE8537ED5.

Research candidate (not yet approved narration): El concilio reunido en Éfeso depone a Nestorio tras una disputa cristológica y eclesiopolítica entre las redes de Alejandría y Antioquía; la delegación de Juan de Antioquía llega después y celebra una asamblea rival.

Las actas preservan la perspectiva de las facciones participantes; el grupo de Cirilo inició la sesión antes de la llegada de Juan de Antioquía. Evitar presentarlo como consenso pacífico y unánime.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 7. A Return after the Exile

[Candidate source](https://www.newadvent.org/fathers/26017.htm): Socrates Scholasticus, Ecclesiastical History VII.45; encabezado del capítulo y consulado de Teodosio.

Research candidate (not yet approved narration): Las reliquias de Juan Crisóstomo son trasladadas desde Comana a Constantinopla y depositadas en la iglesia de los Santos Apóstoles.

Socrates escribe en el siglo V y es una fuente eclesiástica; la transferencia ocurrió décadas después de su muerte en 407.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/26017.htm): Socrates Scholasticus, Church History VII.45.

En 438 los restos de Juan Crisóstomo fueron trasladados de Comana y recibidos en Constantinopla.

Limit: Corregido respecto a 410: el traslado fue en 438. Debe distinguirse la fecha del exilio/muerte (407) de la traslación. Socrates escribe retrospectivamente.

Coverage: Socrates Scholasticus HE VII.45 abierto y leído (líneas 333–336): da el traslado desde Comana a Constantinopla, 27 de enero en el 16.º consulado de Teodosio; la equivalencia moderna es 438.

### 8. The Law Gathered into Books

[Candidate source](https://sourcebooks.fordham.edu/source/codex-theod.asp): Codex Theodosianus, edicto de publicación

Research candidate (not yet approved narration): Se publica el Codex Theodosianus, compilación legal imperial.

Selección oficial de constituciones.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://la.wikisource.org/wiki/Theodosii_novellae/1): Theodosian Novella 1, De Theodosiani codicis auctoritate (Feb 438); Bibliotheca legum chronology

Supports the Code receiving imperial authority/promulgation in February 438; academic legal reference gives effective date 1 Jan 439.

Limit: Do not conflate promulgation in 438 with entry into force in 439; East/West legal reception varied. Original Fordham page should be consulted directly before relying on its exact translation.

Coverage: Read Novella 1 search/index extract and University of Cologne Bibliotheca legum summary; not a full critical edition.

### 9. Across the Strait

[Candidate source](https://www.newadvent.org/fathers/3811.htm): Acts and canons, especially canon 28

Research candidate (not yet approved narration): Concilio de Calcedonia define fórmula cristológica y canon de privilegio para Constantinopla.

Disputado por Roma y varios obispos orientales.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/3811.htm): Acts and canons of Chalcedon, Canon 28 (page section around lines 390–400)

Supports Canon 28’s rationale of Constantinople as New Rome and allocation of equal ecclesiastical privileges / second rank, plus ordination jurisdiction in Pontic, Asian, Thracian dioceses.

Limit: The canon was contested by papal legates/Leo I; source wording must not imply uncontested universal recognition. The council’s Christological definition and canon 28 are distinct proceedings.

Coverage: Opened acts/canons; searched and read canon 28 text; translation/notes are 19th-century.

### 10. The Emperor at the City's Edge

[Candidate source](https://www.britannica.com/biography/Leo-I-Byzantine-emperor): Chronicle tradition; overview

Research candidate (not yet approved narration): León I es proclamado emperador en Constantinopla con participación del patriarca.

Detalles del ritual derivan de fuentes posteriores.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 11. A Letter That Could Not Unite

[Candidate source](https://www.newadvent.org/cathen/07218b.htm): Henotikon text summarized; Evagrius HE III.14

Research candidate (not yet approved narration): Zenón publica el Henotikon para reconciliar posiciones tras Calcedonia.

La política no consiguió consenso e inició cisma con Roma.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.tertullian.org/fathers/evagrius_3_book3.htm): Evagrius, Ecclesiastical History III.13–14; Henotikon text preserved in III.14

Supports Zeno’s letter addressed to clergy and laity of Alexandria, Egypt, Libya, and Pentapolis, invoking Nicaea and Constantinople/Ephesus to pursue unity; the text avoids a direct Chalcedonian two-natures formula.

Limit: The document’s intended audience is regional, not a universal imperial edict to all churches. Evagrius writes late 6th century and narrates retrospectively; 482 is accepted chronology but not explicitly dated in quoted document.

Coverage: Opened translation and read III.13–14 including document text; Walford translation only, not Greek critical edition.

### 12. One Seal after Two Emperors

[Candidate source](https://www.thelatinlibrary.com/marcellinus2.html): Marcellinus Comes, Chronicon, entrada 527: consigna que Justino hizo a Justiniano participante y sucesor del reino el 1 de abril; contexto para el comienzo del gobierno único el 1 de agosto: https://www.iranicaonline.org/articles/justinian-i-flavius-petrus-sabbatius-justinianus/.

Research candidate (not yet approved narration): A la muerte de Justino I, Justiniano pasa de coemperador a gobernante único en Constantinopla.

“Coronación” no debe usarse para el evento del 1 de agosto: Marcellinus fecha la elevación como coemperador en abril. La fecha de gobierno único se reconstruye con la muerte de Justino en agosto.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 13. The City in Ashes

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/War/1A*.html): Procopius, Wars I.24

Research candidate (not yet approved narration): Revuelta de Nika destruye la iglesia previa de Hagia Sophia y amenaza el gobierno de Justiniano.

Procopio describe la represión con sesgo político.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/Wars/1F%2A.html): Procopius, Persian Wars I.24.1 and following

Supports the Nika insurrection in Byzantium/Constantinople, the “Nika” watchword, destruction/fire and threat to imperial rule as narrated by Procopius.

Limit: Correct URL was Wars/1F, not War/1A. Procopius is close to events but rhetorically frames them; avoid treating speeches as verbatim. The earlier Hagia Sophia destruction is part of the account, but separate fire chronology should be checked in text.

Coverage: Read search-result excerpt identifying I.24 and its opening; primary page directly identified, full passage should be opened for detailed wording.

### 14. Stone beneath the Great Dome

[Candidate source](https://sourcebooks.web.fordham.edu/source/procop-deaed1.asp): Procopius, Buildings I.1

Research candidate (not yet approved narration): Justinian y Theodora reconstruyen Hagia Sophia, dedicada en 537.

Panegírico imperial; UNESCO confirma fecha y arquitectos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://sourcebooks.web.fordham.edu/source/procop-deaed1.asp): Procopius, De Aedificiis I.1.

Justinian reconstruyó Hagia Sophia, dedicada en 537.

Limit: Buildings I.1 describe edificio y patrocinio pero la fecha de dedicación 537 debe confirmarse con Chronicon Paschale u otra fuente; no suponer que el pasaje proporciona toda la cronología. Procopio panegírico.

Coverage: Referencia citada identificada; el texto del pasaje no se abrió en esta pasada.

### 15. The Orontes after the Flames

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/Wars/2B%2A.html): Procopio, Guerras persas II.8–10; contextualización de la incursión de 540 en https://online.ucpress.edu/SLA/article/7/2/201/196341/God-s-Wrath-over-Antioch-525-540-CEBeginning-of, especialmente discusión de la narrativa de Procopio y su valor como fuente.

Research candidate (not yet approved narration): Cosroes I captura y saquea Antioquía durante su incursión por la Siria romana; Procopio describe el asalto, el incendio y el traslado posterior de cautivos.

Procopio es fuente principal cercana, pero su narración tiene recursos dramáticos y sus obras difieren en tono; no repetir cifras de muertos/cautivos como datos comprobados sin corroboración.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 16. The Empty Granary

[Candidate source](https://www.metmuseum.org/essays/byzantium-ca-330-1453): Períodos y cultura material

Research candidate (not yet approved narration): Crisis urbana vinculada a peste y suministros durante Justiniano; reparto del jugador es ficción. No simular curación doctrinal.

Crisis urbana vinculada a peste y suministros durante Justiniano; reparto del jugador es ficción. No simular curación doctrinal.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 17. The Chapters on the Table

[Candidate source](https://www.newadvent.org/fathers/3812.htm): Council acts

Research candidate (not yet approved narration): Segundo Concilio de Constantinopla aborda los Tres Capítulos.

La condena tuvo recepción regional desigual.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 18. A City between Two Armies

[Candidate source](https://www.britannica.com/event/Siege-of-Constantinople-626): Chronicle traditions

Research candidate (not yet approved narration): Avaros y persas asedian Constantinopla mientras Heraclio combate en el este.

Cifras y milagros son retrospectivos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.britannica.com/event/Siege-of-Constantinople-626): Chronicle traditions (Theophanes, Chronographia AM 6118; localizador a verificar).

Avaros sitiaron Constantinopla en 626 mientras los persas amenazaban desde la orilla asiática; defensa bizantina repelió el asedio.

Limit: La URL de Britannica es síntesis terciaria; vincular una fuente primaria (Theophanes/Chronicon Paschale) con localizador. Cuidado, persas no son una fuerza de asedio conjunta en la misma ribera.

Coverage: Solo descripción/título de referencia identificado; source primary no consultado en esta pasada.

### 19. News from the Holy City

[Candidate source](https://academic.oup.com/book/6524/chapter-abstract/150435622): Robert G. Hoyland, Witnesses to a World Crisis, capítulo sobre fuentes cristianas orientales del siglo VII; para fecha 638 y tradición sobre visita de Umar, véase el examen de Theophilus of Edessa’s Chronicle, entrada 638, contextualizado en https://www.jstor.org/stable/jj.38238823.

Research candidate (not yet approved narration): Jerusalén/Aelia Capitolina pasa al control árabe tras la guerra romano-persa; la conquista altera el marco político de sus comunidades cristianas orientales.

La fecha oscila en las fuentes entre 636/637 y 638; los relatos detallados de capitulación y encuentro con Umar se transmiten en cronistas posteriores, no en un acta contemporánea segura. Sophronio ofrece testimonio contemporáneo del peligro en Palestina en su sermón de Navidad de 634, pero ese sermón no documenta la rendición de Jerusalén: https://christtheking.info/catholic-resources-on-adversus-judaeos/selections-of-st-sophronius-of-jerusalems-writings-on-the-jews/.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 20. Ships in the Uncertain Years

[Candidate source](https://www.britannica.com/event/Arab-Byzantine-wars): Theophanes, Chronicle

Research candidate (not yet approved narration): Ataques árabes por mar y tierra fracasan ante murallas y flota imperial.

Cronología del primer asedio discutida; “fuego griego” no está documentado en todos los detalles.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.medievalists.net/2022/07/was-constantinople-besieged-in-674-78/): Critical discussion of Theophanes’ chronological source compilation; cites Howard-Johnston and Jankowiak

Supports that the conventional continuous 674–678 siege chronology is contested; modern source criticism identifies editorial/source-chronology problems and alternative reconstructions.

Limit: This is a secondary explainer, not sufficient as final academic citation. Howard-Johnston argues no multi-year siege; Jankowiak places related operations earlier, late 660s. Keep as contested Arab operations around Constantinople, not a confidently dated continuous siege.

Coverage: Read article search extract; identified bibliography and competing arguments. Need primary Theophanes page and academic work directly consulted before final factual signoff.

### 21. Eighteen Sessions by the Palace

[Candidate source](https://www.newadvent.org/fathers/3813.htm): Acts of the Third Council of Constantinople, opening speech of papal legates and synodal proceedings; the session range is also recorded in the Prosopography of the Byzantine Empire, entry Petros 23: https://pbe.kcl.ac.uk/data/D62/F83.htm.

Research candidate (not yet approved narration): The Third Council of Constantinople meets in eighteen sessions and rejects the doctrine of one will and one operation in Christ, condemning key advocates of monothelitism.

The surviving acts are factionally situated and theological terminology is technical. This is distinct from the 553 council already in the corpus; avoid projecting later Roman/Orthodox confessional divisions backward.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 22. Winter at the Walls

[Candidate source](https://www.britannica.com/event/Second-Arab-Siege-of-Constantinople): Theophanes, AM 6209

Research candidate (not yet approved narration): El asedio omeya termina tras resistencia bizantina, invierno severo y ayuda búlgara.

Fuentes bizantinas magnifican bajas enemigas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.britannica.com/event/Second-Arab-Siege-of-Constantinople): Theophanes, Chronographia AM 6209.

Asedio omeya de 717–718 frustrado.

Limit: URL es secundaria; Theophanes es fuente posterior y presenta relato de los ataques. Añadir referencia académica para controversia de cronología/cifras y distinguir bloqueos terrestres y navales.

Coverage: No se inspeccionó fuente primaria en esta pasada.

### 23. An Image beneath the Orders

[Candidate source](https://academic.oup.com/book/26922/chapter-abstract/196030746): Oxford, Iconoclast Controversy 726–843

Research candidate (not yet approved narration): León III inicia políticas contra ciertas imágenes; la cronología y el primer decreto son inciertos.

Evitar escena dramática de destrucción de icono como hecho seguro.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 24. The Assembly at Hieria

[Candidate source](https://www.newadvent.org/fathers/3819.htm): Acts reconstructed from Nicaea II

Research candidate (not yet approved narration): Sínodo de Hieria respalda rechazo de imágenes bajo Constantino V.

Actas originales perdidas; reconstrucción hostil.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/3819.htm): Actas del Concilio de Nicea II (787), pasajes de sesión 7 que citan/sintetizan Hieria (754).

Sínodo de Hieria definió iconoclasia imperial bajo Constantino V.

Limit: No sobreviven actas independientes de Hieria; conocemos posición sobre todo mediante refutación/reconstrucción en Nicea II. Etiquetar la mediación y no tratar como transcripción neutral.

Coverage: Página primaria de Nicea II abierta; reconstrucción exacta de la sección de Hieria aún por fijar.

### 25. Pieces of a Memory

[Candidate source](https://www.newadvent.org/fathers/3819.htm): Acts of Nicaea II

Research candidate (not yet approved narration): Segundo Concilio de Nicea restaura veneración de imágenes y condena iconoclasmo.

Distingue veneración de adoración; traducciones varían.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/3819.htm): Nicaea II, Session VII definition and anathemas on images

Supports council’s defense of images and distinction of honorific veneration from latreia/service; council rejects iconoclast position in its own wording.

Limit: “Restores” can suggest uniform immediate compliance; better say council defines/affirms veneration in 787. The page contains a translated excerpt, not all acts or subsequent enforcement history.

Coverage: Opened full acts page and read definition/anathema and final veneration paragraphs.

### 26. The Court under Irene

[Candidate source](https://www.britannica.com/biography/Irene-Byzantine-empress): Theophanes, Chronicle AM 6289

Research candidate (not yet approved narration): Irene depone a Constantino VI y gobierna como emperatriz.

Theophanes iconófilo y hostil a rivales.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 27. A Crown beyond the Western Sea

[Candidate source](https://www.ancienttexts.org/library/latinlibrary/ein.html): Einhard, Life of Charlemagne 28

Research candidate (not yet approved narration): Coronación imperial de Carlomagno en Roma desafía pretensión universal de Constantinopla.

Einhard escribe décadas después y ofrece explicación política interesada.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.ancienttexts.org/library/latinlibrary/ein.html): Einhard, Vita Karoli Magni 28 (coronación en Roma).

León III coronó a Carlomagno emperador en Roma en Navidad del 800.

Limit: Fuera de la localización oriental de New Rome; la fuente de Einhard es retrospectiva y dice Carlomagno no conocía el plan. Si Anna está en Constantinopla, solo puede enterarse por noticias posteriores; no presentar testigo local en Roma. Evento quizá mantener como noticia exterior, no escena en Constantinopla.

Coverage: Fuente indicada en corpus; pasaje no extraído en esta pasada.

### 28. The Seal That Changed Hands

[Candidate source](https://www.britannica.com/biography/Nicephorus-I-Byzantine-emperor): Theophanes, Chronicle AM 6295

Research candidate (not yet approved narration): Irene es depuesta; Nicéforo I toma el trono en Constantinopla.

Perspectiva iconófila del cronista.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 29. The Roads below Pliska

[Candidate source](https://www.britannica.com/biography/Nicephorus-I-Byzantine-emperor): Theophanes, Chronicle AM 6303

Research candidate (not yet approved narration): Nicéforo muere en campaña contra los búlgaros en Pliska.

Fuentes de corte y crónica dramáticas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 30. A Report from the Thracian Field

[Candidate source](https://www.britannica.com/biography/Leo-V-the-Armenian): Theophanes, Chronicle AM 6305

Research candidate (not yet approved narration): León V recupera el trono tras derrota de Miguel I en Versinikia.

Causas militares y religiosas se entrelazan después en relatos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 31. The Covered Workshop

[Candidate source](https://academic.oup.com/book/26922/chapter-abstract/196030746): Oxford, Iconoclast Controversy

Research candidate (not yet approved narration): Sínodo en Constantinopla reactiva políticas iconoclastas.

Evidencia documental fragmentaria.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 32. The Mosaic Returned

[Candidate source](https://academic.oup.com/book/26922/chapter-abstract/196030746): Oxford, Iconoclast Controversy

Research candidate (not yet approved narration): La regente Teodora restaura la veneración de imágenes en sínodo; comienza la conmemoración del Triunfo de la Ortodoxia.

Sínodo local; término “ortodoxia” en sentido de fuente, no etiqueta de las iglesias modernas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending
