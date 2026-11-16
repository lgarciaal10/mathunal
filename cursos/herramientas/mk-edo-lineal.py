import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 1 EDO de primer orden"
EL=[]
for i in range(0,12):
    for j in range(0,7):
        x0=i*0.5; y0=j*0.5; m=4-2*y0; n=math.hypot(1,m); d=0.2
        EL.append({"t":"segmento","a":[f"{x0-d/n:.4f}",f"{y0-d*m/n:.4f}"],"b":[f"{x0+d/n:.4f}",f"{y0+d*m/n:.4f}"],"c":0})
EL=[e for e in EL if all(-0.95<float(e[k][0])<6.4 and -0.95<float(e[k][1])<3.05 for k in 'ab')]
TR=[[f"{5*k/40:.4f}",f"2+(x-2)*exp(0-2*({5*k/40:.4f}))"] for k in range(41)]
EL+=[{"t":"recta","p":["0","2"],"dir":["1","0"],"guion":True,"c":3,"nombre":"y = 2","guia":True},{"t":"trazo","puntos":TR,"c":2},{"t":"punto","p":["0","x"],"c":1,"nombre":"y(0)"}]
graf={"tipo":"plano","x":[-1,6.5],"y":[-1,3.1],"a":0,"b":3,"inicio":0.5,"elementos":EL,
 "lecturas":[{"rotulo":"y(0)","formula":"x"},{"rotulo":"y(1)","formula":"2+(x-2)*exp(-2)"}],
 "etiquetas":["Valor inicial","Valor en x igual a 1"],"etiquetaSlider":"Valor inicial y(0)",
 "alt":"El campo de pendientes de y prima más 2y igual a 4 y la curva solución que parte de la altura inicial y se acerca a la recta y igual a 2"}
