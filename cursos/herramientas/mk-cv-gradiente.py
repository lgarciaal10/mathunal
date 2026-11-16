import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 1 Cálculo diferencial en varias variables"
R=math.sqrt(5)
CIRC=[[f"{R*math.cos(k*math.pi/20):.4f}",f"{R*math.sin(k*math.pi/20):.4f}"] for k in range(41)]
EL=[{"t":"trazo","puntos":CIRC,"c":3},
    {"t":"vector","a":["2","1"],"b":["3.6","1.8"],"nombre":"∇f","c":1},
    {"t":"vector","a":["2","1"],"b":["2+cos(x)","1+sin(x)"],"nombre":"u","c":0},
    {"t":"punto","p":["2","1"],"c":0}]
graf={"tipo":"plano","x":[-4.2,4.2],"y":[-2.5,2.5],"a":0,"b":6.28,"inicio":0,"elementos":EL,
 "lecturas":[{"rotulo":"derivada direccional, 4 coseno de theta más 2 seno de theta","formula":"4*cos(x)+2*sin(x)"},{"rotulo":"ángulo theta de la dirección u, en grados","formula":"57.2958*x"}],
 "etiquetas":["La derivada direccional es el producto punto del gradiente con u","La dirección u se gira con el deslizador"],"etiquetaSlider":"Ángulo theta, de 0 a 6.28",
 "alt":"Las curvas de nivel de f igual a x al cuadrado más y al cuadrado son circunferencias. En el punto 2, 1 el gradiente, que vale 4, 2 y aquí se dibuja a escala 0.4, apunta hacia afuera, perpendicular a la circunferencia. La flecha u gira alrededor del punto, y la derivada direccional es máxima cuando u apunta como el gradiente"}
