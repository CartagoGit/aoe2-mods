# Estado actual y siguiente entrega

**Corte: 7 de noviembre de 2026.** Esta nota resume el snapshot operativo. DelendAI conectado decide los estados vivos de slices, claims, unidades y publicaciones; las referencias a commits identifican productos y recibos, no sustituyen ese estado.

## Catálogo y producto

- Nueve odiseas, 278 selecciones: 65 dossiers en borrador, 213 selecciones sin dossier, 2.689 pantallas bilingües, 405 objetivos secundarios y 216 principales.
- Geografía: 26 perfiles base y 19 suplementales (45 identidades únicas); faltan 40 identidades para 58 selecciones. El manifiesto registra 50 recursos. Las fuentes modernas no certifican terreno antiguo.
- Yavneh es el dossier 65, integrado como producto `d771747` (merges `1d59d1f` y `aa8d30d`). La revisión independiente acotada del 5 de noviembre comprobó la preservación de los 64 dossiers anteriores, 43/43 checks, 24 testigos y 21/21 saldos/reservas. No es la aprobación de d00002/S4 ni aprueba historia, geografía, motor o juego; S4 sigue sin cerrar.
- Hay dos episodios privados compilados en *Embers of the Covenant*: la apertura histórica de Cesarea y la vista de desarrollo geográfica de Jerusalén, con seis variantes cada uno (12 en total). El episodio 02 usa relieve regional moderno y no es una reconstrucción de terreno antiguo. Hay **cero campañas completas** y **cero episodios históricos plenamente verificados en el motor**.

## Estado operativo

- **i00015/S2 — vista geográfica privada:** integrada en `develop` por `d07fe11`; aprobación formal Terra `e72c4a0`. La corrección cubrió los P2 de vinculación del plan/origen, metadatos GeoTIFF y avisos nativos; la evidencia incluye 52 pruebas nativas enfocadas y `bun run test:export` con 122 pruebas. No demuestra juego ni aprueba geografía histórica. Los logs de exportación se conservan en `/home/cartago/.codex/artifacts/aoe2-mods/private-geographic-preview-independent-20261107/`.
- **x00002/S1 — ciclo de autorización:** aprobación formal e integración publicadas en `95cf894`; gate verde. El producto corrige la separación entre autorización de build privado y preservación de la decisión de origen. No otorga por sí mismo autorización al plan canónico de Jerusalén.
- **i00015/S3 — episodio 02 privado de desarrollo:** el producto está integrado en `861e718`; el [plan canónico](../wiki/faith-origins/episodes/02-civilian-refuge-jerusalem/25-private-geographic-preview-plan.json) ahora tiene `privateBuildAuthorized=true` solo para compilación privada. El gate oficial de instalación/validación pasó y el recibo registra 123 pruebas nativas, cero saltos/fallos/errores, seis variantes y 12 round-trips de contenedor. Terra verificó por separado el listado/extracción de los 12 contenedores; la revisión formal de S3 sigue pendiente. La [guía](PRIVATE-JERUSALEM-GEOGRAPHIC-PREVIEW.md) y el [recibo](../qa/campaign-design/jerusalem-private-geographic-preview-build.json) están integrados. El [ZIP externo](</home/cartago/.codex/artifacts/aoe2-mods/jerusalem-private-geographic-preview-kit-20261107.zip>) tiene SHA-256 `37f4db30982fff05efb2290fbdacb073dd6ad0a1655ed8296aff686fdd674748` (3.256.999 bytes). El recibo conserva `historicalApproval=false`, `gameVerified=false` y `campaignComplete=false`: no hubo prueba en AoE2 ni aprobación histórica.
- **d00002:** S1 está `done`; S2, S3 y S11 siguen en `review`; S4–S10 tienen `changes_requested`. S11 no está aprobado. La inserción de Yavneh no cierra S4, y los borradores no son prueba de motor.
- El intento de MiniMax M3.1 del 7 de noviembre recibió HTTP 429/2056. No se compraron créditos ni se infiere cuota de otros modelos.

## Prioridad y límites

1. Terra termina la revisión formal del producto i00015/S3 y DelendAI registra su veredicto; mientras tanto el episodio 02 es una compilación privada integrada, no una misión histórica aprobada ni una partida verificada.
2. La revisión geométrica de Jerusalén sigue siendo un análisis de referencias modernas y candidatos de ruta, no aprobación de relieve antiguo, agua, colisión o navegación. Véase la [revisión del plan geográfico](../qa/campaign-design/jerusalem-geographic-plan-review-20261105/review.md).
3. El [preflight del episodio 03](../qa/campaign-design/episode03-preflight-20261107/report.md) y la [revisión del arquitecto](../qa/campaign-design/episode03-preflight-20261107/architect-next-decisions.md) identifican decisiones pendientes. No son asignación de implementación ni dossier nuevo.

No producir ahora los 213 dossiers en masa ni trabajar las nueve campañas en paralelo. No alterar IDs, contratos, rangos de cadenas o identidad de campañas para resolver decisiones pendientes. No distribuir mods ni presentar la documentación, extracción o exportación como una partida de AoE2.

## Estado de publicación

El checkout compartido sigue `develop`; `main` es la rama de release, no la base de integración. Los productos aterrizan mediante publicación oficial de DelendAI y su gate. `x00002/S1` pasó su gate en `95cf894`; i00015/S3 pasó su gate oficial de instalación/validación al integrarse en `861e718`. La aceptación formal independiente de S3 sigue pendiente.
