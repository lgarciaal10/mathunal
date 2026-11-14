import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
from fundlib import *
MOD="Módulo 1 Series de Fourier"
NP=121
TS=[round(-math.pi+k*2*math.pi/(NP-1),5) for k in range(NP)]
EL=[{"t":"trazo","puntos":[[str(t),f"sin({t})*sin(x*{t})"] for t in TS],"c":0},
    {"t":"segmento","a":[str(-math.pi),"0"],"b":[str(math.pi),"0"],"c":3}]
INT=[0,math.pi,0,0,0,0,0]
graf={"tipo":"plano","x":[-4.4,4.4],"y":[-1.4,1.4],"a":1,"b":6,"inicio":1,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"integral de seno de x por seno de n x entre menos pi y pi","formula":"("+lagr([round(v,9) for v in INT])+")"},{"rotulo":"período de seno de n x","formula":"2*pi/x"}],
 "etiquetas":["Vale pi con n igual a 1, y cero con los demás n","El período se acorta al subir n"],"etiquetaSlider":"Frecuencia n, de 1 a 6",
 "alt":"La curva del producto de seno de x por seno de n x entre menos pi y pi. Con n igual a 1 el producto es seno al cuadrado y siempre es positivo, y su integral vale pi. Con n mayor que 1 el producto tiene partes positivas y negativas iguales que se cancelan, y la integral vale cero"}
glos={"periodica":"Una función es periódica de período T si f de x más T es igual a f de x para todo x. El período de seno de omega x es 2 pi entre omega.",
 "ortogonal":"Dos funciones son ortogonales en un intervalo si la integral de su producto es cero. Es la versión para funciones del producto punto cero.",
 "producto":"Las fórmulas de producto a suma convierten un producto de senos y cosenos en una suma, y se integran fácilmente.",
 "norma":"La norma al cuadrado de seno de n x en el intervalo de menos pi a pi vale pi, y la del coseno de n x también, si n es distinto de cero."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La curva es el producto de seno de x por seno de n x. La integral de ese producto dice si las dos ondas son ortogonales."],
 [4,9,"Con n igual a 1, el producto es seno al cuadrado, siempre positivo, y la integral vale pi."],
 [9,15,"Con n igual a 2 o a 3, el producto tiene partes positivas y negativas que se cancelan, y la integral vale cero."],
 [15,20,"El período de seno de n x es 2 pi entre n, así que a mayor n más oscila."],
 [20,24,"Por eso los senos y cosenos de frecuencias enteras forman un conjunto ortogonal en el intervalo de menos pi a pi."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,2],[12,3],[15,4],[24,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,24]}}
