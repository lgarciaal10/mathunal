import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
from fundlib import *
MOD="Módulo 2 Sistemas lineales e interpolación"
def vals(t):
    return [(t-1)*(t-2)/2, -t*(t-2), t*(t-1)/2, 2*t*t+1]
TS=[round(-0.5+0.1*k,2) for k in range(0,27)]
EL=[{"t":"trazo","puntos":[[str(t),"("+lagr([round(v,9) for v in vals(t)])+")"] for t in TS],"c":0}]
for xn in (0,1,2):
    EL.append({"t":"punto","p":[str(xn),"("+lagr([round(v,9) for v in vals(xn)])+")"],"c":2})
for xn,yn in ((0,1),(1,3),(2,9)):
    EL.append({"t":"punto","p":[str(xn),str(yn)],"c":3})
graf={"tipo":"plano","x":[-0.8,2.8],"y":[-4.0,11.5],"a":0,"b":3,"inicio":3,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"valor de la curva elegida en x igual a 1","formula":"("+lagr([round(v,9) for v in [vals(1)[i] for i in range(4)]])+")"},{"rotulo":"valor de la curva elegida en x igual a 2","formula":"("+lagr([round(v,9) for v in [vals(2)[i] for i in range(4)]])+")"}],
 "etiquetas":["Es 1 solo para la base L1, y 3 para el polinomio","Es 1 solo para la base L2, y 9 para el polinomio"],"etiquetaSlider":"Curva, 0 a 2 las bases de Lagrange y 3 el polinomio",
 "alt":"Las bases de Lagrange L0, L1 y L2 de los nodos 0, 1 y 2, y el polinomio interpolante. Cada base vale 1 en su nodo y 0 en los otros. El polinomio 2x al cuadrado más 1 pasa por los puntos (0, 1), (1, 3) y (2, 9), marcados en verde"}
glos={"interpolacion":"Interpolar es hallar una función, normalmente un polinomio, que pase exactamente por unos puntos dados.",
 "lagrange":"Las bases de Lagrange L sub i valen 1 en el nodo i y 0 en los demás nodos. El polinomio interpolante es la suma de cada valor por su base.",
 "diferencias":"Las diferencias divididas de Newton calculan los coeficientes del polinomio con cocientes sucesivos. La de primer orden es f de x1 menos f de x0, entre x1 menos x0.",
 "runge":"El fenómeno de Runge es la oscilación grande que aparece en los extremos al interpolar con un polinomio de grado alto en nodos igualmente espaciados."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Hay tres puntos, (0, 1), (1, 3) y (2, 9). Se arma un polinomio con las bases de Lagrange."],
 [4,9,"La base L0 vale 1 en x igual a 0 y vale 0 en los otros dos nodos."],
 [9,14,"La base L1 vale 1 en x igual a 1, y la L2 vale 1 en x igual a 2. Cada una vale cero en los otros nodos."],
 [14,20,"El polinomio es 1 por L0 más 3 por L1 más 9 por L2. Pasa por los tres puntos, y es 2x al cuadrado más 1."],
 [20,24,"Por n más 1 puntos con abscisas distintas pasa un único polinomio de grado a lo sumo n."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[6,0],[9,1],[11,1],[12,2],[15,3],[24,3]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[14,24]}}
