import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 1 Series de Fourier"
NT=8
def ind(n): return f"(1+(x-{n}+0.63)/abs(x-{n}+0.63))/2"
def Sn(t): return "+".join(f"({ind(n)})*({2*(-1)**(n+1)/n:.6f})*{math.sin(n*t):.6f}" for n in range(1,NT+1))
TS=[round(-math.pi+k*math.pi/30,5) for k in range(61)]
EL=[{"t":"trazo","puntos":[[str(t),str(t)] for t in TS],"c":3},
    {"t":"trazo","puntos":[[str(t),Sn(t)] for t in TS],"c":0}]
graf={"tipo":"plano","x":[-8.2,8.2],"y":[-4.5,4.5],"a":1,"b":8,"inicio":3,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"cantidad N de términos de la serie","formula":"x"},{"rotulo":"coeficiente b de N, igual a 2 por menos uno elevado a N más 1, entre N","formula":"2*cos(pi*(x+1))/x"}],
 "etiquetas":["Suma parcial con los primeros N senos","Coeficiente del seno número N, que alterna de signo y decrece"],"etiquetaSlider":"Términos N, de 1 a 8",
 "alt":"La función f de x igual a x entre menos pi y pi, en verde, y su suma parcial de Fourier con N términos, en azul. Con N igual a 1 es una sola onda seno. Al subir N la curva azul se acerca a la recta, salvo cerca de los extremos, donde la extensión periódica tiene un salto"}
glos={"fourier":"La serie de Fourier de una función periódica la escribe como una suma de senos y cosenos de frecuencias enteras.",
 "coeficientes":"Los coeficientes a de n y b de n se calculan con integrales de f por coseno y seno de n x, entre menos pi y pi, divididas entre pi.",
 "par":"Una función es par si f de menos x es igual a f de x. Su serie de Fourier tiene solo cosenos.",
 "impar":"Una función es impar si f de menos x es menos f de x. Su serie de Fourier tiene solo senos."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La función es f de x igual a x, entre menos pi y pi. Es impar, así que su serie solo tiene senos."],
 [4,9,"Con un término, la serie ya sigue la forma de la recta, pero se queda corta."],
 [9,15,"Con 3 y con 5 términos se acerca mejor. Cada término agrega un seno más rápido."],
 [15,20,"Con 8 términos casi coincide con la recta, excepto cerca de los extremos."],
 [20,24,"En los extremos la función se corta, porque al repetirla con período 2 pi aparece un salto."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,3],[13,5],[16,8],[24,8]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,24]}}
