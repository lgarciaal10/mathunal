import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 1 EDO de primer orden"
XR=[-0.5,2.3]; YR=[-0.5,1.03]
EL=campo(lambda x,y:3*abs(y)**(2/3),XR,YR,14,8,0.07)
ARR="((({x}-x)+abs({x}-x))/2)^3"
EL+=[{"t":"trazo","puntos":[["-0.4","0"],["2.2","0"]],"c":3,"guia":True},trazo("(((({x})-x)+abs(({x})-x))/2)^3",-0.4,2.2,52,2),{"t":"punto","p":["x","0"],"c":1,"nombre":"se despega"}]
graf={"tipo":"plano","x":XR,"y":YR,"a":0,"b":1.5,"inicio":0.5,"elementos":EL,
 "lecturas":[{"rotulo":"c","formula":"x"},{"rotulo":"y(2)","formula":"(((2-x)+abs(2-x))/2)^3"}],
 "etiquetas":["Instante en que se despega","Valor de y en x igual a 2"],"etiquetaSlider":"Instante c en que la solución se despega de 0",
 "alt":"El campo de pendientes de y prima igual a 3 por y a la dos tercios, la solución y igual a 0 y una familia de soluciones que se quedan en 0 hasta x igual a c y luego suben como x menos c al cubo"}
glos={"existencia":"El teorema de existencia dice que, bajo ciertas condiciones, hay al menos una solución que pasa por el punto inicial, al menos cerca de él.",
 "unicidad":"El teorema de unicidad dice que, bajo ciertas condiciones, solo hay una solución que pasa por el punto inicial.",
 "picard":"El teorema de Picard y Lindelöf asegura una solución única si la función de la ecuación y su derivada con respecto a y son continuas cerca del punto inicial.",
 "orden":"El orden de una ecuación diferencial es el de la derivada más alta que aparece en ella."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación y prima igual a 3 por y a la dos tercios tiene una solución evidente, y igual a 0, porque entonces los dos lados valen 0."],
 [4,9,"Pero también y igual a x al cubo la cumple, y pasa por el mismo punto inicial (0, 0). Hay dos soluciones por el mismo punto."],
 [9,15,"Más aún, hay una familia entera. La solución se queda en 0 hasta un instante c y luego se despega como x menos c al cubo."],
 [15,19,"No se rompe nada, porque todas son soluciones. Lo que falla es la unicidad."],
 [19,22,"El teorema de Picard explica por qué. La derivada de la función con respecto a y no es continua en y igual a 0."]],
 "canales":{"draw":[[0.3,0],[4,1]],"d":[[4,0],[7,0.5],[10,1.2],[13,0.3],[16,1],[22,0.5]],"guide":[[0.5,0],[1,1]]},
 "intervalos":{"ok":[19,22]}}
