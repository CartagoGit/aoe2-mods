# From Damascus to the Far Horizon / De Damasco al último horizonte

`umayyads` · CDF-I02 · 32 selected episodes · source locale `en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

```json
{
  "editorial": {
    "campaignTitle": {
      "en": "From Damascus to the Far Horizon",
      "es-ES": "De Damasco al último horizonte"
    },
    "publicId": "CDF-I02",
    "internalName": "CDF_Umayyads",
    "sourceLocale": "en",
    "targetEpisodeCount": 32,
    "narratorId": "yasir-cloth-merchant",
    "personaLens": {
      "en": "Prices, credit, cloth and hidden costs",
      "es-ES": "Precios, crédito, tejidos y costes ocultos"
    },
    "deliveryTone": {
      "en": "quick confidence becoming thoughtful doubt",
      "es-ES": "confianza rápida que acaba en duda reflexiva"
    },
    "sequence": [
      {
        "speaker": "collection-narrator",
        "mode": "sober source-qualified historical fact",
        "causePolicy": "attribute motives, miracles and sectarian judgements to their sources; no single moral or theological verdict"
      },
      {
        "speaker": "yasir-cloth-merchant",
        "mode": "fictional personal interpretation with explicit witness basis"
      }
    ],
    "baselineSemanticIdsPreserved": [
      "01-ledgers-of-damascus",
      "02-stone-and-memory",
      "03-the-western-shore",
      "04-the-narrow-sea",
      "05-the-last-crossing"
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
        "campaignId": "first-fitna",
        "route": "muawiya-perspective"
      }
    ],
    "nextRoutes": [
      {
        "id": "completed",
        "key": "progress.umayyads.completed",
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

## act-1: The Ledger of Damascus / El registro de Damasco

Historical year band: [661, 680]. Gobierno y sucesión; Yasir usa cuentas familiares, no memoria adulta de661.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 1 / 01-ledgers-of-damascus | Ledgers of Damascus / Registros de Damasco | 661 CE | damascus | administrative-and-market-logistics |
| 2 / 02-succession-and-rival-records-damascus | The Son Named in the Letter / El hijo nombrado en la carta | 680 CE | damascus | succession-and-rival-records |
| 3 / 03-off-map-witness-and-relief-damascus | News That Crossed the Desert / Noticias que cruzaron el desierto | October680 conventional; Karbala itself off-map | damascus | off-map-witness-and-relief |

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

## act-2: The Second Fracture / La segunda fractura

Historical year band: [683, 698]. Guerra civil, restauración de autoridad, edificios y moneda; efectos distintos para comunidades y comerciantes.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 4 / 04-bounded-civilian-withdrawal-medina | The Roads after al-Harra / Los caminos después de al-Harra | 683 CE | medina | bounded-civilian-withdrawal |
| 5 / 05-finite-siege-and-household-relief-mecca | The City beneath the Siege / La ciudad bajo el asedio | 683 CE | mecca | finite-siege-and-household-relief |
| 6 / 06-separate-delegation-and-supply-jabiya | The Assembly on the Plateau / La asamblea en la meseta | 684 CE | jabiya | separate-delegation-and-supply |
| 7 / 07-administrative-transition-damascus | The Seal of Abd al-Malik / El sello de Abd al-Malik | 685 CE | damascus | administrative-transition |
| 8 / 02-stone-and-memory | Stone and Memory / Piedra y memoria | 691/692 CE | jerusalem | finite-monument-works |
| 9 / 09-civilian-refuge-and-property-records-mecca | After the Second Siege / Después del segundo asedio | 692 CE | mecca | civilian-refuge-and-property-records |
| 10 / 10-fiscal-and-witness-records-kufa | A Governor at the Iraqi Door / Un gobernador a la puerta de Irak | 694 CE | kufa | fiscal-and-witness-records |
| 11 / 11-finite-mint-and-market-reconciliation-damascus | Gold without the Old Portrait / Oro sin el retrato antiguo | 696–697 CE; phasedreforms | damascus | finite-mint-and-market-reconciliation |
| 12 / 03-the-western-shore | The Western Shore / La costa occidental | 698 CE | carthage | finite-harbour-battle-and-withdrawal |

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

## act-3: Across the Oxus / Más allá del Oxus

Historical year band: [700, 712]. Revueltas y campañas orientales con un lugar por misión; mercader no decide teologías de poblaciones conquistadas.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 13 / 13-finite-battle-and-civilian-extraction-kufa | The Fields of the Broken Banner / Los campos del estandarte quebrado | 700–701 CE; DayralJamajimregionalfootprintuncertain | kufa | finite-battle-and-civilian-extraction |
| 14 / 14-provincial-dispatch-and-provision-merv | Orders at the Eastern Gate / Órdenes en la puerta oriental | 705 CE | merv | provincial-dispatch-and-provision |
| 15 / 15-finite-siege-and-trade-recovery-paykand | The Walls of Paykand / Las murallas de Paykand | 706 CE | paykand | finite-siege-and-trade-recovery |
| 16 / 16-finite-relief-and-withdrawal-ramitin | The Roads through Ramitin / Los caminos por Ramitin | 707 CE; localityidentificationqualified | ramitin | finite-relief-and-withdrawal |
| 17 / 17-tribute-and-household-receipts-bukhara | A Receipt at Bukhara's Gate / Un recibo a la puerta de Bujará | 709 CE | bukhara | tribute-and-household-receipts |
| 18 / 18-civilian-record-and-refuge-balkh | A Message from Tokharistan / Un mensaje desde Tojaristán | 710 CE; captureofNizakreported, notplayerexecution | balkh | civilian-record-and-refuge |
| 19 / 19-off-map-dispatch-and-bounded-accounts-balkh | Tribute beyond the Mountain Road / Tributo más allá del camino de montaña | 711 CE; Zabulistanoff-map, locationnotassertedinBalkh | balkh | off-map-dispatch-and-bounded-accounts |

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

## act-4: The Sea and the Far Horizon / El mar y el horizonte lejano

Historical year band: [711, 740]. Iberia, rutas orientales y fracaso anteConstantinopla; los mapas no abarcan toda una provincia en400tiles.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 20 / 04-the-narrow-sea | The Narrow Sea / El mar estrecho | 711–712 CE | gibraltar | finite-strait-convoy-and-civilian-refuge |
| 21 / 21-bounded-river-trade-and-receipts-khwarazm | Accounts on the Lower Oxus / Cuentas en el bajo Oxus | 712 CE | khwarazm | bounded-river-trade-and-receipts |
| 22 / 22-finite-siege-and-property-records-samarkand | The City at the End of the Road / La ciudad al final del camino | 712 CE | samarkand | finite-siege-and-property-records |
| 23 / 23-finite-works-and-source-comparison-bukhara | The Citadel's New Courtyard / El nuevo patio de la ciudadela | 712–713 CE; attendanceclaimsattributed, noconversiongoal | bukhara | finite-works-and-source-comparison |
| 24 / 24-finite-caravan-and-relief-tashkent | Toward the Shash Oasis / Hacia el oasis de Shash | 714 CE; Fergana/Isfijabreportedoff-map | tashkent | finite-caravan-and-relief |
| 25 / 25-finite-withdrawal-and-record-preservation-fergana | The Camp without Its Commander / El campamento sin su comandante | 715 CE; commanderhistoricaldeathreported | fergana | finite-withdrawal-and-record-preservation |
| 26 / 26-finite-siege-withdrawal-and-supply-constantinople | The Winter beyond the Strait / El invierno más allá del estrecho | 717–718 CE; siegefailsregardlesslocalachievement | constantinople | finite-siege-withdrawal-and-supply |
| 27 / 27-bounded-civilian-refuge-kufa | The Quarter after Zayd's Revolt / El barrio después de la revuelta de Zayd | 740 CE; dateconversionvariants | kufa | bounded-civilian-refuge |

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

## act-5: The Last Accounts / Las últimas cuentas

Historical year band: [744, 750]. Revolución, Kufa, Zab y caída oriental; el arco termina sin negar supervivencia omeya posterior enIberia.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 28 / 28-competing-provincial-dispatches-damascus | The Seals That Would Not Hold / Los sellos que no se sostenían | 744–747 CE; onecity receivesreports | damascus | competing-provincial-dispatches |
| 29 / 29-bounded-camp-and-civilian-provision-merv | A Banner Raised in Marw / Un estandarte alzado en Marw | 747 CE | merv | bounded-camp-and-civilian-provision |
| 30 / 30-administrative-and-household-reception-kufa | A New Voice at Kufa / Una voz nueva en Kufa | November749 CE | kufa | administrative-and-household-reception |
| 31 / 05-the-last-crossing | The Last Crossing / El último paso | 750 CE | zab | finite-river-withdrawal |
| 32 / 32-civilian-records-and-final-perspective-fustat | The Dynasty's Last Dispatch / El último despacho de la dinastía | August750 CE; killingatBusirreportedoff-map | fustat | civilian-records-and-final-perspective |

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

### 1. Ledgers of Damascus

[Candidate source](https://www.iranicaonline.org/articles/chronology-of-iranian-history-part-1/): “Chronology…” entries 661 and 661–80; Hasan Iranica, pp. 3–4

Research candidate (not yet approved narration): Muawiya assumes the caliphate after Hasan relinquishes control of Iraq; Damascus serves as the dynasty’s political center.

The transfer was negotiated and staged; do not portray as a single universally accepted coronation.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 2. The Son Named in the Letter

[Candidate source](https://www.iranicaonline.org/articles/asura/): “ʿĀšūrāʾ,” opening paragraph; Iranica chronology entry 680

Research candidate (not yet approved narration): Yazid succeeds Muawiya, whose hereditary designation provokes opposition.

Succession mechanism and legitimacy are described differently across political traditions.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 3. News That Crossed the Desert

[Candidate source](https://www.iranicaonline.org/articles/karbala/): “Karbala,” opening paragraph; “Husayn,” paragraphs 94–99

Research candidate (not yet approved narration): Husayn and his companions are killed at Karbala.

Death day and Gregorian conversion are traditional; number of dead disputed.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 4. The Roads after al-Harra

[Candidate source](https://fada.birzeit.edu/jspui/handle/20.500.11889/1654): Birzeit repository record/title and abstract; 63 AH/683 study of reports on al-Harra

Research candidate (not yet approved narration): Rebellion in Medina ends in the battle of al-Harra against forces sent by Yazid.

Academic thesis focuses on divergent historical reports; exact battle day and casualty claims not used.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 5. The City beneath the Siege

[Candidate source](https://www.jstor.org/stable/jj.18252825): Al-Ṭabarī vol. 20, year 64 (683–684), pp. 1–123; JSTOR excerpt lines 102–109 reports 40-day siege and retreat after Yazid’s death

Research candidate (not yet approved narration): Ibn al-Zubayr’s challenge leads to an Umayyad siege of Mecca; forces withdraw after Yazid’s death.

Volume summary and opening excerpt consulted; underlying account transmits earlier chroniclers, and event details vary.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 6. The Assembly on the Plateau

[Candidate source](https://www.jstor.org/stable/jj.18252825): Al-Ṭabarī vol. 20, years 64–65; translator’s foreword and year 65 section

Research candidate (not yet approved narration): Marwan becomes caliph amid the Second Fitna.

The line of Marwanid succession is a political transition during an unstable civil war; access to full volume restricted.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 7. The Seal of Abd al-Malik

[Candidate source](https://www.iranicaonline.org/articles/chronology-of-iranian-history-part-1/): “Chronology…” entry 685

Research candidate (not yet approved narration): Abd al-Malik succeeds Marwan and gradually reunifies Umayyad-held regions.

Control was contested; no one-day reunification.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 8. Stone and Memory

[Candidate source](https://www.metmuseum.org/exhibitions/listings/2012/byzantium-and-islam/blog/where-in-the-world/posts/dome-of-the-rock): The Met, “The Dome of the Rock”: originally built 688–692, completed 691/692

Research candidate (not yet approved narration): Abd al-Malik’s Dome of the Rock is completed on the Haram al-Sharif.

Building phase spans years; avoid claims about a single motivation.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 9. After the Second Siege

[Candidate source](https://www.jstor.org/stable/jj.18254935): Al-Ṭabarī vol. 21, year 73; book description says Ibn al-Zubayr’s rival caliphate extinguished by end of 73/692

Research candidate (not yet approved narration): Ibn al-Zubayr is defeated and killed; Umayyad authority is restored over the Hijaz.

JSTOR book description consulted; full narrative inaccessible; no siege tactics or casualty details used.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 10. A Governor at the Iraqi Door

[Candidate source](https://journals.library.columbia.edu/index.php/alusur/article/download/uw30sijpesteijn/uw30sijpesteijn/25796): Petra M. Sijpesteijn, “Closing Ranks,” article passage: al-Hajjaj appointed governor of Iraq in 75/694.

Research candidate (not yet approved narration): Al-Hajjaj is appointed governor of Iraq and conducts campaigns against remaining opposition.

Appointment date is supported by the consulted article; avoid adding unverified military actions to the appointment milestone.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 11. Gold without the Old Portrait

[Candidate source](https://www.iranicaonline.org/articles/coins-and-coinage/): “Coins and Coinage,” passage on Abd al-Malik’s reform and anonymous coinage

Research candidate (not yet approved narration): Abd al-Malik reforms coinage, replacing Byzantine/Sasanian-style issues with Islamic inscriptions.

Dates sometimes given as 696 or 697; coin reform was staged across regions.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 12. The Western Shore

[Candidate source](https://en.wikisource.org/wiki/Page:Bury_J_B_The_Cambridge_Medieval_History_Vol_2_1913.djvu/398): Cambridge Medieval History II, p. 370, passage on naval reversal/Carthage

Research candidate (not yet approved narration): Carthage is captured by Arab forces after a Byzantine attempt to recover it.

Older synthesis; exact sequencing and date need modern corroboration.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 13. The Fields of the Broken Banner

[Candidate source](https://www.iranicaonline.org/articles/kufa/): Encyclopaedia Iranica, “Kufa,” passage on the revolt: Ibn al-Ashʿath captures Kufa in 701 and is defeated by al-Ḥajjāj in Rabīʿ I 82/April 701; primary narrative: al-Ṭabarī, History, vol. 18, “The Events of the Years 81–82,” Dayr al-Jamājim report, https://ghayb.com/wp-content/uploads/2016/09/Tabari_Volume_18.pdf.

Research candidate (not yet approved narration): Ibn al-Ashʿath’s large Iraqi military revolt challenges al-Ḥajjāj and Umayyad rule; after taking Kufa, the rebels are defeated near Dayr al-Jamājim.

Al-Ṭabarī preserves later transmitted reports rather than eyewitness records; the secondary source differs on dates and the rebellion’s exact phases. Keep c.700–701 for the broader rising and 701 for the named defeat; do not collapse it into the 740 Zayd revolt.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 14. Orders at the Eastern Gate

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” passage beginning “Under al-Walid I (86–96/705–15)”

Research candidate (not yet approved narration): Al-Walid I becomes caliph; Qutayba is appointed governor of Khorasan around this period.

Hijri/Gregorian conversion; Qutayba’s appointment given as 704/705 in Iranica.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 15. The Walls of Paykand

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” Qutayba campaigns; Paykand in 87/706

Research candidate (not yet approved narration): Qutayba captures Paykand during campaigns across the Oxus.

Military narrative from later sources; do not assert exact battlefield positions.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 16. The Roads through Ramitin

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” Qutayba campaign sequence, 88/707

Research candidate (not yet approved narration): Qutayba takes Rāmetīn and defeats a Sogdian/Turkic relief force near Bukhara.

Dates as conversion in Iranica; detail comes from Arabic chronicles.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 17. A Receipt at Bukhara's Gate

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” Qutayba entry of 90/709; also Iranica “Bukhara ii”

Research candidate (not yet approved narration): Qutayba takes Bukhara and installs a garrison/tribute arrangement.

A local ruler remained; the conquest did not mean immediate cultural conversion or permanent uncontested control.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 18. A Message from Tokharistan

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” Qutayba sequence, 91/710

Research candidate (not yet approved narration): Nizak leads a revolt in Tokharistan and is captured and killed.

Reported in later chronicles; use as regional revolt, not invented field battle.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 19. Tribute beyond the Mountain Road

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” passage on 92/711

Research candidate (not yet approved narration): Qutayba exacts tribute from the Zunbil rulers.

Political submission/tribute is not equivalent to full territorial annexation.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 20. The Narrow Sea

[Candidate source](https://sourcebooks.web.fordham.edu/source/conqspain.asp): Ibn ʿAbd al-Ḥakam, “Conquest of Spain,” crossing narrative

Research candidate (not yet approved narration): Umayyad forces cross from North Africa into Iberia and begin the conquest.

Text composed later; crossing date, landing location and actor details are not certain.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 21. Accounts on the Lower Oxus

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” 93/712 campaign

Research candidate (not yet approved narration): Qutayba takes and garrisons Khwarazm.

Control and chronology are contested in regional scholarship.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 22. The City at the End of the Road

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” campaign after Khwarazm; Gurak’s submission

Research candidate (not yet approved narration): Samarkand submits after Sogdian and Turkic forces are defeated; a garrison is left to collect tribute.

Narrative transmitted by later Arabic sources; submission should not be phrased as permanent occupation.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 23. The Citadel's New Courtyard

[Candidate source](https://www.iranicaonline.org/articles/bukhara-v/): Iranica, “Bukhara v. Archaeology and Monuments,” Qutayba’s mosque

Research candidate (not yet approved narration): Qutayba’s administration builds a mosque in Bukhara’s citadel; local attendance is reportedly incentivized.

The account cites Narshakhi, written centuries later; not a claim of immediate mass conversion.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 24. Toward the Shash Oasis

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” campaigns to 95/714

Research candidate (not yet approved narration): Qutayba campaigns in Shash, Fergana, and as far as Isfijab.

Iranica reports the campaign reach by 95/714; distinguish it from al-Walid’s death in 715.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 25. The Camp without Its Commander

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” final Qutayba paragraph; “Khorasan iv” says ca. August 715

Research candidate (not yet approved narration): Qutayba is killed in a mutiny after al-Walid’s death and Sulayman’s accession.

Iranica dates the mutiny and death to 96/714–715, with the article placing it around August 715 after al-Walid’s death.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 26. The Winter beyond the Strait

[Candidate source](https://www.cambridge.org/core/journals/journal-of-hellenic-studies/article/abs/campaign-of-716718-from-arabic-sources/7FA64C84BFD76CECFF0AB6C528D6C854): E. W. Brooks, “The Campaign of 716–718, from Arabic Sources,” source discussion

Research candidate (not yet approved narration): An Umayyad force besieges Constantinople and withdraws without taking the city.

Campaign is conventionally 717–718; manuscript accounts differ and siege details are contested.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 27. The Quarter after Zayd's Revolt

[Candidate source](https://www.iranicaonline.org/articles/kufa/): Encyclopaedia Iranica, “Kufa,” section on the revolt of Zayd b. ʿAlī; corroborating academic synthesis: St Andrews Encyclopaedia of Theology, “Zaydī Shīʿism,” https://www.saet.ac.uk/Islam/ZaydiShiism.

Research candidate (not yet approved narration): Zayd ibn ʿAlī leads an unsuccessful revolt against Hishām’s Umayyad government in Kufa and is killed after support among Kufans fails to hold.

Traditional chronicles disagree in details of the pledge, defections, death, and treatment of the body. State only the revolt and death at Kufa; do not present later Zaydi identity as already fully formed or confuse this with Husayn’s 680 revolt.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 28. The Seals That Would Not Hold

[Candidate source](https://www.iranicaonline.org/articles/khorasan-iv-the-arab-conquest-and-omayyad-period/): Iranica “Khorasan iv,” section “Estrangement, Division, and Arbitration (97–128/715–45)”

Research candidate (not yet approved narration): Repeated succession crises and provincial revolts weaken the late Umayyad government.

The article supports regional context; precise campaign episodes are numerous and not all need playable scenarios.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 29. A Banner Raised in Marw

[Candidate source](https://www.iranicaonline.org/articles/chronology-of-iranian-history-part-1/): “Chronology…” entries 747; Iranica “Abu Moslem Ḵorāsānī”

Research candidate (not yet approved narration): Abu Muslim raises the Abbasid revolt in Marw.

Beginning of revolt is securely placed in 747; details of popular support and ideology are debated.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 30. A New Voice at Kufa

[Candidate source](https://www.iranicaonline.org/articles/abu-moslem-abd-al-rahman-b/): “Abu Moslem Ḵorāsānī,” passage on Kufa and Friday ceremony, 12 Rabi II 132 / 28 Nov 749

Research candidate (not yet approved narration): Abbasid forces enter Kufa; al-Saffah is proclaimed caliph in November.

Proclamation was a political process; distinguish it from final defeat of Marwan II.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 31. The Last Crossing

[Candidate source](https://www.iranicaonline.org/articles/abu-moslem-abd-al-rahman-b/): “Abu Moslem Ḵorāsānī,” paragraph on Marwan confronting rebels at the Great Zab

Research candidate (not yet approved narration): Marwan II is defeated by Abbasid forces at the Great Zab.

Battle date often given 750; article notes retreat and later death in Egypt.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 32. The Dynasty's Last Dispatch

[Candidate source](https://www.iranicaonline.org/articles/abu-moslem-abd-al-rahman-b/): Same Iranica article, final sentence gives 27 Dhu al-Hijja 132 / 6 Aug. 750

Research candidate (not yet approved narration): Marwan II is killed after retreating to Egypt; Umayyad caliphate in the east ends.

The date is an AH-to-Gregorian conversion in Iranica; an Umayyad branch continues in Iberia, beyond campaign scope.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending
