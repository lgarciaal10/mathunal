import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 2 Orden superior y coeficientes constantes"
graf={"tipo":"plano","x":[-3.2,2.2],"y":[-1.2,7.5],"a":-2.5,"b":1.5,"inicio":0,
 "elementos":[trazo("exp({x})",-3.2,2.2,90,2),
  {"t":"trazo","puntos":[[f"{-3.2+5.4*k/90:.4f}",f"({-3.2+5.4*k/90:.4f})*exp({-3.2+5.4*k/90:.4f})"] for k in range(91)],"c":3,"guia":True},
  {"t":"recta","p":["x","0"],"dir":["0","1"],"guion":True,"c":1},
  {"t":"punto","p":["x","exp(x)"],"c":2},
  {"t":"punto","p":["x","x*exp(x)"],"c":3,"guia":True}],
 "lecturas":[{"rotulo":"posición x","formula":"x"},{"rotulo":"Wronskiano","formula":"exp(2*x)"}],
 "etiquetas":["Posición x","Wronskiano en esa posición"],"etiquetaSlider":"Posición x",
 "alt":"Las soluciones e a la x y x por e a la x de y segunda menos 2y prima más y igual a 0, con una recta vertical que se mueve y el Wronskiano e a la 2x, que nunca vale cero"}
