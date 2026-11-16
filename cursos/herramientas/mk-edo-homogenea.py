import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 2 Orden superior y coeficientes constantes"
W="sqrt(9-x*x/4)"
TR=[[f"{9.5*k/80:.4f}",f"exp(0-x*{9.5*k/80:.4f}/2)*(cos({W}*{9.5*k/80:.4f})+x/(2*{W})*sin({W}*{9.5*k/80:.4f}))"] for k in range(81)]
ENV1=[[f"{9.5*k/20:.4f}",f"exp(0-x*{9.5*k/20:.4f}/2)"] for k in range(21)]
ENV2=[[f"{9.5*k/20:.4f}",f"0-exp(0-x*{9.5*k/20:.4f}/2)"] for k in range(21)]
graf={"tipo":"plano","x":[-0.5,10],"y":[-2.86,2.86],"a":0,"b":5.5,"inicio":1,
 "elementos":[{"t":"trazo","puntos":ENV1,"c":3,"guia":True},{"t":"trazo","puntos":ENV2,"c":3,"guia":True},{"t":"trazo","puntos":TR,"c":2},{"t":"punto","p":["0","1"],"c":1}],
 "lecturas":[{"rotulo":"amortiguamiento b","formula":"x"},{"rotulo":"frecuencia angular","formula":W}],
 "etiquetas":["Amortiguamiento b","Frecuencia angular de la oscilación"],"etiquetaSlider":"Amortiguamiento b",
 "alt":"La solución de y segunda más b por y prima más 9y igual a 0 con y de 0 igual a 1 y y prima de 0 igual a 0, una oscilación que se apaga más rápido al subir b, entre dos curvas envolventes"}
