import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 1 EDO de primer orden"
XR=[-3.4,3.4]; YR=[-1.85,1.85]
EL=campo(lambda x,y:-(2*x+y)/(x+2*y) if abs(x+2*y)>0.15 else None,XR,YR,17,9,0.14)
PTS=[]
for k in range(73):
    th=round(2*math.pi*k/72,6)
    PTS.append([f"cos({th})*sqrt(x/(1+sin({th})*cos({th})))",f"sin({th})*sqrt(x/(1+sin({th})*cos({th})))"])
EL+=[{"t":"trazo","puntos":PTS,"c":2},{"t":"punto","p":["sqrt(x)","0"],"c":1,"nombre":"cruza el eje"}]
graf={"tipo":"plano","x":XR,"y":YR,"a":0.5,"b":3,"inicio":1.5,"elementos":EL,
 "lecturas":[{"rotulo":"C","formula":"x"},{"rotulo":"x donde cruza el eje","formula":"sqrt(x)"}],
 "etiquetas":["Constante C","Cruce con el eje x"],"etiquetaSlider":"Valor de la constante C",
 "alt":"El campo de pendientes de la ecuación exacta y las curvas de nivel x cuadrado más x y más y cuadrado igual a C, que son elipses y siguen la dirección de los segmentos"}
glos={"exacta":"Una ecuación M dx más N dy igual a 0 es exacta si M y N son las derivadas parciales de una misma función psi, o sea si la derivada de M con respecto a y es igual a la de N con respecto a x.",
 "potencial":"La función potencial psi es la que cumple que su derivada con respecto a x es M y con respecto a y es N. Las soluciones son sus curvas de nivel, psi igual a una constante.",
 "integrante":"El factor integrante es una función que, al multiplicar una ecuación no exacta, la vuelve exacta."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación (2x más y) dx más (x más 2y) dy igual a 0 da en cada punto la dirección de la solución. Los segmentos son esas direcciones."],
 [4,9,"Las soluciones son curvas que siguen los segmentos. Aquí son elipses, curvas de nivel de una función psi."],
 [9,15,"Al cambiar la constante C, la curva crece. Cada C es una solución distinta."],
 [15,19,"La función es psi igual a x cuadrado más x y más y cuadrado. Su derivada con respecto a x es 2x más y y con respecto a y es x más 2y."],
 [19,22,"Por eso la ecuación es exacta. Con C igual a 1.5, la elipse cruza el eje x en 1.22."]],
 "canales":{"draw":[[0.3,0],[4,1]],"d":[[4,1.5],[9,0.6],[12,2.8],[15,1.5],[22,1.5]]},
 "intervalos":{"ok":[19,22]}}
