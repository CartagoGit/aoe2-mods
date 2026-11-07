# Campaign production catalogue

Authoritative editorial input: [catalog.json](catalog.json). This is a design contract, not campaignSchema or a playable mod. English is the source; Spanish is supplied for every player-facing screen. Architecture documentation remains in Spanish.

Nine historical campaigns / 39 historical scenarios, plus two separately specified technical lab scenarios. The Milvian pilot reuses the C01 mission, rather than adding a contradictory fortieth historical scenario.

| Identity | English / Español | Period | Missions | Narrator |
|---|---|---|---:|---|
| CDF-C00 / `faith-origins` | [Embers of the Covenant](../wiki/faith-origins/12-production-blueprint.md) / Las brasas de la alianza | c. 50–313 CE | 4 | Miriam of Caesarea |
| CDF-C01 / `imperial-church` | [The Eagle and the Cross](../wiki/imperial-church/12-production-blueprint.md) / El águila y la cruz | 312–337 CE | 3 | Marcus, the Imperial Clerk |
| CDF-C02 / `jewish-tradition` | [Keepers of the Unbroken Word](../wiki/jewish-tradition/12-production-blueprint.md) / Guardianes de la palabra viva | 70–c. 425 CE | 4 | Judith of Tiberias |
| CDF-C03 / `church-of-rome` | [The Keys of the Eternal City](../wiki/church-of-rome/12-production-blueprint.md) / Las llaves de la Ciudad Eterna | 337–800 CE; missions 410–800 | 4 | Leo of the Roman Roads |
| CDF-C04 / `new-rome` | [Beyond the Golden Gate](../wiki/new-rome/12-production-blueprint.md) / Más allá de la Puerta Dorada | 337–843 CE; missions 451–787 | 5 | Anna, the Mosaic Restorer |
| CDF-I00 / `first-caliphs` | [Beneath the Desert Stars](../wiki/first-caliphs/12-production-blueprint.md) / Bajo las estrellas del desierto | 622–656 CE | 5 | Salim, the Caravan Scribe |
| CDF-I01 / `first-fitna` | [The Shattered Oath](../wiki/first-fitna/12-production-blueprint.md) / El juramento quebrado | 656–661 CE | 5 | Farid, the Field Medic |
| CDF-I02 / `umayyads` | [From Damascus to the Far Horizon](../wiki/umayyads/12-production-blueprint.md) / De Damasco al último horizonte | 661–750 CE | 5 | Yasir, the Cloth Merchant |
| CDF-I03 / `house-of-ali` | [The River Remembers](../wiki/house-of-ali/12-production-blueprint.md) / El río recuerda | 656–680 CE | 4 | Dina of the Riverbank |

## Cross-campaign order

| Route remembered | Recommended next | Entry policy |
|---|---|---|
| `progress.faith-origins.christian-perspective = 1` | imperial-church | recommendation + recap, never a lock |
| `progress.faith-origins.jewish-perspective = 1` | jewish-tradition | recommendation + recap, never a lock |
| `progress.imperial-church.western-perspective = 1` | church-of-rome | recommendation + recap, never a lock |
| `progress.imperial-church.eastern-perspective = 1` | new-rome | recommendation + recap, never a lock |
| `progress.jewish-tradition.completed = 1` | No designated direct sequel; offer parallel catalogue | recommendation + recap, never a lock |
| `progress.church-of-rome.completed = 1` | No designated direct sequel; offer parallel catalogue | recommendation + recap, never a lock |
| `progress.new-rome.completed = 1` | No designated direct sequel; offer parallel catalogue | recommendation + recap, never a lock |
| `progress.first-caliphs.completed = 1` | first-fitna | recommendation + recap, never a lock |
| `progress.first-fitna.muawiya-perspective = 1` | umayyads | recommendation + recap, never a lock |
| `progress.first-fitna.ali-perspective = 1` | house-of-ali | recommendation + recap, never a lock |
| `progress.umayyads.completed = 1` | No designated direct sequel; offer parallel catalogue | recommendation + recap, never a lock |
| `progress.house-of-ali.completed = 1` | No designated direct sequel; offer parallel catalogue | recommendation + recap, never a lock |

[Production contract](production-contract.md) · [references and licensing](reference/CREDITS.md) · [sources](sources.json) · [QA](../qa/campaign-design/verification.md)

Regenerate: `python3 tools/design/render.py`; verify: `python3 tools/design/verify.py`. Do not hand-edit generated dossiers or SVGs; modify the authored catalogue or geographic profiles and regenerate. No generated file is native scenario input.
