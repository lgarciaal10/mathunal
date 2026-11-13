import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 1 Cálculo diferencial en varias variables"
MS=[round(-5+0.25*i,3) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(m),f"{m/(1+m*m):.6f}"] for m in MS],"c":3},
    {"t":"punto","p":["x","x/(1+x*x)"],"c":0}]
graf={"tipo":"plano","x":[-5.5,5.5],"y":[-0.8,0.8],"a":-5,"b":5,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"pendiente m de la trayectoria, y igual a m por x","formula":"x"},{"rotulo":"valor al que tiende xy sobre x al cuadrado más y al cuadrado","formula":"x/(1+x*x)"}],
 "etiquetas":["Cada trayectoria recta que llega al origen tiene su pendiente","Cada pendiente da su propio valor, y no es el mismo para todas"],"etiquetaSlider":"Pendiente m, de menos 5 a 5",
 "alt":"Una curva que muestra, para cada pendiente m de la recta y igual a m x que llega al origen, el valor al que tiende la expresión xy entre x al cuadrado más y al cuadrado. El valor es m entre 1 más m al cuadrado, y cambia con m, así que no hay un único límite"}
glos={"limite":"El límite de una función de dos variables en un punto existe solo si el valor al que se acerca es el mismo por cualquier trayectoria.",
 "trayectoria":"Una trayectoria es el camino por el que el punto x y se acerca al punto límite, como una recta o una parábola.",
 "dominio":"El dominio de una función de dos variables es el conjunto de puntos del plano donde la expresión tiene sentido.",
 "continua":"Una función es continua en un punto si el límite existe, la función está definida allí y ambos valores coinciden."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se quiere el límite de xy entre x al cuadrado más y al cuadrado cuando el punto tiende al origen."],
 [4,10,"Sobre la recta y igual a m x, la expresión vale siempre m entre 1 más m al cuadrado."],
 [10,16,"Con m igual a 0 vale 0, y con m igual a 1 vale un medio. Son valores distintos."],
 [16,20,"Con m igual a menos 1 da menos un medio, y con m igual a 3 da 0.3."],
 [20,24,"Como el valor depende de la trayectoria, el límite no existe."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,1],[13,1],[16,-1],[18,3],[24,3]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("En una variable, el {{gl:limite|límite}} se acerca por la izquierda y por la derecha. En dos variables hay infinitas {{gl:trayectoria|trayectorias}}. Si dos de ellas dan valores distintos, el límite no existe. Antes de eso se identifica el {{gl:dominio|dominio}}, y la {{gl:continua|continuidad}} pide que el límite y el valor coincidan.")),
 sec("Un ejemplo","Un ejemplo",P("Se estudia el límite en el origen de xy entre x al cuadrado más y al cuadrado. Cambia la pendiente de la trayectoria y mira el valor."),EQ("f(x,y)=\\dfrac{xy}{x^{2}+y^{2}},\\qquad y=mx\\ \\Rightarrow\\ f=\\dfrac{m}{1+m^{2}}"),{"t":"grafica","animar":"dibujar","alt":"El valor del límite por cada pendiente"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Sobre la recta y igual a x, xy entre x al cuadrado más y al cuadrado vale x al cuadrado entre 2 x al cuadrado. ¿Cuánto es?","opciones":["un medio","1","0","2"],"correcta":"un medio","bien":"Muy bien. Es un medio, y es el valor que toma por esa recta.","mal":"Es x al cuadrado entre 2 x al cuadrado, o sea un medio. Es el valor por esa recta."}),
 sec("Varias pendientes","Pendientes",P("Mira el valor con pendientes 0, 1, menos 1 y 3."),{"t":"acercando","ds":[0,1,-1,3],"alt":"El valor por cuatro pendientes"},P("Por el eje x vale 0, por la diagonal vale un medio. Si el límite existiera, serían iguales.")),
 sec("Dos trayectorias","Pasos",P("Basta con encontrar dos caminos con valores distintos para concluir que no hay límite."),
   PASOS([("y=0:\\ \\dfrac{x\\cdot0}{x^{2}+0}=0","Por el eje x."),
          ("y=x:\\ \\dfrac{x^{2}}{2x^{2}}=\\dfrac{1}{2}","Por la diagonal."),
          ("0\\ne\\dfrac{1}{2}","Los valores son distintos."),
          ("\\lim_{(x,y)\\to(0,0)}\\dfrac{xy}{x^{2}+y^{2}}\\ \\text{no existe}","Entonces el límite no existe.")]),
   OJO("Que dos trayectorias den el mismo valor no prueba que el límite exista. Para probar que existe se necesita una cota, como el teorema del sándwich.")),
 sec("Cuando sí existe","Sándwich",P("Con una cota se puede probar que el límite existe."),
   PASOS([("\\left|\\dfrac{x^{2}y}{x^{2}+y^{2}}\\right|\\le|y|","Porque x al cuadrado entre x al cuadrado más y al cuadrado es a lo sumo 1."),
          ("|y|\\to0\\ \\text{cuando}\\ (x,y)\\to(0,0)","La cota tiende a cero."),
          ("\\lim\\dfrac{x^{2}y}{x^{2}+y^{2}}=0","Por el sándwich."),
          ("f(0,0)=0\\ \\Rightarrow\\ f\\ \\text{es continua en el origen}","Si se define así, es continua.")]),
   OJO("El dominio importa. Por ejemplo, el logaritmo de x más y está definido solo donde x más y es positivo, o sea en un semiplano.")),
 eng("Una placa con una lectura ambigua","La temperatura de una placa cerca de un punto se modela con xy entre x al cuadrado más y al cuadrado. Un sensor que se acerca al origen por distintos caminos da valores distintos.","T(x,y)=\\dfrac{xy}{x^{2}+y^{2}}",
   [("Por el eje x","0"),("Por la diagonal","un medio"),("Conclusión","no hay valor límite en el origen")],"Si un modelo físico da límites que dependen del camino, hay una singularidad. En el origen la temperatura no está bien definida, y el modelo no se puede evaluar allí. Se debe revisar el modelo o excluir ese punto."),
 completar("Por la trayectoria y igual a m x, el valor de xy entre x al cuadrado más y al cuadrado es [[hueco]].","\\dfrac{xy}{x^{2}+y^{2}}\\Big|_{y=mx}=[[hueco]]",
   [("\\dfrac{m}{1+m^{2}}","m entre 1 más m al cuadrado"),("\\dfrac{m}{m^{2}}","m entre m al cuadrado"),("m","m")],0,
   ["","Con m al cuadrado en el denominador faltó el 1 de x al cuadrado.","Con m el denominador no queda simplificado."],"Se reemplaza y por m x y se simplifica x al cuadrado.","Queda m entre 1 más m al cuadrado."),
 error("Alguien intentó probar que el límite existe y se equivocó. Toca el paso que está mal.",
   [("y=0\\ \\Rightarrow\\ f\\to0","Por el eje x.","eje x"),
    ("y=x\\ \\Rightarrow\\ f\\to\\tfrac{1}{2}","Por la diagonal.","diagonal"),
    ("\\text{ambos}\\ \\Rightarrow\\ \\text{el limite existe}","Este paso es el que falla.","concluye que existe")],2,
   "Los valores 0 y un medio son distintos, y eso prueba que el límite no existe. Un límite que existe tiene el mismo valor por todas las trayectorias.",
   "0\\ne\\dfrac{1}{2}\\ \\Rightarrow\\ \\text{no existe}","Compara los valores."),
 ordenar("Estos son los pasos para mostrar que un límite en dos variables no existe, pero están desordenados.",
   [("y=0:\\ f\\to0","Se toma una trayectoria"),
    ("y=x:\\ f\\to\\tfrac{1}{2}","Se toma otra"),
    ("0\\ne\\tfrac{1}{2}","Se comparan"),
    ("\\text{el limite no existe}","Se concluye")],[2,0,3,1],
   "Se toman dos trayectorias, se comparan y se concluye.","Se empieza con una trayectoria."),
]
S+=cierre("Mini simulacro de límites en varias variables",[
 banco("cv_c1_03","Sobre la recta y igual a m x el valor es m entre 1 más m al cuadrado, y depende de m."),
 pmcq("¿Cuánto vale el límite de $\\dfrac{x^{2}y}{x^{2}+y^{2}}$ cuando $(x,y)\\to(0,0)$?",["$0$","no existe","$1$","$\\tfrac12$"],0,"La expresión está acotada por el valor absoluto de y, que tiende a cero."),
 pnum("Sobre la trayectoria $y=2x$, el valor al que tiende $\\dfrac{xy}{x^{2}+y^{2}}$ es (decimal, 1 cifra):","0.4",0.01,"Con m igual a 2, m entre 1 más m al cuadrado es 2 entre 5, o sea 0.4.")])
prac=[
 {"titulo":"La expresión","grafica":{"draw":1},"bloques":[P("Se estudia el límite en el origen."),EQ("f(x,y)=\\dfrac{xy}{x^{2}+y^{2}}")]},
 {"titulo":"Cambia la pendiente","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la pendiente y el valor al que tiende la expresión.")]},
 {"titulo":"La diagonal","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("m=1\\ \\Rightarrow\\ \\dfrac{1}{2}"),P("Por la diagonal el valor es un medio, y por el eje x es 0.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Dos valores distintos bastan para que no exista."}]}]
preg={"tex":"\\lim_{(x,y)\\to(0,0)}\\dfrac{xy}{x^{2}+y^{2}}\\ \\text{es}","opciones":["no existe","$0$","$\\tfrac12$","$1$"],"correcta":0,
 "explicacion":"Por el eje x el valor es 0 y por la diagonal es un medio. Como son distintos, el límite no existe.",
 "verificacion":{"formula":"1/(1+1)+0*x","a":0,"esperado":0.5},
 "pistas":["Prueba con y igual a 0.","Prueba con y igual a x.","Compara los dos valores."],
 "errores":["","El 0 es el valor por el eje x, pero no por todas las trayectorias.","Un medio es el valor por la diagonal, pero no por todas las trayectorias.","El 1 no es el valor por ninguna de las trayectorias vistas."]}
res=["Si dos trayectorias dan valores distintos, el límite en dos variables no existe.","Para probar que existe se usa una cota, como el teorema del sándwich.","La función es continua si el límite existe, la función está definida y ambos coinciden."]
write(lesson("cv-m1-l1","Lección 1 de 7","Dominio, límites y continuidad",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-limites.json")
