import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 3 Laplace, sistemas y series"
N=100
TS=[math.pi*k/N for k in range(N+1)]
CURVA=[[f"{t:.4f}",f"sin(sqrt(x)*{t:.4f})"] for t in TS]
graf={"tipo":"plano","x":[-0.3,3.6],"y":[-1.4,1.4],"a":0.2,"b":10,"inicio":0.5,
 "elementos":[{"t":"recta","p":[str(round(math.pi,6)),"0"],"dir":["0","1"],"guion":True,"c":3},{"t":"trazo","puntos":CURVA,"c":2},{"t":"punto","p":[str(round(math.pi,6)),"sin(pi*sqrt(x))"],"c":1}],
 "lecturas":[{"rotulo":"lambda","formula":"x"},{"rotulo":"y en x=pi","formula":"sin(pi*sqrt(x))"}],
 "etiquetas":["Valor de lambda","Valor de y en x igual a pi"],"etiquetaSlider":"Valor de lambda",
 "alt":"La función seno de la raíz de lambda por x entre 0 y pi. El punto del extremo derecho solo cae sobre el eje cuando lambda vale 1, 4 o 9"}
glos={"frontera":"Un problema de valores en la frontera pide condiciones en dos puntos distintos, por ejemplo y de 0 igual a 0 e y de pi igual a 0, y no los dos en el mismo punto como un problema de valor inicial.",
 "propios":"Los valores propios de un problema de frontera son los valores de lambda para los que existe una solución que no es cero. Las soluciones correspondientes son las funciones propias.",
 "serie":"Una solución en serie de potencias escribe la solución como una suma infinita de potencias de x, con coeficientes que se hallan con una fórmula de recurrencia."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"El problema es y segunda más lambda y igual a 0, con y de 0 igual a 0 y y de pi igual a 0. Las condiciones están en los dos extremos. Esta es la solución seno de la raíz de lambda por x, que ya cumple la primera."],
 [4,8,"Con lambda igual a 0.5, la curva no termina en 0 cuando x llega a pi. Falta cumplir la segunda condición."],
 [8,14,"Al subir lambda, la curva oscila más rápido. Solo en ciertos valores termina justo en 0 en x igual a pi."],
 [14,18,"Eso pasa con lambda igual a 1, 4 y 9. Son los valores propios del problema, y las curvas son seno de n por x."],
 [18,22,"Con lambda igual a 4 la curva es seno de 2x, y el punto del extremo cae sobre el eje."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.5],[8,0.5],[11,2.5],[14,2.5],[15,1],[16,4],[17,9],[18,4],[22,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Esta lección junta dos ideas. Primero, cuando los coeficientes no son constantes, a veces la solución se escribe como una {{gl:serie|serie de potencias}}. Segundo, hay problemas con condiciones en los dos extremos de un intervalo, los {{gl:frontera|problemas de frontera}}. En ellos solo algunos valores de un parámetro, los {{gl:propios|valores propios}}, dan una solución que no es cero.")),
 sec("Un ejemplo","Un ejemplo",P("Mira este problema con condiciones en los dos extremos. La curva es la solución que ya cumple la condición de la izquierda."),EQ("y''+\\lambda y=0,\\qquad y(0)=0,\\ y(\\pi)=0"),{"t":"grafica","animar":"dibujar","alt":"La solución seno de la raíz de lambda por x"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con lambda igual a 9 la solución es seno de 3x. ¿Cuánto vale en x igual a pi, o sea seno de 3 pi?","opciones":[-1,0,1,3],"correcta":0,"bien":"Muy bien. Vale 0, porque 3 pi es un múltiplo de pi. Más abajo se ve qué pasa con otros valores.","mal":"Vale 0, porque 3 pi es un múltiplo de pi y ahí el seno se anula. Más abajo se ve qué pasa con otros valores."}),
 sec("Buscando lambda","Buscando lambda",P("Mueve lambda y mira cuándo el extremo derecho cae sobre el eje."),{"t":"acercando","ds":[0.5,1,4,9],"alt":"La solución para varios valores de lambda"},P("Solo con lambda igual a 1, 4 y 9, y los cuadrados perfectos siguientes, la curva cumple y de pi igual a 0.")),
 sec("Los valores propios","Valores propios",P("Se aplican las dos condiciones a la solución general."),
   PASOS([("y=c_{1}\\cos\\left(\\sqrt{\\lambda}\\,x\\right)+c_{2}\\operatorname{sen}\\left(\\sqrt{\\lambda}\\,x\\right)","La solución general con lambda positivo."),
          ("y(0)=0\\ \\Rightarrow\\ c_{1}=0","La condición de la izquierda."),
          ("y(\\pi)=0\\ \\Rightarrow\\ c_{2}\\operatorname{sen}\\left(\\pi\\sqrt{\\lambda}\\right)=0","Para que c2 no sea 0, el seno debe anularse."),
          ("\\sqrt{\\lambda}=n\\ \\Rightarrow\\ \\lambda_{n}=n^{2},\\quad y_{n}=\\operatorname{sen}nx","Los valores propios son los cuadrados de los enteros.")]),
   OJO("Con c2 igual a 0 siempre se cumplen las dos condiciones, pero esa es la solución cero. Un valor propio es el que permite una solución distinta de cero.")),
 sec("Soluciones en serie","En serie",P("Cuando los coeficientes no son constantes, se prueba una serie de potencias y se halla una recurrencia para los coeficientes."),
   PASOS([("y=\\sum_{n=0}^{\\infty}c_{n}x^{n},\\quad y''=\\sum_{n=0}^{\\infty}(n+2)(n+1)\\,c_{n+2}x^{n}","Se escribe la serie y su segunda derivada, con el índice corrido."),
          ("(n+2)(n+1)\\,c_{n+2}+c_{n}=0","Se reemplaza en y segunda más y igual a 0 y se agrupa cada potencia de x."),
          ("c_{n+2}=-\\dfrac{c_{n}}{(n+2)(n+1)}","La recurrencia."),
          ("c_{0}=1,\\ c_{1}=0\\ \\Rightarrow\\ y=1-\\dfrac{x^{2}}{2}+\\dfrac{x^{4}}{24}-\\cdots=\\cos x","Con c0 igual a 1 y c1 igual a 0, la serie es la del coseno.")]),
   OJO("Este método funciona cerca de un punto ordinario, donde los coeficientes de la ecuación son analíticos. En otros puntos se necesitan métodos más avanzados.")),
 eng("El pandeo de una columna","Una columna esbelta cargada de arriba falla de repente cuando la carga llega a un valor crítico, y se dobla de lado. Ese valor es el menor valor propio de un problema de frontera, con la columna apoyada en los dos extremos.","EI\\,y''+P\\,y=0,\\quad y(0)=y(L)=0",
   [("Largo","3 m"),("Rigidez EI","1.6 millones de N·m²"),("Carga crítica","unos 1750 kN")],"La carga crítica es pi al cuadrado por EI sobre L al cuadrado. Con estos datos queda unos 1750 kilonewton. Las cargas de los valores propios siguientes, 4, 9 veces la primera, corresponden a formas más onduladas que en la práctica no se alcanzan, porque la columna ya falló. Es la fórmula de Euler, que solo vale para columnas esbeltas, y supone un material perfecto y una carga bien centrada."),
 completar("Para que c2 no sea 0, el seno debe anularse en x igual a pi.","\\operatorname{sen}\\left(\\pi\\sqrt{\\lambda}\\right)=0\\ \\Rightarrow\\ \\sqrt{\\lambda}=[[hueco]]",
   [("n","un entero positivo n"),("\\pi","pi"),("\\tfrac{1}{2}","un medio")],0,
   ["","El seno se anula en múltiplos de pi, pero aquí ya aparece pi multiplicando. Lo que debe ser entero es la raíz.","Con un medio, seno de pi sobre 2 vale 1 y no 0."],"El seno vale 0 cuando su argumento es un múltiplo de pi.","Si pi por la raíz es n por pi, la raíz es un entero positivo n."),
 error("Alguien resolvió un problema de frontera y se equivocó en un paso. Toca el paso que está mal.",
   [("y=c_{1}\\cos\\left(\\sqrt{\\lambda}\\,x\\right)+c_{2}\\operatorname{sen}\\left(\\sqrt{\\lambda}\\,x\\right)","La solución general.","la solución general con coseno y seno"),
    ("y(0)=0\\ \\Rightarrow\\ c_{1}=0","Se aplica la condición de la izquierda.","la condición en 0 da c1 igual a 0"),
    ("y(\\pi)=0\\ \\Rightarrow\\ c_{2}=0","Este paso es el que falla.","la condición en pi da c2 igual a 0")],2,
   "Con c2 igual a 0 solo queda la solución cero. Para una solución distinta de cero hay que exigir que el seno se anule, y eso da los valores propios.",
   "\\operatorname{sen}\\left(\\pi\\sqrt{\\lambda}\\right)=0","Piensa si se busca la solución cero o una distinta."),
 ordenar("Estos son los pasos para hallar la recurrencia de la serie de y segunda más y igual a 0, pero están desordenados.",
   [("y=\\sum c_{n}x^{n}","La serie propuesta"),
    ("y''=\\sum (n+2)(n+1)\\,c_{n+2}x^{n}","La segunda derivada"),
    ("(n+2)(n+1)\\,c_{n+2}+c_{n}=0","Se reemplaza y se agrupa"),
    ("c_{n+2}=-\\dfrac{c_{n}}{(n+2)(n+1)}","La recurrencia")],[2,0,3,1],
   "Se propone la serie, se deriva dos veces, se reemplaza y se despeja el coeficiente de más alto índice.","Se empieza proponiendo la serie."),
]
_q=mcq("Para $y''+\\lambda y=0$ con $y(0)=y(\\pi)=0$, el menor valor propio positivo es:",["$1$","$\\pi$","$\\pi^{2}$","$2$"],0,"Hace falta $\\sin(\\pi\\sqrt{\\lambda})=0$, y el menor entero positivo es $1$, así que $\\lambda=1$.")
_q["fuente"]="Pregunta original de esta lección"
S+=cierre("Mini simulacro de series y frontera",[
 banco("ed_c3_14","Un punto es ordinario cuando $p$ y $q$ son analíticas en él, y entonces existe una solución en serie de potencias."),_q])
prac=[
 {"titulo":"El problema","grafica":{"draw":1,"guide":1},"bloques":[P("Una ecuación con condiciones en los dos extremos, 0 y pi."),EQ("y''+\\lambda y=0")]},
 {"titulo":"Cambia lambda","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee el valor de y en x igual a pi, que casi siempre es distinto de 0.")]},
 {"titulo":"Un valor propio","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":4,"bloques":[EQ("\\lambda=4\\ \\Rightarrow\\ y=\\operatorname{sen}2x"),P("Con lambda igual a 4 el extremo cae sobre el eje y y de pi vale 0.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":4},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Pide que el seno se anule en x igual a pi."}]}]
preg={"tex":"y''+\\lambda y=0,\\ y(0)=y(\\pi)=0\\ \\text{tiene solución no nula cuando}\\ \\lambda=","opciones":["$4$","$2$","$\\pi$","$3$"],"correcta":0,
 "explicacion":"La solución que cumple y de 0 igual a 0 es seno de la raíz de lambda por x. En x igual a pi hace falta que seno de pi por la raíz de lambda sea 0, o sea que la raíz sea un entero. Con lambda igual a 4, la raíz es 2.",
 "verificacion":{"formula":"sin(pi*sqrt(x))","a":4,"esperado":0},
 "pistas":["La solución es seno de la raíz de lambda por x.","En x igual a pi, seno de pi por la raíz de lambda debe valer 0.","Eso pasa si la raíz de lambda es un entero."],
 "errores":["","Con lambda igual a 2 la raíz es 1.41, que no es un entero, y seno de 1.41 pi no vale 0.","Con lambda igual a pi la raíz no es un entero, así que el seno no se anula.","Con lambda igual a 3 la raíz es 1.73, que no es un entero. Los valores propios son cuadrados perfectos."]}
res=["Un problema de frontera tiene condiciones en dos puntos. Solo ciertos valores del parámetro, los valores propios, dan soluciones distintas de cero.","Para y segunda más lambda y igual a 0 con y de 0 y y de pi iguales a 0, los valores propios son los cuadrados de los enteros.","Una serie de potencias se resuelve con una recurrencia para los coeficientes cerca de un punto ordinario."]
write(lesson("edo-m3-l5","Lección 5 de 5","Series y problemas de frontera",30,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=5,curso="Ecuaciones Diferenciales"),"edo-series.json")
