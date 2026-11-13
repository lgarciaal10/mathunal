import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 3 Cálculo vectorial"
SS=[round(0.025*i,4) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(s),f"{5*s*s:.5f}"] for s in SS],"c":0},
    {"t":"trazo","puntos":[[str(s),f"{s*s+4*s**4:.5f}"] for s in SS],"c":3},
    {"t":"punto","p":["x","5*x*x"],"c":0},
    {"t":"punto","p":["x","x*x+4*x*x*x*x"],"c":3}]
graf={"tipo":"plano","x":[-0.12,1.2],"y":[-0.5,5.7],"a":0,"b":1,"inicio":0.6,"elementos":EL,
 "lecturas":[{"rotulo":"trabajo acumulado por la recta, 5 s al cuadrado","formula":"5*x*x"},{"rotulo":"trabajo acumulado por la parábola, t al cuadrado más 4 t a la cuarta","formula":"x*x+4*x*x*x*x"}],
 "etiquetas":["Trabajo por el camino recto de 0, 0 a 1, 2","Trabajo por el camino curvo, la parábola y igual a 2 x al cuadrado"],"etiquetaSlider":"Parámetro, de 0 a 1",
 "alt":"El trabajo acumulado del campo F igual a 2x, 2y a lo largo de dos caminos distintos del punto 0, 0 al punto 1, 2. Por el camino recto crece como 5 s al cuadrado, y por la parábola como t al cuadrado más 4 t a la cuarta. Las curvas son distintas en el trayecto, pero las dos terminan en 5, porque el campo es conservativo"}
