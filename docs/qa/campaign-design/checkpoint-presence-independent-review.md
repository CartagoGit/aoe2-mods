# i00006/S1 — revisión técnica independiente

Revisor gpt-6.1-sol, implementador gpt-6-luna. Candidato1fc9f94, padre1d8dc2a. Unidad propia oficial wip/gpt-6.1-sol/review/batch-all-g8/verdicts, sesión25bec362; overview/workflow y review_queue recuperados. Cola vacía; candidato sin integrar, no aprobación formal. Sin ediciones de implementación por el revisor.

Resultado inicial: REQUEST CHANGES por P2. No se encontró P1. El caso principal32ya llega a victoria por ambas APIs, pero subsiste una dependencia terminal espacial cuando sólo existen checkpoints intermedios.

## P2 — Una presencia sólo de checkpoint exige indebidamente batch al terminal

packages/gameplay-state/live-entity-presence.helper.ts, victoryNeedsLivePresence: busca antecesores latched y llama objectiveHasLivePresence. Esa función se amplió para incluir el nuevo checkpoint. Por tanto el predicado que decide si exigir batchfresco terminal incluye checkpoint-entity-presence aunque el recorrido de reevaluación sólo incluye current-entity-presence.

Perfil válido, schema y validateScenarioCapability sin diagnósticos: checkpoint intermedio o2 seguido de o3con sólo pago180F80W, sin currentpresence en todo el perfil. Tras batchfresco/latcho2, salida de fase, pago y latcho3, tickvictory y enter-phasevictory sin batchdevuelven null. Adjuntar batchfrescoVACÍO vuelve tick a victory. Esa observación no tiene nada terminal que certificar; es una condición oculta heredada del checkpoint. ADR0006documenta que las comprobaciones terminales continúan incluyendo sólo current-entity-presence. Se pide mantener ese alcance también en el gate de frescura, sin debilitar legacycurrent.

Reproducción propia: `bun /tmp/checkpoint-independent-fixture.ts`, línea de salida checkpoint-only-terminal: latches[o1,o2,o3],tickWithoutBatch=null,enterWithoutBatch=null,emptyFreshBatch=victory. Fixture deriva del caso32de revisión anterior, proyecta predicados tipados válidos y construye el caso receipt-only por opt-out de presencia final; no importa los tests nuevos del implementador. No se exige que toda misión tenga presencia final, sólo que checkpoint no genere lifetime terminal escondido.

Cierre requerido: regresión checkpointintermedio→final sin currentpresence, victoria por AMBAS APIs sin nuevo loteespacial, incluyendo guardado/carga. Mantener freshbatchyreevaluación de final y predecesores currentlegacy. El caso directo checkpoint→victory continúa rechazado por validator/compiler. El arreglo debe ser reutilizable, no una excepción por IDs/destinos de32.

## Comprobaciones independientes positivas

Fixture temporal /tmp/checkpoint-independent-fixture.ts y log /tmp/checkpoint-independent-fixture.log:497aserciones positivas,90combinaciones de4of6foot×2of4mounted llevadas hasta victoria por ambas APIs. Incluye fases reales intro/o1/o2/o3, desplazamiento deW/C aSW, pago180F80W, nuevos batches monotónicos al latch y terminal. No da por victoria un mero latcho3.

Precondiciones positivas preparadas antes de los adversarios: wrongzone,dead,lookalike/supportsubstitute,unknown,duplicado,unknownzone, stale/guardado positivo, batchnuevo correcto, histórico+recordpredicate, faseincorrecta. Comprueba generacióncausal de un original declarado comoderived-token: el mismo lote falla antes de producir y pasa tras producción. Comprueba prioridad de derrota y finalcurrentabandonado por tickyenterphase. Legacycurrentenobjetivointermedio sigue bloqueando terminal al abandonar sus destinos: la semánticaADR0005no se debilitó.