S=[
 sec("La idea",None,P("Dados unos puntos, {{gl:interpolacion|interpolar}} es encontrar un polinomio que pase exactamente por ellos. Con las bases de {{gl:lagrange|Lagrange}} se arma de forma directa, y con las {{gl:diferencias|diferencias divididas}} de Newton se arma por etapas. Si hay muchos puntos y un grado alto, aparece el {{gl:runge|fenómeno de Runge}}.")),
 sec("Un ejemplo","Un ejemplo",P("Se tienen los puntos (0, 1), (1, 3) y (2, 9). Mira las tres bases de Lagrange y el polinomio que forman."),EQ("P(x)=\\sum_{i}f_{i}\\,L_{i}(x),\\qquad L_{i}(x_{j})=\\begin{cases}1&i=j\\\\0&i\\neq j\\end{cases}"),{"t":"grafica","animar":"dibujar","alt":"Las bases de Lagrange y el polinomio"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El polinomio P es 1 por L0 más 3 por L1 más 9 por L2. En el nodo x igual a 1 solo L1 vale 1 y las demás valen 0. ¿Cuánto vale P de 1?","opciones":[1,3,9,13],"correcta":3,"bien":"Muy bien. Vale 3, que es el valor dado en ese nodo. Más abajo se ve.","mal":"Vale 3, porque solo sobrevive 3 por L1, y L1 vale 1 en ese nodo. Más abajo se ve."}),
 sec("Las bases y el polinomio","Las curvas",P("Mira las bases L0, L1, L2 y el polinomio."),{"t":"acercando","ds":[0,1,2,3],"alt":"Las bases de Lagrange y el polinomio"},P("Cada base vale 1 en un nodo y 0 en los otros. El polinomio combina las tres con los valores de los datos.")),
 sec("Lagrange","Lagrange",P("Cada base se arma con productos de factores que se anulan en los otros nodos."),
   PASOS([("L_{0}(x)=\\dfrac{(x-1)(x-2)}{(0-1)(0-2)}=\\dfrac{(x-1)(x-2)}{2}","Se anula en x igual a 1 y a 2, y vale 1 en x igual a 0."),
          ("L_{1}(x)=-x(x-2),\\qquad L_{2}(x)=\\dfrac{x(x-1)}{2}","Las otras dos bases."),
          ("P(x)=1\\,L_{0}+3\\,L_{1}+9\\,L_{2}=2x^{2}+1","El polinomio que interpola."),
          ("P(0)=1,\\ P(1)=3,\\ P(2)=9","Se comprueba en los tres nodos.")])),
 sec("Diferencias divididas","Newton",P("El mismo polinomio se obtiene por etapas con las diferencias divididas."),
   PASOS([("f[x_{0},x_{1}]=\\dfrac{3-1}{1-0}=2,\\quad f[x_{1},x_{2}]=\\dfrac{9-3}{2-1}=6","Las diferencias de primer orden."),
          ("f[x_{0},x_{1},x_{2}]=\\dfrac{6-2}{2-0}=2","La de segundo orden."),
          ("P(x)=1+2x+2x(x-1)=2x^{2}+1","El polinomio de Newton, igual al de Lagrange.")]),
   OJO("El polinomio interpolante es único, y Lagrange y Newton son dos formas de escribirlo. Con nodos muy numerosos e igualmente espaciados, el polinomio puede oscilar mucho entre ellos, y en esos casos se prefieren splines.")),
 eng("Calibrar una célula de carga","Una célula de carga entrega 1, 3 y 9 milivoltios al aplicarle 0, 1 y 2 kilonewtons. Se interpola un polinomio de segundo grado para estimar la lectura en cargas intermedias, como 1.5 kilonewtons.","P(F)=2F^{2}+1,\\qquad P(1.5)=5.5\\ \\text{mV}",
   [("Cargas de calibración","0, 1 y 2 kN"),("Lecturas","1, 3 y 9 mV"),("Estimación a 1.5 kN","5.5 mV")],"El valor interpolado es 2 por 2.25 más 1, o sea 5.5 milivoltios. Interpolar es confiable entre los puntos de calibración, pero no fuera de ellos. Extrapolar a 4 kilonewtons con este polinomio daría 33 milivoltios, un valor que no se puede asegurar, porque el sensor real puede saturarse."),
 completar("Se calcula una diferencia dividida con los puntos (1, 3) y (2, 9). Falta el resultado.","f[x_{1},x_{2}]=\\dfrac{9-3}{2-1}=[[hueco]]",
   [("6","seis"),("3","tres"),("12","doce")],0,
   ["","Tres es el valor de f en x1, y no el cociente.","Doce es 9 más 3, pero la diferencia dividida resta los valores."],"Se resta y se divide entre la diferencia de abscisas.","9 menos 3 es 6, entre 2 menos 1 que es 1."),
 error("Alguien trabajó con la base de Lagrange L0 y se equivocó en un paso. Toca el paso que está mal.",
   [("L_{0}(x)=\\dfrac{(x-1)(x-2)}{2}","La base L0 para los nodos 0, 1 y 2.","la base es un producto sobre 2"),
    ("L_{0}(0)=\\dfrac{(-1)(-2)}{2}=1","Vale 1 en su nodo.","en x igual a 0 vale 1"),
    ("\\text{Entonces}\\ L_{0}(1)=1","Este paso es el que falla.","en x igual a 1 también vale 1")],2,
   "En x igual a 1 el factor x menos 1 se anula, así que L0 de 1 vale 0. Cada base vale 1 solo en su propio nodo y 0 en los demás.",
   "L_{0}(1)=\\dfrac{(0)(-1)}{2}=0","Evalúa el factor x menos 1 en x igual a 1."),
 ordenar("Estos son los pasos para armar el polinomio de Newton por los puntos (0, 1), (1, 3) y (2, 9), pero están desordenados.",
   [("f[x_{0},x_{1}]=2","Se calcula la primera diferencia entre x0 y x1"),
    ("f[x_{1},x_{2}]=6","Se calcula la primera diferencia entre x1 y x2"),
    ("f[x_{0},x_{1},x_{2}]=\\dfrac{6-2}{2}=2","Se calcula la segunda diferencia"),
    ("P(x)=1+2x+2x(x-1)","Se escribe el polinomio")],[2,0,3,1],
   "Se calculan las diferencias de primer orden, luego la de segundo y se arma el polinomio.","Se empieza con las diferencias de primer orden."),
]
S+=cierre("Mini simulacro de interpolación polinómica",[
 banco("mn_c2_14","Por $n+1$ puntos distintos pasa un único polinomio de grado a lo sumo $n$."),
 banco("mn_c2_15","Cada base de Lagrange vale 1 en su nodo y 0 en los demás."),
 banco("mn_c2_18","$P(0)=1$, $P(1)=3$ y $P(2)=9$ se cumplen con $2x^2+1$.")])
prac=[
 {"titulo":"Tres puntos","grafica":{"draw":1},"bloques":[P("Los puntos (0, 1), (1, 3) y (2, 9) y las curvas de Lagrange."),EQ("P(x)=\\sum f_{i}L_{i}(x)")]},
 {"titulo":"Cambia la curva","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 3. Abajo se leen los valores de la curva elegida en x igual a 1 y a 2.")]},
 {"titulo":"El polinomio","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("P(x)=2x^{2}+1"),P("El polinomio pasa por los tres puntos, y vale 3 en x igual a 1 y 9 en x igual a 2.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Comprueba que el polinomio pasa por los tres puntos."}]}]
preg={"tex":"\\text{El polinomio de grado}\\ \\le2\\ \\text{que pasa por}\\ (0,0),\\ (1,1),\\ (2,4)\\ \\text{es}","opciones":["$x^{2}$","$x$","$2x$","$x^{2}+x$"],"correcta":0,
 "explicacion":"Con x al cuadrado se cumple que en 0 vale 0, en 1 vale 1 y en 2 vale 4. Como el polinomio de grado a lo sumo 2 que pasa por tres puntos es único, es x al cuadrado.",
 "verificacion":{"formula":"2*2+0*x","a":0,"esperado":4},
 "pistas":["Prueba cada opción en x igual a 2.","El valor tiene que ser 4.","Solo x al cuadrado da 4 en x igual a 2 y 1 en x igual a 1."],
 "errores":["","La recta x vale 2 en x igual a 2, y no 4.","La recta 2x vale 2 en x igual a 1, y no 1.","Vale 2 en x igual a 1, y no 1."]}
res=["Por n más 1 puntos con abscisas distintas pasa un único polinomio de grado a lo sumo n.","Cada base de Lagrange vale 1 en su nodo y 0 en los demás, y el polinomio suma valor por base.","Las diferencias divididas dan el mismo polinomio por etapas. Con muchos nodos es mejor usar splines."]
write(lesson("mn-m2-l1","Lección 1 de 4","Interpolación polinómica",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-interpolacion.json")
