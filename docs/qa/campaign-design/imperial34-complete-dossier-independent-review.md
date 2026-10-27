# Independent review: Imperial Church dossier 34 composition

Reviewer: gpt-6-luna (DelendAI review unit d00002/S3, generation 4)  
Reviewed change: `b5a37cd9bf610a396800a8f6638f1ab1df3fabd6`  
Scope: the new Constantinople dossier composition, its supplied source record, and its generated map. This is a partial component review, not approval of the campaign or S3 as a whole.

## Findings

1. **The map legend names water-route styles that are absent from the drawing.** In `docs/design/maps/imperial-church/odyssey/34-church-transfer-constantinople.svg`, the legend says “Cyan dashed: proposed boat passage” and “Dashed blue: schematic regional water.” The nine blue water polylines are all solid and share the same `#247b96` stroke; none is cyan-dashed or otherwise distinguished from the other blue lines. The olive dashed polylines are the proposed land-district connections. The legend therefore asserts two visual distinctions readers cannot identify. Add the corresponding line samples/styles or remove the unsupported distinctions before treating this SVG as a usable map artifact. This does not challenge the explicit disclaimer that the paths are schematic and navigation is pending.

2. **The rendered episode date has a spacing error.** The dossier header displays `November380 CE` rather than `November 380 CE`. The same concatenation appears in generated provenance strings (`arrival24November`, `November380`, and `inDecember`). Correct the player-visible header and, if these strings remain in the dossier, separate the date and month tokens there as well.

## Source and composition checks

I read the relevant passages in Socrates, *Church History* V.6–7 (New Advent/NPNF English translation), Sozomen VII.5 (New Advent/NPNF English translation), and the Latin 380 entry in Marcellinus Comes’ chronicle (The Latin Library transcription labelled Mommsen, *Chronica Minora* II). Socrates reports arrival and church-possession changes on separate November days; Marcellinus places a restoration in December; Sozomen’s account supplies no exact day and includes later building descriptions and attributed traditions. The dossier preserves the November/December disagreement, attributes retrospective confessional framing, keeps Sozomen’s later building and miracle material from proving a 380 location, and does not turn the sources into universal compliance, an exact church footprint, or playable forced conversion. The bounded source inspection does not include a critical apparatus or manuscript review.

The new dossier is clearly marked as a design draft with historical, geographic, native, and game review pending. The local services and Marcus are expressly fictional, with no authentic speech claimed. Its accounting text labels prefix and affordability results as finite arithmetic rather than a playthrough. The map plan qualifies modern surface samples and fictional activity sites rather than presenting them as 380 terrain. The 51 bilingual screens have unique IDs/keys; their caption segments reconstruct the supplied screen text, and every segment stays within the stated 32-word limit. Native capability and gameplay verification remain pending.

By episode ID, the 33 pre-existing `episodes[]` objects are unchanged; the new episode is the sole addition. The corresponding existing `episodeSelection` entry changes only its `contractStatus`. The commit adds one SVG without changing any prior SVG under `docs/design/maps`; it adds the new dossier and updates the arc page.

No heavy validation suite or game run was performed as requested. No approval of prior components, native behavior, game balance, or the full S3 slice is implied.
