# Asignaciones y gates de MiniMax M3.1

El alcance vigente son nueve odiseas y278episodios. Cada episodio tiene un slice mecánico explícito en su propuesta oficial. Las propuestas permanecen bloqueadas: el arquitecto debe cerrar todos los dossiers, capacidades, geografía y nivelación antes de entregar autoría. Las treinta fichas ampliadas de faith-origins y los treinta y dos de la odisea imperial son borradores en revisión, pendientes de escenario nativo.

Lee [plan](../design/odyssey-production-plan.md), [selecciones](../design/odyssey-selections.md), [asignaciones estructuradas](../design/assignments.json), [arquitectura](../architecture/overview.md) y el traspaso. Recupera estados vivos de DelendAI antes de elegir cualquier slice.

| Campaña / título inglés | Propuesta oficial | Episodios | Slices |
|---|---|---:|---|
| faith-origins / Embers of the Covenant | [f00004](../delendai/proposals/blocked/f00004-autoria-designada-embers-of-the-covenant.md) | 30 | S1 conformidad; S2 metadatos; 30 slices individuales; S7 promoción |
| imperial-church / The Eagle and the Cross | [f00003](../delendai/proposals/blocked/f00003-autoria-designada-the-eagle-and-the-cross.md) | 34 | S1 conformidad; S2 metadatos; 34 slices individuales; S6 promoción |
| jewish-tradition / Keepers of the Unbroken Word | [f00005](../delendai/proposals/blocked/f00005-autoria-designada-keepers-of-the-unbroken-word.md) | 30 | S1 conformidad; S2 metadatos; 30 slices individuales; S7 promoción |
| church-of-rome / The Keys of the Eternal City | [f00006](../delendai/proposals/blocked/f00006-autoria-designada-the-keys-of-the-eternal-city.md) | 32 | S1 conformidad; S2 metadatos; 32 slices individuales; S7 promoción |
| new-rome / Beyond the Golden Gate | [f00007](../delendai/proposals/blocked/f00007-autoria-designada-beyond-the-golden-gate.md) | 32 | S1 conformidad; S2 metadatos; 32 slices individuales; S8 promoción |
| first-caliphs / Beneath the Desert Stars | [f00008](../delendai/proposals/blocked/f00008-autoria-designada-beneath-the-desert-stars.md) | 30 | S1 conformidad; S2 metadatos; 30 slices individuales; S8 promoción |
| first-fitna / The Shattered Oath | [f00009](../delendai/proposals/blocked/f00009-autoria-designada-the-shattered-oath.md) | 28 | S1 conformidad; S2 metadatos; 28 slices individuales; S8 promoción |
| umayyads / From Damascus to the Far Horizon | [f00010](../delendai/proposals/blocked/f00010-autoria-designada-from-damascus-to-the-far-horizon.md) | 32 | S1 conformidad; S2 metadatos; 32 slices individuales; S8 promoción |
| house-of-ali / The River Remembers | [f00011](../delendai/proposals/blocked/f00011-autoria-designada-the-river-remembers.md) | 30 | S1 conformidad; S2 metadatos; 30 slices individuales; S7 promoción |

Los IDs de los39escenarios y sus slices anteriores permanecen reservados. Por eso un número S mayor puede preceder a S3: se ejecuta `DependsOn` y `order`, nunca el orden numérico del nombre. Cada propuesta enumera cinco actos, fecha, lugar, operación e identidad de cada episodio. La promoción espera al final ampliado efectivo, no al antiguo final de la base.

Pilotos: f00001 laboratorio T01/T02; f00002 Milvio. i00003 pertenece al arquitecto: fases/transacciones, geografía/transporte, reserva nativa y voz/progreso. s00001 corresponde al arquitecto/tester con motor. d00002/S2–S10 cierran los dossiers de cada odisea y S11 consolida el traspaso. Estas tareas no se transfieren a MiniMax.

## Matriz de actos y trabajos

### Embers of the Covenant

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6, 7, 8 | S8, S9, S10, S11, S12, S3, S13, S14 |
| act-2 | 9, 10, 11, 12, 13, 14, 15 | S15, S16, S17, S18, S19, S20, S21 |
| act-3 | 16, 17, 18, 19, 20, 21 | S22, S4, S23, S24, S25, S5 |
| act-4 | 22, 23, 24, 25, 26, 27 | S26, S27, S28, S29, S30, S31 |
| act-5 | 28, 29, 30 | S32, S33, S6 |

