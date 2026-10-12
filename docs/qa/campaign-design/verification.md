# Verificación de la entrega de diseño

Alcance: nueve campañas históricas, 39 escenarios y dos escenarios de laboratorio. El piloto Milvio comparte la misión C01. No hay 39 mods terminados ni evidencia de partidas. Las matrices de cada misión permanecen pending y los presupuestos estimated.

Integridad: `python3 tools/design/verify.py` y `python3 tools/design/test_design.py`; resultados estructurados en [design-integrity.json](design-integrity.json). Se verifican bilingüismo, voces, rutas sin ciclos, fuentes, transformación geográfica, rosters/bancos finitos, hashes/licencias y asignaciones oficiales. Las pruebas adversariales deben rechazar español ausente, voz errónea, reserva excedida, ciclo y presupuesto insuficiente; también prueban orientación y recorte geográfico sin vértices internos. Las quince pruebas Python incluyen pérdida del ledger del taller, agua de Karbala asociada a otras familias, pago repetido/asignación insolvente y oleadas incompatibles con el abastecimiento o iguales entre dificultades. También rechazan norte/sur unidos por alias, dos treguas en un solo punto y retirada de familias sin vínculo al abastecimiento.

`bun run validate` acredita contratos, compilación, documentación y fixture; no certifica historia, diversión o navegación del mapa final. La revisión independiente y aprobación formal se registran sobre commits técnicos/integrados mediante DelendAI. Recuperar estado vivo del servidor antes de trabajar.

GAME VERIFIED requiere mapas rasterizados, footprint/transporte, fases/ledgers tras guardar/cargar, dificultad, rendimiento, medios/layouts/progreso y coexistencia reales en AoE2. PRODUCTION READY requiere 17 traducciones revisadas, arte/audio/derechos aprobados, contenido calibrado según [protocolo](../../design/production-contract.md) y release:check del artefacto real. Estas tareas tienen propuestas propias y no se ocultan como pruebas pasadas.

## Ampliación en curso d00002

La base de39escenarios dispone ahora de234objetivos secundarios, tres estrategias por misión y1496pantallas históricas EN/es. Los15casos adversariales de diseño pasan, incluidos receptores solapados, reservas opcionales y persistencia atómica. Los casos corresponden a contratos estáticos; no acreditan disparadores nativos, accesibilidad del mapa final, diversión ni equilibrio de partidas. La revisión de odiseas y el diseño de episodios nuevos siguen en curso. El número273es un objetivo editorial, no contenido ya completado.
