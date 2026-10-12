# Contexto permanente del proyecto

Crónicas de la Fe es una fábrica de mods de campañas históricas para AoE2 DE. La conversación final descartó un gestor externo y bloqueos entre campañas: cada campaña debe jugarse por sí sola, con recomendación opcional, recapitulación y progreso acumulativo por rutas. No hay que construir una aplicación Angular ni un launcher.

## Contratos y componentes

Fuentes JSON schemaVersion 1; campaña en campaigns/<id>/campaign.json y escenarios en scenarios/NN-<slug>/scenario.json referenciados por scenarioFiles. Los módulos packages/schemas, localization, historical-validation, gameplay-validation, scenario-compiler, campaign-compiler, assets, audio y aoe2-adapter son la infraestructura. CLI en tools/cli; parser Python y empaquetador externo fijados en tools/python. El diagrama y responsabilidades están en arquitectura.

Los nombres internos CDF_<Name>, publicId CDF-CNN y claves de progreso son permanentes. Las traducciones usan namespaces semánticos compilados mediante config/string-ids.lock.json. El español de España es canónico; hay 17 locales objetivo. El fixture tiene dos muestras draft, no traducciones terminadas. Las carpetas lingüísticas y el rango reservado todavía requieren verificación en el motor.

La colección tiene narrador general estable. Cada campaña añade narrador particular distinto, ficticio cuando corresponda, consistente en introducción, misión y epílogo. Personajes pueden intervenir con voz diferenciada; no imitar a personas reales ni convertir dramatización en fuente. Los contratos incluyen interpretación, idioma/acento, licencia y revisión.

## Capacidades comprobadas y límites

Se generan escenarios 1.59 con AoE2ScenarioParser 0.9.6, unidades/terrenos/tecnologías del catálogo, objetivos, derrota, variables, eventos finitos, reservas y progreso Store Key. Se comprueba reapertura y contenedor. El DSL cubre condiciones timer/destroy/variable/objective/bring/resource y efectos set-variable/line/task/spawn/diplomacy/tribute. La IA económica necesita PER explícito. Los mapas ofrecen terreno base, teselas y elevación; la conectividad es una cuadrícula abstracta, no pathfinding real del motor.

Las envolturas nativas de slideshow/layout se reciben como plantillas acreditadas por el arquitecto/tester; el adaptador resuelve tokens sin inventar sus formatos. La continuidad entre mods, rutas de voz, slots de idioma, guardados, dificultad XS y Return of Rome requieren pruebas específicas. Return of Rome se rechaza expresamente al exportar mientras no exista un perfil probado. Consulta capabilities y la matriz de compatibilidad; ninguna bandera experimental es evidencia.

## Historia y prioridades

El dossier inicial imperial-church documenta la planificación 312–337: Puente Milvio, Nicea y nueva capital. No existe campaña histórica implementada. Las tradiciones sobre Constantino se distinguen de hechos; 325 no representa una división instantánea entre iglesias contemporáneas. Los títulos, geografía, tácticas y representación de civilizaciones se cierran con fuentes antes de autoría.

Primero se valida el laboratorio de rutas; después una misión histórica narrativa; después la campaña de ejemplo. M3.1 solo realiza contenido designado. Los cambios de motor/infraestructura, revisión independiente y pruebas en AoE2 tienen responsables distintos. La fábrica no presupone una tradición religiosa concreta.
