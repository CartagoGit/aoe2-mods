# Crónicas de la Fe

Fábrica de campañas históricas independientes para Age of Empires II: Definitive Edition. El jugador puede descargar cualquier campaña y recibir recomendaciones de continuidad; ninguna predecesora es una dependencia obligatoria.

El contenido canónico es español de España. Los autores escriben claves semánticas y especificaciones JSON; TypeScript valida y produce una representación intermedia, y Python adapta el subconjunto compatible a archivos reales de AoE2. La infraestructura no depende de una religión concreta.

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

Existe un fixture técnico de dos objetivos y dos traducciones de muestra. No hay campañas históricas completas ni 17 traducciones aprobadas. La exportación binaria pasa el round-trip de escenario y contenedor; la carga en AoE2 aún necesita evidencia. No se declara PRODUCTION READY.

El build intermedio es determinista. Los binarios del parser pueden incluir metadatos temporales: se registran sus hashes por ejecución, sin prometer identidad binaria entre ejecuciones. El ZIP ordena archivos y fija fechas.

Lee [plan](docs/production/plan.md), [arquitectura](docs/architecture/overview.md), [comandos](docs/guides/development.md), [preparación de contenido](docs/guides/staging.md), [capacidades](docs/research/aoe2-capabilities.md), [auditoría](docs/qa/audit.md) y [traspaso](docs/handoffs/MINIMAX-M3.1-START.md). Los archivos de `build/`, `dist/`, `.venv/` y `.cache/` son regenerables y no se editan.
