import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 3 Rectas, planos y cónicas"
N=48
EL=[{"t":"trazo","puntos":[[f"5*cos({2*math.pi*k/N:.5f})",f"x*sin({2*math.pi*k/N:.5f})"] for k in range(N+1)],"c":0},
 {"t":"punto","p":["sqrt(25-x*x)","0"],"c":1},
 {"t":"punto","p":["-sqrt(25-x*x)","0"],"c":1},
 {"t":"segmento","a":["0","0"],"b":["sqrt(25-x*x)","0"],"c":3,"guia":True,"guion":True}]
graf={"tipo":"plano","x":[-10.1,10.1],"y":[-5.5,5.5],"a":1,"b":5,"inicio":3,
 "elementos":EL,
 "lecturas":[{"rotulo":"semieje vertical b","formula":"x"},{"rotulo":"distancia c del centro a cada foco","formula":"sqrt(25-x*x)"}],
 "etiquetas":["Semieje vertical de la elipse, con semieje horizontal 5","Distancia del centro a cada foco, c igual a la raíz de 25 menos b al cuadrado"],"etiquetaSlider":"Semieje vertical b",
 "alt":"Una elipse con semieje horizontal 5 y semieje vertical b que se cambia con el deslizador. Dos puntos sobre el eje horizontal marcan los focos, a una distancia c del centro. Con b igual a 5 la elipse es una circunferencia y los focos coinciden"}
glos={"conica":"Las cónicas son las curvas que resultan de cortar un cono con un plano. Son la circunferencia, la elipse, la parábola y la hipérbola.",
 "foco":"Los focos de una elipse son dos puntos tales que la suma de las distancias de cualquier punto de la curva a ellos es constante.",
 "polar":"En coordenadas polares un punto se describe con su distancia r al origen y el ángulo theta que forma con el eje horizontal.",
 "excentricidad":"La excentricidad de una elipse es c entre a. Vale 0 para la circunferencia y se acerca a 1 cuando la elipse es muy alargada."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La elipse tiene semieje horizontal 5 y semieje vertical b. Los focos están sobre el eje horizontal."],
 [4,10,"Los focos están a una distancia c del centro, con c al cuadrado igual a 25 menos b al cuadrado."],
 [10,15,"Con b igual a 3, c vale 4. Es la elipse x al cuadrado sobre 25 más y al cuadrado sobre 9 igual a 1."],
 [15,19,"Con b igual a 5 la elipse es una circunferencia, y los dos focos coinciden en el centro."],
 [19,22,"Cuanto más achatada es la elipse, más lejos del centro están los focos."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,5],[7,4],[10,3],[14,3],[16,5],[19,5],[21,1.5],[22,1.5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[10,15]}}
