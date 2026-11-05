# Estado actual y siguiente entrega

**Corte: 5 de noviembre de 2026.** Esta nota resume el estado operativo compartido. La fuente de verdad de propuestas, claims, unidades y revisiones es el DelendAI conectado; las cifras de cortes fechados en otros documentos describen esos snapshots anteriores.

## Catálogo y producto privado

- Nueve odiseas, 278 selecciones: 65 dossiers en borrador, 213 selecciones sin dossier, 2.689 pantallas bilingües, 405 objetivos secundarios y 216 principales.
- Geografía: 26 perfiles base + 19 suplementales = 45 perfiles únicos. Faltan 40 identidades geográficas para 58 selecciones. El manifiesto registra 50 recursos; los recursos modernos no acreditan terreno antiguo.
- Yavneh es el dossier 65. La inserción aterrizó como producto `d771747` (merges `1d59d1f` y `aa8d30d`). La revisión acotada independiente de GPT-6.1-Terra del 5 de noviembre no encontró P1/P2 en esa transformación: comprobó la preservación de los 64 dossiers previos, 43/43 checks, 24 testigos sin discrepancias y 21/21 saldos/reservas. Véase la [revisión](../qa/campaign-design/yavneh-insertion-review-20261105/review.md), con sus testigos y manifiestos preservados en el repo. Esta revisión no es la aprobación formal de d00002/S4 ni acepta historia, geografía, motor o juego; S4 sigue sin cerrar.
- Hay una apertura histórica privada de Embers of the Covenant en seis variantes EN/es-ES × easy/standard/hard. Hay **cero campañas completas** y **cero episodios históricos plenamente verificados en el motor**. El builder de Jerusalén solo produce el fixture sintético etiquetado y rechaza el build histórico.

## Prioridad y límites

Cerrar primero los bloqueos de arquitectura y herramientas y luego avanzar campaña a campaña, con entregas privadas progresivas de **Embers of the Covenant**. No producir ahora los 213 dossiers en masa ni trabajar las nueve campañas en paralelo. La prioridad no altera IDs, contratos, fuentes, rangos de cadenas ni identidad de campañas.

i00012/S1 e i00013/S1 están oficialmente `done` en `90948b1`; el producto de i00012 (`230173a`) ya estaba integrado, y `90948b1` integra los veredictos, no un nuevo producto. La implementación de cuentas finitas de i00013 **está integrada en develop**, pero S2 aún no está formalmente aprobado: producto `688a1203`, merge certificado `cf84b92f`. GPT-6.1-Sol verificó la corrección del overflow derivado y del informe de subpruebas que podía declarar éxito tras un fallo; 9 pruebas enfocadas y la inyección independiente pasan. El gate oficial de instalación/validate pasó. El primer submit fue rechazado porque DelendAI exige este informe real de S3 antes de entregar S2; no se registró una aprobación por ese intento. i00014/S1 está `done`, pero solo compila un fixture sintético y no habilita un build histórico de Jerusalén. Historia, decisiones de geografía/terreno, composición nativa y pruebas de juego siguen abiertas.

En d00002, S1 está `done`; S2, S3 y S11 están en `review` y no acreditan prueba del motor. S4–S10 tienen revisión `changes_requested`; sus campañas contienen cero o un dossier canónico cada una. La revisión acotada de la inserción de Yavneh no cierra S4.

Root conserva arquitectura, decisiones históricas/geográficas, cierre de packets e integración. Luna mantiene la única implementación de i00013/S2, con nueve archivos autorizados incluido el registro de pruebas en test_design. MiniMax ya recibió el GO para implementar exclusivamente los once archivos de i00015/S2 en su propia unidad desde develop; no inventa historia, presupuesto ni terreno. Cada producto requiere revisión de otro modelo. El usuario prueba los casos reales de motor en Windows/Steam y es-ES.

## Siguientes tres paquetes

1. **i00013/S2 — cuentas finitas de dificultad:** producto `688a1203` integrado en `cf84b92f` con gate y conformidad técnica independiente. Falta reintentar el submit propio después de publicar el [informe sustantivo](../qa/campaign-design/authored-difficulty-accounts-review.md) y registrar aprobación formal. La operación implementada todavía no equivale a aceptación formal. i00013/S3 sigue pendiente.
2. **i00015/S1 → S2 — vista de relieve privada:** la arquitectura final aterrizó en `2c56e3` y su aprobación formal independiente en `e513c000`; S1 está `done`. Root asignó S2 a MiniMax M3.1 Flash, que abrió y reclamó su unidad propia. S2 no está aceptado ni integrado y `privateBuildAuthorized=false`. El DSM moderno no aprueba terreno histórico.
3. **Jerusalén, episodio 02 de Embers:** después de cerrar herramientas y decisiones físicas, root prepara S3 y una entrega privada de dos episodios de la primera campaña. i00014/S1 solo ofrece el rechazo histórico y la compilación sintética. No se afirma aprobación histórica ni prueba de juego; el usuario realiza los casos reales de motor en Windows/Steam y es-ES cuando haya artefacto jugable.

La [revisión geométrica independiente de Jerusalén](../qa/campaign-design/jerusalem-geographic-plan-review-20261105/review.md) confirma el marco completo, los corredores conservadores main/relief (1.225/1.014 celdas) y el almacén trasladado (45 celdas de nivel 5), sin autorizar el plan. Agua, colisión y navegación siguen pendientes. Los resultados no acreditan un mapa antiguo ni juego.

## Gate y estado de publicación

El arreglo de fuente/configuración de `x00001` quedó integrado en `develop` mediante el merge certificado `75416302557adbc5648347e30ccb45dcb95f63ed`; el gate terminó verde (**164 pruebas / 2.159 aserciones**). La [verificación versionada](../qa/delendai-startup-recovery-20261105.json) y su [detalle](../qa/delendai-startup-recovery-20261105.md) confirman el landing y el smoke. `main` es la rama de release configurada y `--branch=main` selecciona la fuente del MCP DelendAI; no cambia la base de trabajo del juego, que es `develop`. El smoke con el launcher oficial del usuario, workspace y configuración canónicos, confirmó **0.1 READY, 0 block, 0 repair** y ocho hooks oficiales. El gate DelendAI `98397` finalizó exitosamente; no está activo. La aprobación formal independiente de `x00001/S1` también quedó integrada en `e513c000`. El overview 0.3 puede seguir mostrando avisos cacheados anteriores; no los tomes como diagnóstico fresco posterior al commit. Los logs crudos están archivados externamente en `/home/cartago/.codex/artifacts/aoe2-mods/delendai-startup-recovery-20261105/` y no son dependencias de este handoff.

Regla operativa: confirma el aterrizaje y estado en el recibo oficial de publicación y el commit; no infieras rama de integración a partir de `--branch=main` del launcher del MCP. El checkout del juego sigue `develop`; nunca se integra manualmente en `main`.
