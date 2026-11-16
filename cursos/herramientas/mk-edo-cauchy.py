import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 2 Orden superior y coeficientes constantes"
XS=[0.2+2.3*k/90 for k in range(91)]
graf={"tipo":"plano","x":[-0.3,2.8],"y":[-1,9],"a":-1,"b":3,"inicio":1,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"exp(x*ln({t:.4f}))"] for t in XS],"c":2},{"t":"punto","p":["1","1"],"c":1}],
 "lecturas":[{"rotulo":"exponente r","formula":"x"},{"rotulo":"r(r-1)-2","formula":"x*(x-1)-2"}],
 "etiquetas":["Exponente r","Valor de r(r-1)-2"],"etiquetaSlider":"Exponente r",
 "alt":"Las funciones x elevado a r para x positivo, que pasan todas por el punto uno uno. Con r igual a 2 y con r igual a menos 1 la expresión r por r menos 1 menos 2 vale cero"}
glos={"cauchyeuler":"Una ecuación de Cauchy-Euler tiene la forma x al cuadrado y segunda más b x y prima más c y igual a 0. El coeficiente de cada derivada es una potencia de x del mismo grado que la derivada.",
 "indicial":"La ecuación indicial sale de reemplazar y igual a x a la r. Es un polinomio en r, y sus raíces dan las soluciones.",
 "ln":"El logaritmo natural de x aparece en la solución cuando la raíz indicial es doble, igual que x aparecía con la raíz doble en coeficientes constantes."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación x al cuadrado por y segunda menos 2y igual a 0 tiene un coeficiente que depende de x. Se prueba con y igual a x elevado a r, para x positivo."],
 [4,8,"Al reemplazar, cada término queda con x a la r, y se llega a r por r menos 1, menos 2, igual a 0."],
 [8,14,"Mueve r y mira la expresión de abajo. Se anula en r igual a 2 y en r igual a menos 1."],
 [14,18,"Con r igual a 2 la solución es x al cuadrado. Con r igual a menos 1 es 1 sobre x."],
 [18,22,"La solución general es c1 por x al cuadrado más c2 sobre x, válida para x positivo."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,2],[12,-1],[16,-1],[18,2],[22,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("En una ecuación de {{gl:cauchyeuler|Cauchy-Euler}} el coeficiente de cada derivada es una potencia de x. Ya no se puede probar con e a la r x. Se prueba con x a la r, porque al derivar baja el exponente y el coeficiente lo vuelve a subir. Todo queda con la misma potencia de x y se llega a una {{gl:indicial|ecuación indicial}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira esta ecuación y una de sus posibles soluciones x a la r. Todas pasan por el punto 1, 1."),EQ("x^{2}y''-2y=0,\\qquad y=x^{r}"),{"t":"grafica","animar":"dibujar","alt":"La función x elevado a r"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Si y es x a la r, entonces x al cuadrado por y segunda es r por (r menos 1) por x a la r. ¿Cuánto vale r por (r menos 1) con r igual a 3?","opciones":[3,6,9,2],"correcta":6,"bien":"Muy bien. Vale 6. Más abajo se ve qué r hacen que todo se anule.","mal":"Vale 6, porque 3 por 2 es 6. Más abajo se ve qué r hacen que todo se anule."}),
 sec("Buscando r","Buscando r",P("Mueve el exponente r y mira cuándo la expresión se anula."),{"t":"acercando","ds":[1,2,-1,3],"alt":"La función para varios valores de r"},P("La expresión r por (r menos 1) menos 2 se anula en r igual a 2 y en r igual a menos 1. Esas son las raíces de la ecuación indicial.")),
 sec("La ecuación indicial","La indicial",P("Se reemplaza y igual a x a la r y se divide entre x a la r."),
   PASOS([("y=x^{r},\\ y'=rx^{r-1},\\ y''=r(r-1)x^{r-2}","Las derivadas."),
          ("x^{2}y''-2y=\\left[r(r-1)-2\\right]x^{r}=0","Cada término queda con x a la r."),
          ("r^{2}-r-2=(r-2)(r+1)=0","La ecuación indicial, con raíces 2 y menos 1."),
          ("y=c_{1}x^{2}+c_{2}x^{-1}","Dos raíces reales distintas dan dos potencias.")])),
 sec("Los tres casos","Tres casos",P("Igual que con coeficientes constantes, hay tres casos, pero con x y con el logaritmo natural de x."),
   PASOS([("r_{1}\\ne r_{2}\\ \\text{reales}\\ \\Rightarrow\\ y=c_{1}x^{r_{1}}+c_{2}x^{r_{2}}","Dos raíces reales distintas."),
          ("r\\ \\text{doble}\\ \\Rightarrow\\ y=(c_{1}+c_{2}\\ln x)\\,x^{r}","Una raíz doble. Se agrega el factor logaritmo natural de x."),
          ("r=\\alpha\\pm\\beta i\\ \\Rightarrow\\ y=x^{\\alpha}\\left[c_{1}\\cos(\\beta\\ln x)+c_{2}\\operatorname{sen}(\\beta\\ln x)\\right]","Raíces complejas.")]),
   OJO("El cambio t igual a logaritmo natural de x convierte la ecuación en una de coeficientes constantes en t. Por eso el logaritmo toma el lugar de x en la tabla de casos de la lección de homogéneas.")),
 eng("El calor en un tubo aislado","La temperatura en una pared cilíndrica depende solo del radio r. En régimen estable cumple r al cuadrado por T segunda más r por T prima igual a 0, una ecuación de Cauchy-Euler. La raíz indicial es doble y vale 0, así que la solución es T igual a c1 más c2 por el logaritmo natural de r.","r^{2}T''+r\\,T'=0",
   [("Radio interior","5 cm a 80 grados"),("Radio exterior","10 cm a 20 grados"),("A 7.5 cm","unos 45 grados")],"Con las dos temperaturas en la pared se halla T igual a menos 179.3 menos 86.6 por el logaritmo natural de r, con r en metros. A 7.5 centímetros la temperatura es de unos 45 grados, y a la mitad geométrica, 7.07 centímetros, es 50. Eso muestra que el aislante no baja la temperatura de forma lineal con el radio. Es un modelo simplificado, porque supone un material uniforme y régimen estable."),
 completar("Si y es x a la r, se calcula x al cuadrado por y segunda.","x^{2}y''=r(r-1)\\,[[hueco]]",
   [("x^{r}","x a la r"),("x^{r-2}","x a la r menos 2"),("x^{r+2}","x a la r más 2")],0,
   ["","y segunda tiene x a la r menos 2, pero al multiplicar por x al cuadrado vuelve a quedar x a la r.","El exponente sube en 2 al multiplicar por x al cuadrado, pero parte de r menos 2, no de r."],"x al cuadrado compensa el x a la menos 2 que sale al derivar dos veces.","Al multiplicar x a la r menos 2 por x al cuadrado queda x a la r."),
 error("Alguien resolvió x al cuadrado y segunda más 5x y prima más 4y igual a 0 y se equivocó en un paso. Toca el paso que está mal.",
   [("y=x^{r}\\ \\Rightarrow\\ r(r-1)+5r+4=0","La ecuación indicial.","la indicial es r por r menos 1, más 5r, más 4"),
    ("r^{2}+4r+4=(r+2)^{2}=0","Se agrupa.","queda r cuadrado más 4r más 4, que es (r más 2) al cuadrado"),
    ("r=-2\\ \\text{(doble)}","La raíz doble.","la raíz es menos 2 doble"),
    ("y=c_{1}x^{-2}+c_{2}x^{-2}","Este paso es el que falla.","y es c1 x a la menos 2 más c2 x a la menos 2")],3,
   "Con la raíz doble, la segunda solución lleva el factor logaritmo natural de x. Las dos potencias iguales se pueden juntar en una sola constante y no dan dos soluciones independientes.",
   "y=(c_{1}+c_{2}\\ln x)\\,x^{-2}","Mira cómo se arma la solución cuando la raíz es doble."),
 ordenar("Estos son los pasos para resolver x al cuadrado por y segunda, más x por y prima, menos 4y igual a 0, pero están desordenados.",
   [("y=x^{r}","La forma que se prueba"),
    ("r(r-1)+r-4=0","La ecuación indicial"),
    ("r^{2}-4=0\\ \\Rightarrow\\ r=\\pm 2","Las raíces"),
    ("y=c_{1}x^{2}+c_{2}x^{-2}","La solución general")],[2,0,3,1],
   "Se prueba x a la r, se llega a la indicial, se hallan las raíces y se arma la solución.","Se empieza con la forma que se prueba."),
]
S+=cierre("Mini simulacro de Cauchy-Euler",[
 banco("ed_c2_05","La ecuación indicial es $(r-2)^2=0$, con raíz doble, y la solución lleva el factor $\\ln x$."),
 banco("ed_c2_19","Se propone $y=x^{r}$ porque cada término queda con la misma potencia de $x$."),
 banco("ed_c2_20","La ecuación indicial es $r(r-1)-2=0$, con raíces $2$ y $-1$, y la positiva es $2$.")])
prac=[
 {"titulo":"Las potencias","grafica":{"draw":1,"guide":1},"bloques":[P("Las funciones x a la r, para x positivo, que pasan por 1, 1."),EQ("x^{2}y''-2y=0")]},
 {"titulo":"Cambia r","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee el valor de r por (r menos 1) menos 2.")]},
 {"titulo":"Una raíz","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("r=2\\ \\Rightarrow\\ r(r-1)-2=0"),P("Con r igual a 2 la expresión vale 0, así que x al cuadrado es solución.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Halla las raíces de la ecuación indicial."}]}]
preg={"tex":"x^{2}y''+xy'+9y=0\\ \\text{(con}\\ x>0\\text{) tiene como solución}","opciones":["$\\cos(3\\ln x)$","$\\cos 3x$","$x^{3}$","$e^{3x}$"],"correcta":0,
 "explicacion":"La ecuación indicial es r por (r menos 1) más r más 9, o sea r cuadrado más 9 igual a 0, con raíces más y menos 3i. Con raíces complejas la solución es x a la parte real por coseno y seno de (parte imaginaria por logaritmo natural de x). Aquí la parte real es 0.",
 "verificacion":{"formula":"x*x*((0-9*cos(3*ln(x))+3*sin(3*ln(x)))/(x*x))+x*(0-3*sin(3*ln(x))/x)+9*cos(3*ln(x))","a":2,"esperado":0},
 "pistas":["Reemplaza y igual a x a la r y halla la ecuación indicial.","Sale r cuadrado más 9 igual a 0.","Las raíces son imaginarias, así que la solución usa seno y coseno del logaritmo natural de x."],
 "errores":["","Ese coseno aparece con coeficientes constantes. Aquí el argumento es el logaritmo natural de x.","Las raíces de r cuadrado más 9 igual a 0 no son reales, así que x elevado a una potencia real no sirve.","Esa exponencial es para coeficientes constantes. En Cauchy-Euler la solución es una potencia de x."]}
res=["En Cauchy-Euler se prueba y igual a x a la r, y se llega a una ecuación indicial en r.","Raíces reales distintas dan dos potencias, una raíz doble agrega el logaritmo natural de x, y raíces complejas dan seno y coseno del logaritmo.","Con t igual a logaritmo natural de x la ecuación se vuelve de coeficientes constantes."]
write(lesson("edo-m2-l4","Lección 4 de 4","Cauchy-Euler",24,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=4,curso="Ecuaciones Diferenciales"),"edo-cauchy.json")
