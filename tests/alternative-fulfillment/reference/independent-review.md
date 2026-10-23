# Revisión independiente de i00007/S2

23 de octubre de 2026 · revisor `gpt-6.1-sol` · implementadores `gpt-6` y `gpt-6-luna`.

Revisión técnica del candidato `cffa31053532c2003f4123326bf570a0218a0ac5` completada sin hallazgos abiertos. La integración oficial y el registro formal de aprobación siguen pendientes al escribir este informe. Este documento por sí solo no es una aprobación de DelendAI.

El revisor reanudó mediante `work enter` la unidad oficial `wip/gpt-6.1-sol/review/i00007-S2-g1/fulfillment-reference-review`, sesión `2fcc367e`, consultó overview, capacidades vivas, propuesta y cola de revisión, y leyó instrucciones, traspasos y [ADR aprobado](../../../docs/architecture/alternative-fulfillment.md). Incorporó el candidato a su propia unidad para ejecutarlo. No modificó implementación ni pruebas; reclamó exclusivamente este informe. El borrador anterior y sus siete reproducciones permanecen en el historial de `554d6e94e3bd35f19eb32364e7121042c166f6f7`; esta continuación inspeccionó el código actual y ejecutó sus regresiones, sin presentar aquellas ejecuciones anteriores como nuevas.

## Hallazgos de esta continuación

| Hallazgo reproducido | Resultado anterior | Corrección y comprobación final |
|---|---|---|
| Trabajo en el patio receptor de otra alternativa | Cambiar `meal-direct.workZoneId` a `materials-court` producía cero diagnósticos: la comparación cubría solamente la recepción de la misma receta. | El validador compara cada zona de trabajo con todas las recepciones, por identidad y huella. La misma reproducción devuelve `fulfillment.contract`; hay regresiones de identidad y solapamiento. |
| Cierre terminal de un secundario en un mundo activo | Cambiar un secundario a `closed-at-terminal` conservando `terminal=null` permitía cargar el estado. | La carga rechaza ambos sentidos de la inconsistencia terminal/secundarios. La reproducción falla con `fulfillment.snapshot-invalid: terminal optional lifecycle`; regresión automatizada incluida. |
| Cobertura de guardado y carga incompleta | Los checkpoints solo comprobaban igualdad y rechazo del epoch anterior, sin continuar el mundo restaurado ni cargar terminales válidos. | Once snapshots cubren reserva, cancelación, compromiso, salida, trabajo, generación, recepción, prefín y terminales. Se continúa con el contexto nuevo, se repiten reserva/compromiso/generación sin doble cargo ni salida, se alcanza victoria y se comprueba inmovilidad terminal. |

Se revisó también la corrección del fixture: las alternativas de refugio usan `materials-court`, `kit-court` y `host-court` respectivamente. La presencia compartida final exige al receptor de comida; v3 añade las salidas seleccionadas y los dos hogares originales en su patio propio. No se exige al trabajador volver a un almacén ajeno al ADR. Una prueba positiva permite perderlo después de registrar su trabajo y completar después la entrega con los destinatarios reales.

## Aceptación comprobada

La implementación sigue S1 mediante un perfil y snapshot v3 estrictamente optativos. Mantiene la envoltura de escenario v1, proyecta explícitamente el contrato compartido sobre v2 y reutiliza su reducer, transacciones de recursos y observador espacial. La selección y los costes proceden del registro; escrow, gasto comprometido, gasto fijo y gasto opcional se contabilizan por separado. No hay un comando nuevo de crédito libre o escritura arbitraria de predicados que complete una receta.

