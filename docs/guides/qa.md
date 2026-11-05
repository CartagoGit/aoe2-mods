# QA y auditoría adversarial

Pruebas automáticas: contratos/referencias/IDs, trazabilidad, traducciones, reservas, ciclos, cuadrícula, voz/recursos, CLI y round-trip del parser/contenedor. Su alcance se registra en audit.md. No prueban diversión, narración real, IA, balance ni persistencia de una partida guardada.

La revisión adversarial recibe especificación e IR y busca victoria prematura, orden alternativo de objetivos, objetivos destruidos antes de mostrarse, falta de recursos, ruta bloqueada y resolución terminal duplicada. Reportar pasos, esperado/observado, versión, hash, severidad y solución concreta. La revisión del mismo implementador es autoauditoría, no peer review.

En el juego: dificultad, inactividad prolongada, matar/convertir/guarnecer/embarcar personaje crítico, bloquear puentes, impedir desembarcos, destruir producción, cambiar diplomacia, guardar/cargar antes de decisiones y finalizar ambas condiciones en un tick. Repetir con mods simultáneos y cambios de idioma.

Un fallo blocking impide release. Los major necesitan corregirse o decisión editorial explícita razonada; los minor quedan documentados. Todo arreglo añade regresión cuando ésta verifica un comportamiento real y no replica el código. El informe incluye casos pendientes, no una lista de checks marcada automáticamente como pasada.