S=[
 sec("La idea",None,P("Antes de resolver una ecuación diferencial conviene preguntar si tiene solución, y si esa solución es la única que pasa por el punto inicial. El teorema de {{gl:picard|Picard y Lindelöf}} da una condición simple para saberlo. Es muy importante en ingeniería, porque un modelo que tiene dos soluciones para los mismos datos no sirve para predecir.")),
 sec("Un ejemplo","Un ejemplo",P("Mira esta ecuación con la condición inicial y de 0 igual a 0."),EQ("y'=3\\,y^{2/3},\\qquad y(0)=0"),{"t":"grafica","animar":"dibujar","alt":"El campo de pendientes y dos soluciones por el origen"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La solución y igual a x al cubo tiene y prima igual a 3x al cuadrado. Con x igual a 1, ¿cuánto vale 3 por y a la dos tercios?","opciones":[1,2,3,6],"correcta":3,"bien":"Muy bien. Vale 3, igual que 3x al cuadrado. Por eso x al cubo es solución.","mal":"Vale 3, porque y vale 1 y 1 a la dos tercios es 1. Es igual a 3x al cuadrado, así que x al cubo es solución."}),
 sec("Muchas soluciones","Muchas soluciones",P("Mira cómo la solución se despega de 0 en instantes distintos."),{"t":"acercando","ds":[0,0.5,1,1.5],"alt":"Soluciones que se despegan de 0 en instantes distintos"},P("Todas pasan por (0, 0) y todas cumplen la ecuación. No hay una solución única.")),
 sec("El teorema","El teorema",P("Para y prima igual a f de x y, con y de x0 igual a y0, el teorema de Picard y Lindelöf dice lo siguiente."),
   EQ("f\\ \\text{y}\\ \\dfrac{\\partial f}{\\partial y}\\ \\text{continuas cerca de}\\ (x_{0},y_{0})\\ \\Rightarrow\\ \\text{hay una solución única}"),
   PASOS([("f(x,y)=3y^{2/3}\\ \\Rightarrow\\ \\dfrac{\\partial f}{\\partial y}=2y^{-1/3}","La derivada tiene y en el denominador."),
          ("\\dfrac{\\partial f}{\\partial y}\\ \\text{no existe en}\\ y=0","No es continua en el punto inicial (0, 0), y el teorema no asegura unicidad."),
          ("y'=x+y^{2},\\ y(0)=1\\ \\Rightarrow\\ \\text{solución única}","Aquí f y su derivada son continuas en todo el plano.")]),
   OJO("Las condiciones del teorema son suficientes, no necesarias. Si no se cumplen, puede haber unicidad igual, pero el teorema no la asegura.")),
 sec("Solo cerca del punto","Solo cerca",P("El teorema habla de una vecindad del punto, no de toda la recta."),
   PASOS([("y'=y^{2},\\quad y(0)=1\\ \\Rightarrow\\ y=\\dfrac{1}{1-x}","La solución existe y es única."),
          ("x\\to 1^{-}\\ \\Rightarrow\\ y\\to\\infty","Pero explota en x igual a 1. Solo existe en el intervalo desde menos infinito hasta 1.")])),
 sec("Orden y verificación","Orden",P("El {{gl:orden|orden}} de una ecuación es el de la derivada más alta."),
   PASOS([("y''+(y')^{3}+y=0\\ \\text{es de orden 2}","La derivada más alta es la segunda. La potencia 3 no cambia el orden."),
          ("y=e^{3x}\\ \\text{cumple}\\ y'=3y","Se deriva y se comprueba. Así se verifica una solución."),
          ("y'(0)=3e^{0}=3","Con la ecuación, y prima en 0 vale 3 por y de 0.")])),
 eng("El vaciado de un tanque","Un tanque con un orificio en el fondo se vacía a una velocidad que depende de la raíz de la altura, por la ley de Torricelli. La ecuación no tiene derivada continua con respecto a h en h igual a 0, y eso significa que cuando el tanque está vacío no se puede saber cuándo empezó a vaciarse.","\\dfrac{dh}{dt}=-k\\sqrt{h}",
   [("Altura inicial","1 m"),("Constante k","0.2 √m/s"),("Tiempo para vaciarse","10 s")],"La solución es h igual a (raíz de h0 menos k t sobre 2) al cuadrado, y llega a 0 en t igual a 2 por la raíz de h0 sobre k, o sea 10 segundos. Después de eso se queda en 0. El tanque vacío tiene muchos pasados posibles, y por eso la unicidad falla hacia atrás. Es un modelo simplificado, porque supone un orificio pequeño y un fluido ideal."),
 completar("Se revisa si y prima igual a 3 por y a la dos tercios cumple el teorema de unicidad. Falta la derivada de f con respecto a y.","\\dfrac{\\partial f}{\\partial y}=[[hueco]]",
   [("2\\,y^{-1/3}","dos y a la menos un tercio"),("2\\,y^{1/3}","dos y a la un tercio"),("3","tres")],0,
   ["","El exponente es 2 sobre 3 menos 1, o sea menos un tercio, y no más un tercio.","Eso sería si f fuera 3y. Aquí hay que derivar 3 por y a la 2 tercios."],"Deriva 3 por y a la dos tercios y baja el exponente.","3 por 2 tercios es 2, y el exponente 2 sobre 3 menos 1 es menos un tercio."),
 error("Alguien aplicó el teorema de unicidad y se equivocó en un paso. Toca el paso que está mal.",
   [("y'=3y^{2/3},\\quad y(0)=0","Es el problema.","y prima es 3 y a la dos tercios con y de 0 igual a 0"),
    ("f\\ \\text{es continua, así que la solución es única}","Este paso es el que falla.","f es continua, así que la solución es única"),
    ("\\text{La solución es}\\ y=0","Depende del paso anterior.","La solución es y igual a 0")],1,
   "El teorema pide también que la derivada de f con respecto a y sea continua. Aquí vale 2 por y a la menos un tercio, que no existe en y igual a 0, y por eso hay más soluciones, como y igual a x al cubo.",
   "\\dfrac{\\partial f}{\\partial y}=2y^{-1/3}\\ \\text{no es continua en}\\ y=0","Revisa si el teorema pide algo más que la continuidad de f."),
 ordenar("Estos son los pasos para decidir si y prima igual a x más y al cuadrado con y de 0 igual a 1 tiene solución única, pero están desordenados.",
   [("f(x,y)=x+y^{2}","Se identifica f"),
    ("\\dfrac{\\partial f}{\\partial y}=2y","Se deriva con respecto a y"),
    ("f\\ \\text{y}\\ \\dfrac{\\partial f}{\\partial y}\\ \\text{son continuas en todo el plano}","Se revisa la continuidad"),
    ("\\text{Hay solución única cerca de}\\ (0,1)","Se aplica el teorema")],[2,0,3,1],
   "Se identifica f, se deriva con respecto a y, se comprueba la continuidad y se aplica el teorema.","Se empieza identificando f."),
]
S+=cierre("Mini simulacro de existencia y unicidad",[banco("ed_c1_17","Es la hipótesis del teorema de Picard y Lindelöf."),banco("ed_c1_18","Si $y=e^{3x}$, entonces $y'=3e^{3x}$ y $y'(0)=3$."),banco("ed_c1_19","La derivada más alta es $y''$, así que el orden es $2$.")])
prac=[
 {"titulo":"Dos soluciones","grafica":{"draw":1,"guide":1},"bloques":[P("La ecuación tiene la solución y igual a 0, en verde, y otras."),EQ("y'=3\\,y^{2/3},\\quad y(0)=0")]},
 {"titulo":"Cambia c","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La solución se queda en 0 hasta el instante c y luego se despega. Abajo se ven c y el valor en x igual a 2.")]},
 {"titulo":"Sin unicidad","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.5,"bloques":[EQ("\\dfrac{\\partial f}{\\partial y}=2y^{-1/3}\\ \\text{no es continua en}\\ y=0"),P("Como la derivada no es continua en el punto inicial, el teorema no asegura una sola solución, y de hecho hay muchas.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Revisa f y también su derivada con respecto a y."}]}]
preg={"tex":"\\text{problema de valor inicial con solución única garantizada}","encabezado":"¿Cuál de estos problemas de valor inicial tiene solución única garantizada por el teorema?","opciones":["$y'=x+y^{2},\\ y(0)=1$","$y'=\\sqrt{|y|},\\ y(0)=0$","$y'=3y^{2/3},\\ y(0)=0$","$y'=y^{1/3},\\ y(0)=0$"],"correcta":0,
 "explicacion":"En el primero, f igual a x más y al cuadrado y su derivada 2y son continuas en todo el plano. En los otros tres, la derivada con respecto a y no existe en y igual a 0, justo donde está el punto inicial.",
 "pistas":["Calcula la derivada de f con respecto a y en cada uno.","Fíjate en y igual a 0, donde empieza cada problema.","El primero tiene derivada 2y, que es continua en todas partes."],
 "errores":["","La derivada de la raíz de y tiene y en el denominador y no está definida en 0. Hay más de una solución.","Ya se vio que tiene muchas soluciones por el origen.","La derivada es un tercio de y a la menos dos tercios, y no está definida en 0."]}
res=["Un problema de valor inicial tiene solución única si f y su derivada con respecto a y son continuas cerca del punto inicial.","Si no se cumplen esas condiciones puede haber más de una solución, como y igual a 0 y y igual a x al cubo.","El teorema habla de una vecindad del punto, y la solución puede dejar de existir más adelante."]
write(lesson("edo-m1-l2","Lección 2 de 6","Existencia y unicidad",24,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Ecuaciones Diferenciales"),"edo-existencia.json")
