import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
from fundlib import *
MOD="Módulo 1 Errores y ecuaciones no lineales"
X=[1.0]
for _ in range(4): X.append(X[-1]-(X[-1]**2-2)/(2*X[-1]))
X1=X[1:]+[X[-1]]
ERR=[abs(x-math.sqrt(2)) for x in X]
LX=lagr([round(v,9) for v in X]); LX1=lagr([round(v,9) for v in X1]); LE=lagr([round(v,9) for v in ERR])
EL=[{"t":"trazo","puntos":[[str(round(0.6+0.05*k,2)),str(round((0.6+0.05*k)**2-2,4))] for k in range(0,37)],"c":0},
 {"t":"recta","p":["("+LX+")","("+LX+")*("+LX+")-2"],"dir":["1","2*("+LX+")"],"c":1},
 {"t":"segmento","a":["("+LX+")","0"],"b":["("+LX+")","("+LX+")*("+LX+")-2"],"c":3,"guia":True,"guion":True},
 {"t":"punto","p":["("+LX+")","("+LX+")*("+LX+")-2"],"c":2},
 {"t":"punto","p":["("+LX1+")","0"],"c":3}]
graf={"tipo":"plano","x":[0.4,2.4],"y":[-2.2,2.8],"a":0,"b":4,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"aproximación x de n","formula":"("+LX+")"},{"rotulo":"error, distancia a la raíz de 2","formula":"("+LE+")"}],
 "etiquetas":["Aproximación de la raíz en la iteración elegida","Error absoluto, que baja muy rápido"],"etiquetaSlider":"Iteración, de 0 a 4",
 "alt":"La curva y igual a x al cuadrado menos 2. En cada iteración se traza la tangente en el punto de la aproximación, y donde esa tangente cruza el eje horizontal queda la siguiente aproximación. Parte de x igual a 1 y llega a 1.4142 en pocas iteraciones"}
glos={"newton":"El método de Newton aproxima la raíz de f con la recta tangente. La siguiente aproximación es donde la tangente cruza el eje.",
 "cuadratica":"La convergencia es cuadrática si el error de una iteración es proporcional al cuadrado del error anterior. Las cifras correctas se duplican en cada paso.",
 "secante":"El método de la secante reemplaza la derivada por la pendiente de la recta que pasa por las dos aproximaciones anteriores.",
 "multiplicidad":"Una raíz tiene multiplicidad m si f y sus derivadas hasta la m menos 1 se anulan en ella. Con m mayor que 1, Newton converge solo linealmente."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se busca la raíz de x al cuadrado menos 2. Se parte de x igual a 1, y se traza la recta tangente en ese punto."],
 [4,9,"Donde la tangente cruza el eje está la siguiente aproximación, 1.5. Se repite con la tangente en ese nuevo punto."],
 [9,15,"La segunda aproximación es 1.4167, y el error baja de 0.086 a 0.0025."],
 [15,20,"Con la tercera y la cuarta, el error ya es de 2 millonésimas y luego casi cero. Las cifras correctas se duplican en cada paso."],
 [20,24,"Por eso Newton converge cuadráticamente, cerca de una raíz simple."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[5,0],[6,1],[9,1],[10,2],[14,2],[15,3],[19,3],[20,4],[24,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,24]}}
