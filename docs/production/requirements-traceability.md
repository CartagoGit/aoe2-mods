# Trazabilidad del encargo

La versión final de la conversación guía este alcance. Las propuestas descartadas del gestor externo/bloqueo de misiones no son requisitos actuales. Esta tabla identifica implementación y límites; un requisito de producción no se da por cumplido solo por tener un esquema.

| Apartado del prompt original | Entrega verificable | Pendiente/responsable |
|---|---|---|
| 1 Alcance/filosofía | README, vision, plan, mods independientes, enforceRequirement=false | Producción de campañas en propuestas posteriores |
| 2 Investigación previa | research/aoe2-capabilities, toolchain fijada, parser real | s00001 acredita motor/DLC/RoR |
| 3 Tecnologías | Bun/TS estricto/Zod/Python, ADR0001 | CI de otros SO pendiente de ejecución remota |
| 4 Repositorio | Módulos reales por dominio, CLI, fixture, documentación/wiki | Sin carpetas de productos vacíos |
| 5 Naming/IDs | standards/naming, localization allocate/lock | Rango de fixture requiere acreditación s00001-S4 |
| 6 Traducción | UTF8, catálogo global, claves/variables/glosario, export individual | 17 revisiones y convivencia: f00001 + s00001-S2 |
| 7 Dos narradores | Contratos/validación de estructura, guía y dossier | Casting/doblaje real: piloto narrativo |
| 8 Audio | Interfaces grabado/local, caché con hash, PCM/normalización pico/SRT, CLI | Voicing y rutas del juego s00001-S3; no backend pago supuesto |
| 9 Visuales | Manifest/derechos/hash/PNG y rutas contenidas | Ilustraciones/capas/aprobación por campaña; no decoder PNG completo |
| 10 Historia/religión | Clasificación y referencias, plantillas, dossier imperial-church | Lectura/contraste/editorial: f00002-S1/f00003-S1 |
| 11 Progresión | Rutas acumulativas, terminal, Store Key, condición recomendación | Cruce mods/save-load/rutas: s00001-S1 |
| 12 Escenarios | Contrato/DSL/IR/binarios/mapas/objetivos/QA | Pathfinding del motor; operaciones nuevas requieren propuesta infra |
| 13 IA | PER explícito, economía declarada, selección inicial y reservas finitas | i00003/S3: IA local acotada, adquisición/alcance/regreso y guardado; no se acredita un leash contando unidades |
| 14 Dificultad | Tres perfiles, recursos/reacción, XS validado sintácticamente | Mapeo/runtime y balance: s00001-S4/pilotos |
| 15 QA/exploits | Validadores, tests adversariales, catálogo/matriz | Exploits reales/save-load/rendimiento: tester por hash |
| 16 DelendAI | Adopción real, unidades desde develop, locks, propuestas y gate oficial activo | Revisión independiente y publicación por cada entrega; no integración manual |
| 17 Comandos | package.json, desarrollo, fixtures; errores reales | release exige candidato y evidencia, no éxito vacío |
| 18 Git/CI/calidad | WIP desde develop, integraciones oficiales acreditadas y configuración CI de tres SO | CI remoto y compatibilidad de otras plataformas requieren su propia ejecución |
| 19 Documentación | Arquitectura/ADR/naming/guías/wiki/QA/handoffs españoles | Se actualiza junto a cambios, no copia narrativa duplicada |
| 20 Fases | production/plan y aceptación de infraestructura | Fase de motor posterior acreditada |
| 21 Condición estricta | audit y niveles independientes | No declarar BASE READY sin revisión ni PRODUCTION READY sin motor |
| 22 Traspaso | Handoffs y piloto acotado con infraestructura integrada/revisada | Autoría histórica bloqueada por d00002, capacidades nativas, geografía, fuentes y juego; no confundirla con el piloto |
| 23 Informe | qa/audit con comandos/resultados/limitaciones/propuestas | Cierre e integración se registran tras herramientas oficiales |

Los tests verifican contratos y comportamientos concretos, no verdad historiográfica, traducción natural, percepción de dificultad o integridad jurídica de una licencia. Esas revisiones forman parte de cada propuesta de contenido y quedan separadas de la automatización.


## Ampliación de odiseas y requisitos observados

El alcance seleccionado es278episodios. El [plan vigente](../design/odyssey-production-plan.md) distingue selección, dossier, revisión técnica, revisión histórica y pruebas reales; un número de pantallas no concede permiso de autoría. La [asignación por campaña y slice](../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md) conserva los IDs, fechas, voces, continuidad y reglas mecánicas.

| Requisito nuevo | Evidencia o reproducción | Propietario y gate pendiente |
|---|---|---|
| Solo originales vivos en lugar actual, sin sustituirlos por visitas pasadas | i00005/S1 integrado/revisado; [contrato](../design/live-entity-presence.md) | i00005/S2–S3: observador nativo y promoción con motor |
| Reunión intermedia que permita retirarse a otro receptor | [Referencia checkpoint revisada](../qa/campaign-design/checkpoint-presence-independent-review.md), i00006/S1 integrada/aprobada en4248102; opt-in de Adrianópolis [reevaluado hasta victoria](../qa/campaign-design/imperial32-independent-review-round2.md) | i00006/S2–S3: observer nativo y promoción; IA, geografía y pruebas AoE2 pendientes |
| Mapas regionales con relieve y rutas coherentes | [Adrianópolis378](../research/odyssey-research/adrianople378-relief-design.md), DSM moderno verificado; no terreno antiguo aprobado | d00002más i00003/S2: fase arqueológica, hidrología, pendientes, footprints y navegación real |
| Dificultad con decisiones y recuperación | [Aceptación de jugabilidad](../design/civic-playability-acceptance.md), auditorías mecánicas fechadas | Arquitecto/tester: planes viables, coste de oportunidad y partidas por dificultad; menos trabajadores no basta |
| Fuentes, voces y desenlaces históricos separados del juego local | Auditorías por episodio y biblias de narrador, ficción marcada | Revisión histórica/editorial independiente y expediente completo antes de MiniMax |

Las capacidades pendientes se registran como requisitos, sin emularlas mediante flags o temporizadores. Sus propuestas y entregas se consultan en DelendAI; esta tabla no cambia estados ni aprueba trabajo propio.
