import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
from fundlib import *
MOD="Módulo 1 Series de Fourier"
NT=10
def ind(j): return f"(1+(x-{j}+0.63)/abs(x-{j}+0.63))/2"
def Sn(t): return "+".join(f"({ind(j)})*({4/math.pi/(2*j-1):.6f})*{math.sin((2*j-1)*t):.6f}" for j in range(1,NT+1))
def S(N,t): return sum(4/math.pi*math.sin((2*j-1)*t)/(2*j-1) for j in range(1,N+1))
NP=181
TS=[round(-math.pi+k*2*math.pi/(NP-1),5) for k in range(NP)]
EL=[{"t":"trazo","puntos":[[str(t),str(1 if t>0 else -1)] for t in [-math.pi,-0.0001]],"c":3},
    {"t":"trazo","puntos":[[str(t),str(1)] for t in [0.0001,math.pi]],"c":3},
    {"t":"trazo","puntos":[[str(t),Sn(t)] for t in TS],"c":0}]
peaks=[max(S(N,t) for t in [k*math.pi/4000 for k in range(1,4000)]) for N in range(0,NT+1)]
pk=[round(p,6) for p in peaks]; pk[0]=0
graf={"tipo":"plano","x":[-8.2,8.2],"y":[-1.8,1.8],"a":1,"b":10,"inicio":3,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"valor máximo de la suma parcial","formula":"("+lagr(pk)+")"},{"rotulo":"exceso sobre 1, como porcentaje del salto total de 2","formula":"(("+lagr(pk)+")-1)*50"}],
 "etiquetas":["Valor más alto de la suma parcial, cerca del salto","Tiende a cerca de 9 por ciento del salto, y no a cero"],"etiquetaSlider":"Términos impares N, de 1 a 10",
 "alt":"La onda cuadrada, que vale menos 1 a la izquierda de 0 y 1 a la derecha, en verde, y la suma parcial de su serie de Fourier con N términos, en azul. Al aumentar N la suma se parece más a la onda, pero junto al salto queda un pico que se estrecha y sigue sobrepasando 1 en cerca de 9 por ciento del salto"}
glos={"dirichlet":"Las condiciones de Dirichlet dicen que si f es periódica y continua a trozos con derivada continua a trozos, su serie de Fourier converge en cada punto al promedio de los límites laterales.",
 "salto":"Una discontinuidad de salto es un punto donde los límites laterales existen pero son distintos.",
 "gibbs":"El fenómeno de Gibbs es el pico que aparece junto a un salto en las sumas parciales. Mide cerca de 9 por ciento del salto y no desaparece al agregar términos, aunque se angosta.",
 "uniforme":"Si f es continua y suave a trozos, su serie converge a f de forma uniforme, sin picos de Gibbs."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La onda cuadrada vale 1 de 0 a pi, y menos 1 de menos pi a 0. Tiene un salto en x igual a 0."],
 [4,9,"Con un término, la serie es una sola onda seno."],
 [9,15,"Con más términos se parece a la onda cuadrada, pero aparece un pico justo antes del salto."],
 [15,20,"Ese pico es el fenómeno de Gibbs. Mide cerca de 9 por ciento del salto y no desaparece al agregar términos."],
 [20,24,"En el salto mismo, la serie converge al promedio de los límites laterales, que aquí es 0."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,3],[13,6],[16,10],[24,10]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,24]}}
