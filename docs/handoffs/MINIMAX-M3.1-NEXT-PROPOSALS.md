# Backlog designado y orden de ejecución

La vista compacta vigente es [CURRENT-STATE](CURRENT-STATE.md), corte 7 de noviembre de 2026. Las tablas y cortes históricos de este archivo no asignan trabajo por sí mismos. Recupera del servidor DelendAI el estado, la ruta, aceptación y dependencias antes de cada slice. La base es develop; toda edición va en una unidad oficial aislada y se publica mediante DelendAI con su gate.

**Dirección vigente:** cerrar primero los bloqueos de arquitectura/herramientas y producir entregas privadas graduales de faith-origins/Embers of the Covenant. El catálogo actual contiene 65 dossiers y 213 selecciones sin dossier; Yavneh eleva esos contadores pero su inserción no cierra d00002/S4. El estado, roles y tres paquetes siguientes están en [CURRENT-STATE](CURRENT-STATE.md). El usuario prueba los casos de motor en Windows/Steam y es-ES; esos resultados aún no existen.

Consulta el [reparto de trabajo y volumen pendiente](LLM-WORK-ALLOCATION.md) y la [cola de paquetes](MINIMAX-M3.1-PARALLEL-QUEUE.md); ambos complementan estos IDs y estados del servidor.

## Snapshot operativo — 7 de noviembre de 2026

i00015/S2 ya está integrado (`d07fe11`) y aprobado formalmente (`e72c4a0`). x00002/S1 también está aprobado e integrado (`95cf894`, gate verde). Root trabaja i00015/S3 en una unidad aislada: el plan canónico de `develop` mantiene `privateBuildAuthorized=false`, mientras que su copia de trabajo autorizada produjo un candidato externo de seis variantes y 12 contenedores. El [ZIP candidato](</home/cartago/.codex/artifacts/aoe2-mods/jerusalem-private-geographic-preview-kit-20261107.zip>) tiene SHA-256 `37f4db30982fff05efb2290fbdacb073dd6ad0a1655ed8296aff686fdd674748`. Siguen en curso `bun run test:export` y la revisión independiente Terra. Ese paquete externo no significa que S3 esté aceptado/integrado ni que exista evidencia de juego.

d00002/S11 continúa `review`; esta actualización no aprueba ni cambia estados de propuestas. Se mantienen 65 dossiers, 213 selecciones sin dossier, 2.689 pantallas, 405 secundarios y 216 principales; una apertura histórica privada, cero campañas completas y cero episodios históricos plenamente verificados en el motor. El episodio 02 solo podrá presentarse como entrega tras completar gate, revisión e integración oficial.

## Infraestructura y arquitectura

| Propuesta | Responsable | Alcance y gate pendiente |
|---|---|---|
| i00001 Fábrica de campañas | Arquitecto; entrega integrada y revisión formal registrada | BASE READY; el fixture exportado no acredita una campaña histórica jugada |
| i00002 Inglés fuente explícito | Arquitecto; integrada | Conserva el fixture legado y los IDs |
| i00004 Naming descriptivo | Arquitecto; integrada | Producción TypeScript `<responsabilidad>.<tipo>.ts`, sin barrels ni index.ts |
| i00003 Capacidades compuestas/mapa/nativo | Arquitecto | S1 de referencia integrado; S2 geografía/transporte, S3 composición/oposición/reloj y S4 narrativa/progreso siguen pendientes. Raster y auditoría parcial no completan S2 |
| i00005 Presencia actual | Arquitecto | S1 de referencia revisado; observación/exportación/pruebas nativas siguen sus slices pendientes |
| i00006 Checkpoint intermedio | Arquitecto | S1 de referencia revisado; no prolongar el puesto intermedio hasta victoria. Nativo y alineación final conservan sus gates |
| i00007 Alternativas y reserva atómica | Arquitecto | S1 decisión aprobada; S2 referencia optativa v3 integrada en 4ac57b8f y aprobación independiente publicada en 66468212; S3 nativo/UI/motor pendiente de i00003 y s00001. El estudio económico por sí solo no implementa ningún slice |
| i00013 Cuentas finitas authored | Luna, con revisión GPT-6.1-Sol | S1/S2/S3 `done`, propuesta cerrada en `472e4d00`; no reimplementar ni reabrir por un handoff antiguo |
| i00015 Vista geográfica privada | Root S1/S3; MiniMax inicial y Luna corrección S2 | S1 `done`; S2 integrado `d07fe11` y aprobado `e72c4a0`. El build S3 candidato tiene seis variantes y 12 contenedores; su export, revisión independiente e integración siguen pendientes. La copia del plan en `develop` continúa `privateBuildAuthorized=false`; no hay aprobación histórica ni evidencia de juego |
| x00002 Ciclo de autorización privada | Arquitecto; revisión Terra | S1 aceptado e integrado en `95cf894`, gate verde. Separa autorización de build privado de aprobación histórica; no autoriza el plan canónico por sí solo |
| s00001 Compatibilidad nativa/motor | Arquitecto + tester con AoE2 | Rutas/progreso, idiomas, plantillas/audio, dificultad/rango e instalación/RoR requieren evidencia real con build/hash |
| d00002 Odiseas extensas | Arquitecto | S1 `done`; S2, S3 y S11 en revisión; S4–S10 con cambios solicitados. Ninguna aprobación histórica o de motor se infiere de los borradores |

