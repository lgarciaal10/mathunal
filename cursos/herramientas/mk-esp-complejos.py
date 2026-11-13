import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 3 Ecuación de Laplace y variable compleja"
RE="exp(0.34657359*x)*cos(0.78539816*x)"
IM="exp(0.34657359*x)*sin(0.78539816*x)"
EL=[{"t":"vector","b":["1","1"],"nombre":"z","c":3},
    {"t":"vector","b":[RE,IM],"nombre":"w","c":0},
    {"t":"punto","p":["1","0"],"c":1}]
graf={"tipo":"plano","x":[-5.5,2.5],"y":[-1.4,3.2],"a":0,"b":4,"inicio":1,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"módulo de z a la n, igual a 2 elevado a n sobre 2","formula":"exp(0.34657359*x)"},{"rotulo":"ángulo de z a la n en grados, 45 por n","formula":"45*x"}],
 "etiquetas":["z igual a 1 más i, con módulo raíz de 2 y ángulo 45 grados","z a la n, cuyo módulo crece y cuyo ángulo se suma"],"etiquetaSlider":"Potencia n, de 0 a 4",
 "alt":"En el plano complejo, el número z igual a 1 más i, con módulo raíz de 2 y ángulo de 45 grados. Al elevarlo a la potencia n el módulo se multiplica por raíz de 2 y el ángulo gira otros 45 grados, de modo que z a la 4 es menos 4"}
