# Primera misión privada: Cesarea

Entrega del 27 de octubre de 2026. Campaña **Embers of the Covenant / Las brasas de la alianza**, episodio **Stone Beneath the Prefect's Name / Piedra bajo el nombre del prefecto**. Es el primer episodio histórico en construcción: contiene tres objetivos principales y seis secundarios, en un mapa de 320 × 320. El contenedor incluye una sola misión; la campaña completa tendrá 30. El siguiente episodio previsto es el refugio civil de Jerusalén y todavía no se incluye.

## Qué descargar y cómo instalar

Para empezar en español, usa `caesarea-opening-es-ES-standard-20261027.zip`. El paquete exterior `caesarea-opening-private-kit-20261027.zip` conserva además las otras cinco variantes, escenarios de editor, recibos y documentación. No hace falta instalar Bun, Python ni una herramienta de desarrollo en el ordenador del juego.

1. Cierra AoE2: Definitive Edition. Descomprime el ZIP español estándar en una carpeta de trabajo.
2. Localiza el perfil activo de AoE2:DE. Desde el gestor de mods puedes usar «Abrir directorio» sobre un mod instalado para reconocerlo. La ubicación habitual es `%USERPROFILE%\Games\Age of Empires 2 DE\<perfil>\mods\local\`. Si hay varios perfiles, utiliza el que abre tu juego.
3. Dentro de `mods\local`, crea `COF-Private-Caesarea`. Copia ahí el contenido del ZIP de la variante. Debe quedar exactamente `COF-Private-Caesarea\resources\_common\campaign\CDF_FaithOrigins_PrivateOpening.aoe2campaign`. La carpeta `resources` debe estar directamente dentro de `COF-Private-Caesarea`.
4. Abre el juego en español, entra en el gestor de mods y activa el mod local si aparece con casilla. Reinicia el juego. Busca la campaña en **Un jugador → Campañas → Campañas personalizadas**; la ubicación y las etiquetas pueden variar según la build. Selecciona la apertura de *Las brasas de la alianza*. El menú de campaña sigue pendiente de comprobación en tu versión.
5. Si el contenedor no aparece, el kit exterior incluye `editor/es-ES/standard/01-administrative-records-caesarea.aoe2scenario`. Copia ese archivo a la carpeta de escenarios del mismo perfil, habitualmente `<perfil>\resources\_common\scenario\`. En **Editor → Cargar escenario**, elige ese nombre. Dentro del editor abre **Menú** y la opción de probar el escenario. Conserva el original: guardarlo desde el editor genera otra versión y otro hash.

La instalación local sigue el [procedimiento publicado en el foro oficial](https://forums.ageofempires.com/t/how-do-you-create-a-installable-mod/125688); el acceso general a campañas personalizadas aparece en la [guía oficial](https://www.ageofempires.com/news/custom-campaigns-for-age-of-empires-ii-definitive-edition-2/). Esta entrega no se publica en el portal de mods. Usa formatos nativos de AoE2:DE; Steam es el primer entorno de prueba, y otras instalaciones requieren comprobar su compatibilidad por build.

## Cómo jugar la misión

Deja terminar la introducción: primero habla la crónica objetiva y después Miriam de Cesarea. Son subtítulos; esta entrega no incorpora voces grabadas. Consulta el panel **Objetivos** durante la partida. Las banderas tienen nombres de destino y los círculos están dibujados en el suelo; al seleccionar un personaje verás su nombre de tarea.

1. Junto a la costa empiezan tres **portadores de registros de dedicación**, numerados 1–3. Lleva a cada uno al círculo **Recogida de registros**. Deben ser esos tres personajes originales. Después espera el mensaje de recepción y el nuevo objetivo.
2. Lleva a cada portador al **Patio de copias**, al este y algo al norte. Las llegadas se acumulan: no necesitan estar los tres simultáneamente, pero deben seguir vivos hasta que se expida el registro. Lleva también al **Copista — registro aún no expedido** al círculo y selecciónalo allí. Esa selección autoriza el pago único de **40 madera y 20 oro**, después de las tres llegadas. Si falta dinero, no debe cobrarse una parte ni expedirse el registro.
3. Tras la confirmación, ese mismo copista pasa a ser el portador del registro expedido. Llévalo al **Archivo del camino norte**. Una visita anterior a la expedición no completa la entrega. La misión cierra sus tareas opcionales al registrar esta entrega final; después muestra el desenlace y la recomendación del siguiente episodio.

Puedes hacer los secundarios antes de la entrega final, en el orden que prefieras:

| Objetivo | Acción concreta | Resultado previsto, una sola vez |
|---|---|---|
| Suministros de hogares | Lleva **Suministros del hogar 1** a **Suministros del hogar oeste**, y el 2 al destino este, junto al patio de copias. | 100 alimento y 50 madera. |
| Etiquetas dañadas | Desde el norte, lleva ambos portadores de etiquetas al **Copista costero: dos etiquetas**. | Nota histórica y pista; sin reconstruir las palabras perdidas de la inscripción. |
| Almacén | Selecciona **Almacén dañado — selecciona para reparar por 50 madera**. | Cobra 50 madera, restaura su salud completa y concede 200 alimento y 100 madera. La acción se autoriza seleccionando el edificio. |
| Comerciante | Lleva al **Comerciante costero** al **Puesto receptor del comerciante**, al este del patio, y selecciónalo después de llegar. | Cobra 50 oro y concede 150 alimento y 50 madera. |
| Guía | Lleva al **Guía del camino norte** al **Cruce del guía**, junto al archivo. | Señala el camino alternativo que ya existe hacia el interior. |
| Hogares voluntarios | Lleva los dos grupos del norte al **Refugio voluntario costero**. | 100 alimento y 25 oro. No sustituyen a los portadores principales. |

Conserva las identidades originales. Perder un personaje opcional debe fallar solo su tarea. Perder al copista antes de la entrega final, o un portador principal antes de la expedición, debe derrotar la misión. Esta apertura civil no tiene enemigos ni plazo secreto; la utilidad estratégica de las recompensas y el reto de cada dificultad siguen pendientes de calibración.

## Cambiar idioma o perfil

El kit exterior contiene seis ZIP: `en` y `es-ES`, cada uno con `easy`, `standard` y `hard`. Instala **una sola variante a la vez**: todas usan la misma ruta interna de campaña. Para cambiarla, cierra el juego y sustituye el contenido de tu carpeta privada con el ZIP elegido. No cargues una partida guardada de otra variante.

Los textos están dentro del escenario; no necesitas un mod adicional de cadenas. El perfil depende del archivo instalado. Cambiar la dificultad en el menú del juego no recompila este prototipo.

| Perfil del archivo | Alimento / madera / oro / piedra inicial | Ayuda de navegación |
|---|---|---|
| easy | 402 / 172 / 97 / 0 | Visión adicional de ambos recorridos. |
| standard | 350 / 150 / 85 / 0 | Destinos señalados; reconocimiento del recorrido durante la partida. |
| hard | 297 / 127 / 72 / 0 | Mismos destinos y objetivos; menor stock inicial. |

Todos permiten pagar el objetivo principal y los costes secundarios sin depender de recompensas previas. Se deshabilitan producción y trabajo económico de estos personajes en la primera iteración. Las reservas de recuperación y sustituciones del diseño aún no tienen implementación nativa; no hay recuperación automática de los originales perdidos.

## Qué comprobar al jugar

La compilación ha comprobado las seis variantes, sus scripts XS, la lectura de cada escenario y la extracción del contenedor con hash idéntico. También pasan 35 pruebas nativas enfocadas y 158 pruebas Bun. Ninguna de esas comprobaciones ejecuta AoE2. La revisión técnica independiente es conforme para este subconjunto privado; no aprueba el slice completo ni la campaña histórica.

El kit incluye `OBSERVACIONES.template.json`. Al probar, conserva el nombre de variante, su hash y la build que muestra el juego. Lo útil es comprobar la misión completa: orden de narradores; los tres pasos principales; secundarios y recompensas sin duplicación; guardar/cargar a mitad de las entregas y después del pago; entrega final con un único desenlace. Un fallo de menú y un fallo de objetivos se registran por separado. Puedes jugar mientras continúa el desarrollo; no hace falta completar una batería de pruebas para que avancemos.

El mar se sitúa al oeste según una costa moderna de referencia; el relieve está aplanado en este prototipo. Los participantes, patios y caminos locales son ficción documentada. No se presenta este mapa como restitución arqueológica de la ciudad romana, ni la inscripción como relato del proceso de Jesús.

La evidencia técnica y los hashes por variante se conservan en `MANIFEST.json` dentro del kit y en `docs/qa/campaign-design/caesarea-private-opening-build.json` del proyecto. El registro de revisión está en `tests/fixtures/native-history/private-delivery-independent-review.md`.