S=[
 sec("La idea",None,P("Las {{gl:conica|cónicas}} son curvas que se obtienen al cortar un cono. Tienen ecuaciones sencillas. La circunferencia es x al cuadrado más y al cuadrado igual a r al cuadrado, la elipse es x al cuadrado sobre a al cuadrado más y al cuadrado sobre b al cuadrado igual a 1, y la hipérbola tiene un signo menos. La elipse tiene dos {{gl:foco|focos}}. Y con las coordenadas {{gl:polar|polares}} se describen estas curvas desde el origen.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la elipse con semieje horizontal 5 y semieje vertical b, y sus dos focos."),EQ("\\dfrac{x^{2}}{25}+\\dfrac{y^{2}}{b^{2}}=1,\\qquad c=\\sqrt{25-b^{2}}"),{"t":"grafica","animar":"dibujar","alt":"La elipse con sus focos"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En la elipse con semiejes 5 y 3, c es la raíz de 25 menos 9. ¿Cuánto vale c?","opciones":[2,3,4,5],"correcta":4,"bien":"Muy bien. Es la raíz de 16, o sea 4. Más abajo se ve en la gráfica.","mal":"Es la raíz de 16, o sea 4, porque 25 menos 9 es 16. Más abajo se ve en la gráfica."}),
 sec("Cambiando el semieje","El semieje",P("Mira la elipse con b igual a 5, 4, 3 y 1.5."),{"t":"acercando","ds":[5,4,3,1.5],"alt":"La elipse con cuatro valores de b"},P("Con b igual a <b>3</b>, los focos están a 4 del centro. Con b igual a 5 son un solo punto.")),
 sec("Las cónicas","Las cónicas",P("Cada cónica tiene su ecuación estándar."),
   PASOS([("x^{2}+y^{2}=9","Circunferencia de centro el origen y radio 3."),
          ("\\dfrac{x^{2}}{4}+\\dfrac{y^{2}}{9}=1","Elipse con semieje 2 en x y semieje 3 en y."),
          ("\\dfrac{x^{2}}{a^{2}}-\\dfrac{y^{2}}{b^{2}}=1","Hipérbola, con un signo menos."),
          ("y=ax^{2}","Parábola.")]),
   OJO("En la elipse se leen los semiejes como las raíces de los denominadores. El de 4 da el semieje 2, y no 4.")),
 sec("Focos","Los focos",P("Los focos están sobre el eje mayor, a una distancia c del centro."),
   PASOS([("c^{2}=a^{2}-b^{2}","En la elipse, con a mayor que b."),
          ("\\dfrac{x^{2}}{25}+\\dfrac{y^{2}}{9}=1:\\quad c=\\sqrt{25-9}=4","Los focos están en (4, 0) y (menos 4, 0)."),
          ("e=\\dfrac{c}{a}=\\dfrac{4}{5}","La excentricidad mide qué tan alargada es.")])),
 sec("Coordenadas polares","Polares",P("Un punto se puede dar por su distancia al origen y su ángulo."),
   PASOS([("x=r\\cos\\theta,\\qquad y=r\\operatorname{sen}\\theta","Para pasar de polares a cartesianas."),
          ("r=3\\ \\Leftrightarrow\\ x^{2}+y^{2}=9","La circunferencia es la curva más simple en polares."),
          ("(r,\\theta)=(2,60^{\\circ})\\ \\Rightarrow\\ (1,\\sqrt{3})","Un ejemplo de conversión.")]),
   OJO("Un mismo punto tiene varias representaciones en polares, porque el ángulo se puede aumentar en 360 grados sin cambiar el punto.")),
 eng("El reflector elíptico","Una bóveda con forma de elipse tiene dos focos. Cualquier onda que sale de un foco rebota en la pared y llega al otro foco. Con semiejes de 5 y 3 metros, los focos están a 4 metros del centro.","c=\\sqrt{5^{2}-3^{2}}=4",
   [("Semiejes","5 m y 3 m"),("Distancia del centro a cada foco","4 m"),("Distancia entre focos","8 m")],"Quien habla en un foco es oído con claridad en el otro, aunque esté lejos, porque todas las ondas llegan al mismo punto. Se usa en galerías de susurros y en algunos equipos médicos que concentran ondas. Es un modelo geométrico de rayos, que no incluye el efecto de los materiales."),
 completar("Se halla la distancia del centro a los focos de la elipse x al cuadrado sobre 16 más y al cuadrado sobre 7 igual a 1.","c=\\sqrt{16-[[hueco]]}",
   [("7","siete"),("\\sqrt{7}","raíz de siete"),("23","veintitrés")],0,
   ["","El denominador ya es el cuadrado del semieje, así que se resta tal cual.","Se sumó en lugar de restar. Para c se resta el cuadrado del semieje menor."],"Se resta el denominador menor.","16 menos 7 es 9, y c vale 3."),
 error("Alguien leyó los semiejes de una elipse y se equivocó en un paso. Toca el paso que está mal.",
   [("\\dfrac{x^{2}}{4}+\\dfrac{y^{2}}{9}=1","La ecuación.","es una elipse"),
    ("a^{2}=4,\\quad b^{2}=9","Se leen los denominadores.","los denominadores son 4 y 9"),
    ("\\text{Entonces los semiejes son}\\ 4\\ \\text{y}\\ 9","Este paso es el que falla.","los semiejes son 4 y 9")],2,
   "Los denominadores son los cuadrados de los semiejes. Los semiejes son las raíces, o sea 2 y 3.",
   "a=2,\\quad b=3","Los semiejes son las raíces de los denominadores."),
 ordenar("Estos son los pasos para pasar el punto de coordenadas polares (2, 60 grados) a cartesianas, pero están desordenados.",
   [("(r,\\theta)=(2,60^{\\circ})","Se parte del punto en polares"),
    ("x=r\\cos\\theta=2\\cdot\\tfrac12=1","Se calcula x"),
    ("y=r\\operatorname{sen}\\theta=2\\cdot\\tfrac{\\sqrt{3}}{2}=\\sqrt{3}","Se calcula y"),
    ("(x,y)=(1,\\sqrt{3})","Se escribe el resultado")],[2,0,3,1],
   "Se parte de r y theta, se calculan x e y con coseno y seno, y se escribe el punto.","Se empieza con el punto en polares."),
]
S+=cierre("Mini simulacro de cónicas y coordenadas polares",[
 banco("gv_c3_03","El radio al cuadrado es 9, así que $x^2+y^2=9$."),
 banco("gv_c3_17","Con suma de cuadrados sobre denominadores y un igual a 1, es una elipse."),
 banco("gv_c3_19","$c=\\sqrt{25-9}=4$.")])
prac=[
 {"titulo":"La elipse","grafica":{"draw":1},"bloques":[P("Una elipse con semieje horizontal 5 y focos sobre el eje."),EQ("\\dfrac{x^{2}}{25}+\\dfrac{y^{2}}{b^{2}}=1")]},
 {"titulo":"Cambia b","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el semieje b y la distancia c de los focos al centro.")]},
 {"titulo":"Con b igual a 3","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("c=\\sqrt{25-9}=4"),P("Con b igual a 3 los focos están a 4 del centro.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"En polares, r constante es una circunferencia."}]}]
preg={"tex":"\\text{En polares, la curva}\\ r=4\\ \\text{es}","opciones":["una circunferencia de radio 4","una recta","una elipse","un solo punto"],"correcta":0,
 "explicacion":"En polares, r es la distancia al origen. Si r vale siempre 4, todos los puntos están a distancia 4 del origen, y forman una circunferencia de radio 4.",
 "verificacion":{"formula":"sqrt(0*x+16)","a":0,"esperado":4},
 "pistas":["r es la distancia al origen.","Si r es constante, la distancia no cambia.","Todos los puntos están a distancia 4."],
 "errores":["","Una recta exigiría que r cambie con el ángulo.","Una elipse necesita dos semiejes distintos, y aquí la distancia es la misma en todas las direcciones.","Un solo punto sería r igual a 0."]}
res=["Las cónicas son la circunferencia, la elipse, la parábola y la hipérbola, y cada una tiene su ecuación estándar.","En la elipse, los semiejes son las raíces de los denominadores y c al cuadrado es a al cuadrado menos b al cuadrado.","En polares, x es r coseno de theta y y es r seno de theta."]
write(lesson("gv-m3-l3","Lección 3 de 4","Cónicas y coordenadas polares",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-conicas.json")
