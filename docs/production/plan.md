# Plan maestro de producción

La fábrica ya está integrada; la prioridad vigente es cerrar la arquitectura y las herramientas pendientes y avanzar después campaña a campaña, empezando por entregas privadas progresivas de **Embers of the Covenant**. El corte operativo, las dependencias y los límites están en [CURRENT-STATE](../handoffs/CURRENT-STATE.md) (5 de noviembre de 2026). Los cortes fechados posteriores conservan el historial que les correspondía.

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

El corte actual contiene 65 dossiers en borrador, 213 selecciones sin dossier, 2.689 pantallas, 405 objetivos secundarios y 216 objetivos principales sobre 278 selecciones. Incluye un dossier Yavneh añadido al catálogo de odiseas; los cortes fechados anteriores mantienen sus cifras históricas. La revisión histórica/editorial, geografía antigua, terreno, composición nativa y calibración siguen siendo gates separados. Ningún dossier autoriza a inventar hechos, objetivos o mapas ni acredita una partida.


Las [nueve biblias de narrador ampliadas](../design/voices/odyssey-narrators.json) fijan biografía ficticia, tono, itinerario, evolución en cinco actos y acceso al conocimiento para cada episodio. La revisión editorial sigue pendiente. El plan de voz no sustituye los dossiers, las fuentes ni la colocación local de las escenas.


El dossier de Sirmio (ID 33, orden 31) y su revisión técnica se integraron oficialmente mediante DelendAI en 559fbc22. El [análisis condicional de preparación](../qa/campaign-design/imperial33-readiness-timing-analysis.md) documenta sensibilidad del plazo difícil a recorridos y velocidades todavía hipotéticos; no acredita un mapa jugable ni nivelación. La [hoja del episodio de Constantinopla](../design/episode-plans/imperial-church/34-church-transfer-constantinople.architect-brief.md) acompaña el dossier ID 34, orden 33. El dossier y sus materiales de perfil/UI son borradores; el plan de mundo no se presenta como mapa jugado ni concede aprobación histórica o nativa. El [corte actual](../handoffs/CURRENT-STATE.md) conserva los contadores vigentes y sus límites.


## Estado sincronizado de arquitectura y piloto — 25 de octubre de 2026

d00002/S1 está `done` con aprobación formal GPT-6.1 integrada en `b9cff83e76b3eaee75cef789b5ace09a1c6b417b` (producto `924ebde2`). Sus dos criterios se cumplieron; el arquitecto corrigió las dos familias P2 numéricas y GPT-6.1 verificó la corrección. La evidencia consta en [aceptación](../research/odyssey-research/common-architecture-acceptance.md) y [revisión independiente](../research/odyssey-research/common-architecture-independent-review.md). En el estado recuperado, d00002/S2–S11 siguen `pending`. El catálogo suma 64 dossiers, 214 selecciones sin dossier, 2.645 pantallas y 398 secundarios; no hay aprobación histórica ampliada. f00001/S3 está `done` con producto `3d955598` y veredicto independiente `9c1486af` integrado en `dc23f194`; f00001/S4 de motor sigue pendiente. i00008/S1–S3 están `done`, incluido el despacho opt-in del auditor cívico en S3. Estos estados no aprueban dossiers ni demuestran comportamiento en AoE2.

El [reparto de trabajo](../handoffs/LLM-WORK-ALLOCATION.md) y la [cola de paquetes](../handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md) documentan la coordinación. La cuota agotada de MiniMax y el rechazo HTTP429/2056 del 24 de octubre son antecedentes; el propietario autorizó explícitamente a Luna para la materialización mecánica, sin compras de créditos ni generación pagada de medios. El piloto técnico no desbloquea propuestas históricas.

El [plan de mundo de Constantinopla](../design/episode-plans/imperial-church/34-constantinople-world-plan.md) aporta 45 pantallas fuente; el [suplemento de UI](../design/episode-plans/imperial-church/34-profile-ui-supplement.json) aporta seis más, para 51 en el dossier ID 34, orden 33, junto con siete secundarios. El dossier cuenta ahora dentro de los totales 64/2.645/398. El manifiesto contiene 49 recursos locales: ocho referencias modernas del Hiyaz y dos del DSM moderno de Jerusalén; no certifican paisaje antiguo, jugabilidad ni uso de producción. La nota de cobertura conserva 22 identidades geográficas pendientes para 25 selecciones. `geography.json` contiene 26 perfiles. La auditoría mecánica cívica actual incluye 64 filas y 54 candidatos estáticos; en una métrica distinta, 63 filas muestran presupuestos accesibles idénticos. Estos conteos no prueban defecto ni balance jugado. i00008/S1–S3 están `done` (S1 matriz de 34 casos prospectivos; no todos ejecutados). S3 habilita el despacho cívico v3 opt-in, no el mapper nativo ni una herramienta v3 de tiempos; `readiness_timing_audit` sigue limitado a su plan authored legacy.


## Corte operativo — 26 de octubre de 2026

El propietario solicita pruebas privadas en paralelo al diseño, con Windows/Steam y español. f00001/S1–S4 están done; S4 producto 9eac67e5 y veredicto 9047d995 entregan hashes, comandos, escenarios diagnósticos originales y ficha de observación, manteniendo GAME VERIFIED/PRODUCTION READY falsos. El [paso a paso](../handoffs/PRIVATE-PILOTS-WINDOWS-STEAM-ES.md) conserva la build por registrar y los casos sin lector/recap/harness bloqueados. s00001 y las capacidades nativas siguen pendientes; no confundir aceptación del dossier de pruebas con ejecución del motor.

