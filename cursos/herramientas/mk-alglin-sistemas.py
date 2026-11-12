import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 1 Matrices, determinantes y sistemas"
SIS=lambda a,b:"\\begin{cases}"+a+"\\\\"+b+"\\end{cases}"
graf={"tipo":"plano","x":[-5,7.83],"y":[-2.5,4.5],"a":-2,"b":4,"inicio":-1,
 "elementos":[
  {"t":"recta","p":["0","4"],"dir":["1","-2"],"nombre":"2x + y = 4","c":0},
  {"t":"recta","p":["x","0"],"dir":["1","1"],"nombre":"x - y = k","c":1},
  {"t":"punto","p":["(4+x)/3","(4-2*x)/3"],"nombre":"solución","c":2}],
 "lecturas":[{"rotulo":"x","formula":"(4+x)/3"},{"rotulo":"y","formula":"(4-2*x)/3"}],
 "etiquetas":["Valor de x en la solución","Valor de y en la solución"],"etiquetaSlider":"Valor de k en la segunda ecuación",
 "alt":"Dos rectas, 2x más y igual a 4 y x menos y igual a k, que se cortan en un punto que se mueve al cambiar k"}
glos={"sistema":"Un sistema de ecuaciones lineales es un conjunto de ecuaciones de primer grado con las mismas incógnitas, que se quiere resolver a la vez.",
 "consistente":"Un sistema es consistente si tiene al menos una solución. Si no tiene ninguna, es inconsistente.",
 "rango":"El rango de una matriz es el número de filas, o de columnas, que son realmente independientes. Se cuenta con los pivotes de la forma escalonada.",
 "homogeneo":"Un sistema homogéneo es uno cuyos términos independientes son todos cero, o sea de la forma A x igual a 0."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"Cada ecuación del sistema es una recta en el plano."],
 [3,6,"La solución es el punto donde las dos rectas se cortan, porque ahí se cumplen las dos ecuaciones."],
 [6,12,"Al cambiar k en la segunda ecuación, esa recta se desliza y el punto de corte se mueve."],
 [12,17,"Con k igual a menos 1, las rectas se cortan en (1, 2)."],
 [17,22,"Se comprueba. 2 por 1 más 2 es 4, y 1 menos 2 es menos 1."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,-1],[9,2],[11,-2],[12,-1],[22,-1]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("Un {{gl:sistema|sistema de ecuaciones lineales}} pide encontrar valores de las incógnitas que cumplan todas las ecuaciones a la vez. Con dos incógnitas, cada ecuación es una recta, y resolver el sistema es encontrar el punto donde se cortan.")),
 sec("Un ejemplo","Un ejemplo",P("Mira este sistema. La primera recta es fija y la segunda depende de un número k."),EQ(SIS("2x+y=4","x-y=k")),{"t":"grafica","animar":"dibujar","alt":"Las dos rectas del sistema y su punto de corte"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con k igual a menos 1, el punto (1, y) está en las dos rectas. ¿Cuánto vale y? Sale de 2 por 1 más y igual a 4.","opciones":[1,2,3,4],"correcta":2,"bien":"Muy bien. Vale 2. Más abajo se ve el punto de corte.","mal":"Vale 2, porque 2 por 1 más y es 4. Más abajo se ve el punto de corte."}),
 sec("El punto de corte","El corte",P("Mira cómo se mueve la solución cuando cambia k."),{"t":"acercando","ds":[-2,-1,1,4],"alt":"Las dos rectas y su punto de corte para varios valores de k"},P("La primera recta no se mueve. La segunda se desliza al cambiar k y arrastra el punto de corte. Con k igual a menos 1 la solución es <b>(1, 2)</b>.")),
 sec("En forma de matriz","En matriz",P("El sistema se puede escribir como una sola ecuación con una matriz, A por x igual a b."),
   EQ(M(2,1,1,-1)+"\\begin{pmatrix}x\\\\y\\end{pmatrix}=\\begin{pmatrix}4\\\\k\\end{pmatrix}"),
   P("La matriz A tiene los coeficientes, el vector x tiene las incógnitas y el vector b tiene los términos de la derecha.")),
 sec("Resolver con k igual a menos 1","Resolver",P("Se suman las ecuaciones para eliminar y."),
   PASOS([(SIS("2x+y=4","x-y=-1"),"Es el sistema con k igual a menos 1."),
          ("3x=3\\ \\Rightarrow\\ x=1","Al sumar, la y se cancela."),
          ("y=4-2x=2","Se reemplaza x en la primera ecuación."),
          ("(x,y)=(1,2)","Es la solución. Se comprueba con la segunda ecuación, 1 menos 2 es menos 1.")])),
 sec("Tres casos","Tres casos",P("Dos rectas pueden cortarse en un punto, no cortarse nunca o ser la misma recta. Eso da tres casos para el sistema."),
   PASOS([("\\det A\\ne 0\\ \\Rightarrow\\ \\text{una solución única}","Las rectas tienen pendientes distintas. Es el caso del ejemplo, con determinante 2 por menos 1 menos 1 por 1, o sea menos 3."),
          ("x+3y=3,\\ \\ 2x+6y=7\\ \\Rightarrow\\ \\text{sin solución}","Son paralelas. Al restar el doble de la primera a la segunda sale 0 igual a 1, que es imposible."),
          ("x+3y=3,\\ \\ 2x+6y=6\\ \\Rightarrow\\ \\text{infinitas soluciones}","Son la misma recta, así que todos sus puntos son soluciones.")])),
 sec("Rango y variables libres","Rango",P("El {{gl:rango|rango}} cuenta cuántas ecuaciones aportan información nueva. Si el sistema es {{gl:consistente|consistente}} y el rango es menor que el número de incógnitas, sobran incógnitas, llamadas variables libres, y hay infinitas soluciones."),
   PASOS([("\\operatorname{rango}(A)=n\\ \\text{y consistente}\\ \\Rightarrow\\ \\text{solución única}","No sobra ninguna incógnita."),
          ("\\operatorname{rango}(A)<n\\ \\text{y consistente}\\ \\Rightarrow\\ \\text{infinitas soluciones}","Hay variables libres."),
          ("\\operatorname{rango}(A)<\\operatorname{rango}\\left([A\\,|\\,b]\\right)\\ \\Rightarrow\\ \\text{sin solución}","Agregar b a la matriz sube el rango, así que b no es combinación de las columnas.")])),
 sec("Sistemas homogéneos","Homogéneos",P("Un sistema {{gl:homogeneo|homogéneo}} tiene todos los términos de la derecha iguales a 0."),
   PASOS([("A\\mathbf{x}=\\mathbf{0}","Siempre es consistente."),
          ("\\mathbf{x}=\\mathbf{0}\\ \\text{es solución}","Es la solución trivial, y siempre sirve."),
          ("\\operatorname{rango}(A)<n\\ \\Rightarrow\\ \\text{hay soluciones no triviales}","Si hay variables libres, además de la trivial hay infinitas más.")])),
 eng("Una carga colgada de dos cables","Un cuerpo de 500 newtons cuelga de dos cables que forman 30 y 60 grados con la horizontal. En equilibrio, las fuerzas horizontales y las verticales se cancelan, y eso da un sistema de dos ecuaciones con las dos tensiones como incógnitas.","\\begin{cases}T_{1}\\cos 30^{\\circ}-T_{2}\\cos 60^{\\circ}=0\\\\ T_{1}\\operatorname{sen}30^{\\circ}+T_{2}\\operatorname{sen}60^{\\circ}=500\\end{cases}",
   [("Peso","500 N"),("Ángulos","30 y 60 grados"),("Tensiones","250 N y 433 N")],"Al resolver el sistema salen T1 igual a 250 newtons y T2 igual a 250 por la raíz de 3, o sea unos 433 newtons. El cable más inclinado hacia la vertical soporta más fuerza. Es un modelo simplificado, porque supone cables sin peso y un nudo que no se mueve."),
 completar("Se resuelve el sistema 2x más y igual a 4 y x menos y igual a menos 1 sumando las dos ecuaciones. Falta el lado derecho.","3x=[[hueco]]",
   [("3","tres"),("5","cinco"),("-3","menos tres")],0,
   ["","Se restaron los lados derechos y no se sumaron. Sumar 4 y menos 1 da 3.","El signo está al revés. 4 más menos 1 es 3, positivo."],"Suma los lados derechos, 4 y menos 1.","Al sumar las ecuaciones se cancela y y queda 3x igual a 4 menos 1, o sea 3."),
 error("Alguien analizó este sistema y se equivocó en un paso. Toca el paso que está mal.",
   [(SIS("x+2y=2","2x+4y=7"),"Es el sistema original.","Las ecuaciones son x más 2y igual a 2 y 2x más 4y igual a 7"),
    ("\\text{Las rectas tienen pendientes distintas, así que hay solución única}","Este paso es el que falla.","Las rectas tienen pendientes distintas, así que hay solución única"),
    ("\\text{La solución es el punto de corte}","Depende del paso anterior.","La solución es el punto de corte")],1,
   "Las dos rectas tienen la misma pendiente. Al restar el doble de la primera a la segunda sale 0 igual a 3, que es imposible. Las rectas son paralelas y el sistema no tiene solución.",
   "2x+4y-2(x+2y)=7-4\\ \\Rightarrow\\ 0=3","Compara los coeficientes de la segunda ecuación con el doble de la primera."),
 ordenar("Estos son los pasos para resolver el sistema 2x más y igual a 4 y x menos y igual a menos 1, pero están desordenados.",
   [("2x+y=4,\\ \\ x-y=-1","Son las dos ecuaciones"),
    ("3x=3\\ \\Rightarrow\\ x=1","Al sumarlas queda 3x igual a 3, o sea x igual a 1"),
    ("y=4-2\\cdot 1=2","Se reemplaza en la primera y sale y igual a 2"),
    ("(x,y)=(1,2)","Es la solución")],[2,0,3,1],
   "Se escriben las ecuaciones, se suman para eliminar y, se despeja x y luego y.","Primero van las ecuaciones."),
]
S+=cierre("Mini simulacro de sistemas",[
 banco("al_c1_04","El determinante $2\\cdot a-2\\cdot 1\\cdot$ ... se anula solo si $a=4$. En ese caso las filas son proporcionales y no hay solución única para todo $\\mathbf{b}$.".replace("$2\\cdot a-2\\cdot 1\\cdot$ ... se anula","$a-4$ se anula")),
 banco("al_c1_16","Con rango menor que el número de incógnitas sobran variables libres, y por eso hay infinitas soluciones."),
 banco("al_c1_15","Al sumar las ecuaciones queda $2x=4$, así que $x=2$.")])
prac=[
 {"titulo":"Las rectas","grafica":{"draw":1},"bloques":[P("Cada ecuación es una recta."),EQ(SIS("2x+y=4","x-y=k"))]},
 {"titulo":"Cambia k","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La segunda recta se desliza y el punto de corte se mueve. Abajo se ven los valores de x y de y en la solución.")]},
 {"titulo":"La solución","grafica":{"draw":1,"ok":True},"laboratorio":True,"d":-1,"bloques":[EQ("(x,y)=(1,2)"),P("Con k igual a menos 1 las rectas se cortan en (1, 2). Se comprueba en las dos ecuaciones.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"ok":True,"d":-1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Elimina una incógnita y reemplaza en la otra ecuación."}]}]
