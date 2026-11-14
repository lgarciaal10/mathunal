import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 2 Espacios vectoriales y transformaciones"
graf={"tipo":"plano","x":[-3.3,6.23],"y":[-2,3.2],"a":-1.5,"b":1.5,"inicio":0.5,
 "elementos":[
  {"t":"poligono","puntos":[["0","0"],["1","0"],["1","1"],["0","1"]],"c":0,"nombre":"cuadrado"},
  {"t":"poligono","puntos":[["0","0"],["1","x"],["1+x","1+x"],["x","1"]],"c":2,"nombre":"imagen"},
  {"t":"vector","b":["1","x"],"nombre":"T(e1)","c":1},
  {"t":"vector","b":["x","1"],"nombre":"T(e2)","c":3}],
 "lecturas":[{"rotulo":"determinante","formula":"1-x*x"},{"rotulo":"área de la imagen","formula":"abs(1-x*x)"}],
 "etiquetas":["Determinante de la matriz","Área de la imagen"],"etiquetaSlider":"Valor de x en la matriz",
 "alt":"El cuadrado de lado 1 y su imagen, un paralelogramo, bajo la transformación cuya matriz tiene unos en la diagonal y x fuera de ella"}
glos={"transformacion":"Una transformación lineal es una función entre espacios de vectores que respeta la suma y la multiplicación por números.",
 "estandar":"La matriz estándar de una transformación tiene como columnas las imágenes de los vectores de la base canónica.",
 "nucleo":"El núcleo de una transformación es el conjunto de vectores que ella manda al cero.",
 "imagen":"La imagen de una transformación es el conjunto de todos los resultados posibles."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"Esta es la transformación cuya matriz tiene unos en la diagonal y x en las otras dos entradas."],
 [3,6,"El cuadrado de lado 1 se transforma en un paralelogramo. Sus lados son las columnas de la matriz."],
 [6,12,"Al cambiar x, el paralelogramo se inclina. Su área cambia con el determinante, 1 menos x al cuadrado."],
 [12,17,"Con x igual a 1, el paralelogramo se aplasta sobre una recta y su área es 0. La transformación pierde una dimensión."],
 [17,22,"Con x igual a 0.5, el área es 0.75. La matriz multiplica áreas por 0.75."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,0.5],[9,-0.6],[11,0.3],[12,1],[16,1],[17,0.5],[22,0.5]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("Una {{gl:transformacion|transformación lineal}} es una función que respeta las sumas y los múltiplos. Toda transformación lineal del plano está dada por una matriz, y esa matriz tiene una lectura geométrica clara, a dónde van los vectores de la base. Con ella se explican giros, estiramientos, cortes y proyecciones.")),
 sec("Un ejemplo","Un ejemplo",P("Mira lo que le hace una matriz al cuadrado de lado 1. El cuadrado tiene lados e1 igual a (1, 0) y e2 igual a (0, 1)."),EQ("A="+M(1,"x","x",1)),{"t":"grafica","animar":"dibujar","alt":"El cuadrado y su imagen"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La imagen de e1 es la primera columna de la matriz, o sea (1, x). Con x igual a 0, ¿cuánto vale su segunda componente?","opciones":[0,0.5,1,2],"correcta":0,"bien":"Muy bien. Vale 0, y la transformación es la identidad. Más abajo se ve cómo cambia al subir x.","mal":"Vale 0, porque la segunda componente es x. Con x igual a 0 la transformación es la identidad. Más abajo se ve cómo cambia."}),
 sec("El cuadrado y su imagen","La imagen",P("Mira cómo cambia el paralelogramo al variar x."),{"t":"acercando","ds":[-0.6,0,0.5,1],"alt":"El cuadrado y su imagen para varios valores de x"},P("Cuando el paralelogramo se aplasta, la transformación pierde una dimensión. El determinante de la matriz mide cuánto cambian las áreas.")),
 sec("Qué es lineal","Lineal",P("Una función T es lineal si respeta las dos operaciones del espacio."),
   PASOS([("T(u+v)=T(u)+T(v)","Aditividad. Transformar una suma es sumar las transformaciones."),
          ("T(cu)=c\\,T(u)","Homogeneidad. Un múltiplo sale de la transformación."),
          ("T(\\mathbf{0})=\\mathbf{0}","Consecuencia. Toda transformación lineal manda el cero al cero.")]),
   OJO("Una función como T(x, y) igual a (x más 1, y) no es lineal, porque manda el cero al (1, 0).")),
 sec("La matriz estándar","La matriz",P("Una transformación lineal queda determinada por lo que hace con e1 y e2. Esas imágenes son las columnas de su {{gl:estandar|matriz estándar}}."),
   PASOS([("T(x,y)=(x+2y,\\ 3x)","Una transformación dada por fórmulas."),
          ("T(1,0)=(1,3),\\quad T(0,1)=(2,0)","Se evalúa en los vectores de la base."),
          ("A="+M(1,2,3,0),"Esas imágenes son las columnas."),
          ("T(\\mathbf{v})=A\\mathbf{v}","Aplicar T es multiplicar por A.")])),
 sec("Giros y composición","Giros",P("La transformación que gira 90 grados el plano manda e1 a (0, 1) y e2 a (menos 1, 0)."),
   PASOS([("R="+M(0,-1,1,0),"Es la matriz de un giro de 90 grados."),
          ("R\\begin{pmatrix}2\\\\1\\end{pmatrix}=\\begin{pmatrix}-1\\\\2\\end{pmatrix}","El vector (2, 1) pasa a (menos 1, 2)."),
          ("T_{2}\\circ T_{1}\\ \\text{tiene matriz}\\ A_{2}A_{1}","Hacer una transformación y luego otra se escribe como el producto de las matrices, en ese orden.")])),
 sec("Núcleo, imagen y determinante","Núcleo e imagen",P("Dos conjuntos describen una transformación. El {{gl:nucleo|núcleo}} reúne lo que se aplasta a cero y la {{gl:imagen|imagen}} reúne lo que se puede alcanzar. El determinante dice por cuánto se multiplican las áreas."),
   PASOS([("\\operatorname{Nu}(T)=\\{v:\\ T(v)=0\\}","El núcleo es el espacio nulo de la matriz."),
          ("\\operatorname{Im}(T)=\\text{espacio columna de}\\ A","La imagen es el espacio columna."),
          ("\\det A\\ne 0\\ \\Rightarrow\\ \\text{núcleo}=\\{0\\},\\ \\text{imagen}=\\mathbb{R}^{2}","Si no se aplasta nada, se puede volver atrás.")])),
 eng("La deformación de una lámina","Cuando una lámina de metal se estira y se corta, cada punto se mueve con una transformación casi lineal, llamada gradiente de deformación. Su determinante dice cuánto cambió el área de la lámina.","F="+M(1.1,0.05,0,0.95),
   [("Estiramiento en x","10 %"),("Compresión en y","5 %"),("Cambio de área","4.5 %")],"El determinante vale 1.1 por 0.95 menos 0.05 por 0, o sea 1.045. El área aumenta un 4.5 por ciento, aunque la lámina se comprimió en una dirección. Es un modelo simplificado, porque supone una deformación uniforme en toda la lámina."),
 completar("Se halla la matriz estándar de T(x, y) igual a (x más 2y, 3x). Falta la imagen de e1 igual a (1, 0).","T(1,0)=[[hueco]]",
   [("(1,3)","uno, tres"),("(2,0)","dos, cero"),("(3,1)","tres, uno")],0,
   ["","Ese vector es T(0, 1), la imagen de e2. Para e1 se reemplaza x por 1 y y por 0.","Las componentes están invertidas. Con x igual a 1 y y igual a 0, queda (1 más 0, 3 por 1)."],"Reemplaza x por 1 y y por 0.","Con x igual a 1 y y igual a 0, la primera componente es 1 y la segunda es 3, o sea (1, 3)."),
 error("Alguien decidió si una función es lineal y se equivocó en un paso. Toca el paso que está mal.",
   [("T(x,y)=(x+1,\\ y)","Es la función.","T de x, y es x más 1, y"),
    ("\\text{Es una suma de x con un número, así que es lineal}","Este paso es el que falla.","Es una suma de x con un número, así que es lineal"),
    ("\\text{Por tanto tiene matriz estándar}","Depende del paso anterior.","Por tanto tiene matriz estándar")],1,
   "Una transformación lineal debe mandar el cero al cero, y aquí T de (0, 0) es (1, 0). Por eso no es lineal y no tiene matriz.",
   "T(0,0)=(1,0)\\ne(0,0)","Evalúa T en el vector cero."),
 ordenar("Estos son los pasos para hallar la matriz del giro de 90 grados, pero están desordenados.",
   [("T\\ \\text{gira el plano 90 grados}","La transformación"),
    ("T(e_{1})=(0,1)","Gira e1 y queda en el eje y"),
    ("T(e_{2})=(-1,0)","Gira e2 y queda en el lado negativo del eje x"),
    ("A="+M(0,-1,1,0),"Las imágenes son las columnas")],[2,0,3,1],
   "Se define el giro, se halla la imagen de cada vector de la base y se arman las columnas.","Se empieza con la descripción de la transformación."),
]
S+=cierre("Mini simulacro de transformaciones lineales",[
 banco("al_c2_13","Es la definición de transformación lineal."),
 banco("al_c2_14","La matriz estándar es $\\begin{pmatrix}2&0\\\\1&1\\end{pmatrix}$ y su determinante es $2$."),
 banco("al_c2_15","Toda transformación lineal manda el cero al cero, porque $T(0)=T(0\\cdot 0)=0\\,T(0)=0$.")])
prac=[
 {"titulo":"El cuadrado","grafica":{"draw":1},"bloques":[P("El cuadrado de lado 1 y su imagen bajo la matriz."),EQ("A="+M(1,"x","x",1))]},
 {"titulo":"Cambia x","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El paralelogramo se inclina y abajo se ven el determinante y el área de la imagen.")]},
 {"titulo":"Se aplasta","grafica":{"draw":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("x=1\\ \\Rightarrow\\ \\det A=1-1=0"),P("Con x igual a 1 las dos columnas son iguales y el paralelogramo se aplasta sobre una recta.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Arma la matriz con las imágenes de e1 y e2 y calcula su determinante."}]}]
