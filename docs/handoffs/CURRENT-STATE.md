# Estado actual y siguiente entrega

**Corte: 7 de noviembre de 2026.** Esta nota resume el snapshot operativo. DelendAI conectado decide los estados vivos de slices, claims, unidades y publicaciones; las referencias a commits identifican productos y recibos, no sustituyen ese estado.

## Catálogo y producto

- Nueve odiseas, 278 selecciones: 65 dossiers en borrador, 213 selecciones sin dossier, 2.689 pantallas bilingües, 405 objetivos secundarios y 216 principales.
- Geografía: 26 perfiles base y 19 suplementales (45 identidades únicas); faltan 40 identidades para 58 selecciones. El manifiesto registra 50 recursos. Las fuentes modernas no certifican terreno antiguo.
- Yavneh es el dossier 65, integrado como producto `d771747` (merges `1d59d1f` y `aa8d30d`). La revisión independiente acotada del 5 de noviembre comprobó la preservación de los 64 dossiers anteriores, 43/43 checks, 24 testigos y 21/21 saldos/reservas. No es la aprobación de d00002/S4 ni aprueba historia, geografía, motor o juego; S4 sigue sin cerrar.
- Hay dos episodios privados compilados en *Embers of the Covenant*: la apertura histórica de Cesarea y el build técnico de desarrollo geográfico de Jerusalén, con seis variantes cada uno (12 en total). El episodio 02 usa relieve regional moderno y no es una reconstrucción de terreno antiguo. Su build actual no implementa la señalización de receptores y la guía espacial necesarias para presentar rutas funcionales; el kit conserva evidencia de compilación e integridad, no de jugabilidad. Hay **cero campañas completas** y **cero episodios históricos plenamente verificados en el motor**.

## Estado operativo

- **i00015/S2 — vista geográfica privada:** integrada en `develop` por `d07fe11`; Terra aprobó esa entrega en `e72c4a0`. La corrección cubrió los P2 de vinculación del plan/origen, metadatos GeoTIFF y avisos nativos; la evidencia incluye 52 pruebas nativas enfocadas y `bun run test:export` con 122 pruebas. La entrega posterior `f77346f` hace que ese veredicto anterior necesite actualización para cerrar la propuesta. No demuestra juego ni aprueba geografía histórica. Los logs de exportación se conservan en `/home/cartago/.codex/artifacts/aoe2-mods/private-geographic-preview-independent-20261107/`.
- **x00002/S1 — ciclo de autorización:** aprobación formal e integración publicadas en `95cf894`; gate verde. DelendAI cerró oficialmente la propuesta en `done`. El producto corrige la separación entre autorización de build privado y preservación de la decisión de origen. No otorga por sí mismo autorización al plan canónico de Jerusalén.
- **i00015/S3 — build técnico del episodio 02:** el producto quedó integrado en `861e718`; la aprobación formal independiente de S3 está en `7cd39fb` y cubre el alcance revisado. El plan canónico tiene `privateBuildAuthorized=true` solo para compilación privada. El gate oficial de instalación/validación pasó; el recibo registra 123 pruebas nativas, cero saltos/fallos/errores, seis variantes y 12 round-trips de contenedor. Terra verificó por separado listado y extracción de los 12 contenedores; su journal finalizó con 165 pruebas y 2.161 aserciones. La revisión posterior halló que la salida contiene los 17 originales pero no las 10 señales/guías de recepción y orientación necesarias para funcionar como guía. La [guía](PRIVATE-JERUSALEM-GEOGRAPHIC-PREVIEW.md) y el [recibo](../qa/campaign-design/jerusalem-private-geographic-preview-build.json) describen la compilación técnica; el ZIP externo `/home/cartago/.codex/artifacts/aoe2-mods/jerusalem-private-geographic-preview-kit-20261107.zip` tiene SHA-256 `37f4db30982fff05efb2290fbdacb073dd6ad0a1655ed8296aff686fdd674748` (3.256.999 bytes), evidencia de integridad del kit, no de jugabilidad. El recibo conserva `historicalApproval=false`, `gameVerified=false` y `campaignComplete=false`.
- **i00015:** la cola marca S1/S2/S3 `done`, pero la propuesta permanece globalmente en `review`. El workflow oficial rechazó el cierre por veredictos S1/S2 obsoletos frente a entregas posteriores. x00003, correctivo de wayfinding, sigue preparándose en la unidad de root; no está integrado ni entregado.
- **d00002:** S1 está `done`; S2, S3 y S11 siguen en `review`; S4–S10 tienen `changes_requested`. S11 no está aprobado. La inserción de Yavneh no cierra S4, y los borradores no son prueba de motor.
- El intento de MiniMax M3.1 del 7 de noviembre recibió HTTP 429/2056. No se compraron créditos ni se infiere cuota de otros modelos.

## Prioridad y límites

1. i00015/S3 recibió aprobación formal para el alcance técnico entregado; la propuesta global sigue en `review`. La revalidación de S1/S2 se aplaza hasta que x00003/R2 quede aceptado; el correctivo está definido y Terra dio conformidad técnica en `0921ff9`, pero aún no está integrado. El build actual carece de señalización y guía de receptores y no debe presentarse como orientación funcional.
2. La revisión geométrica de Jerusalén sigue siendo un análisis de referencias modernas y candidatos de ruta, no aprobación de relieve antiguo, agua, colisión o navegación. Véase la [revisión del plan geográfico](../qa/campaign-design/jerusalem-geographic-plan-review-20261105/review.md).
3. El [preflight del episodio 03](../qa/campaign-design/episode03-preflight-20261107/report.md) y la [revisión del arquitecto](../qa/campaign-design/episode03-preflight-20261107/architect-next-decisions.md) identifican decisiones pendientes. No son asignación de implementación ni dossier nuevo.

No producir ahora los 213 dossiers en masa ni trabajar las nueve campañas en paralelo. No alterar IDs, contratos, rangos de cadenas o identidad de campañas para resolver decisiones pendientes. No distribuir mods ni presentar esta compilación o el kit como una entrega jugable de Jerusalén.

## Estado de publicación

El checkout compartido sigue `develop`; `main` es la rama de release, no la base de integración. Los productos aterrizan mediante publicación oficial de DelendAI y su gate. `x00002/S1` pasó su gate en `95cf894`; i00015/S3 pasó su gate oficial de instalación/validación y recibió aprobación formal independiente en `7cd39fb`.
