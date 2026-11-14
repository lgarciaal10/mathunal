import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 2 Espacios vectoriales y transformaciones"
graf={"tipo":"plano","x":[-6,7.2],"y":[-3,4.2],"a":-3,"b":2.5,"inicio":2,
 "elementos":[
  {"t":"recta","p":["0","0"],"dir":["1","1"],"nombre":"espacio columna","c":0},
  {"t":"recta","p":["0","0"],"dir":["1","-1"],"guion":True,"nombre":"espacio nulo","c":2},
  {"t":"vector","b":["x","1"],"nombre":"v","c":1},
  {"t":"vector","b":["x+1","x+1"],"nombre":"Av","c":3}],
 "lecturas":[{"rotulo":"primera componente de Av","formula":"x+1"},{"rotulo":"segunda componente de Av","formula":"x+1"}],
 "etiquetas":["Primera componente de Av","Segunda componente de Av"],"etiquetaSlider":"Primera componente del vector v",
 "alt":"La matriz con todos los unos actúa sobre el vector v igual a (x, 1). El resultado Av siempre cae sobre la recta del espacio columna, y es cero cuando v cae sobre la recta del espacio nulo"}
glos={"espacio_col":"El espacio columna de una matriz es el conjunto de todas las combinaciones de sus columnas, o sea todos los resultados posibles de A por un vector.",
 "espacio_nulo":"El espacio nulo de una matriz es el conjunto de todos los vectores x que cumplen A por x igual a 0.",
 "rango":"El rango de una matriz es la dimensión de su espacio columna, o sea el número de pivotes de su forma escalonada.",
 "nulidad":"La nulidad de una matriz es la dimensión de su espacio nulo, o sea el número de variables libres."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"La matriz A tiene todas sus entradas iguales a 1. Sus dos columnas son el vector (1, 1)."],
 [3,6,"Todo lo que sale de multiplicar A por un vector está sobre la recta y igual a x. Esa recta es el espacio columna."],
 [6,12,"Al mover el vector v, el resultado Av se desliza sobre esa recta, y nunca sale de ella."],
 [12,17,"Cuando v cae sobre la recta punteada, Av es el vector cero. Esa recta es el espacio nulo."],
 [17,22,"El espacio columna tiene dimensión 1 y el nulo también. Suman 2, que es el número de columnas."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,2],[9,0.5],[11,-3],[12,-1],[15,-1],[16.5,2],[22,2]],"guide":[[3,0],[4,1]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("Cada matriz tiene dos espacios importantes. El {{gl:espacio_col|espacio columna}} es todo lo que se puede obtener al multiplicarla por vectores. El {{gl:espacio_nulo|espacio nulo}} es el conjunto de vectores que la matriz manda a cero. Sus dimensiones se llaman {{gl:rango|rango}} y {{gl:nulidad|nulidad}}, y están ligadas por un teorema muy útil.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la matriz A con todos los unos, que actúa sobre un vector v igual a (x, 1)."),EQ("A="+M(1,1,1,1)+",\\qquad Av="+M(1,1,1,1)+"\\begin{pmatrix}x\\\\1\\end{pmatrix}=(x+1)\\begin{pmatrix}1\\\\1\\end{pmatrix}"),{"t":"grafica","animar":"dibujar","alt":"Las dos rectas, el vector v y el resultado Av"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con x igual a 2, el vector v es (2, 1). ¿Cuánto vale la primera componente de Av, que es x más 1?","opciones":[1,2,3,4],"correcta":3,"bien":"Muy bien. Vale 3. Más abajo se ve el resultado sobre la recta.","mal":"Vale 3, porque 2 más 1 es 3. Más abajo se ve el resultado sobre la recta."}),
 sec("Lo que sale de A","Lo que sale",P("Mira cómo se mueve Av al cambiar v."),{"t":"acercando","ds":[-3,-1,1,2.5],"alt":"El resultado Av para varios valores de v"},P("El resultado siempre está sobre la recta del espacio columna. Y cuando v cae sobre la recta punteada, el resultado es el vector cero.")),
 sec("Espacio columna y rango","Columna",P("El espacio columna se genera con las columnas de la matriz. Su dimensión es el rango, que es el número de pivotes."),
   PASOS([("A="+M(1,2,2,4)+"\\xrightarrow{R_{2}-2R_{1}}"+M(1,2,0,0),"Se escalona la matriz."),
          ("\\operatorname{rango}A=1","Hay un solo pivote."),
          ("\\text{Espacio columna}=\\operatorname{gen}\\{(1,2)\\}","La segunda columna es el doble de la primera, así que genera lo mismo.")])),
 sec("Espacio nulo y nulidad","Nulo",P("El espacio nulo se halla resolviendo A x igual a 0. Cada variable libre aporta un vector a su base."),
   PASOS([("A="+M(1,1,1,1)+",\\quad Ax=0\\ \\Rightarrow\\ x_{1}+x_{2}=0","Las dos ecuaciones son la misma."),
          ("x_{2}=t\\ \\text{libre},\\quad x_{1}=-t","Una variable libre, t."),
          ("\\operatorname{Nu}(A)=\\operatorname{gen}\\{(-1,1)\\},\\quad \\text{nulidad}=1","El espacio nulo es la recta punteada de la gráfica.")])),
 sec("El teorema del rango","El teorema",P("Cada columna de la matriz o tiene un pivote o es una variable libre. Eso da una cuenta muy simple."),
   EQ("\\operatorname{rango}(A)+\\operatorname{nulidad}(A)=n\\quad (n=\\text{número de columnas})"),
   PASOS([("A\\ \\text{de}\\ 4\\times 6\\ \\text{con rango}\\ 3\\ \\Rightarrow\\ \\text{nulidad}=6-3=3","Se usa el número de columnas, que es 6."),
          ("\\text{El espacio columna es un subespacio de}\\ \\mathbb{R}^{m}","Sus vectores tienen m componentes, una por fila."),
          ("\\text{El espacio nulo es un subespacio de}\\ \\mathbb{R}^{n}","Sus vectores tienen n componentes, una por columna.")]),
   OJO("La nulidad se calcula con el número de columnas n y no con el de filas.")),
 eng("Un brazo robótico redundante","Un brazo con 5 articulaciones mueve su extremo en un espacio de 3 dimensiones. La matriz jacobiana, de 3 por 5, relaciona las velocidades de las articulaciones con la del extremo. Su espacio nulo reúne los movimientos internos que no mueven el extremo.","\\dot{\\mathbf{x}}=J\\,\\dot{\\boldsymbol{\\theta}},\\quad J\\ \\text{de}\\ 3\\times 5",
   [("Articulaciones","5"),("Dimensión de la tarea","3"),("Movimientos internos","2")],"Si el rango de J es 3, la nulidad es 5 menos 3, o sea 2. Hay un espacio de dimensión 2 de movimientos de las articulaciones que dejan el extremo quieto, y se pueden usar para esquivar obstáculos. Es un modelo simplificado, porque el jacobiano cambia con la postura del brazo."),
 completar("Una matriz de 4 por 6 tiene rango 3. Falta la nulidad.","\\operatorname{nulidad}=n-\\operatorname{rango}=[[hueco]]",
   [("3","tres"),("1","uno"),("2","dos")],0,
   ["","Se usó el número de filas, 4, en vez del de columnas, 6. La nulidad es 6 menos 3.","Revisa la cuenta. El número de columnas es 6 y el rango es 3, así que la nulidad es 3."],"Usa el número de columnas.","La matriz tiene 6 columnas. La nulidad es 6 menos 3, o sea 3."),
 error("Alguien calculó el rango de una matriz y se equivocó en un paso. Toca el primer paso donde aparece el error.",
   [("A="+M(1,2,2,4),"Es la matriz.","La matriz es 1, 2, 2, 4"),
    ("\\text{Tiene dos filas distintas de cero, así que el rango es 2}","Este paso es el que falla.","Tiene dos filas distintas de cero, así que el rango es 2"),
    ("\\text{Por tanto la nulidad es}\\ 2-2=0","Depende del paso anterior.","Por tanto la nulidad es 2 menos 2, o sea 0")],1,
   "Las filas deben ser independientes para contar, y aquí la segunda es el doble de la primera. Al escalonar queda una fila de ceros, así que el rango es 1 y la nulidad es 1.",
   "\\operatorname{rango}A=1,\\quad \\text{nulidad}=2-1=1","Escalona la matriz y cuenta los pivotes."),
 ordenar("Estos son los pasos para hallar el espacio nulo de la matriz con todos los unos, pero están desordenados.",
   [("Ax=0,\\quad A="+M(1,1,1,1),"El sistema homogéneo"),
    ("R_{2}\\leftarrow R_{2}-R_{1}\\ \\Rightarrow\\ x_{1}+x_{2}=0","Se resta la fila 1 y queda una sola ecuación"),
    ("x_{2}=t,\\quad x_{1}=-t","Una variable libre"),
    ("\\operatorname{Nu}(A)=\\operatorname{gen}\\{(-1,1)\\}","El espacio nulo es la recta generada por (menos 1, 1)")],[2,0,3,1],
   "Se plantea el sistema homogéneo, se elimina, se identifica la variable libre y se escribe el espacio nulo.","Se empieza con el sistema A x igual a 0."),
]
S+=cierre("Mini simulacro de espacios fundamentales",[
 banco("al_c2_01","Con 3 columnas y rango 2, la nulidad es $3-2=1$."),
 banco("al_c2_10","Cada columna es pivote o variable libre, así que el rango y la nulidad suman las columnas."),
 banco("al_c2_12","Los vectores del espacio columna tienen tantas componentes como filas tiene la matriz.")])
prac=[
 {"titulo":"La matriz y las rectas","grafica":{"draw":1},"bloques":[P("La matriz A tiene todas sus entradas iguales a 1."),EQ("A="+M(1,1,1,1))]},
 {"titulo":"Mueve v","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El vector v cambia y Av se desliza sobre la recta del espacio columna. Abajo se ven sus dos componentes.")]},
 {"titulo":"Al espacio nulo","grafica":{"draw":1,"guide":1},"laboratorio":True,"d":-1,"bloques":[P("Con x igual a menos 1, el vector v cae sobre la recta punteada y Av es el vector cero. Esa recta es el espacio nulo.")]},
 {"titulo":"Rango y nulidad","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("\\operatorname{rango}+\\operatorname{nulidad}=1+1=2=n"),P("Hay una dirección que sobrevive, el espacio columna, y una que se pierde, el espacio nulo.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Escalona y cuenta los pivotes. Las columnas sin pivote son la nulidad."}]}]
preg={"tex":"\\text{Nulidad de}\\ "+MC(4,1,2,0,1,0,0,1,3,1,2,1,4),"opciones":["$2$","$1$","$3$","$0$"],"correcta":0,
 "explicacion":"La tercera fila es la suma de las dos primeras, así que al escalonar se anula. Quedan 2 pivotes, el rango es 2. La matriz tiene 4 columnas y la nulidad es 4 menos 2, o sea 2.",
 "verificacion":{"formula":"4-2+0*x","a":0,"esperado":2},
 "pistas":["Escalona la matriz. ¿Qué pasa con la tercera fila?","La tercera fila es la suma de las dos primeras, así que queda de ceros y el rango es 2.","La nulidad es el número de columnas menos el rango."],
 "errores":["","Es el resultado si el rango fuera 3. Pero la tercera fila es combinación de las otras dos.","Con 4 columnas y rango 2, la nulidad no puede ser 3. Es 4 menos 2.","Con 4 columnas y solo 2 pivotes, quedan 2 columnas sin pivote, así que la nulidad no es 0."]}
res=["El espacio columna son los resultados posibles de A por un vector, y el espacio nulo son los vectores que A manda a cero.","El rango cuenta los pivotes y la nulidad cuenta las variables libres.","Rango más nulidad es igual al número de columnas."]
write(lesson("alglin-m2-l2","Lección 2 de 4","Espacios fundamentales y rango",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-fundamentales.json")