S=[
 sec("La idea",None,P("Una función {{gl:periodica|periódica}} se repite cada cierto período. La suma de ondas de distinto período es periódica si sus períodos tienen un múltiplo común. Dos funciones son {{gl:ortogonal|ortogonales}} si la integral de su producto es cero. Con las fórmulas de {{gl:producto|producto a suma}} se prueba que los senos y cosenos de frecuencias enteras son ortogonales entre sí, y de ahí salen los coeficientes de Fourier.")),
 sec("Un ejemplo","Un ejemplo",P("Mira el producto de seno de x por seno de n x. Cuando la parte positiva y la negativa se compensan, la integral vale cero."),EQ("\\displaystyle\\int_{-\\pi}^{\\pi}\\operatorname{sen}(mx)\\operatorname{sen}(nx)\\,dx=\\begin{cases}\\pi&m=n\\\\0&m\\neq n\\end{cases}"),{"t":"grafica","animar":"dibujar","alt":"El producto de dos senos"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con n igual a 1, el producto es seno de x al cuadrado, que nunca es negativo. ¿La integral de menos pi a pi es positiva, cero o negativa?","opciones":["Positiva","Cero","Negativa"],"correcta":"Positiva","bien":"Muy bien. Es positiva, y vale pi. Más abajo se ve que con n distinto de 1 se anula.","mal":"Es positiva, porque seno al cuadrado nunca es negativo y no se cancela. Vale pi. Más abajo se ve que con n distinto de 1 se anula."}),
 sec("Cambiando la frecuencia","La frecuencia",P("Mira el producto con n igual a 1, 2, 3 y 5."),{"t":"acercando","ds":[1,2,3,5],"alt":"El producto para cuatro frecuencias"},P("Solo con n igual a 1 el producto es siempre positivo. Con los demás, las partes positivas y negativas son iguales.")),
 sec("Períodos","Períodos",P("El período de una onda y el de una suma."),
   PASOS([("T=\\dfrac{2\\pi}{\\omega}","El período de seno de omega x."),
          ("\\cos\\!\\left(\\tfrac{2}{3}x+1\\right):\\ T=\\dfrac{2\\pi}{2/3}=3\\pi","Un ejemplo, con la frecuencia 2 tercios."),
          ("\\operatorname{sen}\\!\\left(\\tfrac{\\pi}{3}t\\right)+\\operatorname{sen}\\!\\left(\\tfrac{2\\pi}{5}t\\right):\\ T_{1}=6,\\ T_{2}=5","Los períodos de cada término."),
          ("T=\\operatorname{mcm}(6,5)=30","El período de la suma es el mínimo común múltiplo.")]),
   OJO("Para una suma de ondas, el período no es la suma ni el promedio de los períodos, sino el menor tiempo en que todas se repiten juntas.")),
 sec("Ortogonalidad","Ortogonalidad",P("Con las identidades de producto a suma se calculan estas integrales."),
   PASOS([("\\displaystyle\\int_{-\\pi}^{\\pi}\\operatorname{sen}(mx)\\cos(nx)\\,dx=0","Seno y coseno siempre son ortogonales."),
          ("\\operatorname{sen}3x\\cos5x=\\tfrac12\\left[\\operatorname{sen}8x-\\operatorname{sen}2x\\right]\\ \\Rightarrow\\ \\displaystyle\\int=0","Un ejemplo."),
          ("\\displaystyle\\int_{-\\pi}^{\\pi}\\cos^{2}(2x)\\,dx=\\pi=3.1416","La norma al cuadrado de coseno de 2x."),
          ("\\displaystyle\\int_{-L}^{L}f\\,dx=\\int_{a}^{a+2L}f\\,dx","Para una función de período 2L, el punto de partida no importa.")]),
   OJO("La ortogonalidad no depende del intervalo que se escoja, sino de que tenga la longitud de un período. En menos pi a pi funciona para frecuencias enteras.")),
 eng("Separar señales por frecuencia","Un analizador de vibraciones recibe una señal que mezcla ondas de distintas frecuencias. Para saber cuánto aporta la frecuencia n, multiplica la señal por seno de n x y la integra en un período. Las demás frecuencias se anulan por la ortogonalidad.","\\displaystyle\\int_{-\\pi}^{\\pi}\\operatorname{sen}(x)\\operatorname{sen}(3x)\\,dx=0",
   [("Señal 1","seno de x"),("Señal 2","seno de 3x"),("Integral del producto","0")],"Ese principio es la base de los analizadores de espectro. Cada coeficiente mide la cantidad de una frecuencia, sin que las otras interfieran. Si el intervalo de integración no coincide con un múltiplo del período, las frecuencias se filtran unas en otras, y se habla de fuga espectral."),
 completar("Se calcula el período de coseno de dos tercios de x más 1. Falta el resultado.","T=\\dfrac{2\\pi}{2/3}=[[hueco]]",
   [("3\\pi","tres pi"),("2\\pi","dos pi"),("\\pi","pi")],0,
   ["","2 pi es el período de coseno de x, y aquí la frecuencia es menor, así que el período es mayor.","Pi sería el período de coseno de 2x, que oscila más rápido."],"El período es 2 pi entre la frecuencia.","Dividir entre 2 tercios es multiplicar por 3 medios, y queda 3 pi."),
 error("Alguien halló el período de una suma de ondas y se equivocó en un paso. Toca el paso que está mal.",
   [("T_{1}=6,\\quad T_{2}=5","Los períodos de cada onda.","los períodos son 6 y 5"),
    ("T=6+5=11","Este paso es el que falla.","se suman los períodos"),
    ("\\text{El período es 11}","Resultado.","el período es 11")],1,
   "El período de la suma es el menor número en que las dos ondas se repiten juntas, o sea, el mínimo común múltiplo de 6 y 5, que es 30.",
   "T=\\operatorname{mcm}(6,5)=30","Busca el menor número que contiene a 6 y a 5."),
 ordenar("Estos son los pasos para calcular la integral de seno de 3x por coseno de 5x entre menos pi y pi, pero están desordenados.",
   [("\\operatorname{sen}3x\\cos5x=\\tfrac12\\left[\\operatorname{sen}8x+\\operatorname{sen}(-2x)\\right]","Se usa producto a suma"),
    ("=\\tfrac12\\left[\\operatorname{sen}8x-\\operatorname{sen}2x\\right]","Se simplifica"),
    ("\\displaystyle\\int_{-\\pi}^{\\pi}\\operatorname{sen}(kx)\\,dx=0","Cada seno de frecuencia entera se integra a cero"),
    ("\\text{la integral vale}\\ 0","Se concluye")],[2,0,3,1],
   "Se convierte el producto en suma, se simplifica y se integra cada seno, que da cero.","Se empieza con la identidad de producto a suma."),
]
S+=cierre("Mini simulacro de funciones periódicas y ortogonalidad",[
 banco("es_c1_02","Los senos y cosenos de frecuencias enteras son ortogonales con el producto interno de la integral."),
 banco("es_c1_04","$\\int_{-\\pi}^{\\pi}\\cos^2(2x)\\,dx=\\pi=3.1416$."),
 banco("es_c1_05","Los períodos son 6 y 5, y el mínimo común múltiplo es 30.")])
prac=[
 {"titulo":"El producto","grafica":{"draw":1},"bloques":[P("El producto de seno de x por seno de n x."),EQ("\\operatorname{sen}(x)\\operatorname{sen}(nx)")]},
 {"titulo":"Cambia n","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 1 a 6. Abajo se leen la integral del producto y el período de seno de n x.")]},
 {"titulo":"n igual a 3","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("\\displaystyle\\int\\operatorname{sen}x\\operatorname{sen}3x\\,dx=0"),P("Con n igual a 3 las partes positivas y negativas se compensan.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Busca el menor tiempo en que las dos ondas se repiten juntas."}]}]
preg={"tex":"\\text{El período de}\\ f(t)=\\operatorname{sen}(2t)+\\cos(3t)\\ \\text{es}","opciones":["$2\\pi$","$\\pi$","$6\\pi$","$\\dfrac{2\\pi}{3}$"],"correcta":0,
 "explicacion":"Seno de 2t tiene período pi y coseno de 3t tiene período 2 pi entre 3. El menor tiempo en que las dos se repiten es 2 pi, porque 2 pi es dos veces pi y tres veces 2 pi entre 3.",
 "verificacion":{"formula":"2*pi+0*x","a":0,"esperado":6.2832},
 "pistas":["Halla el período de cada término.","Son pi y 2 pi entre 3.","Busca un valor que sea múltiplo de los dos."],
 "errores":["","Pi es el período del seno, pero el coseno de 3t no se repite en pi.","6 pi es un período común, pero no el menor.","Dos pi entre 3 es el período del coseno, y el seno no se repite en ese tiempo."]}
res=["El período de seno de omega x es 2 pi entre omega, y el de una suma es el mínimo común múltiplo.","Los senos y cosenos de frecuencias enteras son ortogonales en un intervalo de longitud 2 pi.","La integral de una función periódica sobre un período no depende del punto de partida."]
write(lesson("es-m1-l1","Lección 1 de 5","Funciones periódicas y ortogonalidad",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-ortogonalidad.json")
