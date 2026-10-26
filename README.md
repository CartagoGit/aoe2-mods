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

BASE READY: infraestructura integrada mediante DelendAI, gate certificado y revisiones independientes. i00001 está cerrada; d00002/S1 está `done`, mientras S2–S11 siguen pendientes según el estado recuperado para esta consolidación. f00001/S1–S4 están `done`: S4 entrega el kit privado revisado (producto `9eac67e5`, veredicto `9047d995`), mientras las pruebas reales del motor siguen pendientes en s00001. i00008/S1–S3 están `done`; S3 usa la rama opt-in del auditor cívico y no añade soporte nativo. Ninguno de estos estados aprueba contenido histórico ni evidencia de juego. Recupera el estado vivo antes de actuar.

Existe un fixture técnico de dos objetivos y dos traducciones de muestra. No hay campañas históricas completas ni 17 traducciones aprobadas. La exportación binaria pasa el round-trip de escenario y contenedor; la carga en AoE2 aún necesita evidencia. No se declara PRODUCTION READY.

El build intermedio es determinista. Los binarios del parser pueden incluir metadatos temporales: se registran sus hashes por ejecución, sin prometer identidad binaria entre ejecuciones. El ZIP ordena archivos y fija fechas.

Lee [plan](docs/production/plan.md), [arquitectura](docs/architecture/overview.md), [comandos](docs/guides/development.md), [preparación de contenido](docs/guides/staging.md), [capacidades](docs/research/aoe2-capabilities.md), [auditoría](docs/qa/audit.md) y [traspaso](docs/handoffs/MINIMAX-M3.1-START.md). Los archivos de `build/`, `dist/`, `.venv/` y `.cache/` son regenerables y no se editan.

## Catálogo preparado por el arquitecto

El alcance vigente son [nueve odiseas y 278 episodios seleccionados](docs/design/odyssey-selections.md), organizados en cinco actos por campaña. El catálogo tiene 64 dossiers de diseño en borrador (30 de faith-origins y 34 de imperial-church), 214 selecciones sin dossier, 2.645 pantallas bilingües y 398 objetivos secundarios. Constantinopla380 es el dossier ID 34, orden 33; su plan de mundo auxiliar y perfil no certifican mapa jugable, revisión histórica ni ejecución nativa. Siguen pendientes la revisión histórica/editorial, el terreno navegable, la calibración en AoE2 y toda aprobación ampliada. No se autoriza autoría histórica por completar los pilotos técnicos. i00008/S3 conserva la compatibilidad legacy por registro y permite el despacho v3 opt-in; el informe regenerado tiene 64 filas, 54 candidatos estáticos y 63 casos con presupuesto accesible idéntico entre dificultades. No habilita exportación nativa.

El [catálogo anterior](docs/design/README.md) conserva 39 contratos históricos, 1.496 pantallas EN/es-ES, 234 secundarios, nueve biblias de narrador y 26 perfiles geográficos. El manifiesto tiene 49 recursos locales, incluidos ocho recursos modernos del Hijaz y dos referencias DSM modernas de Jerusalén; ninguno acredita terreno antiguo ni aprobación de producción. La nota de cobertura conserva 22 identidades geográficas pendientes para 25 selecciones. La investigación mantiene créditos, licencias y hashes. Las [asignaciones](docs/handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md) distinguen esa base de los dossiers extendidos. El [reparto de trabajo](docs/handoffs/LLM-WORK-ALLOCATION.md) y la [cola de paquetes](docs/handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md) describen las entregas paralelas con sus gates nativos y pruebas de motor pendientes.

```sh
python3 tools/design/render.py
python3 tools/design/verify.py
python3 tools/design/test_design.py
```

La [primera prueba para Windows/Steam en español](docs/handoffs/PRIVATE-PILOTS-WINDOWS-STEAM-ES.md) permite probar los dos fixtures y sus escenarios originales de diagnóstico mientras continúa el diseño. El [registro de avance por interacción](docs/qa/campaign-design/interaction-progress-checkpoints.md) conserva cortes verificables. i00009/S2 de recompensas authored/zero está integrado y revisado (producto `0cf4d064`, veredicto `9f4be255`); i00010/S1–S2 están aprobados: producto pooled `d86c5613`, revisión independiente `afa036fc`. Ninguno añade exportación de perfiles compuestos ni acredita un escenario histórico jugado.
