# Metodología de coherencia curricular

**Autora: Cynthia Mercedes Gorozabel Villavicencio.** Investigación aplicada de alcance exploratorio, caso Matemáticas ADM16. [Autoría](AUTORIA.md) · [Condiciones de uso](LICENSE).

Este repositorio permite comprender y aplicar indicadores para analizar lo que la planificación y los registros dicen, no dicen o dicen parcialmente sobre resultados de aprendizaje (RA). **No produce promedios, no cambia ponderaciones y no inventa notas por RA.**

## Empiece aquí

1. [Guía de lectura en cinco minutos](docs/EMPEZAR.md).
2. [La metodología y su aporte](docs/METODOLOGIA.md).
3. [Fichas por dimensión](fichas/README.md).
4. [Resultados documentales del caso](docs/RESULTADOS_CASO.md).
5. [Datos sintéticos y sus límites](datos/README.md).
6. [Ponencia de 10 minutos](ponencia/README.md) y [bibliografía validada](bibliografia/Bibliografia_validada_y_respaldo.md).

Ejemplos legibles: [acta ficticia de 35 personas](ejemplos/ACTA_SINTETICA.md) · [sílabo SIM-S1](ejemplos/SIM-S1.md) · [SIM-S2](ejemplos/SIM-S2.md) · [SIM-S3](ejemplos/SIM-S3.md) · [resultado de la demostración](resultados/DEMO.md).

## Las tres dimensiones

| Dimensión | Pregunta central | Acceso |
|---|---|---|
| Sílabo individual | ¿Coinciden taxonomía, RA, actividades y evidencia prevista? | [Tres indicadores](fichas/01-individual/README.md) |
| Intersyllabus | ¿Qué cambia y qué puede compararse entre versiones? | [Tres indicadores](fichas/02-intersyllabus/README.md) |
| Sílabo-acta | ¿Hasta dónde se puede rastrear cada nota hacia un RA? | [Cuatro indicadores](fichas/03-silabo-acta/README.md) |
| Complemento macro-micro | ¿Los RA de unidad se relacionan con el propósito global? | [Ficha cualitativa](fichas/04-complemento/IND-MACRO-ALIGNMENT.md) |

Cada ficha contiene definición, pregunta, aplicación, evidencia, razonamiento, conclusión y límites. Una lectura fácil precede al detalle técnico. No son indicadores psicométricos ya validados ni acreditaciones institucionales.

## Ejecute la demostración

Requiere Python 3.10 o posterior; solo biblioteca estándar, sin servicios externos.

```sh
python scripts/generar_datos.py
python scripts/analizar_datos.py
python -m unittest discover -s tests -v
```

La generación es reproducible. Produce 35 personas ficticias, tres sílabos de demostración, un acta agregada y un escenario ampliado con 700 registros por criterio. Las calificaciones, personas y firmas son **inventadas desde cero**. No se publican actas reales ni filas reales con nombres cambiados. Los resultados de la demostración nunca se presentan como hallazgos UTM.

## Gobernanza y uso

[Gobernanza](docs/GOBERNANZA.md) · [Procedencia y privacidad](docs/PROCEDENCIA.md) · [Registro de revisión](docs/REVISION.md) · [Trazabilidad de contenidos publicados](docs/INVENTARIO.md).

[Arquitectura y productos del antecedente](docs/ARQUITECTURA_PROPUESTA.md): propuesta de diseño diferenciada de lo efectivamente ejecutado.

Uso permitido exclusivamente no comercial con atribución obligatoria. No vender, cobrar, facturar ni incorporar a servicios comerciales. [Leer condiciones completas](LICENSE). La publicación en GitHub no constituye autorización comercial ni aprobación externa de la metodología.