glos={"gradiente":"El gradiente de f es el vector de las derivadas parciales. Apunta hacia donde f crece más rápido y es perpendicular a las curvas de nivel.",
 "direccional":"La derivada direccional de f en la dirección u es la razón de cambio de f al moverse en esa dirección, y vale el gradiente por u.",
 "nivel":"Una curva de nivel es el conjunto de puntos donde f toma un valor constante.",
 "unitario":"Un vector unitario es un vector de longitud 1, y la derivada direccional se calcula con una dirección unitaria."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La función es x al cuadrado más y al cuadrado. Sus curvas de nivel son circunferencias, y se mira el punto 2, 1."],
 [4,10,"El gradiente en ese punto es 4, 2. Apunta hacia afuera, perpendicular a la circunferencia."],
 [10,16,"Con la dirección u en el ángulo 0, la derivada direccional vale 4, el producto punto del gradiente con u."],
 [16,20,"Cuando u apunta como el gradiente, la derivada direccional es máxima, y vale 4.47, la magnitud del gradiente."],
 [20,24,"Cuando u va sobre la curva de nivel, la derivada direccional es cero, porque f no cambia."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,0],[13,0],[16,0.4636],[18,0.4636],[20,2.034],[24,2.034]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("El {{gl:gradiente|gradiente}} reúne las derivadas parciales en un vector. Apunta hacia donde f crece más rápido, y es perpendicular a las {{gl:nivel|curvas de nivel}}. La {{gl:direccional|derivada direccional}} mide el cambio de f al avanzar en una dirección dada por un vector {{gl:unitario|unitario}}, y se calcula con un producto punto.")),
 sec("Un ejemplo","Un ejemplo",P("La función es x al cuadrado más y al cuadrado, y el punto es 2, 1. Gira la dirección u y mira la derivada direccional."),EQ("\\nabla f(2,1)=(4,2),\\qquad D_{u}f=\\nabla f\\cdot u=4\\cos\\theta+2\\operatorname{sen}\\theta"),{"t":"grafica","animar":"dibujar","alt":"El gradiente y la dirección u en el punto 2, 1"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Para f igual a x al cuadrado más y al cuadrado, ¿cuál es el gradiente en el punto 1, 2?","opciones":["(2, 4)","(1, 2)","(2, 2)","(4, 2)"],"correcta":"(2, 4)","bien":"Muy bien. Las parciales son 2x y 2y, y en 1, 2 valen 2 y 4.","mal":"El gradiente es 2x, 2y, y en el punto 1, 2 vale 2, 4."}),
 sec("Girar la dirección","Direcciones",P("Mira la derivada direccional con theta igual a 0, 0.46, 1.57 y 2.03."),{"t":"acercando","ds":[0,0.4636,1.57,2.034],"alt":"Cuatro direcciones desde el punto"},P("En 0.46 la derivada es máxima, y en 2.03 es cero.")),
 sec("Calcular el gradiente","Cálculo",P("El gradiente son las parciales, y su magnitud da la máxima razón de cambio."),
   PASOS([("f=x^{2}+y^{2}\\ \\Rightarrow\\ \\nabla f=(2x,\\,2y)","El gradiente."),
          ("\\nabla f(1,2)=(2,4)","Evaluado en 1, 2."),
          ("\\|\\nabla f(3,4)\\|=\\sqrt{6^{2}+8^{2}}=10","Su magnitud en 3, 4."),
          ("D_{u}f=\\nabla f\\cdot u,\\quad u=(1,0)\\ \\Rightarrow\\ D_{u}f=f_{x}","En la dirección del eje x es la parcial respecto a x.")]),
   OJO("La dirección u debe ser unitaria. Si el vector dado no lo es, se divide entre su longitud antes de calcular el producto punto.")),
 sec("Máximo, mínimo y nivel","Extremos",P("El producto punto con u depende del ángulo entre u y el gradiente."),
   PASOS([("D_{u}f=\\|\\nabla f\\|\\cos\\alpha","Donde alfa es el ángulo entre u y el gradiente."),
          ("\\alpha=0\\ \\Rightarrow\\ D_{u}f=\\|\\nabla f\\|","Máximo, hacia el gradiente."),
          ("\\alpha=\\pi\\ \\Rightarrow\\ D_{u}f=-\\|\\nabla f\\|","Mínimo, en sentido contrario."),
          ("\\alpha=\\tfrac{\\pi}{2}\\ \\Rightarrow\\ D_{u}f=0","Sobre la curva de nivel.")]),
   OJO("El gradiente da la dirección del máximo crecimiento, pero no el valor de f. Para saber el valor de f en esa dirección, se reemplaza.")),
 eng("El camino de máximo ascenso","Un robot de exploración sube una colina de altura h de x, y. Para ganar altura lo más rápido posible, avanza en la dirección del gradiente de h.","\\text{dirección}=\\dfrac{\\nabla h}{\\|\\nabla h\\|},\\qquad \\text{pendiente máxima}=\\|\\nabla h\\|",
   [("Gradiente","dirección de máximo ascenso"),("Sobre una curva de nivel","altura constante"),("Magnitud","pendiente más fuerte")],"Este es el mismo principio del descenso por gradiente, que se usa para entrenar modelos de aprendizaje automático. Se avanza en sentido opuesto al gradiente para minimizar una función de error."),
 completar("La derivada direccional de f en la dirección unitaria u es el gradiente [[hueco]] u.","D_{u}f=\\nabla f\\ [[hueco]]\\ u",
   [("\\cdot","el producto punto"),("\\times","el producto cruz"),("+","la suma")],0,
   ["","El producto cruz da un vector, y la derivada direccional es un número.","La suma de un vector con otro da un vector, y no un número."],"Es un número que sale del producto punto.","Es el producto punto."),
 error("Alguien calculó la derivada direccional de f igual a x al cuadrado más y al cuadrado en 1, 2 con u igual a 3, 4 sobre 5, y se equivocó. Toca el paso que está mal.",
   [("\\nabla f(1,2)=(2,4)","Gradiente.","gradiente"),
    ("D_{u}f=(2,4)\\cdot(3,4)=22","Este paso es el que falla.","usa u sin dividir entre 5"),
    ("D_{u}f=22","Resultado.","22")],1,
   "El vector 3, 4 no es unitario, porque su longitud es 5. Se debe usar 3 quintos, 4 quintos, y el resultado es 22 entre 5, o sea 4.4.",
   "D_{u}f=(2,4)\\cdot\\left(\\tfrac{3}{5},\\tfrac{4}{5}\\right)=\\tfrac{22}{5}","Divide el vector entre su longitud."),
 ordenar("Estos son los pasos para calcular una derivada direccional, pero están desordenados.",
   [("\\nabla f=(f_{x},f_{y})","Se calcula el gradiente"),
    ("\\nabla f(P)","Se evalúa en el punto"),
    ("u=\\dfrac{v}{\\|v\\|}","Se hace unitaria la dirección"),
    ("D_{u}f=\\nabla f(P)\\cdot u","Se hace el producto punto")],[2,0,3,1],
   "Primero el gradiente, luego el punto, después la dirección unitaria y al final el producto punto.","Se empieza con el gradiente."),
]
S+=cierre("Mini simulacro de gradiente y derivada direccional",[
 banco("cv_c1_02","El gradiente de x al cuadrado más y al cuadrado en 1, 2."),
 banco("cv_c1_09","La magnitud del gradiente en 3, 4."),
 banco("cv_c1_10","La dirección del máximo crecimiento."),
 banco("cv_c1_11","La derivada direccional con gradiente 3, 4 y u igual a 1, 0.")])
prac=[
 {"titulo":"El punto","grafica":{"draw":1},"bloques":[P("Se estudia la función en el punto 2, 1."),EQ("f=x^{2}+y^{2},\\quad P=(2,1)")]},
 {"titulo":"Gira u","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la derivada direccional y el ángulo de u.")]},
 {"titulo":"Hacia el gradiente","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.4636,"bloques":[EQ("D_{u}f=\\|\\nabla f\\|=\\sqrt{20}\\approx4.47"),P("Con u hacia el gradiente, la derivada direccional es máxima.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.4636},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El máximo es la magnitud del gradiente."}]}]
preg={"tex":"\\nabla f(P)=(3,4),\\ u=\\left(\\tfrac{3}{5},\\tfrac{4}{5}\\right).\\ D_{u}f\\ \\text{vale}","opciones":["$5$","$7$","$1$","$\\tfrac{7}{5}$"],"correcta":0,
 "explicacion":"El producto punto es 3 por 3 quintos más 4 por 4 quintos, o sea 25 quintos, que es 5. Es la magnitud del gradiente porque u apunta como el gradiente.",
 "verificacion":{"formula":"3*3/5+4*4/5+0*x","a":0,"esperado":5},
 "pistas":["Haz el producto punto.","Multiplica componente por componente.","Suma los dos productos."],
 "errores":["","El 7 es la suma 3 más 4, y no el producto punto.","El 0 sería con u perpendicular al gradiente. El 1 no sale de este producto punto.","El 7 quintos mezcla mal los términos."]}
res=["El gradiente es el vector de derivadas parciales, apunta hacia el máximo crecimiento y es perpendicular a las curvas de nivel.","La derivada direccional es el gradiente por u, con u unitario.","El máximo de la derivada direccional es la magnitud del gradiente."]
write(lesson("cv-m1-l5","Lección 5 de 7","Gradiente y derivada direccional",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-gradiente.json")
