import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 3 Laplace, sistemas y series"
N=160
TS=[-0.5+8.5*k/N for k in range(N+1)]
U=lambda t:f"(1+({t:.4f}-x)/sqrt(({t:.4f}-x)*({t:.4f}-x)+0.000001))/2"
RESP=[[f"{t:.4f}",f"(1-exp(0-({t:.4f}-x)))*{U(t)}"] for t in TS]
ESC=[[f"{t:.4f}",U(t)] for t in TS]
graf={"tipo":"plano","x":[-0.5,8],"y":[-0.35,1.45],"a":0.5,"b":4,"inicio":1.5,
 "elementos":[{"t":"trazo","puntos":ESC,"c":3,"guia":True},{"t":"trazo","puntos":RESP,"c":2},{"t":"punto","p":["x","0"],"c":1}],
 "lecturas":[{"rotulo":"instante del escalón a","formula":"x"},{"rotulo":"y en t=5","formula":"1-exp(0-(5-x))"}],
 "etiquetas":["Instante del escalón a","Valor de y en t igual a 5"],"etiquetaSlider":"Instante del escalón a",
 "alt":"La respuesta de y prima más y igual a un escalón que se enciende en t igual a a, con y de 0 igual a 0. No pasa nada antes de a, y después sube hacia 1. Al mover a, la respuesta se desplaza sin cambiar de forma"}
