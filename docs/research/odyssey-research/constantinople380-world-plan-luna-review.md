# Revisión independiente del plan de mundo de Constantinopla (S3)

**Revisor:** gpt-6-luna  
**Fecha:** 2026-10-24  
**Base:** develop `b9cff83`  
**Versión revisada:** `4c881123e25e3a06a69cb1a62bd05c82d365d93b`  
**Alcance:** revisión independiente del componente del plan de mundo y sus textos asociados. No es aprobación de S3, aprobación histórica, prueba de juego ni certificación de producción. La actividad parcial previa de GPT-6.1 no se toma como revisión independiente finalizada.

## Resultado

No quedan hallazgos bloqueantes en el componente tras la corrección de `4c88112`. Durante la revisión del tip `28b624a` señalé que dos objetivos hablaban de hogares/lector como si fueran actores presentes, mientras las condiciones y entidades sólo comprobaban la llegada de cajas/copias a zonas. El tip final lo aclara como puestos de recogida y mesa receptora con destinatarios fuera de escena; las ofertas, instrucciones, racionales y textos de finalización quedan alineados en inglés y español. Se conserva el contrato de llegada a zonas, sin añadir actores ni cambiar predicados o alcance de infraestructura.

También se añadió `sourceBindings` para la nota retrospectiva, con dos citas y punteros explícitos a la selección canónica. La referencia conserva el patrón de identidad de fuente ya usado por el dossier y declara que no es una clave global de cadena.

## Comprobaciones

- La selección canónica coincide con el orden y la continuidad declarados: episodio `34-church-transfer-constantinople`, “Las puertas de Nueva Roma”, seguido de `29-council-and-final-perspective-constantinople`, “Bajo el mismo cielo oriental”. La nota retrospectiva distingue explícitamente la perspectiva del jugador de lo que el escriba ficticio Marcus podría conocer en 380.
- Los seis costes del plan coinciden con `imperial34-care-allocation-plan.json`. El cálculo independiente de combinaciones financiables da 9/9 en fácil, 7/9 en estándar y 3/9 en difícil. No encontré discrepancias en los importes ni en los recibos documentados.
- Los identificadores de las 19 ubicaciones y los 21 corredores cierran; los centros de tile recalculados coinciden con el marco geográfico publicado y permanecen dentro de la cuadrícula de 400×400. Las rutas de trabajo usan corredores existentes y sus longitudes declaradas concuerdan con la suma recalculada de segmentos.
- Los hashes de los datos OSM originales y GeoJSON derivado coinciden con sus manifiestos; ambos conservan 60 líneas/ways y 1184 coordenadas. La comparación publicada de 513 segmentos contra 21 corredores y 10 áreas circulares informa un margen mínimo de 10,4113 tiles. Ese control sólo compara con la línea costera actual: el expediente no demuestra máscara de tierra, ribera de 380, pendiente, huellas de edificios ni navegabilidad. El propio plan mantiene esas comprobaciones pendientes.
- Las 45 pantallas tienen 131 segmentos de subtítulos en total. Los segmentos concatenan exactamente el texto EN/es-ES, ninguno supera 32 palabras. Los textos se declaran originales; la presentación nativa y QA de localización siguen pendientes.
- `sourceInputs` incluye ocho entradas. Verifiqué que las dos citas del nuevo `sourceBindings` señalan pasajes y punteros de selección canónica, y que el vínculo está calificado como contextual, no como nueva aprobación histórica.

## Límites y estado

La verificación se hizo sobre datos estáticos, contratos y geometría reproducible; no ejecuté una partida ni confirmé presentación nativa. El plan no aporta todavía una máscara de terreno antigua, prueba de ruta sobre el mapa del juego, auditoría arqueológica de parcelas ni ajuste de balance con jugadores. La licencia ODbL y atribución de OSM aparecen en manifiestos y créditos; cualquier distribución autónoma del SVG debe conservar también los avisos de atribución Copernicus indicados en el expediente DSM.

`bun run validate` terminó correctamente: comprobación TypeScript/Biome, 142 tests (2069 expectativas), documentación y `campaign:validate` para una campaña. Este resultado no convierte la revisión en aprobación de S3 ni sustituye QA nativa, histórica o de producción.
