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
La lección de la Regla de la cadena es la lección insignia del aprendizaje guiado. Trae pistas y errores explicados en el quiz, tres actividades (completar, encontrar el error y ordenar), un ejemplo de ingeniería, un mini simulacro con preguntas reales del banco y un repaso espaciado. Las otras 23 lecciones ya tienen pistas y errores explicados en su quiz. Doce más tienen mini simulacro con preguntas reales del banco, hasta completar 13 con la lección insignia. Todas tienen la tarjeta de avance y repaso con insignias. Las respuestas de las 39 preguntas de simulacro se verificaron con cálculo simbólico independiente. Quince lecciones más ya tienen su ejemplo de ingeniería, los de confianza alta, con cifras verificadas con cálculo; en total son 16. `datos/ejemplos-ingenieria-propuestos.md` trae los ocho restantes (confianza media o baja), que siguen sin insertar a la espera de revisión.

Las 24 lecciones están escritas, con los tres modos Ver, Leer y Practicar, y pasan el validador. La estructura de módulos sale del banco y es provisional hasta confirmar el temario oficial.

## Otras materias
Las 10 materias restantes tienen su estructura en `datos/estructuras/`, con los temas del banco sin ordenar de forma pedagógica y todos pendientes. Algunas necesitarán tipos de gráfica nuevos en el motor, por ejemplo vectores, superficies o campos.

## Cómo seguir
1. Elegir un tema pendiente en el archivo de estructura.
2. Copiar una lección parecida de `lecciones/`, cambiar su contenido y validar con `node plantilla/validar.js`.
3. Construir la página con `python3 plantilla/construir.py` y probarla en el navegador, en escritorio y en celular.


## Cálculo Integral
Las 13 lecciones de la estructura provisional `datos/estructuras/calcint.json` están escritas como borradores para revisión, en `lecciones/calcint-*.json`. Cada una se genera con un script `herramientas/mk-<nombre>.py` que usa `herramientas/mklib.py`. Diez traen simulacro con 3 preguntas reales del banco y las otras tres no, porque el banco no tiene 3 preguntas distintas de ese tema. Todas traen un ejemplo de ingeniería con cifras verificadas con cálculo. `herramientas/probar.sh nombre` valida, construye y prueba una lección, y `herramientas/sync.sh` la copia al repositorio. La página de avance sale de `hub/build-hub.py`.

## Álgebra Lineal
Las 12 lecciones de `datos/estructuras/alglin.json` están escritas como borradores para revisión, en `lecciones/alglin-*.json`, con el mismo método de scripts `herramientas/mk-alglin-<nombre>.py`. Usan el tipo de gráfica `plano`, que dibuja vectores, polígonos, rectas y puntos cuyas coordenadas son fórmulas de un parámetro. Diez traen simulacro con 3 preguntas reales del banco y dos no, porque el banco no tiene 3 preguntas distintas de ese tema. `herramientas/mklib.py` trae `banco(id)`, que arma una pregunta del simulacro con el registro del banco en `bank/alglin-todo.json`, y ese archivo se genera con la extracción de `herramientas/extraer-banco.js`.
