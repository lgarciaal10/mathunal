# Plantilla de lección MathUNAL

Una lección es un archivo JSON. El motor la convierte en una página con tres modos de estudio, Ver, Leer y Practicar, que comparten el mismo contenido.

## Cómo se usa
1. Copiar `../lecciones/calculo-limite-1.json` y cambiar su contenido.
2. Validar con `node validar.js ../lecciones/mi-leccion.json --katex ruta/katex.min.js`.
3. Construir con `python3 construir.py ../lecciones/mi-leccion.json salida.html`.

El validador revisa el esquema, que cada ecuación renderice con KaTeX, que las cifras de la gráfica y de la pregunta cuadren con un cálculo numérico, que los capítulos de la animación no dejen huecos y que los textos no lleven dos puntos, punto y coma ni guiones largos ni prometan resultados.

## Qué trae el JSON
- `grafica` define los rangos, la curva, la función con su hueco y el límite.
- `ver` trae los capítulos con subtítulos y los cuadros clave de la animación.
- `leer.secciones` es una lista de bloques de tipo `p`, `eq`, `grafica`, `piensa`, `acercando`, `pasos`, `ojo`, `pregunta` y `resumen`.
- `practicar.pasos` son los pasos del laboratorio con el estado de la gráfica en cada uno.
- `pregunta` es el ejercicio con su verificación numérica.
- `glosario` trae los términos que se subrayan en el texto con `{{gl:clave|texto}}`.

## Lo que todavía no cubre
Esta versión dibuja un solo tipo de gráfica, una función con un hueco y dos puntos que se acercan. Otros temas, como derivadas o integrales, necesitan ampliar el motor con nuevos tipos de gráfica.

Los cuatro temas de color del sitio (Azul, Negro, Gris y Claro) vienen en `base.css` y se guardan en `localStorage` con la misma clave del sitio, `mu-theme`.
