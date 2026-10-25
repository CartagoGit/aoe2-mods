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

BASE READY: infraestructura integrada mediante DelendAI, gate certificado y revisiones independientes. i00001 está cerrada; d00002/S1 está `done`. f00001/S2 está `done` tras el producto `9d5e744b` y el veredicto formal `137fdd73` (aceptación 3/3). i00008/S1 está `done`; S2 está `done` tras el producto `6f06737` y el veredicto formal `e08a5cb`. i00008/S3 se está implementando: añade compatibilidad cívica opt-in al auditor y sincroniza el traspaso; aún requiere revisión independiente e integración oficial. Ninguno de estos estados aprueba contenido histórico ni evidencia de juego. Recupera el estado vivo antes de actuar.

Existe un fixture técnico de dos objetivos y dos traducciones de muestra. No hay campañas históricas completas ni 17 traducciones aprobadas. La exportación binaria pasa el round-trip de escenario y contenedor; la carga en AoE2 aún necesita evidencia. No se declara PRODUCTION READY.

El build intermedio es determinista. Los binarios del parser pueden incluir metadatos temporales: se registran sus hashes por ejecución, sin prometer identidad binaria entre ejecuciones. El ZIP ordena archivos y fija fechas.

Lee [plan](docs/production/plan.md), [arquitectura](docs/architecture/overview.md), [comandos](docs/guides/development.md), [preparación de contenido](docs/guides/staging.md), [capacidades](docs/research/aoe2-capabilities.md), [auditoría](docs/qa/audit.md) y [traspaso](docs/handoffs/MINIMAX-M3.1-START.md). Los archivos de `build/`, `dist/`, `.venv/` y `.cache/` son regenerables y no se editan.

## Catálogo preparado por el arquitecto

El alcance vigente son [nueve odiseas y 278 episodios seleccionados](docs/design/odyssey-selections.md), organizados en cinco actos por campaña. La [planificación](docs/design/odyssey-production-plan.md) y d00002 siguen en curso: 63 dossiers, 215 selecciones sin dossier, 2.594 pantallas bilingües y 391 objetivos secundarios; siguen pendientes la revisión histórica, el terreno navegable, la calibración en AoE2 y la aprobación ampliada. No se autoriza autoría histórica por completar el piloto técnico. i00008/S3 mantiene el auditor cívico opt-in y sus handoffs en revisión; no altera el informe legacy de 63 dossiers ni habilita autoría histórica o exportación nativa.

El [catálogo anterior](docs/design/README.md) conserva 39 contratos históricos, 1.496 pantallas EN/es-ES, 234 secundarios, nueve biblias de narrador y 26 perfiles geográficos. El manifiesto contiene 47 recursos locales, incluidos ocho recursos modernos del Hijaz (cuatro recortes DSM y cuatro vistas); faltan 22 identidades geográficas que afectan a 25 selecciones. La investigación mantiene créditos, licencias y hashes. Las [asignaciones](docs/handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md) distinguen esa base de las odiseas pendientes. El [reparto de trabajo](docs/handoffs/LLM-WORK-ALLOCATION.md) y la [cola de paquetes](docs/handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md) describen las entregas paralelas: fuentes en staging de episodios aprobados, con gates nativos y pruebas del motor antes de exportación/promoción.

```sh
python3 tools/design/render.py
python3 tools/design/verify.py
python3 tools/design/test_design.py
```
