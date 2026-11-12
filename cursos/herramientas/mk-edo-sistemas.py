import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 3 Laplace, sistemas y series"
N=120
TS=[10.0*k/N for k in range(N+1)]
ORB=[[f"exp(x*{t:.4f})*cos({t:.4f})",f"exp(x*{t:.4f})*sin({t:.4f})"] for t in TS]
CIR=[[f"cos({t:.4f})",f"sin({t:.4f})"] for t in [2*math.pi*k/60 for k in range(61)]]
graf={"tipo":"plano","x":[-4.03,4.03],"y":[-2.2,2.2],"a":-0.5,"b":0.3,"inicio":0,
 "elementos":[{"t":"trazo","puntos":CIR,"c":3,"guia":True},{"t":"trazo","puntos":ORB,"c":2},{"t":"punto","p":["1","0"],"c":1}],
 "lecturas":[{"rotulo":"parte real a","formula":"x"},{"rotulo":"radio tras una vuelta","formula":"exp(2*pi*x)"}],
 "etiquetas":["Parte real a","Radio después de una vuelta"],"etiquetaSlider":"Parte real a",
 "alt":"La trayectoria del sistema x prima igual a a por x menos y, y prima igual a x más a por y, que parte de uno cero. Con a negativa se enrolla hacia el origen, con a cero es un círculo y con a positiva se aleja"}