### The Eagle and the Cross

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6 | S3, S7, S8, S9, S10, S11 |
| act-2 | 7, 8, 9, 10, 11, 12 | S12, S14, S15, S13, S16, S4 |
| act-3 | 13, 14, 15, 16, 17, 18, 19 | S17, S5, S18, S19, S20, S21, S22 |
| act-4 | 20, 21, 22, 23, 24, 25 | S23, S24, S25, S26, S27, S28 |
| act-5 | 26, 27, 28, 29, 30, 31, 32, 33, 34 | S29, S30, S33, S34, S35, S36, S31, S37, S32 |

### Keepers of the Unbroken Word

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5 | S3, S8, S9, S10, S11 |
| act-2 | 6, 7, 8, 9, 10, 11, 12 | S12, S13, S14, S15, S16, S17, S18 |
| act-3 | 13, 14, 15, 16, 17 | S4, S19, S20, S5, S21 |
| act-4 | 18, 19, 20, 21, 22, 23, 24 | S22, S23, S24, S25, S26, S27, S28 |
| act-5 | 25, 26, 27, 28, 29, 30 | S29, S30, S31, S32, S33, S6 |

### The Keys of the Eternal City

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6 | S8, S9, S10, S11, S12, S13 |
| act-2 | 7, 8, 9, 10, 11, 12 | S3, S14, S15, S16, S17, S18 |
| act-3 | 13, 14, 15, 16, 17, 18 | S19, S20, S21, S22, S4, S23 |
| act-4 | 19, 20, 21, 22, 23, 24, 25 | S24, S25, S26, S27, S28, S29, S30 |
| act-5 | 26, 27, 28, 29, 30, 31, 32 | S31, S5, S32, S33, S34, S35, S6 |

### Beyond the Golden Gate

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6, 7, 8 | S9, S10, S11, S12, S13, S14, S15, S16 |
| act-2 | 9, 10, 11, 12, 13, 14, 15, 16, 17 | S3, S17, S18, S19, S4, S20, S21, S5, S22 |
| act-3 | 18, 19, 20, 21, 22 | S23, S24, S25, S26, S6 |
| act-4 | 23, 24, 25 | S27, S28, S7 |
| act-5 | 26, 27, 28, 29, 30, 31, 32 | S29, S30, S31, S32, S33, S34, S35 |

### Beneath the Desert Stars

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6, 7 | S9, S10, S11, S12, S13, S14, S3 |
| act-2 | 8, 9, 10, 11, 12, 13, 14 | S15, S16, S17, S18, S19, S20, S21 |
| act-3 | 15, 16, 17, 18, 19, 20, 21 | S22, S4, S23, S24, S5, S6, S25 |
| act-4 | 22, 23, 24, 25, 26 | S26, S27, S7, S28, S29 |
| act-5 | 27, 28, 29, 30 | S30, S31, S32, S33 |

### The Shattered Oath

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5 | S3, S9, S10, S11, S12 |
| act-2 | 6, 7, 8, 9, 10, 11 | S13, S14, S4, S15, S16, S17 |
| act-3 | 12, 13, 14, 15, 16 | S18, S5, S19, S20, S21 |
| act-4 | 17, 18, 19, 20, 21, 22, 23 | S22, S23, S24, S6, S25, S26, S27 |
| act-5 | 24, 25, 26, 27, 28 | S28, S29, S30, S31, S7 |

### From Damascus to the Far Horizon

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3 | S3, S9, S10 |
| act-2 | 4, 5, 6, 7, 8, 9, 10, 11, 12 | S11, S12, S13, S14, S4, S15, S16, S17, S5 |
| act-3 | 13, 14, 15, 16, 17, 18, 19 | S18, S19, S20, S21, S22, S23, S24 |
| act-4 | 20, 21, 22, 23, 24, 25, 26, 27 | S6, S25, S26, S27, S28, S29, S30, S31 |
| act-5 | 28, 29, 30, 31, 32 | S32, S33, S34, S7, S35 |

### The River Remembers

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5 | S8, S9, S10, S3, S11 |
| act-2 | 6, 7, 8, 9, 10 | S4, S12, S13, S14, S15 |
| act-3 | 11, 12, 13, 14, 15, 16 | S16, S17, S5, S18, S19, S20 |
| act-4 | 17, 18, 19, 20, 21, 22, 23 | S21, S22, S23, S24, S25, S26, S27 |
| act-5 | 24, 25, 26, 27, 28, 29, 30 | S28, S29, S30, S31, S32, S33, S6 |

