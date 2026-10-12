# Localización

Steam confirma 17 idiomas de interfaz/subtítulos en la consulta fechada. config/languages.json mantiene locales separados y carpetas candidatas del motor; folderVerified=false hasta inspección y prueba de una instalación objetivo. Los candidatos no se presentan como códigos definitivamente acreditados.

La configuración exige exactamente los 17 locales de la colección, sin locales ni carpetas repetidos; no puede reducirse para superar release. La fuente es es-ES; mantener es-LATAM, chino simplificado y tradicional separados. Cada catálogo tiene estado draft/translated/reviewed/approved y revisor. No declarar aprobada una traducción automática por existir. Inglés no es un fallback garantizado del motor: generar el destino completo y probarlo.

Todos los textos pasan por claves: título, descripción, objetivos, diálogos, decisiones, intro/outro, victoria/derrota, subtítulos y avisos. validateCatalogs exige igualdad de placeholders y marcadores, claves canónicas, control UTF-8 y límite editorial 4000 (no límite oficial del motor). La interpolación se resuelve antes de exportar.

El lock se actualiza mediante ids:allocate, conserva IDs y evita colisiones internas. Comprobar el rango contra cadenas del juego y mods coinstalados antes de producción. No cambiar IDs publicados ni aprovechar un rango ilustrativo como si fuese reservado.

Glosario por término/locale, forma preferida y variantes prohibidas. QA visual: el mismo evento en todos los locales, alfabetos no latinos, saltos y anchura, idioma cambiado a mitad de campaña, 2/5/10 mods activos y prioridades invertidas. Registrar versiones de todos los paquetes que compartan el archivo de cadenas.

## Paneles y nombres del escenario

scenario.messages contiene claves semánticas instructions, hints, victory, loss, history y scouts, obligatorias en contenido que no sea fixture. Se exportan a message_manager.<campo>_string_table_id y se vacía el fallback ASCII para no incrustar español como traducción universal. El fixture prueba persistencia; abrir automáticamente esos paneles y su apariencia requieren prueba del motor.

Unidades y facciones admiten nameKey opcional: el compilador genera efectos de cambio de nombre con string_id. Usarlo para héroes/personajes y delegaciones que deban presentarse con nombre propio. No traducir el identificador técnico. Cuando balance.<perfil>.hints es true y hay clave de panel hints, el setup muestra una pista traducida durante 10s; el panel sigue teniendo texto localizado. No sustituir así un diálogo narrado.
