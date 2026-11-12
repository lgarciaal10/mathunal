import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 3 Funciones, trigonometría y geometría analítica"
CIR=[[f"{3+math.cos(2*math.pi*k/60):.4f}",f"{math.sin(2*math.pi*k/60):.4f}"] for k in range(61)]
graf={"tipo":"plano","x":[-8,13],"y":[-1.5,10],"a":0,"b":1,"inicio":0,
 "elementos":[{"t":"trazo","puntos":CIR,"c":3,"guia":True},
  {"t":"segmento","a":["1","1"],"b":["7","9"],"c":2},
  {"t":"segmento","a":["1","1"],"b":["1+6*x","1+8*x"],"c":1,"guia":True,"guion":True},
  {"t":"punto","p":["1","1"],"c":2},{"t":"punto","p":["7","9"],"c":2},
  {"t":"punto","p":["1+6*x","1+8*x"],"c":1,"guia":True}],
 "lecturas":[{"rotulo":"fracción recorrida s","formula":"x"},{"rotulo":"distancia desde A","formula":"10*x"}],
 "etiquetas":["Fracción recorrida de A a B","Distancia recorrida desde A"],"etiquetaSlider":"Fracción recorrida s",
 "alt":"El segmento del punto A, 1 coma 1, al punto B, 7 coma 9, que mide 10, con un punto que se mueve de A a B. Abajo, cerca de A, la circunferencia de centro 3, 0 y radio 1. Con s igual a un medio el punto es el punto medio, 4 coma 5"}
