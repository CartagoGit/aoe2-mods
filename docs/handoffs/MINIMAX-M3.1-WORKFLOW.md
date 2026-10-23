# Trabajo y recuperación de contexto

## Ciclo de un slice

Descubrir estado → comprobar dependencias → entrar en unidad desde develop → reclamar archivos → leer brief/fuentes → implementar contenido → validar → revisión técnica independiente → publicar por el gate oficial → aprobación formal del hash integrado desde unidad review de otro modelo → cierre oficial. Las operaciones proceden del catálogo vivo de DelendAI, no de nombres copiados de un chat. Ver docs/guides/delendai.md: el runtime actual rechaza aprobar commits que aún no están en develop.

Los slices de dossier, borradores y QA tienen propiedad diferenciada. Preparar contenido en staging/campaigns; el slice de materialización posee simultáneamente campañas completas, borradores, IDs y glosario, y los integra juntos. Seguir [staging](../guides/staging.md): staging:check --partial declara pendientes; sin --partial exige fuentes completas. Todos los slices mantienen bun run validate verde; serializar la modificación del registro global. Un gate e2e significa ejecutar el alcance declarado y documentar las pruebas de motor pendientes.

Los commits de una unidad se realizan con Git dentro de ese worktree; work checkpoint desde un servidor anclado al checkout compartido no captura otro worktree. Consulta el esquema y el workflow actual antes de usarlo.

Cada checkpoint contiene: propuesta/slice, archivos editados, commit, resultados reales, limitación, siguiente acción y locks vigentes. No guardar secretos, rutas personales ni sesiones del proveedor de voz en documentos compartidos. Renovar el heartbeat según el runtime y liberar el lock al finalizar.

## Prompt de continuación completo

```text
Continúa como MiniMax M3.1 en Crónicas de la Fe sin asumir que el chat anterior sigue vigente. Lee AGENTS.md, README.md, docs/qa/audit.md y los cinco handoffs. Recupera Git y el estado vivo de DelendAI: rama develop, unidad propia, propuesta/slice, dependencias, locks, último checkpoint, revisión y resultados del gate. Declara tu identidad real.

Si existe una unidad pendiente propia, inspecciona sus cambios y commit antes de abrir otra. Conserva cambios ajenos. Si la unidad se retiró, utiliza la recuperación oficial y su ref conservada; no recrees ni pierdas el trabajo. Verifica la base develop antes de implementar.

Localiza la siguiente tarea de contenido designada en NEXT-PROPOSALS, comprobando IDs y estados actuales. Continúa solo el slice permitido y listo. Lee su propuesta, brief, fuentes y acceptance. Reutiliza contratos y compiladores existentes; no cambies arquitectura ni config global fuera de su slice. Si una dependencia/revisión/prueba de motor falta, registra la causa y la tarea responsable, sin declarar que se superó.

Sigue WORKFLOW y QUALITY-GATES: evidencia histórica, narradores diferenciados, sourceLocale=en y español completo, IDs permanentes, 17 locales, derechos de medios, voces offline, objetivos/recuperación, economía finita, dificultades y QA. Ejecuta validación y exportación según el cambio. Vincula el QA del motor al ZIP probado y su hash; invalida la evidencia si cambia el artefacto.

Prepara los borradores en staging/campaigns y sigue docs/guides/staging.md. Incorpora campañas, escenarios, catálogos, lock de IDs y glosario juntos únicamente en el slice de materialización que posee esas rutas. No crees una carpeta activa con referencias pendientes ni claves sin ID. El gate global permanece verde en cada entrega.

Presenta la entrega a revisión independiente y publica exclusivamente mediante DelendAI. No autoaprobar, no editar estados manualmente ni hacer commits/push de develop. Deja checkpoint y reporte del slice; continúa con el siguiente solo cuando sus dependencias estén satisfechas. La publicación pública y generación masiva pagada siguen requiriendo autorización específica.
```

## Cierre verificable

El reporte distingue pruebas estáticas, round-trip, observaciones del juego y revisiones humanas. Indica el hash exacto revisado, versión del juego y plataforma cuando corresponda. Una propuesta de contenido no cierra PRODUCTION READY con solo unit tests; una propuesta de infraestructura no cierra su revisión con una autoaprobación.

## Ampliación de diseño vigente

El encargo vigente usa inglés como fuente inicial y nueve odiseas con 278 episodios seleccionados; los 39 contratos del catálogo previo conservan su identidad. La planificación específica está en [catálogo](../design/README.md), [contrato](../design/production-contract.md) y [asignaciones porcampaña](MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md). Esos dossiers sustituyen los briefs provisionales en decisiones editoriales; conservan IDs existentes y los gates de pilotos/capacidades/motor. MiniMax verifica y materializa, no diseña historia, narradores, mapas ni nuevas economías. Recuperar estados oficiales antes de elegir slice.


## Integridad de los criterios servidos

En el runtime observado, los ítems indentados de cada lista `acceptance` deben permanecer contiguos: una línea en blanco termina su lectura en la vista de slices. Los requisitos de reloj relativo de Sirmio y control previo al briefing ya existían en i00003, pero dos líneas vacías los ocultaban. El arquitecto corrigió únicamente esa separación, sin alterar sus textos, frontmatter, estados, dependencias o firmas de revisión. El parser instalado reconoce ahora cuatro criterios en S3 y tres en S4; la vista del servidor debe comprobarse tras la integración oficial. Leer también el documento completo: una vista reducida no autoriza a omitir un requisito visible en la fuente ni a inventar una operación nativa.


Constantinopla380 continúa sin dossier completo. El arquitecto ha preparado un [estudio de asignación finita](../design/episode-plans/imperial-church/34-care-allocation.study.md) y DelendAI ha creado [i00007](../delendai/proposals/ready/infras/i00007-alternative-fulfillment-plans-with-atomic-reservation-and-persistent-recipe-identity.md) para decidir y acreditar la capacidad faltante de selección/reserva de alternativas. La enumeración económica 9/7/3 no es una operación del adaptador ni nivelación jugada. MiniMax no debe convertirla en pagos fijos simultáneos, decidir sus mapas ni diseñar contratos. El catálogo conserva 63 dossiers y 215 selecciones sin expediente completo.

La [comprobación de visibilidad](../qa/campaign-design/geographic-padding-and-proposal-visibility-checkpoint.md) confirmó después de la integración 327cc456 que la API oficial ya muestra los cuatro criterios S3 y tres S4 de i00003, incluidos reloj relativo y control previo al briefing de Sirmio. La divergencia inicial quedó resuelta sin cambios del runtime. i00007 también aparece en el servidor con sus tres slices pendientes. Ninguna de esas lecturas acredita implementación nativa ni aprobación de contenido.