i00009/S2 está integrado y aprobado3/3 (producto 0cf4d064, veredicto 9f4be255), con112 pruebas de diseño y157 Bun/2136 aserciones; mantiene64/2645/398/49 y todos los artefactos anteriores. i00010/S1 tiene aprobación independiente en f4a2599; S2 queda como paquete mecánico, con puente artificial TypeScript explícito en Files para probar el reducer real sin ampliar esquemas. MiniMax volvió a ejecutar una consulta preparatoria de sólo lectura tras el restablecimiento de cuota; eso no es aún una muestra de implementación.

La primera [comparación de progreso](../qa/campaign-design/interaction-progress-checkpoints.md)63→64 corresponde al intervalo reconstruido anterior, no a una media. La aclaración de plataforma recibida durante el trabajo es steering; no crea por sí sola otro intervalo completo comparable. El trabajo de Jerusalén/Kent sigue siendo diseño parcial y no aumenta el catálogo de64 dossiers.


La aclaración posterior del propietario mantiene los mods independientes de la tienda: Steam identifica su primer entorno de prueba, no una dependencia de distribución. El código de compilación/exportación no contiene llamadas o rutas Steam; el único enlace de Steam en config corresponde a la consulta de idiomas. Los formatos son AoE2:DE y la compatibilidad de cada instalación/build requiere pruebas propias; no se acredita consola, otra edición o Return of Rome por esa independencia. El [siguiente diagnóstico grande](../handoffs/LARGE-MAP-DIAGNOSTIC-PACKET.md) es un paquete parcial no asignado de i00003/S2, sin geografía histórica ni cierre de transporte/motor.


## Reanudación contrastada con la sesión separada de MiniMax

El servidor confirma i00008/i00009/i00010 cerradas. i00009/S3 está aprobado por MiniMax contra producto 34f87ce y publicado en 7cbac2b; root no repite ni se atribuye ese veredicto. El trabajo integrado de mapas a7f8dcd y Jerusalén 4a0bdab es parcial: no cierra i00003/S2 ni d00002/S4. El diagnóstico de 400 × 400 ya se ha exportado mediante el adaptador real y su binario se ha inspeccionado, con 158 pruebas / 2138 aserciones pasando y export 3 variantes / 2 round-trips. Carga/orientación/movimiento y performance siguen sin verificarse en AoE2. El [packet de presencia](../handoffs/MINIMAX-M3.1-PRESENCE.md) deja preparada la futura promoción de Milán 350, todavía bloqueada por la infraestructura nativa.


La ejecución de 400 × 400 posterior incorpora inspección nativa reproducible y recibos enlazados por SHA, con regresiones de fallo de exportación/ZIP. La revisión técnica acotada de MiniMax confirmó las correcciones; no constituye aprobación de todo i00003/S2. Los artefactos privados r2 conservan escenarios originales, catálogos, comandos, logs y revisión, con juego verificado falso.


Recopilación visual: el preview del levantamiento de Jerusalén 1864–1865 conserva fuente, hash, derechos atribuidos y limitación cronológica explícita; el manifiesto registra 50 recursos. No se convierten calles o edificios del siglo XIX en huellas del año 70. Los contadores actuales están en [CURRENT-STATE](../handoffs/CURRENT-STATE.md).

## Prioridad del propietario: primera campaña jugable en paralelo

El 26 de octubre el propietario aclara que el objetivo es avanzar una primera campaña real mientras el arquitecto completa diseño y coordina MiniMax/Luna. El embarque del diagnóstico es una observación auxiliar, no una secuencia de pruebas triviales que deba bloquear ese trabajo. El [plan de entrega progresiva](../handoffs/FIRST-CAMPAIGN-VERTICAL-DELIVERY.md) comienza por faith-origins/01-administrative-records-caesarea. Se conserva el alcance de campaña independiente y la revisión por episodio; no se espera a cerrar los 214 dossiers para producir una primera iteración privada, ni se presenta esa iteración como la campaña completa.


## Primera misión histórica privada — 27 de octubre de 2026

El cambio de prioridad del propietario ya tiene un producto concreto: [Cesarea, apertura de la primera campaña](../handoffs/PRIVATE-CAESAREA-OPENING.md), con tres objetivos principales, seis secundarios y seis variantes EN/es-ES × easy/standard/hard. El código `c55c3bd` se integró en `e443aaaa`; la revisión independiente acotada está integrada en `6e1245e4`. El [recibo](../qa/campaign-design/caesarea-private-opening-build.json) conserva hashes del escenario, contenedor, ZIP por variante y kit privado. Pasan 35 pruebas nativas enfocadas y 158 pruebas Bun, más lectura/escritura y XS de las seis variantes. Ninguna de esas evidencias es una partida en AoE2.

El prototipo no habilita el exportador público v2/v3 ni cierra los slices amplios. Quedan la prueba real de la misión, guardado/carga, rutas, interfaz y calibración; es una apertura civil sin combate ni plazo secreto. La dirección vigente y los contadores están en [CURRENT-STATE](../handoffs/CURRENT-STATE.md); seis variantes siguen siendo un solo episodio, no una campaña completa.
