import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 3 Ecuación de Laplace y variable compleja"
CIRC=[[f"x*cos({k*math.pi/20:.5f})",f"x*sin({k*math.pi/20:.5f})"] for k in range(41)]
EL=[{"t":"trazo","puntos":CIRC,"c":0},
    {"t":"punto","p":["0","0"],"c":3},
    {"t":"punto","p":["1","0"],"c":1}]
IND="(1+(x-1)/(abs(x-1)+0.000001))/2"
graf={"tipo":"plano","x":[-4.4,4.4],"y":[-2.44,2.44],"a":0.3,"b":2.2,"inicio":0.6,"elementos":EL,
 "lecturas":[{"rotulo":"suma de residuos dentro del contorno","formula":"-2+2.71828*"+IND},{"rotulo":"radio r del contorno","formula":"x"}],
 "etiquetas":["Los residuos son menos 2 en z igual a 0 y e en z igual a 1","El contorno es un círculo de radio r, recorrido en sentido positivo"],"etiquetaSlider":"Radio r, de 0.3 a 2.2",
 "alt":"En el plano complejo, un círculo de radio r centrado en el origen, y dos polos de la función, uno en z igual a 0 y otro en z igual a 1. Con r menor que 1 el círculo encierra solo el polo en 0. Con r mayor que 1 encierra los dos"}
