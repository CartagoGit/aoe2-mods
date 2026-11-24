# Crónicas de la Fe

Fábrica de campañas históricas independientes para Age of Empires II: Definitive Edition. El jugador puede descargar cualquier campaña y recibir recomendaciones de continuidad; ninguna predecesora es una dependencia obligatoria.

El contenido nuevo se concibe primero en inglés (`sourceLocale=en`) y tiene versión completa en español de España. El fixture legado declara `es-ES` y conserva IDs. Los autores escriben claves semánticas y especificaciones JSON; TypeScript valida y produce una representación intermedia, y Python adapta el subconjunto compatible a archivos reales de AoE2. La infraestructura no depende de una religión concreta.

## Empezar

Instala Bun 1.4.2, Python 3.10 o posterior y un compilador C (GCC/Clang; MinGW en Windows), o proporciona `RGE_CAMPAIGN_BIN` con una compilación de la revisión fijada. No hace falta Docker.

```sh
bun install --frozen-lockfile
python tools/python/setup.py
bun run validate
bun run test:export
bun run campaigns:list
bun run campaign:build technical-pilot --export
```

En Linux/macOS puede ser necesario usar `python3`. El adaptador usa `.venv` automáticamente; `COF_PYTHON` permite seleccionar otro intérprete. Las llamadas externas usan argumentos sin shell. No se toca la instalación, el perfil ni el ejecutable del juego.

## Estado y alcance

El corte operativo es [CURRENT-STATE](docs/handoffs/CURRENT-STATE.md), fechado 5 de noviembre de 2026; prevalece sobre cifras y estados de los cortes históricos que siguen abajo. Recupera el estado vivo de DelendAI antes de reclamar o revisar trabajo.

Existe un fixture técnico de dos objetivos y dos traducciones de muestra. No hay campañas históricas completas ni 17 traducciones aprobadas. La exportación binaria pasa el round-trip de escenario y contenedor; la carga en AoE2 aún necesita evidencia. No se declara PRODUCTION READY.

El build intermedio es determinista. Los binarios del parser pueden incluir metadatos temporales: se registran sus hashes por ejecución, sin prometer identidad binaria entre ejecuciones. El ZIP ordena archivos y fija fechas.

Lee [plan](docs/production/plan.md), [arquitectura](docs/architecture/overview.md), [comandos](docs/guides/development.md), [preparación de contenido](docs/guides/staging.md), [capacidades](docs/research/aoe2-capabilities.md), [auditoría](docs/qa/audit.md) y [traspaso](docs/handoffs/MINIMAX-M3.1-START.md). Los archivos de `build/`, `dist/`, `.venv/` y `.cache/` son regenerables y no se editan.

## Primera misión histórica privada

Ya se ha generado la apertura de **Embers of the Covenant**, Cesarea: tres objetivos principales y seis secundarios, con seis variantes EN/es-ES × easy/standard/hard. La [guía de instalación y juego](docs/handoffs/PRIVATE-CAESAREA-OPENING.md) y el [recibo de compilación](docs/qa/campaign-design/caesarea-private-opening-build.json) identifican los archivos privados y sus hashes. El código está integrado en `e443aaaa` y la revisión técnica acotada en `6e1245e4`. Pasan 35 pruebas nativas enfocadas y 158 pruebas Bun; las seis variantes pasan escritura/lectura nativa, XS y extracción del contenedor.

Es una apertura privada de un episodio, con ejecución y gameplay en AoE2 aún pendientes. No constituye una campaña histórica completa ni habilita la exportación pública general de perfiles v2/v3. El siguiente episodio previsto de **Embers of the Covenant** es Jerusalén, cuyo build histórico continúa bloqueado por decisiones de geografía y terreno; [CURRENT-STATE](docs/handoffs/CURRENT-STATE.md) resume la secuencia vigente.

## Catálogo preparado por el arquitecto

El alcance vigente son [nueve odiseas y 278 episodios seleccionados](docs/design/odyssey-selections.md). En el corte actual hay 65 dossiers de diseño en borrador, 213 selecciones sin dossier, 2.689 pantallas bilingües, 405 objetivos secundarios y 216 objetivos principales. Yavneh es el dossier 65, un borrador sin aprobación histórica, terreno antiguo, build nativo ni prueba de juego. Las aprobaciones ampliadas y los episodios históricos plenamente verificados en el motor siguen en cero. Los estados de infraestructura y la dirección de producción están en [CURRENT-STATE](docs/handoffs/CURRENT-STATE.md).

El catálogo anterior de 39 contratos conserva sus propios contadores históricos. El catálogo ampliado tiene 26 perfiles geográficos base y 19 suplementales, 45 identidades únicas; su nota de cobertura actual conserva 40 identidades ausentes que afectan a 58 selecciones. El manifiesto registra 50 recursos. Las referencias modernas de Jerusalén no certifican terreno antiguo. Consulta el [reparto de trabajo](docs/handoffs/LLM-WORK-ALLOCATION.md), la [cola de paquetes](docs/handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md) y [CURRENT-STATE](docs/handoffs/CURRENT-STATE.md) para el estado vigente.

```sh
python3 tools/design/render.py
python3 tools/design/verify.py
python3 tools/design/test_design.py
```

La [primera prueba para Windows/Steam en español](docs/handoffs/PRIVATE-PILOTS-WINDOWS-STEAM-ES.md) permite probar los dos fixtures y sus escenarios originales de diagnóstico mientras continúa el diseño. El [registro de avance por interacción](docs/qa/campaign-design/interaction-progress-checkpoints.md) conserva cortes verificables. i00009/S2 de recompensas authored/zero está integrado y revisado (producto `0cf4d064`, veredicto `9f4be255`); i00010/S1–S2 están aprobados (producto `d86c5613`, veredicto `afa036fc`). Ninguno añade exportación de perfiles compuestos ni acredita un escenario histórico jugado.


Corte recuperado tras la ejecución separada de MiniMax: i00008/i00009/i00010 están cerradas en DelendAI; i00009/S3 tiene revisión independiente MiniMax integrada en `7cbac2b`. El diagnóstico artificial 300/400 está integrado parcialmente en `a7f8dcd` y el diseño parcial de Jerusalén en `4a0bdab`; no completan sus slices. La primera exportación real de 400 × 400 y sus recibos se han ejecutado en la unidad propia del arquitecto, manteniendo `gameVerified=false`. El [paquete de presencia](docs/handoffs/MINIMAX-M3.1-PRESENCE.md) prepara una futura asignación, bloqueada todavía por i00003/S3 e i00005/S2.


La [referencia visual de Jerusalén de 1865](docs/research/odyssey-research/jerusalem-wilson-1865-reference-collection.json) conserva sus bytes/hash y aviso de derechos en el manifiesto de 50 recursos. Es una referencia moderna, no geografía del año 70. El corte actual de dossiers y cobertura está en [CURRENT-STATE](docs/handoffs/CURRENT-STATE.md); los conteos 49 de cortes anteriores conservan su significado histórico.
