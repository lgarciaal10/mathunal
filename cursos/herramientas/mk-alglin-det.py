import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 1 Matrices, determinantes y sistemas"
def M(*c):
    n=int(len(c)**0.5+0.5); rows=[c[i*n:(i+1)*n] for i in range(n)]
    return "\\begin{pmatrix}"+"\\\\".join("&".join(str(v) for v in r) for r in rows)+"\\end{pmatrix}"
graf={"tipo":"plano","x":[-2.8,6.73],"y":[-1.5,3.7],"a":-1,"b":2.5,"inicio":2,
 "elementos":[
  {"t":"vector","b":["2","1"],"nombre":"u","c":0},
  {"t":"vector","b":["1","x"],"nombre":"v","c":1},
  {"t":"poligono","puntos":[["0","0"],["2","1"],["3","1+x"],["1","x"]],"c":2},
  {"t":"recta","p":["0","0"],"dir":["2","1"],"guion":True,"guia":True,"c":3}],
 "lecturas":[{"rotulo":"determinante","formula":"2*x-1"},{"rotulo":"área","formula":"abs(2*x-1)"}],
 "etiquetas":["Determinante","Área del paralelogramo"],"etiquetaSlider":"Valor de x en el vector v",
 "alt":"Dos vectores u igual a (2, 1) y v igual a (1, x) que forman un paralelogramo cuya área cambia al mover v, con una recta punteada sobre la que los vectores quedan alineados"}
