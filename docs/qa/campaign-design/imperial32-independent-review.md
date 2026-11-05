# Revisión independiente imperial32 — bloqueo de presencia por checkpoint

Revisor gpt-6.1-sol. Candidato f35ad5c109395ff8804ded3d01a9cc2b4039d101 sobre develop1d8dc2a929b1fbc8e9db0dae655df5c0b8a884f4. Unidad review propia abierta oficialmente por DelendAI, wip/gpt-6.1-sol/review/batch-all-g8/verdicts, sesión25bec362. El runtime reutilizó g8; candidato incorporado por fast-forward únicamente dentro de ella. Ninguna edición en el repositorio; checkout compartido intacto. Overview, discovery/workflow y review_queue consultados; cola vacía, sin veredicto formal sobre d00002incompleto.

## P1 — El diseño exige presencia limitada a checkpoint, capacidad que la referencia actual no expresa

Alcance: nuevo32-defeat-and-withdrawal-adrianople/display30/f00003S35. o2requiere4originales foot actualmente oeste y2mounted actualmente central; o3requiere4foot+2mounted actualmente suroeste y180F80W. Texto, qa y presencePlan dicen que ambos checkpoints anteriores quedan liberados tras o2, sin residencia continua. Sin embargo, los cuatro requisitos usan el mismo current-entity-presence actual sin lifetime o liberación explícitos. requiredCapabilities/presencePlan citan la referencia i00005S1como implementada, sin identificar que esta nueva combinación necesita semántica adicional.

La referencia vigente reevalúa en victoria TODA presencia de objetivos latched que sean antecesores requeridos: packages/gameplay-state/live-entity-presence.helper.ts:129–146; los dos accesos terminales de capability-state.reducer.ts usan esa comprobación (enter-phase victory y tick). ADR0005 lo documenta: el terminal requiere nuevo batch y recheck de requisitos latched relevantes. El esquema estricto sólo tiene id/kind/entities/destinations/requiredCount; no expresa duración, checkpoint-only, release o sustitución. No hay evidencia de una regresión frente al contrato S1ya aprobado: el nuevo contenido demanda una capacidad distinta del comportamiento documentado.

Reproducción propia: /tmp/imperial32-reference-fixture.ts proyecta los requisitos reales a un perfil tipado válido y validateScenarioCapability devuelve[]. Arranca por intro/phase1, registra originales, latcho1, phase2, batchfresco4footW+2mountedC, latcho2, phase3, pago180F80W, nuevos grupos válidos4footSW+2mountedSW, latcho3. Un tick final fresco y enter-phase victory fresco devuelven ambos terminal=null aunque objectiveLatches=[o1,o2,o3]. El fallo no es que falte observar o completar o3: se reexige o2en destinos abandonados. Evidencia de estados /tmp/imperial32-terminal-reproduction.json; error intencional /tmp/imperial32-terminal-failure.log.

La regla obliga en el terminal a4footW y4footSW con sólo6identidades originales. En la geografía del dossier son zonas separadas, sin solape físico. Por tanto no existe una asignación físicamente válida que complete ese terminal. No debe certificarse victoria por el mero latcho3 ni emular una pertenencia simultánea a zonas disjuntas.

Comandos:

```
export DELENDAI_AGENT_ID=gpt-6.1-sol
bun /tmp/imperial32-reference-fixture.ts
bun /tmp/imperial32-reference-fixture.ts --assert-terminal
```

El primero informa90combinaciones y290aserciones positivas, y muestra explícitamente expectedvictory/actualnull. El segundo falla con expectedvictory/receivednull. No se cuenta ese fallo como test superado. Los imports absolutos apuntan a la unidad review de esta sesión y el JSON extraído está en /tmp/imperial32-episode.json.

Criterio de cierre: registrar infraestructura real para lifetime explícito/reusable de presencia por checkpoint, definir compatibilidad de perfiles existentes y su política de terminal, implementar referencia/compilación/validación/snapshot con revisión independiente y luego reevaluar este dossier hasta terminal real. Mantener defaultyfingerprints/semántica de casos existentes según contrato; no quitar globalmente rechecks, cambiar arrived por presencia, congelar cohortes, alterar identidades ni fingir un campo ejecutable nuevo. El diseño32queda bloqueado para promoción mecánica hasta esa decisión/implementación; historia/native/game siguen pendientes por separado. No se modifica i00005S1ni se revoca su aprobación por este informe.

No se detectaron P2adicionales dentro del alcance revisado.