Las pruebas ejecutadas incluyen 27 ensayos de reserva por dificultad/pareja, los 95 recorridos de referencia de la matriz y los 24 testigos anteriores a la financiación mediante acciones opcionales reales de la referencia. Cubren selección parcial, duplicada, desconocida o de otro servicio; insolvencia conjunta; costes cero, fraccionarios y desbordados; preview obsoleto; cuentas protegidas; recompensa posterior al pago; cancelación y devolución única; bloqueo tras compromiso; trabajo, salidas y recibos cualificados; patio incorrecto; pérdida de salida o destinatario frente a pérdida exclusivamente opcional; y ambas APIs terminales con presencia fresca. Ocho carreras adicionales observan la muerte de una salida o destinatario en el mismo lote que solicita victoria. Los guardados prueban fingerprint, shares, escrow, identidad, versión y rotación del contexto de entrada.

Los límites de referencia son explícitos: un plan, hasta ocho servicios y ocho recetas por servicio, máximo 4096 selecciones, trabajadores distintos entre servicios, inputs originales, una zona por identidad y lote, y como máximo un predicado inicial de llegada por secundario. Este último límite conserva los recibos heredados sin modificar v2.

## Compatibilidad

La comparación directa con `4be89b5b2801f54503d3a1cc4763ea942f975850` no muestra cambios en el esquema v2, reducer/factory/esquema del snapshot v2, fixture de checkpoint ni lock de cadenas. Se recalcularon en la ejecución independiente los hashes del fixture v2 con stock `10F/20W/30G/40S` y las demás cuentas vacías:

| Evidencia v2 | SHA-256 |
|---|---|
| Fingerprint del contrato | `6ce58d83eb099c0324dce3a0e338773b390d1c49d7b47b2d5605276a769a5ac1` |
| Snapshot canónico inicial | `0b3281bdca1992db26f0a1c1f38be1ab8a4e1f32da38da025dad8c0a58aafbab` |
| IR canónico compilado | `bd53f051c74e7abf75dba31f6a7c30fff0bb9124906756cc7213161fb0e6b329` |

## Ejecución independiente

En la unidad del revisor, con el candidato incorporado en `a82889d5c60ff63b743c8bb25d129d652d4bff5b`:

- `bun run validate`: salida 0; 142 pruebas, 2069 aserciones, comprobación documental y una campaña validadas. Incluye las 34 pruebas del nuevo fixture.
- `bun run test:export`: salida 0; tres variantes, dos round-trips, `unsupportedModeRejected=true`, `gameVerified=false`.
- Repetición directa de las dos reproducciones anteriores: ambas rechazan tras la corrección.
- Renderer nativo: prueba automatizada de rechazo explícito del perfil v3 antes de abrir plantillas o escribir artefactos.
- Python: se alimentó `export_scenario` con el resultado real de `compileCapabilityProfile(v3)` dentro de su envoltura ScenarioIR v2; rechazo explícito `capability-not-implemented`, sin exportación.

La exportación usó `COF_PYTHON=/home/cartago/_projects/games/aoe2-mods/.venv/bin/python` y `RGE_CAMPAIGN_BIN=/home/cartago/_projects/games/aoe2-mods/.cache/toolchain/3c40203b650de9888ca82fae1276ea67bf3d3d93/rge_campaign`, las herramientas fijadas del checkout compartido, porque la unidad aislada no contiene una `.venv` propia. No se instaló ni modificó el adaptador. La validación intermedia anterior a la corrección había fallado por formato del fixture; su ejecución final pasa sin ese error.

## Límites y siguiente gate

La generación es elegibilidad causal de una identidad latente en la referencia. Los 95 recorridos, 24 testigos y 33 decisiones normativas de S1 no son pruebas de juego. Los round-trips pertenecen al fixture exportable existente, no al perfil v3. No se acredita UI, generación física de unidades, navegación, geografía histórica, calibración, diversión ni ejecución en AoE2. El adaptador continúa rechazando el perfil compuesto. S3 y los gates de autoría histórica siguen pendientes.

Falta únicamente registrar el veredicto independiente con el hash efectivamente integrado después de la publicación oficial y su gate. El implementador no queda autoaprobado por este informe.
