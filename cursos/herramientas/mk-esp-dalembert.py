import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 2 Transformada de Fourier y EDP de evolución"
XS=[round(-6+0.25*i,3) for i in range(49)]
EL=[{"t":"trazo","puntos":[[str(xv),f"0.5*(exp(-(({xv})-x)*(({xv})-x))+exp(-(({xv})+x)*(({xv})+x)))"] for xv in XS],"c":0},
    {"t":"trazo","puntos":[[str(xv),f"0.5*exp(-(({xv})-x)*(({xv})-x))"] for xv in XS],"c":3}]
graf={"tipo":"plano","x":[-6.5,6.5],"y":[-0.3,1.2],"a":0,"b":5,"inicio":0,"elementos":EL,
 "lecturas":[{"rotulo":"posición de cada pulso, x igual a c por t","formula":"x"},{"rotulo":"valor en x igual a 0, e elevado a menos t al cuadrado","formula":"exp(-x*x)"}],
 "etiquetas":["El pulso que viaja a la derecha","La suma de los dos, que es la cuerda"],"etiquetaSlider":"Tiempo t, de 0 a 5",
 "alt":"Un pulso inicial en forma de campana en el centro de una cuerda infinita se divide en dos pulsos de la mitad de altura. Uno viaja a la derecha y el otro a la izquierda, con velocidad c igual a 1. La curva verde es solo el pulso que va a la derecha"}
