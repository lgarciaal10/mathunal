import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 2 Transformada de Fourier y EDP de evolución"
XS=[round(k*math.pi/40,5) for k in range(41)]
EL=[{"t":"trazo","puntos":[[str(xv),f"sin({xv})*cos(x)+0.5*sin({2*xv})*cos(2*x)"] for xv in XS],"c":0},
    {"t":"trazo","puntos":[[str(xv),f"sin({xv})*cos(x)"] for xv in XS],"c":3}]
graf={"tipo":"plano","x":[-0.4,3.6],"y":[-1.8,1.8],"a":0,"b":6.28,"inicio":0,"elementos":EL,
 "lecturas":[{"rotulo":"factor del modo uno, coseno de t","formula":"cos(x)"},{"rotulo":"factor del modo dos, coseno de 2 t","formula":"cos(2*x)"}],
 "etiquetas":["El modo uno, que es la nota fundamental","El modo dos oscila al doble de rapidez"],"etiquetaSlider":"Tiempo t, de 0 a 6.28",
 "alt":"Una cuerda de longitud pi con los extremos fijos. La forma total es la suma del modo uno, seno de x por coseno de t, y la mitad del modo dos, seno de 2x por coseno de 2t. La curva verde es solo el modo uno. A diferencia del calor, los modos no se apagan, sino que oscilan"}
glos={"onda":"La ecuación de onda, u sub t t igual a c al cuadrado u sub x x, describe cómo se propagan y vibran las perturbaciones, como en una cuerda.",
 "nodo":"Un nodo es un punto de la cuerda que no se mueve durante la vibración de un modo.",
 "armonico":"Los armónicos son los modos de frecuencia n veces la fundamental. Dan el timbre de un instrumento.",
 "fundamental":"La frecuencia fundamental es la del primer modo, la más baja, y define la nota que se escucha."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Una cuerda de longitud pi con los extremos fijos. Su forma inicial es la suma de dos modos, seno de x y la mitad de seno de 2x."],
 [4,10,"A diferencia del calor, los modos no se apagan, sino que oscilan, cada uno con coseno de n t."],
 [10,16,"Con t igual a pi, el modo uno cambió de signo y el modo dos volvió a su valor inicial."],
 [16,20,"En un periodo completo, de 0 a 2 pi, la cuerda vuelve a su forma inicial."],
 [20,24,"Los armónicos oscilan con frecuencia n veces la fundamental, y por eso se oye una nota con timbre."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,1.57],[13,3.14],[16,3.14],[18,6.28],[24,6.28]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("La ecuación de {{gl:onda|onda}} describe la cuerda vibrante. Se resuelve igual que la de calor, por separación de variables, pero ahora cada modo oscila y no se apaga. El modo n es seno de n x por coseno de n c t, y su frecuencia es n veces la {{gl:fundamental|fundamental}}. Los {{gl:armonico|armónicos}} dan el timbre, y los {{gl:nodo|nodos}} son los puntos quietos.")),
 sec("Un ejemplo","Un ejemplo",P("La cuerda tiene longitud pi y c igual a 1. Mueve el tiempo y mira cómo oscilan los dos modos."),EQ("u_{tt}=u_{xx},\\qquad u(x,t)=\\operatorname{sen}x\\cos t+\\tfrac{1}{2}\\operatorname{sen}2x\\cos2t"),{"t":"grafica","animar":"dibujar","alt":"La cuerda vibrando con dos modos"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En la ecuación de calor los modos decaen como e elevado a menos n al cuadrado t. En la de onda, ¿cómo evoluciona cada modo en el tiempo?","opciones":["Oscila con coseno de n t","Decae como e elevado a menos n t","Crece sin límite","Se mantiene fijo"],"correcta":"Oscila con coseno de n t","bien":"Muy bien. En la onda los modos oscilan y no se apagan, porque no hay disipación.","mal":"En la onda cada modo oscila con coseno de n c t, y no se apaga. Eso es porque no hay disipación."}),
 sec("La cuerda en el tiempo","El tiempo",P("Mira la cuerda con t igual a 0, 1.57, 3.14 y 4.71."),{"t":"acercando","ds":[0,1.57,3.14,4.71],"alt":"La cuerda en cuatro instantes"},P("A t igual a 1.57 el modo uno pasa por cero, y a t igual a 3.14 cambió de signo.")),
 sec("Separación de variables","Separación",P("Se busca la solución como un producto, y se obtienen dos ecuaciones de oscilación."),
   PASOS([("u(x,t)=F(x)\\,G(t)","Se propone una solución separada."),
          ("\\dfrac{G''}{c^{2}G}=\\dfrac{F''}{F}=-\\lambda","Cada lado depende de una sola variable."),
          ("F(0)=F(L)=0\\ \\Rightarrow\\ F=\\operatorname{sen}\\dfrac{n\\pi x}{L},\\ \\lambda=\\left(\\dfrac{n\\pi}{L}\\right)^{2}","Los extremos fijos determinan F y lambda."),
          ("u_{n}=\\operatorname{sen}\\dfrac{n\\pi x}{L}\\cos\\dfrac{n\\pi ct}{L}","El modo n, cuando la cuerda parte del reposo.")]),
   OJO("La constante de separación debe ser negativa, como en la de calor. Si no, no hay solución con los extremos fijos que no sea nula.")),
 sec("Frecuencias de la cuerda","Frecuencias",P("Cada modo tiene su frecuencia, y son múltiplos de la fundamental."),
   PASOS([("f_{n}=\\dfrac{nc}{2L}","La frecuencia del modo n."),
          ("f_{1}=\\dfrac{c}{2L}","La fundamental."),
          ("f_{n}=n\\,f_{1}","Los armónicos son múltiplos enteros."),
          ("c=\\sqrt{T/\\rho}","La velocidad depende de la tensión T y de la densidad lineal.")]),
   OJO("Más tensión sube la frecuencia, y más densidad la baja. Por eso se afina una cuerda cambiando su tensión.")),
 eng("La cuerda de una guitarra","Una cuerda de 0.65 metros de longitud se afina para que su nota fundamental sea 330 hertz. Con esa frecuencia se calcula la velocidad de la onda en la cuerda.","c=2Lf_{1}=2\\,(0.65)\\,(330)\\approx429\\ \\text{m/s}",
   [("Longitud","0.65 m"),("Fundamental","330 Hz"),("Velocidad de la onda","cerca de 429 m/s")],"Al presionar la cuerda con un dedo, la longitud efectiva baja y la fundamental sube, porque f es c entre 2L. En la práctica, la rigidez de la cuerda cambia un poco los armónicos, y por eso se ajusta con el oído."),
 completar("En la cuerda con extremos fijos, la frecuencia del modo n es n veces la [[hueco]].","f_{n}=n\\cdot[[hueco]]",
   [("f_{1}","fundamental"),("f_{n+1}","la siguiente"),("c","la velocidad")],0,
   ["","La siguiente frecuencia no es una referencia fija para todos los modos.","La velocidad no es una frecuencia, y sus unidades son otras."],"El modo n tiene n veces la frecuencia fundamental.","La frecuencia fundamental es la del primer modo."),
 error("Alguien calculó la frecuencia fundamental de una cuerda de 0.5 metros con velocidad 440 metros por segundo, y se equivocó. Toca el paso que está mal.",
   [("f_{1}=\\dfrac{c}{2L}","La fórmula.","la fórmula"),
    ("f_{1}=\\dfrac{440}{0.5}","Este paso es el que falla.","falta el 2"),
    ("f_{1}=880\\ \\text{Hz}","Resultado.","da 880")],1,
   "En el denominador va 2L, y no L. Entonces f1 es 440 entre 1, o sea 440 hertz.",
   "f_{1}=\\dfrac{440}{2\\,(0.5)}=440\\ \\text{Hz}","Calcula 2 por L."),
 ordenar("Estos son los pasos para obtener la frecuencia del modo n de una cuerda, pero están desordenados.",
   [("u=F(x)\\,G(t)","Se separan las variables"),
    ("F=\\operatorname{sen}(n\\pi x/L)","Los extremos fijos dan F"),
    ("G=\\cos(n\\pi ct/L)","Se obtiene la oscilación en el tiempo"),
    ("f_{n}=nc/(2L)","Se lee la frecuencia")],[2,0,3,1],
   "Primero se separa, después F, luego G y por último se lee la frecuencia.","Se empieza separando las variables."),
]
S+=cierre("Mini simulacro de la cuerda vibrante",[
 banco("es_c2_12","La ecuación de onda unidimensional."),
 banco("es_c2_14","Los armónicos son múltiplos de la fundamental."),
 banco("es_c2_15","La fundamental con L 0.5 y c 440.")])
prac=[
 {"titulo":"Dos modos","grafica":{"draw":1},"bloques":[P("La forma inicial es la suma de dos modos."),EQ("u(x,0)=\\operatorname{sen}x+\\tfrac{1}{2}\\operatorname{sen}2x")]},
 {"titulo":"Avanza el tiempo","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen los factores de oscilación de cada modo.")]},
 {"titulo":"Medio periodo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3.14,"bloques":[EQ("\\cos\\pi=-1,\\quad\\cos2\\pi=1"),P("Con t igual a pi, el modo uno cambió de signo y el modo dos quedó igual.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3.14},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El modo n oscila con coseno de n t."}]}]
