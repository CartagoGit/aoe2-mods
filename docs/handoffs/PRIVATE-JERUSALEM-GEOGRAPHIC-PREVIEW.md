# Segunda entrega privada: Jerusalén

Embers of the Covenant / Las brasas de la alianza — **When the City Held Its Breath / Cuando la ciudad contuvo el aliento**, hacia 30–33 d. C. Esta versión de desarrollo permite comprobar el relieve regional y el funcionamiento de la misión. Es el episodio 02 de una campaña prevista de 30; el siguiente es **A Table in Jerusalem / Una mesa en Jerusalén**. El episodio 03 todavía no está incluido.

## Instalación y entrada directa al episodio

Para la primera prueba usa `variants/faith-origins-jerusalem-private-es-ES-standard-2026-11-07.zip`, la variante **es-ES / standard**. No necesitas Bun, Python ni herramientas de desarrollo en Windows. Instala una sola variante: la dificultad y los textos corresponden al archivo instalado, no se recompilan al cambiar el menú del juego.

1. Cierra AoE2:DE y descomprime el ZIP de la variante.
2. Localiza el perfil que usa el juego. La ruta habitual es `%USERPROFILE%\Games\Age of Empires 2 DE\<perfil>\mods\local\`; puedes reconocerla mediante «Abrir directorio» de un mod instalado.
3. Crea `COF-Private-Jerusalem` dentro de `mods\local` y copia ahí el contenido de la variante. `resources` debe estar directamente dentro de esa carpeta.
4. Abre el juego y activa el mod local si el gestor muestra una casilla; reinicia. En campañas personalizadas aparecerán un contenedor de Jerusalén y otro progresivo con Cesarea seguida de Jerusalén. Para probar el segundo episodio directamente elige Jerusalén. Las etiquetas del menú y su presentación requieren comprobación en tu build.
5. Si no aparece en campañas, copia `editor/es-ES/standard/faith-origins-02-private-geographic-preview.aoe2scenario` a `<perfil>\resources\_common\scenario\`. Abre **Editor → Cargar escenario** y después **Menú → Probar escenario**, según las etiquetas de tu versión. No sobrescribas el original al guardar desde el editor.

La instalación es local, sin publicación en el portal. Steam es nuestro primer entorno de prueba; los archivos son formatos de AoE2:DE sin dependencia de su tienda. La compatibilidad de otras instalaciones se comprueba por build.

## Los tres objetivos principales

Deja terminar la crónica objetiva y el relevo a Miriam. Miriam es un personaje ficticio que conoce este episodio mediante cartas y relatos heredados, no una testigo ocular. Las 39 pantallas y el orden de narradores se conservan. Esta versión usa subtítulos y no incluye voces grabadas.

1. Al noroeste empiezan ocho **Representantes del hogar**, numerados 1–8. Lleva al menos seis originales vivos al círculo **Patio receptor meridional**. Cada identidad cuenta una vez. Las visitas se acumulan: no es necesario apiñar seis personajes simultáneamente. Puedes incorporar al séptimo y al octavo después; el registro no queda congelado en los seis primeros.
2. Después del mensaje del primer objetivo, selecciona un representante original vivo que esté dentro de ese patio. Su selección autoriza el pago único y completo de **240 alimento**. No debe cobrar parcialmente ni repetir el cobro al seleccionar de nuevo o cargar una partida.
3. Lleva al menos seis hogares registrados en el patio al **Refugio del camino sur**. Deben ser esos originales y seis de las llegadas finales deben seguir vivos al resolverse la misión. Una identidad que nunca pasó por el patio no puede sustituirlos. El desenlace cierra los secundarios y recomienda el episodio 03.

Hay ocho hogares principales y se requieren seis; la pérdida irreversible de un tercero antes del desenlace provoca derrota. No existe sustitución automática. Los visitantes opcionales no cuentan como hogares principales. Esta versión civil carece de enemigos y plazo secreto; no hace falta repetir la prueba de embarque del diagnóstico anterior.

## Secundarios y rutas

Puedes resolverlos antes del desenlace, en cualquier orden. Perder un participante opcional debe fallar solo su tarea.

| Tarea | Acción | Efecto único |
|---|---|---|
| Vecinos sin registrar | Lleva los dos porteadores de ayuda al punto occidental y oriental del patio que indica cada nombre. | 100 alimento y 50 madera. |
| Nombres en dos fragmentos | Lleva los dos portadores de copia desde el sur a **Entrega occidental de copias**, junto al distrito inicial. | Nota histórica y pista del objetivo principal. No reconstruye un documento antiguo real. |
| Techo del almacén | Selecciona el **Almacén dañado**, al norte del patio. | Paga 50 madera, restaura su salud y recibe 200 alimento y 100 madera. No requiere ordenar una reparación ordinaria a un aldeano. |
| Comerciante de los olivos | Lleva al comerciante al **Puesto de remesas del patio** y selecciónalo después de llegar. | Paga 50 oro; recibe 150 alimento y 50 madera. |
| Guía de la cresta | Lleva al guía a su punto junto al refugio. | Revela o marca el desvío occidental previsto. No crea un puente ni acredita su navegación. |
| Dos hogares visitantes | Lleva ambos visitantes del sur a **Recepción occidental de visitantes**, en el noroeste. | 100 alimento y 25 oro. No sustituyen a los ocho hogares principales. |

Los dos corredores son candidatos dentro de coordenadas regionales reales. Puedes comparar la ruta principal y el desvío occidental; la geometría no certifica que el motor los recorra sin problemas. El relieve no se ha aplanado para ocultar fallos.

## Dificultad de esta versión

| Perfil | Alimento / madera / oro / piedra inicial |
|---|---|
| easy | 402 / 172 / 86 / 0 |
| standard | 350 / 150 / 75 / 0 |
| hard | 297 / 127 / 63 / 0 |

Todos permiten pagar los 240 de alimento y ambos costes opcionales sin depender de premios previos. En este builder cambia el stock inicial; no se ha implementado una ayuda de navegación distinta por perfil. Sus etiquetas no acreditan todavía un reto equilibrado. No hay recolección, producción, banco económico accesible ni recuperación de originales en esta iteración. Las reservas y los tiempos estimados del dossier no se presentan como capacidades nativas. La utilidad de las recompensas debe evaluarse en las siguientes iteraciones.

## Qué observar al jugar

El kit incluye una ficha pendiente de observaciones; no contiene partidas ficticias. Basta empezar jugando la misión completa: no necesitas completar toda la tabla para que continúe el desarrollo. Registra la build visible del juego, variante y hash del escenario antes de la prueba.

| Caso | Resultado esperado o dato que registrar |
|---|---|
| Carga y presentación | Distinguir error de menú de error del escenario; introducción objetiva seguida de Miriam, aviso de desarrollo legible. |
| Rutas y relieve | Recorrer ambos candidatos con un hogar; registrar atascos y coordenadas, orientación, cambios de elevación y acceso a cada círculo. |
| Almacén y marcadores | Seleccionar y rodear el almacén; comprobar que no bloquea el acceso al patio, solapa personajes ni aparece en un desnivel roto. |
| Registro principal | Visitas en momentos distintos, seis identidades diferentes, incorporación posterior del séptimo/octavo; repetir entradas no añade hogares. |
| Pago | Selección fuera del patio no paga; dentro y después del objetivo 1 cobra 240 una vez. Guardar/cargar antes y después no duplica ni pierde el recibo. |
| Refugio y desenlace | Solo cuentan originales registrados, seis llegadas vivas; victoria y recomendación del 03 una vez. Opcionales cerrados después del terminal. |
| Secundarios | Comprobar costes y premios de la tabla, repetición de selección, guía y nota; guardar/cargar entre llegada y selección. |
| Dificultad | Registrar duración, dudas, utilidad de decisiones y premios; comparar archivos de perfiles distintos en partidas nuevas. No cargar un guardado de otra variante. |
| Continuidad privada | Contenedor progresivo: Cesarea y después Jerusalén. El contenedor directo evita repetir Cesarea; comprobar el acceso real en tu build. |

## Historia, geografía y procedencia

El contexto literario es el testimonio retrospectivo de Tácito sobre la ejecución de Christus por Poncio Pilato bajo Tiberio. La datación hacia 30–33 es una reconstrucción; el pasaje no documenta estos hogares ni una operación de refugio. Los personajes y distritos de actividad son ficción explícita.

Las civilizaciones y los modelos del motor son aproximaciones técnicas; no acreditan vestuario romano ni una atribución étnica o religiosa de los participantes. La cubierta del suelo es provisional.

El mapa tiene **340 × 340** celdas y usa un recorte georreferenciado moderno de Copernicus GLO-30 como referencia de relieve regional. Incluye superficies modernas y vegetación: no es terreno desnudo del siglo I. La ausencia de una capa de agua conocida no demuestra suelo seco. No se incorporan calles de época posterior ni figuras arqueológicas sin permiso.

El almacén es el único original desplazado en el binding privado: tres celdas al norte dentro de su mismo distrito ficticio. Se conserva su posición de origen; los otros 16 originales y las 10 zonas mantienen su fuente. El binding histórico permanece sin aprobación. Ninguna compilación o extracción de contenedor es una partida en AoE2.

El ZIP original de Cesarea se conserva íntegro: SHA256 `0d589ef21deedb8e8947c7c768d1dc0a5725b44de0c0d80846be28584b193c8a`. El contenedor progresivo reutiliza sus escenarios exactos, sin reconstruirlos con fuentes posteriores. `MANIFEST.json` del nuevo kit y el recibo del proyecto identifican los hashes reales de esta entrega. Los avisos de fuente, modificación y licencia de Copernicus acompañan los archivos derivados; no implican respaldo de Copernicus, la Unión Europea, ESA, DLR o Airbus.
