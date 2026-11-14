import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 1 Series de Fourier"
NT=5
def ssin(t): return sum(2*(-1)**(n+1)/n*math.sin(n*t) for n in range(1,NT+1))
def scos(t): return math.pi/2-4/math.pi*sum(math.cos(n*t)/n**2 for n in range(1,2*NT,2))
TS=[round(-math.pi+k*math.pi/30,5) for k in range(61)]
def Ls(t): return f"({ssin(t):.6f})*(1-x)+({scos(t):.6f})*x"
EL=[{"t":"trazo","puntos":[[str(t),f"{t:.5f}*(1-x)+{abs(t):.5f}*x"] for t in TS],"c":3},
    {"t":"trazo","puntos":[[str(t),Ls(t)] for t in TS],"c":0},
    {"t":"segmento","a":["0","-3.6"],"b":["0","3.6"],"c":3,"guion":True,"guia":True}]
graf={"tipo":"plano","x":[-8.2,8.2],"y":[-4.5,4.5],"a":0,"b":1,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"valor de la serie en x igual a pi","formula":"3.141593*x"},{"rotulo":"término constante a0 entre 2","formula":"1.570796*x"}],
 "etiquetas":["0 con la serie de senos, que tiene un salto en pi. Pi con la serie de cosenos, que es continua","0 con senos, porque no tiene término constante. Pi medios con cosenos"],"etiquetaSlider":"Extensión, 0 impar con senos y 1 par con cosenos",
 "alt":"La función f de x igual a x dada solo entre 0 y pi, y sus dos extensiones a menos pi y pi. La impar, en verde, es la recta x y su serie de solo senos tiene saltos en los extremos. La par, que es el valor absoluto de x, tiene una serie de solo cosenos y es continua. La curva azul es la suma parcial de cinco términos"}
