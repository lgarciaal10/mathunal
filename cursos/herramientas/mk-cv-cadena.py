import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 1 Cálculo diferencial en varias variables"
TS=[round(0.05*i,3) for i in range(30)]
EL=[{"t":"trazo","puntos":[[str(t),f"{t**5:.5f}"] for t in TS],"c":0},
    {"t":"recta","p":["x","x*x*x*x*x"],"dir":["1","5*x*x*x*x"],"c":1},
    {"t":"punto","p":["x","x*x*x*x*x"],"c":1}]
graf={"tipo":"plano","x":[-0.2,1.5],"y":[-0.6,6],"a":0,"b":1.4,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"derivada por la cadena, f sub x por x prima más f sub y por y prima","formula":"2*x*x*x*x+3*x*x*x*x"},{"rotulo":"valor de z igual a x por y, que es t a la 5","formula":"x*x*x*x*x"}],
 "etiquetas":["La pendiente de la tangente es dz entre dt, y se calcula con la regla de la cadena","El valor de z a lo largo de la curva"],"etiquetaSlider":"Tiempo t, de 0 a 1.4",
 "alt":"La función z igual a x por y, evaluada a lo largo de la curva x igual a t al cuadrado y y igual a t al cubo, es z igual a t a la quinta. La recta tangente en cada t tiene pendiente igual a la regla de la cadena, que es 5 por t a la cuarta"}