glos={"campo":"Un campo vectorial asigna un vector a cada punto del plano o del espacio, como la velocidad de un fluido o una fuerza.",
 "linea":"La integral de línea de un campo a lo largo de una curva es el trabajo del campo, y suma F punto dr a lo largo del camino.",
 "conservativo":"Un campo es conservativo si es el gradiente de una función potencial. Su trabajo no depende del camino, solo de los extremos.",
 "potencial":"La función potencial phi cumple que el gradiente de phi es el campo, y el trabajo entre A y B es phi de B menos phi de A."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"El campo F igual a 2x, 2y es el gradiente de la función x al cuadrado más y al cuadrado, así que es conservativo."],
 [4,10,"Se calcula el trabajo del origen al punto 1, 2 por dos caminos, uno recto y otro curvo."],
 [10,16,"Con el parámetro en 0.6, los trabajos acumulados son distintos, porque los caminos recorren distintos tramos."],
 [16,20,"Al llegar al final del camino, los dos trabajos valen 5, que es phi de 1, 2 menos phi de 0, 0."],
 [20,24,"Por eso, si el campo es conservativo, el trabajo solo depende de los extremos, y en una curva cerrada vale cero."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.2],[8,0.2],[10,0.6],[13,0.6],[16,1],[18,1],[24,1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Un {{gl:campo|campo vectorial}} da un vector en cada punto. Su {{gl:linea|integral de línea}} mide el trabajo a lo largo de un camino. Si el campo es {{gl:conservativo|conservativo}}, tiene una función {{gl:potencial|potencial}} y el trabajo solo depende de los extremos, de modo que en una curva cerrada vale cero.")),
 sec("Un ejemplo","Un ejemplo",P("El campo es 2x, 2y y el potencial es x al cuadrado más y al cuadrado. Se recorren dos caminos del origen al punto 1, 2."),EQ("\\mathbf{F}=(2x,2y)=\\nabla\\varphi,\\quad \\varphi=x^{2}+y^{2},\\quad W=\\varphi(1,2)-\\varphi(0,0)=5"),{"t":"grafica","animar":"dibujar","alt":"El trabajo acumulado por dos caminos"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Si el campo es conservativo y la curva es cerrada, ¿cuánto vale el trabajo?","opciones":[0,1,"2 pi","depende del camino"],"correcta":0,"bien":"Muy bien. Vuelve al mismo punto, y la diferencia de potencial es cero.","mal":"Vale cero, porque el punto inicial y el final son el mismo y la diferencia de potencial es cero."}),
 sec("Dos caminos","Caminos",P("Mira el trabajo acumulado con el parámetro en 0.3, 0.6, 0.8 y 1."),{"t":"acercando","ds":[0.3,0.6,0.8,1],"alt":"Los dos trabajos con cuatro valores del parámetro"},P("Las curvas se separan en el trayecto, pero se encuentran en 5 al final.")),
 sec("Trabajo por un camino","Cálculo",P("Se parametriza el camino y se calcula F punto r prima."),
   PASOS([("\\mathbf{r}(t)=(t,2t),\\ 0\\le t\\le1","El camino recto."),
          ("\\mathbf{F}\\cdot\\mathbf{r}'=(2t,4t)\\cdot(1,2)=10t","F evaluado en el camino, por la velocidad."),
          ("W=\\displaystyle\\int_{0}^{1}10t\\,dt=5","El trabajo."),
          ("\\mathbf{r}(t)=(t,2t^{2})\\ \\Rightarrow\\ W=\\displaystyle\\int_{0}^{1}(2t+16t^{3})\\,dt=1+4=5","Por la parábola también da 5.")]),
   OJO("Se reemplaza x y y por sus expresiones en t antes de integrar, para que la integral sea de una variable. No se puede integrar con x y y mezcladas con t.")),
 sec("Cuándo es conservativo","Criterio",P("Hay un criterio sencillo con las derivadas parciales."),
   PASOS([("\\mathbf{F}=(P,Q)\\ \\text{es conservativo}\\ \\Leftrightarrow\\ \\dfrac{\\partial P}{\\partial y}=\\dfrac{\\partial Q}{\\partial x}","En un dominio simplemente conexo."),
          ("\\mathbf{F}=(2x,2y):\\ P_{y}=0=Q_{x}","Se cumple."),
          ("f(A)=2,\\ f(B)=7\\ \\Rightarrow\\ \\displaystyle\\int_{C}\\nabla f\\cdot d\\mathbf{r}=5","El teorema fundamental para integrales de línea."),
          ("\\displaystyle\\oint_{C}\\mathbf{F}\\cdot d\\mathbf{r}=0","En una curva cerrada.")]),
   OJO("El criterio de las derivadas pide un dominio simplemente conexo, sin agujeros. En un dominio con agujero, como el plano sin el origen, puede fallar.")),
 eng("El trabajo de un campo de fuerza","Un campo de fuerza conservativo, como la gravedad, hace un trabajo que solo depende de la altura inicial y la final. No importa si la rampa es recta o curva.","W=\\varphi(B)-\\varphi(A)",
   [("Camino recto","5 J"),("Camino curvo","5 J"),("Curva cerrada","0 J")],"Por eso la energía potencial está bien definida. Con fuerzas de fricción, el campo no es conservativo, y el trabajo sí depende del camino."),
 completar("Si F es el gradiente de phi, el trabajo de A a B es phi de [[hueco]] menos phi de A.","W=\\varphi([[hueco]])-\\varphi(A)",
   [("B","el punto final"),("A","el punto inicial"),("C","la curva")],0,
   ["","El punto inicial ya está restando.","La curva no es un punto donde se evalúe phi."],"El trabajo es el potencial final menos el inicial.","Es B."),
 error("Alguien intentó calcular el trabajo de un campo conservativo y se equivocó. Toca el paso que está mal.",
   [("\\mathbf{F}=\\nabla\\varphi,\\ \\varphi=x^{2}+y^{2}","Hay potencial.","potencial"),
    ("W=\\varphi(1,2)+\\varphi(0,0)=5","Este paso es el que falla.","suma los potenciales"),
    ("W=5","Resultado.","5")],1,
   "El trabajo es la diferencia de potencial, y no la suma. Se resta el valor inicial, aunque aquí phi de 0, 0 vale cero.",
   "W=\\varphi(1,2)-\\varphi(0,0)=5-0","Final menos inicial."),
 ordenar("Estos son los pasos para el trabajo de un campo conservativo, pero están desordenados.",
   [("P_{y}=Q_{x}","Se verifica que es conservativo"),
    ("\\varphi\\ \\text{con}\\ \\nabla\\varphi=\\mathbf{F}","Se halla el potencial"),
    ("\\varphi(B)","Se evalúa en el punto final"),
    ("W=\\varphi(B)-\\varphi(A)","Se resta el valor inicial")],[2,0,3,1],
   "Primero se verifica, luego se halla el potencial, después se evalúa y por último se resta.","Se empieza verificando que sea conservativo."),
]
S+=cierre("Mini simulacro de integrales de línea",[
 banco("cv_c3_04","El potencial del campo 2x, 2y, 2z."),
 banco("cv_c3_06","La integral de línea de un campo conservativo."),
 banco("cv_c3_07","El criterio con las derivadas parciales."),
 banco("cv_c3_08","El trabajo con f de A igual a 2 y f de B igual a 7."),
 banco("cv_c3_09","La integral sobre una curva cerrada.")])
prac=[
 {"titulo":"El campo","grafica":{"draw":1},"bloques":[P("El campo es el gradiente de un potencial."),EQ("\\mathbf{F}=(2x,2y)")]},
 {"titulo":"Recorre los caminos","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen los trabajos acumulados por la recta y por la parábola.")]},
 {"titulo":"Al final","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("1+4=5=5\\cdot1"),P("Al final del camino los dos trabajos valen 5.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El trabajo es la diferencia de potencial."}]}]
preg={"tex":"f(A)=2,\\ f(B)=7.\\ \\displaystyle\\int_{C}\\nabla f\\cdot d\\mathbf{r}\\ \\text{vale}","opciones":["$5$","$9$","$14$","$2$"],"correcta":0,
 "explicacion":"El trabajo es f de B menos f de A, o sea 7 menos 2, que da 5.",
 "verificacion":{"formula":"7-2+0*x","a":0,"esperado":5},
 "pistas":["El campo es un gradiente.","El trabajo es una diferencia de potencial.","Final menos inicial."],
 "errores":["","El 9 es la suma, y no la diferencia.","El 14 es el producto.","El 2 es solo el valor inicial."]}
res=["La integral de línea mide el trabajo de un campo a lo largo de un camino.","Si el campo es conservativo, el trabajo solo depende de los extremos y vale phi de B menos phi de A.","En una curva cerrada, el trabajo conservativo es cero."]
write(lesson("cv-m3-l1","Lección 1 de 5","Campos vectoriales e integrales de línea",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-lineas.json")
