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
- **Área entre curvas** (`"tipo": "entre"`). Como el área, pero con dos curvas. Lleva `funcion` (la de arriba), `inferior` (la de abajo), `primitiva` de la resta, y `a` y `b`, que son los cortes. El estado `d` es el x del límite superior y las lecturas son el área acumulada y la separación entre curvas. El validador revisa que las curvas se corten en `a` y `b`, que la de arriba quede arriba y que la primitiva derive en la resta.
- **Asíntota** (`"tipo": "asintota"`). Un punto que recorre la curva con las asíntotas dibujadas. Lleva `funcion`, `asintotas` (cada una con `x` o `y` y una `etiqueta`) y `deslizador` con `ancla`, `dmin` y `dmax`, que fija el recorrido del deslizador en escala logarítmica. Con `"expandir": true` la ventana se agranda para que quepan valores grandes de x.

Las fórmulas aceptan números, `x`, `+ - * / ^`, paréntesis y las funciones `sin cos tan exp ln sqrt abs` y la constante `pi`.

## Zoom
Con `"zoom": {"factor": N}` en `grafica`, el motor acepta el estado `zoom` de 0 a 1. La ventana se acerca N veces al punto de interés, las marcas pasan a decimales y aparece el rótulo Zoom. Reglas prácticas para elegir N.
- En un hueco conviene un ancho final de unos 0.004, o sea N igual al ancho del eje x dividido entre 0.004.
- En una secante conviene un ancho final de unos 0.08.

`agregar-zoom.py` agrega un capítulo de 4 segundos en Ver, una frase en Leer y el paso Mira de cerca en Practicar. En Leer, el bloque `acercando` hace el zoom solo al terminar, y se puede apagar con `"zoom": false` en el bloque. En Ver se controla con el canal `zoom` y en Practicar con `"zoom": 1` en el estado del paso.

## Aprendizaje guiado
Estos componentes sirven para que el estudiante no reciba la respuesta de entrada.

**Quiz con pistas y errores explicados.** En `pregunta` se agregan dos campos.
- `pistas` es una lista de 1 a 4 textos. El estudiante los pide de a uno, y cada respuesta errada revela la siguiente sola.
- `errores` trae un texto por opción, y el de la opción correcta va vacío. Cada texto explica qué error produce ese resultado. Donde no se esté seguro de la causa, conviene escribir "Revisa la cuenta" con el cálculo correcto, en vez de inventar un motivo.

Con alguno de los dos campos el quiz deja reintentar, y después de dos fallos ofrece mostrar la respuesta. Sin ellos se comporta como antes.

**Bloques nuevos** para `leer.secciones` y `practicar.pasos`.
- `completar`. Una ecuación con `[[hueco]]` y opciones `{"tex": "..."}`. Lleva `correcta`, `errores` (uno por opción), `pista` y `porque`.
- `error`. Una solución en `pasos` con un paso equivocado, indicado por `mal`. Lleva `correccion`, `explicacion` y `pista`. Cada paso puede traer `porque`, que se muestra si el estudiante lo toca por equivocación.
- `ordenar`. Los `pasos` van en el orden correcto y `mezcla` es la permutación con que se muestran, que no puede dejarlos ya en orden. El estudiante los toca en secuencia.
- `simulacro`. Una lista de `preguntas` del banco, cada una con `fuente`. Puede ser de opción múltiple (`opciones` y `correcta`) o numérica (`respuesta` y `tolNum`). El texto admite matemática en línea entre signos de dólar.
- `ingenieria`. Una tarjeta "¿Para qué sirve?" con `titulo`, `html`, `tex` opcional, `datos` (pares `k` y `v`) y `cierre`.
- `repaso`. La tarjeta que muestra cuándo volver a la lección.

## Insignias y avance
La tarjeta `repaso` también muestra qué modos de estudio usó la persona y cuatro insignias, que se guardan en `localStorage` con la clave `mu-progreso`.
- Lo viste todo, por haber usado Ver, Leer y Practicar.
- Sin pistas, por acertar el quiz al primer intento y sin pistas.
- Simulacro perfecto, por acertar las 3 preguntas. Solo aparece en lecciones que tienen simulacro.
- Repasaste a tiempo, por responder el quiz o el simulacro el día que la lección estaba vencida.

No hay rachas, puntos ni tablas de posiciones. Las insignias describen cómo se estudió y no empujan a entrar todos los días.

## Repaso espaciado
El motor guarda en `localStorage`, con la clave `mu-repaso`, el resultado de cada quiz y simulacro. Si el resultado es bueno, el próximo repaso se aleja a 1, 3, 7, 14 y 30 días. Si falla, vuelve a 1 día. Cuando una lección vence, aparece un aviso arriba. `window.MU.repaso.pendientes()` devuelve las lecciones vencidas, para que el sitio arme una vista de repaso con todas. Como `localStorage` es por origen, ese listado completo solo funciona con todas las lecciones bajo el mismo dominio.

Los validadores revisan que `errores` tenga un texto por opción, que `mezcla` sea una permutación, que cada pregunta del simulacro traiga su fuente y que todas las ecuaciones rendericen.

## Lo que todavía no cubre
Más de dos curvas, curvas cerradas completas, superficies y vectores, que se necesitarán para varias variables, álgebra lineal y ecuaciones diferenciales.

Los cuatro temas de color del sitio (Azul, Negro, Gris y Claro) vienen en `base.css` y se guardan en `localStorage` con la misma clave del sitio, `mu-theme`.
