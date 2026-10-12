# Identificadores y naming

Campaña: `imperial-church`; ID público: `CDF-C01`; nombre del motor: `CDF_ImperialChurch`. El ID del portal de mods será otro dato y no se inventa antes de publicar. Escenario/carpeta: `01-milvian-bridge`. Personas/facciones/fuentes: ASCII kebab-case, semántico y estable. La documentación puede llevar tildes en su contenido; las rutas usan ASCII y sin espacios.

Texto: `campaign.imperial-church.title`, `scenario.milvian-bridge.intro`, `character.constantine.name`. Progreso: `progress.imperial-church.western-perspective`. Usar una clave por ruta acumulativa; no una variable única que sustituya victorias anteriores. Nadie escribe IDs numéricos en los guiones.

No renombrar campañas publicadas ni namespaces de progreso. Un cambio de esquema requiere migración, fixture previo, comparación de IDs y ADR. Las claves retiradas permanecen reservadas en config/string-ids.lock.json. Los IDs de unidades/civilizaciones del motor se obtienen del catálogo fijado del parser; no son identificadores religiosos ni prueban exactitud histórica.