## Prompt de ejecución por slice

```text
Trabaja solo en <proposalId>/<sliceId> designado por DelendAI, bajo tu identidad real MiniMax M3.1. Base develop y unidad aislada oficial; confirma ancestro, reclama exclusivamente Files. Lee AGENTS.md y recupera gate/review policy del servidor.

Tu fuente editorial aprobada es docs/design/odysseys/<campaignId>.json y el expediente docs/wiki/<campaignId>/episodes/<scenarioId>/15-odyssey-dossier.md, junto a la geografía y biblia del narrador consolidadas por d00002. El catálogo base de39misiones conserva evidencia, no sustituye el dossier ampliado. No cambies la trama, el narrador, los resultados históricos, los mapas regionales, las rutas, los umbrales o los presupuestos por tu cuenta. No conviertas estimaciones en mediciones. Si una instrucción resulta incompatible con el motor, registra reproducción y devuelve la decisión al arquitecto; conserva trabajo independiente autorizado.

Materializa en staging con sourceLocale=en, todas las claves EN/es-ES, general factual antes de persona subjetiva, eventos ficticios declarados, mapas300–400 orientados geográficamente, roster finito y recuperación. IDs de unidades/terrenos/tecnologías vienen del catálogo fijado; los números de cadenas se asignan con ids:allocate solo en el slice de promoción que posee el lock/glosario. Cumple literalmente los predicados compuestos y estados; no uses un timer para fingir escolta, entrega, acuerdo o batalla.

Usa las capacidades reutilizables acreditadas; no toques packages/tools fuera de propuesta explícita. Si i00003/s00001 o los pilotos siguen pendientes, no desbloquees autoría nativa por suposición. Los17idiomas y medios mantienen estados reales; referencias descargadas no son arte de release aprobado. Sin generación pagada masiva ni publicación del mod.

Ejecuta staging:check --partial cuando la propuesta lo permita; completo sin --partial antes de promoción. Materializa campaña+IDs/glosario conjuntamente, bun run validate verde, export/candidate cuando aplique; adjunta hash, build y QA real en los slices que lo requieren. Solicita revisor distinto, corrige hallazgos, integra exclusivamente por work publish, aprobación formal según el runtime y nunca autoapruebes. Continúa únicamente con el siguiente slice oficialmente implementable.
```

El arquitecto mantiene los generadores/verificador del diseño. MiniMax no edita los dossiers generados; los cambios aprobados se realizan en catálogo/perfiles y se regeneran. Cada misión enlaza todos sus objetivos, pantallas, fuentes y coordenadas, evitando que el agente invente trabajo para rellenar una carpeta.

## Ampliación en curso y naming obligatorio

`d00002` prepara odiseas extensas: esta matriz asigna278slices de episodio, pero no cierra sus decisiones ni autoriza ejecución. Recupera sus estados reales antes de empezar. Ninguna capacidad faltante pasa a MiniMax por omisión. La base dispone de seis objetivos secundarios por misión, con predicados/financiación/estado/QA y tres estrategias en el catálogo y [plan](../design/odyssey-production-plan.md). Materializa todos esos contratos sin sustituirlos por timers, suministros infinitos ni eliminación de tareas difíciles. Respeta el naming i00004: responsabilidad.tipo.ts, importaciones directas, sin index/barrels y carpetas por dominio.

La [selección de las nueve odiseas](../design/odyssey-selections.md) contiene los278episodios y enlaza los nuevos documentos `14-odyssey-arc.md`. Cada entrada fija identidad, orden, acto, título EN/es, fecha, localización y operación principal. Es una selección editorial con auditorías de fuentes todavía en curso: no son278expedientes completos. No la uses para rellenar pantallas, nivelación o coordenadas con decisiones tuyas. Los episodios adicionales solo se asignarán tras los expedientes completos de d00002 y las capacidades acreditadas de i00003.

## Expedientes ampliados en revisión

Treinta episodios de faith-origins (órdenes 1–30) tienen expediente legible en `docs/wiki/faith-origins/episodes/<id>/15-odyssey-dossier.md` y fuente editable en `docs/design/odysseys/faith-origins.json`. Los generadores comparten identidad, transacciones, financiación, subtítulos y QA; los hechos, voz personal y decisiones de cada misión son autoría explícita del arquitecto. Hay 1.191 pantallas y 180 secundarios en los borradores ampliados. Los expedientes no están aprobados y sus planos SVG muestran controles geográficos, no terreno navegable. No produzcas binarios a partir de estos borradores.