glos={"distancia":"La distancia entre dos puntos sale del teorema de Pitágoras. Es la raíz de la diferencia de las x al cuadrado más la diferencia de las y al cuadrado.",
 "puntomedio":"El punto medio de un segmento tiene como coordenadas el promedio de las coordenadas de los extremos.",
 "circunferencia":"Una circunferencia es el conjunto de puntos a una distancia r, el radio, de un punto fijo, el centro. Su ecuación es x menos h al cuadrado más y menos k al cuadrado igual a r al cuadrado."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Los puntos A, 1 coma 1, y B, 7 coma 9, definen un segmento. Un punto se va a mover de A a B."],
 [4,8,"La distancia entre A y B sale de Pitágoras. Es la raíz de 6 al cuadrado más 8 al cuadrado, o sea 10."],
 [8,14,"Mueve s. La distancia recorrida desde A crece de 0 a 10."],
 [14,18,"Con s igual a un medio, el punto es el punto medio, 4 coma 5. Es el promedio de las coordenadas de A y de B."],
 [18,22,"Abajo, cerca de A, está la circunferencia de centro 3, 0 y radio 1. Su ecuación es x al cuadrado más y al cuadrado, menos 6x, más 8, igual a 0."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[11,1],[13,0.5],[18,0.5],[22,0.5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("La geometría analítica describe figuras con ecuaciones. Con las coordenadas se calcula la {{gl:distancia|distancia}} entre puntos, el {{gl:puntomedio|punto medio}} de un segmento, la ecuación de una recta y la ecuación de una {{gl:circunferencia|circunferencia}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira un segmento, un punto que lo recorre y una circunferencia."),EQ("d=\\sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}"),{"t":"grafica","animar":"dibujar","alt":"Un segmento y una circunferencia"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Entre A, 1 coma 1, y B, 7 coma 9, la diferencia de x es 6 y la de y es 8. ¿Cuánto vale la raíz de 6 al cuadrado más 8 al cuadrado?","opciones":[10,12,14,100],"correcta":10,"bien":"Muy bien. Vale 10, porque 36 más 64 es 100. Es una terna pitagórica.","mal":"Vale 10, porque 36 más 64 es 100, y la raíz de 100 es 10."}),
 sec("Recorriendo el segmento","El segmento",P("Mira la distancia recorrida desde A al avanzar por el segmento."),{"t":"acercando","ds":[0,0.5,1,0.25],"alt":"El punto en varios lugares del segmento"},P("La distancia recorrida es 10 por s. Con s igual a un medio llegamos al punto medio, que está a 5 de cada extremo.")),
 sec("Distancia y punto medio","Distancia",P("Las dos fórmulas se usan con las coordenadas de los extremos."),
   PASOS([("d=\\sqrt{(7-1)^{2}+(9-1)^{2}}=\\sqrt{36+64}=10","La distancia entre A y B."),
          ("M=\\left(\\dfrac{x_{1}+x_{2}}{2},\\ \\dfrac{y_{1}+y_{2}}{2}\\right)=(4,5)","El punto medio."),
          ("(2,-1)\\ \\text{y}\\ (6,5)\\ \\Rightarrow\\ M=(4,2)","Otro ejemplo de punto medio.")])),
 sec("La recta","La recta",P("Una recta se escribe con un punto y la pendiente."),
   PASOS([("y-y_{1}=m\\,(x-x_{1})","La forma punto-pendiente."),
          ("m=2,\\ (0,-3)\\ \\Rightarrow\\ y=2x-3","Un ejemplo."),
          ("m_{1}=m_{2}\\ \\text{(paralelas)},\\qquad m_{1}m_{2}=-1\\ \\text{(perpendiculares)}","Rectas paralelas y perpendiculares.")]),
   OJO("Los lados opuestos de un paralelogramo son paralelos y tienen la misma pendiente.")),
 sec("La circunferencia","Circunferencia",P("Se completa el cuadrado para leer el centro y el radio."),
   PASOS([("(x-h)^{2}+(y-k)^{2}=r^{2}","La ecuación con centro h, k y radio r."),
          ("x^{2}+y^{2}-6x+8=0\\ \\Rightarrow\\ (x-3)^{2}+y^{2}=9-8=1","Se completa el cuadrado en x y se pasa la constante."),
          ("\\text{centro}\\ (3,0),\\quad r=1","Se lee el centro y el radio.")])),
 eng("El avance de una fresadora","Una fresadora de control numérico mueve el cabezal en línea recta entre dos puntos del plano. La distancia entre ellos define el tiempo de avance.","d=\\sqrt{\\Delta x^{2}+\\Delta y^{2}}",
   [("De","10, 20 mm"),("A","40, 60 mm"),("Recorrido","50 mm")],"El cabezal se mueve 30 milímetros en x y 40 en y, así que la distancia es la raíz de 900 más 1600, o sea 50 milímetros. Con una velocidad de avance de 25 milímetros por segundo, tarda 2 segundos. Es el tiempo de movimiento en línea recta, sin considerar aceleraciones al arrancar y frenar."),
 completar("Se completa el cuadrado de x al cuadrado más y al cuadrado menos 6x más 8.","(x-[[hueco]])^{2}+y^{2}=1",
   [("3","tres"),("6","seis"),("-3","menos tres")],0,
   ["","El número es la mitad del coeficiente de x, y no el coeficiente completo.","Con x más 3 el centro quedaría en menos 3, y el término de x sería positivo."],"Es la mitad del coeficiente de x.","La mitad de 6 es 3, y el centro está en x igual a 3."),
 error("Alguien calculó la distancia entre 1 coma 1 y 4 coma 5 y se equivocó en un paso. Toca el paso que está mal.",
   [("d=\\sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}","La fórmula.","la fórmula de la distancia"),
    ("d=\\sqrt{3+4}","Este paso es el que falla.","queda la raíz de 3 más 4"),
    ("d=\\sqrt{7}","El resultado.","la distancia es raíz de 7")],1,
   "Cada diferencia se eleva al cuadrado antes de sumar. Es 3 al cuadrado más 4 al cuadrado, o sea 9 más 16, y la distancia es 5.",
   "d=\\sqrt{9+16}=5","Recuerda elevar al cuadrado cada diferencia."),
 ordenar("Estos son los pasos para hallar la recta por 1 coma 2 y 3 coma 8, pero están desordenados.",
   [("m=\\dfrac{8-2}{3-1}=3","La pendiente"),
    ("y-2=3(x-1)","La forma punto-pendiente"),
    ("y=3x-3+2","Se distribuye"),
    ("y=3x-1","Se reducen términos")],[2,0,3,1],
   "Se calcula la pendiente, se usa la forma punto-pendiente y se despeja y.","Se empieza con la pendiente."),
]
S+=cierre("Mini simulacro de geometría analítica",[
 banco("mb_c3_15","Se calcula $\\sqrt{3^2+4^2}=\\sqrt{25}=5$."),
 banco("mb_c3_16","El punto medio es el promedio, $\\left(\\tfrac{2+6}{2},\\tfrac{-1+5}{2}\\right)=(4,2)$."),
 banco("mb_c3_17","Se completa el cuadrado, $(x-3)^2+y^2=1$, y el radio es $1$.")])
prac=[
 {"titulo":"El segmento","grafica":{"draw":1,"guide":1},"bloques":[P("Un segmento y una circunferencia."),EQ("A(1,1),\\ B(7,9)")]},
 {"titulo":"Mueve el punto","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee la distancia recorrida desde A.")]},
 {"titulo":"El punto medio","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.5,"bloques":[EQ("s=\\tfrac{1}{2}\\ \\Rightarrow\\ M=(4,5)"),P("Con s igual a un medio, el punto está a 5 de cada extremo.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Eleva al cuadrado cada diferencia y suma."}]}]
preg={"tex":"\\text{La distancia entre}\\ (-1,2)\\ \\text{y}\\ (4,14)\\ \\text{es}","opciones":["$13$","$17$","$7$","$169$"],"correcta":0,
 "explicacion":"La diferencia de x es 5 y la de y es 12. Entonces la distancia es la raíz de 25 más 144, o sea la raíz de 169, que es 13.",
 "verificacion":{"formula":"sqrt((4+1)*(4+1)+(14-2)*(14-2))+0*x","a":0,"esperado":13},
 "pistas":["Resta las x y resta las y.","Salen 5 y 12.","Eleva al cuadrado, suma y saca la raíz."],
 "errores":["","Ese es 5 más 12. Hay que elevar al cuadrado, sumar y después sacar la raíz.","Ese es 12 menos 5. No es la fórmula de la distancia.","Ese valor es 25 más 144, y falta sacar la raíz."]}
res=["La distancia es la raíz de la suma de los cuadrados de las diferencias de x y de y.","El punto medio es el promedio de las coordenadas, y las rectas paralelas tienen la misma pendiente.","La circunferencia tiene la ecuación x menos h al cuadrado más y menos k al cuadrado igual a r al cuadrado, y se lee completando el cuadrado."]
write(lesson("mb-m3-l4","Lección 4 de 4","Geometría analítica",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=7,curso="Matemáticas Básicas"),"matbas-geoanalitica.json")
