# Imperial32 — revisión independiente del dossier real alineado

18Octubre2026. Revisor gpt-6.1-sol. Candidato1ebafca, unidadreviewoficialpropia g10/sesióna3886e7d, basada en develop4248102. Overview y review_queue recuperados; cola vacía. Ninguna edición de implementación o contenido por el revisor. No aprobación formal de d00002incompleto.

## Resultado por alcance

P1original de f35ad5c CERRADO TÉCNICAMENTE para el dossier real32en1ebafca. Se conserva el hallazgo original en /tmp/imperial32-independent-review.md y su copia histórica del proyecto: aquella entrega no se convierte retrospectivamente en válida.

El audittool nuevo requiere cambios por unP2separado descrito abajo; no se concede conformidad final de ese tool en1ebafca. No reabre i00006S1ni su aprobación formal4248102.

## P1original resuelto en contenido real

Leído y extraído episodes[]/32-defeat-and-withdrawal-adrianople del candidato. o2/req1–2soncheckpoint-entity-presence con gatei00006ycheckpointPresencePlan exacto; o3/req1–2siguen current-entity-presence con presencePlan exacto i00005. Factorycopia opcionalmente ambos planes sin defaults nuevos. Wikisahora imprimen esos planes sin ejecutar capacidades.

Fixturepropio /tmp/imperial32-real-round2-fixture.ts, JSONfuente/tmp/imperial32-round2-episode.json, log/tmp/imperial32-real-round2-fixture.log. Adapta sólo metadatos de planificación al perfil estricto de referencia, sin mutar los discriminantes authored o2/o3. Validador tipado devuelve[].499aserciones propias:90combinaciones4of6foot×2of4mounted hasta victoria REAL por tickyenter-phase, con avance intro/o1/o2/o3, pagos, observaciones frescas y desplazamientoW/C→SW. Incluye cambios de grupos originales, presencia no simultánea, salida/dead/unknown/lookalike/soporte, faseincorrecta, generacióncausal, receipt/flagsinsuficientes, save/load, pago180F80Wuna vez, finalabandonado y prioridadderrota. Mantiene controleslegacycurrent. No confunde latcho3con victoria.

Comparación JSONindependiente:31dossiers anteriores y31blueprints son estructuralmente idénticos a1d8dc2a. Para32frenteaf35ad5c, worldContract/mapPlan/difficulty/secondaryObjectives/secondaryBudget/historicalBrief/historicalOutcome/screens son idénticos. Sólo objectivePlan/provenance/capabilities/planes cambian dentro del dossier; no se altera historia, geometría, recursos, IDs o cuotas para ocultarP1. Mapa y DSMno se vuelven a certificar por este alineamiento. Código/tests/ADR/propuesta i00006son idénticos a4248102formalmente aprobado.

## P2 — El clasificador confunde claves descriptivas o contenedores cero con deadlines positivos

Nuevo tools/design/civic_difficulty_audit.script.py, deadline_fields. El walker registra cualquier valor truthy cuya clave contenga deadline/timeLimit/countdown/expires/clock, incluyendo texto y objetos cuyos valores numéricos son todos cero. No demuestra un deadline estructurado positivo.

Reproducción propia /tmp/civic-audit-independent-review.py, desde elcheckoutcon `python3 /tmp/civic-audit-independent-review.py`:

- {'stateMachine':{'phaseClock':'relative-to-phase-entry'}} → ['/stateMachine/phaseClock']
- {'deadlineSecondsByDifficulty':{'easy':0,'standard':0,'hard':0}} → ['/deadlineSecondsByDifficulty']
- {'editorialReviewNotes':{'deadline':'Do not introduce any deadline'}} → ['/editorialReviewNotes/deadline']

Un reloj relativo sin vencimiento, cero segundos en todos los perfiles y una instrucción editorial negativa no son presión temporal. El tool los reporta como explicitStructuredDeadlinePresent=true y puede excluir de staticRiskCandidate un episodio cívico cuyo presupuesto idéntico sí merecería inspección. El reporte actual62no contiene estos casos y sus0deadlines siguen reproducibles; el defecto afecta a la regla reutilizable, no demuestra una cuenta actual errónea ni invalida el dossier32.

Criterio de cierre: reconocer evidencia numérica positiva o predicado estructurado de vencimiento real, ignorar prosa/planificación/reloj relativo sin límite y contenedores sin valores positivos. Añadir regresiones negativas anteriores y positivas para un deadline válido con segundos por dificultad. Mantener missingbudget/profilesfailclosed; ninguna detección da aprobación de jugabilidad. Espera reevaluación del hashcorregido; el revisor no implementa la solución.

## Resto del audit y fuentes

El modo check readonly reproduce exactamente los hashes y datos persistidosschema2. Cobertura9campaigns,7con0dossiers;62dossiers,54riskcandidates,8conhostiles,0deadlines,212objetivosprincipales,384secundarios,2553pantallas. Los hashes se recomputan antes/despuésde lectura; eliminar profile/budget/recurso requerido produce error, no se rellena silenciosamente. Valores de prosa ordinaria y roughDuration/warningsno se cuentan en la prueba base; el P2precisa el caso de claves descriptivas. Predicatekindsdetecta checkpoint-entity-presence donde corresponde.

Archivo civic-difficulty-mechanical-audit-62-2026-10-17.json byteporbyteidéntico al reporte62de f35ad5c. No se refecha ni reatribuye snapshot17Octcomo18Oct.

