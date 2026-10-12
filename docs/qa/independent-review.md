# Revisión independiente de la fábrica

Fecha 2026-10-12. Baseline 4f6ea4ada828bb4a77f69f64d87faf8a1a89540e; implementador GPT-6, instancia revisora distinta /root/independent_review, también GPT-6. Revisión autorizada por el propietario. El revisor ejecutó 33/33 pruebas y tres round-trips; comprobó además persistencia de PER. Solicitó correcciones técnicas.

| Prioridad | Hallazgo | Corrección y evidencia |
|---|---|---|
| P1 | Proveedores locales compartían caché | ID configurado y hash executable/argv; regresión ejecutando dos WAV distintos y misma versión |
| P1 | Huella del ZIP omitía motor/generadores/dependencias | Hashes engine, locks y todos los generadores TS/Python; pruebas mutan cada entrada y conservan cambios editoriales/QA |
| P1 | Alias y colisiones de rutas nativas | Función portable compartida, comparación sin mayúsculas, reserva de compilados y colisiones globales con hash distinto; test con dos campañas |
| P1 | Slices activaban contenido antes de escenarios/IDs | Preparación staging y materialización conjunta bajo propiedad de campañas/lock/glosario; propuestas oficiales y cinco handoffs actualizados |
| P2 | WAV aceptaba alineación/chunks/frames inválidos | blockAlign consistente, chunks completos con padding y frames íntegros; regressions negativas |
| P2 | Victoria final sin progreso | Obligatorio fuera de fixture; misiones intermedias pueden omitirlo y rutas finales pueden escribir sus propias claves |
| P2 | IDs ambiguos de eventos/reservas | Unicidad de triggers y reservas dentro de cada facción; añadida unicidad de QA/compatibilidad |
| P2 | Política lingüística podía reducirse o pisar archivos | Exactamente 17 locales de colección y destinos únicos; pruebas de eliminación y duplicados |

El comprobador staging distingue esquemas parciales y campañas completas; nunca incorpora borradores al proyecto ni acredita multimedia/IDs/exportación. Las pruebas globales siguen recorriendo todas las campañas activas. No se implementaron campañas históricas completas.

## Restricción de la aprobación formal

DelendAI rechazó registrar request_changes desde la unidad del implementador: exige una unidad propia kind=review. Rechazó después entrar con gpt-6-independent-review porque agent debe ser el ID exacto del modelo; no permite sufijos para diferenciar instancias. Ambas instancias son GPT-6, mientras requirePeerReview exige reviewer distinto del implementer. No se inventó identidad, desactivó la política ni autoaprobó.

La revisión técnica de otra instancia existe, pero no equivale a aprobación formal. El cierre oficial requiere un modelo revisor diferente real y autorizado o una resolución legítima del propietario/runtime. Permanece pendiente también el bootstrap del gate de develop. El documento de auditoría y verification.json conservan ambos bloqueos.

## Segunda revisión técnica

La instancia revisora confirmó conformidad con 2843c0df707df45e633f22d5fc87e04c66d2b0b6: validate=0, 41/41 pruebas,124 expectativas y tres round-trips reales. Los ocho hallazgos están resueltos. Su única aclaración documental se aplicó: exportar únicamente campañas materializadas; staging no es un target de exportación. El propietario autorizó revisión formal con GPT-6.1 para cumplir legítimamente la identidad diferente exigida por DelendAI; pendiente del resultado real.