La [matriz de asignaciones](MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md), las propuestas completas y los dossiers individuales gobiernan cada episodio. No se delegan decisiones pendientes de historia, nivelación, terreno ni contratos al agente de contenido.

## Propuestas de contenido

| Propuesta | Campaña / entrega | Extensión y estado del diseño |
|---|---|---|
| f00001 | Piloto técnico de rutas independientes | S1 especificación del arquitecto/revisión; S2 staging, S3 materialización conjunta con IDs/glosario, S4 informe; conservar su alcance acotado |
| f00002 | Piloto narrativo de Puente Milvio | Tras el piloto técnico y capacidades nativas; no abre automáticamente una saga |
| f00003 | The Eagle and the Cross | 34 selecciones y dossiers (órdenes 1–34); Constantinopla380 es ID 34, orden33/S37 |
| f00004 | Embers of the Covenant | 30 selecciones y 30 dossiers sin aprobación histórica, de terreno ni juego |
| f00005 | Keepers of the Unbroken Word | 30 selecciones; un dossier Yavneh en borrador, 29 pendientes; sin aprobación histórica |
| f00006 | The Keys of the Eternal City | 32 selecciones; ningún dossier ampliado completo |
| f00007 | Beyond the Golden Gate | 32 selecciones; ningún dossier ampliado completo |
| f00008 | Beneath the Desert Stars | 30 selecciones; ningún dossier ampliado completo |
| f00009 | The Shattered Oath | 28 selecciones; ningún dossier ampliado completo |
| f00010 | From Damascus to the Far Horizon | 32 selecciones; ningún dossier ampliado completo |
| f00011 | The River Remembers | 30 selecciones; ningún dossier ampliado completo |

Las nueve propuestas históricas conservan sus bloqueos y dependencias. Las selecciones, las biblias de narrador y una tabla no autorizan producir contenido. La propuesta de cada campaña contiene sus slices por acto/episodio y la promoción conjunta; recuperar siempre la versión integrada actual. No usar el antiguo reparto de tres misiones imperiales como instrucciones vigentes.

El brief inicial del piloto está en [00-brief](../wiki/route-pilot/00-brief.md); S1 lo revisa, S2 prepara ambos bundles y S3 los materializa junto con sus IDs. Ver [staging](../guides/staging.md). Su fuente puede prepararse antes de acreditar el motor; su entrega publicable conserva el gate de compatibilidad. No integrar campañas incompletas ni esperar IDs de un slice posterior.

## Constantinopla y criterios que no deben perderse

El [estudio de asignación finita](../design/episode-plans/imperial-church/34-care-allocation.study.md) conserva nueve combinaciones y asequibilidad all-skip de 9/7/3. El [ADR](../architecture/alternative-fulfillment.md) y la [referencia revisada](../../tests/alternative-fulfillment/reference/README.md) resuelven S1–S2; la aritmética aislada no acredita la operación nativa, el terreno ni un reto jugado. MiniMax no debe traducir alternativas a pagos fijos simultáneos ni diseñar sus identidades, costes o recorridos. Constantinopla380 ya tiene dossier de diseño ID 34 (dossier 64), con 51 pantallas y siete secundarios. Su revisión histórica/editorial, nativa, geográfica y de juego sigue pendiente; el perfil y las pantallas no son evidencia de motor.

La [comprobación de visibilidad](../qa/campaign-design/geographic-padding-and-proposal-visibility-checkpoint.md) ya confirmó en la API oficial los cuatro criterios S3 y tres S4 de i00003 después de integrar 327cc456. Conservar el reloj relativo y el control previo al briefing de Sirmio. La divergencia inicial quedó resuelta sin cambios del runtime; no se determinó su causa transitoria exacta. El 23 de octubre se confirmó formalmente i00007/S2 `done` mediante `proposal_review action=status`, con implementador GPT-6 y revisor GPT-6.1; la aprobación está integrada en 66468212. Leer siempre la propuesta completa y recuperar el estado vivo; una vista resumida o anterior no sustituye el veredicto ni desbloquea S3.

## Dependencias y cierre

La versión observada admite DependsOn dentro de slices; create_proposal no ofrece un argumento de dependencias entre propuestas. Los prerrequisitos externos figuran en su aceptación y en los bloqueos oficiales: comprobarlos explícitamente antes de actuar, sin desbloquear editando frontmatter. i00007/S3 no se vuelve implementable por completar S2 si i00003 o las pruebas de motor siguen pendientes.

