# Estado actual y siguiente entrega

**Corte: 5 de noviembre de 2026.** Esta nota resume el estado operativo compartido. La fuente de verdad de propuestas, claims, unidades y revisiones es el DelendAI conectado; las cifras de cortes fechados en otros documentos describen esos snapshots anteriores.

## Catálogo y producto privado

- Nueve odiseas, 278 selecciones: 65 dossiers en borrador, 213 selecciones sin dossier, 2.689 pantallas bilingües, 405 objetivos secundarios y 216 principales.
- Geografía: 26 perfiles base + 19 suplementales = 45 perfiles únicos. Faltan 40 identidades geográficas para 58 selecciones. El manifiesto registra 50 recursos; los recursos modernos no acreditan terreno antiguo.
- Yavneh es el dossier 65. La inserción aterrizó como producto `d771747` (merges `1d59d1f` y `aa8d30d`). La revisión acotada independiente de GPT-6.1-Terra del 5 de noviembre no encontró P1/P2 en esa transformación: comprobó la preservación de los 64 dossiers previos, 43/43 checks, 24 testigos sin discrepancias y 21/21 saldos/reservas. Véase el [informe](/home/cartago/.codex/artifacts/aoe2-mods/yavneh-canonical-insertion-independent-20261105/review.md). Esta revisión no es la aprobación formal de d00002/S4 ni acepta historia, geografía, motor o juego; S4 sigue sin cerrar.
- Hay una apertura histórica privada de Embers of the Covenant en seis variantes EN/es-ES × easy/standard/hard. Hay **cero campañas completas** y **cero episodios históricos plenamente verificados en el motor**. El builder de Jerusalén solo produce el fixture sintético etiquetado y rechaza el build histórico.

## Prioridad y límites

Cerrar primero los bloqueos de arquitectura y herramientas y luego avanzar campaña a campaña, con entregas privadas progresivas de **Embers of the Covenant**. No producir ahora los 213 dossiers en masa ni trabajar las nueve campañas en paralelo. La prioridad no altera IDs, contratos, fuentes, rangos de cadenas ni identidad de campañas.

i00012/S1 e i00013/S1 están oficialmente `done` en `90948b1`; el producto de i00012 (`230173a`) ya estaba integrado, y `90948b1` integra los veredictos, no un nuevo producto. La operación de cuentas finitas de i00013 **no está disponible en develop**: i00013/S2 sigue pendiente; existe implementación WIP `bef5374` en otra unidad y GPT-6.1-Sol pidió corregir un P2 de overflow en valores derivados antes de revisar/publicar. i00014/S1 está `done`, pero solo compila un fixture sintético y no habilita un build histórico de Jerusalén. Historia, decisiones de geografía/terreno, composición nativa y pruebas de juego siguen abiertas.

En d00002, S1 está `done`; S2, S3 y S11 están en `review` y no acreditan prueba del motor. S4–S10 tienen revisión `changes_requested`; sus campañas contienen cero o un dossier canónico cada una. La revisión acotada de la inserción de Yavneh no cierra S4.

Root conserva arquitectura, decisiones históricas/geográficas, cierre de packets e integración. Luna mantiene la unidad WIP de los ocho archivos de i00013/S2 hasta resolver el overflow, pasar revisión y aterrizar el producto; no se abre otra implementación. MiniMax recibe un paquete mecánico nativo cerrado después de la decisión cartográfica de root; no inventa historia, presupuesto ni terreno. Cada producto requiere revisión de otro modelo. El usuario prueba los casos reales de motor en Windows/Steam y es-ES.

## Siguientes tres paquetes

1. **i00013/S2 — cuentas finitas de dificultad:** la operación no existe en `develop`. El código WIP `bef5374` está en corrección tras el P2 de overflow derivado; completar la corrección, obtener review independiente y gate oficial antes de tratarla como disponible. i00013/S3 sigue pendiente.
2. **i00015/S1 → S2 — vista de relieve privada:** el candidato arquitectónico `5020d0b` tiene conformidad de alcance de GPT-6.1-Terra, pero todavía no está integrado y `privateBuildAuthorized=false`. Root completa la integración y aceptación formal de S1; MiniMax solo inicia S2 después de una decisión GO explícita. El DSM moderno no aprueba terreno histórico.
3. **Jerusalén, episodio 02 de Embers:** después de cerrar herramientas y decisiones físicas, root prepara S3 y una entrega privada de dos episodios de la primera campaña. i00014/S1 solo ofrece el rechazo histórico y la compilación sintética. No se afirma aprobación histórica ni prueba de juego; el usuario realiza los casos reales de motor en Windows/Steam y es-ES cuando haya artefacto jugable.

## Gate y estado de publicación

El arreglo de fuente/configuración de `x00001` quedó integrado en `develop` mediante el merge certificado `75416302557adbc5648347e30ccb45dcb95f63ed`; el gate terminó verde (**164 pruebas / 2.159 aserciones**). El [recibo de publicación](</home/cartago/.codex/artifacts/aoe2-mods/delendai-startup-recovery-20261105/publish.stdout.json>) confirma el landing en `develop`. `main` es la rama de release configurada y `--branch=main` selecciona la fuente del MCP DelendAI; no cambia la base de trabajo del juego, que es `develop`. El smoke con el launcher oficial del usuario, workspace y configuración canónicos, confirmó **0.1 READY, 0 block, 0 repair** y ocho hooks oficiales. Sus recibos son [JSON](/home/cartago/.codex/artifacts/aoe2-mods/delendai-startup-recovery-20261105/verified-launcher-smoke.json) y [stderr](/home/cartago/.codex/artifacts/aoe2-mods/delendai-startup-recovery-20261105/verified-launcher.stderr.log). El gate DelendAI `98397` finalizó exitosamente; no está activo. No se declara aquí aprobación formal de `x00001`. El overview 0.3 puede seguir mostrando avisos cacheados anteriores; no los tomes como diagnóstico fresco posterior al commit.

Regla operativa: confirma el aterrizaje y estado en el recibo oficial de publicación y el commit; no infieras rama de integración a partir de `--branch=main` del launcher del MCP. El checkout del juego sigue `develop`; nunca se integra manualmente en `main`.