glos={"mediorango":"Una función dada solo en el intervalo de 0 a L se puede desarrollar en una serie de solo senos o de solo cosenos, según como se extienda a menos L.",
 "impar":"La extensión impar copia la función con signo contrario en el intervalo negativo. Da una serie de senos.",
 "par":"La extensión par copia la función en el intervalo negativo. Da una serie de cosenos.",
 "frontera":"Las condiciones de frontera deciden la serie. Con extremos en cero se usan senos, y con derivada cero en los extremos se usan cosenos."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La función es f de x igual a x, dada solo entre 0 y pi. Se puede extender de dos maneras al intervalo de menos pi a pi."],
 [4,10,"Con la extensión impar queda una serie de solo senos. En pi hay un salto, así que la serie vale 0 allí."],
 [10,16,"Con la extensión par queda una serie de solo cosenos. La función extendida es continua, y no hay salto ni picos."],
 [16,20,"El término constante de la serie de cosenos es el promedio, pi medios. La de senos no tiene término constante."],
 [20,24,"Así se escoge la serie según las condiciones de frontera del problema."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[7,0],[10,1],[16,1],[24,1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[10,24]}}
S=[
 sec("La idea",None,P("En muchos problemas físicos la función solo está definida en un intervalo de 0 a L. Para desarrollarla en serie de Fourier se la extiende al intervalo simétrico, y hay dos formas. Con la extensión {{gl:impar|impar}} queda una serie de senos, y con la extensión {{gl:par|par}} queda una serie de cosenos. La elección depende de las {{gl:frontera|condiciones de frontera}}.")),
 sec("Un ejemplo","Un ejemplo",P("La función f de x igual a x en el intervalo de 0 a pi. Mueve el deslizador para ver las dos extensiones y las sumas parciales de sus series."),EQ("x=\\sum\\dfrac{2(-1)^{n+1}}{n}\\operatorname{sen}nx,\\qquad x=\\dfrac{\\pi}{2}-\\dfrac{4}{\\pi}\\sum_{n\\ \\text{impar}}\\dfrac{\\cos nx}{n^{2}}"),{"t":"grafica","animar":"dibujar","alt":"Las dos extensiones de la función"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Para obtener una serie que solo tenga senos, ¿cómo se extiende la función al intervalo negativo?","opciones":["De forma impar","De forma par"],"correcta":"De forma impar","bien":"Muy bien. Una función impar solo tiene senos. Más abajo se ve el efecto en los extremos.","mal":"De forma impar, porque una función impar solo tiene senos. Más abajo se ve el efecto en los extremos."}),
 sec("Las dos extensiones","Las extensiones",P("Mira las dos extensiones y sus sumas parciales."),{"t":"acercando","ds":[0,1],"alt":"La extensión impar y la par"},P("La serie de cosenos converge mejor, porque la extensión par es continua. La de senos tiene un salto en pi.")),
 sec("Cómo se calcula","Cómo se calcula",P("Se usan las fórmulas de la parte par o impar, integrando solo de 0 a pi."),
   PASOS([("b_{n}=\\dfrac{2}{\\pi}\\displaystyle\\int_{0}^{\\pi}f(x)\\operatorname{sen}(nx)\\,dx","Serie de senos, con extensión impar."),
          ("a_{n}=\\dfrac{2}{\\pi}\\displaystyle\\int_{0}^{\\pi}f(x)\\cos(nx)\\,dx","Serie de cosenos, con extensión par."),
          ("f(x)=\\operatorname{sen}x:\\ \\dfrac{a_{0}}{2}=\\dfrac{1}{\\pi}\\displaystyle\\int_{0}^{\\pi}\\operatorname{sen}x\\,dx=\\dfrac{2}{\\pi}=0.6366","El término constante de la serie de cosenos."),
          ("\\operatorname{sen}^{2}x=\\dfrac12-\\dfrac12\\cos2x","Esta función ya está escrita como una serie de Fourier.")])),
 sec("Cuál escoger","Cuál escoger",P("Las condiciones de frontera de la ecuación orientan la elección."),
   PASOS([("u(0)=u(L)=0\\ \\Rightarrow\\ \\text{serie de senos}","Los extremos fijos, como una cuerda sujeta."),
          ("u'(0)=u'(L)=0\\ \\Rightarrow\\ \\text{serie de cosenos}","Los extremos aislados, sin flujo de calor."),
          ("\\text{extensión par continua}\\ \\Rightarrow\\ \\text{sin picos de Gibbs}","La serie de cosenos suele converger más rápido.")]),
   OJO("La función original, entre 0 y L, es la misma en los dos casos. Lo que cambia es la extensión, y por eso la serie converge distinto fuera del intervalo, aunque coincidan adentro.")),
 eng("Una barra con los extremos aislados","Una barra metálica de longitud pi tiene sus extremos aislados térmicamente, así que no hay flujo de calor en ellos. La condición es que la derivada de la temperatura sea cero en los dos extremos, y la solución se arma con una serie de cosenos.","u_{x}(0,t)=u_{x}(\\pi,t)=0\\ \\Rightarrow\\ \\text{cosenos}",
   [("Extremos","aislados"),("Condición","derivada nula"),("Serie","de cosenos")],"En la serie de cosenos el término constante es la temperatura promedio de la barra, que se mantiene con el tiempo porque no entra ni sale calor. Con los extremos a temperatura fija, en cambio, se usan senos, y la temperatura tiende al valor de los extremos. Elegir bien la extensión es lo que hace que el desarrollo cumpla las condiciones de frontera."),
 completar("Se elige la extensión para una serie de solo senos.","\\text{Se extiende la función de forma}\\ [[hueco]]",
   [("\\text{impar}","impar"),("\\text{par}","par"),("\\text{constante}","constante")],0,
   ["","Una extensión par da una serie de cosenos y no de senos.","Una extensión constante no corresponde a una serie de Fourier de senos."],"Los senos son funciones impares.","La extensión impar da una función impar, que solo tiene senos."),
 error("Alguien calculó el término constante de la serie de cosenos de seno de x en el intervalo de 0 a pi y se equivocó en un paso. Toca el paso que está mal.",
   [("\\dfrac{a_{0}}{2}=\\dfrac{1}{\\pi}\\displaystyle\\int_{0}^{\\pi}\\operatorname{sen}x\\,dx","La fórmula.","el promedio de la función"),
    ("\\displaystyle\\int_{0}^{\\pi}\\operatorname{sen}x\\,dx=1","Este paso es el que falla.","la integral vale 1"),
    ("\\dfrac{a_{0}}{2}=\\dfrac{1}{\\pi}","Resultado.","queda 1 sobre pi")],1,
   "La integral de seno de x entre 0 y pi es menos coseno evaluado en pi menos en 0, o sea 1 más 1, que da 2. El término constante es 2 entre pi, o sea 0.6366.",
   "\\displaystyle\\int_{0}^{\\pi}\\operatorname{sen}x\\,dx=2\\ \\Rightarrow\\ \\dfrac{a_{0}}{2}=\\dfrac{2}{\\pi}","Evalúa menos coseno en los dos extremos."),
 ordenar("Estos son los pasos para hallar la serie de Fourier de seno al cuadrado de x, pero están desordenados.",
   [("\\operatorname{sen}^{2}x=\\dfrac{1-\\cos2x}{2}","Se usa la identidad del ángulo doble"),
    ("=\\dfrac12-\\dfrac12\\cos2x","Se separan los términos"),
    ("\\dfrac{a_{0}}{2}=\\dfrac12,\\ \\ a_{2}=-\\dfrac12","Se identifican los coeficientes"),
    ("\\text{los demás coeficientes valen}\\ 0","No hace falta integrar")],[2,0,3,1],
   "Se usa la identidad, se separan los términos y se identifican los coeficientes sin integrar.","Se empieza con la identidad del ángulo doble."),
]
S+=cierre("Mini simulacro de series de senos y cosenos",[
 banco("es_c1_19","Para una serie de senos se extiende la función de forma impar."),
 banco("es_c1_20","$\\dfrac{1}{\\pi}\\int_0^{\\pi}\\sin x\\,dx=\\dfrac{2}{\\pi}=0.6366$."),
 banco("es_c1_21","$\\sin^2x=\\dfrac{1}{2}-\\dfrac{1}{2}\\cos2x$.")])
prac=[
 {"titulo":"Dos extensiones","grafica":{"draw":1},"bloques":[P("La función x en el intervalo de 0 a pi y sus extensiones."),EQ("f(x)=x,\\quad 0<x<\\pi")]},
 {"titulo":"Cambia la extensión","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador entre 0 y 1. Abajo se leen el valor de la serie en pi y el término constante.")]},
 {"titulo":"La extensión par","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("S(\\pi)=\\pi,\\quad \\dfrac{a_{0}}{2}=\\dfrac{\\pi}{2}"),P("Con la extensión par la función es continua, y la serie vale pi en pi.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Una serie de cosenos es una serie de una función par."}]}]
preg={"tex":"\\text{Serie de cosenos de }f\\text{ en }[0,L]\\text{. Se extiende }f","opciones":["de forma par a $[-L,L]$","de forma impar a $[-L,L]$","con período $L$","como cero"],"correcta":0,
 "explicacion":"Los cosenos son funciones pares, así que la extensión que da una serie de solo cosenos es la par. Eso copia la función en el intervalo negativo.",
 "verificacion":{"formula":"1+0*x","a":0,"esperado":1},
 "pistas":["Los cosenos son funciones pares.","La serie solo tendrá lo que tenga la extensión.","Es la extensión par."],
 "errores":["","La extensión impar da una serie de solo senos.","Extender con período L no da necesariamente una serie de cosenos.","Extender con cero no es una extensión par ni impar de la función."]}
res=["Una función dada en el intervalo de 0 a L se desarrolla en senos con la extensión impar y en cosenos con la par.","Con extremos en cero se usa la serie de senos, y con derivada cero en los extremos la de cosenos.","La serie de cosenos suele converger más rápido, porque la extensión par es continua."]
write(lesson("es-m1-l5","Lección 5 de 5","Series de senos y cosenos",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-senoscosenos.json")