glos={"lineal":"Una EDO lineal de primer orden se puede escribir como y prima más p de x por y igual a q de x, con la y y su derivada solo a la primera potencia.",
 "factor":"El factor integrante es una función que, al multiplicar la ecuación, convierte el lado izquierdo en la derivada de un producto.",
 "estacionaria":"La solución estacionaria es la que no cambia con el tiempo. Es el valor al que se acercan las demás soluciones."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación y prima más 2y igual a 4 dice que la pendiente es 4 menos 2y. Es cero cuando y vale 2."],
 [4,8,"Por eso las soluciones que parten abajo suben, y las que parten arriba bajan, hacia la recta y igual a 2."],
 [8,14,"Al cambiar el valor inicial, la curva cambia, pero todas se acercan a 2."],
 [14,18,"La solución es y igual a 2 más (y de 0 menos 2) por e a la menos 2x. El término con exponencial se va apagando."],
 [18,22,"Con y de 0 igual a 0.5, la solución vale 1.80 en x igual a 1."]],
 "canales":{"draw":[[0.3,0],[7.5,1]],"d":[[8,0.5],[10,2.8],[12,0.2],[14,0.5],[22,0.5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Una EDO {{gl:lineal|lineal}} de primer orden aparece cuando algo cambia en proporción a lo que ya hay, más una entrada externa. Se resuelve multiplicando por una función especial, el {{gl:factor|factor integrante}}, que deja el lado izquierdo como la derivada de un producto. Se usa en circuitos, mezclas y enfriamiento con ambiente variable.")),
 sec("Un ejemplo","Un ejemplo",P("Mira esta ecuación, que mezcla la solución con una entrada constante."),EQ("y'+2y=4"),{"t":"grafica","animar":"dibujar","alt":"El campo de pendientes y una solución"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La pendiente es 4 menos 2y. Cuando y vale 2, ¿cuánto vale la pendiente?","opciones":[-2,0,2,4],"correcta":0,"bien":"Muy bien. Vale 0, y ahí la solución es plana. Más abajo se ve el campo.","mal":"Vale 0, porque 4 menos 2 por 2 es 0. Ahí la solución es plana. Más abajo se ve el campo."}),
 sec("Hacia la solución estacionaria","Estacionaria",P("Mira cómo se mueve la solución para valores iniciales distintos."),{"t":"acercando","ds":[0.2,0.5,2.8,3],"alt":"La curva solución para varios valores iniciales"},P("Todas las curvas se acercan a la recta y igual a 2, que es la {{gl:estacionaria|solución estacionaria}}.")),
 sec("El factor integrante","Factor integrante",P("Primero se escribe la ecuación en la forma y prima más p de x por y igual a q de x. Después se calcula el factor integrante."),
   EQ("\\mu(x)=e^{\\int p(x)\\,dx}"),
   PASOS([("y'+2y=4,\\quad p(x)=2,\\quad q(x)=4","Es la forma estándar."),
          ("\\mu(x)=e^{\\int 2\\,dx}=e^{2x}","Se integra p. No hace falta sumar constante."),
          ("\\left(e^{2x}y\\right)'=4e^{2x}","Al multiplicar por mu, el lado izquierdo es la derivada de mu por y."),
          ("e^{2x}y=2e^{2x}+C\\ \\Rightarrow\\ y=2+Ce^{-2x}","Se integra y se despeja.")]),
   OJO("Se multiplica toda la ecuación por mu, incluido el lado derecho.")),
 sec("Con condición inicial","Condición inicial",PASOS([("y(0)=y_{0}\\ \\Rightarrow\\ y_{0}=2+C","Se reemplaza x igual a 0."),
          ("y=2+(y_{0}-2)\\,e^{-2x}","Es la solución. Se acerca a 2 cuando x crece."),
          ("y_{0}=0.5\\ \\Rightarrow\\ y(1)=2-1.5\\,e^{-2}\\approx 1.797","Con el valor inicial de la gráfica.")])),
 sec("Con un coeficiente variable","Coeficiente variable",P("El método es el mismo si el lado derecho depende de x."),
   PASOS([("y'+y=x\\ \\Rightarrow\\ \\mu=e^{x}","Aquí p vale 1."),
          ("\\left(e^{x}y\\right)'=x\\,e^{x}\\ \\Rightarrow\\ e^{x}y=(x-1)e^{x}+C","Se integra por partes el lado derecho."),
          ("y=x-1+Ce^{-x}","Se divide entre mu.")])),
 eng("La carga de un condensador","Un condensador se carga a través de una resistencia con una fuente constante. El voltaje del condensador cumple una EDO lineal, y su solución muestra cómo se acerca al voltaje de la fuente.","\\tau\\,v'+v=V,\\quad \\tau=RC",
   [("Fuente","12 V"),("Constante de tiempo","1 s"),("Voltaje a los 2 s","10.4 V")],"Con el condensador descargado al inicio, la solución es v igual a 12 por (1 menos e a la menos t). A los 2 segundos vale 12 por (1 menos e a la menos 2), o sea unos 10.4 voltios. Es un modelo simplificado, porque supone un condensador y una resistencia ideales."),
 completar("Se halla el factor integrante de y prima más 2y igual a 4. Falta el exponente.","\\mu(x)=e^{[[hueco]]}",
   [("2x","dos x"),("x^{2}","x al cuadrado"),("2","dos")],0,
   ["","Eso saldría si p fuera x. Aquí p vale 2, y su integral es 2x.","Falta integrar. La integral de 2 con respecto a x es 2x."],"Integra p de x, que vale 2.","La integral de 2 con respecto a x es 2x, así que mu es e a la 2x."),
 error("Alguien calculó un factor integrante y se equivocó en un paso. Toca el paso que está mal.",
   [("y'+2y=4,\\quad p(x)=2","Se identifica p.","y prima más 2y igual a 4, con p igual a 2"),
    ("\\mu=e^{p(x)}=e^{2}","Este paso es el que falla.","mu es e elevado a p, o sea e al cuadrado"),
    ("\\left(e^{2}y\\right)'=4e^{2}","Depende del paso anterior.","La derivada de e al cuadrado por y es 4 por e al cuadrado")],1,
   "El exponente del factor integrante es la integral de p, no p. Hay que integrar, y el resultado es e a la 2x, que sí tiene derivada que da el término 2y.",
   "\\mu=e^{\\int p\\,dx}=e^{2x}","Comprueba si la derivada de mu por y da y prima más 2y."),
 ordenar("Estos son los pasos para resolver y prima más y igual a x, pero están desordenados.",
   [("\\mu=e^{\\int 1\\,dx}=e^{x}","Se calcula el factor integrante"),
    ("\\left(e^{x}y\\right)'=x\\,e^{x}","Se multiplica y se reconoce la derivada"),
    ("e^{x}y=(x-1)e^{x}+C","Se integra por partes"),
    ("y=x-1+Ce^{-x}","Se despeja y")],[2,0,3,1],
   "Se halla mu, se multiplica, se integra y se despeja y.","Primero se calcula el factor integrante."),
]
S+=cierre("Mini simulacro de EDO lineales",[banco("ed_c1_09","Es la definición del factor integrante."),banco("ed_c1_03","Con $\\mu=e^x$ queda $(e^xy)'=e^{2x}$, así que $y=\\frac12e^x+Ce^{-x}$."),banco("ed_c1_10","La solución es $y=5e^{-x}$, y $y(\\ln 2)=5/2=2.5$.")])
prac=[
 {"titulo":"El campo","grafica":{"draw":1,"guide":1},"bloques":[P("La ecuación fija una pendiente en cada punto."),EQ("y'+2y=4")]},
 {"titulo":"Cambia y(0)","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La solución parte del valor inicial y se acerca a la recta y igual a 2.")]},
 {"titulo":"La solución","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.5,"bloques":[EQ("y=2+(y_{0}-2)\\,e^{-2x}"),P("Con y de 0 igual a 0.5, el término exponencial se apaga y la solución se acerca a 2.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Halla el factor integrante, integra y usa la condición inicial."}]}]
preg={"tex":"y'+3y=6,\\ y(0)=1\\ \\Rightarrow\\ y(1)","opciones":["$1.950$","$2$","$1$","$0.950$"],"correcta":0,
 "explicacion":"El factor integrante es e a la 3x. Queda la derivada de e a la 3x por y igual a 6 por e a la 3x, y se integra, e a la 3x por y igual a 2 por e a la 3x más C. Entonces y es 2 más C por e a la menos 3x. Con y de 0 igual a 1, C es menos 1. En x igual a 1 vale 2 menos e a la menos 3, o sea 1.950.",
 "verificacion":{"formula":"2-exp(0-3)+0*x","a":0,"esperado":1.9502},
 "pistas":["Calcula el factor integrante, e a la integral de 3.","Queda y igual a 2 más C por e a la menos 3x.","Con y de 0 igual a 1, C vale menos 1. Evalúa en x igual a 1."],
 "errores":["","Ese es el valor estacionario. La solución todavía no lo alcanza en x igual a 1.","Ese es el valor inicial. La solución ya cambió en x igual a 1.","Revisa la cuenta. 2 menos e a la menos 3 es 2 menos 0.0498."]}
res=["Una EDO lineal se escribe y prima más p y igual a q y se resuelve con el factor integrante mu igual a e a la integral de p.","El lado izquierdo se vuelve la derivada de mu por y, y se integra.","Las soluciones se acercan a la solución estacionaria cuando los términos con exponencial negativo se apagan."]
write(lesson("edo-m1-l3","Lección 3 de 6","EDO lineal de primer orden",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Ecuaciones Diferenciales"),"edo-lineal.json")
