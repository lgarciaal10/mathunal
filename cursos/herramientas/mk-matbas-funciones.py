import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 3 Funciones, trigonometría y geometría analítica"
graf={"tipo":"plano","x":[-7.5,9],"y":[-4,5],"a":-0.5,"b":2,"inicio":1,
 "elementos":[{"t":"recta","p":["0","0"],"dir":["1","1"],"guion":True,"c":3},
  {"t":"recta","p":["0","-2"],"dir":["1","3"],"c":2},
  {"t":"recta","p":["0","2/3"],"dir":["3","1"],"c":0,"guia":True},
  {"t":"segmento","a":["x","3*x-2"],"b":["3*x-2","x"],"c":3,"guia":True,"guion":True},
  {"t":"punto","p":["x","3*x-2"],"c":2},
  {"t":"punto","p":["3*x-2","x"],"c":0,"guia":True}],
 "lecturas":[{"rotulo":"f(a)","formula":"3*x-2"},{"rotulo":"inversa de f(a)","formula":"((3*x-2)+2)/3"}],
 "etiquetas":["Valor de f en a","La inversa lleva ese valor de vuelta a a"],"etiquetaSlider":"Valor de a",
 "alt":"La recta y igual a 3x menos 2, su inversa y igual a x más 2 sobre 3, y la recta y igual a x. Las dos gráficas son reflejos una de la otra respecto a y igual a x. Un punto a, f de a se refleja en f de a, a"}
