import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 3 Laplace, sistemas y series"
N=90
TS=[6.0*k/N for k in range(N+1)]
graf={"tipo":"plano","x":[-0.4,6.2],"y":[-0.6,2],"a":-3,"b":3,"inicio":0,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"(2+x)*exp(0-{t:.4f})-(1+x)*exp(0-2*{t:.4f})"] for t in TS],"c":2},{"t":"punto","p":["0","1"],"c":1}],
 "lecturas":[{"rotulo":"y'(0)","formula":"x"},{"rotulo":"y(1)","formula":"(2+x)*exp(0-1)-(1+x)*exp(0-2)"}],
 "etiquetas":["Velocidad inicial y'(0)","Valor y(1)"],"etiquetaSlider":"Velocidad inicial y'(0)",
 "alt":"La solución de y segunda más 3y prima más 2y igual a 0, con y de 0 igual a 1, para distintos valores de y prima de 0. Todas las curvas parten de 1 y decaen hacia 0"}
glos={"inversa":"La transformada inversa recupera la función de t a partir de su transformada. Se hace con la tabla, después de separar la expresión en fracciones parciales.",
 "parciales":"Las fracciones parciales descomponen una fracción grande en una suma de fracciones simples, cada una con una inversa conocida.",
 "pvi":"Un problema de valor inicial es una ecuación diferencial junto con los valores de la solución y sus derivadas en t igual a 0."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"El problema es y segunda más 3y prima más 2y igual a 0, con y de 0 igual a 1. Esta es la solución cuando y prima de 0 vale 0."],
 [4,8,"Se transforma la ecuación. Las derivadas se vuelven multiplicaciones por s y los valores iniciales quedan dentro. Sale Y de s igual a (s más 3 más a) sobre (s más 1)(s más 2)."],
 [8,14,"Con fracciones parciales y la tabla se invierte. La solución es (2 más a) e a la menos t, menos (1 más a) e a la menos 2t. Cambia a con el deslizador."],
 [14,18,"Con a igual a 3 la curva sube hasta cerca de 1.6 antes de decaer. Todas terminan en 0, porque los exponentes son negativos."],
 [18,22,"Con a igual a menos 1 desaparece el segundo término y queda y igual a e a la menos t, así que y de 1 vale 0.37."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,3],[14,3],[15,-1],[22,-1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("La transformada de Laplace convierte un problema de valor inicial en una ecuación con álgebra. Las derivadas se vuelven multiplicaciones por s, y los valores iniciales entran solos en la ecuación. Se despeja Y de s y se regresa a t con la {{gl:inversa|transformada inversa}}, usando {{gl:parciales|fracciones parciales}} y la tabla.")),
 sec("Un ejemplo","Un ejemplo",P("Mira este {{gl:pvi|problema de valor inicial}} y su solución."),EQ("y''+3y'+2y=0,\\qquad y(0)=1,\\ y'(0)=a"),{"t":"grafica","animar":"dibujar","alt":"La solución del problema"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La inversa de 1 sobre (s más 2) es e a la menos 2t. ¿Cuánto vale en t igual a 0 la inversa de 5 sobre (s más 2)?","opciones":[1,2,5,10],"correcta":5,"bien":"Muy bien. Vale 5, porque la constante sale multiplicando. Más abajo se ve cómo se usa.","mal":"Vale 5, porque 5 por e a la menos 2t en t igual a 0 es 5. Más abajo se ve cómo se usa."}),
 sec("Cambia el valor inicial","Valor inicial",P("Mira cómo cambia la solución con la velocidad inicial."),{"t":"acercando","ds":[-3,-1,0,3],"alt":"La solución para varias velocidades iniciales"},P("Todas las curvas parten de 1 y terminan en 0, pero la forma intermedia depende de la velocidad inicial.")),
 sec("Transformar las derivadas","Derivadas",P("La clave es cómo se transforman las derivadas. Los valores iniciales aparecen aquí."),
   PASOS([("\\mathcal{L}\\{y'\\}=sY(s)-y(0)","La primera derivada."),
          ("\\mathcal{L}\\{y''\\}=s^{2}Y(s)-s\\,y(0)-y'(0)","La segunda derivada."),
          ("s^{2}Y-s-a+3(sY-1)+2Y=0","Se aplica al ejemplo, con y de 0 igual a 1 y y prima de 0 igual a a."),
          ("Y(s)=\\dfrac{s+3+a}{(s+1)(s+2)}","Se despeja Y de s.")])),
 sec("Fracciones parciales e inversa","La inversa",P("Se separa Y en fracciones simples y se invierte cada una."),
   PASOS([("Y=\\dfrac{2+a}{s+1}-\\dfrac{1+a}{s+2}","Se halla A y B en A sobre (s más 1) más B sobre (s más 2)."),
          ("\\mathcal{L}^{-1}\\left\\{\\dfrac{1}{s-c}\\right\\}=e^{ct}","Esta fórmula de la tabla se usa con c igual a menos 1 y menos 2."),
          ("y=(2+a)e^{-t}-(1+a)e^{-2t}","La solución del problema.")]),
   OJO("Verifica siempre con los valores iniciales. En t igual a 0 la solución debe dar 1, porque 2 más a menos 1 menos a es 1.")),
 sec("Una tabla corta","Tabla corta",P("Estas inversas son las que más se usan."),
   PASOS([("\\mathcal{L}^{-1}\\left\\{\\dfrac{1}{s-a}\\right\\}=e^{at}","Una exponencial."),
          ("\\mathcal{L}^{-1}\\left\\{\\dfrac{b}{s^{2}+b^{2}}\\right\\}=\\operatorname{sen}bt,\\quad \\mathcal{L}^{-1}\\left\\{\\dfrac{s}{s^{2}+b^{2}}\\right\\}=\\cos bt","Seno y coseno. El seno lleva b en el numerador."),
          ("\\mathcal{L}^{-1}\\left\\{\\dfrac{n!}{s^{n+1}}\\right\\}=t^{n}","Una potencia de t.")])),
 eng("Un circuito con bobina","Al cerrar un interruptor en un circuito con una bobina y una resistencia, la corriente no salta al valor final, sube poco a poco. La ecuación es de primer orden y con Laplace se resuelve en pocos pasos.","L\\,i'+R\\,i=V,\\quad i(0)=0",
   [("Bobina","0.5 H"),("Resistencia","10 ohmios"),("Fuente","12 V")],"Con estos datos la ecuación es i prima más 20i igual a 24, y la transformada da I igual a 24 sobre s por (s más 20), que se separa en 1.2 sobre s menos 1.2 sobre (s más 20). La corriente es 1.2 por (1 menos e a la menos 20t), amperios. La constante de tiempo es 0.05 segundos y en 0.15 segundos llega al 95 por ciento del valor final de 1.2 amperios. Es un modelo ideal, porque no incluye la resistencia interna de la fuente."),
 completar("Se transforma la segunda derivada con los valores iniciales.","\\mathcal{L}\\{y''\\}=s^{2}Y(s)-s\\,y(0)-[[hueco]]",
   [("y'(0)","la derivada inicial"),("y(0)","el valor inicial"),("Y(s)","la transformada")],0,
   ["","El valor inicial ya apareció multiplicado por s. Lo que falta es el de la derivada.","La transformada ya aparece en el primer término, con s al cuadrado. Falta un valor inicial."],"Aparecen y de 0 y y prima de 0.","Se resta primero s por y de 0 y luego y prima de 0."),
 error("Alguien resolvió un problema de valor inicial con Laplace y se equivocó en un paso. Toca el paso que está mal.",
   [("y''+4y=0,\\ y(0)=0,\\ y'(0)=2\\ \\Rightarrow\\ s^{2}Y-2+4Y=0","Se transforma la ecuación.","se transforma la ecuación y queda s cuadrado Y menos 2 más 4Y"),
    ("Y=\\dfrac{2}{s^{2}+4}","Se despeja Y.","Y es 2 sobre s cuadrado más 4"),
    ("y=2\\operatorname{sen}2t","Este paso es el que falla.","y es 2 seno de 2t")],2,
   "La fórmula del seno ya trae el b en el numerador. Con b igual a 2, 2 sobre s cuadrado más 4 es justo la transformada de seno de 2t, sin factor extra.",
   "y=\\operatorname{sen}2t","Compara el numerador con el b de la tabla."),
 ordenar("Estos son los pasos para resolver y prima más y igual a 1, con y de 0 igual a 0, pero están desordenados.",
   [("sY+Y=\\dfrac{1}{s}","Se transforma la ecuación"),
    ("Y=\\dfrac{1}{s(s+1)}","Se despeja Y"),
    ("Y=\\dfrac{1}{s}-\\dfrac{1}{s+1}","Fracciones parciales"),
    ("y=1-e^{-t}","La inversa")],[2,0,3,1],
   "Se transforma, se despeja, se separa en fracciones parciales y se invierte con la tabla.","Se empieza transformando la ecuación."),
]
S+=cierre("Mini simulacro de Laplace inversa",[
 banco("ed_c3_02","Se usa $\\mathcal{L}\\{\\sin bt\\}=\\dfrac{b}{s^2+b^2}$. Falta el $b=2$ del numerador, así que se divide entre $2$."),
 banco("ed_c3_03","Al derivar en $t$ se multiplica por $s$ y se resta el valor inicial."),
 banco("ed_c3_11","Se invierte $\\mathcal{L}\\{e^{at}\\}=\\dfrac{1}{s-a}$ con $a=3$.")])
prac=[
 {"titulo":"El problema","grafica":{"draw":1,"guide":1},"bloques":[P("Una ecuación de segundo orden con y de 0 igual a 1 y y prima de 0 igual a a."),EQ("y''+3y'+2y=0")]},
 {"titulo":"Cambia a","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee la velocidad inicial y el valor de y en t igual a 1.")]},
 {"titulo":"Un caso simple","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":-1,"bloques":[EQ("a=-1\\ \\Rightarrow\\ y=e^{-t}"),P("Con a igual a menos 1 solo queda una exponencial, y y de 1 vale 0.37.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":-1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Transforma, despeja Y e invierte."}]}]
preg={"tex":"y'+3y=0,\\ y(0)=2\\ \\text{tiene como solución}","opciones":["$2e^{-3t}$","$2e^{3t}$","$e^{-3t}$","$\\tfrac{2}{3}e^{-3t}$"],"correcta":0,
 "explicacion":"La transformada da sY menos 2 más 3Y igual a 0, o sea Y igual a 2 sobre (s más 3). Su inversa es 2 por e a la menos 3t.",
 "verificacion":{"formula":"(0-6*exp(0-3*x))+3*2*exp(0-3*x)","a":1,"esperado":0},
 "pistas":["Transforma la ecuación con y de 0 igual a 2.","Queda sY menos 2 más 3Y igual a 0.","Y es 2 sobre (s más 3)."],
 "errores":["","El signo del exponente sale de s más 3, que corresponde a menos 3, no a más 3.","Se perdió el valor inicial 2. Aparece como numerador de Y.","Con 2 sobre (s más 3) no se divide entre 3. La inversa de 1 sobre (s más 3) es e a la menos 3t."]}
res=["Laplace convierte las derivadas en multiplicaciones por s y mete los valores iniciales en la ecuación.","Se despeja Y de s, se separa en fracciones parciales y se invierte con la tabla.","Siempre se verifica con los valores iniciales."]
write(lesson("edo-m3-l2","Lección 2 de 5","Laplace inversa y problemas de valor inicial",30,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=9,curso="Ecuaciones Diferenciales"),"edo-inversa.json")