Si una operación no existe, el arquitecto registra y resuelve su propuesta; MiniMax conserva el bloqueo y no fabrica un binario, un flag de pausa ni una mecánica alternativa. El contenido sigue inglés fuente y español completo, fuente histórica atribuida, narrador común objetivo antes de la persona de campaña, recomendaciones no bloqueantes y progreso acumulativo sin borrar otras rutas.

Ejecutar los [gates](MINIMAX-M3.1-QUALITY-GATES.md), solicitar revisión por modelo distinto y publicar por DelendAI. Una revisión pendiente no desaparece al cambiar de modelo. Un rechazo conserva la unidad y el motivo; no resetear ni forzar develop. No distribuir mods ni generar medios de pago masivamente sin autorización específica.

## Corte histórico de estado — 24 de octubre de 2026 (d00002/S1)

DelendAI registra **S1 `done`** y una revisión formal `approve` de GPT-6.1; la aprobación y metadatos quedaron integrados en `b9cff83e76b3eaee75cef789b5ace09a1c6b417b` (producto `924ebde2`). Se cumplieron los dos criterios formales. El arquitecto corrigió las dos familias P2 numéricas (contadores y vectores de recursos) y GPT-6.1 verificó las correcciones; la evidencia y el alcance constan en [aceptación común](../research/odyssey-research/common-architecture-acceptance.md) y [revisión independiente](../research/odyssey-research/common-architecture-independent-review.md). La verificación registrada fue 142 pruebas Bun, 2.069 aserciones y 90 pruebas de diseño; no acredita juego ni aprobación de contenido ampliado.

Este corte histórico del 24 de octubre registraba S2–S11 `pending` y 63/2.594/391. Ese estado y esos contadores se conservan como snapshot, no como asignación vigente; véase [CURRENT-STATE](CURRENT-STATE.md).

En el corte posterior, el plan de mundo de Constantinopla con 45 pantallas y siete secundarios era material auxiliar. El dossier ID 34, orden 33, integra ese material y seis pantallas UI, con 51 pantallas y siete secundarios. Consulta el [plan de mundo](../design/episode-plans/imperial-church/34-constantinople-world-plan.md) y su [revisión independiente](../research/odyssey-research/constantinople380-world-plan-luna-review.md); no son prueba de mapa jugado ni aprobación histórica.

La secuencia de MiniMax se gestiona por slices con aceptación propia: no requiere esperar a que terminen las nueve odiseas, ni desbloquea por sí sola propuestas históricas. f00001/S1, especificado por el arquitecto, está `done` tras aprobación formal independiente e integración; MiniMax aún no ha trabajado. El intento OpenCode MiniMax-M3.1-Flash del 24 de octubre fue rechazado antes de ejecutar herramientas (HTTP 429/2056, límite de Token Plan); la consulta separada de cuota OAuth MMX indicó 0 % semanal general. La sesión `ses_e90709888ffegF4vCs3Axe1zWY` no dejó ediciones. En ese corte f00001/S2 seguía pendiente de cuota para el trabajador designado; consulta el estado sincronizado al inicio de este documento. Consulta la [especificación](../wiki/route-pilot/02-implementation-specification.md) y la [matriz de aceptación](../wiki/route-pilot/03-acceptance-matrix.md); cada estado vivo lo determina DelendAI.

Esta actualización no cierra ningún slice distinto de S1.


El corte26 de octubre añade i00009/S2 aceptado e integrado (0cf4d064/9f4be255) y i00010/S1 aprobado (f4a2599). El próximo paquete de código designable es i00010/S2 conforme al [packet actualizado](POOLED-SURVIVOR-PROJECTION-PACKET.md), que incluye un fixture TypeScript artificial dentro de su Files. Recuperar esa lista integrada antes de reclamar. i00009/S3 de guía/evidencia sigue separado y no aprueba historia. No confundir la consulta MiniMax de sólo lectura con implementación; los64 dossiers permanecen en borrador.


## Estado recuperado desde la conversación externa — 26 de octubre

i00008/i00009/i00010 están cerradas en DelendAI y sus productos/revisiones se conservan. No volver a reclamar sus S1 ni repetir la revisión de i00009/S3 (MiniMax, producto 34f87ce, revisión 7cbac2b). i00003/S2 sigue pending: a7f8dcd integra solo el diagnóstico artificial 300/400, no toda la aceptación de terreno/transporte; root está acreditando su exportación de 400 × 400. d00002/S4 también sigue pending: 4a0bdab integra decisiones y texto parcial de Jerusalén, no el dossier 65.

La ausencia de [MINIMAX-M3.1-PRESENCE.md](MINIMAX-M3.1-PRESENCE.md) queda resuelta documentalmente. Es un paquete de preparación de i00005/S3, no una asignación activa: S2 y i00003/S3 siguen bloqueando la ejecución nativa. Root debe entregar operaciones reales y sus gates antes de asignarlo. La producción histórica f00003–f00011 conserva sus bloqueos; MiniMax no debe inventar el siguiente contenido para mantener actividad.
