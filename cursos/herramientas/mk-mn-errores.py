import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
from fundlib import *
MOD="Módulo 1 Errores y ecuaciones no lineales"
TR="x*0+(-t-0.3)"
def tr(t): return f"{-t-0.3}"
def rd(t): return f"{t-16}"
def tot(t): return f"{math.log10(10**(-t-0.3)+10**(t-16)):.5f}"
KS=[round(0.5*i,1) for i in range(0,33)]
EL=[{"t":"trazo","puntos":[[str(k),tr(k)] for k in KS if k>=0],"c":0},
    {"t":"trazo","puntos":[[str(k),rd(k)] for k in KS if k>=0],"c":1},
    {"t":"trazo","puntos":[[str(k),tot(k)] for k in KS],"c":3},
    {"t":"segmento","a":["x","-17"],"b":["x","ln(exp(-(x+0.3)*ln(10))+exp((x-16)*ln(10)))/ln(10)"],"guia":True,"guion":True,"c":3},
    {"t":"punto","p":["x","ln(exp(-(x+0.3)*ln(10))+exp((x-16)*ln(10)))/ln(10)"],"c":3}]
graf={"tipo":"plano","x":[-1.0,17.0],"y":[-18.5,1.5],"a":1,"b":15,"inicio":4,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"tamaño del paso h, en potencias de diez, h igual a 10 a la menos k","formula":"x"},{"rotulo":"logaritmo del error total","formula":"ln(exp(-(x+0.3)*ln(10))+exp((x-16)*ln(10)))/ln(10)"}],
 "etiquetas":["Valor de k, donde h es diez elevado a menos k","Logaritmo en base 10 del error total de la derivada numérica"],"etiquetaSlider":"Valor de k, de 1 a 15",
 "alt":"Tres curvas del logaritmo del error de una derivada numérica en función de k, con h igual a diez elevado a menos k. El error de truncamiento baja al achicar h. El error de redondeo sube. La suma tiene forma de V, con su mínimo cerca de k igual a 8"}
glos={"absoluto":"El error absoluto es la diferencia entre el valor exacto y el aproximado.",
 "relativo":"El error relativo es el error absoluto dividido entre el valor exacto. Mide el error en proporción.",
 "cifras":"Las cifras significativas son los dígitos con que un número se conoce con confianza. Los ceros a la izquierda no cuentan.",
 "epsilon":"El épsilon de máquina mide la separación entre los números de la máquina cerca de uno, es decir, la distancia entre 1 y el siguiente número representable. Muchos textos lo definen como el menor número que hace que uno más épsilon sea mayor que uno.",
 "cancelacion":"La cancelación catastrófica es la pérdida de cifras significativas al restar dos números casi iguales."}
