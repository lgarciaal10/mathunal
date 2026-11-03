# Plantilla de lección MathUNAL

Una lección es un archivo JSON. El motor la convierte en una página con tres modos de estudio, Ver, Leer y Practicar, que comparten el mismo contenido.

## Cómo se usa
1. Copiar `../lecciones/calculo-limite-1.json` (gráfica de hueco) o `../lecciones/calculo-derivada-1.json` (gráfica de secante) y cambiar su contenido.
2. Validar con `node validar.js ../lecciones/mi-leccion.json --katex ruta/katex.min.js`.
3. Construir con `python3 construir.py ../lecciones/mi-leccion.json salida.html`.
4. Opcional, agregar zoom con `python3 agregar-zoom.py ../lecciones/mi-leccion.json FACTOR`.

El validador revisa el esquema, que cada ecuación renderice con KaTeX, que las cifras de la gráfica y de la pregunta cuadren con un cálculo numérico, que los capítulos de la animación no dejen huecos y que los textos no lleven dos puntos, punto y coma ni guiones largos ni prometan resultados.

## Qué trae el JSON
- `grafica` define los rangos, la curva y el tipo de gráfica (ver abajo).
- `ver` trae los capítulos con subtítulos y los cuadros clave de la animación.
- `leer.secciones` es una lista de bloques de tipo `p`, `eq`, `grafica`, `piensa`, `acercando`, `pasos`, `ojo`, `pregunta` y `resumen`.
- `practicar.pasos` son los pasos del laboratorio con el estado de la gráfica en cada uno.
- `pregunta` es el ejercicio con su verificación numérica.
- `glosario` trae los términos que se subrayan en el texto con `{{gl:clave|texto}}`.

## Tipos de gráfica
- **Hueco** (por defecto). Una función con un hueco y dos puntos que se acercan por los lados. Lleva `curva`, `funcion`, `hueco` y `limite`. Con `punto` se agrega el valor f(a) como un punto aparte, y con el estado `fix` ese punto sube hasta el límite.
- **Secante** (`"tipo": "secante"`). Una secante que se vuelve tangente. Lleva `funcion`, `a`, `derivada` y `limite`, que es la pendiente de la tangente. Con `"normal": true` dibuja también la recta normal, y con `rotulos` cambia los nombres de las lecturas, por ejemplo `["h", "velocidad media"]`. Para que la normal se vea perpendicular, los rangos x e y tienen que dar la misma escala (550 por 300 píxeles).

- **Teorema del valor medio** (`"tipo": "tvm"`). Una cuerda fija entre `a` y `b` y una tangente que recorre la curva. Lleva `funcion`, `a`, `b`, `derivada`, `c` (el punto del teorema) y `limite`, que es la pendiente de la cuerda. El estado `d` es el x del punto móvil y el deslizador de Practicar recorre el intervalo.

- **Newton** (`"tipo": "newton"`). Tangentes sucesivas que cortan el eje x. Lleva `funcion`, `derivada`, `x0`, `pasos` y `raiz`. El estado `d` es el número de tangentes dibujadas y puede llevar decimales para animar. El deslizador de Practicar recorre las iteraciones.
- **Área** (`"tipo": "area"`). El área bajo la curva desde `a` hasta un x que se mueve, con una franja delgada en el borde. Lleva `funcion`, `primitiva`, `a`, `b` y `franja`. El estado `d` es el x del límite superior y `guide` muestra la franja.
- **Asíntota** (`"tipo": "asintota"`). Un punto que recorre la curva con las asíntotas dibujadas. Lleva `funcion`, `asintotas` (cada una con `x` o `y` y una `etiqueta`) y `deslizador` con `ancla`, `dmin` y `dmax`, que fija el recorrido del deslizador en escala logarítmica. Con `"expandir": true` la ventana se agranda para que quepan valores grandes de x.

Las fórmulas aceptan números, `x`, `+ - * / ^`, paréntesis y las funciones `sin cos tan exp ln sqrt abs` y la constante `pi`.

## Zoom
Con `"zoom": {"factor": N}` en `grafica`, el motor acepta el estado `zoom` de 0 a 1. La ventana se acerca N veces al punto de interés, las marcas pasan a decimales y aparece el rótulo Zoom. Reglas prácticas para elegir N.
- En un hueco conviene un ancho final de unos 0.004, o sea N igual al ancho del eje x dividido entre 0.004.
- En una secante conviene un ancho final de unos 0.08.

`agregar-zoom.py` agrega un capítulo de 4 segundos en Ver, una frase en Leer y el paso Mira de cerca en Practicar. En Leer, el bloque `acercando` hace el zoom solo al terminar, y se puede apagar con `"zoom": false` en el bloque. En Ver se controla con el canal `zoom` y en Practicar con `"zoom": 1` en el estado del paso.

## Lo que todavía no cubre
Gráficas con más de una curva, curvas cerradas completas, superficies y vectores, que se necesitarán para varias variables, álgebra lineal y ecuaciones diferenciales.

Los cuatro temas de color del sitio (Azul, Negro, Gris y Claro) vienen en `base.css` y se guardan en `localStorage` con la misma clave del sitio, `mu-theme`.
