# Crear una campaña

Primero completar el dossier wiki y el brief de diseño, aprobar cronología, perspectivas, civilizaciones y mecánicas. Después añadir campaigns/ID/campaign.json y scenarios/NN-slug/scenario.json, tomando el fixture como referencia estructural y los JSON Schema generados como contrato.

campaign.json contiene metadatos, fuentes/afirmaciones, narradores, introducción/epílogo, locales, recursos y evidencias. scenarioFiles mantiene el orden del contenedor. No contiene código ejecutable; los escenarios se validan en conjunto para cerrar referencias.

Una campaña necesita narrador general y cronista particular distinguibles, intro/outro para cada misión, recapitulación y recomendación estática. Los sucesores consultan claves permanentes, pero deben arrancar aunque no exista su predecesora. No reemplazar hechos por bifurcaciones contrafactuales sin etiquetarlas.

Toda propuesta limita sus archivos a campaigns/ID y docs/wiki/ID, salvo reserva explícita del lock y glosario. Las extensiones del compilador pertenecen a propuestas de infraestructura. Las ramas religiosas o políticas nuevas no requieren rediseñar el pipeline; requieren dossiers y campañas autocontenidas.