S=[
 sec("La idea",None,P("Toda función periódica razonable se puede escribir como una suma de senos y cosenos, que es su {{gl:fourier|serie de Fourier}}. Los {{gl:coeficientes|coeficientes}} salen de integrales. Si la función es {{gl:par|par}}, solo aparecen cosenos, y si es {{gl:impar|impar}}, solo aparecen senos. Reconocer la simetría ahorra la mitad del trabajo.")),
 sec("Un ejemplo","Un ejemplo",P("La función f de x igual a x entre menos pi y pi es impar. Mira cómo la serie, solo con senos, se acerca a ella al sumar más términos."),EQ("x=\\sum_{n=1}^{\\infty}\\dfrac{2(-1)^{n+1}}{n}\\operatorname{sen}(nx)"),{"t":"grafica","animar":"dibujar","alt":"Las sumas parciales de la serie de Fourier"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En la serie de x, el coeficiente del primer seno es 2 por menos uno elevado a 2, entre 1. ¿Cuánto vale b1?","opciones":[1,2,4,6],"correcta":2,"bien":"Muy bien. Vale 2, porque menos uno elevado a 2 es 1, y 2 por 1 entre 1 es 2. Más abajo se ve el primer seno.","mal":"Vale 2, porque menos uno elevado a 2 es 1, y 2 por 1 entre 1 da 2. Más abajo se ve el primer seno."}),
 sec("Sumando términos","Los términos",P("Mira la suma parcial con 1, 3, 5 y 8 términos."),{"t":"acercando","ds":[1,3,5,8],"alt":"La suma parcial con cuatro cantidades de términos"},P("Cada término nuevo corrige un poco más. Cerca de los extremos la serie tarda más en llegar a la recta.")),
 sec("Los coeficientes","Los coeficientes",P("Para una función con período 2 pi se usan estas fórmulas."),
   PASOS([("a_{0}=\\dfrac{1}{\\pi}\\displaystyle\\int_{-\\pi}^{\\pi}f(x)\\,dx,\\quad a_{n}=\\dfrac{1}{\\pi}\\displaystyle\\int_{-\\pi}^{\\pi}f(x)\\cos(nx)\\,dx","Los coeficientes de los cosenos."),
          ("b_{n}=\\dfrac{1}{\\pi}\\displaystyle\\int_{-\\pi}^{\\pi}f(x)\\operatorname{sen}(nx)\\,dx","Los coeficientes de los senos."),
          ("f(x)\\sim\\dfrac{a_{0}}{2}+\\displaystyle\\sum_{n\\ge1}\\big(a_{n}\\cos nx+b_{n}\\operatorname{sen}nx\\big)","La serie de Fourier."),
          ("f(x)=x:\\ b_{n}=\\dfrac{2}{n}(-1)^{n+1},\\ b_{1}=2","Los coeficientes de la función del ejemplo.")])),
 sec("Simetrías","Simetrías",P("La paridad dice qué coeficientes se anulan."),
   PASOS([("f\\ \\text{par}\\ \\Rightarrow\\ b_{n}=0","Solo cosenos y el término constante."),
          ("f\\ \\text{impar}\\ \\Rightarrow\\ a_{0}=a_{n}=0","Solo senos."),
          ("f(x)=|x|:\\ \\dfrac{a_{0}}{2}=\\dfrac{\\pi}{2}=1.5708","Par. El promedio de la función es pi medios."),
          ("f(x)=x^{2}:\\ \\dfrac{a_{0}}{2}=\\dfrac{\\pi^{2}}{3}=3.2899,\\qquad f(x)=5:\\ \\text{solo el término constante}","Otras funciones pares.")]),
   OJO("El término constante es a0 entre 2, y es el valor promedio de la función en un período. Es fácil olvidar el dos del denominador.")),
 eng("Armónicos de una fuerza periódica","Una fuerza en forma de diente de sierra actúa sobre una estructura. Se descompone en sus armónicos, que son senos de frecuencias que son múltiplos de la fundamental. Cada armónico tiene una amplitud que se obtiene con el coeficiente b de n.","b_{n}=\\dfrac{2}{n}\\,(-1)^{n+1}",
   [("Fundamental, n igual a 1","amplitud 2"),("Segundo armónico","amplitud 1"),("Tercer armónico","amplitud 0.67")],"Si la estructura tiene una frecuencia natural cerca de uno de estos armónicos, entra en resonancia y vibra mucho. Por eso se calcula el espectro de la fuerza. Los armónicos de orden alto pesan cada vez menos, y suelen bastar los primeros para el análisis."),
 completar("Se aplica la simetría de una función impar. Falta el coeficiente que se anula.","f\\ \\text{impar}\\ \\Rightarrow\\ [[hueco]]=0",
   [("a_{n}","los coeficientes de los cosenos"),("b_{n}","los coeficientes de los senos"),("b_{1}","solo el primer seno")],0,
   ["","Los senos son justamente los términos que sí aparecen en una función impar.","El primer seno no se anula, y para f de x igual a x vale 2."],"Una función impar solo tiene senos.","Los cosenos son pares, y no aparecen en una función impar."),
 error("Alguien analizó la serie de Fourier de f de x igual a x y se equivocó en un paso. Toca el paso que está mal.",
   [("f(x)=x\\ \\text{es impar}","La paridad.","la función es impar"),
    ("\\text{Entonces}\\ b_{n}=0\\ \\text{y solo hay cosenos}","Este paso es el que falla.","los senos se anulan"),
    ("a_{n}=\\dfrac{2}{n}","Los coeficientes.","an vale 2 sobre n")],1,
   "Una función impar tiene a de n igual a cero y solo senos, que es lo contrario. Los coeficientes distintos de cero son los b de n, que valen 2 entre n con signos alternados.",
   "a_{n}=0,\\quad b_{n}=\\dfrac{2}{n}(-1)^{n+1}","Recuerda qué simetría tienen los senos."),
 ordenar("Estos son los pasos para calcular b1 de f de x igual a x en el intervalo de menos pi a pi, pero están desordenados.",
   [("b_{1}=\\dfrac{1}{\\pi}\\displaystyle\\int_{-\\pi}^{\\pi}x\\operatorname{sen}x\\,dx","Se escribe la fórmula"),
    ("\\displaystyle\\int x\\operatorname{sen}x\\,dx=-x\\cos x+\\operatorname{sen}x","Se integra por partes"),
    ("\\dfrac{1}{\\pi}\\Big[(-\\pi\\cos\\pi)-(\\pi\\cos\\pi)\\Big]=\\dfrac{2\\pi}{\\pi}","Se evalúa entre menos pi y pi"),
    ("b_{1}=2","Se calcula")],[2,0,3,1],
   "Se escribe la fórmula, se integra por partes y se evalúa en los extremos.","Se empieza escribiendo la fórmula."),
]
S+=cierre("Mini simulacro de coeficientes de Fourier y simetrías",[
 banco("es_c1_08","Una función impar solo tiene senos."),
 banco("es_c1_10","$b_1=\\dfrac{2}{1}(-1)^{2}=2$."),
 banco("es_c1_11","$\\dfrac{a_0}{2}=\\dfrac{1}{\\pi}\\int_0^{\\pi}x\\,dx=\\dfrac{\\pi}{2}$.")])
prac=[
 {"titulo":"La función","grafica":{"draw":1},"bloques":[P("La recta y sus sumas parciales de Fourier."),EQ("f(x)=x")]},
 {"titulo":"Suma términos","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 1 a 8. Abajo se leen N y el coeficiente del seno número N.")]},
 {"titulo":"Ocho términos","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":8,"bloques":[EQ("b_{8}=-\\dfrac{2}{8}=-0.25"),P("Con 8 términos, la serie casi coincide con la recta.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":8},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El término constante es el valor promedio de la función."}]}]
preg={"tex":"\\text{El término constante}\\ \\dfrac{a_{0}}{2}\\ \\text{de}\\ f(x)=x^{2}\\ \\text{en}\\ (-\\pi,\\pi)\\ \\text{es}","opciones":["$\\dfrac{\\pi^{2}}{3}$","$\\pi^{2}$","$\\dfrac{\\pi}{2}$","$0$"],"correcta":0,
 "explicacion":"El término constante es el promedio de la función. La integral de x al cuadrado de menos pi a pi es 2 pi al cubo entre 3, y al dividir entre 2 pi queda pi al cuadrado entre 3, o sea 3.2899.",
 "verificacion":{"formula":"pi*pi/3+0*x","a":0,"esperado":3.2899},
 "pistas":["Es el promedio de x al cuadrado en el intervalo.","La integral vale 2 pi al cubo entre 3.","Se divide entre la longitud del intervalo, que es 2 pi."],
 "errores":["","Pi al cuadrado es el valor máximo de la función, y no el promedio.","Pi medios es el promedio de la función valor absoluto de x, no de x al cuadrado.","Cero sería el promedio de una función impar, y x al cuadrado es par."]}
res=["Una función par tiene solo cosenos y el término constante, y una impar tiene solo senos.","Los coeficientes son integrales de f por coseno y seno de n x, divididas entre pi.","El término constante es el promedio de la función. Para x al cuadrado vale pi al cuadrado entre 3."]
write(lesson("es-m1-l1","Lección 1 de 5","Coeficientes de Fourier y simetrías",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-coeficientes.json")