## Voces de las odiseas ampliadas

La autoridad de diseño de voz ampliada es [odyssey-narrators.json](../design/voices/odyssey-narrators.json), con nueve fichas legibles en ese directorio y un plan de acceso al conocimiento para cada uno de los 278 episodios. La voz objetiva resume hechos y límites documentales antes de dar paso a la persona ficticia de campaña. No conviertas biografías inventadas en fuentes antiguas ni atribuyas acceso a concilios, revelaciones o motivos privados. Cada dossier debe precisar la colocación local; una edad compatible no demuestra presencia.

Marcus mantiene `imperial-clerk`, pero en la odisea ampliada su vida es c.334–403, frente al arco legado c.290–350. No copies recuerdos de 312 a los nuevos textos. La migración debe aprobarse antes de promoción nativa. Las biblias ampliadas siguen pendientes de revisión editorial y no autorizan nuevas campañas ni generación pagada de audio.


La apertura de imperial-church tiene dossiers individuales para los órdenes 1–3: sector táctico terrestre del Puente Milvio, preparación local en Milán y patios ficticios en Nicomedia. Entrada, objetivos, voz, pagos, fuerzas finitas y QA están especificados. Son 33 expedientes ampliados en total (1.317 pantallas, 198 secundarios); su revisión histórica y capacidades nativas siguen pendientes. El control territorial sostenido usa la semántica de derrota inmediata de la referencia: no inventar un periodo de gracia. No extraer cifras militares del roster ficticio como datos históricos.

Roma (orden 4) mantiene dos cadenas de solicitudes/registros y dos retornos distintos, cada uno respaldado por su propia recepción y salida. Arlés (orden 5) prepara tres puestos terrestres y distribuye seis ayudantes y tres asignaciones de120 de alimento antes de archivar un registro ficticio. Ni la audiencia ni las decisiones conciliares se convierten en votación jugable; no usar Ostia como sede por figurar un obispo de esa ciudad. Hay 62 borradores (2.553 pantallas, 384 secundarios; órdenes imperiales 1–30, 32 y 34), todos sujetos a los gates históricos/nativos.

Cibalae (orden 6) exige al menos ocho auxiliares originales realmente registrados al preparar la retirada y los cuatro cofres originales en el punto local de reunión; no sustituir el registro por toda la lista inicial ni por miembros del convoy opcional. Su desvío occidental debe ser viable sin combate ni secundarios tras auditoría nativa de los límites enemigos. La reunión local norteña no representa el itinerario histórico completo a Sirmio. El orden 7 conserva tres contextos jurídicos separados, provisiones rurales de 180/120, un pago de 90 madera/30 oro y tres resúmenes derivados con destinos propios. No crear una prohibición global de trabajo, un mercado de libertad personal ni una puntuación de obediencia religiosa.

Corrección cronológica de 324: Adriánopolis ocupa el orden 8 (S14), Crisópolis el 9 (S15) y la correspondencia alejandrina el 10 (S13). Los números incluidos en IDs semánticos no se reinterpretan como orden. Eusebio sitúa la carta en contexto posterior a la victoria; no se la presenta como causa de las batallas. `DependsOn` conserva S12→S14→S15→S13→S16→S4 y todas las propuestas siguen bloqueadas.

Words over Alexandria es el orden 10, ID estable `08-disputed-correspondence-alexandria`, slice S13. Conservar notas norte/este distintas, aviso derivado único y mensajero original. En o4, cada salida se apoya en su propio recibo de o3; ninguna llegada oriental previa cumple una llegada condicionada. El reparto no simula consenso, convierte una exhortación en verdad ni restaura una casa episcopal documentada. Los órdenes 8–9 ya tienen dossier, pero su nuevo contrato de transporte requiere capacidades y revisión antes de autoría.

The Maritsa Crossing (orden8, S14) y Across the Bright Shore (orden9, S15) comparten el [contrato pendiente de viajes con manifiesto](../research/odyssey-research/manifest-water-journeys.md). Respetar las identidades originales, las cuatro plazas compartidas por embarcación y el registro real de preparados/cruzados. Preparar diez auxiliares antes del último pago permite dos pérdidas posteriores; preparar ocho exige conservar los ocho. No sustituir déficit con originales que no figuren en el recibo. En Crisópolis, dos cargas norteñas y dos sureñas tienen receptores distintos; los secundarios son exclusivamente europeos. Cada embarque, cruce y desembarque requiere evidencia y capacidad nativa implementada. El contenido sigue bloqueado; MiniMax no implementará esa arquitectura ni elegirá nuevos pasos históricos.

