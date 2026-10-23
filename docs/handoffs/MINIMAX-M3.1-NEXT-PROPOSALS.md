# Backlog designado y orden de ejecución

Recupera del servidor DelendAI el estado, ruta, aceptación y dependencias de cada propuesta antes de trabajar. Los IDs siguientes fueron asignados por el servidor; no son números que otro agente deba fabricar. La base de trabajo es develop y toda edición pertenece a una unidad oficial aislada. Publicación oficial y gate, sin commits manuales de develop.

La primera tarea designada para MiniMax continúa siendo **f00001/S1, piloto técnico**, si su estado vivo lo permite. El alcance histórico vigente son nueve odiseas, 278 selecciones y cinco actos por campaña. Hay 63 dossiers de diseño redactados, 215 selecciones sin dossier y ninguna aprobación ampliada de juego. La base anterior de 39 contratos conserva identidad; no es la extensión final del catálogo.

## Infraestructura y arquitectura

| Propuesta | Responsable | Alcance y gate pendiente |
|---|---|---|
| i00001 Fábrica de campañas | Arquitecto; entrega integrada y revisión formal registrada | BASE READY; el fixture exportado no acredita una campaña histórica jugada |
| i00002 Inglés fuente explícito | Arquitecto; integrada | Conserva el fixture legado y los IDs |
| i00004 Naming descriptivo | Arquitecto; integrada | Producción TypeScript `<responsabilidad>.<tipo>.ts`, sin barrels ni index.ts |
| i00003 Capacidades compuestas/mapa/nativo | Arquitecto | S1 de referencia integrado; S2 geografía/transporte, S3 composición/oposición/reloj y S4 narrativa/progreso siguen pendientes. Raster y auditoría parcial no completan S2 |
| i00005 Presencia actual | Arquitecto | S1 de referencia revisado; observación/exportación/pruebas nativas siguen sus slices pendientes |
| i00006 Checkpoint intermedio | Arquitecto | S1 de referencia revisado; no prolongar el puesto intermedio hasta victoria. Nativo y alineación final conservan sus gates |
| i00007 Alternativas y reserva atómica | Arquitecto | S1 decisión explícita; S2 referencia/compilador solo tras decisión; S3 nativo/UI/motor con prerrequisitos externos. Ningún slice implementado por el estudio económico |
| s00001 Compatibilidad nativa/motor | Arquitecto + tester con AoE2 | Rutas/progreso, idiomas, plantillas/audio, dificultad/rango e instalación/RoR requieren evidencia real con build/hash |
| d00002 Odiseas extensas | Arquitecto | S1 arquitectura común; S2–S10 una campaña cada uno; S11 consolidación y traspaso. Continúa en curso |

La [matriz de asignaciones](MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md), las propuestas completas y los dossiers individuales gobiernan cada episodio. No se delegan decisiones pendientes de historia, nivelación, terreno ni contratos al agente de contenido.

## Propuestas de contenido

| Propuesta | Campaña / entrega | Extensión y estado del diseño |
|---|---|---|
| f00001 | Piloto técnico de rutas independientes | S1 dossier, S2 staging, S3 materialización conjunta con IDs/glosario, S4 informe; conservar su alcance acotado |
| f00002 | Piloto narrativo de Puente Milvio | Tras el piloto técnico y capacidades nativas; no abre automáticamente una saga |
| f00003 | The Eagle and the Cross | 34 selecciones, 33 dossiers (órdenes 1–32 y 34). Constantinopla380, orden33/S37, continúa sin dossier completo |
| f00004 | Embers of the Covenant | 30 selecciones y 30 dossiers sin aprobación histórica, de terreno ni juego |
| f00005 | Keepers of the Unbroken Word | 30 selecciones; ningún dossier ampliado completo |
| f00006 | The Keys of the Eternal City | 32 selecciones; ningún dossier ampliado completo |
| f00007 | Beyond the Golden Gate | 32 selecciones; ningún dossier ampliado completo |
| f00008 | Beneath the Desert Stars | 30 selecciones; ningún dossier ampliado completo |
| f00009 | The Shattered Oath | 28 selecciones; ningún dossier ampliado completo |
| f00010 | From Damascus to the Far Horizon | 32 selecciones; ningún dossier ampliado completo |
| f00011 | The River Remembers | 30 selecciones; ningún dossier ampliado completo |

Las nueve propuestas históricas conservan sus bloqueos y dependencias. Las selecciones, las biblias de narrador y una tabla no autorizan producir contenido. La propuesta de cada campaña contiene sus slices por acto/episodio y la promoción conjunta; recuperar siempre la versión integrada actual. No usar el antiguo reparto de tres misiones imperiales como instrucciones vigentes.

El brief inicial del piloto está en [00-brief](../wiki/route-pilot/00-brief.md); S1 lo revisa, S2 prepara ambos bundles y S3 los materializa junto con sus IDs. Ver [staging](../guides/staging.md). Su fuente puede prepararse antes de acreditar el motor; su entrega publicable conserva el gate de compatibilidad. No integrar campañas incompletas ni esperar IDs de un slice posterior.

## Constantinopla y criterios que no deben perderse

El [estudio de asignación finita](../design/episode-plans/imperial-church/34-care-allocation.study.md) tiene nueve combinaciones y asequibilidad all-skip de 9/7/3. i00007 registra la operación faltante; esa aritmética no implementa una elección, reserva, terreno ni reto jugado. MiniMax no debe traducirla a pagos fijos simultáneos ni diseñar sus identidades, costes o recorridos.

La [comprobación de visibilidad](../qa/campaign-design/geographic-padding-and-proposal-visibility-checkpoint.md) ya confirmó en la API oficial los cuatro criterios S3 y tres S4 de i00003 después de integrar 327cc456. Conservar el reloj relativo y el control previo al briefing de Sirmio. La divergencia inicial quedó resuelta sin cambios del runtime; no se determinó su causa transitoria exacta. i00007 también es visible como ready con sus tres slices pendientes. Leer siempre la propuesta integrada completa y recuperar el estado vivo; visibilidad no equivale a implementación ni aprobación.

## Dependencias y cierre

La versión observada admite DependsOn dentro de slices; create_proposal no ofrece un argumento de dependencias entre propuestas. Los prerrequisitos externos figuran en su aceptación y en los bloqueos oficiales: comprobarlos explícitamente antes de actuar, sin desbloquear editando frontmatter. i00007/S3 no se vuelve implementable por completar S2 si i00003 o las pruebas de motor siguen pendientes.

Si una operación no existe, el arquitecto registra y resuelve su propuesta; MiniMax conserva el bloqueo y no fabrica un binario, un flag de pausa ni una mecánica alternativa. El contenido sigue inglés fuente y español completo, fuente histórica atribuida, narrador común objetivo antes de la persona de campaña, recomendaciones no bloqueantes y progreso acumulativo sin borrar otras rutas.

Ejecutar los [gates](MINIMAX-M3.1-QUALITY-GATES.md), solicitar revisión por modelo distinto y publicar por DelendAI. Una revisión pendiente no desaparece al cambiar de modelo. Un rechazo conserva la unidad y el motivo; no resetear ni forzar develop. No distribuir mods ni generar medios de pago masivamente sin autorización específica.