Wikirenderer ejecutado directamente en memoria para22/30/31/32, comprobando presencia de cada plan existente en salida; sin escrituras. Metadata real separados entre checkpointyfinal; no cambiaelcontenido previo.

Selections33/34sólo cambian historicalSelectionfrenteaf35, sin convertirse en dossiers ni cambiar sus IDs/orden/mecánica. Audits17Octconservan atribución y cautelas, conflictos de día/mes y lecturas no realizadas. ColeccióngeográficaSirmium18Octatribuida a gpt-6-luna, restringida a marco regional, fases y límites; no ubicación de acceso379, sala, muelle o máscara seca. Esta revisión comprueba límites/documentación, no revalida globalmente fuentes históricas ni afirma haber leído las obras citadas completas.

## Gates propios1ebafca

- bun run validate: exit0,107tests/424expectativas; docs/campaignválidos. /tmp/imperial32-round2-validate.log.
- python3 tools/design/test_design.py:58testsOK. /tmp/imperial32-round2-python.log.
- python3 tools/design/verify.py: exit0,62/278dossiers,2553pantallas,384secundarios,36assets adicionales,0aprobados. /tmp/imperial32-round2-design.log.
- FixtureREAL:499aserciones/90pares hasta ambasAPIs, exit0. Auditoríaestática reproducida y adversariosP2registrados.

Sin test:exportnuevo: códigoi00006formal idéntico, ningún adaptador modificado en este delta. Nativeobserver/IA/terreno/packing/gameplay/historia siguen gates propios. Pendiente fix del toolP2 antes de conformidad final del alcanceextra. Sin edición de contratos ni aprobación de d00002.

## Reevaluación del audittool —18Octubre2026, dca4079

Delta inspeccionado sobre1ebafca: sólo civic_difficulty_audit.script.py y nuevo test_civic_difficulty_audit.py; dossier, JSONsnapshot, runtimeTS y archivos restantes no cambian. P2CERRADO para este candidato. El detector ignora clock/prosa/bools, no usa truthinessde contenedores y reconoce límites positivos soportados. El predicado real phase-deadlineexige los tres perfiles enteros positivos y rechaza datos malformed, sin convertir ausencia de datos en ausencia de presión.

Reejecutado el fixture independiente /tmp/civic-audit-independent-review.py: los tres repros originales ahora dan[], hashes/datosrecomputados coinciden,9campaigns/7zero y missingbudget/profilefailclosed siguen pasando. Pruebas propias adicionales:6negativos(infinito,boolseconds,negativo,revisionmetadata,prosa,clocknumérico) y un predicado válido anidado dentro de objectivePlan/predicate/requirements;7aserciones pasan. Tests permanentes nuevos:4testsOK. Modo check readonly pasa con exactamente62dossiers/54riesgos/8hostiles/0deadlines/212objetivosprincipales/384secundarios/2553pantallas; no modifica ni refecha el snapshot.

Conforme técnicamente con el alcance revisado en dca4079: P1original32cerrado en1ebafca y P2deltool cerrado en este delta, sin nuevosP1/P2detectados. No se repiten validate/Python58/fixture499porque el delta no toca sus archivos; sus resultados propios sobre1ebafcase conservan arriba y la publicación ejecutará su gate oficial. No es aprobación formal de d00002ni de fuentehistórica, IA, observernativo, geografía o juego. S1i00006formal sigue intacto. Unidadg10se retira oficialmente conservando tip y evidencia externa.

## Wiring y protección contra obsolescencia —18Octubre2026, c78fa8152819dd8d23b6d8b052c38b1ac8cff0a1

Unidadreviewpropia reabierta oficialmente g10/sesióna3886e7d. Inspeccionado exclusivamente el delta c78sobre dca: read/fingerprints/build_auditadmitenrootexplícito, check_reportcentraliza comparación y verify.pyla invoca con el rootde validación. documentation.validator.tsya ejecuta verify.pyytest_design.py, y test_designimporta las5pruebas de auditoría. No cambia JSONsnapshot/dossier/runtimeTS, por lo que no se repiten499aserciones de32ni exportación.

Comprobaciones propias:5testsstandaloneOK; suitePythonintegrada63testsOK (/tmp/imperial32-final-python.log); verifyactualexit0 (/tmp/imperial32-final-verify.log). No se repite todo validate porque el delta no cambiaTypeScript ni contenido; el gate oficial de publicación lo ejecutará.

Fixturepropio adicional /tmp/civic-audit-wiring-independent.py, log /tmp/civic-audit-wiring-independent.log: roottemporal explícito, reporte alterado sólo sourceSha256, sólo counts, y bytes reales de un archivo fuente cambiados sin cambio semántico (newline). verifydetecta Stale mechanical audit en los tres casos. Restaurar fuente/reporte elimina el error cívico. El espejotemporal usa symlinks de assets y conserva sus denegaciones independientes Unsafe reference path; no se atribuye aprobación global a ese espejo. El checkoutreal pasa verify. Ninguna escritura se realiza en el repositorio.

Conforme técnicamente con el alcance revisado a c78fa81: P1de32cerrado en1ebafca, P2de auditoríacerrado en dca4079 y wiringantistaleverificado en este delta. Sin nuevosP1/P2detectados. Se conservan fechas y evidencias iniciales. No aprobación formal de d00002/S3/S1incompletos, ni de historia/native/gameplay. Retirooficialg10conserva tipc78y evidencia externa.