preg={"tex":"u_{tt}=u_{xx},\\ u(0,t)=u(\\pi,t)=0,\\ u_t(x,0)=0.\\ \\text{El modo 3 es}","opciones":["$\\operatorname{sen}3x\\cos3t$","$\\operatorname{sen}3x\\,e^{-9t}$","$\\operatorname{sen}x\\cos3t$","$\\operatorname{sen}3x\\cos t$"],"correcta":0,
 "explicacion":"El modo n es seno de n x por coseno de n t. Con n igual a 3, es seno de 3x por coseno de 3t.",
 "verificacion":{"formula":"sin(3*pi/2)*cos(0)+0*x","a":0,"esperado":-1},
 "pistas":["Es una ecuación de onda, y no de calor.","El modo n oscila con coseno de n t.","Con n igual a 3, la parte de x y la de t tienen un 3."],
 "errores":["","Con el exponencial sería la ecuación de calor, y no la de onda.","Con seno de x no cumple los extremos para n igual a 3.","Con coseno de t la frecuencia no es la del modo 3."]}
res=["En la ecuación de onda cada modo seno de n x oscila como coseno de n c t, y no se apaga.","La frecuencia del modo n es n veces la fundamental, y la fundamental es c entre 2L.","Los extremos fijos y la separación de variables determinan los modos."]
write(lesson("es-m2-l4","Lección 4 de 5","Ecuación de onda y cuerda vibrante",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-onda.json")