S=[
 sec("La idea",None,P("El método de {{gl:newton|Newton}} aproxima la curva por su tangente. La raíz de la tangente se toma como la nueva aproximación, y se repite. Si se parte de un punto cercano a una raíz simple, la convergencia es {{gl:cuadratica|cuadrática}}, es decir, muy rápida. El método de la {{gl:secante|secante}} evita la derivada. Y con raíces de {{gl:multiplicidad|multiplicidad}} mayor que 1, Newton se vuelve lento.")),
 sec("Un ejemplo","Un ejemplo",P("Se busca la raíz de x al cuadrado menos 2 desde x igual a 1. Mira la tangente en cada iteración y dónde cruza el eje."),EQ("x_{n+1}=x_{n}-\\dfrac{f(x_{n})}{f'(x_{n})}"),{"t":"grafica","animar":"dibujar","alt":"La curva y las tangentes de Newton"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con f de x igual a x al cuadrado menos 2 y x0 igual a 1, f vale menos 1 y f prima vale 2. ¿Cuánto vale x1, que es 1 menos f entre f prima?","opciones":[0.5,1.5,2,2.5],"correcta":1.5,"bien":"Muy bien. Es 1 menos menos un medio, o sea 1.5. Más abajo se ve la tangente.","mal":"Es 1.5, porque 1 menos (menos 1 entre 2) es 1 más un medio. Más abajo se ve la tangente."}),
 sec("Las iteraciones","Las iteraciones",P("Mira la tangente y el error en las iteraciones 0, 1, 2 y 3."),{"t":"acercando","ds":[0,1,2,3],"alt":"Las tangentes en cuatro iteraciones"},P("El error baja de 0.41 a 0.086, luego a 0.0025 y luego a 2 millonésimas.")),
 sec("La fórmula","La fórmula",P("La tangente en x de n es y igual a f de x de n más f prima de x de n por x menos x de n. Su raíz da la fórmula."),
   PASOS([("x_{n+1}=x_{n}-\\dfrac{f(x_{n})}{f'(x_{n})}","La fórmula de Newton."),
          ("f(x)=x^{2}-2:\\quad x_{1}=1-\\dfrac{-1}{2}=1.5","Con f igual a x al cuadrado menos 2 y x0 igual a 1."),
          ("f(x)=e^{2x}-e^{x}-2,\\ x_{0}=0:\\quad x_{1}=0-\\dfrac{-2}{1}=2","Otro ejemplo, que muestra que x1 puede estar lejos."),
          ("x_{n+1}=\\dfrac{1}{2}\\left(x_{n}+\\dfrac{2}{x_{n}}\\right)","Para x al cuadrado menos 2 la fórmula se simplifica, y es la que usan las calculadoras.")]),
   OJO("Newton puede fallar. Si la derivada es casi cero o si x0 está lejos de la raíz, las iteraciones pueden salirse. Por eso se combina con bisección cuando se necesita seguridad.")),
 sec("La secante y la rapidez","La secante",P("La secante evita calcular la derivada y a cambio converge un poco más despacio."),
   PASOS([("f'(x_{n})\\approx\\dfrac{f(x_{n})-f(x_{n-1})}{x_{n}-x_{n-1}}","La secante aproxima la derivada con dos puntos."),
          ("\\text{raíz simple}\\ \\Rightarrow\\ \\text{Newton cuadrático}","El error de un paso es del orden del cuadrado del anterior."),
          ("\\text{raíz de multiplicidad}\\ m>1\\ \\Rightarrow\\ \\text{Newton lineal}","Pierde la rapidez, y converge de forma lineal.")]),
   OJO("La secante necesita dos puntos iniciales, y no la derivada. Su convergencia es de orden 1.62, entre la lineal y la cuadrática.")),
 eng("La raíz cuadrada en una calculadora","Las calculadoras no tienen una tabla de raíces. Calculan la raíz de 2 con la fórmula de Newton para x al cuadrado menos 2, que es el promedio de x y 2 entre x. Con pocas iteraciones el resultado ya tiene todas las cifras de la pantalla.","x_{n+1}=\\dfrac{1}{2}\\left(x_{n}+\\dfrac{2}{x_{n}}\\right)",
   [("Iteración 1","1.5"),("Iteración 2","1.41667"),("Iteración 3","1.414216")],"Se parte de x0 igual a 1. Después de 3 iteraciones el valor es 1.414216, y el error es de 2 millonésimas. Cada paso duplica las cifras correctas, y eso es lo que hace tan rápido a Newton. Con más iteraciones el error baja al límite de la precisión de la máquina."),
 completar("Se calcula la primera iteración de Newton para f de x igual a x al cuadrado menos 2 con x0 igual a 1. Falta la derivada.","x_{1}=1-\\dfrac{-1}{[[hueco]]}",
   [("2","dos, que es f prima de 1"),("1","uno"),("-1","menos uno")],0,
   ["","Uno es f de 1 en valor absoluto, y no es la derivada, que es 2x.","Menos uno es f de 1, y la derivada es 2 por 1."],"La derivada de x al cuadrado menos 2 es 2x.","Con x igual a 1, la derivada es 2."),
 error("Alguien hizo la primera iteración de Newton y se equivocó en un paso. Toca el paso que está mal.",
   [("f(x)=x^{2}-2,\\quad f'(x)=2x","Se escribe la función y su derivada.","la función y su derivada"),
    ("x_{1}=x_{0}+\\dfrac{f(x_{0})}{f'(x_{0})}=1-\\dfrac{1}{2}=0.5","Este paso es el que falla.","la fórmula con signo más"),
    ("\\text{La aproximación es}\\ 0.5","Depende del paso anterior.","queda 0.5")],1,
   "La fórmula de Newton resta el cociente. Con x0 igual a 1 queda 1 menos menos 1 entre 2, o sea 1.5. Con el signo más se obtiene 0.5, que está lejos de la raíz.",
   "x_{1}=1-\\dfrac{-1}{2}=1.5","Revisa el signo de la fórmula."),
 ordenar("Estos son los pasos de una iteración de Newton para x al cuadrado menos 2 desde x0 igual a 1, pero están desordenados.",
   [("f(x)=x^{2}-2,\\ \\ f'(x)=2x","Se escriben f y su derivada"),
    ("f(1)=-1,\\ \\ f'(1)=2","Se evalúan en x0"),
    ("x_{1}=1-\\dfrac{-1}{2}","Se sustituye en la fórmula"),
    ("x_{1}=1.5","Se calcula")],[2,0,3,1],
   "Se escriben f y f prima, se evalúan, se sustituye en la fórmula y se calcula.","Se empieza escribiendo la función y su derivada."),
]
S+=cierre("Mini simulacro de Newton-Raphson y secante",[
 banco("mn_c1_15","Se resta el cociente de f entre f prima."),
 banco("mn_c1_16","$1-\\dfrac{-1}{2}=1.5$."),
 banco("mn_c1_18","Cerca de una raíz simple, el error se eleva al cuadrado en cada paso.")])
prac=[
 {"titulo":"La tangente","grafica":{"draw":1},"bloques":[P("La curva y la tangente en la aproximación."),EQ("f(x)=x^{2}-2")]},
 {"titulo":"Itera","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 4. Abajo se leen la aproximación y su error.")]},
 {"titulo":"Iteración 3","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("x_{3}=1.414216,\\quad \\text{error}\\approx2\\times10^{-6}"),P("Con la iteración 3, el error ya es de dos millonésimas.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Resta el cociente de f entre f prima."}]}]
preg={"tex":"\\text{Newton con}\\ f(x)=x^{2}-2\\ \\text{y}\\ x_{0}=2,\\ x_{1}=","opciones":["$1.5$","$2.5$","$1$","$0.5$"],"correcta":0,
 "explicacion":"f de 2 es 2 y f prima de 2 es 4. Entonces x1 es 2 menos 2 entre 4, o sea 2 menos 0.5, que da 1.5.",
 "verificacion":{"formula":"2-2/4+0*x","a":0,"esperado":1.5},
 "pistas":["Calcula f de 2 y f prima de 2.","Son 2 y 4.","Resta 2 entre 4 de 2."],
 "errores":["","Dos más 0.5 da 2.5, pero la fórmula resta.","Uno saldría de dividir 2 entre 2, pero f prima de 2 es 4.","Medio es solo el cociente, y falta restarlo de x0."]}
res=["Newton usa la tangente. Cada aproximación es x menos f entre f prima.","Cerca de una raíz simple, el error se eleva al cuadrado, y las cifras correctas se duplican.","La secante reemplaza la derivada por una diferencia, y con multiplicidad mayor que 1 Newton se vuelve lineal."]
write(lesson("mn-m1-l2","Lección 2 de 4","Newton-Raphson y secante",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-newton.json")
