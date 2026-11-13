import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 2 Transformada de Fourier y EDP de evolución"
D=0.5
OM=[D*k+D/2 for k in range(40)]
def suma(xs):
    return "+".join(f"{math.sin(w)/w*D:.6f}*cos({w:.2f}*{xs})*(1+(x-{w:.2f})/(abs(x-{w:.2f})+0.000001))/2" for w in OM)
XS=[round(-2.5+0.125*i,3) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(xv),f"0.63662*({suma(str(xv))})"] for xv in XS],"c":0}]
EL+= [{"t":"segmento","a":[-1,0],"b":[1,0],"c":3}]
graf={"tipo":"plano","x":[-3,3],"y":[-0.4,1.3],"a":0.5,"b":20,"inicio":20,"elementos":EL,
 "lecturas":[{"rotulo":"frecuencia máxima W","formula":"x"},{"rotulo":"valor de la integral en x igual a 0","formula":"0.63662*("+suma("0")+")"}],
 "etiquetas":["Con W grande se acerca al pulso","El pulso original vale 1 entre menos 1 y 1"],"etiquetaSlider":"Frecuencia máxima W, de 0.5 a 20",
 "alt":"La integral de Fourier del pulso que vale 1 entre menos 1 y 1, cortada en la frecuencia W. Con W pequeña es una campana suave, y al crecer W se acerca a la forma rectangular, con pequeñas ondas cerca de los saltos"}
