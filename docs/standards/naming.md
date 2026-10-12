# Identificadores y naming

Campaña: `imperial-church`; ID público: `CDF-C01`; nombre del motor: `CDF_ImperialChurch`. El ID del portal de mods será otro dato y no se inventa antes de publicar. Escenario/carpeta: `01-milvian-bridge`. Personas/facciones/fuentes: ASCII kebab-case, semántico y estable. La documentación puede llevar tildes en su contenido; las rutas usan ASCII y sin espacios.

Texto: `campaign.imperial-church.title`, `scenario.milvian-bridge.intro`, `character.constantine.name`. Progreso: `progress.imperial-church.western-perspective`. Usar una clave por ruta acumulativa; no una variable única que sustituya victorias anteriores. Nadie escribe IDs numéricos en los guiones.

No renombrar campañas publicadas ni namespaces de progreso. Un cambio de esquema requiere migración, fixture previo, comparación de IDs y ADR. Las claves retiradas permanecen reservadas en config/string-ids.lock.json. Los IDs de unidades/civilizaciones del motor se obtienen del catálogo fijado del parser; no son identificadores religiosos ni prueban exactitud histórica.

## Archivos TypeScript de producción

Los módulos de producción usan `<responsabilidad>.<tipo>.ts`: ambos segmentos describen el propósito real del archivo y usan ASCII kebab-case. Ejemplos: `campaign.schema.ts`, `filesystem.helper.ts`, `gameplay.validator.ts`, `scenario.compiler.ts`, `native-campaign.renderer.ts`, `audio-build.pipeline.ts` y `chronicles.script.ts`. Se conservan los directorios de dominio existentes. No se usan `index.ts`, barrels ni imports que dependan de resolución implícita de directorio; cada import apunta al archivo concreto.

Los archivos de prueba conservan la convención existente `*.test.ts` (o `*.spec.ts` donde ya se use), con nombre de responsabilidad descriptivo. Una prueba puede importar el módulo de producción por su ruta explícita.
