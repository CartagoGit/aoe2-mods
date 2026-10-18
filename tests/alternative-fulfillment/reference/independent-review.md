# Revisión independiente de i00007/S2

18 de octubre de 2026 · revisor `gpt-6.1-sol` · implementadores `gpt-6` y `gpt-6-luna`.

Estado: revisión técnica de fuente completada hasta `a945a2625b008cf81fdf1b25f30d5a3bd44e52a6`; pruebas finales, hash integrado y aprobación formal pendientes. Este borrador no acredita una aprobación de DelendAI.

La revisión se realiza en la unidad oficial `wip/gpt-6.1-sol/review/i00007-S2-g1/fulfillment-reference-review`, sesión `2fcc367e`. El revisor no ha modificado la implementación ni las pruebas. Se consultaron el overview, las capacidades vivas y la cola de revisión de DelendAI, además de las instrucciones, traspasos, propuesta y [ADR aprobado](../../../docs/architecture/alternative-fulfillment.md).

## Hallazgos reproducidos y correcciones

| Caso | Reproducción independiente | Corrección inspeccionada |
|---|---|---|
| Prioridad de derrota | Un `shared tick` con derrota conocida y lote espacial desconocido conservaba `terminal=null`. | `79c6771` evalúa esa derrota antes del rechazo espacial. Repetido: derrota con escrow intacto. |
| Elegibilidad causal | Un trabajador declarado como salida derivada compartida no producida permitía comprometer una receta; `generationReady=false`. | `79c6771` consulta elegibilidad; `0b6f69d` limita los inputs del primer v3 a originales y rechaza productores compartidos. |
| Restauración del core | Se aceptaban fase u objetivo desconocidos, secundario ausente, recompensa desconocida y terminal incompatible con su fase. | `0b6f69d` añade validación semántica exclusiva del envoltorio v3. Las cinco reproducciones rechazan. |
| Acciones compartidas externas | `destroy-entity/constructor` y `record-forbidden-entry/unknown` podían lanzar al validar el estado delegado. | `0b6f69d` y `e3e2d01` comprueban muerte autoritativa y pertenencia de identidades antes de delegar. |
| Observación restaurada | El campo de observación podía faltar, provocando un fallo en la próxima transición. | `e3e2d01` exige el envelope y rechaza entidades con secuencia nula. |
| Salida de fase | Reservar, abandonar la fase del plan y cancelar dejaba una reserva inaccesible en un mundo no terminal. | `9db42be` impide abandonar un plan incompleto. Repetido: la cancelación sigue disponible y devuelve exactamente el escrow. |
| Reserva restaurada fuera de fase | Alterar una reserva a otra fase declarada conservando membership permitía cargar el mismo bloqueo. | `a945a26` rechaza planes activos incompletos fuera de su fase, conservando el escrow congelado en derrota. |

No quedan hallazgos de fuente abiertos de estas reproducciones. La comprobación final de las regresiones automatizadas permanece pendiente.

## Compatibilidad y límites

Se compararon directamente con `4be89b5b2801f54503d3a1cc4763ea942f975850`: esquema v2, esquema/factory/reducer del snapshot v2, fixture de checkpoint y lock de cadenas conservan sus bytes. El modelo de acciones añade un parser compartido y el compilador proyecta explícitamente v3 sobre la maquinaria existente; no se copia el motor de referencia.

El revisor recalculó estos resultados del fixture legado con stock `10F/20W/30G/40S` y las demás cuentas vacías:

| Evidencia v2 | SHA-256 |
|---|---|
| Fingerprint del contrato | `6ce58d83eb099c0324dce3a0e338773b390d1c49d7b47b2d5605276a769a5ac1` |
| Snapshot canónico inicial | `0b3281bdca1992db26f0a1c1f38be1ab8a4e1f32da38da025dad8c0a58aafbab` |
| IR canónico compilado | `bd53f051c74e7abf75dba31f6a7c30fff0bb9124906756cc7213161fb0e6b329` |

Los límites v3 son explícitos: un plan, hasta ocho servicios y ocho recetas por servicio, máximo 4096 selecciones, trabajadores distintos entre servicios, inputs originales, una zona por identidad en cada observación y como máximo un predicado de llegada inicial por secundario. El último límite evita una colisión de índices de los recibos heredados sin modificar v2. El fingerprint v3 cubre el plan completo y el contexto efímero rota al cargar.

El adaptador nativo y Python siguen rechazando perfiles compuestos. La generación se representa como elegibilidad causal de una identidad latente de referencia. Ningún dato de este informe acredita creación física de unidades, UI, navegación, geografía, dificultad, diversión o pruebas de AoE2. S3 y los gates de autoría histórica continúan pendientes.

## Validación

Ejecución independiente intermedia en `65acde00491507b046ac7034446af5082a18a246`: `bun run validate`, salida 0; 108 tests, 426 aserciones, comprobación documental y una campaña validadas. El adaptador no cambia en S2.

La ejecución final del candidato completo y su evidencia integrada se añadirán al concluir las pruebas adversariales pendientes. Las 33 decisiones, 95 expectativas financieras y 24 testigos especificados por S1 no se presentan aquí como pruebas de juego.