glos={"det":"El determinante es un número que se calcula de una matriz cuadrada. En dimensión 2 es el área con signo del paralelogramo que forman sus columnas.",
 "invertible":"Una matriz es invertible si existe otra matriz que la deshace. Eso pasa si y solo si su determinante no es cero.",
 "cofactores":"El desarrollo por cofactores calcula un determinante eligiendo una fila, multiplicando cada elemento por su subdeterminante y alternando los signos.",
 "triangular":"Una matriz triangular tiene ceros debajo de la diagonal principal, o encima de ella."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"Estos son dos vectores del plano, u igual a (2, 1) y v igual a (1, x)."],
 [3,6,"Los dos vectores forman un paralelogramo."],
 [6,12,"Al mover v, el área del paralelogramo cambia. El determinante da esa área con signo."],
 [12,17,"Cuando v cae sobre la recta de u, el paralelogramo se aplasta y el determinante vale 0."],
 [17,22,"Con x igual a 2 el determinante vale 3. Es 2 por 2 menos 1 por 1."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,2],[9,0.8],[14,0.5],[16.5,-0.5],[18,2],[22,2]],"guide":[[12,0],[13,1]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("El {{gl:det|determinante}} es un número que resume una matriz cuadrada. En dimensión 2 es el área con signo del paralelogramo que forman sus columnas. Si el determinante es 0, el paralelogramo se aplasta en una recta, y eso dice que la matriz no se puede invertir.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la matriz cuya primera columna es el vector u igual a (2, 1) y cuya segunda columna es el vector v igual a (1, x)."),EQ("A="+M(2,1,1,"x")+"\\ \\Rightarrow\\ \\det A=2x-1"),P("Las dos columnas forman un paralelogramo, y la gráfica muestra cómo cambia al mover v."),{"t":"grafica","animar":"dibujar","alt":"Los vectores u y v y el paralelogramo que forman"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Cuando x vale 2 el determinante es 2 por 2 menos 1 por 1. ¿Cuánto vale?","opciones":[1,2,3,4],"correcta":3,"bien":"Muy bien. Vale 3. Más abajo se ve el paralelogramo con esa área.","mal":"Vale 3, porque 2 por 2 es 4 y 4 menos 1 es 3. Más abajo se ve el paralelogramo con esa área."}),
 sec("El paralelogramo","El paralelogramo",P("Mira cómo cambia el determinante, que es el área con signo, a medida que se mueve v."),{"t":"acercando","ds":[-0.5,0.5,1,2],"alt":"El paralelogramo de los vectores u y v para varios valores de x"},P("Con x igual a 0.5 el vector v queda sobre la recta de u y el determinante es 0. Con x menor que 0.5 el determinante es negativo, porque el orden de los vectores se invierte.")),
 sec("Determinante de 2 por 2","De 2 por 2",EQ("\\det"+M("a","b","c","d")+"=ad-bc"),
   PASOS([("\\det"+M(2,1,1,"x")+"=2\\cdot x-1\\cdot 1=2x-1","Se multiplican los elementos de la diagonal principal y se resta el producto de la otra diagonal."),
          ("x=2:\\quad \\det A=4-1=3","Es el área del paralelogramo de la gráfica."),
          ("x=\\dfrac{1}{2}:\\quad \\det A=0","Las columnas quedan alineadas y la matriz no tiene inversa.")]),
   OJO("El signo importa. Un determinante negativo no significa un área negativa, sino que el orden de las columnas invierte la orientación.")),
 sec("Determinante de 3 por 3","De 3 por 3",P("Se puede desarrollar por una fila, multiplicando cada elemento por el determinante que queda al quitar su fila y su columna, con signos que alternan más, menos, más. A esto se le llama desarrollo por {{gl:cofactores|cofactores}}."),
   PASOS([("\\det"+M(1,2,0,0,1,3,2,0,1)+"=1\\cdot\\det"+M(1,3,0,1)+"-2\\cdot\\det"+M(0,3,2,1)+"+0","Se desarrolla por la primera fila. El cero hace desaparecer el tercer término."),
          ("=1\\cdot(1-0)-2\\cdot(0-6)=1+12","Se calculan los determinantes de 2 por 2."),
          ("=13","Es el valor del determinante.")]),
   OJO("Conviene desarrollar por la fila o la columna que tenga más ceros, para hacer menos cuentas.")),
 sec("Con eliminación","Con eliminación",P("Otra forma es llevar la matriz a una forma {{gl:triangular|triangular}}, donde el determinante es el producto de la diagonal. Sumar un múltiplo de una fila a otra no cambia el determinante."),
   PASOS([("R_{3}\\leftarrow R_{3}-2R_{1}:\\quad "+M(1,2,0,0,1,3,0,-4,1),"Se hace cero el 2 de la tercera fila."),
          ("R_{3}\\leftarrow R_{3}+4R_{2}:\\quad "+M(1,2,0,0,1,3,0,0,13),"Se hace cero el menos 4."),
          ("\\det=1\\cdot 1\\cdot 13=13","En una matriz triangular, el determinante es el producto de la diagonal. Sale el mismo 13.")])),
 sec("Propiedades","Propiedades",P("Estas reglas ahorran cuentas y se usan mucho."),
   PASOS([("\\det(AB)=\\det A\\cdot\\det B","El determinante de un producto es el producto de los determinantes."),
          ("\\text{Intercambiar dos filas cambia el signo del determinante}","Se invierte la orientación."),
          ("\\det(kA)=k^{n}\\det A\\quad (A\\ \\text{de}\\ n\\times n)","Cada una de las n filas se multiplica por k. Para una matriz 2 por 2 con determinante 5, el de 3A es 9 por 5."),
          ("A\\ \\text{invertible}\\iff\\det A\\ne 0","Es la {{gl:invertible|condición de invertibilidad}}.")])),
 eng("La singularidad de un brazo robótico","Un brazo con dos eslabones mueve su punta según el ángulo de sus dos articulaciones. La matriz que relaciona las velocidades de las articulaciones con la de la punta se llama jacobiana, y su determinante dice si el brazo puede moverse en cualquier dirección.","\\det J=l_{1}\\,l_{2}\\operatorname{sen}\\theta_{2}",
   [("Eslabón 1","0.5 m"),("Eslabón 2","0.4 m"),("Con codo a 90 grados","det igual a 0.2 m²")],"Con el codo a 90 grados el determinante vale 0.5 por 0.4 por 1, o sea 0.2 metros cuadrados, y el brazo se mueve bien en todas las direcciones. Cuando el codo está estirado, theta 2 es 0, el determinante se anula y el brazo pierde una dirección de movimiento. Eso se llama una singularidad. Es un modelo simplificado, porque no incluye los límites de las articulaciones."),
 completar("Se calcula el determinante de una matriz de 2 por 2. Falta el producto de la diagonal secundaria.","\\det"+M(3,1,2,4)+"=3\\cdot 4-[[hueco]]",
   [("1\\cdot 2","uno por dos"),("3\\cdot 2","tres por dos"),("1\\cdot 4","uno por cuatro")],0,
   ["","Ese producto mezcla un elemento de la diagonal principal con otro de la secundaria. La diagonal secundaria tiene el 1 y el 2.","Ese producto usa el 4, que ya está en la diagonal principal. La diagonal secundaria es 1 y 2."],"La diagonal secundaria va de arriba a la derecha hasta abajo a la izquierda.","La diagonal secundaria tiene el 1 y el 2, y su producto es 2. El determinante es 12 menos 2, o sea 10."),
 error("Alguien calculó este determinante intercambiando filas y se equivocó en un paso. Toca el paso que está mal.",
   [("A="+M(0,1,2,3),"Es la matriz de partida.","La matriz es 0 1, 2 3"),
    ("\\text{Se intercambian las filas y queda}\\ "+M(2,3,0,1)+"\\ \\text{con determinante}\\ 2\\cdot 1=2","Este paso es el que falla.","Se intercambian las filas y el determinante es 2 por 1, o sea 2"),
    ("\\text{Por tanto}\\ \\det A=2","Esta conclusión depende del paso anterior.","Por tanto el determinante de A es 2")],1,
   "Intercambiar dos filas cambia el signo del determinante, así que el de A es el opuesto del de la matriz con las filas intercambiadas. Con la fórmula directa, 0 por 3 menos 1 por 2 da menos 2.",
   "\\det A=0\\cdot 3-1\\cdot 2=-2","Calcula el determinante de A con la fórmula directa y compáralo."),
 ordenar("Estos son los pasos para el determinante de una matriz de 3 por 3 con eliminación, pero están desordenados.",
   [("A="+M(1,2,0,0,1,3,2,0,1),"La matriz de partida"),
    ("R_{3}\\leftarrow R_{3}-2R_{1}","A la tercera fila se le resta dos veces la primera"),
    ("R_{3}\\leftarrow R_{3}+4R_{2}","A la tercera fila se le suma cuatro veces la segunda"),
    ("\\det A=1\\cdot 1\\cdot 13=13","El determinante es el producto de la diagonal, 13")],[2,0,3,1],
   "Se parte de la matriz, se hacen ceros bajo la diagonal con dos operaciones de fila y se multiplica la diagonal.","Primero se escribe la matriz."),
]
S+=cierre("Mini simulacro de determinantes",[
 num("$\\det\\begin{pmatrix}2&1\\\\3&4\\end{pmatrix}$","5",0.001,"Se aplica $ad-bc=2\\cdot 4-1\\cdot 3=5$."),
 mcq("Si se intercambian dos filas de una matriz, su determinante:",["cambia de signo","no cambia","se multiplica por $2$","se hace $0$"],0,"Intercambiar dos filas invierte la orientación y cambia el signo del determinante."),
 num("Si $A$ es $3\\times3$ con $\\det A = 5$, entonces $\\det(2A)$ es:","40",0.001,"Se usa $\\det(kA)=k^{n}\\det A$ con $k=2$ y $n=3$, o sea $8\\cdot 5=40$.")])
prac=[
 {"titulo":"Los vectores","grafica":{"draw":1},"bloques":[P("Estos son dos vectores del plano."),EQ("u=(2,1),\\qquad v=(1,x)")]},
 {"titulo":"Mueve v","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El vector v cambia, el paralelogramo se deforma y abajo se ven el determinante y el área.")]},
 {"titulo":"Se aplasta","grafica":{"draw":1,"guide":1},"laboratorio":True,"d":0.5,"bloques":[P("Con x igual a 0.5 el vector v queda sobre la recta punteada de u. El paralelogramo no tiene área y el determinante es 0.")]},
 {"titulo":"El resultado","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("\\det"+M(2,1,1,2)+"=2\\cdot 2-1\\cdot 1=3"),P("Con x igual a 2 el determinante vale 3, justo el área del paralelogramo.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Cuida los signos al desarrollar por cofactores."}]}]
preg={"tex":"\\det"+M(1,0,2,0,3,1,1,1,0),"opciones":["$-7$","$7$","$-5$","$5$"],"correcta":0,
 "explicacion":"Se desarrolla por la primera fila. El primer elemento 1 multiplica el determinante de 3, 1, 1, 0, que vale menos 1. El segundo elemento es 0. El tercer elemento 2 multiplica el determinante de 0, 3, 1, 1, que vale menos 3, con signo más. La suma es menos 1 menos 6, o sea menos 7.",
 "verificacion":{"formula":"1*(3*0-1*1)-0*(0*0-1*1)+2*(0*1-3*1)+0*x","a":0,"esperado":-7},
 "pistas":["Desarrolla por la primera fila, que tiene un cero.","El primer cofactor es el determinante de 3, 1, 1, 0. El tercero es el de 0, 3, 1, 1.","Suma 1 por el primero, menos 0 por el segundo, más 2 por el tercero."],
 "errores":["","El signo está al revés. Revisa los dos determinantes de 2 por 2, que valen menos 1 y menos 3.","Revisa la cuenta. El primer término es 1 por menos 1 y el tercero es 2 por menos 3.","Revisa la cuenta y el signo. Suma menos 1 y menos 6."]}
res=["En dimensión 2, el determinante es el área con signo del paralelogramo de las columnas, y vale ad menos bc.","Se calcula por cofactores o llevando la matriz a forma triangular. Intercambiar filas cambia el signo.","Una matriz es invertible si y solo si su determinante no es cero."]
write(lesson("alglin-m1-l4","Lección 4 de 4","Determinantes",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-det.json")
