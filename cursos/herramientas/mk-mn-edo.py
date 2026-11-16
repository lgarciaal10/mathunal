import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
MOD="Módulo 3 Ajuste, integración y ecuaciones diferenciales"
def ind(j): return f"(1+(x-{j}-0.37)/abs(x-{j}-0.37))/2"
EL=[{"t":"trazo","puntos":[[str(round(0.05*k,2)),str(round(math.exp(0.05*k),5))] for k in range(0,21)],"c":0}]
for j in range(8):
    I=ind(j)
    ta=f"({I})*{j}/x"; tb=f"({I})*{j+1}/x"
    ya=f"1+({I})*(exp({j}*ln(1+1/x))-1)"; yb=f"1+({I})*(exp({j+1}*ln(1+1/x))-1)"
    EL.append({"t":"segmento","a":[ta,ya],"b":[tb,yb],"c":3})
    EL.append({"t":"punto","p":[tb,yb],"c":2})
graf={"tipo":"plano","x":[-0.2,1.4],"y":[0.4,3.4],"a":1,"b":8,"inicio":2,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"valor en t igual a 1 con n pasos de Euler","formula":"exp(x*ln(1+1/x))"},{"rotulo":"error frente al valor exacto, e","formula":"2.718281828-exp(x*ln(1+1/x))"}],
 "etiquetas":["Aproximación de y de 1, igual a 1 más 1 entre n elevado a n","Diferencia con e, que es 2.7183"],"etiquetaSlider":"Número de pasos n, de 1 a 8",
 "alt":"La solución exacta y igual a e elevado a t, en azul, entre 0 y 1. En verde, el método de Euler con n pasos, que sigue la tangente en cada paso. Con 1 paso llega a 2, con 2 pasos a 2.25 y con 8 pasos a 2.566. Siempre queda por debajo de la curva exacta"}
glos={"progresiva":"La diferencia progresiva aproxima la derivada con f de x más h menos f de x, entre h. Su error es de orden h.",
 "centrada":"La diferencia centrada usa f de x más h menos f de x menos h, entre 2h. Su error es de orden h al cuadrado.",
 "euler":"El método de Euler resuelve y prima igual a f de t y avanzando con la tangente. y de n más 1 es y de n más h por f de t de n y de n.",
 "rk4":"El método de Runge-Kutta de cuarto orden promedia cuatro pendientes en cada paso. Su error global es de orden h a la cuarta."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se resuelve y prima igual a y, con y de 0 igual a 1. La solución exacta es la curva e elevado a t."],
 [4,9,"Con un paso, Euler sigue la tangente y llega a 2 en t igual a 1."],
 [9,15,"Con 2 pasos llega a 2.25, y con 4 pasos llega a 2.44."],
 [15,20,"Con 8 pasos llega a 2.566. Se acerca a e, que es 2.718, pero despacio, porque el error baja como h."],
 [20,24,"Métodos de orden mayor, como Runge-Kutta de cuarto orden, bajan el error como h a la cuarta."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,2],[13,4],[16,8],[24,8]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,24]}}