## Evidencia restante

-90subconjuntos conjuntos15×6correctos en cada evaluación de presencia o2y o3;290aserciones propias. Incluyen reparto erróneo, historial insuficiente, observaciones secuenciales no simultáneas, salida/reentrada, cambio de originales, apoyo no sustituto, desconocido rechazado, muerto no contado, dos pérdidas toleradas/tercera irrecuperable por grupo, pago180F80Wuna vez tras carga y necesidad de batchfresco al latch. Estas propiedades locales pasan; la victoria integral falla como arriba.
-31episodios y31blueprints anteriores son estructuralmente idénticos a1d8dc2a. Cambios de formato no son nuevos cambios semánticos. Identidad/progreso/lock activos no se modifican. Frontmatter de i00003es idéntico byte por byte; su único delta es acceptance pendiente S3sobre límites de oposición, sin cambio de lifecycle/review. No formalapprove/globalhistoria.
-14support+4mountedoriginales son el ejército amigo inicial; footstragglers no son reemplazos militares. Hostiles8/14/22seleccionados, producción y movilizaciones desactivadas, miembros máximos no seleccionados ausentes. Roles genéricos no son IDs nativos certificados. Límites de persecución, adquisición, proyectiles y retorno son requisitos futuros explícitos, no IA implementada.
-MapaSVG renderizado con ImageMagick y visto en /tmp/imperial32-review-map.png. Ocho grounds ficticios con orientación regional coherente; ciudad26.5556,41.6769fuera del bbox26.6–26.76/41.7–41.87alSW.53centros potenciales únicos/18zonas. Mínimo centro76.62; radio calculado81.62tiles, frente al audit conservador81.24; ambos dentro del marco. Hash b6f15f52d9807a5efc8ba49b41edc345e14fddfc9913fb1bf6ffd39da27fea93coincide. No rasterantiguo/huellas/pathfinding/IAcertificados.
-Stock all-skip de tres perfiles recalculado inicio+banco−reservaopcional=1070F640W210G120S; costeprincipal180F80W. El presupuesto estático no demuestra tensión o pacing.
-Lectura directa seleccionada Ammianus31.12.3/10–17,31.13y31.15.1–4en Rolfe: derrota, variantes de muerte, dispersión y posterior ciudad/asíedio diferenciados. La fuente no ubica grounds ni autoriza rescate de Valens;31.15.4no garantiza entrada de supervivientes. La lectura latina y divergencia Yonge/hora ya comprobadas en revisión anterior mantienen su límite: hora≠millas, posición anterior≠campo. No se afirma crítica manuscrita o localización exacta. Marcus44recibe informes en vida clerical ficticia de Constantinopla; la narración posterior no es un despacho378que posea ni convierte al personaje en testigo.
-ModernDSM: script propio /tmp/imperial32-relief-review.py, ejecutado con uv/rasterio/numpy, verifica los1414samples, coordenadas interpoladas/pixelindices/valores, ocho5×5ventanas, min/maxyascenso/descenso por segmento, distancias y agregados.4376aserciones propias pasan; hashfuente y EPSG4326/Point coinciden. No reproduce ni sustituye4335del implementador, registra comprobación independiente. No añade dependencia al proyecto ni afirma datos del motor. Dataset distingue612×576ventana y351900válidos, y DSMmoderno de DTM378. Bandas0–7son candidato provisional dentro del rango schema existente, no transformación implementada/terreno histórico. Faltan superficie antigua, hidrología, suelo seco, rampas y huellas.

## Gates propios

- `bun run validate`: exit0,102tests/389expectativas, documentación/enlaces y campaña válidos; /tmp/imperial32-review-validate.log.
- `python3 tools/design/verify.py`: exit0,62dossiers/278selecciones,0aprobados,2553pantallas,384secundarios,36assets adicionales; /tmp/imperial32-review-design.log.
- `python3 tools/design/test_design.py`:57tests OK; /tmp/imperial32-review-design-tests.log.
- Fixture propio:90combinaciones/290aserciones locales pasan; prueba integral de terminal falla intencionalmente con --assert-terminal. Los gates estáticos no detectan este desajuste de lifetime.

No test:export: ningún adaptador cambió. No prueba AoE2, IA, balance, traducciones finales, historia global ni aprobación formal de slice. Retiro oficial conserva tip y evidencia externa; P1se entrega al arquitecto antes de promoción.

Fuente directa para las afirmaciones históricas acotadas: https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/31%2A.html .
