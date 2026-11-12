import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 2 Ecuaciones, inecuaciones y sistemas"
TS=[-2+10*k/100 for k in range(101)]
graf={"tipo":"plano","x":[-2.5,8.5],"y":[-1,6],"a":0.5,"b":4,"inicio":2,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"abs({t:.4f}-3)"] for t in TS],"c":2},
  {"t":"recta","p":["0","x"],"dir":["1","0"],"guion":True,"c":3,"guia":True},
  {"t":"segmento","a":["3-x","x"],"b":["3+x","x"],"c":3,"guia":True},
  {"t":"punto","p":["3-x","x"],"c":1},{"t":"punto","p":["3+x","x"],"c":1}],
 "lecturas":[{"rotulo":"extremo izquierdo","formula":"3-x"},{"rotulo":"extremo derecho","formula":"3+x"}],
 "etiquetas":["Extremo izquierdo","Extremo derecho"],"etiquetaSlider":"Altura r de la recta",
 "alt":"La gráfica de valor absoluto de x menos 3, una V con vértice en 3, y una recta horizontal de altura r. Los x para los que la V queda por debajo de la recta van de 3 menos r a 3 más r"}
glos={"inecuacion":"Una inecuación es una desigualdad con una incógnita. Su solución es un conjunto de valores, que se escribe como un intervalo o una unión de intervalos.",
 "intervalo":"Un intervalo es un conjunto de números entre dos extremos. Con corchetes incluye el extremo y con paréntesis no lo incluye.",
 "valorabsoluto":"El valor absoluto de un número es su distancia al cero. El valor absoluto de x menos 3 es la distancia de x a 3."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La V es el valor absoluto de x menos 3. Mide la distancia de x al número 3."],
 [4,8,"La recta horizontal es la altura r. La desigualdad pide los x donde la V queda por debajo de la recta."],
 [8,14,"Al subir r el intervalo se ensancha hacia los dos lados. Los extremos son 3 menos r y 3 más r."],
 [14,18,"Con r igual a 2 el intervalo va de 1 a 5. Son los números que están a menos de 2 unidades de 3."],
 [18,22,"Con r igual a 4 el intervalo va de menos 1 a 7."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,2],[8,2],[11,4],[13,2],[17,2],[18,4],[22,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Una {{gl:inecuacion|inecuación}} se resuelve casi igual que una ecuación, con una diferencia clave. Al multiplicar o dividir por un número negativo, el sentido de la desigualdad se invierte. La solución casi siempre es un {{gl:intervalo|intervalo}}, o una unión de varios.")),
 sec("Un ejemplo","Un ejemplo",P("Mira qué números cumplen que su distancia a 3 es menor que r."),EQ("|x-3|<r"),{"t":"grafica","animar":"dibujar","alt":"La V del valor absoluto y una recta horizontal"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El valor absoluto de x menos 3 es la distancia de x a 3. Si esa distancia es menor que 2, ¿cuál es el extremo derecho del intervalo?","opciones":[1,3,5,7],"correcta":5,"bien":"Muy bien. Es 5, porque 3 más 2 es 5. El izquierdo es 1.","mal":"Es 5, porque 3 más 2 es 5. El izquierdo es 1."}),
 sec("Cambiando r","Cambiando r",P("Mira cómo cambia el intervalo al mover la altura r."),{"t":"acercando","ds":[2,4,0.5,3],"alt":"El intervalo para varios valores de r"},P("El intervalo siempre está centrado en 3, y el valor de r es su radio.")),
 sec("Inecuaciones lineales","Lineales",P("Se despeja como en una ecuación. Al multiplicar por un negativo, la desigualdad cambia de sentido."),
   PASOS([("3x-7>2\\ \\Rightarrow\\ 3x>9\\ \\Rightarrow\\ x>3","Se suma 7 y se divide entre 3."),
          ("-2x+6>2\\ \\Rightarrow\\ -2x>-4\\ \\Rightarrow\\ x<2","Se divide entre menos 2, y la desigualdad se invierte."),
          ("x\\in(-\\infty,2)","La solución en notación de intervalos.")]),
   OJO("En un intervalo, el paréntesis indica que el extremo no se incluye, y el corchete que sí. El infinito siempre va con paréntesis.")),
 sec("Valor absoluto, cuadráticas y fracciones","Otros tipos",P("Cada tipo se resuelve de forma distinta."),
   PASOS([("|x-3|<2\\ \\Leftrightarrow\\ -2<x-3<2\\ \\Leftrightarrow\\ 1<x<5","El valor absoluto menor que un número es un intervalo."),
          ("x^{2}-4\\ge 0\\ \\Rightarrow\\ x\\le -2\\ \\text{o}\\ x\\ge 2","Se hallan las raíces y se prueba un valor en cada tramo."),
          ("\\dfrac{x-1}{x+2}\\le 0\\ \\Rightarrow\\ -2<x\\le 1","Se prueban los tramos. El extremo menos 2 se excluye porque anula el denominador.")]),
   OJO("En una inecuación con fracción nunca se puede multiplicar por el denominador sin saber su signo. Es más seguro estudiar el signo del cociente en cada tramo.")),
 eng("La tolerancia de una pieza","Un eje se fabrica con un diámetro de 25 milímetros y una tolerancia de 0.05. La pieza se acepta si su diámetro cumple una desigualdad con valor absoluto.","|d-25|\\le 0.05",
   [("Diámetro nominal","25 mm"),("Tolerancia","0.05 mm"),("Rango aceptado","24.95 a 25.05 mm")],"La desigualdad dice que la distancia entre la medida y 25 es de a lo más 0.05, o sea que el diámetro está entre 24.95 y 25.05. Una pieza que mide 25.07 se rechaza. El intervalo es cerrado, porque los extremos todavía se aceptan. Es una regla de calidad simple, y no considera el error del instrumento de medida."),
 completar("Se quita el valor absoluto de una desigualdad con menor que.","|x-3|<2\\ \\Rightarrow\\ [[hueco]]<x-3<2",
   [("-2","menos dos"),("0","cero"),("2","dos")],0,
   ["","Con 0 solo se tendría la mitad de la distancia. El otro lado de la desigualdad es menos 2.","Con 2 a los dos lados, la desigualdad no tendría sentido. El lado izquierdo es el opuesto."],"El valor absoluto menor que 2 significa entre menos 2 y 2.","El límite inferior es menos 2."),
 error("Alguien resolvió una inecuación y se equivocó en un paso. Toca el paso que está mal.",
   [("-2x+6>2","La inecuación.","la inecuación es menos 2x más 6 mayor que 2"),
    ("-2x>-4","Se resta 6.","se resta 6 en los dos lados"),
    ("x>2","Este paso es el que falla.","al dividir queda x mayor que 2")],2,
   "Al dividir entre un número negativo, la desigualdad cambia de sentido. Menos 4 dividido entre menos 2 es 2, y queda x menor que 2.",
   "x<2","Pregúntate qué pasa al dividir por un número negativo."),
 ordenar("Estos son los pasos para resolver x al cuadrado menos 4 mayor o igual que 0, pero están desordenados.",
   [("x^{2}-4=0\\ \\Rightarrow\\ x=\\pm 2","Se hallan las raíces"),
    ("\\text{tramos:}\\ (-\\infty,-2),\\ (-2,2),\\ (2,\\infty)","Se separan los tramos"),
    ("x=0\\ \\Rightarrow\\ -4<0\\ \\text{no cumple}","Se prueba un valor en cada tramo"),
    ("(-\\infty,-2]\\cup[2,\\infty)","La solución")],[2,0,3,1],
   "Se hallan las raíces, se separan los tramos, se prueba un valor en cada uno y se unen los que cumplen.","Se empieza hallando las raíces."),
]
S+=cierre("Mini simulacro de inecuaciones",[
 banco("mb_c2_07","El valor absoluto menor que $2$ da $-2<x-3<2$, o sea $1<x<5$."),
 banco("mb_c2_13","Las raíces son $\\pm2$, y la parábola es positiva afuera de ellas."),
 banco("mb_c2_14","El cociente es negativo entre $-2$ y $1$. Se excluye $-2$ porque anula el denominador.")])
prac=[
 {"titulo":"La V","grafica":{"draw":1,"guide":1},"bloques":[P("La V del valor absoluto de x menos 3 y una recta de altura r."),EQ("|x-3|<r")]},
 {"titulo":"Cambia r","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen los extremos del intervalo.")]},
 {"titulo":"Un intervalo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":4,"bloques":[EQ("r=4\\ \\Rightarrow\\ -1<x<7"),P("Con r igual a 4 el intervalo va de menos 1 a 7.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":4},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Cuida el sentido de la desigualdad al dividir por un negativo."}]}]
preg={"tex":"5-2x\\ge 1\\ \\text{tiene como solución}","opciones":["$x\\le 2$","$x\\ge 2$","$x\\le -2$","$x\\ge -2$"],"correcta":0,
 "explicacion":"Se resta 5 y queda menos 2x mayor o igual que menos 4. Al dividir entre menos 2 la desigualdad se invierte, y queda x menor o igual que 2.",
 "verificacion":{"formula":"5-2*x","a":2,"esperado":1},
 "pistas":["Resta 5 a los dos lados.","Queda menos 2x mayor o igual que menos 4.","Al dividir entre menos 2 hay que invertir la desigualdad."],
 "errores":["","Se olvidó invertir la desigualdad al dividir entre un número negativo.","Eso sale de restar mal. Menos 4 dividido entre menos 2 es 2, no menos 2.","Aquí se invirtió el signo del número y no el sentido de la desigualdad."]}
res=["Al multiplicar o dividir una inecuación por un negativo, la desigualdad cambia de sentido.","El valor absoluto de x menos a menor que r es el intervalo de a menos r a a más r.","En cuadráticas y fracciones se hallan las raíces, se separan los tramos y se prueba un valor en cada uno."]
write(lesson("mb-m2-l3","Lección 3 de 5","Inecuaciones",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=7,curso="Matemáticas Básicas"),"matbas-inecuaciones.json")
