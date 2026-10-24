# Especificación de escenarios

El contrato exige: fecha/período/lugar, afirmaciones y personajes, geografía y mapa, facciones justificadas y economía, objetivos main/secondary con requisitos, victoria/derrota, variables iniciales, balance easy/standard/hard, narrativa intro/events/outro, tecnologías, recompensas, dependencias, medios, QA y métricas.

Los timers de objetivos del perfil actual cuentan desde el inicio del escenario. Una misión no puede depender del timer como si comenzara al activarse el objetivo. Los objetivos de destruir referencian una unidad permanente; una destrucción anticipada debe satisfacer después el requisito o tener recuperación documentada y probada.

El grafo exige referencias existentes y ausencia de ciclos; el flood-fill verifica la cuadrícula declarada, no el pathfinding del motor, las huellas de edificios ni los transportes. Derrota primero y variable terminal común previenen resoluciones múltiples en el diseño, pero el orden en un tick real requiere prueba.

No considerar terminado un escenario por tener unidades. Necesita información al jugador, vías de recuperación, duración estimada y medida separadas, escenarios de derrota, guardado/carga, tres dificultades y exploits reproducibles.

Eventos declarativos: triggers con condiciones timer/destroy/variable/objective/bring/resource y efectos set-variable/line/task/spawn/diplomacy/tribute. Una vez por evento, sin bucles. Los spawn consumen reservas declaradas y la suma de eventos no puede exceder maxWaves/totalBudget. victory.routes permite finales con claves separadas; el orden declarado arbitra coincidencias entre rutas. tecnologías vacías deja defaults; lista no vacía funciona como whitelist de tecnologías para las facciones del perfil.

El mapa admite baseTerrain y tiles con position, terrain y elevation 0–7 (límite del perfil). Usa los nombres del catálogo, nunca números a mano. No hay suavizado automático de colinas: el autor define pendientes transitables y las prueba en el motor. blocked modela obstáculos como muros de Gaia; la BFS abstracta no representa navegación, tamaño de edificios ni movimiento por agua.

Para elecciones, bring referencia una unidad y rectángulo from/to; para economía, resource comprueba un saldo mínimo. Un evento puede cambiar diplomacy (source/target/state/mutual) o transferir tribute. Todo tributo requiere en ese evento una condición resource que cubra su coste total, sin recursos de Gaia ni donantes infinitos. Los eventos son no repetitivos; decidir si la diplomacia es recíproca de forma explícita. Los objetivos también usan bring/resource sin duplicar reglas de compilación.