ver={"duracion":24.0,"capitulos":[
 [0,5,"Al calcular una derivada con una diferencia hay dos errores. El de truncamiento baja cuando se achica el paso h."],
 [5,10,"El de redondeo sube cuando se achica h, porque se restan números cada vez más parecidos."],
 [10,16,"La suma tiene forma de V. Con k igual a 4, el error es de truncamiento y vale cerca de 10 a la menos 4."],
 [16,21,"Con k igual a 8 se llega al mínimo, y el error total ronda 10 a la menos 8."],
 [21,24,"Con k mayor que 8, el redondeo domina. Achicar h más allá de ese punto empeora el resultado."]],
 "canales":{"draw":[[0.3,0],[4.5,1]],"d":[[5,4],[10,4],[12,8],[16,8],[17,12],[21,12],[22,15],[24,15]],"guide":[[5,0],[6,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("En el cálculo numérico siempre hay errores. El error {{gl:absoluto|absoluto}} es la diferencia con el valor exacto, y el {{gl:relativo|relativo}} la divide entre el valor. Los números se escriben con cierta cantidad de {{gl:cifras|cifras significativas}}, y la máquina guarda una cantidad finita, que se mide con el {{gl:epsilon|épsilon de máquina}}. Restar números casi iguales produce {{gl:cancelacion|cancelación}}.")),
 sec("Un ejemplo","Un ejemplo",P("Al derivar numéricamente aparecen dos errores. Mira el logaritmo del error total, en función de k, donde el paso es h igual a diez elevado a menos k."),EQ("E(h)\\approx\\dfrac{h}{2}\\,|f''|+\\dfrac{\\varepsilon}{h}"),{"t":"grafica","animar":"dibujar","alt":"Las curvas de los errores de truncamiento y de redondeo"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Si el valor exacto es 2 y se aproxima por 2.1, el error absoluto es 0.1. ¿Cuánto vale el error relativo, que es el absoluto entre el exacto?","opciones":[0.05,0.1,0.2,2],"correcta":0.05,"bien":"Muy bien. Es 0.1 entre 2, o sea 0.05, un 5 por ciento. Más abajo se ve la gráfica de errores.","mal":"Es 0.05, porque 0.1 entre 2 es 0.05. Más abajo se ve la gráfica de errores."}),
 sec("Variando el paso","El paso",P("Mira los errores con k igual a 3, 6, 8 y 12."),{"t":"acercando","ds":[3,6,8,12],"alt":"Los errores con cuatro valores de k"},P("El error total baja hasta k igual a 8 y vuelve a subir después. No siempre achicar el paso mejora el resultado.")),
 sec("Tipos de error","Tipos",P("Se miden de varias formas."),
   PASOS([("E_{abs}=|x-x^{*}|,\\quad E_{rel}=\\dfrac{|x-x^{*}|}{|x|}","Absoluto y relativo."),
          ("x=2,\\ x^{*}=2.1:\\quad E_{rel}=\\dfrac{0.1}{2}=0.05","El error relativo del ejemplo."),
          ("0.004530\\ \\text{tiene 4 cifras significativas}","Los ceros a la izquierda no cuentan, pero el cero final sí."),
          ("0.0034567\\ \\to\\ 0.00346\\ \\text{con 3 cifras}","Se redondea al número de cifras pedido.")]),
   OJO("El error relativo sirve para comparar. Un error de 1 metro es enorme al medir una mesa y despreciable al medir una carretera.")),
 sec("Punto flotante","Punto flotante",P("La máquina guarda los números con una cantidad finita de dígitos, y eso tiene consecuencias."),
   PASOS([("1+\\varepsilon_{maq}>1","El épsilon de máquina es la distancia entre 1 y el siguiente número que la máquina puede representar. En doble precisión es cerca de 2.2 por 10 a la menos 16."),
          ("\\sqrt{x^{2}+1}-x\\ \\text{para}\\ x\\ \\text{grande}","Se restan números casi iguales y se pierden cifras."),
          ("\\dfrac{1}{\\sqrt{x^{2}+1}+x}","La misma expresión reescrita no pierde cifras.")]),
   OJO("La cancelación sale de restar números casi iguales con precisión finita. A veces se evita reescribiendo la fórmula, como con la raíz de x al cuadrado más 1 menos x. En otros casos, como la derivada numérica, solo se controla eligiendo bien el paso.")),
 eng("Cuánto achicar el paso de una derivada","Un sensor entrega una posición cada cierto tiempo, y la velocidad se estima con la diferencia de dos posiciones consecutivas dividida entre el paso. Achicar el paso reduce el error del método, pero amplifica el ruido y el redondeo de las mediciones.","E_{total}=\\text{truncamiento}+\\text{redondeo}",
   [("Paso muy grande","domina el truncamiento"),("Paso muy pequeño","domina el redondeo"),("Paso óptimo","cerca de la raíz del épsilon")],"Con aritmética de doble precisión el paso óptimo de una diferencia progresiva está cerca de 10 a la menos 8. Con mediciones reales, que tienen mucho más ruido que el épsilon de máquina, el paso óptimo es mucho mayor. Por eso se filtra la señal antes de derivarla, o se usa una diferencia centrada con paso moderado."),
 completar("Se calcula el error relativo de aproximar 2 por 2.1.","E_{rel}=\\dfrac{|2-2.1|}{[[hueco]]}",
   [("2","el valor exacto"),("2.1","el valor aproximado"),("0.1","el error absoluto")],0,
   ["","El error relativo se divide entre el valor exacto, y no entre el aproximado.","Dividir entre el error absoluto daría siempre 1."],"El denominador es el valor exacto.","0.1 entre 2 es 0.05."),
 error("Alguien contó las cifras significativas del número 0.004530 y se equivocó en un paso. Toca el paso que está mal.",
   [("0.004530","El número.","el número es 0.004530"),
    ("\\text{Los ceros a la izquierda}\\ (0.00)\\ \\text{no cuentan}","Se descartan los ceros iniciales.","los ceros de la izquierda no cuentan"),
    ("\\text{Quedan 4,5,3 y el 0 final: son 3 cifras}","Este paso es el que falla.","son 3 cifras")],2,
   "El cero final también cuenta, porque indica que la medida llega hasta esa cifra. Quedan cuatro cifras, 4, 5, 3 y 0.",
   "4,\\ 5,\\ 3,\\ 0\\ \\Rightarrow\\ 4\\ \\text{cifras}","Cuenta también el cero del final."),
 ordenar("Estos son los pasos para calcular el error relativo de aproximar 2 por 2.1, pero están desordenados.",
   [("x=2,\\quad x^{*}=2.1","Se identifican el valor exacto y el aproximado"),
    ("E_{abs}=|2-2.1|=0.1","Se calcula el error absoluto"),
    ("E_{rel}=\\dfrac{0.1}{2}","Se divide entre el valor exacto"),
    ("E_{rel}=0.05","Se calcula")],[2,0,3,1],
   "Se calcula el error absoluto y se divide entre el valor exacto.","Se empieza identificando los dos valores."),
]
S+=cierre("Mini simulacro de errores y punto flotante",[
 banco("mn_c1_02","Los ceros iniciales no cuentan, pero el cero final sí. Son $4,5,3,0$."),
 banco("mn_c1_03","El épsilon de máquina es el menor número que hace que $1+\\varepsilon>1$."),
 banco("mn_c1_04","Restar números casi iguales produce cancelación y pérdida de cifras.")])
prac=[
 {"titulo":"Dos errores","grafica":{"draw":1},"bloques":[P("El error de truncamiento y el de redondeo, en escala logarítmica."),EQ("E(h)\\approx\\dfrac{h}{2}|f''|+\\dfrac{\\varepsilon}{h}")]},
 {"titulo":"Cambia k","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen k y el logaritmo del error total.")]},
 {"titulo":"El mínimo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":8,"bloques":[EQ("k=8\\ \\Rightarrow\\ \\log_{10}E\\approx-8"),P("Con k igual a 8 el error es el menor posible.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":8},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El error relativo se divide entre el valor exacto."}]}]
preg={"tex":"\\text{El redondeo a 3 cifras significativas de}\\ 0.0034567\\ \\text{es}","opciones":["$0.00346$","$0.0035$","$0.003$","$0.00345$"],"correcta":0,
 "explicacion":"Los ceros de la izquierda no cuentan. Las tres primeras cifras significativas son 3, 4 y 5, y la siguiente es 6, que sube la última a 6. El resultado es 0.00346.",
 "verificacion":{"formula":"0.00346+0*x","a":0,"esperado":0.00346},
 "pistas":["Los ceros de la izquierda no cuentan.","Las cifras son 3, 4, 5 y se mira el 6 que sigue.","El 6 hace que el 5 suba a 6."],
 "errores":["","Ese tiene dos cifras significativas, 3 y 5, y se piden tres.","Ese tiene una cifra significativa, y se piden tres.","Ese redondea hacia abajo, pero la cifra que sigue es 6 y obliga a subir."]}
res=["El error relativo es el absoluto entre el valor exacto, y sirve para comparar.","Los ceros a la izquierda no son cifras significativas, y restar números casi iguales pierde cifras.","Al derivar numéricamente hay un paso óptimo, porque achicarlo reduce el truncamiento pero aumenta el redondeo."]
write(lesson("mn-m1-l4","Lección 4 de 4","Errores y aritmética de punto flotante",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-errores.json")