Jerusalén (orden 13) prepara siete remesas originales distintas y seis trabajadores en cinco patios ficticios de la meseta. Respeta sus tres pagos separados: piedra/madera, madera y alimento/oro. Son preparativos; no certifican carga física, edificio terminado ni dedicación de 335. El año inicial exacto y las fases de la Rotonda permanecen cualificados. Los secundarios son seis operaciones finitas y se pueden omitir; la piedra que falta al inicio se obtiene de recolección ordinaria. El SVG romano descargado es una referencia moderna con CC BY-SA 4.0, no una planta acreditada de 326–330.

Constantinopla (orden 14, ID estable `03-new-capital`) exige reparto exacto 3/2/3 y asignaciones distintas de 80 madera/80 piedra, 60 madera/40 piedra y 120 alimento. Tres avisos entregan y regresan mediante sus propios recibos; los ocho trabajadores regresan mediante sus recibos de asignación. No sustituir once identidades por una cantidad agregada ni una visita previa por regreso. No añadir muralla teodosiana, acueducto de Valente, Santa Sofía de Justiniano, reparto estatal de pan o población de fe uniforme en 330. La ceremonia histórica permanece fuera de la causalidad del presupuesto ficticio.


Los órdenes15–16 añaden la carta persa sin fecha precisa y el concilio de Tiro. El primer mapa es un circuito local ficticio en Nicomedia, presentado como interludio retrospectivo después de330 sin fechar la carta después de330: tres contextos separados originan un paquete pagado y dos escribientes regresan mediante sus propios recibos. Ni entrega en Persia ni respuesta real quedan acreditadas. Tiro conserva dos cadenas de informes y ayudantes con receptores y presupuestos propios; solo los informes regresan causalmente. Dos resúmenes cualificados se derivan de tres notas exactas y un pago compartido, y se entregan en destinos distintos. Ningún pago decide veredicto o doctrina. Seis secundarios por episodio, tres enfoques combinables y viabilidad estática con todos omitidos. Son dos mapas400, geografía propuesta pendiente de relieve, costa antigua y navegación nativa. El nuevo localizador de Nicomedia tiene licenciaCCBYSA3.0, hash y crédito; es moderno y solo de investigación. Total actual:62 borradores,2.553 pantallas y384 secundarios;216 selecciones sin dossier y cero aprobaciones ampliadas.

No materializar f00003/S18–S19 mientras falten las aprobaciones del dossier y capacidades. S18 conserva el ID original de selección y la fecha corregida; S19 usa las atribuciones y lugares separados. No usar recibo de paquete para regreso de escribientes, recibo de ayudante para regreso de informe, ni cambiar destino para obtener victoria.


Órdenes17–19 corresponden a f00003/S20–S22, aún pendientes. Mantén las tres categorías de Arrio distintas sin elegir causa de muerte; en18 los dos libros quedan en sus patios, vuelven los cuatro escribientes por sus propios recibos y los avisos van a destinos diferentes. En19 las fuerzas son la selección inicial exacta, nunca miembros invisibles del máximo:20amigos y16/24/32enemigos, seis guardias constantes. Protege los seis hogares originales y conserva ambos accesos de o2 hasta completar o4; una visita pasada no satisface control actual. No generar tropas nuevas ni rescatar víctimas históricas. El patio seguro corregido es[28.948,41.012], no el anterior[28.948,41.009] sobre la costa representada. Requiere terreno antiguo, leashes, observer nativo, guardado/carga y combate probado antes de materializar. El cierre de acto recomienda el episodio20 yConcilios sin concordia sin completar la campaña ni lanzar automáticamente nada.


Orden20 corresponde a f00003/S23, pendiente. Dos patios receptores locales NO son dos concilios históricos dentro deSofia:Philippopolis queda fuera. No cambiar3/2trabajadores ni presupuestos140F40W/80F40W para simplificar; cada registro deriva de su propia nota y del único recibo receptor exacto. Ocho secundarios independientes, ninguna pérdida opcional derrota main, ninguna recompensa suple una nota original. Mantén fecha cualificada, común→Marcus con papeles heredados de su infancia, fases de arquitectura separadas, y aviso de continuar con el regreso deAlejandría sin terminar campaña. Nunca convertir apelaciones canónicas en voto de verdad o compra de autoridad. El compuesto nativo sigue bloqueado hasta su gate, aunque el validador estructural haya corregido IDs duplicados.