Esquema nuevo estricto, mismo perfilv2/sourceenvelope, compilerconserva discriminante. Validador compartido valida identidades/destinos/cardinalidades y rechaza checkpointgobernando transición directaavictoria; compilerrechaza eseperfil. En reducers se reutiliza observer/generation/presence y se rechaza recordpredicate para ambos kinds. No se modificó snapshot/fingerprintfactory; los perfiles nooptin mantienen datos/defaults y el algoritmo previo. La ampliación del discriminante cambia el fingerprintde quien opta, de forma explícita; no introduce cambios a IDs o campañas.

Pythonmantiene checkpointPresencePlan separado de presencePlan y gate i00006nativepending. El bloque de validación de identidades/destinos/cardinalidad está repetido entre los dos kinds; helpercompartido podría evitar deriva, pero esta duplicación corta no es por sí sola unP1/P2 ni motivo para inventar una abstracción amplia. La factoryd00002optin no se revisa como parte deS1.

## Gates propios iniciales

- `bun run validate`: exit0,106tests/416expectativas; docs/campaignchecks válidos. /tmp/checkpoint-review-validate.log.
- `python3 tools/design/test_design.py`:58testsOK. /tmp/checkpoint-review-python.log.
- `COF_PYTHON=/tmp/i00006-export-venv/bin/python RGE_CAMPAIGN_BIN=/tmp/i00006-rge-toolchain/rge_campaign bun run test:export`: exit0,3variantes/2roundtrips, unsupportedModeRejected=true, gameVerified=false. /tmp/checkpoint-review-export.log. Tres hashes fuente de herramienta externa verificados contra config/toolchain.json; no se distribuye esa herramienta.
- Fixture independiente:497aserciones positivas/90pares completos, más comparaciónP2explícita. Un suiteverde no cierra elP2.

Pendientes: fixyreevaluación independiente antes de publicación/aprobación formalS1. S2observernativo,S3promoción, historiageografíayAoE2siguen sin aprobar. El P1def35ad5cfue una capacidad ausente, no una regresión de la referencialegacy; el nuevo kindloresuelve en su caso principal, sujeto a cerrar esteP2reusable.

## Reevaluación independiente —18Octubre2026, e532b4078430008ef0b1883ef1f62a259d253df0

Unidadoficialpropia g9, sesión e4d1d980. Se conserva íntegro el hallazgo inicial REQUESTCHANGES1fc9f94arriba. Nueva revisión del delta e532b40sobre1fc9f94, sin cambios de implementación por el revisor.

P2resuelto técnicamente. victoryNeedsLivePresence ahora consulta sólo objetivos con current-entity-presence; observer/latch continúan admitiendo ambos kinds y el recorrido terminal conserva íntegramente los checkslegacycurrent. Los nuevos helpers privados separan el gate terminal del gate local. No hay excepción por episodio, identidad ni destino.

Reejecutado el fixture propio adaptando únicamente sus imports a la nueva unidad. /tmp/checkpoint-independent-fixture-round2.ts, log /tmp/checkpoint-independent-round2.log:499aserciones positivas y90pares completos hasta victoria por tickyenterphase. Incluye la reproducción original receipt-only, ahora ambasAPIsdanvictorySINbatch, y nuevas comprobaciones propias tras serializar/cargar ese estado. --assert-receipt-only ya no falla. El fixture sigue verificando precondiciones adversariales, causalidad de generación, fase, pagos y protecciónlegacy/final. La ronda inicial de17Octno se reescribe como exitosa.

Exportpropio18Oct: COF_PYTHON=/tmp/i00006-export-venv/bin/python y RGE_CAMPAIGN_BIN=/tmp/i00006-rge-toolchain/rge_campaign, bun run test:export exit0;3variantes,2roundtrips,unsupportedModeRejected=true,gameVerified=false. Log /tmp/checkpoint-review-round2-export.log. El gatePython58tests de ronda inicial sigue aplicable a archivosPythonidénticos en este fix; no se repite sin cambio o fallo nuevo.

Observaciónmenor, noP1/P2: el nombre private isContinuousLivePresenceRequirement/objectiveHasContinuousLivePresence significa 'requiere reevaluación terminal', no residencia continua durante las fases. isTerminalPresenceRequirement/objectiveHasTerminalPresence sería más preciso para evitar confusión futura en adaptación nativa. No altera el resultado técnico.