glos={"dominio":"El dominio de una función es el conjunto de valores de x para los que la función está definida. Hay que excluir los que dividen por cero, dan una raíz de un negativo o un logaritmo de un número no positivo.",
 "inversa":"La función inversa deshace lo que hace f. Si f lleva a en b, la inversa lleva b en a. Solo existe si f no repite valores.",
 "composicion":"La composición de f y g, que se escribe f de g de x, aplica primero g y luego f al resultado."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La recta y igual a 3x menos 2 es la función f. La recta punteada, y igual a x, es el eje de simetría."],
 [4,8,"La inversa deshace lo que hace f. Su gráfica es el reflejo de la de f en la recta y igual a x."],
 [8,14,"Mueve a. El punto de f y su reflejado intercambian la x y la y. Si f lleva a en b, la inversa lleva b en a."],
 [14,18,"Con a igual a 2, f de a es 4, y la inversa de 4 vuelve a 2."],
 [18,22,"Siempre se cumple. La inversa de f de a es a, como se lee abajo."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[11,-0.5],[13,2],[14,2],[22,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Una función asigna a cada x un solo valor. Lo primero que se pregunta es para qué valores está definida, su {{gl:dominio|dominio}}. También se pueden combinar funciones con la {{gl:composicion|composición}}, y deshacerlas con la {{gl:inversa|función inversa}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira una función y su inversa."),EQ("f(x)=3x-2,\\qquad f^{-1}(x)=\\dfrac{x+2}{3}"),{"t":"grafica","animar":"dibujar","alt":"La función y su inversa"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Si f de x es 3x menos 2, ¿cuánto vale f de 2?","opciones":[2,4,6,8],"correcta":4,"bien":"Muy bien. Vale 4. La inversa debe llevar el 4 de vuelta al 2.","mal":"Vale 4, porque 3 por 2 menos 2 es 4. La inversa debe llevar el 4 de vuelta al 2."}),
 sec("La inversa","La inversa",P("Mira cómo se corresponden los puntos de f y de su inversa."),{"t":"acercando","ds":[2,-0.5,1,0],"alt":"Puntos de la función y de su inversa"},P("Los puntos de la inversa tienen las coordenadas intercambiadas. Por eso las dos gráficas son simétricas respecto a la recta y igual a x.")),
 sec("Dominio","Dominio",P("Se buscan los valores que hay que excluir."),
   PASOS([("f(x)=\\sqrt{4-x}\\ \\Rightarrow\\ 4-x\\ge 0\\ \\Rightarrow\\ x\\le 4","Dentro de una raíz cuadrada no puede haber un negativo."),
          ("f(x)=\\dfrac{1}{x^{2}-9}\\ \\Rightarrow\\ x\\ne 3,\\ x\\ne -3","El denominador no puede ser 0."),
          ("f(x)=\\ln(x-1)\\ \\Rightarrow\\ x>1","El argumento de un logaritmo debe ser positivo.")]),
   OJO("El dominio de una suma o de un producto de funciones es la intersección de los dominios de cada una.")),
 sec("Composición e inversa","Composición",P("Para componer, se reemplaza una función dentro de la otra. Para invertir, se intercambian x y y y se despeja."),
   PASOS([("f(x)=x^{2}+1,\\ g(x)=2x\\ \\Rightarrow\\ (f\\circ g)(x)=(2x)^{2}+1=4x^{2}+1","Se reemplaza g dentro de f."),
          ("y=3x-2\\ \\Rightarrow\\ x=3y-2","Se intercambian x y y."),
          ("y=\\dfrac{x+2}{3}\\ \\Rightarrow\\ f^{-1}(x)=\\dfrac{x+2}{3}","Se despeja y.")]),
   OJO("El orden de la composición importa. En general, f de g de x no es igual a g de f de x.")),
 eng("De Celsius a Fahrenheit","La conversión entre grados Celsius y Fahrenheit es una función lineal, y la conversión contraria es su inversa. Es el ejemplo clásico de una pareja de funciones inversas.","F=1.8\\,C+32\\ \\Rightarrow\\ C=\\dfrac{F-32}{1.8}",
   [("Dato del tablero","194 grados Fahrenheit"),("En Celsius","90 grados"),("Congelación del agua","32 grados F")],"Con la función inversa, 194 grados Fahrenheit equivalen a 194 menos 32, o sea 162, dividido entre 1.8, o sea 90 grados Celsius. Si se aplica la conversión y luego su inversa, se vuelve al valor original. Es lo que se ve en la gráfica con las dos rectas simétricas."),
 completar("Se despeja la inversa de f de x igual a 3x menos 2. Ya se intercambiaron x y y.","x=3y-2\\ \\Rightarrow\\ y=\\dfrac{x+[[hueco]]}{3}",
   [("2","dos"),("-2","menos dos"),("3","tres")],0,
   ["","Hay que pasar el menos 2 al otro lado, y pasa sumando.","Con 3 sumando se estaría usando el coeficiente de y, y no el término constante."],"Se suma 2 en los dos lados y se divide entre 3.","El menos 2 pasa sumando."),
 error("Alguien halló el dominio de 1 sobre x al cuadrado menos 16 y se equivocó en un paso. Toca el paso que está mal.",
   [("x^{2}-16\\ne 0","El denominador no puede ser 0.","el denominador no es cero"),
    ("x^{2}\\ne 16\\ \\Rightarrow\\ x\\ne 4","Este paso es el que falla.","x al cuadrado distinto de 16, entonces x distinto de 4"),
    ("\\text{Dominio: todos los reales menos}\\ 4","La conclusión.","el dominio son todos los reales menos 4")],1,
   "La ecuación x al cuadrado igual a 16 tiene dos soluciones, 4 y menos 4. Hay que excluir las dos.",
   "x\\ne 4\\ \\text{y}\\ x\\ne -4","Recuerda que una raíz cuadrada tiene dos signos."),
 ordenar("Estos son los pasos para hallar la inversa de f de x igual a 2x más 6, pero están desordenados.",
   [("y=2x+6","Se escribe y"),
    ("x=2y+6","Se intercambian x y y"),
    ("y=\\dfrac{x-6}{2}","Se despeja y"),
    ("f^{-1}(x)=\\dfrac{x-6}{2}","La inversa")],[2,0,3,1],
   "Se intercambian x y y, se despeja y y se nombra la inversa.","Se empieza escribiendo y."),
]
S+=cierre("Mini simulacro de funciones",[
 banco("mb_c3_01","El radicando debe ser no negativo, $4-x\\ge0$, así que $x\\le4$."),
 banco("mb_c3_03","Se intercambian $x$ y $y$ y se despeja, y queda $f^{-1}(x)=\\dfrac{x+2}{3}$."),
 banco("mb_c3_04","Se reemplaza $g(x)=2x$ dentro de $f$, y queda $(2x)^2+1=4x^2+1$.")])
prac=[
 {"titulo":"Función e inversa","grafica":{"draw":1,"guide":1},"bloques":[P("La recta de f, su reflejo y la recta de simetría."),EQ("f(x)=3x-2")]},
 {"titulo":"Mueve a","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee f de a y lo que devuelve la inversa.")]},
 {"titulo":"Ida y vuelta","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("f(2)=4,\\quad f^{-1}(4)=2"),P("La inversa devuelve el valor original.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"En una composición se calcula primero la función de adentro."}]}]
preg={"tex":"f(x)=2x+1,\\ g(x)=x^{2}.\\ \\text{Entonces}\\ (f\\circ g)(3)\\ \\text{vale}","opciones":["$19$","$49$","$13$","$7$"],"correcta":0,
 "explicacion":"Primero se calcula g de 3, que es 9. Después f de 9 es 2 por 9 más 1, o sea 19.",
 "verificacion":{"formula":"2*(x*x)+1","a":3,"esperado":19},
 "pistas":["En f de g de 3, se calcula primero g.","g de 3 es 9.","Ahora calcula f de 9."],
 "errores":["","Ese es g de f de 3. Se aplicó primero f, pero en f de g el orden es el contrario.","Ese valor sale de calcular g de 3 como 6, duplicando en lugar de elevar al cuadrado. Primero hay que elevar 3 al cuadrado.","Ese es f de 3. Falta aplicar g antes."]}
res=["El dominio excluye los valores que dividen por cero, dan raíces de negativos o logaritmos de números no positivos.","En una composición se aplica primero la función de adentro.","Para invertir se intercambian x y y y se despeja. La gráfica de la inversa es el reflejo en y igual a x."]
write(lesson("mb-m3-l2","Lección 2 de 4","Funciones, dominio, rango e inversa",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=13,curso="Matemáticas Básicas"),"matbas-funciones.json")