Órdenes 21–22 corresponden a f00003/S24–S25, todavía pendientes. Alejandría exige tres parejas originales distintas, tres ayudantes distribuidos uno por anfitrión y provisiones 150F/30W oeste, 150F/40W este, 150F/30W sur. Las tres notas se derivan de su propia pareja y del mismo recibo exacto de provisiones (o2/req-4), sin volver a cobrar. Los hogares permanecen con sus anfitriones. Milán guarda tres legajos y custodios en tres depósitos; solo los tres escribientes de informe regresan al patio sur. Su salida usa sus propias llegadas de o2/req-5, nunca las de custodios de req-4 ni las de legajos; no valen visitas anticipadas. Cada depósito recibe 100F/60W/20S. Conserva los siete/seis secundarios, sus identidades separadas, ventajas finitas y coste visible; todos se pueden omitir. No transformes crónica anónima en autobiografía de Atanasio, relato infantil en testimonio adulto, ni noticias de 350 en final de guerra en 353. Los relevos de voz son explícitos según edad y acceso al conocimiento. Continúa después con Milán de 355; no es final de campaña ni inicio automático. La investigación 23–29 está recopilada, con alcance leído y errores corregidos, pero todavía no son dossiers ni aprobación de historia o figuras.


Órdenes23–24 corresponden a f00003/S26–S27, pendientes.23 usa tres notas locales distintas, tres salidas financiadas con un único recibo120W30G y dos ayudantes ordinarios que reciben180F y regresan tras su propio recibo de o3/req-4; su lista solo tiene recepción histórica, sin prometer custodia actual.24 requiere cualesquiera seis supervivientes de ocho originales y una nota original; tercer civil perdido derrota. Nunca congeles la primera cohorte de seis ni exijas salida de los ocho. No sustituir con evacuados opcionales. Cuatro guardias fijos por dificultad, extras elegidos para cap16/22/28,20 amigos iniciales sin producción/reemplazo. Control del cruce hasta cierre del refugio, aun tomando alternativa oeste; coste100F60W preparación +240F60W refugio. Siete secundarios por episodio y tres enfoques combinables; reparto y daño real aún necesitan AoE2. Conserva noche13/14Mequir cualificada y hechos posteriores separados, común→Marcus con relatos recibidos, ningún control de huida histórica deAtanasio.

Corrección transversal: recepción registrada nunca demuestra residencia/custodia ni coincidencia física entre mensajero y nota.15/16/18/21/23 lo dicen expresamente.22 necesita presencia actual de sus tres legajos y custodios al cierre, y queda bloqueado por [i00005](../delendai/proposals/ready/infras/i00005-presencia-actual-de-entidades-distinta-del-historial-de-entregas.md) además de sus demás gates. Lee [contrato](../design/live-entity-presence.md): no reemplazar por flag arrived, timer, cambio de propietario, actores inmovilizados o inventario ficticio. La referencia está implementada y revisada según el registro posterior; los observadores nativos siguen pendientes. Las pruebas del diseño solo certifican coherencia de la especificación y rechazo de soporte falso.


Orden25 corresponde a f00003/S28, pendiente. Dos grupos originales de tres ayudantes: recepción occidental o3/req-3→salida o4/req-1→regreso o4/req-2; recepción oriental o3/req-4→salida o4/req-3→regreso o4/req-4. Nunca intercambies recibos ni uses el de una copia. Ambas copias registran entrega, sin custodia actual; índice independiente al archivo sur. Costes120W30G en taller y120F en cada patio. Siete secundarios explícitamente situados y redactados, tres enfoques combinables, sin cambiar el desenlace. La mención de invierno procede de relatos posteriores: no inventar plazo mortal ni sala conciliar certificada. La vista de400×400 aún necesita paisaje denso, orillas y drenajes fechados, navegación y pruebas de ritmo; no rellenar ni alterar esos controles por iniciativa de MiniMax. El paso al quinto acto conserva la continuidad dentro de la campaña.