glos={"reduccion":"La reducción de orden sirve cuando ya se conoce una solución y1 de una ecuación lineal de segundo orden. Se busca otra de la forma y2 igual a v por y1, y queda una ecuación para v que es más fácil.",
 "wronskiano":"El Wronskiano de dos funciones y1 y y2 es y1 por la derivada de y2, menos la derivada de y1 por y2. Si es distinto de cero, las funciones son independientes.",
 "independientes":"Dos soluciones son linealmente independientes si ninguna es un múltiplo de la otra. Con dos independientes se arma la solución general."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación y segunda menos 2y prima más y igual a 0 tiene la solución y1 igual a e a la x. Falta una segunda solución, independiente de la primera."],
 [4,8,"La reducción de orden busca y2 como v por y1. Al reemplazar queda v segunda igual a 0, así que v vale x y y2 es x por e a la x."],
 [8,14,"El Wronskiano compara las dos soluciones en un punto. Mueve la recta vertical y mira cómo cambia su valor, que es e a la 2x."],
 [14,18,"El Wronskiano nunca vale 0. Entonces las dos soluciones son independientes en todo el eje y forman una base."],
 [18,22,"En x igual a 1 el Wronskiano vale e al cuadrado, unos 7.39."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[9,-2],[13,1],[22,1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Una ecuación lineal de segundo orden necesita dos soluciones independientes para armar la solución general. A veces solo se conoce una. La {{gl:reduccion|reducción de orden}} fabrica la segunda a partir de la primera. Y el {{gl:wronskiano|Wronskiano}} es la prueba que dice si dos soluciones son {{gl:independientes|independientes}}.")),
 sec("Un ejemplo","Un ejemplo",P("Esta ecuación tiene la solución e a la x. Se busca una segunda."),EQ("y''-2y'+y=0,\\qquad y_{1}=e^{x}"),{"t":"grafica","animar":"dibujar","alt":"La solución conocida y1"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El Wronskiano de coseno de x y seno de x es coseno por coseno, menos menos seno por seno. ¿Cuánto vale?","opciones":[0,1,-1,2],"correcta":1,"bien":"Muy bien. Vale 1, porque coseno cuadrado más seno cuadrado es 1. Más abajo se calcula otro.","mal":"Vale 1, porque coseno cuadrado más seno cuadrado es 1. Más abajo se calcula otro."}),
 sec("La segunda solución","La segunda",P("Mira la segunda solución junto a la primera y cómo cambia el Wronskiano."),{"t":"acercando","ds":[-2,-1,0,1],"alt":"El Wronskiano en varias posiciones"},P("La segunda solución es x por e a la x. El Wronskiano de las dos vale e a la 2x, que es positivo en todo punto.")),
 sec("Reducción de orden","Reducción",P("Se busca y2 igual a v por y1 y se reemplaza en la ecuación."),
   PASOS([("y_{2}=v\\,e^{x}","La forma buscada."),
          ("y_{2}'=(v'+v)e^{x},\\quad y_{2}''=(v''+2v'+v)e^{x}","Se deriva con la regla del producto."),
          ("(v''+2v'+v)-2(v'+v)+v=v''=0","Se reemplaza en la ecuación y casi todo se cancela."),
          ("v=x\\ \\Rightarrow\\ y_{2}=x\\,e^{x}","Con v igual a x se tiene una solución distinta de y1. Se omite la constante porque solo se necesita una.")]),
   OJO("En general los términos con v se cancelan porque y1 ya es solución. Siempre queda una ecuación en v' que se resuelve como una de primer orden.")),
 sec("El Wronskiano","El Wronskiano",P("El Wronskiano de y1 y y2 se calcula con esta fórmula."),
   PASOS([("W(y_{1},y_{2})=y_{1}y_{2}'-y_{1}'y_{2}","La definición."),
          ("W=e^{x}(x+1)e^{x}-e^{x}\\,x\\,e^{x}=e^{2x}","Con y1 igual a e a la x y y2 igual a x e a la x."),
          ("W\\ne 0\\ \\Rightarrow\\ \\text{independientes}","Como no se anula, las soluciones son independientes y la solución general es c1 y1 más c2 y2.")]),
   OJO("Si el Wronskiano vale 0 en un punto, las funciones pueden ser dependientes. Para soluciones de la misma ecuación lineal, basta mirar un solo punto.")),
 eng("Una puerta que cierra sin golpear","Un cierrapuertas hidráulico se ajusta para que la puerta vuelva sin rebotar. Eso es el amortiguamiento crítico, donde la ecuación característica tiene una raíz doble. La segunda solución con la raíz doble sale justo por reducción de orden.","\\theta''+6\\theta'+9\\theta=0",
   [("Ángulo inicial","0.5 rad"),("Raíz doble","menos 3"),("Hasta el 1 por ciento","unos 2.2 s")],"Con la raíz doble r igual a menos 3, una solución es e a la menos 3t, y la reducción de orden da la otra, t por e a la menos 3t. Con la puerta soltada desde el reposo en 0.5 radianes, el ángulo es 0.5 más 1.5 t, por e a la menos 3t. Baja sin cruzar el cero y queda en el 1 por ciento del ángulo inicial en unos 2.2 segundos. Es un modelo simplificado, porque supone una fricción lineal."),
 completar("Si y2 es v por e a la x, se deriva con la regla del producto.","y_{2}'=(v'+[[hueco]])\\,e^{x}",
   [("v","la función v"),("v''","la segunda derivada de v"),("1","el número uno")],0,
   ["","La derivada de e a la x es e a la x, así que queda v y no su segunda derivada.","La derivada de e a la x es e a la x por v, no un uno suelto."],"Es la regla del producto, v prima por e a la x más v por e a la x.","Sale v prima por e a la x, más v por la derivada de e a la x, que es e a la x."),
 error("Alguien calculó el Wronskiano de e a la x y e a la 2x y se equivocó en un paso. Toca el paso que está mal.",
   [("W=y_{1}y_{2}'-y_{1}'y_{2}","La fórmula del Wronskiano.","la definición del Wronskiano"),
    ("y_{1}y_{2}'=e^{x}\\cdot 2e^{2x}=2e^{3x}","Primer término.","el primer término es 2 e a la 3x"),
    ("y_{1}'y_{2}=e^{x}\\cdot e^{2x}=e^{3x}","Segundo término.","el segundo término es e a la 3x"),
    ("W=2e^{3x}+e^{3x}=3e^{3x}","Este paso es el que falla.","W es 3 e a la 3x")],3,
   "La fórmula resta el segundo término. Debe ser 2 e a la 3x menos e a la 3x, que da e a la 3x.",
   "W=2e^{3x}-e^{3x}=e^{3x}","Mira el signo entre los dos términos."),
 ordenar("Estos son los pasos para hallar una segunda solución de y segunda menos 4y prima más 4y igual a 0, sabiendo que e a la 2x es solución, pero están desordenados.",
   [("y_{2}=v\\,e^{2x}","La forma buscada"),
    ("y_{2}'=(v'+2v)e^{2x},\\ y_{2}''=(v''+4v'+4v)e^{2x}","Las derivadas"),
    ("v''e^{2x}=0","Se reemplaza y se cancela casi todo"),
    ("v=x\\ \\Rightarrow\\ y_{2}=x\\,e^{2x}","La segunda solución")],[2,0,3,1],
   "Se propone y2 igual a v por y1, se deriva, se reemplaza y queda v segunda igual a 0.","Se empieza con la forma buscada."),
]
S+=cierre("Mini simulacro de Wronskiano",[
 banco("ed_c2_17","Dos soluciones de una ecuación lineal de segundo orden son independientes cuando su Wronskiano no se anula."),
 banco("ed_c2_18","El Wronskiano es $e^{x}\\cdot 2e^{2x}-e^{x}\\cdot e^{2x}=e^{3x}$, que en $x=0$ vale $1$.")])
prac=[
 {"titulo":"Dos soluciones","grafica":{"draw":1,"guide":1},"bloques":[P("La solución e a la x y su compañera x por e a la x."),EQ("y''-2y'+y=0")]},
 {"titulo":"Mueve la posición","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La recta vertical se mueve y abajo se lee el Wronskiano, que siempre es positivo.")]},
 {"titulo":"Nunca vale cero","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("W=e^{2x}>0"),P("En x igual a 1 el Wronskiano vale unos 7.39.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Usa y1 por y2 prima menos y1 prima por y2."}]}]
preg={"tex":"W(x,\\,x^{2})\\ \\text{en}\\ x=2\\ \\text{vale}","opciones":["$4$","$12$","$0$","$8$"],"correcta":0,
 "explicacion":"Con y1 igual a x y y2 igual a x cuadrado, W es x por 2x menos 1 por x cuadrado, o sea x cuadrado. En x igual a 2 vale 4.",
 "verificacion":{"formula":"x*2*x-1*x*x","a":2,"esperado":4},
 "pistas":["Usa W igual a y1 por y2 prima menos y1 prima por y2.","y2 prima es 2x y y1 prima es 1.","Queda 2x cuadrado menos x cuadrado."],
 "errores":["","Ahí se sumaron los dos términos en vez de restarlos. La fórmula lleva una resta.","Eso significaría que son dependientes, pero x y x cuadrado no son múltiplos una de la otra.","Falta restar el segundo término, y1 prima por y2, que vale x cuadrado."]}
res=["La reducción de orden busca y2 como v por y1 y deja una ecuación fácil para v.","El Wronskiano es y1 por y2 prima menos y1 prima por y2.","Si el Wronskiano no se anula, las soluciones son independientes y forman una base."]
write(lesson("edo-m2-l3","Lección 3 de 4","Reducción de orden y Wronskiano",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=5,curso="Ecuaciones Diferenciales"),"edo-wronskiano.json")
