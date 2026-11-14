import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 1 Matrices, determinantes y sistemas"
graf={"tipo":"plano","x":[-3.5,9.33],"y":[-2,5],"a":-1,"b":1.5,"inicio":1,
 "elementos":[
  {"t":"vector","b":["2","1"],"nombre":"a1","c":0},
  {"t":"vector","a":["2","1"],"b":["2+x","1+2*x"],"nombre":"x2 por a2","c":1},
  {"t":"vector","b":["2+x","1+2*x"],"nombre":"Ax","c":2},
  {"t":"vector","b":["1","2"],"nombre":"a2","c":3,"guia":True}],
 "lecturas":[{"rotulo":"primera componente de Ax","formula":"2+x"},{"rotulo":"segunda componente de Ax","formula":"1+2*x"}],
 "etiquetas":["Primera componente","Segunda componente"],"etiquetaSlider":"Valor de x2",
 "alt":"Las columnas a1 igual a (2, 1) y a2 igual a (1, 2) de una matriz, y el vector Ax que se obtiene sumando a1 con x2 veces a2"}
glos={"matriz":"Una matriz es una tabla rectangular de números. Una matriz de m por n tiene m filas y n columnas.",
 "columnas":"Las columnas de una matriz son sus listas verticales de números. Cada una se puede ver como un vector.",
 "traspuesta":"La matriz traspuesta A con T se obtiene cambiando las filas por las columnas de A.",
 "traza":"La traza de una matriz cuadrada es la suma de los números de su diagonal principal."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"La matriz A tiene dos columnas, a1 igual a (2, 1) y a2 igual a (1, 2)."],
 [3,6,"Multiplicar A por el vector (1, x2) es combinar sus columnas, 1 por a1 más x2 por a2."],
 [6,12,"Al cambiar x2, la segunda flecha se alarga o se acorta y el resultado Ax se mueve."],
 [12,17,"Con x2 igual a 1, Ax es (3, 3), la suma de las dos columnas."],
 [17,22,"Con x2 igual a 0, el resultado es solo a1, o sea (2, 1)."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,0],[9,1.5],[11,-0.5],[12,1],[16,1],[17,0],[22,0]],"guide":[[3,0],[4,1]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("Una {{gl:matriz|matriz}} es una tabla de números que representa muchas cosas, como un sistema de ecuaciones, un cambio de coordenadas o una transformación. Lo más importante es entender cómo se multiplican, porque ese producto describe cómo se combinan los efectos.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la matriz A cuyas {{gl:columnas|columnas}} son los vectores a1 igual a (2, 1) y a2 igual a (1, 2). Se multiplica por el vector (1, x2)."),EQ("A\\begin{pmatrix}1\\\\x_{2}\\end{pmatrix}="+M(2,1,1,2)+"\\begin{pmatrix}1\\\\x_{2}\\end{pmatrix}=1\\cdot a_{1}+x_{2}\\cdot a_{2}"),{"t":"grafica","animar":"dibujar","alt":"Las columnas de la matriz y el vector resultado"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Cuando x2 vale 1, el resultado es 1 por a1 más 1 por a2. ¿Cuánto vale su primera componente?","opciones":[2,3,4,5],"correcta":3,"bien":"Muy bien. Es 2 más 1, o sea 3. Más abajo se ve el vector resultado.","mal":"Es 2 más 1, o sea 3, porque a1 aporta 2 y a2 aporta 1. Más abajo se ve el vector resultado."}),
 sec("Combinando columnas","Combinando",P("Mira cómo se mueve el resultado al cambiar x2."),{"t":"acercando","ds":[-0.5,0,1,1.5],"alt":"El vector resultado cuando cambia x2"},P("El producto de una matriz por un vector siempre es una combinación de sus columnas, con los números del vector como pesos.")),
 sec("Tamaños y entradas","Tamaño",P("Una matriz de m por n tiene m filas y n columnas. Su entrada de la fila i y la columna j se escribe a con subíndices i y j."),
   PASOS([("A="+M(2,1,1,2)+"\\ \\text{es de 2 por 2}","Tiene 2 filas y 2 columnas."),
          ("A=\\begin{pmatrix}1&0&3\\\\2&1&0\\end{pmatrix}\\ \\text{es de 2 por 3}","Tiene 2 filas y 3 columnas."),
          ("a_{12}=0","La entrada de la fila 1 y la columna 2 de esta última vale 0.")])),
 sec("Suma y multiplicación por un número","Suma",P("Se suman las matrices del mismo tamaño entrada por entrada, y un número multiplica todas las entradas."),
   PASOS([(M(1,2,3,4)+"+"+M(0,1,1,0)+"="+M(1,3,4,4),"Se suman las entradas que están en la misma posición."),
          ("3"+M(1,2,3,4)+"="+M(3,6,9,12),"El número multiplica cada entrada.")])),
 sec("Producto de matrices","Producto",P("Cada entrada del producto AB es la fila de A por la columna de B, multiplicando y sumando. Para que se pueda, las columnas de A deben ser tantas como las filas de B."),
   PASOS([("A="+M(1,0,2,1)+",\\quad B="+M(3,1,0,2),"Son dos matrices de 2 por 2."),
          ("AB="+M("1\\cdot 3+0\\cdot 0","1\\cdot 1+0\\cdot 2","2\\cdot 3+1\\cdot 0","2\\cdot 1+1\\cdot 2")+"="+M(3,1,6,4),"Cada entrada es fila por columna."),
          ("BA="+M(5,1,4,2),"Al multiplicar en el otro orden sale otra matriz.")]),
   OJO("El producto de matrices no es conmutativo. En general AB y BA son distintos, y a veces uno de los dos ni siquiera se puede hacer.")),
 sec("Traspuesta y traza","Traspuesta",P("La {{gl:traspuesta|traspuesta}} cambia filas por columnas. La {{gl:traza|traza}} suma la diagonal."),
   PASOS([("\\left("+M(3,1,6,4)+"\\right)^{T}="+M(3,6,1,4),"Las filas pasan a ser columnas."),
          ("(AB)^{T}=B^{T}A^{T}","La traspuesta de un producto es el producto de las traspuestas en orden contrario."),
          ("\\operatorname{tr}"+M(4,1,2,6)+"=4+6=10","La traza es la suma de la diagonal principal.")])),
 sec("La inversa de una matriz de 2 por 2","La inversa",P("La inversa de A es la matriz que, multiplicada por A, da la identidad. Para 2 por 2 hay una fórmula."),
   EQ("A="+M("a","b","c","d")+"\\ \\Rightarrow\\ A^{-1}=\\dfrac{1}{ad-bc}"+M("d","-b","-c","a")),
   PASOS([("A="+M(2,1,1,1)+",\\quad ad-bc=2-1=1","El determinante no es cero, así que existe la inversa."),
          ("A^{-1}="+M(1,-1,-1,2),"Se intercambian los de la diagonal y se cambia el signo de los otros dos."),
          ("AA^{-1}="+M(1,0,0,1),"Se comprueba multiplicando.")])),
 eng("Una fuerza en ejes inclinados","En mecánica, a veces se necesita girar una fuerza un ángulo dado. Ese giro se hace con una matriz de rotación, y la fuerza girada es el producto de la matriz por el vector de la fuerza.","F'=R\\,F=\\begin{pmatrix}\\cos\\theta&-\\operatorname{sen}\\theta\\\\ \\operatorname{sen}\\theta&\\cos\\theta\\end{pmatrix}\\begin{pmatrix}100\\\\0\\end{pmatrix}",
   [("Fuerza","100 N sobre el eje x"),("Giro","30 grados"),("Componentes","86.6 N y 50 N")],"El producto da 100 por el coseno de 30 grados y 100 por el seno de 30 grados, o sea 86.6 newtons y 50 newtons. La longitud de la fuerza no cambia, porque una rotación solo gira los vectores. Es un modelo simplificado, porque solo trata fuerzas en el plano."),
 completar("Se calcula la entrada de la fila 2 y la columna 2 del producto AB con A de filas (1, 0) y (2, 1), y B de filas (3, 1) y (0, 2). Se toma la fila 2 de A y la columna 2 de B.","(AB)_{22}=2\\cdot 1+1\\cdot 2=[[hueco]]",
   [("4","cuatro"),("2","dos"),("5","cinco")],0,
   ["","Falta sumar. 2 por 1 es 2 y 1 por 2 es 2, y la suma es 4.","Revisa la cuenta. 2 por 1 es 2 y 1 por 2 es 2, y la suma es 4."],"Multiplica y luego suma los dos productos.","2 por 1 es 2 y 1 por 2 es 2. La suma es 4."),
 error("Alguien comparó AB con BA y se equivocó en un paso. Toca el paso que está mal.",
   [("AB="+M(3,1,6,4),"Es el producto de A por B, y está bien.","A B es 3 1, 6 4"),
    ("\\text{Como el producto de números es conmutativo, }BA=AB","Este paso es el que falla.","Como el producto de números es conmutativo, B A es igual a A B"),
    ("\\text{Por tanto}\\ BA="+M(3,1,6,4),"Depende del paso anterior.","Por tanto B A es 3 1, 6 4")],1,
   "El producto de matrices no es conmutativo. Al calcularlo, BA da la de filas (5, 1) y (4, 2), que es distinta de AB.",
   "BA="+M(5,1,4,2)+"\\ne AB","Calcula BA con la regla de fila por columna y compárala."),
 ordenar("Estos son los pasos para hallar la inversa de A con filas (2, 1) y (1, 1) y comprobarla, pero están desordenados.",
   [("\\det A=2\\cdot 1-1\\cdot 1=1","El determinante es 1"),
    ("A^{-1}=\\dfrac{1}{1}"+M(1,-1,-1,2),"Se aplica la fórmula de la inversa"),
    ("AA^{-1}="+M("2-1","-2+2","1-1","-1+2"),"Se multiplica A por la inversa"),
    ("="+M(1,0,0,1),"Sale la identidad")],[2,0,3,1],
   "Se calcula el determinante, se aplica la fórmula, se multiplica por A y debe salir la identidad.","Primero se necesita el determinante."),
]
S+=cierre("Mini simulacro de matrices",[
 banco("al_c1_01","Es el producto de $A$ por una matriz que intercambia columnas, así que intercambia las columnas de $A$."),
 banco("al_c1_07","La traspuesta de un producto es el producto de las traspuestas en orden contrario."),
 banco("al_c1_08","La traza es la suma de la diagonal, $2+7=9$.")])
prac=[
 {"titulo":"Las columnas","grafica":{"draw":1},"bloques":[P("Estas son las columnas de la matriz y el resultado de multiplicarla por un vector."),EQ("Ax=1\\cdot a_{1}+x_{2}\\cdot a_{2}")]},
 {"titulo":"Cambia x2","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La segunda flecha se estira y el resultado Ax cambia. Abajo se ven sus dos componentes.")]},
 {"titulo":"Suma de columnas","grafica":{"draw":1,"guide":1},"laboratorio":True,"d":1,"bloques":[P("Con x2 igual a 1, el resultado es a1 más a2, o sea (3, 3).")]},
 {"titulo":"Resultado","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0,"bloques":[EQ(M(2,1,1,2)+"\\begin{pmatrix}1\\\\0\\end{pmatrix}=\\begin{pmatrix}2\\\\1\\end{pmatrix}"),P("Con x2 igual a 0 el vector solo toma la primera columna.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Multiplica fila por columna y suma."}]}]
preg={"tex":"\\operatorname{tr}(AB)\\ \\text{con}\\ A="+M(1,2,0,1)+",\\ B="+M(1,0,3,1),"opciones":["$8$","$4$","$10$","$7$"],"correcta":0,
 "explicacion":"El producto AB es la matriz de filas (7, 2) y (3, 1), porque la primera entrada es 1 por 1 más 2 por 3. Su traza es la suma de la diagonal, 7 más 1, o sea 8.",
 "verificacion":{"formula":"((1*1+2*3)+(0*0+1*1))+0*x","a":0,"esperado":8},
 "pistas":["Primero calcula el producto AB con fila por columna.","La primera entrada es 1 por 1 más 2 por 3, y la última es 0 por 0 más 1 por 1.","La traza es la suma de las dos entradas de la diagonal del producto."],
 "errores":["","Se multiplicaron las trazas de A y de B, que son 2 y 2. La traza del producto no es el producto de las trazas.","Revisa el producto. La entrada (1, 1) es 7 y la (2, 2) es 1.","Es solo la primera entrada de la diagonal del producto. Falta sumar la segunda, que es 1."]}
res=["Un producto de matriz por vector es una combinación de las columnas de la matriz.","En el producto AB, cada entrada es una fila de A por una columna de B. No es conmutativo.","La traspuesta de un producto invierte el orden. La traza suma la diagonal. La inversa 2 por 2 usa el determinante."]
write(lesson("alglin-m1-l1","Lección 1 de 4","Matrices y operaciones",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-matrices.json")