Órdenes26–27 corresponden a f00003/S29–S30, pendientes.26: seis ayudantes en parejas y tres notas, una por patio; tres asignaciones exactas120F80W20S, total360F240W60S, sin credo puntuable ni objetivo de templo.27: o2/req-1 autoriza solo salida occidental o3/req-1; o2/req-2 solo salida oriental o3/req-3; llegadas o3/req-2/4, a destinos distintos. Ambas notas llegan en o3/req-6/7, antes de o4; o4/req-1 paga100W20G para derivación o4/req-2 y entrega o4/req-3. Total420F340W20G. La cronología es un producto local ficticio basado en contenidos recibidos, no presencia simultánea ni original imperial. Las notas de calendarización y el anuncio de muerte no se convierten en fechas de otro acontecimiento. No autoría nativa hasta cerrar fuentes, terreno, capacidades y calibración;62borradores/2.553pantallas/384secundarios/36referencias adicionales no son aprobación.

La selección de cobertura365–380 está integrada y técnicamente revisada; siguen pendientes tres dossiers nuevos y la calibración de los capítulos cívicos. MiniMax no crea episodios adicionales, inventa combate, modifica tiempos o resuelve esos puntos por su cuenta. La voz común da el marco documental; la voz personal vive escenas ficticias concretas sin recitar instrucciones de implementación. Los nuevos offsets por identidad y los hubs observados son explícitos; nunca ignorar un campo inválido ni recolocar actores sin el gate de terreno.


Presencia actual: i00005/S1 está formalmente done en d793ae4, con correcciones983ef905, reevaluación técnicaGPT6.1 y revisión fresh propia deGPT6Luna. La referencia rechaza identidades no producidas y conserva prioridad de derrota/plazo aunque el lote espacial sea inválido. Pruebas propias de revisión102/389 y export3variantes/2round-trips; gameVerified=false. La ficha deMilán22 enlaza esa procedencia y sigue declarando implementación nativa pendiente. No ejecutar S2/S3 ni autoría histórica por interpretar esa aprobación de referencia como observación enAoE2.


ID28/Tesalónica, ahora orden32, corresponde a f00003/S31: tres contextos llegan en o1; o2/req-1 paga160W40G y respalda las dos derivaciones distintas; o3/req-3 yreq-4 son las recepciones propias de mensajeros que autorizan respectivamente o4/req-1 yreq-3. Sus regresos son o4/req-2 yreq-4. Las cuotas desiguales del sureste/noreste son140F60W y100F60W. Total240F280W40G. No transportar una ley aConstantinopla por rebautizar un patio local.

ID29/Constantinopla, ahora orden34, corresponde a f00003/S32: los tres contextos se reciben en o1; un recibo180W30G financia tres índices en o2. Cada índice y escribiente original tiene un receptor asignado; o3 paga100F40W20S en cada uno. Total300F300W30G60S. Después se elige perspectiva occidental u oriental con claves canónicas acumulativas. Las sucesoras son The Keys of the Eternal City/CDF-C03 y Beyond the Golden Gate/CDF-C04: ambas vuelven a337, tienen narrador propio, recomendación de antecedente y recapitulación sin bloqueo. No voto doctrinal ni cisma moderno en381. CanonIII debe consultarse enCCEL, no en la transcripción incompletaNewAdvent3808; carta382 y transmisión451 no son objetos de381.

La selección actual tiene62dossiers/2.553pantallas/384secundarios/36referencias locales adicionales. El inventario completo de la selección imperial actual no cierra su revisión de cobertura363–380, fuentes, relieve, navegación ni ritmo. El arquitecto resuelve cualquier ampliación y actualiza asignaciones/slices antes de que MiniMax implemente; no generar episodios nuevos por iniciativa mecánica.


La [enmienda de cobertura imperial](../design/imperial-coverage-amendment.md) fija cinco capítulos nuevos para365–380 y una migración atómica a34imperiales/278selecciones implementada, aún sin conceder autoría: preserva IDs, progreso y cinco actos; requiere actualizar conjuntamente contratos, propuestas, narrador, asignaciones y validación antes de activarse.


Enmienda de cobertura vigente: nuevos IDs30/31/32/33/34 se presentan respectivamente en órdenes28/29/30/31/33, mediante S33/S34/S35/S36/S37. Los IDs antiguos28ley/29concilio pasan a órdenes32/34 y conservan S31/S32; promociónS6 sigue dependiendo del últimoS32. Cadena desdeS30: S33→S34→S35→S36→S31→S37→S32. Es una asignación de propuestas bloqueadas, no expedientes ni capacidades acreditadas. El total seleccionado es278, con62dossiers redactados y216pendientes; los39contratos y claves de progreso anteriores permanecen reservados.


