# Backlog designado y orden de ejecución

Estos IDs fueron creados por el servidor el 2026-10-12. Son referencias observadas, no IDs que el agente deba fabricar. Recupera sus estados, rutas y dependencias actuales de DelendAI; las transiciones oficiales pueden cambiar la ubicación.

Estado de entrega: i00001 done, revisada formalmente por gpt-6.1-sol e integrada. f00001 ready; comenzar únicamente S1. s00001/f00002/f00003 siguen blocked por pruebas de motor y dependencias de contenido. BASE READY no supone GAME VERIFIED.

| Propuesta observada | Responsable | Slices y dependencia |
|---|---|---|
| i00001 Fábrica de campañas | Arquitecto | S1 infraestructura, auditoría, revisión e integración |
| s00001 Compatibilidad nativa/motor | Arquitecto + tester con AoE2 | S1 progreso/rutas; S2 locales/coexistencia; S3 plantillas/audio; S4 dificultad/rango; S5 instalación y experimento RoR |
| f00001 Piloto técnico de rutas | M3.1 contenido | S1 dossier; S2 bundles en staging; S3 materialización conjunta/IDs/glosario; S4 informe. Tras i00001 revisada/integrada |
| f00002 Piloto Puente Milvio | M3.1 contenido | S1 evidencia; S2 bundle en staging; S3 materialización/IDs/glosario; S4 QA. Tras piloto técnico revisado y capacidades de motor acreditadas |
| f00003 Iglesia imperial 312–337 | M3.1 contenido | S1 dossier; S2 metadatos en staging; S3 batalla312; S4 diplomacia325; S5 economía330 y bundle completo; S6 materialización/IDs/QA. Tras pilotos y adaptación necesaria |

El brief inicial está en docs/wiki/route-pilot/00-brief.md; S1 lo revisa, S2 prepara ambos bundles y S3 los materializa junto a sus IDs. Las matrices tests/compatibility/*.json son planes pendientes. Seguir [staging](../guides/staging.md); ninguna entrega integra campañas incompletas ni espera IDs de un slice posterior.

La primera tarea que se asignará a M3.1 es S1 del piloto técnico. Sigue la propuesta completa y el brief, sin decidir nuevos formatos. Es posible crear fuentes del piloto antes de acreditar el motor; su entrega publicable permanece bloqueada hasta la compatibilidad. El piloto histórico no desbloquea la campaña futura por su mera existencia.

## Dependencias de contenido y de infraestructura

La coexistencia lingüística, rango de cadenas y plantillas nativas son decisiones del arquitecto con evidencia del juego. Un gate local no las confirma. s00001 requiere un tester con instalación legal de AoE2 y versión registrada. No delegar en M3.1 la afirmación de que estas capacidades funcionan sin probarlas.

Si la mecánica histórica del brief requiere condiciones/efectos que no están en el DSL actual (diálogo UI propio, conquista/economía compleja, navegación), abrir una propuesta de ampliación de infraestructura con contratos y round-trip antes de autoría de ese escenario. M3.1 registra la necesidad; el arquitecto la implementa y revisa. No sustituir dichas mecánicas por un temporizador silencioso.

## Desbloqueo y cierre

Las dependencias están descritas en las propuestas y este registro; la versión instalada admite DependsOn dentro de slices, pero no un argumento de dependencias entre propuestas en create_proposal. Usa estados oficiales bloqueados y motivo explícito mientras sus requisitos falten. No editar frontmatter para desbloquear.

Una revisión independiente pendiente no desaparece al cambiar de modelo. Un lock caducado se consulta y reclama de nuevo con la identidad correcta. La integración se efectúa solo por work publish según el servidor; un rechazo conserva la unidad y documenta la condición necesaria. Consultar audit antes de empezar.

## Ampliación de diseño vigente

El usuario ha fijado inglés como fuente inicial y un catálogo de nueve campañas/39escenarios. La planificación específica está en [catálogo](../design/README.md), [contrato](../design/production-contract.md) y [asignaciones porcampaña](MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md). Esos dossiers sustituyen los briefs provisionales en decisiones editoriales; conservan IDs existentes y los gates de pilotos/capacidades/motor. MiniMax verifica y materializa, no diseña historia, narradores, mapas ni nuevas economías. Recuperar estados oficiales antes de elegir slice.
