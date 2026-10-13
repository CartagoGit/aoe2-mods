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

BASE READY: infraestructura integrada mediante DelendAI, gate certificado y revisión formal independiente por GPT-6.1. i00001 cerrada; f00001/S1 es la primera tarea lista para MiniMax M3.1. Ver auditoría y recuperar el estado vivo antes de trabajar.

Existe un fixture técnico de dos objetivos y dos traducciones de muestra. No hay campañas históricas completas ni 17 traducciones aprobadas. La exportación binaria pasa el round-trip de escenario y contenedor; la carga en AoE2 aún necesita evidencia. No se declara PRODUCTION READY.

El build intermedio es determinista. Los binarios del parser pueden incluir metadatos temporales: se registran sus hashes por ejecución, sin prometer identidad binaria entre ejecuciones. El ZIP ordena archivos y fija fechas.

Lee [plan](docs/production/plan.md), [arquitectura](docs/architecture/overview.md), [comandos](docs/guides/development.md), [preparación de contenido](docs/guides/staging.md), [capacidades](docs/research/aoe2-capabilities.md), [auditoría](docs/qa/audit.md) y [traspaso](docs/handoffs/MINIMAX-M3.1-START.md). Los archivos de `build/`, `dist/`, `.venv/` y `.cache/` son regenerables y no se editan.

## Catálogo preparado por el arquitecto

El alcance vigente son [nueve odiseas y 273 episodios seleccionados](docs/design/odyssey-selections.md), organizados en cinco actos por campaña. La [planificación](docs/design/odyssey-production-plan.md) y d00002 siguen en curso. Hay veinticinco dossiers ampliados (órdenes 1–25) de *Embers of the Covenant*, con 987 pantallas bilingües y 150 objetivos secundarios; requieren revisión histórica independiente, terreno navegable y calibración en AoE2. No son veinticinco escenarios jugables ni desbloquean la autoría histórica de MiniMax.

El [catálogo anterior](docs/design/README.md) conserva 39 contratos históricos, 1.496 pantallas EN/es-ES, 234 secundarios, nueve biblias de narrador y 26 entornos geográficos. La investigación incluye 14 referencias originales y [dieciséis nuevos recursos locales](docs/research/odyssey-research/reference-manifest.json), con créditos, licencias y hashes. Las [asignaciones](docs/handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md) distinguen esa base de las odiseas pendientes. Las capacidades y pruebas del motor mantienen sus gates antes de producir contenido.

```sh
python3 tools/design/render.py
python3 tools/design/verify.py
python3 tools/design/test_design.py
```
