# Datos: qué es real y qué es sintético

| Carpeta | Contenido | Uso permitido en el razonamiento |
|---|---|---|
| contexto/ | Extractos curriculares por unidad y comprobaciones documentales del caso sin filas estudiantiles | Fundamentar hallazgos de planificación; originales completos reservados |
| sinteticos/ | Personas, notas y firmas ficticias generadas desde cero | Aprender el formato y contrastar agregación frente a vínculos explícitos |

## Alineación con la estructura real

Se conservan 35 registros; ND, NP, NTA y NE; máximos por ciclo 15, 10, 10 y 15; suma NF del segundo ciclo; TOT como acumulado de ambos ciclos hasta 100; asistencia sobre 100 con dos null. Los valores individuales y nombres se crean sin leer el acta. No se replican distribuciones de notas ni estados de acreditación reales.

El escenario agregado no incluye RA o criterio. El ampliado contiene 700 filas: 35 personas × 5 RA × 4 criterios por componente. Cada fila tiene actividad, criterio, unidad, RA, ciclo, puntuación y máximo. La asignación por unidad fue inventada y se declara en PLAN dentro de scripts/generar_datos.py; no se deduce del sílabo ni de horas de enseñanza. No existe un umbral de logro ni un dictamen de aprobación.

## Diccionario

| Campo | Significado |
|---|---|
| ND | Nota Docencia, componente del segundo ciclo |
| NP | Nota Práctica, componente del segundo ciclo |
| NTA | Nota Trabajo Autónomo, componente del segundo ciclo |
| NE | Nota Examen, componente del segundo ciclo |
| NF | Suma de los cuatro componentes del segundo ciclo |
| TOT | Suma de puntos del primer y segundo ciclo |
| asistencia | Valor entre 0 y 100 o null; no se suma a NF |
| observacion | SIN_DICTAMEN_SIMULADO; no se inventa regla institucional |
| criterio_id | Identificador ficticio de criterio; no una rúbrica validada |
| tipo | Etiqueta obligatoria que identifica el carácter sintético |

Firmas: rótulos ficticios sin validez. Véase [procedencia](../docs/PROCEDENCIA.md). Los archivos no permiten identificar personas reales ni representan logros empíricos.
