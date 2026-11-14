import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 3 Cálculo vectorial"
CIRC=[[f"x*cos({k*math.pi/20:.5f})",f"x*sin({k*math.pi/20:.5f})"] for k in range(41)]
EL=[{"t":"trazo","puntos":CIRC,"c":0},
    {"t":"vector","a":["x","0"],"b":["x","0.8"],"nombre":"F","c":1},
    {"t":"punto","p":["0","0"],"c":3}]
graf={"tipo":"plano","x":[-4.2,4.2],"y":[-2.5,2.5],"a":0.5,"b":2.4,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"área encerrada por la curva, pi r al cuadrado","formula":"pi*x*x"},{"rotulo":"circulación de F igual a menos y, x, es decir 2 por el área","formula":"2*pi*x*x"}],
 "etiquetas":["La curva es una circunferencia de radio r, recorrida en sentido antihorario","La circulación del campo que gira es el doble del área"],"etiquetaSlider":"Radio r, de 0.5 a 2.4",
 "alt":"Una circunferencia de radio r recorrida en sentido antihorario. El campo F igual a menos y, x gira alrededor del origen, con rotacional 2. Por el teorema de Green, la circulación a lo largo de la curva es la integral doble del rotacional, o sea 2 por el área encerrada, que vale 2 pi r al cuadrado"}