glos={"cadena":"La regla de la cadena en varias variables suma, para cada variable, la derivada parcial por la derivada de esa variable respecto a t.",
 "compuesta":"Una función compuesta en varias variables es una función z igual a f de x y, donde x y y dependen de otra variable t.",
 "arbol":"El diagrama de árbol dibuja las dependencias, y cada camino de z a t da un término de la regla de la cadena.",
 "implicita":"La derivación implícita calcula dy entre dx de una ecuación F de x y igual a cero con la fórmula menos F sub x entre F sub y."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La función es z igual a x por y, y x y y dependen del tiempo t, con x igual a t al cuadrado y y igual a t al cubo."],
 [4,10,"La regla de la cadena suma dos caminos, y vale f sub x por x prima más f sub y por y prima."],
 [10,16,"Con t igual a 1, f sub x es y igual a 1 y x prima es 2. Luego f sub y es x igual a 1 y y prima es 3. La suma da 5."],
 [16,20,"En general da 5 t a la cuarta, que es la derivada de t a la quinta, y coincide."],
 [20,24,"La regla de la cadena permite derivar sin hacer la composición completa."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.5],[8,0.5],[10,1],[13,1],[16,1.2],[18,1.2],[24,1.2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Cuando z depende de x y y, y estas dependen de t, la {{gl:cadena|regla de la cadena}} suma un término por cada variable intermedia. La {{gl:compuesta|función compuesta}} se puede derivar sin reemplazar todo, y el {{gl:arbol|diagrama de árbol}} ayuda a no olvidar caminos. Con una ecuación implícita se usa la regla de la {{gl:implicita|derivación implícita}}.")),
 sec("Un ejemplo","Un ejemplo",P("La función es z igual a x por y con x igual a t al cuadrado y y igual a t al cubo. Mueve t y mira la pendiente."),EQ("\\dfrac{dz}{dt}=f_{x}\\,\\dfrac{dx}{dt}+f_{y}\\,\\dfrac{dy}{dt}=y\\cdot2t+x\\cdot3t^{2}=5t^{4}"),{"t":"grafica","animar":"dibujar","alt":"La función de t y su tangente"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con z igual a x por y, ¿cuánto vale f sub x?","opciones":["y","x","1","x por y"],"correcta":"y","bien":"Muy bien. Se deriva respecto a x y y queda constante.","mal":"f sub x es y, porque al derivar respecto a x, y se trata como constante."}),
 sec("A lo largo de la curva","Pendiente",P("Mira la pendiente con t igual a 0.5, 1, 1.2 y 1.4."),{"t":"acercando","ds":[0.5,1,1.2,1.4],"alt":"La pendiente en cuatro valores de t"},P("Con t igual a 1 la pendiente es 5, y crece rápido después.")),
 sec("La regla","Regla",P("Se suman los caminos, y cada uno multiplica dos derivadas."),
   PASOS([("z=f(x,y),\\ x=x(t),\\ y=y(t)","Las dependencias."),
          ("\\dfrac{dz}{dt}=\\dfrac{\\partial f}{\\partial x}\\dfrac{dx}{dt}+\\dfrac{\\partial f}{\\partial y}\\dfrac{dy}{dt}","La regla de la cadena."),
          ("f=xy,\\ x=t^{2},\\ y=t^{3}","El ejemplo."),
          ("\\dfrac{dz}{dt}=y(2t)+x(3t^{2})=t^{3}(2t)+t^{2}(3t^{2})=5t^{4}","El resultado.")]),
   OJO("En el resultado, x y y se reemplazan por sus expresiones en t, para que la respuesta quede en una sola variable.")),
 sec("Derivación implícita","Implícita",P("La regla de la cadena da una fórmula corta para dy entre dx cuando y está definida por una ecuación."),
   PASOS([("F(x,y)=0","La ecuación."),
          ("\\dfrac{dy}{dx}=-\\dfrac{F_{x}}{F_{y}}","La fórmula, con F sub y distinta de cero."),
          ("F=x^{2}+y^{2}-25","Una circunferencia."),
          ("\\dfrac{dy}{dx}=-\\dfrac{2x}{2y}=-\\dfrac{x}{y}","La pendiente en cada punto.")]),
   OJO("La fórmula exige F sub y distinta de cero. Donde F sub y vale cero la tangente es vertical, y dy entre dx no existe.")),
 eng("Cambio de temperatura de un dron","Un dron vuela por una región donde la temperatura es T de x y y. Su posición cambia con el tiempo, y se quiere saber cómo cambia la temperatura que mide.","\\dfrac{dT}{dt}=T_{x}\\,\\dfrac{dx}{dt}+T_{y}\\,\\dfrac{dy}{dt}",
   [("T sub x","cambio por metro hacia el este"),("dx entre dt","velocidad hacia el este"),("Resultado","cambio de temperatura por segundo")],"La regla de la cadena combina el mapa de temperatura con la trayectoria del dron. Es la base para controlar sensores y para el descenso por gradiente en optimización."),
 completar("Con z igual a f de x, y, la derivada de z respecto a t es f sub x por dx entre dt más [[hueco]].","\\dfrac{dz}{dt}=f_{x}\\dfrac{dx}{dt}+[[hueco]]",
   [("f_{y}\\dfrac{dy}{dt}","f sub y por dy entre dt"),("f_{y}\\dfrac{dx}{dt}","f sub y por dx entre dt"),("f_{xy}","f sub xy")],0,
   ["","Cada derivada parcial se multiplica por la derivada de su propia variable.","La derivada mixta no aparece en la regla de la cadena."],"Cada camino aporta un término.","Falta el camino por y."),
 error("Alguien derivó z igual a x por y con x igual a t al cuadrado y y igual a t al cubo, y se equivocó. Toca el paso que está mal.",
   [("z=xy,\\ x=t^{2},\\ y=t^{3}","Datos.","datos"),
    ("\\dfrac{dz}{dt}=y\\cdot2t","Este paso es el que falla.","falta el camino por y"),
    ("\\dfrac{dz}{dt}=2t^{4}","Resultado.","2 t a la 4")],1,
   "Faltó el segundo camino, el de y. La regla suma y por 2t más x por 3t al cuadrado, y da 5t a la cuarta.",
   "\\dfrac{dz}{dt}=y(2t)+x(3t^{2})=5t^{4}","Suma los dos caminos."),
 ordenar("Estos son los pasos para aplicar la regla de la cadena, pero están desordenados.",
   [("f_{x},\\ f_{y}","Se calculan las derivadas parciales"),
    ("x',\\ y'","Se derivan x y y respecto a t"),
    ("f_{x}x'+f_{y}y'","Se arma la suma"),
    ("\\text{todo en terminos de }t","Se reemplaza x y y por sus expresiones")],[2,0,3,1],
   "Primero las parciales, luego x prima y y prima, después la suma y al final todo en términos de t.","Se empieza con las derivadas parciales."),
]
S+=cierre("Mini simulacro de la regla de la cadena",[
 banco("cv_c1_12","La regla de la cadena para z de x, y con x y y que dependen de t."),
 pnum("Con $z=x^{2}y$, $x=t$ y $y=t^{2}$, el valor de $\\dfrac{dz}{dt}$ en $t=1$ es:","4",0.01,"z es t a la 4, y su derivada es 4 t al cubo, o sea 4 en t igual a 1."),
 pmcq("Si $x^{2}+y^{2}=25$, entonces $\\dfrac{dy}{dx}$ vale:",["$-\\dfrac{x}{y}$","$\\dfrac{x}{y}$","$-\\dfrac{y}{x}$","$-2x$"],0,"Con F igual a x al cuadrado más y al cuadrado menos 25, menos F sub x entre F sub y es menos x entre y.")])
prac=[
 {"titulo":"La curva","grafica":{"draw":1},"bloques":[P("Se evalúa f a lo largo de la curva."),EQ("z=xy,\\quad x=t^{2},\\quad y=t^{3}")]},
 {"titulo":"Mueve t","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la pendiente por la regla de la cadena y el valor de z.")]},
 {"titulo":"En t igual a 1","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("\\dfrac{dz}{dt}=1\\cdot2+1\\cdot3=5"),P("Con t igual a 1, f sub x vale 1, x prima vale 2, f sub y vale 1 y y prima vale 3.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Se suma un término por cada variable."}]}]
preg={"tex":"z=xy,\\ x=t^{2},\\ y=t^{3}.\\ \\dfrac{dz}{dt}\\Big|_{t=1}\\ \\text{vale}","opciones":["$5$","$2$","$3$","$6$"],"correcta":0,
 "explicacion":"La regla da y por 2t más x por 3 t al cuadrado. En t igual a 1, es 2 más 3, o sea 5.",
 "verificacion":{"formula":"1*2+1*3+0*x","a":0,"esperado":5},
 "pistas":["Calcula f sub x y f sub y.","Multiplica cada una por la derivada de su variable.","Suma los dos términos."],
 "errores":["","El 2 es solo el primer camino, y falta el segundo.","El 3 es solo el segundo camino, y falta el primero.","El 6 es el producto de 2 y 3, y no la suma."]}
res=["La regla de la cadena suma un término por cada variable intermedia.","Se multiplica cada derivada parcial por la derivada de su variable respecto a t.","En una ecuación implícita, dy entre dx es menos F sub x entre F sub y."]
write(lesson("cv-m1-l4","Lección 4 de 7","Regla de la cadena",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-cadena.json")
