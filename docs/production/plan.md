# Plan maestro de producción

El encargo consiste en construir la fábrica antes de entregar a MiniMax M3.1 la creación de contenido. La última decisión de la conversación reemplaza el gestor externo por mods independientes y recomendaciones opcionales. No se construirán ahora sagas históricas completas.

## Secuencia y entregables

| Fase | Trabajo | Evidencia exigida |
|---|---|---|
| 0 | Adopción DelendAI, investigación y corrección de supuestos | Capacidades fechadas, fuentes, incertidumbres y propuesta oficial |
| 1 | Arquitectura, naming, contratos, IDs y esquema de escenarios | Tipado estricto, JSON Schema y fixtures válidos |
| 2 | CLI, compiladores, localización e historia | Casos positivos y negativos, IDs estables, referencias cerradas |
| 3 | Gameplay, QA, voz, recursos y adaptadores | Reserva finita, conectividad abstracta, WAV/hash/licencia, round-trip real |
| 4 | Estándares, plantillas wiki y pilotos especificados | Dossier histórico con afirmaciones clasificadas, diseño de misiones |
| 5 | Auditoría, integración y traspaso | Gates, revisión independiente, backlog con slices y prompts |
| 6 | Pruebas en AoE2 y producción de contenido | Capturas, build del juego, idioma, dificultad, hash y QA por artefacto |

No cerrar un hito por tener carpetas. Las fases 0–5 entregan herramientas reales y prueban sus límites; las pruebas de motor no se reemplazan por tests estáticos. La fase 6 requiere el juego y queda gobernada por propuestas de compatibilidad y contenido.

## Decisiones fijadas

JSON UTF-8 sin BOM para fuentes, módulos TypeScript por dominio sin npm packages vacíos, Python fijado para AoE2ScenarioParser, herramienta externa rge_campaign fijada por commit/hash. El archivo campaña referencia cada escenario por ruta; los escenarios tienen carpetas ordenadas. No Angular ni servicios permanentes.

Semántica de victoria acumulativa: cada ruta escribe su clave a 1; nunca elimina otras. CampaignVariable solo decide mensajes narrativos, no permisos. Toda campaña incluye recapitulación y explicación del orden recomendado.

La base de cada trabajo es develop. El WIP inicial incorporó explícitamente el commit de setup de develop tras la corrección del usuario; no se reescribió historia ni se perdió trabajo.

## Estados de preparación

BASE READY: arquitectura, contratos, CLI, validadores, docs y tests pasan, y la revisión de infraestructura está resuelta. EXPORT READY: archivos binarios del perfil implementado hacen round-trip; no equivale a cutscenes/audio/IA económica verificados. GAME VERIFIED: motor real probado con versión y hash. PRODUCTION READY: contenido, 17 textos revisados, medios, derechos y QA superan release.

Si falta una capacidad, su propuesta queda diferenciada de las tareas de contenido. M3.1 no decidirá arquitectura ni ampliará alcance por su cuenta. La tabla de trazabilidad enlaza cada requisito con código, prueba o evidencia pendiente.

Los slices de contenido preparan borradores en staging/campaigns y los materializan completos junto a IDs/glosario en un slice con propiedad conjunta. Cada integración mantiene el gate global pasando; ver [preparación](../guides/staging.md). Esta secuencia evita referencias pendientes y catálogos sin IDs entre entregas.

## Ampliación solicitada: diseño de todas las campañas

El propietario exige ahora planificación individual de las nueve campañas explícitas del catálogo: ver [índice](../design/README.md) y [contrato de producción](../design/production-contract.md). La implementación del diseño comprende 43 fuentes consultadas con cautelas, 39 planos regionales, 1.496 pantallas bilingües, nueve biblias de narrador, presupuestos easy/standard/hard estimados y propuestas oficiales de autoría. i00002 declara la fuente inglesa por campaña conservando el fixture legado. i00003 cubre capacidades reutilizables faltantes; s00001 acredita el motor. No se afirma balance jugado, traducciones aprobadas ni mods completos por tener documentación.

## Encargo vigente de odiseas extensas

La última ampliación del usuario sustituye la extensión de 39 misiones por nueve odiseas: 30/29/30/32/32/30/28/32/30 episodios, 273 en total, cinco actos cada una. Consulta [plan completo](../design/odyssey-production-plan.md) y [selecciones](../design/odyssey-selections.md). La base de 39 contratos conserva identidad y evidencia; no se fuerza su cierre antiguo a mitad de la nueva cronología.

Treinta dossiers ampliados de faith-origins están redactados (1.191 pantallas y 180 secundarios; órdenes 1–30); aún requieren aprobación histórica, terreno y navegación, capacidades nativas y calibración. La apertura imperial añade veintinueve dossiers (órdenes 1–29), con combate local acotado, despacho de ida/regreso, hospitalidad, retirada y cadenas de contexto jurídico. En total hay 59 borradores, 2.427 pantallas y 363 secundarios. Los demás 214 episodios tienen selección, no expediente completo. d00002 y las nueve propuestas de autoría histórica siguen pendientes; ninguna tabla concede a MiniMax permiso para inventar historia, objetivos o mapas. El piloto técnico conserva su alcance acotado y sus propios gates.


Las [nueve biblias de narrador ampliadas](../design/voices/odyssey-narrators.json) fijan biografía ficticia, tono, itinerario, evolución en cinco actos y acceso al conocimiento para cada episodio. La revisión editorial sigue pendiente. El plan de voz no sustituye los dossiers, las fuentes ni la colocación local de las escenas.
