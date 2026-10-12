# IA y dificultad

Cada facción declara objetivos, economía, recursos iniciales, suministro, producción, reserva, movilización, reacción, límites y retirada. Los refuerzos tienen origen, causa, contrajuego, maxWaves, unitsPerWave, intervalo y totalBudget. El validador rechaza reservas insuficientes; un campo reserve por sí solo no ejecuta una IA.

El adaptador soporta reservas iniciales con AI None y órdenes tras el tiempo de reacción, eventos finitos de spawn y scripts PER explícitos mediante aiScript. Las economías standard/scripted de enemigos exigen PER; el exportador no sustituye una economía por oleadas. La serialización se prueba; la estrategia efectiva se acredita jugando.

El contrato permite easy/standard/hard como perfiles internos. Los enums del parser distinguen EASIEST=4, STANDARD=3, MODERATE=2, HARD=1, HARDEST=0 y EXTREME=-1. El adaptador usa xsGetDifficulty con comparaciones exactas/rangos, validado por xs-check; la correspondencia de la UI y el balance requieren prueba en el juego. Los nombres internos no se presentan como nombres oficiales.

Conservar trama/victoria; variar recursos, tiempos, pistas, coordinación y composición. Medir duración, pérdidas, gasto, presión, ataques, rutas alternativas y estancamiento. No declarar mediciones si son estimaciones. Revisión en tres niveles con estrategias razonables, sin requerir exploits. Una misión táctica, una diplomática y una económica prueban variedad antes de expandir la saga.
