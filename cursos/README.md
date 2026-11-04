# Cursos de MathUNAL

Esta carpeta guarda el trabajo de los cursos. Todo es un borrador para revisar y no está conectado al sitio.

## Qué hay
- `plantilla/` trae el motor de lecciones, el validador, el constructor y el script de zoom. El README de esa carpeta explica cómo escribir una lección.
- `lecciones/` trae cada lección como un archivo JSON.
- `mockups/` trae cada lección ya construida como una página HTML de un solo archivo, y los mockups de la portada y de la lista de temas.
- `datos/` trae el mapa de temas del banco y la estructura de cada curso. `calculo-diferencial-estructura.json` dice qué lección corresponde a cada tema.
- `video/` trae el proyecto de Remotion con el video de la regla de la cadena.
- `herramientas/` trae los scripts que sacan los datos del banco de preguntas.

## Estado de Cálculo Diferencial
La lección de la Regla de la cadena es la lección insignia del aprendizaje guiado. Trae pistas y errores explicados en el quiz, tres actividades (completar, encontrar el error y ordenar), un ejemplo de ingeniería, un mini simulacro con preguntas reales del banco y un repaso espaciado. Las otras 23 lecciones ya tienen pistas y errores explicados en su quiz. Doce más tienen mini simulacro con preguntas reales del banco, hasta completar 13 con la lección insignia. Todas tienen la tarjeta de avance y repaso con insignias. Las respuestas de las 36 preguntas de simulacro se verificaron con cálculo simbólico independiente. `datos/ejemplos-ingenieria-propuestos.md` trae los ejemplos de ingeniería propuestos para las otras 23 lecciones, pendientes de revisión.

Las 24 lecciones están escritas, con los tres modos Ver, Leer y Practicar, y pasan el validador. La estructura de módulos sale del banco y es provisional hasta confirmar el temario oficial.

## Otras materias
Las 10 materias restantes tienen su estructura en `datos/estructuras/`, con los temas del banco sin ordenar de forma pedagógica y todos pendientes. Algunas necesitarán tipos de gráfica nuevos en el motor, por ejemplo vectores, superficies o campos.

## Cómo seguir
1. Elegir un tema pendiente en el archivo de estructura.
2. Copiar una lección parecida de `lecciones/`, cambiar su contenido y validar con `node plantilla/validar.js`.
3. Construir la página con `python3 plantilla/construir.py` y probarla en el navegador, en escritorio y en celular.