glos={"dalembert":"La fórmula de D'Alembert da la solución de la ecuación de onda en una cuerda infinita como suma de dos ondas viajeras.",
 "viajera":"Una onda viajera es una forma que se desplaza sin cambiar. F de x menos c t va a la derecha, y F de x más c t va a la izquierda.",
 "caracteristica":"Las rectas x menos c t igual a una constante, y x más c t igual a una constante, son las características, por donde viaja la información.",
 "velocidad":"La velocidad inicial g de x aporta un término de integral. Si la cuerda parte del reposo, ese término no aparece."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Una cuerda infinita tiene un pulso en forma de campana en el centro, y parte del reposo."],
 [4,10,"La fórmula de D'Alembert dice que el pulso se parte en dos de la mitad de altura, y cada uno viaja con velocidad c."],
 [10,16,"Con t igual a 2 hay dos pulsos de altura 0.5 en x igual a más y menos 2, y el centro ya casi vale cero."],
 [16,20,"Cada pulso conserva su forma mientras viaja, porque en una cuerda ideal no hay disipación."],
 [20,24,"La solución es una suma de dos ondas viajeras, una hacia cada lado."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,1],[13,2],[16,2],[18,4],[24,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("En una cuerda infinita la ecuación de onda tiene una solución explícita, la {{gl:dalembert|fórmula de D'Alembert}}. La solución es una suma de dos {{gl:viajera|ondas viajeras}}, una hacia cada lado, que se desplazan a velocidad c. Siguen las {{gl:caracteristica|características}}. Si la cuerda no parte del reposo, la {{gl:velocidad|velocidad inicial}} suma un término de integral.")),
 sec("Un ejemplo","Un ejemplo",P("El pulso inicial es una campana en el centro. Mueve el tiempo y mira cómo se parte en dos."),EQ("u(x,t)=\\tfrac{1}{2}\\big[f(x+ct)+f(x-ct)\\big],\\qquad f(x)=e^{-x^{2}}"),{"t":"grafica","animar":"dibujar","alt":"El pulso partiéndose en dos ondas viajeras"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La función F de x menos c t, con c positiva, ¿hacia dónde se desplaza al crecer t?","opciones":["Hacia la derecha","Hacia la izquierda","No se mueve","Se apaga"],"correcta":"Hacia la derecha","bien":"Muy bien. Para mantener x menos c t constante, x debe crecer con t.","mal":"Va hacia la derecha. Para mantener x menos c t constante, x tiene que crecer con el tiempo."}),
 sec("El pulso se parte","Pulsos",P("Mira la cuerda con t igual a 0, 1, 2 y 4."),{"t":"acercando","ds":[0,1,2,4],"alt":"La cuerda en cuatro instantes"},P("A t igual a 2 hay dos pulsos de la mitad de altura, y están en x igual a más y menos 2.")),
 sec("La fórmula","Fórmula",P("La solución general es suma de dos ondas viajeras. Los datos iniciales fijan cuáles."),
   PASOS([("u(x,t)=F(x-ct)+G(x+ct)","Toda solución de la ecuación de onda tiene esta forma."),
          ("u(x,0)=f(x),\\ u_{t}(x,0)=0\\ \\Rightarrow\\ F=G=\\tfrac{1}{2}f","Con velocidad inicial cero, las dos ondas son la mitad de f."),
          ("u=\\tfrac{1}{2}\\big[f(x-ct)+f(x+ct)\\big]","La fórmula de D'Alembert."),
          ("u_{t}(x,0)=g\\ \\Rightarrow\\ +\\dfrac{1}{2c}\\displaystyle\\int_{x-ct}^{x+ct}g(s)\\,ds","Si hay velocidad inicial, se suma este término.")]),
   OJO("Cada onda lleva la mitad de la forma inicial. Si se olvida el un medio, la altura inicial en t igual a 0 saldría el doble.")),
 sec("Un cálculo","Cálculo",P("Se aplica la fórmula con f igual a seno de x, y c igual a 2."),
   PASOS([("u=\\tfrac{1}{2}\\big[\\operatorname{sen}(x+2t)+\\operatorname{sen}(x-2t)\\big]","D'Alembert con f igual a seno."),
          ("\\operatorname{sen}A+\\operatorname{sen}B=2\\operatorname{sen}\\dfrac{A+B}{2}\\cos\\dfrac{A-B}{2}","Identidad de suma de senos."),
          ("u=\\operatorname{sen}x\\cos2t","Coincide con el modo de la cuerda de largo pi."),
          ("x=\\dfrac{\\pi}{2},\\ t=\\dfrac{\\pi}{4}:\\ u=1\\cdot\\cos\\dfrac{\\pi}{2}=0","Un valor concreto.")]),
   OJO("Con f igual a seno de x, D'Alembert y la separación de variables dan el mismo resultado. Son dos caminos para la misma solución.")),
 eng("Un pulso en un cable largo","Un pulso de tensión viaja por un cable largo, y se parte en dos pulsos que se alejan en sentidos opuestos. La velocidad depende de las propiedades del cable.","c=\\sqrt{T/\\rho}",
   [("Tensión","100 N"),("Densidad lineal","0.25 kg/m"),("Velocidad","20 m/s")],"Con una velocidad de 20 metros por segundo, un pulso tarda 0.5 segundos en recorrer 10 metros. Mientras no llegue a un extremo, cada pulso mantiene su forma. Después aparece la reflexión, que no cubre esta fórmula de cuerda infinita."),
 completar("En la fórmula de D'Alembert, cuando la cuerda parte del reposo, u de x y t es [[hueco]] por la suma de f de x más c t y f de x menos c t.","u(x,t)=[[hueco]]\\big[f(x+ct)+f(x-ct)\\big]",
   [("\\dfrac{1}{2}","un medio"),("1","uno"),("2","dos")],0,
   ["","Con 1, la altura inicial en t igual a 0 sería el doble de f.","Con 2, sería aún más grande, y en t igual a 0 no daría f."],"Cada onda viajera lleva la mitad de la forma inicial.","El factor es un medio."),
 error("Alguien aplicó la fórmula de D'Alembert con f igual a seno de x y c igual a 2, y se equivocó. Toca el paso que está mal.",
   [("u=\\tfrac{1}{2}\\big[\\operatorname{sen}(x+2t)+\\operatorname{sen}(x-2t)\\big]","Se aplica la fórmula.","la fórmula"),
    ("u=\\operatorname{sen}x\\cos t","Este paso es el que falla.","queda coseno de t"),
    ("u\\!\\left(\\tfrac{\\pi}{2},\\tfrac{\\pi}{4}\\right)=\\cos\\tfrac{\\pi}{4}","Valor.","valor")],1,
   "La suma de senos da seno de x por coseno de 2t, y no de t. Con c igual a 2, el factor es coseno de 2t.",
   "u=\\operatorname{sen}x\\cos2t","Usa la identidad de suma de senos."),
 ordenar("Estos son los pasos para resolver la cuerda infinita con D'Alembert, pero están desordenados.",
   [("u=F(x-ct)+G(x+ct)","Se escribe la forma general"),
    ("F=G=f/2","Con reposo, se ajustan los datos"),
    ("u=\\tfrac{1}{2}[f(x-ct)+f(x+ct)]","Se obtiene la fórmula"),
    ("u(x_{0},t_{0})","Se calcula")],[2,0,3,1],
   "Primero la forma general, luego se ajustan los datos, después la fórmula y por último se evalúa.","Se empieza con la forma general."),
]
S+=cierre("Mini simulacro de la fórmula de D'Alembert",[
 banco("es_c2_17","La fórmula de D'Alembert."),
 banco("es_c2_18","El valor con c igual a 2 y f igual a seno.")])
prac=[
 {"titulo":"Pulso inicial","grafica":{"draw":1},"bloques":[P("La cuerda es infinita y parte del reposo."),EQ("f(x)=e^{-x^{2}}")]},
 {"titulo":"Avanza el tiempo","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la posición de cada pulso y el valor en el centro.")]},
 {"titulo":"Dos pulsos","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("u(0,2)=e^{-4}\\approx0.018"),P("Con t igual a 2 el centro casi vale cero, y hay dos pulsos en más y menos 2.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Cada pulso lleva un medio de la forma inicial."}]}]
preg={"tex":"u_{tt}=u_{xx},\\ u(x,0)=e^{-x^{2}},\\ u_t(x,0)=0.\\ \\text{El valor }u(0,1)\\text{ es}","opciones":["$e^{-1}$","$\\dfrac{1}{2}e^{-1}$","$e^{-2}$","$1$"],"correcta":0,
 "explicacion":"Con c igual a 1, u de 0 y 1 es un medio por f de 1 más f de menos 1, o sea un medio por dos e a la menos 1. Da e a la menos 1.",
 "verificacion":{"formula":"0.5*(exp(-1)+exp(-1))+0*x","a":0,"esperado":0.3679},
 "pistas":["Aplica D'Alembert con c igual a 1.","Evalúa f en x más t y en x menos t.","f de 1 y f de menos 1 valen lo mismo."],
 "errores":["","Un medio de e a la menos 1 olvida que hay dos ondas que se suman.","Con e a la menos 2 se evaluó f en 2, pero lo correcto es f en 1.","Con 1 sería el valor en t igual a 0, y no en t igual a 1."]}
res=["La fórmula de D'Alembert escribe la solución como suma de dos ondas viajeras, una hacia cada lado.","Si parte del reposo, cada onda lleva la mitad de la forma inicial.","Las ondas viajeras mantienen su forma, y se mueven a velocidad c."]
write(lesson("es-m2-l5","Lección 5 de 5","Fórmula de D'Alembert",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-dalembert.json")
