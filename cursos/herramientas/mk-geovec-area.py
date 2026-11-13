import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 1 Vectores y rectas en el plano"
graf={"tipo":"plano","x":[-3.5,11.5],"y":[-3.0,5.2],"a":-2,"b":6,"inicio":1,
 "elementos":[
  {"t":"poligono","puntos":[["0","0"],["3","0"],["3+x","2"],["x","2"]],"c":3},
  {"t":"vector","b":["3","0"],"nombre":"u","c":0},
  {"t":"vector","b":["x","2"],"nombre":"v","c":1}],
 "lecturas":[{"rotulo":"área del paralelogramo","formula":"abs(3*2-0*x)"},{"rotulo":"longitud de v","formula":"sqrt(x*x+4)"}],
 "etiquetas":["Valor absoluto del determinante de u y v","Longitud del lado inclinado"],"etiquetaSlider":"Primera componente de v",
 "alt":"Un paralelogramo formado por el vector u igual a (3, 0) y el vector v igual a (x, 2). Al mover el deslizador el paralelogramo se inclina, pero su base y su altura no cambian, así que el área siempre vale 6"}
glos={"paralelogramo":"El paralelogramo de dos vectores es la figura de cuatro lados que ellos forman. Su área es el valor absoluto del determinante de los vectores.",
 "determinante":"El determinante de dos vectores del plano es u1 por v2 menos u2 por v1. Su valor absoluto es el área del paralelogramo.",
 "orientacion":"El signo del determinante indica la orientación. Es positivo si v queda a la izquierda de u, y negativo si queda a la derecha.",
 "triangulo":"El triángulo formado por dos vectores tiene la mitad del área del paralelogramo."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"El paralelogramo está formado por u igual a (3, 0) y v igual a (x, 2)."],
 [3,9,"Al mover x, el lado v se inclina, pero la base sigue valiendo 3 y la altura sigue valiendo 2."],
 [9,15,"El área es base por altura, 3 por 2, que da 6, aunque el paralelogramo se incline."],
 [15,19,"El determinante u1 por v2 menos u2 por v1 da lo mismo, 3 por 2 menos 0 por x, o sea 6."],
 [19,22,"El triángulo con los mismos lados tiene la mitad del área, es decir, 3."]],
 "canales":{"draw":[[0.3,0],[2.8,1]],"d":[[3,1],[6,3],[9,5],[12,-2],[15,1],[19,1],[22,1]],"guide":[[3,0],[4,1]]},
 "intervalos":{"ok":[15,22]}}