glos={"residuo":"El residuo de una función en un polo es el coeficiente de uno entre z menos z cero, en su desarrollo de Laurent.",
 "cauchy":"El teorema integral de Cauchy dice que la integral de una función analítica sobre un contorno cerrado, sin polos adentro, vale cero.",
 "polo":"Un polo es un punto donde la función se hace infinita, de la forma uno entre z menos z cero elevado a un entero positivo.",
 "teoremares":"El teorema de los residuos dice que la integral sobre un contorno cerrado vale 2 pi i por la suma de los residuos de los polos que quedan adentro."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La función tiene dos polos, uno en z igual a 0 y otro en z igual a 1, y se integra sobre un círculo de radio r."],
 [4,10,"Con un radio de 0.5 el círculo solo encierra el polo del origen, y la suma de residuos es menos 2."],
 [10,16,"Con radio 1.5 encierra los dos polos, y la suma de residuos es e menos 2, cerca de 0.72."],
 [16,20,"La integral vale 2 pi i por esa suma, así que cambia al cruzar el polo en z igual a 1."],
 [20,24,"Si no hay polos adentro, la integral es cero. Solo cuentan los polos encerrados."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.6],[8,0.6],[10,1.5],[16,1.5],[18,2.0],[24,2.0]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("El {{gl:cauchy|teorema de Cauchy}} dice que, si la función es analítica adentro y sobre un contorno cerrado, la integral vale cero. Si hay {{gl:polo|polos}} adentro, entonces cuenta el {{gl:residuo|residuo}} de cada uno. El {{gl:teoremares|teorema de los residuos}} da la integral como 2 pi i por la suma de residuos encerrados.")),
 sec("Un ejemplo","Un ejemplo",P("La función tiene polos en 0 y en 1. Cambia el radio del círculo y mira qué polos quedan adentro."),EQ("f(z)=\\dfrac{e^{z}}{z^{2}(z-1)}"),{"t":"grafica","animar":"dibujar","alt":"Un círculo de radio r y los polos de la función"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Una función analítica en todo el plano se integra sobre un círculo, y no tiene polos. ¿Cuánto vale la integral?","opciones":[0,1,"2 pi i","pi"],"correcta":0,"bien":"Muy bien. Sin polos dentro, el teorema de Cauchy da cero.","mal":"Sin polos adentro vale cero, por el teorema de Cauchy. Solo los polos aportan a la integral."}),
 sec("El radio y los polos","Polos",P("Mira el círculo con radios 0.4, 0.9, 1.2 y 2."),{"t":"acercando","ds":[0.4,0.9,1.2,2],"alt":"El contorno con cuatro radios"},P("Con radios 0.4 y 0.9 solo el polo del origen está adentro. Con 1.2 y 2 están los dos.")),
 sec("Calcular el residuo","Residuos",P("Para un polo doble se deriva una vez, y para uno simple se evalúa el resto."),
   PASOS([("\\operatorname{Res}_{z=0}f=\\dfrac{d}{dz}\\left[\\dfrac{e^{z}}{z-1}\\right]_{z=0}","Polo doble en 0, se multiplica por z al cuadrado y se deriva."),
          ("\\dfrac{e^{z}(z-1)-e^{z}}{(z-1)^{2}}\\bigg|_{z=0}=\\dfrac{-1-1}{1}=-2","El valor de la derivada."),
          ("\\operatorname{Res}_{z=1}f=\\dfrac{e^{1}}{1^{2}}=e","Polo simple en 1, se evalúa el resto."),
          ("\\oint_{|z|=1.5}f\\,dz=2\\pi i\\,(e-2)","Con los dos polos adentro.")]),
   OJO("Con el círculo de radio menor que 1, el polo en 1 queda afuera. Entonces la integral es 2 pi i por menos 2, o sea menos 4 pi i.")),
 sec("Los teoremas","Teoremas",P("Estos son los resultados que se usan una y otra vez."),
   PASOS([("\\oint_{C}f\\,dz=0\\quad\\text{si f es analitica adentro}","Teorema de Cauchy."),
          ("\\operatorname{Res}_{z_{0}}\\dfrac{1}{z}=1\\ \\Rightarrow\\ \\oint_{|z|=r}\\dfrac{dz}{z}=2\\pi i","El caso básico."),
          ("\\operatorname{Res}_{z_{0}}\\dfrac{p}{q}=\\dfrac{p(z_{0})}{q'(z_{0})}","Polo simple con p y q."),
          ("\\oint_{C}f\\,dz=2\\pi i\\displaystyle\\sum\\operatorname{Res}","Teorema de los residuos.")]),
   OJO("El contorno debe recorrerse en sentido positivo, o sea antihorario. En sentido contrario la integral cambia de signo.")),
 eng("Una integral real con residuos","La integral de uno entre uno más x al cuadrado, de menos infinito a infinito, se calcula con un semicírculo grande en el plano superior y un solo residuo.","\\displaystyle\\int_{-\\infty}^{\\infty}\\dfrac{dx}{1+x^{2}}=2\\pi i\\cdot\\dfrac{1}{2i}=\\pi",
   [("Polo en el semiplano superior","z igual a i"),("Residuo","uno entre 2i"),("Resultado","pi")],"Este truco convierte integrales reales difíciles en un cálculo de residuos. Se usa en procesamiento de señales y en electromagnetismo, y se complementa con la verificación de que el arco grande no aporta."),
 completar("El residuo de uno entre z en z igual a cero es [[hueco]].","\\operatorname{Res}_{z=0}\\dfrac{1}{z}=[[hueco]]",
   [("1","uno"),("0","cero"),("2\\pi i","dos pi i")],0,
   ["","Con cero se confunde con una función analítica.","Con 2 pi i se confunde el residuo con el valor de la integral."],"El residuo es el coeficiente de uno entre z, que aquí es 1.","Es 1."),
 error("Alguien calculó la integral de uno entre z sobre el círculo de radio 3 y se equivocó. Toca el paso que está mal.",
   [("\\operatorname{Res}_{z=0}\\dfrac{1}{z}=1","El residuo.","el residuo"),
    ("\\oint\\dfrac{dz}{z}=\\operatorname{Res}=1","Este paso es el que falla.","da 1"),
    ("\\text{resultado}=1","Resultado.","1")],1,
   "Falta el factor 2 pi i del teorema de los residuos. La integral es 2 pi i por el residuo, o sea 2 pi i.",
   "\\oint\\dfrac{dz}{z}=2\\pi i\\cdot1=2\\pi i","Multiplica por 2 pi i."),
 ordenar("Estos son los pasos para calcular una integral de contorno con residuos, pero están desordenados.",
   [("z_{1},\\ z_{2},\\dots","Se encuentran los polos"),
    ("z_{k}\\ \\text{dentro de}\\ C","Se eligen los que quedan adentro"),
    ("\\operatorname{Res}_{z_{k}}f","Se calcula cada residuo"),
    ("\\oint_{C}f\\,dz=2\\pi i\\sum\\operatorname{Res}","Se aplica el teorema")],[2,0,3,1],
   "Se hallan los polos, se eligen los de adentro, se calculan los residuos y se aplica el teorema.","Se empieza hallando los polos."),
]
S+=cierre("Mini simulacro de integración compleja",[
 banco("es_c3_21","El teorema de Cauchy."),
 banco("es_c3_22","El residuo de uno entre z."),
 banco("es_c3_24","El teorema de los residuos."),
 banco("es_c3_25","El residuo de un polo simple p entre q.")])
prac=[
 {"titulo":"Los polos","grafica":{"draw":1},"bloques":[P("La función tiene un polo doble en 0 y uno simple en 1."),EQ("f(z)=\\dfrac{e^{z}}{z^{2}(z-1)}")]},
 {"titulo":"Cambia el radio","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la suma de residuos encerrados y el radio.")]},
 {"titulo":"Los dos adentro","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1.5,"bloques":[EQ("-2+e\\approx0.718"),P("Con radio 1.5 están los dos polos, y la suma de residuos es e menos 2.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Solo cuentan los polos dentro del contorno."}]}]
preg={"tex":"\\oint_{|z|=2}\\dfrac{dz}{z}\\ \\text{vale}","opciones":["$2\\pi i$","$0$","$\\pi i$","$4\\pi i$"],"correcta":0,
 "explicacion":"El polo en cero queda dentro del círculo de radio 2, y su residuo es 1. Entonces la integral es 2 pi i por 1.",
 "verificacion":{"formula":"2*pi*1+0*x","a":0,"esperado":6.2832},
 "pistas":["Mira si el polo en cero está dentro del círculo.","El residuo de uno entre z es 1.","Multiplica por 2 pi i."],
 "errores":["","Cero sería si el polo estuviera afuera.","Pi i olvida el factor 2.","4 pi i multiplica de más por el radio."]}
res=["El teorema de Cauchy dice que la integral es cero si no hay polos adentro.","El teorema de los residuos da la integral como 2 pi i por la suma de residuos adentro.","Solo cuentan los polos que quedan dentro del contorno."]
write(lesson("es-m3-l3","Lección 3 de 5","Integración compleja y residuos",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-residuos.json")