No nuevosP1/P2detectados en e532dentrodeS1. Conforme técnicamente sujeto al gateglobalpropio final registrado a continuación. No aprobación formal antes de integración ni deS2/S3/native/historia/jugabilidad. Factoryoptind00002continúa fuera delalcance deS1yrequiere su reevaluación posterior.

Gateglobalpropio18Octsobre e532b40: `bun run validate` exit0,107tests/424expectativas; documentación/enlaces y campaignvalidate válidos. Log /tmp/checkpoint-review-round2-validate.log. Conformidad técnica S1confirmada; P2inicial cerrado para este hash. Ninguna aprobación formal emitida. Unidadg9se conserva abierta para revisión formal del hash integrado cuando se publique oficialmente.

## Delta de nomenclatura —18Octubre2026,39a9beda79fd95c7f3f14e2702d095d68b7e212b

Inspección propia del diff contra e532b40: sólo helperprivado isContinuousLivePresenceRequirement→isTerminalPresenceRequirement y objectiveHasContinuousLivePresence→objectiveHasTerminalPresence, sus llamadas y formato. Ningún cambio semántico. La observación menor de nomenclatura queda atendida.

Pruebas propias focales: `bun test tests/unit/checkpoint-presence.test.ts tests/unit/entity-presence.test.ts`, exit0,18tests/123expectativas. Log /tmp/checkpoint-review-rename-tests.log. La conformidad técnica de e532b40se extiende a39a9bed; no se repite el gatecompleto porque este delta sólo renombra privados. Sin nuevosP1/P2detectados. Pendiente publicaciónoficial y revisiónformalS1delhashintegrado; sin aprobaciónnative/historia/game.

## Revisión formal e integración del veredicto —18Octubre2026

Implementación publicada oficialmente en84d4f2da0053fdaaa749dd9ee469d4e823dfc685. Inspección propia: árbol de packages/tests/ADR/diseño idéntico a39a9beda; sólo submitmetadata adicional. `62bf2e5` registróS1review y canonicalizó incidentalmente pathnamef00003; `de508b8` restauró el nombre anterior con100%identidad. El primer gate falló en docs:check por enlaces legacy rotos, según comunicación de publicación del implementador/root; el revisor verificó los dos deltas Git reales, no afirma haber ejecutado personalmente aquel primer gatefallido. La publicación corregida declaróinstallfrozen+validatepasados.

Propio validate sobre84d4f2dexit0:107tests/424expectativas ydocs/campaignválidos, log /tmp/checkpoint-review-integrated-validate.log. proposal_review status confirmó S1in_review/implementergpt-6-luna, sinreviewer. La primera llamadaapprovefue rechazada por falta de evidence.acceptanceCriteriapara los cuatrocriterios; no se contabiliza como aprobación. Segunda llamada concriterios4/4yevidencia empírica fue aceptada: reviewerindependiente gpt-6.1-sol, S1done, review-statedone/veredictoapproved,quorum1. Commits automáticos6b5d6efclaimyb5d324dapprove.

El tool volvió a canonicalizar f00003ENLAunidadreviewg9. Se comprobó igualdadbyteporbyte con el contenido integrado84d4y se restauró exclusivamente el nombrelegacyencommitce44434,0líneasinsertadas/eliminadas. No se tocó el renamecolateral compartido ni se editó frontmatter/manualmenteestado de propuestas.

Publicación oficial de unidadreviewg9: landed=true, mergedSha4248102f523d5edd0554e59bc11f15ed2cf79199, contra84d4f2da. Certificación declarada y pasada: bun install --frozen-lockfile + bun run validate. Runtime retiró worktree yrefs g9 después de integrar. EsteSHAcontiene el veredicto formal S1; S2yS3continúanpending y la propuesta permanece abierta. No aprueba d00002, observernativo,AoE2,historia ni contenido. El informe conserva el P2original y todas las rondas con sus hashes propios.