S=[
 sec("La idea",None,P("Una ecuación escrita como M dx más N dy igual a 0 es {{gl:exacta|exacta}} si viene de una función {{gl:potencial|potencial}} psi de x y, con M igual a la derivada parcial de psi con respecto a x y N igual a la de psi con respecto a y. Entonces sus soluciones son las curvas de nivel de psi. Esta idea es la misma de las fuerzas conservativas y los campos de gradiente.")),
 sec("Un ejemplo","Un ejemplo",P("Mira esta ecuación. Sus soluciones son curvas cerradas."),EQ("(2x+y)\\,dx+(x+2y)\\,dy=0"),{"t":"grafica","animar":"dibujar","alt":"El campo de direcciones y una curva solución"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La solución cruza el eje x en x igual a la raíz de C. Con C igual a 4, ¿cuánto vale x?","opciones":[1,2,4,16],"correcta":2,"bien":"Muy bien. Vale 2. Más abajo se ve la curva.","mal":"Vale 2, porque la raíz de 4 es 2. Más abajo se ve la curva."}),
 sec("Curvas de nivel","Curvas de nivel",P("Mira cómo cambia la solución con la constante."),{"t":"acercando","ds":[0.6,1.5,2.8],"alt":"La curva solución para varios valores de C"},P("Cada curva es una solución. Pasan una sola por cada punto, y todas siguen las direcciones del campo.")),
 sec("Reconocer una exacta","Reconocer",EQ("\\dfrac{\\partial M}{\\partial y}=\\dfrac{\\partial N}{\\partial x}"),
   PASOS([("M=2x+y,\\quad N=x+2y","Se identifican M y N."),
          ("\\dfrac{\\partial M}{\\partial y}=1,\\quad \\dfrac{\\partial N}{\\partial x}=1","Las derivadas cruzadas son iguales, así que es exacta."),
          ("\\dfrac{\\partial M}{\\partial y}\\ne\\dfrac{\\partial N}{\\partial x}\\ \\Rightarrow\\ \\text{no es exacta}","Si no coinciden, no hay función potencial.")])),
 sec("Hallar la potencial","Hallar psi",PASOS([("\\psi_{x}=2x+y\\ \\Rightarrow\\ \\psi=x^{2}+xy+g(y)","Se integra M con respecto a x. La constante de integración puede depender de y."),
          ("\\psi_{y}=x+g'(y)=x+2y\\ \\Rightarrow\\ g'(y)=2y\\ \\Rightarrow\\ g=y^{2}","Se deriva con respecto a y y se compara con N."),
          ("\\psi=x^{2}+xy+y^{2}=C","La solución es la curva de nivel.")]),
   OJO("Al integrar M con respecto a x no se suma una constante, sino una función g de y. Olvidarlo es el error más común.")),
 sec("Factor integrante","Factor integrante",P("Si no es exacta, a veces se arregla multiplicando por un {{gl:integrante|factor integrante}}."),
   PASOS([("y\\,dx-x\\,dy=0\\ \\text{no es exacta}","Las derivadas cruzadas son 1 y menos 1."),
          ("\\mu=\\dfrac{1}{y^{2}}\\ \\Rightarrow\\ \\dfrac{dx}{y}-\\dfrac{x}{y^{2}}\\,dy=0","Al multiplicar queda exacta."),
          ("\\psi=\\dfrac{x}{y}=C","La solución son rectas por el origen.")])),
 eng("Un campo de fuerzas conservativo","Una fuerza que viene de una energía potencial, F igual a menos el gradiente de U, es conservativa, y la función ψ de abajo es menos U. El trabajo no depende del camino, y las trayectorias de energía constante son las curvas de nivel. Reconocerla es revisar si la ecuación es exacta.","\\mathbf{F}=(2x+y,\\ x+2y)=\\nabla\\psi,\\quad \\psi=x^{2}+xy+y^{2}",
   [("Fuerza","(2x + y, x + 2y)"),("Punto inicial","(0, 0)"),("Punto final","(1, 1)")],"Como F sale de psi, el trabajo de (0, 0) a (1, 1) es psi de (1, 1) menos psi de (0, 0), o sea 3 menos 0, igual a 3 julios, por cualquier camino. Es un modelo simplificado, porque supone una fuerza que depende solo de la posición."),
 completar("Se halla la función potencial integrando M igual a 2x más y con respecto a x. Falta la parte que depende de y.","\\psi=x^{2}+xy+[[hueco]]",
   [("g(y)","g de y"),("C","C"),("0","cero")],0,
   ["","La constante C aparece al final, en psi igual a C. Aquí hace falta una función de y, porque al derivar con respecto a x desaparece.","No se puede poner 0. Hay que sumar una función de y, que se halla después con N."],"Al integrar con respecto a x, lo que depende solo de y se perdió.","La constante de integración puede depender de y, y se llama g de y."),
 error("Alguien resolvió una ecuación exacta y se equivocó en un paso. Toca el primer paso donde aparece el error.",
   [("M=2x+y,\\quad N=x+2y,\\quad M_{y}=N_{x}=1","Es exacta.","M es 2x más y, N es x más 2y, y las derivadas cruzadas son 1"),
    ("\\psi=\\int M\\,dx=x^{2}+xy+C","Este paso es el que falla.","Psi es x al cuadrado más x y más C"),
    ("\\psi=x^{2}+xy+C=0","Depende del paso anterior.","Psi es x al cuadrado más xy más C igual a 0")],1,
   "Al integrar M con respecto a x falta la función g de y, no una constante. Si se deriva con respecto a y, aparece x más g prima de y, y eso debe ser igual a x más 2y. Entonces g es y al cuadrado.",
   "\\psi=x^{2}+xy+g(y),\\ g'(y)=2y\\ \\Rightarrow\\ \\psi=x^{2}+xy+y^{2}","Deriva psi con respecto a y y compáralo con N."),
 ordenar("Estos son los pasos para resolver (2x más y) dx más (x más 2y) dy igual a 0, pero están desordenados.",
   [("M_{y}=N_{x}=1","Se comprueba que es exacta"),
    ("\\psi=x^{2}+xy+g(y)","Se integra M con respecto a x"),
    ("g'(y)=2y\\ \\Rightarrow\\ g=y^{2}","Se compara con N"),
    ("x^{2}+xy+y^{2}=C","Es la solución")],[2,0,3,1],
   "Se comprueba, se integra M, se halla g con N y se escribe la solución.","Primero se comprueba que es exacta."),
]
S+=cierre("Mini simulacro de ecuaciones exactas",[banco("ed_c1_12","Es la condición de exactitud."),banco("ed_c1_04","$M=2xy$ y $N=x^2$ tienen $M_y=N_x=2x$, así que es exacta y $\\psi=x^2y$."),banco("ed_c1_13","Las derivadas cruzadas son $M_y=2x$ y $N_x=2x$.")])
prac=[
 {"titulo":"Las curvas","grafica":{"draw":1},"bloques":[P("Las soluciones son curvas de nivel."),EQ("x^{2}+xy+y^{2}=C")]},
 {"titulo":"Cambia C","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La elipse crece con C y siempre sigue los segmentos del campo. Abajo se ven C y el cruce con el eje x.")]},
 {"titulo":"Una solución","grafica":{"draw":1,"ok":True},"laboratorio":True,"d":1.5,"bloques":[EQ("\\psi(x,y)=C,\\quad \\psi_{x}=2x+y,\\ \\psi_{y}=x+2y"),P("Con C igual a 1.5 la curva cruza el eje x en 1.22.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"ok":True,"d":1.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Comprueba que es exacta, integra M y halla g con N."}]}]