glos={"caracteristica":"La ecuación característica de y segunda más b por y prima más c por y igual a 0 es r cuadrado más b por r más c igual a 0. Sus raíces r dan las soluciones e a la r x.",
 "amortiguada":"Una oscilación amortiguada es la que se va apagando con el tiempo, como un resorte con fricción.",
 "frecuencia":"La frecuencia angular es la rapidez con que gira la oscilación, en radianes por segundo. El período es 2 pi sobre ella."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación y segunda más b por y prima más 9y igual a 0 describe un resorte con fricción. Esta es su solución, con y de 0 igual a 1."],
 [4,8,"Con poca fricción, el resorte oscila muchas veces. Las curvas punteadas son la envolvente, que baja como e a la menos b t sobre 2."],
 [8,14,"Al subir b, las oscilaciones se apagan más rápido y su frecuencia baja un poco."],
 [14,18,"Con b cerca de 6, casi no oscila. Con b igual a 6 la ecuación característica tiene una raíz doble y el resorte vuelve sin rebotar."],
 [18,22,"Con b igual a 1, las raíces son complejas, menos 0.5 más y menos 2.96 i, y la solución es e a la menos 0.5 x por una combinación de coseno y seno."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.2],[8,1],[10,3],[13,5.5],[14,5.5],[17,1],[22,1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Las ecuaciones de segundo orden con coeficientes constantes describen resortes, circuitos y vibraciones. Se resuelven probando soluciones de la forma e a la r x. Eso lleva a la {{gl:caracteristica|ecuación característica}}, un polinomio cuyas raíces dicen cómo es la solución, si crece, decae u oscila.")),
 sec("Un ejemplo","Un ejemplo",P("Mira un resorte con fricción. La ecuación y su solución con el resorte soltado desde el reposo en y igual a 1."),EQ("y''+b\\,y'+9y=0,\\qquad y(0)=1,\\ y'(0)=0"),{"t":"grafica","animar":"dibujar","alt":"La oscilación amortiguada"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Sin fricción, b igual a 0, la ecuación característica es r cuadrado más 9 igual a 0 y la frecuencia angular es la raíz de 9. ¿Cuánto vale?","opciones":[1,3,6,9],"correcta":3,"bien":"Muy bien. Vale 3. Más abajo se ve cómo baja al subir b.","mal":"Vale 3, la raíz de 9. Más abajo se ve cómo baja al subir b."}),
 sec("Más fricción","Más fricción",P("Mira cómo cambia la oscilación al subir el amortiguamiento b."),{"t":"acercando","ds":[0.2,1,3,5.5],"alt":"La oscilación para varios valores de b"},P("La {{gl:amortiguada|oscilación amortiguada}} se apaga más rápido y su {{gl:frecuencia|frecuencia angular}} baja, porque es la raíz de 9 menos b al cuadrado sobre 4.")),
 sec("La ecuación característica","Característica",P("Se reemplaza y por e a la r x y se divide entre e a la r x."),
   PASOS([("y''-3y'+2y=0,\\quad y=e^{rx}","Una ecuación de ejemplo."),
          ("r^{2}-3r+2=0\\ \\Rightarrow\\ (r-1)(r-2)=0","La ecuación característica."),
          ("r=1,\\ r=2\\ \\Rightarrow\\ y=c_{1}e^{x}+c_{2}e^{2x}","Dos raíces reales distintas dan dos exponenciales.")])),
 sec("Los tres casos","Tres casos",P("Según las raíces de la ecuación característica hay tres formas de solución."),
   PASOS([("r_{1}\\ne r_{2}\\ \\text{reales}\\ \\Rightarrow\\ y=c_{1}e^{r_{1}x}+c_{2}e^{r_{2}x}","Dos raíces reales distintas."),
          ("r\\ \\text{doble}\\ \\Rightarrow\\ y=(c_{1}+c_{2}x)\\,e^{rx}","Una raíz doble. Se agrega el factor x para tener dos soluciones independientes."),
          ("r=\\alpha\\pm\\beta i\\ \\Rightarrow\\ y=e^{\\alpha x}(c_{1}\\cos\\beta x+c_{2}\\operatorname{sen}\\beta x)","Raíces complejas. La parte real da el decaimiento y la imaginaria, la oscilación.")])),
 sec("El caso del ejemplo","El ejemplo",P("Con b igual a 1 la ecuación característica es r cuadrado más r más 9, con raíces complejas."),
   PASOS([("r=\\dfrac{-1\\pm\\sqrt{1-36}}{2}=-\\dfrac{1}{2}\\pm 2.96\\,i","La parte real es menos un medio y la imaginaria es la frecuencia."),
          ("y=e^{-x/2}\\left(c_{1}\\cos 2.96x+c_{2}\\operatorname{sen}2.96x\\right)","Es la forma de la solución. Con las condiciones iniciales se hallan c1 y c2.")]),
   OJO("Con b igual a 6 la raíz es doble y vale menos 3. Con b mayor que 6 hay dos raíces reales negativas y no hay oscilación.")),
 eng("La suspensión de un vehículo","Una rueda con amortiguador se modela como una masa, un resorte y un amortiguador. Su ecuación es de segundo orden con coeficientes constantes, y el amortiguador se escoge para que la rueda no rebote demasiado.","m\\,y''+c\\,y'+k\\,y=0",
   [("Masa","250 kg"),("Rigidez","2250 N/m"),("Amortiguamiento crítico","1500 N·s/m")],"La frecuencia natural es la raíz de k sobre m, o sea 3 radianes por segundo. El amortiguamiento crítico, donde la raíz es doble, es 2 por la raíz de k por m, o sea 1500 newton segundo por metro. Con 750, la mitad, el vehículo todavía oscila un poco al pasar un bache. Es un modelo simplificado, porque supone un resorte y un amortiguador lineales."),
 completar("Se halla la ecuación característica de y segunda menos 3y prima más 2y igual a 0.","r^{2}-3r+2=[[hueco]]",
   [("0","cero"),("1","uno"),("3","tres")],0,
   ["","La ecuación característica se iguala a 0, porque la ecuación original es igual a 0.","Ese 3 es el coeficiente de r en el lado izquierdo y no un valor para igualar. La ecuación característica se iguala a 0."],"Se iguala a 0, igual que la EDO.","La EDO es igual a 0, así que su ecuación característica también."),
 error("Alguien resolvió una ecuación y se equivocó en un paso. Toca el paso que está mal.",
   [("y''+9y=0\\ \\Rightarrow\\ r^{2}+9=0","Es la ecuación característica.","y segunda más 9y igual a 0 da r cuadrado más 9 igual a 0"),
    ("r=\\pm 3i","Las raíces son imaginarias.","Las raíces son más y menos 3i"),
    ("y=c_{1}e^{3x}+c_{2}e^{-3x}","Este paso es el que falla.","y es c1 e a la 3x más c2 e a la menos 3x")],2,
   "Las raíces son imaginarias, no reales. Con r igual a mas o menos beta i la solución es c1 coseno de beta x más c2 seno de beta x. Aquí es c1 coseno de 3x más c2 seno de 3x.",
   "y=c_{1}\\cos 3x+c_{2}\\operatorname{sen}3x","Fíjate si las raíces son reales o imaginarias."),
 ordenar("Estos son los pasos para resolver y segunda más 2y prima más 5y igual a 0, pero están desordenados.",
   [("r^{2}+2r+5=0","La ecuación característica"),
    ("r=-1\\pm 2i","Las raíces con la fórmula cuadrática"),
    ("\\alpha=-1,\\ \\beta=2","La parte real y la imaginaria"),
    ("y=e^{-x}(c_{1}\\cos 2x+c_{2}\\operatorname{sen}2x)","La solución")],[2,0,3,1],
   "Se plantea la ecuación característica, se hallan las raíces complejas y se arma la solución.","Se empieza con la ecuación característica."),
]
S+=cierre("Mini simulacro de ecuaciones homogéneas",[banco("ed_c2_01","La característica es $r^2+r-6=(r-2)(r+3)$, con raíces $2$ y $-3$."),banco("ed_c2_02","La característica es $r^2+4=0$, con raíces $\\pm 2i$."),banco("ed_c2_03","La característica es $(r-3)^2=0$, con raíz doble $3$.")])
prac=[
 {"titulo":"La oscilación","grafica":{"draw":1,"guide":1},"bloques":[P("Un resorte soltado desde el reposo, con fricción b."),EQ("y''+b\\,y'+9y=0")]},
 {"titulo":"Cambia b","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Con más fricción las oscilaciones se apagan antes. Abajo se ven b y la frecuencia angular.")]},
 {"titulo":"Casi sin oscilar","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5.5,"bloques":[EQ("b=6\\ \\Rightarrow\\ r=-3\\ \\text{(doble)}"),P("Con b cerca de 6 casi no hay oscilación. Es el caso del amortiguamiento crítico.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Halla las raíces de la ecuación característica."}]}]
preg={"tex":"y''+4y'+13y=0\\ \\text{oscila con frecuencia angular}","opciones":["$3$","$2$","$13$","$\\sqrt{13}$"],"correcta":0,
 "explicacion":"La ecuación característica es r cuadrado más 4r más 13 igual a 0, con raíces menos 2 más y menos 3i. La parte imaginaria, 3, es la frecuencia angular. La parte real, menos 2, es el decaimiento.",
 "verificacion":{"formula":"sqrt(13-4)+0*x","a":0,"esperado":3},
 "pistas":["Halla las raíces de r cuadrado más 4r más 13 igual a 0.","Salen menos 2 más y menos 3i.","La frecuencia angular es la parte imaginaria."],
 "errores":["","Ese es el decaimiento, la parte real con el signo cambiado. La frecuencia es la parte imaginaria.","Ese es el término constante. La frecuencia sale de la raíz, no del coeficiente.","Esa es la raíz del término constante, y no resta el efecto del 4. La frecuencia es la raíz de 13 menos 4."]}
res=["La ecuación característica se obtiene probando e a la r x.","Raíces reales distintas dan exponenciales, una raíz doble agrega el factor x y raíces complejas dan seno y coseno con una exponencial.","La parte real de la raíz da el decaimiento y la imaginaria da la frecuencia."]
write(lesson("edo-m2-l1","Lección 1 de 4","Homogénea con coeficientes constantes",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Ecuaciones Diferenciales"),"edo-homogenea.json")