glos={"green":"El teorema de Green convierte una integral de línea sobre una curva cerrada en una integral doble sobre la región que encierra.",
 "positivo":"El sentido positivo de recorrido es el antihorario, que deja la región a la izquierda.",
 "circulacion":"La circulación de un campo es la integral de línea del campo sobre una curva cerrada.",
 "area":"Con campos como menos y sobre 2, x sobre 2 la circulación da el área encerrada, y es una forma de calcular áreas."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Una curva cerrada recorrida en sentido antihorario encierra una región, y el campo menos y, x gira alrededor del origen."],
 [4,10,"El teorema de Green dice que la circulación es la integral doble de Q sub x menos P sub y sobre la región."],
 [10,16,"Con este campo, Q sub x menos P sub y vale 2, así que la circulación es 2 veces el área."],
 [16,20,"Con radio 1 el área es pi, cerca de 3.14, y la circulación es 2 pi, cerca de 6.28."],
 [20,24,"Con radio 2.4 la circulación llega a 36.2. Green cambia un cálculo sobre la frontera por otro sobre la región."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.8],[8,0.8],[10,1],[16,1],[18,2.4],[24,2.4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("El teorema de {{gl:green|Green}} relaciona la {{gl:circulacion|circulación}} de un campo sobre una curva cerrada con una integral doble sobre la región. La curva se recorre en {{gl:positivo|sentido positivo}}, o sea antihorario. Con campos bien escogidos, la circulación da el {{gl:area|área}} encerrada.")),
 sec("Un ejemplo","Un ejemplo",P("El campo menos y, x se integra sobre una circunferencia. Cambia el radio y mira la circulación."),EQ("\\oint_{C}P\\,dx+Q\\,dy=\\iint_{D}\\left(\\dfrac{\\partial Q}{\\partial x}-\\dfrac{\\partial P}{\\partial y}\\right)dA,\\qquad \\oint_{C}-y\\,dx+x\\,dy=2A"),{"t":"grafica","animar":"dibujar","alt":"La circunferencia con su campo de giro"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con P igual a menos y y Q igual a x, ¿cuánto vale Q sub x menos P sub y?","opciones":[2,0,1,-2],"correcta":2,"bien":"Muy bien. Q sub x es 1 y P sub y es menos 1, y la resta da 2.","mal":"Q sub x vale 1 y P sub y vale menos 1, así que la resta da 1 más 1, o sea 2."}),
 sec("Distintos radios","Radios",P("Mira la circulación con radios 0.8, 1, 1.6 y 2.4."),{"t":"acercando","ds":[0.8,1,1.6,2.4],"alt":"La circulación con cuatro radios"},P("La circulación crece con el cuadrado del radio, porque el área también lo hace.")),
 sec("Aplicar Green","Cálculo",P("Se pasa de la curva a la región, y la integral doble es más corta."),
   PASOS([("P=-y,\\quad Q=x","El campo."),
          ("Q_{x}-P_{y}=1-(-1)=2","El integrando de Green."),
          ("\\oint_{C}(-y\\,dx+x\\,dy)=\\displaystyle\\iint_{D}2\\,dA=2\\pi r^{2}","La circulación."),
          ("r=1\\ \\Rightarrow\\ 2\\pi\\approx6.2832","Con el círculo unidad.")]),
   OJO("Si la curva se recorre en sentido horario, la circulación cambia de signo. Revisa siempre el sentido de la curva antes de aplicar el teorema.")),
 sec("Otro ejemplo","Otro",P("Con P igual a 0 y Q igual a x, la circulación es el área."),
   PASOS([("\\oint_{C}x\\,dy","La integral de línea."),
          ("Q=x,\\ P=0\\ \\Rightarrow\\ Q_{x}-P_{y}=1","El integrando."),
          ("\\oint_{C}x\\,dy=\\displaystyle\\iint_{D}dA=\\text{area de }D","Es el área."),
          ("\\text{circulo unidad: }\\pi","Con el círculo unidad.")]),
   OJO("El teorema de Green es el caso en dos dimensiones de los teoremas de Stokes y de la divergencia, que se ven en la última lección.")),
 eng("El planímetro","Un planímetro es un instrumento que calcula el área de una figura recorriendo su borde. Funciona con el teorema de Green, porque la integral de línea de un campo adecuado da el área.","A=\\dfrac{1}{2}\\oint_{C}(-y\\,dx+x\\,dy)",
   [("Entrada","recorrer el contorno"),("Salida","área encerrada"),("Ventaja","no se mide el interior")],"El teorema de Green permite medir áreas de terrenos irregulares recorriendo su perímetro. Es la base de los métodos de topografía con coordenadas de los vértices."),
 completar("Por el teorema de Green, la circulación de P dx más Q dy es la integral doble de Q sub x menos [[hueco]].","\\oint P\\,dx+Q\\,dy=\\iint\\left(Q_{x}-[[hueco]]\\right)dA",
   [("P_{y}","P sub y"),("P_{x}","P sub x"),("Q_{y}","Q sub y")],0,
   ["","P sub x aparece en la divergencia, y no en el rotacional.","Q sub y aparece en la divergencia, y no en el rotacional."],"El rotacional en el plano es Q sub x menos P sub y.","Es P sub y."),
 error("Alguien aplicó Green a menos y dx más x dy sobre el círculo unidad y se equivocó. Toca el paso que está mal.",
   [("P=-y,\\ Q=x","Componentes.","componentes"),
    ("Q_{x}-P_{y}=1-1=0","Este paso es el que falla.","P sub y vale 1"),
    ("\\oint=0","Resultado.","cero")],1,
   "P sub y es la derivada de menos y respecto a y, que vale menos 1. Entonces Q sub x menos P sub y es 1 más 1, o sea 2, y la integral vale 2 pi.",
   "Q_{x}-P_{y}=1-(-1)=2","Cuida el signo de P."),
 ordenar("Estos son los pasos para aplicar el teorema de Green, pero están desordenados.",
   [("P,\\ Q","Se identifican P y Q"),
    ("Q_{x}-P_{y}","Se calcula el integrando"),
    ("\\iint_{D}\\left(Q_{x}-P_{y}\\right)dA","Se plantea la integral doble"),
    ("\\text{valor}","Se calcula")],[2,0,3,1],
   "Se identifican P y Q, se calcula el integrando, se plantea la integral y se calcula.","Se empieza con P y Q."),
]
S+=cierre("Mini simulacro del teorema de Green",[
 banco("cv_c3_03","La integral de x dy sobre el círculo unidad."),
 banco("cv_c3_10","El enunciado del teorema de Green."),
 banco("cv_c3_11","La circulación de menos y dx más x dy."),
 banco("cv_c3_19","Green es un caso bidimensional de otros teoremas.")])
prac=[
 {"titulo":"El campo","grafica":{"draw":1},"bloques":[P("El campo gira alrededor del origen."),EQ("\\mathbf{F}=(-y,x)")]},
 {"titulo":"Cambia el radio","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el área y la circulación.")]},
 {"titulo":"Con r igual a 1","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("A=\\pi,\\quad \\oint=2\\pi"),P("Con r igual a 1 la circulación es el doble del área.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"La curva se recorre en sentido antihorario."}]}]
preg={"tex":"\\displaystyle\\oint_{C}x\\,dy\\ \\text{sobre la circunferencia unidad vale}","opciones":["$\\pi$","$0$","$2\\pi$","$-\\pi$"],"correcta":0,
 "explicacion":"Con P igual a 0 y Q igual a x, Q sub x menos P sub y vale 1. La integral doble de 1 es el área, que es pi.",
 "verificacion":{"formula":"pi*1*1+0*x","a":0,"esperado":3.1416},
 "pistas":["Aplica Green con P igual a 0 y Q igual a x.","El integrando vale 1.","La integral de 1 es el área."],
 "errores":["","Cero sería si el campo fuera conservativo.","2 pi es la circulación de menos y, x, y no la de x dy.","Menos pi sería con el sentido horario."]}
res=["El teorema de Green cambia una integral de línea sobre una curva cerrada por una integral doble de Q sub x menos P sub y.","La curva se recorre en sentido antihorario.","Con el campo menos y, x la circulación es el doble del área."]
write(lesson("cv-m3-l3","Lección 3 de 5","Teorema de Green",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-green.json")