preg={"tex":SIS("x+2y=5","3x-y=1")+"\\ \\Rightarrow\\ y=?","opciones":["$2$","$1$","$3$","$-1$"],"correcta":0,
 "explicacion":"De la segunda ecuación, y es 3x menos 1. Al reemplazar en la primera queda x más 6x menos 2 igual a 5, o sea 7x igual a 7 y x igual a 1. Entonces y vale 3 por 1 menos 1, o sea 2.",
 "verificacion":{"formula":"(1*1-3*5)/(1*(0-1)-2*3)+0*x","a":0,"esperado":2},
 "pistas":["Despeja y en la segunda ecuación.","Queda y igual a 3x menos 1. Reemplázalo en la primera.","Sale 7x igual a 7. Con x calculado, halla y."],
 "errores":["","Ese es el valor de x y no el de y. Falta reemplazarlo para hallar y.","Revisa la cuenta. Con x igual a 1, y es 3 por 1 menos 1.","Revisa el signo. De la segunda ecuación y es 3x menos 1, y con x igual a 1 da 2."]}
res=["Cada ecuación lineal con dos incógnitas es una recta, y la solución es donde se cortan.","Un sistema puede tener solución única, ninguna o infinitas. El determinante y el rango lo deciden.","Un sistema homogéneo siempre tiene la solución trivial. Si el rango es menor que las incógnitas, tiene más."]
write(lesson("alglin-m1-l2","Lección 2 de 4","Sistemas de ecuaciones lineales",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-sistemas.json")