glos={"sistema":"Un sistema lineal x prima igual a A x describe varias cantidades que cambian y se influyen entre sí. A es una matriz de números.",
 "planofase":"El plano de fase dibuja las trayectorias del sistema, con una cantidad en cada eje. No muestra el tiempo, muestra por dónde pasa la solución.",
 "propios":"Los valores propios de A, las raíces de su ecuación característica, deciden la forma de las trayectorias."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"El sistema x prima igual a A x, con A igual a la matriz con a, menos 1, 1, a, describe dos cantidades que se influyen. Esta es la trayectoria que parte de 1, 0 cuando a vale 0."],
 [4,8,"Los valores propios de A son a más i y a menos i. La parte imaginaria da el giro y la parte real decide si la trayectoria se encoge o se aleja."],
 [8,14,"Con a negativa la trayectoria se enrolla hacia el origen, una espiral estable. Con a positiva se aleja, una espiral inestable."],
 [14,18,"Con a igual a 0 los valores propios son imaginarios puros y la trayectoria es un círculo. Es un centro."],
 [18,22,"Con a igual a menos 0.2, después de una vuelta el radio queda en 0.28, y el origen es un sumidero."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,-0.4],[12,0.25],[14,0],[16,0],[17,-0.2],[22,-0.2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Un {{gl:sistema|sistema lineal}} x prima igual a A x tiene varias incógnitas que dependen unas de otras. Su solución se dibuja en el {{gl:planofase|plano de fase}}. Los {{gl:propios|valores propios}} de la matriz A dicen si las trayectorias se acercan al origen, se alejan, giran o hacen una mezcla de esas cosas.")),
 sec("Un ejemplo","Un ejemplo",P("Mira un sistema con giro. La solución que parte de 1, 0 se dibuja como una curva en el plano."),EQ("\\mathbf{x}'=\\begin{pmatrix}a&-1\\\\1&a\\end{pmatrix}\\mathbf{x},\\qquad \\mathbf{x}(0)=\\begin{pmatrix}1\\\\0\\end{pmatrix}"),{"t":"grafica","animar":"dibujar","alt":"La trayectoria en el plano de fase"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Una matriz diagonal con 1 y menos 1 tiene como valores propios 1 y menos 1. ¿Cuánto vale su producto, que es el determinante?","opciones":[-1,0,1,2],"correcta":-1,"bien":"Muy bien. Vale menos 1. Cuando es negativo, los valores propios tienen signos opuestos.","mal":"Vale menos 1, porque 1 por menos 1 es menos 1. Cuando es negativo, los valores propios tienen signos opuestos."}),
 sec("Cambia la parte real","Parte real",P("Mira cómo cambia la trayectoria al variar a."),{"t":"acercando","ds":[0,-0.4,0.25,-0.2],"alt":"La trayectoria para varios valores de a"},P("La parte real de los valores propios es a. Si es negativa, el origen atrae. Si es positiva, repele. Si es 0, las trayectorias dan vueltas sin acercarse ni alejarse.")),
 sec("Valores propios","Valores propios",P("Se buscan las raíces de la ecuación característica de A."),
   PASOS([("\\det(A-\\lambda I)=(a-\\lambda)^{2}+1=0","Se desarrolla el determinante de la matriz A menos lambda por la identidad."),
          ("\\lambda=a\\pm i","Dos valores propios complejos."),
          ("\\mathbf{x}(t)=e^{at}\\begin{pmatrix}\\cos t\\\\ \\operatorname{sen}t\\end{pmatrix}","La solución que parte de 1, 0. El factor exponencial viene de la parte real y el giro de la imaginaria.")])),
 sec("Clasificación","Clasificación",P("La forma del origen se lee de los valores propios."),
   PASOS([("\\lambda_{1},\\lambda_{2}\\ \\text{reales}<0\\ \\Rightarrow\\ \\text{nodo estable}","Todas las trayectorias entran al origen."),
          ("\\lambda_{1}>0>\\lambda_{2}\\ \\Rightarrow\\ \\text{punto silla}","Unas trayectorias entran y otras salen. Es inestable."),
          ("\\lambda=\\alpha\\pm\\beta i\\ \\Rightarrow\\ \\alpha<0\\ \\text{espiral estable},\\ \\alpha>0\\ \\text{inestable},\\ \\alpha=0\\ \\text{centro}","Con parte imaginaria hay giro.")]),
   OJO("Un origen es estable si todos los valores propios tienen parte real negativa. Con parte real 0 las trayectorias no se acercan al origen, aunque tampoco se alejan.")),
 eng("Dos tanques conectados","Dos tanques de agua con sal están conectados entre sí y reciben agua limpia. Las concentraciones x1 y x2 cumplen un sistema lineal, y los valores propios dicen qué tan rápido se limpian los tanques.","\\mathbf{x}'=\\begin{pmatrix}-0.3&0.1\\\\0.1&-0.3\\end{pmatrix}\\mathbf{x}",
   [("Valores propios","menos 0.2 y menos 0.4"),("Tipo de origen","nodo estable"),("Modo lento","mitad en unas 3.5 horas")],"Los valores propios son menos 0.3 más y menos 0.1, o sea menos 0.2 y menos 0.4 por hora. Los dos son negativos, así que ambos tanques se limpian. A largo plazo domina el modo lento, e a la menos 0.2 t, y la concentración baja a la mitad en ln 2 sobre 0.2, unas 3.5 horas. Es un modelo simplificado, porque supone mezcla perfecta en cada tanque y caudales constantes."),
 completar("Se hallan los valores propios de la matriz con filas 0, menos 1 y 1, 0. La ecuación característica es lambda al cuadrado más 1 igual a 0.","\\lambda=[[hueco]]",
   [("\\pm i","imaginarios"),("\\pm 1","reales"),("0","cero")],0,
   ["","Con lambda al cuadrado igual a menos 1, no hay raíces reales.","Con lambda igual a 0 no se cumple, porque sale 1 y no 0."],"Se despeja lambda al cuadrado igual a menos 1.","Las raíces cuadradas de menos 1 son más y menos i."),
 error("Alguien clasificó el origen de x prima igual a A x, con A diagonal con menos 1 y 2, y se equivocó en un paso. Toca el paso que está mal.",
   [("A=\\begin{pmatrix}-1&0\\\\0&2\\end{pmatrix}\\ \\Rightarrow\\ \\lambda=-1,\\ 2","Una matriz diagonal tiene como valores propios sus entradas.","los valores propios son menos 1 y 2"),
    ("\\lambda_{1}<0<\\lambda_{2}","Tienen signos opuestos.","los valores propios tienen signos opuestos"),
    ("\\text{es un nodo estable}","Este paso es el que falla.","es un nodo estable")],2,
   "Con signos opuestos el origen es un punto silla, que es inestable. Un nodo estable pide que los dos valores propios sean negativos.",
   "\\text{es un punto silla}","Fíjate en los signos de los valores propios."),
 ordenar("Estos son los pasos para clasificar el origen del sistema con matriz de filas menos 2, 1 y 1, menos 2, pero están desordenados.",
   [("(-2-\\lambda)^{2}-1=0","El determinante de A menos lambda I"),
    ("\\lambda^{2}+4\\lambda+3=0","Se desarrolla"),
    ("\\lambda=-1,\\ \\lambda=-3","Las raíces"),
    ("\\text{ambos negativos}\\ \\Rightarrow\\ \\text{nodo estable}","La clasificación")],[2,0,3,1],
   "Se plantea el determinante, se desarrolla, se hallan las raíces y se clasifica con sus signos.","Se empieza con el determinante."),
]
S+=cierre("Mini simulacro de sistemas lineales",[
 banco("ed_c3_05","Los valores propios son $1$ y $-1$, de signos opuestos, así que el origen es un punto silla."),
 banco("ed_c3_13","El origen es un sumidero cuando todos los valores propios tienen parte real negativa.")])
prac=[
 {"titulo":"La trayectoria","grafica":{"draw":1,"guide":1},"bloques":[P("Un sistema con giro, que parte de 1, 0."),EQ("\\mathbf{x}'=\\begin{pmatrix}a&-1\\\\1&a\\end{pmatrix}\\mathbf{x}")]},
 {"titulo":"Cambia a","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Con a negativa la trayectoria se enrolla hacia el origen. Abajo se lee el radio después de una vuelta.")]},
 {"titulo":"Un sumidero","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":-0.2,"bloques":[EQ("a=-0.2\\ \\Rightarrow\\ \\text{espiral estable}"),P("Con a igual a menos 0.2 el radio se reduce a 0.28 en cada vuelta.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":-0.2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Halla los valores propios y mira su parte real."}]}]
preg={"tex":"\\mathbf{x}'=\\begin{pmatrix}0&2\\\\-2&0\\end{pmatrix}\\mathbf{x}\\ \\text{tiene en el origen}","opciones":["un centro","una espiral estable","un punto silla","un nodo inestable"],"correcta":0,
 "explicacion":"La ecuación característica es lambda al cuadrado más 4 igual a 0, con valores propios más y menos 2i. Son imaginarios puros, así que las trayectorias son cerradas y el origen es un centro.",
 "verificacion":{"formula":"0*0-4*(0*0-2*(0-2))","a":0,"esperado":-16},
 "pistas":["Halla los valores propios con el determinante de A menos lambda I.","Sale lambda al cuadrado más 4 igual a 0.","Los valores propios son más y menos 2i, sin parte real."],
 "errores":["","Para una espiral estable la parte real debe ser negativa. Aquí es 0.","Un punto silla pide valores propios reales de signos opuestos. Aquí son imaginarios.","Un nodo pide valores propios reales. Aquí son imaginarios y hay giro."]}
res=["Un sistema lineal x prima igual a A x se estudia con los valores propios de A.","Valores propios reales negativos dan un nodo estable, reales de signos opuestos dan una silla, y complejos dan una espiral o un centro.","El origen es estable cuando todos los valores propios tienen parte real negativa."]
write(lesson("edo-m3-l4","Lección 4 de 5","Sistemas lineales y plano fase",30,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=6,curso="Ecuaciones Diferenciales"),"edo-sistemas.json")
