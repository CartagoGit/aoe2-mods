# Technical laboratory screens

Two fictional campaigns, 32×32 exception. English source with complete Spanish; all persistence/UI tests remain pending.

## The Roads Remember

{
  "id": "route-observer",
  "kind": "fictional technical-lab person",
  "occupation": "Observer of choices",
  "temperament": "Curious, explanatory",
  "knowledgeLimits": "Only the fictional experiment; no historical eyewitness or authentic accent claimed."
}

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.route-pilot.title` / always | none → next | The Roads Remember | Los caminos recuerdan |
| `campaign.route-pilot.fact` / always | collection-narrator → next | This is a fictional technical laboratory. It checks independent campaigns, cumulative choices and recaps, without representing a historical event. | Este es un laboratorio técnico ficticio. Comprueba campañas independientes, elecciones acumulativas y recapitulaciones sin representar un hecho histórico. |
| `campaign.route-pilot.personal` / always | route-observer → next | I keep the record of these paths. Choose one, then return to discover that remembering another does not erase the first. | Guardo el registro de estos caminos. Elige uno y vuelve para comprobar que recordar otro no borra el primero. |
| `campaign.route-pilot.advice` / always | collection-narrator → next | Destroy A for Route A or B for Route B. Your record remembers both after replay. Continue with An Open Chronicle (CDF-T02). | Destruye A para la ruta A o B para la ruta B. El registro recuerda ambas tras rejugar. Continúa con Una crónica abierta (CDF-T02). |
| `campaign.route-pilot.instructions` / corresponding laboratory state | collection-narrator → next | Complete the preparation, then destroy A or B. If both fall at once, Route A has declared priority. | Completa la preparación y destruye A oB. Si ambos caen a la vez, la rutaA tiene prioridad. |
| `campaign.route-pilot.hints` / corresponding laboratory state | collection-narrator → next | The two routes remain available on replay; completing B does not remove A. | Las dos rutas siguen disponibles al rejugar; completarB no eliminaA. |
| `campaign.route-pilot.scouts` / corresponding laboratory state | collection-narrator → next | The lab is32×32. Your guard starts west; the two targets are northeast and southeast. | El laboratorio mide32×32. Tu guardia empieza al oeste; los dos objetivos están al noreste y sureste. |
| `campaign.route-pilot.history` / corresponding laboratory state | collection-narrator → next | No historical event is represented. This checks engine behaviour with a fictional layout. | No se representa un hecho histórico. Se comprueba el motor con una disposición ficticia. |
| `campaign.route-pilot.loss` / corresponding laboratory state | collection-narrator → next | Your essential guard was lost or the test window expired. Reload or restart. | Has perdido al guardia esencial o ha terminado el plazo de prueba. Carga o reinicia. |
| `campaign.route-pilot.victory-a` / corresponding laboratory state | collection-narrator → next | Route A is recorded. Continue with An Open Chronicle (CDF-T02); replay may also recordB. | La rutaA queda registrada. Continúa con Una crónica abierta (CDF-T02); al rejugar puedes registrarB. |
| `campaign.route-pilot.victory-b` / corresponding laboratory state | collection-narrator → next | Route B is recorded. Continue with An Open Chronicle (CDF-T02); replay preservesA. | La rutaB queda registrada. Continúa con Una crónica abierta (CDF-T02); al rejugar se conservaA. |

## An Open Chronicle

{
  "id": "route-archivist",
  "kind": "fictional technical-lab person",
  "occupation": "Keeper of the cumulative ledger",
  "temperament": "Calm, precise",
  "knowledgeLimits": "Only the fictional experiment; no historical eyewitness or authentic accent claimed."
}

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `campaign.route-successor.title` / always | none → next | An Open Chronicle | Una crónica abierta |
| `campaign.route-successor.fact` / always | collection-narrator → next | This is a fictional technical laboratory. It checks independent campaigns, cumulative choices and recaps, without representing a historical event. | Este es un laboratorio técnico ficticio. Comprueba campañas independientes, elecciones acumulativas y recapitulaciones sin representar un hecho histórico. |
| `campaign.route-successor.personal` / always | route-archivist → next | I keep the record of these paths. Choose one, then return to discover that remembering another does not erase the first. | Guardo el registro de estos caminos. Elige uno y vuelve para comprobar que recordar otro no borra el primero. |
| `campaign.route-successor.advice` / always | collection-narrator → next | Recommended earlier: The Roads Remember (CDF-T01). You may begin here; the recap explains both paths. | Se recomienda jugar antes Los caminos recuerdan (CDF-T01). Puedes empezar aquí: la recapitulación explica ambos caminos. |
| `campaign.route-successor.recap-missing` / recap-missing | collection-narrator → next | No previous route is available. The earlier lab had two endings; you may continue without it. | No hay una ruta anterior disponible. El laboratorio anterior tenía dos finales; puedes continuar sin jugarlo. |
| `campaign.route-successor.recap-a` / recap-a | collection-narrator → next | RouteA is remembered. RouteB remains available in the earlier lab. | Se recuerda la rutaA. La rutaB sigue disponible en el laboratorio anterior. |
| `campaign.route-successor.recap-b` / recap-b | collection-narrator → next | RouteB is remembered. RouteA remains available in the earlier lab. | Se recuerda la rutaB. La rutaA sigue disponible en el laboratorio anterior. |
| `campaign.route-successor.recap-both` / recap-both | collection-narrator → next | Both earlier routes are remembered. The ledger has kept both choices. | Se recuerdan ambas rutas anteriores. El registro conserva las dos elecciones. |
| `campaign.route-successor.recap-unknown` / recap-unknown | collection-narrator → next | Progress could not be consulted. Here is the same sufficient summary; no prerequisite blocks you. | No se ha podido consultar el progreso. Aquí tienes un resumen suficiente; ningún requisito bloquea la partida. |
| `campaign.route-successor.victory` / corresponding laboratory state | collection-narrator → next | The recap test is complete. Return to the campaign menu. | La prueba de recapitulación ha terminado. Vuelve al menú de campañas. |
| `campaign.route-successor.instructions` / corresponding laboratory state | collection-narrator → next | Read or skip the recap. The10-second lab ending tests presentation, not historical gameplay. | Lee o salta la recapitulación. El final de laboratorio a10segundos prueba presentación, no juego histórico. |
