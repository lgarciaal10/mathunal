import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 1 Matrices, determinantes y sistemas"
def AUG(*c,n=3):
    rows=[c[i*(n+1):(i+1)*(n+1)] for i in range(len(c)//(n+1))]
    return "\\left(\\begin{array}{"+"c"*n+"|c}"+"\\\\".join("&".join(str(v) for v in r) for r in rows)+"\\end{array}\\right)"
graf={"tipo":"plano","x":[-5.5,7.33],"y":[-2,5],"a":-0.5,"b":1.5,"inicio":0,
 "elementos":[
  {"t":"recta","p":["0","4"],"dir":["1","-2"],"nombre":"fila 1","c":0},
  {"t":"recta","p":["1","2"],"dir":["1+x","1-2*x"],"nombre":"fila 2 nueva","c":1},
  {"t":"punto","p":["1","2"],"nombre":"solución","c":2}],
 "lecturas":[{"rotulo":"coeficiente de x","formula":"1-2*x"},{"rotulo":"coeficiente de y","formula":"-1-x"}],
 "etiquetas":["Coeficiente de x en la fila 2","Coeficiente de y en la fila 2"],"etiquetaSlider":"Múltiplo m que se resta de la fila 1",
 "alt":"Una recta fija, la primera ecuación, y la segunda ecuación que gira alrededor de la solución al restarle m veces la primera, hasta quedar horizontal cuando m vale un medio"}
glos={"pivote":"El pivote es el primer número distinto de cero de una fila, de izquierda a derecha, en una matriz escalonada.",
 "escalonada":"Una matriz escalonada tiene los pivotes bajando hacia la derecha, con ceros debajo de cada uno.",
 "rref":"La forma escalonada reducida tiene pivotes iguales a 1 y ceros también arriba de cada pivote. Es única para cada matriz.",
 "aumentada":"La matriz aumentada es la matriz del sistema con una columna más al final, que lleva los términos de la derecha."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"Este es el sistema 2x más y igual a 4 y x menos y igual a menos 1. Sus rectas se cortan en (1, 2)."],
 [3,6,"Una operación de fila reemplaza la ecuación 2 por ella menos m veces la ecuación 1. La solución no cambia."],
 [6,12,"Al variar m, la nueva recta gira alrededor de la solución, siempre pasando por (1, 2)."],
 [12,17,"Con m igual a un medio, el coeficiente de x se vuelve 0. La recta queda horizontal, y igual a 2."],
 [17,22,"Ese es el objetivo de la eliminación, ceros bajo los pivotes. Ahora se lee y y luego x."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,0],[9,1.2],[11,-0.4],[12,0.5],[22,0.5]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("La eliminación de Gauss-Jordan resuelve sistemas de cualquier tamaño con tres operaciones sobre las filas. No cambian la solución, y sirven para ir haciendo ceros hasta que la solución se lee sola. Se escribe en una {{gl:aumentada|matriz aumentada}} para no repetir las incógnitas.")),
 sec("Un ejemplo","Un ejemplo",P("Mira las dos rectas del sistema, y cómo cambia la segunda al restarle un múltiplo de la primera."),EQ("\\begin{cases}2x+y=4\\\\x-y=-1\\end{cases}"),{"t":"grafica","animar":"dibujar","alt":"La primera recta y la segunda recta que se puede girar alrededor de la solución"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La fila 2 nueva es la ecuación 2 menos m veces la 1, y su coeficiente de x es 1 menos 2m. ¿Cuánto vale con m igual a un medio?","opciones":[0,0.5,1,2],"correcta":0,"bien":"Muy bien. Vale 0, y ahí la recta queda horizontal. Más abajo se ve.","mal":"Vale 0, porque 1 menos 2 por un medio es 0. Ahí la recta queda horizontal, y más abajo se ve."}),
 sec("Girar la recta","Girar",P("Mira cómo gira la segunda recta al cambiar m."),{"t":"acercando","ds":[-0.4,0,0.5,1],"alt":"La segunda recta girando alrededor de la solución"},P("La solución, el punto (1, 2), nunca se mueve. Con m igual a <b>un medio</b>, la recta queda horizontal.")),
 sec("Las tres operaciones","Operaciones",P("Estas son las únicas operaciones permitidas sobre las filas, y ninguna cambia las soluciones."),
   PASOS([("R_{i}\\leftrightarrow R_{j}","Intercambiar dos filas."),
          ("R_{i}\\leftarrow cR_{i}\\quad (c\\ne 0)","Multiplicar una fila por un número que no sea cero."),
          ("R_{i}\\leftarrow R_{i}+cR_{j}","Sumarle a una fila un múltiplo de otra. Es la que hace los ceros.")]),
   OJO("Multiplicar una fila por 0 no está permitido, porque borra una ecuación y cambia el sistema.")),
 sec("Un sistema de 3 por 3","De 3 por 3",P("Mira cómo se llega a una forma {{gl:escalonada|escalonada}} con {{gl:pivote|pivotes}}, para el sistema x más y más z igual a 6, 2x menos y más z igual a 3 y x más 2y menos z igual a 2."),
   PASOS([(AUG(1,1,1,6,2,-1,1,3,1,2,-1,2),"Es la matriz aumentada del sistema."),
          ("R_{2}\\leftarrow R_{2}-2R_{1},\\ R_{3}\\leftarrow R_{3}-R_{1}:\\quad "+AUG(1,1,1,6,0,-3,-1,-9,0,1,-2,-4),"Se hacen ceros bajo el primer pivote."),
          ("R_{2}\\leftrightarrow R_{3},\\ R_{3}\\leftarrow R_{3}+3R_{2}:\\quad "+AUG(1,1,1,6,0,1,-2,-4,0,0,-7,-21),"Se cambian las filas para tener un pivote de 1 y se hacen ceros bajo el segundo."),
          ("z=3,\\quad y=-4+2z=2,\\quad x=6-y-z=1","Se despeja hacia atrás, de abajo hacia arriba.")])),
 sec("Forma reducida","Reducida",P("Si se sigue eliminando hacia arriba y se divide cada fila entre su pivote, se llega a la {{gl:rref|forma escalonada reducida}}, donde la solución se lee directamente."),
   PASOS([(AUG(1,0,0,1,0,1,0,2,0,0,1,3),"La solución se lee en la última columna, x igual a 1, y igual a 2 y z igual a 3.")]),
   OJO("La forma escalonada reducida es única. No depende del orden en que se hagan las operaciones, aunque la escalonada simple sí puede variar.")),
 sec("El rango con pivotes","Rango",P("El número de pivotes es el rango de la matriz. Las columnas sin pivote son las variables libres."),
   PASOS([(M(1,2,1,2,4,2,3,6,4)+"\\xrightarrow{R_{2}-2R_{1},\\ R_{3}-3R_{1}}"+M(1,2,1,0,0,0,0,0,1),"Se hacen ceros bajo el primer pivote."),
          ("\\operatorname{rango}=2","Hay dos filas con pivote, la primera y la tercera. La fila de ceros no aporta.")])),
 eng("Las corrientes de tres mallas","En un circuito con tres mallas, la ley de Kirchhoff de voltajes da una ecuación por malla con las corrientes como incógnitas. Es un sistema de 3 por 3 que se resuelve con eliminación.","\\begin{cases}6i_{1}-2i_{2}=10\\\\-2i_{1}+7i_{2}-3i_{3}=0\\\\-3i_{2}+8i_{3}=5\\end{cases}",
   [("Fuentes","10 V y 5 V"),("Resistencias","de 1 a 6 ohmios"),("Corrientes","2 A, 1 A y 1 A")],"Con eliminación se llega a las corrientes i1 igual a 2 amperios, i2 igual a 1 amperio e i3 igual a 1 amperio. Se comprueba en cada ecuación. Es un modelo simplificado, porque supone resistencias ideales y fuentes constantes."),
 completar("Se resta 2 veces la fila 1 a la fila 2 en la matriz aumentada, con fila 1 igual a (1, 1, 1 | 6) y fila 2 igual a (2, menos 1, 1 | 3). Falta el segundo elemento de la nueva fila 2.","R_{2}-2R_{1}=\\left(0,\\ [[hueco]],\\ -1\\ \\middle|\\ -9\\right)",
   [("-3","menos tres"),("-1","menos uno"),("1","uno")],0,
   ["","Ese es el elemento original sin restar nada. Hay que restar 2 veces el segundo elemento de la fila 1, que es 1.","Revisa el signo. Menos 1 menos 2 por 1 es menos 3."],"El segundo elemento es menos 1 menos 2 por 1.","Menos 1 menos 2 por 1 da menos 3."),
 error("Alguien hizo una operación de fila y se equivocó en un paso. Toca el paso que está mal.",
   [("R_{1}=(1,\\ 1,\\ 1\\ |\\ 6),\\quad R_{2}=(2,\\ -1,\\ 1\\ |\\ 3)","Son las dos filas de partida.","La fila 1 es 1, 1, 1, 6 y la fila 2 es 2, menos 1, 1, 3"),
    ("R_{2}-2R_{1}=(0,\\ -3,\\ -1\\ |\\ 3-6)=(0,\\ -3,\\ -1\\ |\\ -3)","Este paso es el que falla.","La fila 2 menos 2 veces la fila 1 es 0, menos 3, menos 1, menos 3"),
    ("\\text{La nueva fila 2 es}\\ (0,\\ -3,\\ -1\\ |\\ -3)","Depende del paso anterior.","La nueva fila 2 es 0, menos 3, menos 1, menos 3")],1,
   "La operación se hace en todos los elementos de la fila, incluido el de la derecha. Hay que restar 2 veces el 6, y no una vez, así que sale 3 menos 12, o sea menos 9.",
   "R_{2}-2R_{1}=(0,\\ -3,\\ -1\\ |\\ 3-12)=(0,\\ -3,\\ -1\\ |\\ -9)","Revisa si en el último elemento se restó 2 veces el 6."),
 ordenar("Estos son los pasos para resolver el sistema de 3 por 3 de la lección, pero están desordenados.",
   [("R_{2}\\leftarrow R_{2}-2R_{1},\\ R_{3}\\leftarrow R_{3}-R_{1}","Se hacen ceros bajo el primer pivote"),
    ("R_{2}\\leftrightarrow R_{3}","Se intercambian las filas 2 y 3 para tener un pivote de 1"),
    ("R_{3}\\leftarrow R_{3}+3R_{2}\\ \\Rightarrow\\ -7z=-21","Se hace cero bajo el segundo pivote y sale menos 7z igual a menos 21"),
    ("z=3,\\ y=2,\\ x=1","Se sustituye hacia atrás")],[2,0,3,1],
   "Primero ceros bajo el primer pivote, luego un intercambio, otra eliminación y al final la sustitución hacia atrás.","Se empieza con las eliminaciones del primer pivote."),
]
S+=cierre("",None)
prac=[
 {"titulo":"Las dos ecuaciones","grafica":{"draw":1},"bloques":[P("La primera ecuación es fija. La segunda se va a modificar."),EQ("\\begin{cases}2x+y=4\\\\x-y=-1\\end{cases}")]},
 {"titulo":"Resta un múltiplo","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La segunda ecuación cambia a ella menos m veces la primera. Gira alrededor de la solución, que no se mueve.")]},
 {"titulo":"Un cero","grafica":{"draw":1,"ok":True},"laboratorio":True,"d":0.5,"bloques":[EQ("R_{2}-\\tfrac{1}{2}R_{1}:\\quad 0\\cdot x-\\tfrac{3}{2}\\,y=-3"),P("Con m igual a un medio el coeficiente de x es 0 y la recta es horizontal. De ahí se lee y igual a 2.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"ok":True,"d":0.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Cuenta los pivotes de la forma escalonada."}]}]