preg={"tex":"(3x^{2}+y)\\,dx+(x+2y)\\,dy=0","encabezado":"La solución general de (3x al cuadrado más y) dx más (x más 2y) dy igual a 0 es:","opciones":["$x^{3}+xy+y^{2}=C$","$x^{3}+xy=C$","$x^{3}+2xy+y^{2}=C$","$3x^{2}+xy+y^{2}=C$"],"correcta":0,
 "explicacion":"Las derivadas cruzadas son 1 y 1, así que es exacta. Al integrar M con respecto a x queda x al cubo más x y más g de y. Al derivar con respecto a y, x más g prima, que debe valer x más 2y, y entonces g es y al cuadrado.",
 "pistas":["Comprueba las derivadas cruzadas de M y N.","Integra 3x al cuadrado más y con respecto a x.","Deriva el resultado con respecto a y y compáralo con x más 2y."],
 "errores":["","Falta la parte con y al cuadrado. Al derivar con respecto a y solo sale x, no x más 2y.","El término xy aparece con coeficiente 1, no 2. La derivada con respecto a x debe dar 3x al cuadrado más y.","Esa no es la integral de 3x al cuadrado. Al integrar con respecto a x se obtiene x al cubo."]}
res=["Una ecuación M dx más N dy es exacta si las derivadas parciales cruzadas, M con respecto a y y N con respecto a x, son iguales.","Se halla psi integrando M con respecto a x, sumando una función g de y, y comparando con N. La solución es psi igual a una constante.","Si no es exacta, a veces un factor integrante la vuelve exacta."]
write(lesson("edo-m1-l4","Lección 4 de 6","Exactas y factor integrante",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Ecuaciones Diferenciales"),"edo-exactas.json")
