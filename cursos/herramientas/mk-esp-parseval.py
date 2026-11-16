import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
from fundlib import *
MOD="Módulo 1 Series de Fourier"
NT=8
TOT=2*math.pi**2/3
H=[4/n**2 for n in range(1,NT+1)]
CUM=[0]+[sum(H[:k]) for k in range(1,NT+1)]
EL=[]
for n in range(1,NT+1):
    EL.append({"t":"poligono","puntos":[[str(n-0.4),"0"],[str(n+0.4),"0"],[str(n+0.4),f"{H[n-1]:.6f}"],[str(n-0.4),f"{H[n-1]:.6f}"]],"c":0})
    ind=lagr([1 if N>=n else 0 for N in range(NT+1)])
    EL.append({"t":"poligono","puntos":[[str(n-0.4),"0"],[str(n+0.4),"0"],[str(n+0.4),f"{H[n-1]:.6f}*({ind})"],[str(n-0.4),f"{H[n-1]:.6f}*({ind})"]],"c":3})
LC="("+lagr([round(v,9) for v in CUM])+")"
graf={"tipo":"plano","x":[-0.8,9.8],"y":[-0.7,4.6],"a":0,"b":8,"inicio":1,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"suma de los primeros N cuadrados b de n al cuadrado","formula":LC},{"rotulo":"porcentaje de la energía total, 2 pi al cuadrado entre 3","formula":f"{LC}/{TOT:.6f}*100"}],
 "etiquetas":["Suma de 4 entre n al cuadrado hasta N","Cuánto del total ya reúnen los primeros N armónicos"],"etiquetaSlider":"Términos N, de 0 a 8",
 "alt":"Barras con los cuadrados de los coeficientes b de n de la serie de Fourier de x, que valen 4 entre n al cuadrado. Los primeros N están en verde. La suma de todas las barras, hasta infinito, es 2 pi al cuadrado entre 3, que es el promedio de x al cuadrado multiplicado por 2. Con 3 términos ya se reúne casi 83 por ciento"}
glos={"parseval":"La identidad de Parseval dice que la energía de una función, la integral de su cuadrado entre pi, es igual a la suma de los cuadrados de sus coeficientes de Fourier.",
 "energia":"La energía de una señal es la integral de su cuadrado. En un armónico es proporcional al cuadrado de su amplitud.",
 "leibniz":"La serie de Leibniz es uno menos un tercio más un quinto, y así. Suma pi entre 4, y sale de evaluar la onda cuadrada en pi medios.",
 "basel":"La suma de uno entre n al cuadrado vale pi al cuadrado entre 6. Sale de evaluar la serie de x al cuadrado en pi."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Cada barra es el cuadrado del coeficiente b de n de la serie de x, que vale 4 entre n al cuadrado."],
 [4,9,"Con un término se tiene 4, que es el 61 por ciento del total."],
 [9,15,"Con 3 términos suma 5.44, casi 83 por ciento."],
 [15,20,"La suma completa, hasta infinito, es 2 pi al cuadrado entre 3, o sea 6.58. Esa es la identidad de Parseval."],
 [20,24,"De ahí sale que la suma de uno entre n al cuadrado vale pi al cuadrado entre 6."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,3],[14,3],[16,8],[24,8]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,24]}}
