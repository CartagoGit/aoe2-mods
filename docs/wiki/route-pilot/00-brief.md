# Brief cerrado del laboratorio de rutas

Documento de infraestructura que prepara la autoría de f00001. S1 revisa y detalla esta especificación; no parte de una campaña en blanco. El objetivo es demostrar dos finales acumulativos sin dependencias obligatorias ni atribuciones históricas.

## Identidad y escenarios

route-pilot: CDF-T01 / CDF_RoutePilot. route-successor: CDF-T02 / CDF_RouteSuccessor. Cada mod contiene un escenario independiente 01-route-choice y 01-recap respectivamente. Fecha y geografía se identifican como laboratorio ficticio; no inventar fuentes históricas. Campaña no destinada al catálogo comercial.

Mapa inicial 32×32, terreno grass-1, sin agua ni elevación; inicio (6,16). Facciones: humano slot1 y adversario slot2, civilización técnica justificada como representación de prueba. Objetivos A y B: castillos en (24,8) y (24,24), sin superponer huellas ni cerrar pasillos. Tropas técnicas humanas: héroe guard/character esencial en (6,16) y dos battering-ram en (8,14)/(8,18). El adversario no reconstruye castillos y no tiene recursos ni economía oculta. El tester comprobará que las unidades/edificios y caminos tienen posiciones válidas en el motor.

Objetivo común prepare de 1s, destruir A o destruir B. victory.objectives=[prepare]; victory.routes ordenada A,B, cada ruta exige su objetivo y escribe progress.route-pilot.route-a o progress.route-pilot.route-b. El terminal común decide una sola victoria por partida; si ambos objetivos se cumplen en el mismo tick, prioridad A según orden de exportación, pendiente de acreditación. Rejugar B nunca elimina A, y viceversa. Derrota: héroe esencial o timeout900s; arbitraje derrota primero. No bloquear objetivos destruidos antes de prepare: la condición de unidad destruida debe persistir.

El sucesor termina mediante temporizador de 10s para comprobar la presentación. Muestra resumen suficiente para un jugador nuevo y recomendaciones opcionales. La condición nativa de recomendación combina ausencia de ambas claves; A, B o ambas permiten recapitulaciones diferenciadas. El arquitecto proporciona una plantilla SequenceItems probada: el autor no inventa un operador lógico del layout.

## Textos y medios

Todos los textos usan campaign.route-pilot.*, scenario.route-pilot-choice.*, campaign.route-successor.* y scenario.route-successor-recap.* para evitar colisiones. General collection-narrator presenta el laboratorio; narrador particular route-observer ficticio explica elecciones y consecuencias. Especificar las dos voces y títulos/objetivos/eventos en es-ES y traducir a los 17 locales registrados con estados reales. Imágenes originales sencillas de mapa/elección con procedencia; grabación/local TTS permitido, sin generación pagada masiva. Los medios completos se empaquetan tras s00001-S3; no distribuir una muestra silenciosa como doblaje terminado.

## QA y entrega

Ejecutar planes tests/compatibility/progression.json y localization.json: perfil nuevo, A, B, ambos órdenes de replay, simultaneidad, guardar antes del final/cargar después, sucesor solo y cambio de idioma. Declarar estimated al diseñar duración; después measured únicamente con evidencia. Exportar ambos mods, registrar hashes, validar sin colisiones y presentar revisión independiente. El cierre de fuentes puede separar las evidencias del motor pendientes; la publicación final exige release:check.