S=[
 sec("La idea",None,P("Dos vectores del plano forman un {{gl:paralelogramo|paralelogramo}}. Su área se calcula con el {{gl:determinante|determinante}} de las componentes, y el signo de ese determinante dice la {{gl:orientacion|orientación}}. Con eso se calculan áreas de triángulos y de terrenos a partir de las coordenadas de los vértices.")),
 sec("Un ejemplo","Un ejemplo",P("Mira el paralelogramo de u igual a (3, 0) y v igual a (x, 2). Al mover x se inclina, pero el área no cambia."),EQ("A=\\left|u_{1}v_{2}-u_{2}v_{1}\\right|=\\left|3\\cdot2-0\\cdot x\\right|=6"),{"t":"grafica","animar":"dibujar","alt":"El paralelogramo de u y v"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El paralelogramo tiene base 3 y altura 2. ¿Cuánto vale su área?","opciones":[5,6,8,12],"correcta":6,"bien":"Muy bien. Es base por altura, o sea 6. Más abajo se ve que no cambia al inclinarlo.","mal":"Es base por altura, 3 por 2, o sea 6. Más abajo se ve que no cambia al inclinarlo."}),
 sec("Inclinando el paralelogramo","Inclinando",P("Mira el paralelogramo para x igual a menos 2, 1, 3 y 5."),{"t":"acercando","ds":[-2,1,3,5],"alt":"El paralelogramo con cuatro inclinaciones"},P("Aunque cambia la forma, la base y la altura son las mismas, y el área sigue siendo 6.")),
 sec("El determinante como área","Determinante",P("El área sale de un determinante de dos por dos."),
   PASOS([("A=|u_{1}v_{2}-u_{2}v_{1}|","El valor absoluto del determinante."),
          ("u=(3,0),\\ v=(1,2):\\quad |3\\cdot2-0\\cdot1|=6","Con el ejemplo del banco."),
          ("u=(2,1),\\ v=(1,3):\\quad |6-1|=5","Otro paralelogramo, con área 5."),
          ("u_{1}v_{2}-u_{2}v_{1}=0\\ \\Rightarrow\\ u\\parallel v","Si el área es cero, los vectores son paralelos y el paralelogramo se aplasta en un segmento.")]),
   OJO("El signo del determinante se pierde al tomar valor absoluto. Antes de eso sirve para saber si v está a la izquierda o a la derecha de u.")),
 sec("Triángulos y terrenos","Triángulos",P("Un triángulo es la mitad de un paralelogramo."),
   PASOS([("A_{\\triangle}=\\tfrac12\\left|u_{1}v_{2}-u_{2}v_{1}\\right|","El área del triángulo es la mitad."),
          ("(0,0),\\ (4,0),\\ (0,3):\\quad \\tfrac12|4\\cdot3-0\\cdot0|=6","Un triángulo recto de catetos 4 y 3."),
          ("(0,0),\\ (40,0),\\ (10,30):\\quad \\tfrac12|40\\cdot30|=600","Un terreno de 600 metros cuadrados.")]),
   OJO("Para un triángulo con un vértice fuera del origen, primero se restan las coordenadas de ese vértice para obtener los dos vectores de los lados.")),
 eng("El área de un terreno triangular","Un terreno tiene vértices en (0, 0), (40, 0) y (10, 30), con las medidas en metros. Sus lados desde el origen son los vectores (40, 0) y (10, 30), y el área es la mitad del valor absoluto de su determinante.","A=\\tfrac12\\left|40\\cdot30-0\\cdot10\\right|=600",
   [("Vértices","(0,0), (40,0), (10,30)"),("Determinante","1200"),("Área","600 m²")],"El determinante da 1200 y el área es la mitad, 600 metros cuadrados. Esta forma es cómoda en topografía, porque solo usa las coordenadas de los vértices, sin necesidad de medir alturas. Con más vértices se divide el terreno en triángulos y se suman las áreas."),
 completar("Se calcula el área del paralelogramo de u igual a (3, 0) y v igual a (1, 2). Falta el resultado.","A=|3\\cdot2-0\\cdot1|=[[hueco]]",
   [("6","seis"),("5","cinco"),("3","tres")],0,
   ["","Cinco saldría de sumar en lugar de restar, o de usar otros números. Aquí 3 por 2 es 6 y 0 por 1 es 0.","Tres es el área del triángulo, la mitad del paralelogramo."],"Calcula 3 por 2 menos 0 por 1.","El determinante es 6 y su valor absoluto es 6."),
 error("Alguien calculó el área de un triángulo de lados u igual a (3, 0) y v igual a (1, 2) y se equivocó en un paso. Toca el paso que está mal.",
   [("u=(3,0),\\quad v=(1,2)","Son los dos vectores.","los lados son estos"),
    ("u_{1}v_{2}-u_{2}v_{1}=6","El determinante.","el determinante vale 6"),
    ("\\text{Entonces el área del triángulo es}\\ 6","Este paso es el que falla.","el área del triángulo es 6")],2,
   "El determinante da el área del paralelogramo, que es 6. El triángulo es la mitad, o sea 3.",
   "A_{\\triangle}=\\tfrac12\\cdot6=3","Recuerda cuántos triángulos caben en un paralelogramo."),
 ordenar("Estos son los pasos para calcular el área del paralelogramo de u igual a (3, 0) y v igual a (1, 2), pero están desordenados.",
   [("u_{1}v_{2}-u_{2}v_{1}","Se arma el determinante"),
    ("3\\cdot2-0\\cdot1","Se sustituyen las componentes"),
    ("6","Se calcula"),
    ("A=|6|=6","Se toma el valor absoluto")],[2,0,3,1],
   "Se arma el determinante, se sustituye, se calcula y se toma el valor absoluto.","Se empieza armando el determinante."),
]
S+=cierre("Mini simulacro de área y aplicaciones",[
 banco("gv_c1_12","El área es el valor absoluto de $3\\cdot2-0\\cdot1=6$."),
 num("El área del triángulo de vértices $(0,0)$, $(4,0)$ y $(0,3)$ es:","6",0.001,"Es la mitad del determinante, o sea $\\tfrac12\\cdot12=6$."),
 mcq("El área del paralelogramo de $\\mathbf{u}=(1,2)$ y $\\mathbf{v}=(3,1)$ es:",["$5$","$7$","$1$","$-5$"],0,"El determinante es $1\\cdot1-2\\cdot3=-5$, y el área es su valor absoluto, $5$.")])
prac=[
 {"titulo":"El paralelogramo","grafica":{"draw":1},"bloques":[P("Un paralelogramo de lados u y v."),EQ("A=|u_{1}v_{2}-u_{2}v_{1}|")]},
 {"titulo":"Inclina v","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el área y la longitud del lado inclinado.")]},
 {"titulo":"Mismo área","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5,"bloques":[EQ("A=|3\\cdot2-0\\cdot x|=6"),P("Con cualquier x el área vale 6, porque la base y la altura no cambian.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Calcula el determinante y toma su valor absoluto."}]}]
preg={"tex":"\\text{Área del paralelogramo de}\\ (2,1)\\ \\text{y}\\ (1,3)","opciones":["$5$","$7$","$6$","$1$"],"correcta":0,
 "explicacion":"El determinante es 2 por 3 menos 1 por 1, o sea 6 menos 1, que da 5. Su valor absoluto es 5.",
 "verificacion":{"formula":"abs(2*3-1*1)+0*x","a":0,"esperado":5},
 "pistas":["Calcula 2 por 3 menos 1 por 1.","Da 5.","El valor absoluto de 5 es 5."],
 "errores":["","Siete sale de sumar 6 y 1. Hay que restar.","Seis es solo el primer producto. Falta restar 1 por 1.","Uno es solo el segundo producto. Falta el primero y la resta."]}
res=["El área del paralelogramo de dos vectores es el valor absoluto de su determinante.","El área del triángulo es la mitad, y se puede calcular con las coordenadas de los vértices.","Un determinante cero indica vectores paralelos, y el signo indica la orientación."]
write(lesson("gv-m1-l4","Lección 4 de 4","Área y aplicaciones",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-area.json")