glos={"integral":"La integral de Fourier representa una función no periódica como una suma continua de ondas de todas las frecuencias.",
 "pulso":"El pulso es la función que vale 1 entre menos 1 y 1, y cero afuera.",
 "dirichlet":"La integral de Dirichlet es la integral de seno de omega entre omega, de cero a infinito, y vale pi medios.",
 "salto":"En un salto, la integral converge al promedio de los límites a cada lado."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"El pulso vale 1 entre menos 1 y 1, y no es periódico, así que no sirve una serie de Fourier."],
 [4,10,"Se usa una suma continua de ondas coseno, con frecuencias omega desde 0 hasta una frecuencia máxima W."],
 [10,16,"Con W igual a 2 se ve una campana suave. Con W igual a 5, ya aparece la forma de caja, con pequeñas ondas."],
 [16,20,"Con W igual a 20 la caja es casi perfecta, y en x igual a 1 la integral da un promedio, un medio."],
 [20,24,"Cuantas más frecuencias se incluyen, más fiel es la reconstrucción de la función."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.5],[8,0.5],[10,2],[13,5],[16,5],[18,20],[24,20]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("La {{gl:integral|integral de Fourier}} extiende la serie a funciones que no son periódicas. En lugar de sumar ondas de frecuencias n, suma de forma continua ondas de todas las frecuencias omega. Funciona bien para funciones absolutamente integrables, como el {{gl:pulso|pulso}}, y en un {{gl:salto|salto}} da el promedio de los dos lados.")),
 sec("Un ejemplo","Un ejemplo",P("El pulso vale 1 entre menos 1 y 1. Su integral de Fourier es una suma continua de cosenos. Cambia la frecuencia máxima W y mira cómo mejora el parecido."),EQ("f(x)=\\dfrac{2}{\\pi}\\displaystyle\\int_{0}^{\\infty}\\dfrac{\\operatorname{sen}\\omega}{\\omega}\\cos(\\omega x)\\,d\\omega"),{"t":"grafica","animar":"dibujar","alt":"La reconstrucción del pulso con frecuencias hasta W"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La integral de Fourier se usa para funciones no periódicas. ¿Y la serie de Fourier?","opciones":["Para funciones periódicas","Solo para polinomios","Para cualquier función","Solo para funciones pares"],"correcta":"Para funciones periódicas","bien":"Muy bien. La serie es para funciones periódicas y la integral para las que no lo son.","mal":"La serie de Fourier representa funciones periódicas. Para las que no lo son se usa la integral."}),
 sec("Más frecuencias","Frecuencias",P("Mira la reconstrucción con W igual a 2, 5, 10 y 20."),{"t":"acercando","ds":[2,5,10,20],"alt":"La integral con cuatro frecuencias máximas"},P("Con pocas frecuencias hay una campana suave. Con muchas, casi se ve la caja, con pequeñas ondas en los bordes.")),
 sec("Los pasos","Pasos",P("Se calcula la transformada del pulso, y luego se reconstruye con la fórmula de inversión."),
   PASOS([("A(\\omega)=\\dfrac{1}{\\pi}\\displaystyle\\int_{-1}^{1}\\cos(\\omega s)\\,ds=\\dfrac{2\\operatorname{sen}\\omega}{\\pi\\omega}","El coeficiente de cada frecuencia, para una función par."),
          ("f(x)=\\displaystyle\\int_{0}^{\\infty}A(\\omega)\\cos(\\omega x)\\,d\\omega","La integral de Fourier de una función par."),
          ("x=0:\\ \\dfrac{2}{\\pi}\\displaystyle\\int_{0}^{\\infty}\\dfrac{\\operatorname{sen}\\omega}{\\omega}\\,d\\omega=\\dfrac{2}{\\pi}\\cdot\\dfrac{\\pi}{2}=1","Con la integral de Dirichlet se confirma que vale 1."),
          ("x=1:\\ f(1)=\\dfrac{1+0}{2}=\\dfrac{1}{2}","En el salto, la integral da el promedio.")]),
   OJO("En x igual a 1 la función vale 1 por la izquierda y 0 por la derecha. La integral no da ni 1 ni 0, sino el promedio, un medio.")),
 sec("La integral de Dirichlet","Dirichlet",P("Esta integral aparece una y otra vez, y vale pi medios."),
   PASOS([("\\displaystyle\\int_{0}^{\\infty}\\dfrac{\\operatorname{sen}\\omega}{\\omega}\\,d\\omega=\\dfrac{\\pi}{2}","Valor de Dirichlet."),
          ("u=2\\omega:\\ \\displaystyle\\int_{0}^{\\infty}\\dfrac{\\operatorname{sen}2\\omega}{\\omega}\\,d\\omega=\\displaystyle\\int_{0}^{\\infty}\\dfrac{\\operatorname{sen}u}{u}\\,du=\\dfrac{\\pi}{2}","Una constante positiva dentro del seno no cambia el valor."),
          ("\\operatorname{sen}(a\\omega)\\ \\text{con}\\ a>0\\ \\Rightarrow\\ \\dfrac{\\pi}{2}","Vale pi medios para todo a positivo.")]),
   OJO("Con a negativo el valor cambia de signo, porque seno es impar. Con a positivo siempre da pi medios.")),
 eng("Un pulso de radar","Un transmisor emite un pulso rectangular corto de 1 microsegundo. Para saber qué ancho de banda necesita, se mira su descomposición en frecuencias.","W\\approx\\dfrac{2\\pi}{\\tau}",
   [("Duración del pulso","1 µs"),("Ancho de banda aproximado","unos 6 millones de rad por segundo"),("Frecuencia equivalente","cerca de 1 MHz")],"Cuanto más corto es el pulso, más frecuencias necesita su integral de Fourier. Por eso un pulso muy corto requiere un ancho de banda mayor, y es un compromiso de diseño."),
 completar("La integral de Dirichlet de cero a infinito de seno de omega entre omega vale [[hueco]].","\\displaystyle\\int_{0}^{\\infty}\\dfrac{\\operatorname{sen}\\omega}{\\omega}\\,d\\omega=[[hueco]]",
   [("\\dfrac{\\pi}{2}","pi medios"),("\\pi","pi"),("1","uno")],0,
   ["","Con pi, el valor sería el doble de lo que es.","Con 1 sería una cifra sin sentido para esta integral."],"Es un resultado clásico de la integral de Dirichlet.","Vale pi medios."),
 error("Alguien calculó el valor de la integral de Fourier de un pulso en el borde x igual a 1 y se equivocó. Toca el paso que está mal.",
   [("f(1^-)=1,\\quad f(1^+)=0","Límites a cada lado.","los límites"),
    ("\\text{valor}=1","Este paso es el que falla.","da 1"),
    ("\\text{resultado}=1","Resultado.","queda 1")],1,
   "En un salto la integral converge al promedio de los límites a cada lado, y por eso da un medio y no 1.",
   "\\dfrac{1+0}{2}=\\dfrac{1}{2}","Promedia los dos límites."),
 ordenar("Estos son los pasos para representar un pulso con la integral de Fourier, pero están desordenados.",
   [("Se calcula A(ω) con un coseno entre menos 1 y 1","Se obtiene el coeficiente"),
    ("Se escribe la integral de A(ω) por coseno de ωx","Se arma la integral"),
    ("En x igual a 0 sale pi medios por 2 sobre pi","Se verifica con Dirichlet"),
    ("En x igual a 1 se toma el promedio","Se revisa el salto")],[2,0,3,1],
   "Primero el coeficiente, luego la integral, después el centro y por último el salto.","Se empieza calculando el coeficiente A de omega."),
]
S+=cierre("Mini simulacro de la integral de Fourier",[
 banco("es_c2_01","La integral de Fourier es para funciones no periódicas."),
 banco("es_c2_03","La integral de Dirichlet vale pi medios."),
 banco("es_c2_04","Con sen 2 omega la integral vale lo mismo.")])
prac=[
 {"titulo":"El pulso","grafica":{"draw":1},"bloques":[P("El pulso vale 1 entre menos 1 y 1, y 0 afuera."),EQ("f(x)=\\begin{cases}1&|x|<1\\\\0&|x|>1\\end{cases}")]},
 {"titulo":"Sube la frecuencia","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen W y el valor de la integral en el centro.")]},
 {"titulo":"Cerca de la caja","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":20,"bloques":[EQ("\\dfrac{2}{\\pi}\\cdot\\dfrac{\\pi}{2}=1"),P("Con frecuencias hasta 20 el valor en x igual a 0 es casi 1.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":20},"bloques":[{"t":"pregunta"},{"t":"nota","html":"En el salto se promedian los dos lados."}]}]
preg={"tex":"\\text{Con la integral de Fourier del pulso, el valor en }x=1\\text{ es}","opciones":["$\\dfrac{1}{2}$","$1$","$0$","$\\dfrac{\\pi}{2}$"],"correcta":0,
 "explicacion":"En x igual a 1 hay un salto de 1 a 0, y la integral converge al promedio, un medio.",
 "verificacion":{"formula":"(1+0)/2+0*x","a":0,"esperado":0.5},
 "pistas":["Hay un salto en x igual a 1.","La integral da el promedio de los dos lados.","Promedia 1 y 0."],
 "errores":["","El valor 1 es el del lado izquierdo, y no el de la integral.","El valor 0 es el del lado derecho, y no el de la integral.","Pi medios es el valor de la integral de Dirichlet, y no el del pulso."]}
res=["La integral de Fourier representa funciones no periódicas con una suma continua de ondas.","En un salto converge al promedio de los límites a cada lado.","La integral de Dirichlet vale pi medios."]
write(lesson("es-m2-l3","Lección 3 de 5","Integral de Fourier",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-integral.json")