S=[
 sec("La idea",None,P("Una serie de Fourier no siempre converge a la función. Según el teorema de {{gl:dirichlet|Dirichlet}}, en un punto de continuidad converge a f, y en una discontinuidad de {{gl:salto|salto}} converge al promedio de los dos límites laterales. Cerca del salto, las sumas parciales muestran el fenómeno de {{gl:gibbs|Gibbs}}. Si f es continua y suave a trozos, la convergencia es {{gl:uniforme|uniforme}}.")),
 sec("Un ejemplo","Un ejemplo",P("La onda cuadrada tiene un salto en 0. Mira sus sumas parciales y el pico junto al salto."),EQ("f(x)=\\dfrac{4}{\\pi}\\displaystyle\\sum_{k\\ \\text{impar}}\\dfrac{\\operatorname{sen}kx}{k}"),{"t":"grafica","animar":"dibujar","alt":"Las sumas parciales de la onda cuadrada"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La función vale menos 1 a la izquierda de 0 y 1 a la derecha. ¿A qué valor converge la serie justo en x igual a 0, que es el promedio de los dos límites?","opciones":[-1,0,1,2],"correcta":0,"bien":"Muy bien. El promedio de menos 1 y 1 es 0. Más abajo se ve que todas las sumas parciales valen 0 en ese punto.","mal":"Converge a 0, que es el promedio de menos 1 y 1. Más abajo se ve que todas las sumas parciales valen 0 en ese punto."}),
 sec("Agregando términos","Los términos",P("Mira la suma parcial con 1, 3, 6 y 10 términos."),{"t":"acercando","ds":[1,3,6,10],"alt":"La suma parcial con cuatro cantidades de términos"},P("El pico junto al salto se angosta, pero su altura se queda cerca de 1.18, es decir, un 9 por ciento del salto por encima de 1.")),
 sec("Convergencia","Convergencia",P("El teorema de Dirichlet describe a qué converge la serie en cada punto."),
   PASOS([("f\\ \\text{continua en}\\ x_{0}\\ \\Rightarrow\\ S(x_{0})=f(x_{0})","En un punto de continuidad converge a f."),
          ("S(x_{0})=\\dfrac{f(x_{0}^{+})+f(x_{0}^{-})}{2}","En un salto converge al promedio de los límites laterales."),
          ("f=1\\ \\text{en}\\ (0,\\pi),\\ f=-1\\ \\text{en}\\ (-\\pi,0):\\ S(0)=0","La onda cuadrada, en el salto."),
          ("h=2\\ \\text{en}\\ (0,L),\\ h=-1\\ \\text{en}\\ (-L,0):\\ S(0)=\\dfrac{2-1}{2}=0.5","Un salto de menos 1 a 2.")]),
   OJO("En el punto del salto la serie no vale lo que f valga ahí. La serie converge al promedio de los límites, y puede coincidir o no con el valor que se le asignó a f en ese punto.")),
 sec("El fenómeno de Gibbs","Gibbs",P("El pico de Gibbs es una propiedad de la convergencia cerca de un salto."),
   PASOS([("\\text{pico}\\approx1+0.0895\\cdot2\\approx1.179","El exceso es cerca de 9 por ciento del salto, que aquí es 2."),
          ("N\\to\\infty\\ \\Rightarrow\\ \\text{el pico se angosta pero no baja}","Al agregar términos no desaparece."),
          ("f\\ \\text{continua y}\\ C^{1}\\ \\text{a trozos}\\ \\Rightarrow\\ \\text{convergencia uniforme}","Sin saltos no hay picos de Gibbs.")]),
   OJO("Gibbs no es un error de cálculo, sino una propiedad de aproximar un salto con ondas suaves. Se atenúa multiplicando los coeficientes por un factor que decrece, como en los factores de Fejér.")),
 eng("El rebote de una señal cuadrada","Una señal cuadrada que pasa por un filtro pasa bajos pierde sus armónicos altos, y queda como una suma parcial de su serie. En la salida aparece un rebote junto a cada flanco, el fenómeno de Gibbs, que se llama también ringing.","\\text{pico}\\approx1.18\\ \\text{con salto de}\\ -1\\ \\text{a}\\ 1",
   [("Salto","de menos 1 a 1"),("Pico de la suma parcial","cerca de 1.18"),("Al agregar armónicos","se angosta, pero no baja")],"En un amplificador o en un enlace de datos, ese rebote puede superar el nivel permitido en 9 por ciento del salto. Por eso se diseñan los filtros con una transición suave, y no con un corte abrupto, y se deja un margen en los niveles de la señal."),
 completar("Se calcula el valor de la serie de Fourier de la onda cuadrada en el salto. Falta el resultado.","\\dfrac{1+(-1)}{2}=[[hueco]]",
   [("0","cero"),("1","uno"),("-1","menos uno")],0,
   ["","Uno es el límite por la derecha, y no el promedio de los dos.","Menos uno es el límite por la izquierda, y no el promedio."],"Es el promedio de los dos límites laterales.","1 más menos 1 es 0, y el promedio es 0."),
 error("Alguien dijo a qué valor converge la serie de la onda cuadrada en x igual a 0 y se equivocó en un paso. Toca el paso que está mal.",
   [("f(0^{+})=1,\\quad f(0^{-})=-1","Los límites laterales.","1 a la derecha y menos 1 a la izquierda"),
    ("\\text{La serie converge a}\\ f(0^{+})=1","Este paso es el que falla.","converge al límite de la derecha"),
    ("S(0)=1","Resultado.","el valor es 1")],1,
   "En un salto, la serie converge al promedio de los dos límites laterales, y no a uno solo de ellos. El promedio de 1 y menos 1 es 0, y todas las sumas parciales valen 0 en x igual a 0.",
   "S(0)=\\dfrac{1+(-1)}{2}=0","Recuerda qué dice el teorema de Dirichlet en un salto."),
 ordenar("Estos son los pasos para hallar el valor de la serie en el salto de una función con límites 2 y menos 1, pero están desordenados.",
   [("\\text{salto de}\\ -1\\ \\text{a}\\ 2\\ \\text{en}\\ x=0","Se identifica el salto"),
    ("h(0^{+})=2,\\quad h(0^{-})=-1","Se leen los límites laterales"),
    ("\\dfrac{2+(-1)}{2}","Se promedian"),
    ("S(0)=0.5","Se calcula")],[2,0,3,1],
   "Se identifica el salto, se leen los límites laterales y se promedian.","Se empieza identificando el salto."),
]
S+=cierre("Mini simulacro de convergencia de Dirichlet y fenómeno de Gibbs",[
 banco("es_c1_14","En un salto, la serie converge al promedio de los límites laterales."),
 banco("es_c1_16","$\\dfrac{1+(-1)}{2}=0$."),
 banco("es_c1_17","Gibbs es el pico de cerca de 9 por ciento del salto que no desaparece al agregar términos.")])
prac=[
 {"titulo":"La onda cuadrada","grafica":{"draw":1},"bloques":[P("La onda cuadrada y sus sumas parciales."),EQ("f(x)=\\pm1")]},
 {"titulo":"Agrega términos","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 1 a 10. Abajo se leen el valor máximo de la suma parcial y el exceso sobre 1.")]},
 {"titulo":"Diez términos","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":10,"bloques":[EQ("\\text{pico}\\approx1.18"),P("Con 10 términos el pico sigue en cerca de 1.18, cerca de 9 por ciento del salto.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":10},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Promedia los dos límites laterales."}]}]
preg={"tex":"f(0^{+})=3,\\ f(0^{-})=1.\\ \\text{La serie en 0 vale}","opciones":["$2$","$3$","$1$","$0$"],"correcta":0,
 "explicacion":"En un salto, la serie converge al promedio de los dos límites laterales. El promedio de 3 y 1 es 2.",
 "verificacion":{"formula":"(3+1)/2+0*x","a":0,"esperado":2},
 "pistas":["Es el promedio de los dos límites.","Los límites son 3 y 1.","Su promedio es 2."],
 "errores":["","Tres es el límite de la derecha, y la serie converge al promedio.","Uno es el límite de la izquierda, y la serie converge al promedio.","Cero sería el promedio si los límites fueran opuestos, como menos 1 y 1."]}
res=["En un punto de continuidad la serie converge a f, y en un salto converge al promedio de los límites laterales.","El fenómeno de Gibbs es un pico de cerca de 9 por ciento del salto que no desaparece al agregar términos.","Si f es continua y suave a trozos, la serie converge de manera uniforme."]
write(lesson("es-m1-l3","Lección 3 de 5","Convergencia de Dirichlet y fenómeno de Gibbs",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-gibbs.json")
print('picos',pk)
