# Revisión geométrica independiente del plan candidato Jerusalén

Revisor gpt-6.1-terra · 2026-11-05. Resultado: no se identificó una discrepancia material en la geometría comprobada. No autoriza el plan ni revisa o ejecuta la futura implementación S2. Es una comprobación de un borrador de desarrollo, sin aprobación histórica, de colisión, navegación, balance ni juego.

Se ejecutó de nuevo el extractor TIFF, la verificación de 495.187 muestras, el compilador bilineal y el cuantizador del repositorio. La extracción y verificación usan el mismo extractor: no constituyen dos decodificadores independientes. El informe anterior con LibTIFF es evidencia separada; no se repitió aquí. TIFF PixelIsPoint y EPSG:4326 se leyeron del archivo, y el datum vertical declarado procede de documentación del producto, no de una comprobación independiente. Es un DSM moderno con construcciones y vegetación, no terreno desnudo antiguo.

Los SHA-256 fijados en plan coinciden: binding `55d1c27acc7e55c5caeb070c016d1d364a3b6b5a5255a6797b3471101863f713`, campaña `0db4c1c70be830847a73d577922e619e8b1c22cd9faf08f2fa5aac44ee5c1d5a`, TIFF `49c2c666dee43187bb5438fc989ce84fc1807c8cafeb65c09293786e18729276`. Plan `66cb1293c47e795b7b0eeaf5b60b3c236284aa20c21190bc6d4e65c1226f5a2f`; comparación de rutas 18 `6ed1ec13faf7f2d3d2fa525b310da615457ea700dd3f685a42f90beb3b894da8`. El plan no fija el hash del archivo 18: esta revisión contrasta sus puntos y conserva su hash observado, no presenta ese archivo como entrada verificada por hash del futuro builder.

Marco de 340×340, bbox [35.12,31.70,35.30,31.86]: 115.600 muestras, ninguna ausente, rango 208.161999–966.471753 m y niveles 0–7 con histograma 482/4112/11012/19951/27073/42326/10073/571. Se confirmó que los puntos de ambos corredores coinciden con la fuente 18 y la proyección existente, que entrega dos decimales; el cálculo de segmentos empleó esos puntos continuos authored sin redondeo adicional a casillas.

| Corredor | Ancho | Radio conservador | Celdas | Bounds x/y inclusivos | Fuera/nodata | Saltos entre vecinos |
|---|---:|---:|---:|---|---:|---|
| main | 10 | 5.70710678 | 1225 | [177,143]–[206,242] | 0/0 | 2166 de 0, 148 de 1, ninguno ≥2 |
| relief | 6 | 3.70710678 | 1014 | [161,145]–[204,240] | 0/0 | 1771 de 0, 83 de 1, ninguno ≥2 |

La envolvente usa distancia del centro nativo [x+0.5,y+0.5] al segmento, `width/2 + sqrt(0.5)`, incluidos extremos. Es una sobreaproximación de las casillas que pueden tocar la cápsula; no es rasterización poligonal exacta ni prueba de transitabilidad. La lista de agua conocida vacía significa cobertura desconocida, no prueba de suelo seco. Los saltos de un nivel, obstáculos, cruces, edificios, colisiones y comportamiento de unidades requieren evaluación nativa y juego.

Binding: 17 IDs de entidades y 10 zonas únicos. Tras aplicar únicamente el traslado propuesto del mismo almacén de [200.05,189.88] a [200.05,186.88], sus centros nativos pasan [200.5,189.5]→[200.5,186.5]. El centro queda a 11.3889 del hub de radio 12; las holguras adicionales mínimas son 3.3889 respecto de exclusión de receptores y 26.4631 respecto de otros cuerpos. Su envolvente conservadora radio 3+sqrt(0.5) abarca 45 celdas, todas de nivel 5. Los 17 centros y 10 zonas quedan dentro del marco; la separación mínima entre centros de cuerpos es 4 casillas. El radio 3 es una suposición geométrica, no una huella medida del motor.

Plan mantiene `privateBuildAuthorized=false`, `historicalApproval=false` y `gameVerified=false`. El script y JSON adjuntos son evidencia de esta revisión, no del futuro auditor S2. SHA-256: `audit.py` 5d51b32f4f8d4abaeb349cf951f2cf173aa452bafdecb2394d49bd9d079e7e51; `independent-geometry.json` d4d645feb3aa8aa39ef6dfb1df35bcce945f0c5d75d0dcaf78e3e0512050e14b. No se modificó el repositorio ni se ejecutaron gates pesados.