preg={"tex":"\\operatorname{rango}"+M(1,2,1,2,4,2,3,6,5),"opciones":["$2$","$3$","$1$","$0$"],"correcta":0,
 "explicacion":"Se resta 2 veces la fila 1 a la fila 2 y 3 veces la fila 1 a la fila 3. La fila 2 queda de ceros y la fila 3 queda (0, 0, 2). Hay dos filas con pivote, así que el rango es 2.",
 "verificacion":{"formula":"2+0*x","a":0,"esperado":2},
 "pistas":["Haz ceros bajo el primer pivote.","La fila 2 es el doble de la fila 1, así que se anula.","Cuenta las filas que quedan con algún número distinto de cero."],
 "errores":["","Contar las filas no basta. La fila 2 es el doble de la 1 y no aporta nada nuevo.","Hay una fila de ceros, pero la tercera fila sigue teniendo un pivote, así que el rango es más que 1.","La matriz no es nula, así que su rango es al menos 1."]}
res=["Las tres operaciones de fila no cambian las soluciones, y se usan para hacer ceros bajo los pivotes.","Con la matriz aumentada se resuelve un sistema de cualquier tamaño, hasta llegar a la forma escalonada reducida, que es única.","El número de pivotes es el rango, y las columnas sin pivote son variables libres."]
write(lesson("alglin-m1-l3","Lección 3 de 4","Eliminación de Gauss-Jordan",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal",ejercicios=4),"alglin-gauss.json")
