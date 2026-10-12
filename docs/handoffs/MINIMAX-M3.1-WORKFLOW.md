# Trabajo y recuperación de contexto

## Ciclo de un slice

Descubrir estado → comprobar dependencias → entrar en unidad desde develop → reclamar archivos → leer brief/fuentes → implementar contenido → validar → entregar evidencia → revisión independiente → publicar oficialmente → registrar cierre. Las operaciones proceden del catálogo vivo de DelendAI, no de nombres copiados de un chat.

Los slices de dossier, contenido, registro global y QA tienen propiedad diferenciada. Los IDs/glosario se modifican en una unidad que los reclame; si dos campañas necesitan cambiarlos, serializa ese trabajo. No adelantes un slice dependiente del contenido que todavía no existe. Un gate e2e de una propuesta significa ejecutar el alcance declarado, no simular AoE2 cuando no está disponible.

Los commits de una unidad se realizan con Git dentro de ese worktree; work checkpoint desde un servidor anclado al checkout compartido no captura otro worktree. Consulta el esquema y el workflow actual antes de usarlo.

Cada checkpoint contiene: propuesta/slice, archivos editados, commit, resultados reales, limitación, siguiente acción y locks vigentes. No guardar secretos, rutas personales ni sesiones del proveedor de voz en documentos compartidos. Renovar el heartbeat según el runtime y liberar el lock al finalizar.

## Prompt de continuación completo

```text
Continúa como MiniMax M3.1 en Crónicas de la Fe sin asumir que el chat anterior sigue vigente. Lee AGENTS.md, README.md, docs/qa/audit.md y los cinco handoffs. Recupera Git y el estado vivo de DelendAI: rama develop, unidad propia, propuesta/slice, dependencias, locks, último checkpoint, revisión y resultados del gate. Declara tu identidad real.

Si existe una unidad pendiente propia, inspecciona sus cambios y commit antes de abrir otra. Conserva cambios ajenos. Si la unidad se retiró, utiliza la recuperación oficial y su ref conservada; no recrees ni pierdas el trabajo. Verifica la base develop antes de implementar.

Localiza la siguiente tarea de contenido designada en NEXT-PROPOSALS, comprobando IDs y estados actuales. Continúa solo el slice permitido y listo. Lee su propuesta, brief, fuentes y acceptance. Reutiliza contratos y compiladores existentes; no cambies arquitectura ni config global fuera de su slice. Si una dependencia/revisión/prueba de motor falta, registra la causa y la tarea responsable, sin declarar que se superó.

Sigue WORKFLOW y QUALITY-GATES: evidencia histórica, narradores diferenciados, canonical es-ES, IDs permanentes, 17 locales, derechos de medios, voces offline, objetivos/recuperación, economía finita, dificultades y QA. Ejecuta validación y exportación según el cambio. Vincula el QA del motor al ZIP probado y su hash; invalida la evidencia si cambia el artefacto.

Presenta la entrega a revisión independiente y publica exclusivamente mediante DelendAI. No autoaprobar, no editar estados manualmente ni hacer commits/push de develop. Deja checkpoint y reporte del slice; continúa con el siguiente solo cuando sus dependencias estén satisfechas. La publicación pública y generación masiva pagada siguen requiriendo autorización específica.
```

## Cierre verificable

El reporte distingue pruebas estáticas, round-trip, observaciones del juego y revisiones humanas. Indica el hash exacto revisado, versión del juego y plataforma cuando corresponda. Una propuesta de contenido no cierra PRODUCTION READY con solo unit tests; una propuesta de infraestructura no cierra su revisión con una autoaprobación.