Revisión técnica de la migración: [informe independiente](../qa/campaign-design/imperial-coverage-migration-independent-review.md), sobre8a37f763, confirma preservación de IDs/frontmatter/continuidad y reproduce el bypass corregido del scope. Pruebas propias102/389 y57Python; no aprobación global o histórica. Hay ahora34recursos adicionales de investigación: los dos originales deSirmio se conservaron conhash/autor/licencia y límites modernos. El perfil sirmium es un marco regional candidato; no una proclamación localizada ni mapa379aprobado.

Orden28/ID30, *Beyond the Quiet River*, corresponde a f00003/S33 y tiene dossier en revisión. Conserva seis voluntarios originales, cualquier mínimo de cuatro simultáneamente presentes en sus puestos asignados (1–3 noroeste,4–6 sureste), sin fijar la primera cohorte ni exigir residencia continua. Comprobar en o2/req-1 y o3/req-4 mediante presencia actual i00005; la referencia revisada no acredita observador nativo. Lotes1–2 al noroeste y lote3 al sureste. Total380F240W, con reparto160F80W /100F100W y luego120F60W al sureste. Solo o2/req-4 del recadero permite salida o3/req-1 y llegada o3/req-2. Siete secundarios independientes; sus vecinos/cajas no sustituyen originales. El New River y la villa no se localizan ni se cruzan; la carta y el regreso históricos no dependen del jugador. El [gate cívico](../design/civic-playability-acceptance.md) conserva las decisiones de dificultad y ritmo bajo responsabilidad del arquitecto.

Orden29/ID31, *The Empty Chair*, corresponde a f00003/S34 y tiene dossier en revisión. Cada grupo de cuatro hogares necesita tres originales propios: centrales al oeste, nororientales al sureste; perder dos de un grupo derrota aunque queden seis entre ambos. o2 registra recepción; o3/req-2/3 exige presencia actual de ambos mínimos, sin fijar los primeros tres. Los lotes tienen receptor propio. Preparación80F60W por origen; acogida120F40W oeste/180F60W sureste: total460F220W. Catorce escoltas iniciales y8/14/20hostiles seleccionados, sin producción, reposición ni IDs invisibles. No hay cuota de muertes, asalto a prisión o reconquista de iglesias. Los rodeos propuestos necesitan terreno/anchura y sobres completos de adquisición, alcance y leash acreditados; no prometer seguridad a partir de líneasSVG. Siete secundarios independientes, ninguno sustituye hogar ni lote principal. Sócrates371, marco convencional373y días civiles no verificados permanecen separados.

El relieve deEdirne se conserva como referencia moderna de investigación en el manifiesto, con recorte, vista, hashes y avisosCopernicus. No es el mapa aprobado deAdrianópolis378ni prueba su ubicación. El arquitecto decide todavía ese dossier; MiniMax no coloca el campo de batalla desde una traducción de ocho millas o desde un pin moderno.


Orden30/ID32, *Where the Eagles Fell*, corresponde a f00003/S35. Su dossier es diseño en revisión, no permiso de autoría. Originales a pie6mínimo4; exploradores montados4mínimo2: una tercera baja en cualquiera derrota. o1recoge ambos mínimos; o2comprueba presencia simultánea de4a pie al oeste y2montados en el centro; o3reúne ambos mínimos vivos en la acogida suroccidental y cobra180F80Wuna vez. No se congela a los primeros integrantes ni hay permanencia continua o cuota de bajas enemigas. Catorce tropas de apoyo adicionales no sustituyen originales; fuerza militar total18incluidos los cuatro montados, sin producción ni reposición. Hostiles seleccionados8/14/22del máximo22, no IDs invisibles. Roles y representantes nativos siguen sin acreditarse: no simular herida inicial, curación o IA acotada mediante campos ignorados.

Usa el perfil regional separado `adrianople378`, no el cruce fluvial de324. El [relieve comparado](../research/odyssey-research/adrianople378-relief-design.md) fija marco, puntos, rutas y candidato de alturas con límites explícitos. La ciudad queda fuera del mapa al suroeste; no se identifica campo de batalla, círculo de carros, casa deValente o puerta antigua ni se garantiza entrada urbana. Latín hora octava no es radio de ocho millas. La derrota/muerte histórica no cambia. Actor packing, microhidrología, pendientes transitables, observador, envolvente de IA y dificultad real pertenecen al arquitecto/tester y deben cerrarse antes de materializar; MiniMax no los inventa.