S=[
 sec("La idea",None,P("La derivada y las ecuaciones diferenciales también se aproximan con fórmulas sencillas. La diferencia {{gl:progresiva|progresiva}} y la {{gl:centrada|centrada}} aproximan la derivada con valores de f. El método de {{gl:euler|Euler}} avanza una ecuación diferencial siguiendo la tangente en cada paso, y el método de {{gl:rk4|Runge-Kutta}} lo hace con mejor precisión. Todos tienen un orden, que dice cómo baja el error al achicar el paso.")),
 sec("Un ejemplo","Un ejemplo",P("Se resuelve y prima igual a y con y de 0 igual a 1 usando Euler con n pasos hasta t igual a 1. Mira cómo se acerca a la curva exacta."),EQ("y_{n+1}=y_{n}+h\\,f(t_{n},y_{n}),\\qquad h=\\dfrac{1}{n}"),{"t":"grafica","animar":"dibujar","alt":"El método de Euler y la curva exacta"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con un solo paso de longitud 1, Euler hace y1 igual a y0 más h por f, con y0 igual a 1, h igual a 1 y f igual a 1. ¿Cuánto vale y1?","opciones":[1,2,2.5,3],"correcta":2,"bien":"Muy bien. Es 1 más 1, o sea 2, mientras el valor exacto es 2.718. Más abajo se ve cómo mejora con más pasos.","mal":"Es 2, porque 1 más 1 por 1 es 2. El valor exacto es 2.718. Más abajo se ve cómo mejora con más pasos."}),
 sec("Más pasos","Más pasos",P("Mira Euler con 1, 2, 4 y 8 pasos."),{"t":"acercando","ds":[1,2,4,8],"alt":"El método de Euler con cuatro cantidades de pasos"},P("El resultado en t igual a 1 sube de 2 a 2.25, 2.44 y 2.566, siempre por debajo del valor exacto, 2.718.")),
 sec("Derivadas numéricas","Derivadas",P("Se aproxima la derivada con un cociente de diferencias."),
   PASOS([("f'(x)\\approx\\dfrac{f(x+h)-f(x)}{h}","Diferencia progresiva. Su error es de orden h."),
          ("f'(x)\\approx\\dfrac{f(x+h)-f(x-h)}{2h}","Diferencia centrada. Su error es de orden h al cuadrado."),
          ("f(x)=x^{2},\\ x=1,\\ h=0.1:\\ \\dfrac{1.21-1}{0.1}=2.1","Con la progresiva queda 2.1, que tiene error 0.1."),
          ("\\dfrac{1.21-0.81}{0.2}=2.0","Con la centrada queda 2.0, que aquí es exacto.")]),
   OJO("Achicar mucho el paso no siempre mejora el resultado. Al restar números casi iguales se pierden cifras, como se vio en la lección de errores.")),
 sec("Euler y Runge-Kutta","Euler y RK4",P("En cada paso se avanza con una pendiente."),
   PASOS([("y'=y,\\ y(0)=1,\\ h=0.1:\\quad y_{1}=1+0.1\\cdot1=1.1","Un paso de Euler."),
          ("y'=t\\left(y+\\tfrac12\\right),\\ h=0.2,\\ y(0.2)=1.01:\\quad y(0.4)\\approx1.01+0.2\\cdot0.2\\cdot1.51=1.0704","Otro ejemplo, que usa t en la pendiente."),
          ("\\text{Euler: error local}\\ O(h^{2}),\\ \\text{global}\\ O(h)","Los errores locales se acumulan y el global es de un orden menos."),
          ("\\text{RK4: error global}\\ O(h^{4})","Mucho más preciso, con cuatro evaluaciones de f por paso.")]),
   OJO("En Euler, la pendiente del paso es la del punto inicial. Por eso se queda atrás cuando la solución es convexa, como e elevado a t, y se queda por debajo.")),
 eng("La velocidad a partir de posiciones","Un sensor mide la posición de una pieza a los 0.9, 1.0 y 1.1 segundos, y entrega 0.81, 1.00 y 1.21 metros. Para estimar la velocidad en t igual a 1 se usa la diferencia centrada, que es más precisa que la progresiva.","v(1)\\approx\\dfrac{1.21-0.81}{0.2}=2.0\\ \\text{m/s}",
   [("Posiciones","0.81, 1.00 y 1.21 m"),("Diferencia centrada","2.0 m/s"),("Diferencia progresiva","2.1 m/s")],"Con la posición x al cuadrado, la velocidad exacta en t igual a 1 es 2.0 metros por segundo, y la diferencia centrada la da sin error. La progresiva da 2.1, que está equivocada en 5 por ciento. Con datos reales, con ruido, hay que filtrar antes de derivar, porque derivar amplifica el ruido."),
 completar("Se hace un paso de Euler para y prima igual a y, con y0 igual a 1 y h igual a 0.1. Falta el valor de f.","y_{1}=1+0.1\\cdot[[hueco]]",
   [("1","f de 0 y 1, que vale 1"),("0.1","el paso"),("1.1","el resultado")],0,
   ["","0.1 es el paso h, que ya multiplica. El valor que falta es la pendiente f.","1.1 es el resultado final, y no la pendiente."],"La pendiente es f de t0 y y0, que aquí es y0.","f de 0 y 1 es 1, y 1 más 0.1 por 1 da 1.1."),
 error("Alguien hizo un paso de Euler para y prima igual a y, con y0 igual a 1 y h igual a 0.1, y se equivocó en un paso. Toca el paso que está mal.",
   [("y_{0}=1,\\quad f(t,y)=y,\\quad h=0.1","Los datos.","los datos del problema"),
    ("y_{1}=h\\,f(t_{0},y_{0})=0.1","Este paso es el que falla.","queda 0.1"),
    ("\\text{El valor aproximado es}\\ 0.1","Depende del paso anterior.","y1 vale 0.1")],1,
   "La fórmula de Euler suma el incremento al valor anterior. Queda y0 más h por f, o sea 1 más 0.1 por 1, que es 1.1. Con 0.1 se olvida el valor inicial.",
   "y_{1}=y_{0}+h\\,f=1+0.1\\cdot1=1.1","Revisa la fórmula completa de Euler."),
 ordenar("Estos son los pasos para aproximar la derivada de x al cuadrado en x igual a 1 con la diferencia centrada y h igual a 0.1, pero están desordenados.",
   [("f(1.1)=1.21,\\quad f(0.9)=0.81","Se evalúa f en x más h y en x menos h"),
    ("f(1.1)-f(0.9)=0.4","Se restan"),
    ("\\dfrac{0.4}{2\\cdot0.1}","Se divide entre 2h"),
    ("f'(1)\\approx2","Se calcula")],[2,0,3,1],
   "Se evalúa f en los dos lados, se resta y se divide entre 2h.","Se empieza evaluando f a los dos lados."),
]
S+=cierre("Mini simulacro de diferenciación numérica y EDO",[
 banco("mn_c3_16","La diferencia centrada tiene error de orden $h^2$."),
 banco("mn_c3_18","$y_1=1+0.1\\cdot1=1.1$."),
 banco("mn_c3_19","El método de Runge-Kutta de cuarto orden tiene error global de orden $h^4$.")])
prac=[
 {"titulo":"Euler y la curva exacta","grafica":{"draw":1},"bloques":[P("El método de Euler y la solución exacta de y prima igual a y."),EQ("y'=y,\\ y(0)=1")]},
 {"titulo":"Cambia los pasos","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 1 a 8. Abajo se leen el valor en t igual a 1 y su error.")]},
 {"titulo":"Ocho pasos","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":8,"bloques":[EQ("\\left(1+\\tfrac18\\right)^{8}=2.566"),P("Con 8 pasos el valor es 2.566, y el error es 0.152.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":8},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Suma el incremento al valor anterior."}]}]
preg={"tex":"\\text{Euler para}\\ y'=2y,\\ y(0)=1,\\ h=0.1:\\ y_{1}=","opciones":["$1.2$","$1.1$","$2$","$0.2$"],"correcta":0,
 "explicacion":"La pendiente es f igual a 2 por y0, o sea 2. Entonces y1 es 1 más 0.1 por 2, que da 1.2.",
 "verificacion":{"formula":"1+0.1*2*1+0*x","a":0,"esperado":1.2},
 "pistas":["Calcula la pendiente f de t0 y y0.","Es 2 por 1, o sea 2.","Suma h por la pendiente a y0."],
 "errores":["","1.1 sería para y prima igual a y, con pendiente 1.","Dos es la pendiente, y no el valor de y1.","0.2 es solo el incremento, y falta sumarlo a y0."]}
res=["La diferencia progresiva tiene error de orden h, y la centrada de orden h al cuadrado.","Euler avanza con la tangente, con error local de orden h al cuadrado y global de orden h.","Runge-Kutta de cuarto orden tiene error global de orden h a la cuarta."]
write(lesson("mn-m3-l2","Lección 2 de 4","Diferenciación numérica y EDO",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-edo.json")
