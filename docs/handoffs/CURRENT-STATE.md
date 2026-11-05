# Estado actual y siguiente entrega

**Corte: 5 de noviembre de 2026.** Esta nota resume el estado operativo compartido. La fuente de verdad de propuestas, claims, unidades y revisiones es el DelendAI conectado; las cifras de cortes fechados en otros documentos describen esos snapshots anteriores.

## Catálogo y producto privado

- Nueve odiseas, 278 selecciones: 65 dossiers en borrador, 213 selecciones sin dossier, 2.689 pantallas bilingües, 405 objetivos secundarios y 216 principales.
- Geografía: 26 perfiles base + 19 suplementales = 45 perfiles únicos. Faltan 40 identidades geográficas para 58 selecciones. El manifiesto registra 50 recursos; los recursos modernos no acreditan terreno antiguo.
- Yavneh es el dossier 65. La inserción aterrizó como producto `d771747` (merges `1d59d1f` y `aa8d30d`). La revisión acotada independiente de GPT-6.1-Terra del 5 de noviembre no encontró P1/P2 en esa transformación: comprobó la preservación de los 64 dossiers previos, 43/43 checks, 24 testigos sin discrepancias y 21/21 saldos/reservas. Véase el [informe](/home/cartago/.codex/artifacts/aoe2-mods/yavneh-canonical-insertion-independent-20261105/review.md). Esta revisión no es la aprobación formal de d00002/S4 ni acepta historia, geografía, motor o juego; S4 sigue sin cerrar.
- Hay una apertura histórica privada de Embers of the Covenant en seis variantes EN/es-ES × easy/standard/hard. Hay **cero campañas completas** y **cero episodios históricos plenamente verificados en el motor**. El builder de Jerusalén solo produce el fixture sintético etiquetado y rechaza el build histórico.

## Prioridad y límites

Cerrar primero los bloqueos de arquitectura y herramientas y luego avanzar campaña a campaña, con entregas privadas progresivas de **Embers of the Covenant**. No producir ahora los 213 dossiers en masa ni trabajar las nueve campañas en paralelo. La prioridad no altera IDs, contratos, fuentes, rangos de cadenas ni identidad de campañas.

La arquitectura de cuentas finitas i00013/S1 sigue pendiente de revisión/aceptación independiente y formal; i00013/S2 no está implementada. i00012 sigue en review. i00014/S1 está `done`, pero solo compila un fixture sintético y no habilita un build histórico de Jerusalén. Historia, decisiones de geografía/terreno, composición nativa y pruebas de juego siguen abiertas.

Root conserva arquitectura, decisiones históricas/geográficas, cierre de packets e integración. Luna puede implementar los ocho archivos de i00013/S2 únicamente después de la aceptación de i00013/S1. MiniMax recibe un paquete mecánico nativo cerrado después de la decisión cartográfica de root; no inventa historia, presupuesto ni terreno. Cada producto requiere revisión de otro modelo. El usuario prueba los casos reales de motor en Windows/Steam y es-ES.

## Siguientes tres paquetes

1. **i00012 — reutilización local de proyección:** slice S1 en review. La aceptación formal y el gate sobre el producto exacto siguen pendientes; no es una mejora de rendimiento general ni un desbloqueo de contenido histórico.
2. **i00013 — cuentas finitas de dificultad:** revisar y aceptar S1; solo después comenzar S2, asignado a Luna. La operación de fábrica aún no existe y ningún dossier usa este modo como funcional.
3. **Jerusalén, episodio 02 de Embers:** root cierra la arquitectura de datos geográficos privados, la decisión de geografía/terreno y el binding físico; después entrega a MiniMax el paquete nativo mecánico. i00014/S1 solo ofrece el rechazo histórico y la compilación sintética; el juego y la aprobación histórica continúan pendientes. La prueba del usuario llega tras una entrega privada que sí pueda construir un episodio histórico.

## Gate y estado de publicación

El 5 de noviembre root confirmó el arreglo de configuración de `x00001` en `main` (`75416302557adbc5648347e30ccb45dcb95f63ed`), el gate real verde (**164 pruebas / 2.159 aserciones**) y el smoke del host `main` listo, con ocho hooks oficiales. El producto fuente está pendiente de publicación/integración; por tanto, no se declara `x00001` aprobado ni integrado. El gate DelendAI de publicación `98397` está activo. Root confirmó que `develop` no se cambió con ese arreglo. El overview 0.3 puede seguir mostrando avisos cacheados de la configuración anterior; no los tomes como lectura fresca posterior al commit.
