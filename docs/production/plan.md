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

La última ampliación del usuario sustituye la extensión de 39 misiones por nueve odiseas: 30/34/30/32/32/30/28/32/30 episodios, 278 en total, cinco actos cada una. Consulta [plan completo](../design/odyssey-production-plan.md) y [selecciones](../design/odyssey-selections.md). La base de 39 contratos conserva identidad y evidencia; no se fuerza su cierre antiguo a mitad de la nueva cronología.

Treinta dossiers ampliados de faith-origins están redactados (1.191 pantallas y 180 secundarios; órdenes 1–30); aún requieren aprobación histórica, terreno y navegación, capacidades nativas y calibración. La apertura imperial añade treinta y tres dossiers de treinta y cuatro seleccionados (órdenes 1–32 y 34), con combate local acotado, despacho de ida/regreso, hospitalidad, retirada y cadenas de contexto jurídico. En total hay 63 borradores, 2.594 pantallas y 391 secundarios; quedan 215 selecciones sin dossier. d00002/S1 está formalmente `done`; S2–S11 siguen `pending` según la consulta viva. Las nueve propuestas de autoría histórica siguen bloqueadas; ninguna tabla concede permiso para inventar historia, objetivos o mapas. El piloto técnico conserva su alcance y gates propios.


Las [nueve biblias de narrador ampliadas](../design/voices/odyssey-narrators.json) fijan biografía ficticia, tono, itinerario, evolución en cinco actos y acceso al conocimiento para cada episodio. La revisión editorial sigue pendiente. El plan de voz no sustituye los dossiers, las fuentes ni la colocación local de las escenas.


El dossier de Sirmio (ID 33, orden 31) y su revisión técnica se integraron oficialmente mediante DelendAI en 559fbc22. El [análisis condicional de preparación](../qa/campaign-design/imperial33-readiness-timing-analysis.md) documenta sensibilidad del plazo difícil a recorridos y velocidades todavía hipotéticos; no acredita un mapa jugable ni nivelación. La [hoja del episodio de Constantinopla](../design/episode-plans/imperial-church/34-church-transfer-constantinople.architect-brief.md) conserva el orden 33 sin dossier completo hasta resolver un problema jugable propio. Hay 63 borradores completos de diseño y 215 selecciones sin dossier, ninguna aprobación ampliada de juego.


## Estado sincronizado de arquitectura y piloto — 25 de octubre de 2026

d00002/S1 está `done` con aprobación formal GPT-6.1 integrada en `b9cff83e76b3eaee75cef789b5ace09a1c6b417b` (producto `924ebde2`). Sus dos criterios se cumplieron; se corrigieron las dos familias P2 numéricas y GPT-6.1 verificó la corrección. La evidencia consta en [aceptación](../research/odyssey-research/common-architecture-acceptance.md) y [revisión independiente](../research/odyssey-research/common-architecture-independent-review.md). S2–S11 siguen `pending` según DelendAI; se mantienen 63 dossiers, 215 selecciones sin dossier, 2.594 pantallas y 391 secundarios, sin aprobación ampliada. f00001/S2 se implementó por Luna, fue revisado y se integró en `9d5e744b`; la consulta viva aún muestra S2 `review`, no `done`. S3 sólo se considera después del veredicto formal integrado. El usuario autorizó a Luna para el trabajo mecánico del piloto mientras MiniMax carece de cuota; no hubo cambio automático de proveedor ni gasto.

El [reparto de trabajo](../handoffs/LLM-WORK-ALLOCATION.md) y la [cola de paquetes](../handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md) documentan la coordinación. La planificación admite entregas por tarea/slice según su aceptación oficial; no hace falta esperar al cierre de las nueve odiseas para evaluar un piloto acotado, pero el piloto no desbloquea propuestas históricas. La cuota de MiniMax agotada y el rechazo HTTP429/2056 del 24 de octubre son antecedentes, no el estado del trabajo mecánico: el usuario autorizó a Luna para f00001/S2. No se afirma cambio de proveedor ni compra de créditos.

El [plan parcial de mundo de Constantinopla](../design/episode-plans/imperial-church/34-constantinople-world-plan.md) agrega 45 pantallas EN/es-ES y siete secundarios auxiliares, fuera del dossier 64 y de los totales 63/2.594/391. El manifiesto tiene 47 recursos locales, cuatro de ellos datos de elevación modernos del Hijaz; faltan 22 identidades geográficas que afectan a 25 selecciones. `geography.json` contiene 26 perfiles y la auditoría cívica señala 54 candidatos estáticos de riesgo entre 63 dossiers; ninguno de esos recuentos acredita mapa jugable o balance. i00008/S1 tiene una decisión arquitectónica propuesta con 34 casos en 3 slices, pero DelendAI aún muestra S1 `review`; el mapper no está implementado y S2/S3 siguen `pending`.
