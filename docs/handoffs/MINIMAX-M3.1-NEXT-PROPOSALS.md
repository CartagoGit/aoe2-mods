# Backlog designado y orden de ejecución

Recupera del servidor DelendAI el estado, ruta, aceptación y dependencias de cada propuesta antes de trabajar. Los IDs siguientes fueron asignados por el servidor; no son números que otro agente deba fabricar. La base de trabajo es develop y toda edición pertenece a una unidad oficial aislada. Publicación oficial y gate, sin commits manuales de develop.

**f00001/S1, piloto técnico**, fue especificado por el arquitecto, aprobado formalmente por `gpt-6-luna` e integrado (`06e688e`, metadatos `3c41b4f5`); está `done`. f00001/S2 fue implementado por `gpt-6-luna`, revisado por GPT-6 e integrado en `9d5e744b`. La consulta viva de DelendAI todavía registra f00001 `in-progress` y S2 `review`; no afirmar `done` hasta que el veredicto formal se integre en el servidor. S3 se inicia solo después de ese estado oficial. El propietario autorizó a Luna para este trabajo mecánico durante la cuota agotada de MiniMax, sin cambio de proveedor ni compra de créditos. El alcance histórico vigente son nueve odiseas y 278 selecciones: 63 dossiers, 215 selecciones sin dossier, 2.594 pantallas y 391 secundarios. La base anterior de 39 contratos conserva identidad.

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
| s00001 Compatibilidad nativa/motor | Arquitecto + tester con AoE2 | Rutas/progreso, idiomas, plantillas/audio, dificultad/rango e instalación/RoR requieren evidencia real con build/hash |
| d00002 Odiseas extensas | Arquitecto | S1 arquitectura común; S2–S10 una campaña cada uno; S11 consolidación y traspaso. Continúa en curso |

La [matriz de asignaciones](MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md), las propuestas completas y los dossiers individuales gobiernan cada episodio. No se delegan decisiones pendientes de historia, nivelación, terreno ni contratos al agente de contenido.

## Propuestas de contenido

| Propuesta | Campaña / entrega | Extensión y estado del diseño |
|---|---|---|
| f00001 | Piloto técnico de rutas independientes | S1 especificación del arquitecto/revisión; S2 staging, S3 materialización conjunta con IDs/glosario, S4 informe; conservar su alcance acotado |
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

El [estudio de asignación finita](../design/episode-plans/imperial-church/34-care-allocation.study.md) conserva nueve combinaciones y asequibilidad all-skip de 9/7/3. El [ADR](../architecture/alternative-fulfillment.md) y la [referencia revisada](../../tests/alternative-fulfillment/reference/README.md) resuelven S1–S2; la aritmética aislada no acredita la operación nativa, el terreno ni un reto jugado. MiniMax no debe traducir alternativas a pagos fijos simultáneos ni diseñar sus identidades, costes o recorridos. Constantinopla380 sigue sin dossier completo.

La [comprobación de visibilidad](../qa/campaign-design/geographic-padding-and-proposal-visibility-checkpoint.md) ya confirmó en la API oficial los cuatro criterios S3 y tres S4 de i00003 después de integrar 327cc456. Conservar el reloj relativo y el control previo al briefing de Sirmio. La divergencia inicial quedó resuelta sin cambios del runtime; no se determinó su causa transitoria exacta. El 23 de octubre se confirmó formalmente i00007/S2 `done` mediante `proposal_review action=status`, con implementador GPT-6 y revisor GPT-6.1; la aprobación está integrada en 66468212. Leer siempre la propuesta completa y recuperar el estado vivo; una vista resumida o anterior no sustituye el veredicto ni desbloquea S3.

## Dependencias y cierre

La versión observada admite DependsOn dentro de slices; create_proposal no ofrece un argumento de dependencias entre propuestas. Los prerrequisitos externos figuran en su aceptación y en los bloqueos oficiales: comprobarlos explícitamente antes de actuar, sin desbloquear editando frontmatter. i00007/S3 no se vuelve implementable por completar S2 si i00003 o las pruebas de motor siguen pendientes.

Si una operación no existe, el arquitecto registra y resuelve su propuesta; MiniMax conserva el bloqueo y no fabrica un binario, un flag de pausa ni una mecánica alternativa. El contenido sigue inglés fuente y español completo, fuente histórica atribuida, narrador común objetivo antes de la persona de campaña, recomendaciones no bloqueantes y progreso acumulativo sin borrar otras rutas.

Ejecutar los [gates](MINIMAX-M3.1-QUALITY-GATES.md), solicitar revisión por modelo distinto y publicar por DelendAI. Una revisión pendiente no desaparece al cambiar de modelo. Un rechazo conserva la unidad y el motivo; no resetear ni forzar develop. No distribuir mods ni generar medios de pago masivamente sin autorización específica.

## Corte histórico de estado — 24 de octubre de 2026 (d00002/S1)

DelendAI registra **S1 `done`** y una revisión formal `approve` de GPT-6.1; la aprobación y metadatos quedaron integrados en `b9cff83e76b3eaee75cef789b5ace09a1c6b417b` (producto `924ebde2`). Se cumplieron los dos criterios formales. El arquitecto corrigió las dos familias P2 numéricas (contadores y vectores de recursos) y GPT-6.1 verificó las correcciones; la evidencia y el alcance constan en [aceptación común](../research/odyssey-research/common-architecture-acceptance.md) y [revisión independiente](../research/odyssey-research/common-architecture-independent-review.md). La verificación registrada fue 142 pruebas Bun, 2.069 aserciones y 90 pruebas de diseño; no acredita juego ni aprobación de contenido ampliado.

S2–S11 siguen `pending`. El catálogo conserva 63 dossiers, 215 selecciones sin dossier, 2.594 pantallas y 391 objetivos secundarios; hay cero aprobaciones ampliadas. La producción histórica de MiniMax sigue bloqueada.

El plan parcial de Constantinopla, con 45 pantallas EN/es-ES y siete objetivos secundarios, está en [plan de mundo](../design/episode-plans/imperial-church/34-constantinople-world-plan.md) y su [revisión independiente](../research/odyssey-research/constantinople380-world-plan-luna-review.md). Sigue siendo un plan auxiliar, no el dossier 64; sus 45 pantallas y siete secundarios quedan fuera de los totales de 63 dossiers, 2.594 pantallas y 391 secundarios.

La secuencia de MiniMax se gestiona por slices con aceptación propia: no requiere esperar a que terminen las nueve odiseas, ni desbloquea por sí sola propuestas históricas. f00001/S1, especificado por el arquitecto, está `done` tras aprobación formal independiente e integración; MiniMax aún no ha trabajado. El intento OpenCode MiniMax-M3.1-Flash del 24 de octubre fue rechazado antes de ejecutar herramientas (HTTP 429/2056, límite de Token Plan); la consulta separada de cuota OAuth MMX indicó 0 % semanal general. La sesión `ses_e90709888ffegF4vCs3Axe1zWY` no dejó ediciones. En ese corte f00001/S2 seguía pendiente de cuota para el trabajador designado; consulta el estado sincronizado al inicio de este documento. Consulta la [especificación](../wiki/route-pilot/02-implementation-specification.md) y la [matriz de aceptación](../wiki/route-pilot/03-acceptance-matrix.md); cada estado vivo lo determina DelendAI.

Esta actualización no cierra ningún slice distinto de S1.