S=[
 sec("La idea",None,P("La identidad de {{gl:parseval|Parseval}} relaciona la {{gl:energia|energía}} de una función con la de sus coeficientes. Es un teorema de Pitágoras para funciones. También permite sumar series famosas, como la de {{gl:basel|uno entre n al cuadrado}} y la de {{gl:leibniz|Leibniz}}, evaluando una serie de Fourier en un punto conveniente.")),
 sec("Un ejemplo","Un ejemplo",P("Para f de x igual a x, el promedio de x al cuadrado, multiplicado por 2, es 2 pi al cuadrado entre 3. Mira cómo los cuadrados de los coeficientes lo van reuniendo."),EQ("\\dfrac{1}{\\pi}\\displaystyle\\int_{-\\pi}^{\\pi}f(x)^{2}\\,dx=\\dfrac{a_{0}^{2}}{2}+\\sum_{n\\ge1}\\left(a_{n}^{2}+b_{n}^{2}\\right)"),{"t":"grafica","animar":"dibujar","alt":"Las barras de los cuadrados de los coeficientes"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El coeficiente b1 de la serie de x vale 2, así que su cuadrado vale 4. Si el total de la energía es 6.58, ¿qué fracción aproximada reúne el primer término?","opciones":["Unos 6 de cada 10","Unos 2 de cada 10","Casi todo"],"correcta":"Unos 6 de cada 10","bien":"Muy bien. 4 entre 6.58 es 0.61. El primer armónico reúne el 61 por ciento. Más abajo se ve.","mal":"4 entre 6.58 es 0.61, o sea unos 6 de cada 10. Más abajo se ve."}),
 sec("Sumando armónicos","Los armónicos",P("Mira la energía reunida con 1, 3, 5 y 8 armónicos."),{"t":"acercando","ds":[1,3,5,8],"alt":"La energía con cuatro cantidades de armónicos"},P("Con 8 armónicos ya se reúne el 93 por ciento. La suma completa da exactamente 2 pi al cuadrado entre 3.")),
 sec("La identidad","La identidad",P("Cada coeficiente aporta un cuadrado a la suma."),
   PASOS([("\\dfrac{1}{L}\\displaystyle\\int_{-L}^{L}f^{2}\\,dx=\\dfrac{a_{0}^{2}}{2}+\\sum(a_{n}^{2}+b_{n}^{2})","La identidad de Parseval en [menos L, L]."),
          ("f(x)=x:\\ \\dfrac{1}{\\pi}\\displaystyle\\int_{-\\pi}^{\\pi}x^{2}dx=\\dfrac{2\\pi^{2}}{3}","El lado izquierdo."),
          ("\\sum b_{n}^{2}=\\sum\\dfrac{4}{n^{2}}","El lado derecho."),
          ("\\sum\\dfrac{1}{n^{2}}=\\dfrac{\\pi^{2}}{6}","Al igualar y despejar.")])),
 sec("Sumas de series","Sumas",P("Evaluando una serie de Fourier en un punto se obtienen sumas exactas."),
   PASOS([("x^{2}=\\dfrac{\\pi^{2}}{3}+4\\displaystyle\\sum\\dfrac{(-1)^{n}}{n^{2}}\\cos nx","La serie de x al cuadrado."),
          ("x=\\pi:\\ \\pi^{2}=\\dfrac{\\pi^{2}}{3}+4\\sum\\dfrac{1}{n^{2}}\\ \\Rightarrow\\ \\sum\\dfrac{1}{n^{2}}=\\dfrac{\\pi^{2}}{6}","Evaluada en pi."),
          ("x=0:\\ 0=\\dfrac{\\pi^{2}}{3}+4\\sum\\dfrac{(-1)^{n}}{n^{2}}\\ \\Rightarrow\\ \\sum\\dfrac{(-1)^{n+1}}{n^{2}}=\\dfrac{\\pi^{2}}{12}=0.8225","Evaluada en 0."),
          ("\\text{onda cuadrada en}\\ \\tfrac{\\pi}{2}:\\ 1=\\dfrac{4}{\\pi}\\left(1-\\dfrac13+\\dfrac15-\\cdots\\right)\\ \\Rightarrow\\ \\dfrac{\\pi}{4}=0.7854","La serie de Leibniz.")]),
   OJO("Para que la evaluación sea válida, la serie debe converger a f en ese punto. En puntos de salto hay que usar el promedio de los límites laterales.")),
 eng("La energía de un armónico","La potencia de una señal periódica es la suma de las potencias de sus armónicos. En una señal en diente de sierra, el primer armónico reúne el 61 por ciento de la energía total, y los tres primeros reúnen el 83 por ciento. Con eso se decide qué filtro diseñar.","P_{total}=\\sum_{n}\\dfrac{b_{n}^{2}}{2}",
   [("Primer armónico","61 %"),("Tres primeros","83 %"),("Ocho primeros","93 %")],"Si un sistema solo deja pasar los tres primeros armónicos, perderá una sexta parte de la energía de la señal, que es un 17 por ciento. Esa estimación se hace sin integrar de nuevo, solo sumando cuadrados de coeficientes. Es el motivo por el que Parseval se usa mucho en análisis de señales."),
 completar("Se despeja la suma de uno entre n al cuadrado a partir de la identidad de Parseval para f de x igual a x.","4\\sum\\dfrac{1}{n^{2}}=\\dfrac{2\\pi^{2}}{3}\\ \\Rightarrow\\ \\sum\\dfrac{1}{n^{2}}=[[hueco]]",
   [("\\dfrac{\\pi^{2}}{6}","pi al cuadrado entre 6"),("\\dfrac{\\pi^{2}}{3}","pi al cuadrado entre 3"),("\\dfrac{\\pi^{2}}{12}","pi al cuadrado entre 12")],0,
   ["","Falta dividir entre 4. Dos pi al cuadrado entre 3, dividido entre 4, es pi al cuadrado entre 6.","Pi al cuadrado entre 12 es la suma alternada, y no la de todos los términos positivos."],"Se divide entre 4.","2 pi al cuadrado entre 3, entre 4, es pi al cuadrado entre 6."),
 error("Alguien obtuvo la serie de Leibniz de la onda cuadrada y se equivocó en un paso. Toca el paso que está mal.",
   [("f\\!\\left(\\tfrac{\\pi}{2}\\right)=1=\\dfrac{4}{\\pi}\\left(1-\\dfrac{1}{3}+\\dfrac{1}{5}-\\cdots\\right)","Se evalúa la serie en pi medios.","se evalúa en pi medios"),
    ("\\text{Entonces la suma vale}\\ \\dfrac{4}{\\pi}","Este paso es el que falla.","la suma vale 4 entre pi"),
    ("\\text{Resultado: }1.273","Depende del anterior.","da 1.273")],1,
   "Al despejar la suma, el 4 entre pi pasa dividiendo. Queda la suma igual a pi entre 4, o sea 0.7854.",
   "1-\\dfrac13+\\dfrac15-\\cdots=\\dfrac{\\pi}{4}","Despeja la suma con cuidado."),
 ordenar("Estos son los pasos para sumar uno entre n al cuadrado con la serie de x al cuadrado, pero están desordenados.",
   [("x^{2}=\\dfrac{\\pi^{2}}{3}+4\\sum\\dfrac{(-1)^{n}}{n^{2}}\\cos nx","Se parte de la serie de x al cuadrado"),
    ("x=\\pi:\\ \\pi^{2}=\\dfrac{\\pi^{2}}{3}+4\\sum\\dfrac{1}{n^{2}}","Se evalúa en pi, donde coseno de n pi es menos uno elevado a n"),
    ("4\\sum\\dfrac{1}{n^{2}}=\\dfrac{2\\pi^{2}}{3}","Se despeja la suma"),
    ("\\sum\\dfrac{1}{n^{2}}=\\dfrac{\\pi^{2}}{6}","Se divide entre 4")],[2,0,3,1],
   "Se evalúa la serie en pi, se despeja la suma y se divide entre 4.","Se empieza con la serie de x al cuadrado."),
]
S+=cierre("Mini simulacro de la identidad de Parseval y sumas de series",[
 banco("es_c1_22","Evaluando la serie de $x^2$ en $x=\\pi$ se obtiene $\\pi^2/6$."),
 banco("es_c1_24","La serie de Leibniz suma $\\pi/4=0.7854$."),
 banco("es_c1_25","La identidad de Parseval iguala la energía de f con la suma de los cuadrados de los coeficientes.")])
prac=[
 {"titulo":"Los cuadrados","grafica":{"draw":1},"bloques":[P("Los cuadrados de los coeficientes de la serie de x."),EQ("b_{n}^{2}=\\dfrac{4}{n^{2}}")]},
 {"titulo":"Suma armónicos","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 8. Abajo se leen la suma de cuadrados y el porcentaje de la energía total.")]},
 {"titulo":"Tres armónicos","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("4+1+\\tfrac49=5.44"),P("Con tres armónicos se reúne casi el 83 por ciento de la energía.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Se evalúa la serie de x al cuadrado en pi."}]}]
preg={"tex":"\\displaystyle\\sum_{n=1}^{\\infty}\\dfrac{1}{n^{2}}=","opciones":["$\\dfrac{\\pi^{2}}{6}$","$\\dfrac{\\pi^{2}}{12}$","$\\dfrac{\\pi}{4}$","$1$"],"correcta":0,
 "explicacion":"Se evalúa la serie de x al cuadrado en x igual a pi. Queda pi al cuadrado igual a pi al cuadrado entre 3 más 4 por la suma, y se despeja la suma, que vale pi al cuadrado entre 6, cerca de 1.645.",
 "verificacion":{"formula":"pi*pi/6+0*x","a":0,"esperado":1.6449},
 "pistas":["Usa la serie de x al cuadrado en x igual a pi.","Coseno de n pi por menos uno elevado a n da uno.","Despeja la suma."],
 "errores":["","Pi al cuadrado entre 12 es la suma con signos alternados.","Pi entre 4 es la serie de Leibniz, que sale de otra función.","Uno es solo el primer término, y la suma es mayor."]}
res=["La identidad de Parseval iguala la energía de f con la suma de los cuadrados de los coeficientes.","Evaluando la serie de x al cuadrado se obtiene la suma de uno entre n al cuadrado, que es pi al cuadrado entre 6.","La serie de Leibniz suma pi entre 4, y sale de la onda cuadrada evaluada en pi medios."]
write(lesson("es-m1-l4","Lección 4 de 5","Identidad de Parseval y sumas de series",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-parseval.json")