glos={"polar":"La forma polar escribe un número complejo como r por e elevado a i theta, con r el módulo y theta el ángulo.",
 "euler":"La fórmula de Euler dice que e elevado a i theta es coseno de theta más i seno de theta.",
 "analitica":"Una función es analítica en un punto si es derivable en el sentido complejo en todo un entorno del punto.",
 "modulo":"El módulo de un número complejo es su distancia al origen."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"El número 1 más i está a raíz de 2 del origen, con un ángulo de 45 grados."],
 [4,10,"Al elevarlo a la n, el módulo se eleva a la n y el ángulo se multiplica por n."],
 [10,16,"Con n igual a 2, el módulo es 2 y el ángulo es 90 grados, o sea z al cuadrado vale 2i."],
 [16,20,"Con n igual a 4, el ángulo es 180 grados y z a la 4 vale menos 4."],
 [20,24,"Por eso 1 más i elevado a la 8 vale 16, porque el módulo es 2 a la 4 y el ángulo da una vuelta completa."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,2],[13,3],[16,4],[18,4],[24,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Un número complejo se escribe en {{gl:polar|forma polar}} como r por e elevado a i theta, con la {{gl:euler|fórmula de Euler}}. Con esa forma, multiplicar es sumar ángulos y multiplicar {{gl:modulo|módulos}}, y elevar a una potencia es sencillo. Una función de variable compleja es {{gl:analitica|analítica}} cuando es derivable en todo un entorno.")),
 sec("Un ejemplo","Un ejemplo",P("El número 1 más i tiene módulo raíz de 2 y ángulo 45 grados. Cambia la potencia n y mira cómo gira y crece."),EQ("z=1+i=\\sqrt{2}\\,e^{i\\pi/4},\\qquad z^{n}=2^{n/2}\\,e^{i\\,n\\pi/4}"),{"t":"grafica","animar":"dibujar","alt":"Las potencias de 1 más i en el plano complejo"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El número 1 más i tiene módulo raíz de 2. ¿Cuánto vale el módulo de su cuadrado?","opciones":[2,1,4,"raíz de 2"],"correcta":2,"bien":"Muy bien. El módulo se eleva al cuadrado, y raíz de 2 al cuadrado es 2.","mal":"El módulo del cuadrado es el cuadrado del módulo. Raíz de 2 al cuadrado vale 2."}),
 sec("Las potencias","Potencias",P("Mira z a la n con n igual a 0, 1, 2 y 4."),{"t":"acercando","ds":[0,1,2,4],"alt":"Potencias de 1 más i"},P("Con n igual a 2 sale 2i, y con n igual a 4 sale menos 4.")),
 sec("Forma polar y Euler","Polar",P("Se pasa de la forma rectangular a la polar con el módulo y el ángulo."),
   PASOS([("|z|=\\sqrt{1^{2}+1^{2}}=\\sqrt{2}","El módulo."),
          ("\\theta=\\arctan\\dfrac{1}{1}=\\dfrac{\\pi}{4}","El ángulo, porque está en el primer cuadrante."),
          ("z=\\sqrt{2}\\,e^{i\\pi/4}","La forma polar."),
          ("z^{8}=(\\sqrt{2})^{8}e^{i\\,8\\pi/4}=16\\,e^{i\\,2\\pi}=16","La potencia 8, con módulo 16 y ángulo de una vuelta.")]),
   OJO("El ángulo depende del cuadrante. Con la arcotangente sola se puede confundir el segundo cuadrante con el cuarto, así que mira los signos de las partes real e imaginaria.")),
 sec("Euler y analiticidad","Euler",P("De la fórmula de Euler salen valores famosos, y la analiticidad usa la derivada compleja."),
   PASOS([("e^{i\\theta}=\\cos\\theta+i\\operatorname{sen}\\theta","Fórmula de Euler."),
          ("e^{i\\pi}=\\cos\\pi+i\\operatorname{sen}\\pi=-1","El valor en theta igual a pi."),
          ("f'(z_0)=\\displaystyle\\lim_{h\\to0}\\dfrac{f(z_0+h)-f(z_0)}{h}","La derivada compleja, con h complejo."),
          ("f\\ \\text{es derivable en un entorno de}\\ z_0","Analítica es derivable en un entorno, y no solo en un punto.")]),
   OJO("Derivable solo en un punto no alcanza para ser analítica. La función módulo al cuadrado, por ejemplo, es derivable solo en cero, y no es analítica en ninguna parte.")),
 eng("La corriente alterna con fasores","Una corriente alterna de 50 amperios de amplitud y fase 45 grados se representa con un número complejo. Con la forma polar es fácil sumar corrientes y aplicar la impedancia.","I=50\\,e^{i\\pi/4}=25\\sqrt{2}\\,(1+i)",
   [("Amplitud","50 A"),("Fase","45 grados"),("Parte real","cerca de 35.4 A")],"Los ingenieros eléctricos usan fasores para sumar señales de la misma frecuencia. Con la forma polar, multiplicar por una impedancia es multiplicar módulos y sumar fases, y el cálculo se vuelve muy corto."),
 completar("Con la fórmula de Euler, e elevado a i pi vale [[hueco]].","e^{i\\pi}=[[hueco]]",
   [("-1","menos uno"),("1","uno"),("i","i")],0,
   ["","Con 1 se confunde con e elevado a 0.","Con i se confunde con e elevado a i pi medios."],"Coseno de pi es menos 1 y seno de pi es 0.","Vale menos uno."),
 error("Alguien escribió 1 más i en forma polar y se equivocó. Toca el paso que está mal.",
   [("|z|=\\sqrt{1+1}=\\sqrt{2}","Módulo.","el módulo"),
    ("\\theta=\\dfrac{\\pi}{2}","Este paso es el que falla.","ángulo pi medios"),
    ("z=\\sqrt{2}\\,e^{i\\pi/2}","Resultado.","la polar")],1,
   "El ángulo de 1 más i es arctan de 1 sobre 1, o sea pi cuartos. Pi medios sería el de la i sola.",
   "\\theta=\\arctan(1)=\\dfrac{\\pi}{4}","Divide la parte imaginaria entre la real."),
 ordenar("Estos son los pasos para calcular 1 más i elevado a la 8, pero están desordenados.",
   [("|z|=\\sqrt{2}","Módulo"),
    ("\\theta=\\dfrac{\\pi}{4}","Ángulo"),
    ("z^{8}=(\\sqrt{2})^{8}e^{i\\,8\\pi/4}","Se aplica la potencia"),
    ("z^{8}=16","Se simplifica")],[2,0,3,1],
   "Primero el módulo, luego el ángulo, después la potencia y por último se simplifica.","Se empieza con el módulo."),
]
S+=cierre("Mini simulacro de números complejos",[
 banco("es_c3_13","El valor de (1+i) a la 8."),
 banco("es_c3_14","La fórmula de Euler en theta igual a pi."),
 banco("es_c3_15","La forma polar de 1 más i."),
 banco("es_c3_16","Qué significa ser analítica.")])
prac=[
 {"titulo":"El número z","grafica":{"draw":1},"bloques":[P("El número es 1 más i."),EQ("z=1+i")]},
 {"titulo":"Eleva a la n","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Solo importan los valores enteros de n. Abajo se leen el módulo y el ángulo.")]},
 {"titulo":"La cuarta potencia","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":4,"bloques":[EQ("z^{4}=4\\,e^{i\\pi}=-4"),P("Con n igual a 4 el ángulo es 180 grados y el módulo es 4.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":4},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Se elevan los módulos y se suman los ángulos."}]}]
preg={"tex":"\\text{El valor de }(1+i)^{4}\\text{ es}","opciones":["$-4$","$4$","$4i$","$-4i$"],"correcta":0,
 "explicacion":"El módulo es raíz de 2 elevado a 4, o sea 4, y el ángulo es 4 por pi cuartos, o sea pi. Da 4 por e a la i pi, que es menos 4.",
 "verificacion":{"formula":"4*cos(pi)+0*x","a":0,"esperado":-4},
 "pistas":["Pasa 1 más i a forma polar.","El módulo se eleva a la 4, y el ángulo se multiplica por 4.","El ángulo queda en pi."],
 "errores":["","Con signo positivo se olvidó que el ángulo es pi y no una vuelta completa.","Con 4i se tomó un ángulo de pi medios.","Con menos 4i se tomó un ángulo de 3 pi medios."]}
res=["Un número complejo se escribe como r por e elevado a i theta, con r el módulo y theta el ángulo.","Al elevar a la n, el módulo se eleva a la n y el ángulo se multiplica por n.","Una función es analítica si es derivable en un entorno del punto."]
write(lesson("es-m3-l1","Lección 1 de 5","Números complejos y funciones analíticas",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-complejos.json")