glos={"escalon":"La función escalón u de t menos a vale 0 antes de t igual a a y 1 después. Sirve para encender o apagar una fuerza en un instante.",
 "delta":"La delta de Dirac representa un golpe muy corto y muy fuerte, de área 1, en un instante. No es una función común. Se define por lo que hace dentro de una integral.",
 "desplazamiento":"La propiedad de desplazamiento dice que retrasar una función a unidades de tiempo multiplica su transformada por e a la menos a s."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación y prima más y igual a un escalón que se enciende en t igual a a. Antes de a no pasa nada. Esta es la respuesta con a igual a 1.5."],
 [4,8,"La curva de apoyo es el escalón u de t menos a, que vale 0 antes de a y 1 después. La respuesta sube hacia 1 desde ese instante."],
 [8,14,"Mueve a y mira cómo la respuesta se desplaza igual, sin cambiar de forma. Solo se retrasa."],
 [14,18,"Eso es la propiedad de desplazamiento. Si f de t tiene transformada F de s, la función retrasada f de t menos a por el escalón tiene transformada e a la menos a s por F de s."],
 [18,22,"Con a igual a 3, la respuesta en t igual a 5 es 1 menos e a la menos 2, o sea 0.86."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1.5],[8,1.5],[10,0.5],[13,4],[14,3],[22,3]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Muchas fuerzas se encienden o se apagan de golpe, o llegan como un golpe corto. El {{gl:escalon|escalón}} y la {{gl:delta|delta de Dirac}} sirven para modelarlas. Con Laplace se resuelven fácil, porque retrasar una función en el tiempo solo multiplica su transformada por una exponencial.")),
 sec("Un ejemplo","Un ejemplo",P("Mira una ecuación con una fuerza que se enciende en t igual a a. La respuesta parte de 0."),EQ("y'+y=u(t-a),\\qquad y(0)=0"),{"t":"grafica","animar":"dibujar","alt":"La respuesta al escalón"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El escalón u de t menos 2 vale 0 antes de t igual a 2 y 1 después. ¿Cuánto vale 3 por u de t menos 2 en t igual a 5?","opciones":[0,1,3,5],"correcta":3,"bien":"Muy bien. Vale 3, porque en t igual a 5 el escalón ya está encendido. Más abajo se ve la respuesta a un escalón.","mal":"Vale 3, porque en t igual a 5 el escalón ya vale 1. Más abajo se ve la respuesta a un escalón."}),
 sec("Moviendo el escalón","Moviendo a",P("Mira cómo se desplaza la respuesta al cambiar el instante del escalón."),{"t":"acercando","ds":[1.5,0.5,4,3],"alt":"La respuesta para varios valores de a"},P("La forma de la respuesta no cambia. Solo se retrasa a unidades de tiempo.")),
 sec("Las transformadas","Transformadas",P("Estas son las dos transformadas nuevas y la propiedad de desplazamiento."),
   PASOS([("\\mathcal{L}\\{u(t-a)\\}=\\dfrac{e^{-as}}{s}","El escalón retrasado."),
          ("\\mathcal{L}\\{\\delta(t-a)\\}=e^{-as}","La delta de Dirac retrasada, por su propiedad de filtrado."),
          ("\\mathcal{L}\\{f(t-a)\\,u(t-a)\\}=e^{-as}F(s)","La {{gl:desplazamiento|propiedad de desplazamiento}}.")])),
 sec("Resolver el ejemplo","El ejemplo",P("Se transforma la ecuación con y de 0 igual a 0."),
   PASOS([("sY+Y=\\dfrac{e^{-as}}{s}","Se transforman los dos lados."),
          ("Y=e^{-as}\\left(\\dfrac{1}{s}-\\dfrac{1}{s+1}\\right)","Se despeja Y y se separa en fracciones parciales."),
          ("y=\\left(1-e^{-(t-a)}\\right)u(t-a)","Cada fracción se invierte con la tabla, y el factor exponencial retrasa la respuesta.")]),
   OJO("La respuesta vale 0 antes de t igual a a. Eso lo asegura el factor u de t menos a. Si se olvida, aparece una respuesta que empieza antes de que se encienda la fuerza.")),
 eng("El golpe sobre un resorte","Un martillo golpea una masa sujeta a un resorte. El golpe dura tan poco que se modela como una delta de Dirac. Lo que importa es el impulso, la fuerza por el tiempo, que cambia la velocidad de la masa de golpe.","m\\,y''+k\\,y=J\\,\\delta(t)",
   [("Masa","2 kg"),("Rigidez","200 N/m"),("Impulso","4 N·s")],"El impulso da a la masa una velocidad inicial de J sobre m, o sea 2 metros por segundo. La frecuencia natural es la raíz de k sobre m, 10 radianes por segundo, y la respuesta es y igual a 0.2 por seno de 10t, en metros. La masa oscila con una amplitud de 0.20 metros. Es un modelo idealizado, porque ningún golpe es instantáneo, y no incluye amortiguamiento."),
 completar("Se transforma el escalón retrasado.","\\mathcal{L}\\{u(t-a)\\}=\\dfrac{e^{-as}}{[[hueco]]}",
   [("s","s"),("s^{2}","s al cuadrado"),("1","uno")],0,
   ["","Con s al cuadrado se transformaría una rampa, no un escalón.","Con 1 se transformaría la delta, no el escalón."],"Sin el retraso, la transformada del escalón es 1 sobre s.","El escalón sin retraso tiene transformada 1 sobre s, y el retraso agrega el factor exponencial."),
 error("Alguien resolvió y prima más y igual a u de t menos 1, con y de 0 igual a 0, y se equivocó en un paso. Toca el paso que está mal.",
   [("sY+Y=\\dfrac{e^{-s}}{s}","Se transforma la ecuación.","se transforma la ecuación y queda e a la menos s sobre s"),
    ("Y=e^{-s}\\left(\\dfrac{1}{s}-\\dfrac{1}{s+1}\\right)","Fracciones parciales.","se separa en fracciones parciales"),
    ("y=1-e^{-t}","Este paso es el que falla.","y es 1 menos e a la menos t")],2,
   "El factor e a la menos s retrasa la respuesta una unidad. Falta cambiar t por t menos 1 y multiplicar por el escalón u de t menos 1.",
   "y=\\left(1-e^{-(t-1)}\\right)u(t-1)","Fíjate en el factor e a la menos s."),
 ordenar("Estos son los pasos para resolver y prima más y igual a delta de t menos a, con y de 0 igual a 0, pero están desordenados.",
   [("y'+y=\\delta(t-a),\\ y(0)=0","El problema"),
    ("(s+1)Y=e^{-as}","Se transforma"),
    ("Y=\\dfrac{e^{-as}}{s+1}","Se despeja Y"),
    ("y=e^{-(t-a)}\\,u(t-a)","La inversa, con el retraso")],[2,0,3,1],
   "Se transforma, se despeja Y y se invierte aplicando el desplazamiento.","Se empieza con la ecuación transformada."),
]
S+=cierre("Mini simulacro de escalón y delta",[
 banco("ed_c3_06","La función constante 1 es el escalón sin retraso, y su transformada es $\\dfrac{1}{s}$."),
 banco("ed_c3_12","La propiedad de filtrado da $\\int_0^\\infty e^{-st}\\delta(t-a)\\,dt=e^{-as}$.")])
prac=[
 {"titulo":"La respuesta","grafica":{"draw":1,"guide":1},"bloques":[P("Una fuerza que se enciende en t igual a a."),EQ("y'+y=u(t-a)")]},
 {"titulo":"Mueve el escalón","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La respuesta se desplaza sin cambiar de forma. Abajo se lee y en t igual a 5.")]},
 {"titulo":"Un caso","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("a=3\\ \\Rightarrow\\ y(5)=1-e^{-2}\\approx 0.86"),P("Con a igual a 3, el escalón lleva 2 unidades de tiempo encendido en t igual a 5.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Aplica el desplazamiento, cambia t por t menos a."}]}]
preg={"tex":"\\mathcal{L}^{-1}\\left\\{\\dfrac{e^{-2s}}{s+1}\\right\\}\\ \\text{en}\\ t=3\\ \\text{vale}","opciones":["$0.37$","$0.05$","$1$","$0.14$"],"correcta":0,
 "explicacion":"La inversa de 1 sobre (s más 1) es e a la menos t. Con el factor e a la menos 2s se retrasa 2 unidades, y queda e a la menos (t menos 2) por u de t menos 2. En t igual a 3 vale e a la menos 1, que es 0.37.",
 "verificacion":{"formula":"exp(0-(x-2))","a":3,"esperado":0.367879},
 "pistas":["La inversa sin retraso es e a la menos t.","El retraso cambia t por t menos 2.","Evalúa e a la menos (3 menos 2)."],
 "errores":["","Ese es e a la menos 3, que sale de olvidar el retraso.","Eso sería el valor del escalón y no de la respuesta. Falta la exponencial.","Ese es e a la menos 2, que sale de usar a en vez de t menos a."]}
res=["El escalón retrasado tiene transformada e a la menos a s sobre s, y la delta retrasada tiene e a la menos a s.","Retrasar una función a unidades multiplica su transformada por e a la menos a s.","Al invertir hay que cambiar t por t menos a y multiplicar por el escalón."]
write(lesson("edo-m3-l3","Lección 3 de 5","Función escalón y delta de Dirac",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=3,curso="Ecuaciones Diferenciales"),"edo-escalon.json")