preg={"tex":"T(x,y)=(3x-y,\\ x+2y)\\ \\text{multiplica las áreas por}","opciones":["$7$","$5$","$6$","$-7$"],"correcta":0,
 "explicacion":"La matriz estándar tiene columnas T(1, 0) igual a (3, 1) y T(0, 1) igual a (menos 1, 2). Su determinante es 3 por 2 menos menos 1 por 1, o sea 7. Las áreas se multiplican por 7.",
 "verificacion":{"formula":"3*2-(0-1)*1+0*x","a":0,"esperado":7},
 "pistas":["Halla la matriz estándar con las imágenes de e1 y e2.","Las columnas son (3, 1) y (menos 1, 2).","El factor de las áreas es el determinante, 3 por 2 menos menos 1 por 1."],
 "errores":["","Se olvidó el signo del segundo término. Menos 1 por 1 se resta, así que se suma 1.","Revisa la cuenta. 3 por 2 es 6, y se suma 1 porque el otro producto es negativo.","El factor de área usa el valor absoluto del determinante, y aquí el determinante es positivo, 7."]}
res=["Una transformación es lineal si respeta sumas y múltiplos. Manda el cero al cero.","Su matriz estándar tiene como columnas las imágenes de los vectores de la base.","El determinante dice por cuánto se multiplican las áreas, y si es cero se pierde una dimensión."]
write(lesson("alglin-m2-l4","Lección 4 de 4","Transformaciones lineales",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-transformaciones.json")
