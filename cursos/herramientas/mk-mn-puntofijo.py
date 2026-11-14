import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
from fundlib import *
MOD="Módulo 1 Errores y ecuaciones no lineales"
X=[1.0]
for _ in range(8): X.append(math.cos(X[-1]))
PF=0.7390851332
def ind(n): return f"(1+(x-{n}-0.37)/abs(x-{n}-0.37))/2"
EL=[{"t":"trazo","puntos":[[str(round(0.05*k,2)),str(round(math.cos(0.05*k),5))] for k in range(0,29)],"c":0},
    {"t":"recta","p":["0","0"],"dir":["1","1"],"c":3}]
for n in range(8):
    a,b,c=X[n],X[n+1],X[n+1]
    I=ind(n)
    # vertical (xn,xn)->(xn,g(xn)) y horizontal (xn,g)->(g,g); colapsan en (x0,x0)
    EL.append({"t":"segmento","a":[f"1+({I})*({a-1:.9f})",f"1+({I})*({a-1:.9f})"],"b":[f"1+({I})*({a-1:.9f})",f"1+({I})*({b-1:.9f})"],"c":1})
    EL.append({"t":"segmento","a":[f"1+({I})*({a-1:.9f})",f"1+({I})*({b-1:.9f})"],"b":[f"1+({I})*({b-1:.9f})",f"1+({I})*({b-1:.9f})"],"c":2})
EL.append({"t":"punto","p":[str(PF),str(PF)],"c":3})
graf={"tipo":"plano","x":[-0.9,2.4],"y":[-0.3,1.5],"a":0,"b":8,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"aproximación x de n, con x0 igual a 1","formula":"("+lagr([round(v,9) for v in X])+")"},{"rotulo":"distancia al punto fijo 0.7391","formula":"("+lagr([round(abs(v-PF),9) for v in X])+")"}],
 "etiquetas":["Aproximación después de n iteraciones","Error, que se reduce con oscilaciones"],"etiquetaSlider":"Iteración, de 0 a 8",
 "alt":"La curva y igual a coseno de x y la recta y igual a x. Desde x igual a 1 se sube hasta la curva y se va en horizontal hasta la recta, y se repite. Los segmentos forman una espiral que se cierra alrededor del cruce, en 0.7391, que es el punto fijo"}
glos={"fijo":"Un punto fijo de g es un número p tal que g de p es igual a p. Es donde la curva y igual a g de x cruza la recta y igual a x.",
 "iteracion":"La iteración de punto fijo parte de x0 y repite x de n más 1 igual a g de x de n.",
 "contraccion":"Si el valor absoluto de la derivada de g en el punto fijo es menor que 1, la iteración converge si se parte de un punto cercano.",
 "lineal":"La convergencia es lineal si el error de cada paso es una fracción fija del error anterior."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La curva es g de x igual a coseno de x, y la recta es y igual a x. Un punto fijo está donde se cruzan."],
 [4,10,"Se parte de x0 igual a 1. Se sube hasta la curva, se va en horizontal hasta la recta, y se repite."],
 [10,16,"La espiral se cierra alrededor del cruce, en 0.7391. Las aproximaciones alternan un lado y otro."],
 [16,20,"Converge porque la pendiente de la curva en ese punto, en valor absoluto, es 0.67, menor que 1."],
 [20,24,"Si la pendiente fuera mayor que 1, la espiral se abriría y la iteración no convergería."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[7,2],[10,4],[14,6],[17,8],[24,8]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Un {{gl:fijo|punto fijo}} de g es un número que g deja igual. Para encontrarlo se usa la {{gl:iteracion|iteración}} de punto fijo, que aplica g una y otra vez. Cuando la curva de g es suave cerca del punto fijo, la {{gl:contraccion|convergencia}} depende de la pendiente de g allí. Si es menor que 1 en valor absoluto, la iteración converge de forma {{gl:lineal|lineal}}.")),
 sec("Un ejemplo","Un ejemplo",P("Se parte de x igual a 1 y se aplica el coseno una y otra vez. Mira cómo se forma la espiral."),EQ("x_{n+1}=\\cos x_{n},\\qquad x_{0}=1"),{"t":"grafica","animar":"dibujar","alt":"La espiral de la iteración de punto fijo"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con x0 igual a 1, el siguiente valor es el coseno de 1, y redondeado vale 0.54. Si luego se aplica el coseno a 0.54, ¿sube o baja el valor respecto de 0.54?","opciones":["Sube","Baja"],"correcta":"Sube","bien":"Muy bien. Sube a 0.86. La iteración oscila alrededor del punto fijo. Más abajo se ve la espiral.","mal":"Sube, a 0.86. Los valores oscilan, uno arriba y otro abajo del punto fijo. Más abajo se ve la espiral."}),
 sec("Las iteraciones","Las iteraciones",P("Mira la espiral con 0, 2, 4 y 8 iteraciones."),{"t":"acercando","ds":[0,2,4,8],"alt":"La espiral con cuatro cantidades de iteraciones"},P("Las aproximaciones se acercan a 0.7391 con oscilaciones cada vez más pequeñas.")),
 sec("Cuándo converge","Cuándo converge",P("Todo depende de la pendiente de g en el punto fijo."),
   PASOS([("|g'(p)|<1\\ \\Rightarrow\\ \\text{convergencia local}","Si el valor absoluto de la derivada es menor que 1."),
          ("g(x)=\\cos x:\\ |g'(0.74)|=\\operatorname{sen}0.74\\approx0.67","En el ejemplo, la derivada vale 0.67 en valor absoluto, así que converge."),
          ("0<|g'(p)|<1\\ \\Rightarrow\\ \\text{convergencia lineal}","El error se multiplica por unos 0.67 en cada paso."),
          ("|g'(p)|>1\\ \\Rightarrow\\ \\text{diverge}","La espiral se abre.")]),
   OJO("Una sola ecuación puede escribirse como punto fijo de varias maneras, y no todas convergen. Hay que elegir la g con derivada pequeña en el punto fijo.")),
 sec("Calcular un punto fijo","Calcular",P("Para algunas funciones el punto fijo se puede calcular a mano."),
   PASOS([("g(p)=p","La definición."),
          ("g(x)=\\dfrac{x}{3}-5:\\ \\ p=\\dfrac{p}{3}-5","Se plantea la ecuación."),
          ("\\dfrac{2p}{3}=-5\\ \\Rightarrow\\ p=-7.5","Se despeja p.")]),
   OJO("Para detener la iteración se compara la diferencia entre dos aproximaciones consecutivas con la tolerancia. Una diferencia pequeña no garantiza un error pequeño si la convergencia es muy lenta.")),
 eng("El factor de fricción en una tubería","La ecuación de Colebrook para el factor de fricción f de un fluido en una tubería es implícita, porque f está a los dos lados. Se resuelve como iteración de punto fijo, partiendo de un valor razonable de f y reemplazándolo en el lado derecho.","\\dfrac{1}{\\sqrt{f}}=-2\\log_{10}\\left(\\dfrac{\\varepsilon/D}{3.7}+\\dfrac{2.51}{\\mathrm{Re}\\sqrt{f}}\\right)",
   [("Reynolds","100 000"),("Rugosidad relativa","0.001"),("Factor de fricción","cerca de 0.022")],"Para estos datos, el factor de fricción queda cerca de 0.022. La iteración converge rápido porque el lado derecho depende poco de f, o sea, la derivada es pequeña. Este tipo de ecuación implícita aparece en hidráulica, en transferencia de calor y en el diseño de redes de tuberías."),
 completar("Se calcula el punto fijo de g de x igual a x entre 3 menos 5. Falta el valor.","\\dfrac{2p}{3}=[[hueco]]",
   [("-5","menos cinco"),("5","cinco"),("-15","menos quince")],0,
   ["","El signo es negativo, porque p menos p entre 3 queda igual a menos 5.","Menos quince sería el valor de p multiplicado por 3, y la ecuación aún no se despeja."],"Pasa p entre 3 al lado izquierdo y deja el término constante.","De p igual a p entre 3 menos 5 sale 2p entre 3 igual a menos 5."),
 error("Alguien analizó la convergencia de una iteración de punto fijo y se equivocó en un paso. Toca el paso que está mal.",
   [("g(x)=1.5x-1,\\quad p=2","La función y su punto fijo.","g de 2 es 2"),
    ("g'(p)=1.5","La derivada.","la derivada vale 1.5"),
    ("\\text{Entonces converge, porque}\\ g'(p)>0","Este paso es el que falla.","converge porque es positiva")],2,
   "La condición es que el valor absoluto de la derivada sea menor que 1. Aquí vale 1.5, que es mayor que 1, así que la iteración diverge, aunque la derivada sea positiva.",
   "|g'(p)|=1.5>1\\ \\Rightarrow\\ \\text{diverge}","Revisa cuál es la condición exacta."),
 ordenar("Estos son los pasos para iterar con el coseno desde x0 igual a 1, pero están desordenados.",
   [("x_{0}=1","Se parte del valor inicial"),
    ("x_{1}=\\cos1=0.5403","Se aplica g una vez"),
    ("x_{2}=\\cos0.5403=0.8576","Se aplica g otra vez"),
    ("|x_{n+1}-x_{n}|<\\text{tolerancia}","Se detiene cuando el cambio es pequeño")],[2,0,3,1],
   "Se parte del valor inicial, se aplica g varias veces y se detiene cuando el cambio es menor que la tolerancia.","Se empieza con el valor inicial."),
]
S+=cierre("Mini simulacro de iteración de punto fijo",[
 banco("mn_c1_11","La iteración converge localmente si el valor absoluto de la derivada es menor que 1."),
 banco("mn_c1_12","$p=\\dfrac{p}{3}-5\\Rightarrow p=-7.5$."),
 banco("mn_c1_14","Con derivada entre 0 y 1, el error se multiplica por una constante, es decir, convergencia lineal.")])
prac=[
 {"titulo":"La curva y la recta","grafica":{"draw":1},"bloques":[P("El punto fijo es donde la curva cruza la recta."),EQ("g(x)=\\cos x")]},
 {"titulo":"Itera","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 8. Abajo se leen la aproximación y su distancia al punto fijo.")]},
 {"titulo":"Ocho iteraciones","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":8,"bloques":[EQ("x_{8}=0.7504,\\quad p=0.7391"),P("Con ocho iteraciones, el error ya es de unos 0.011.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":8},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Compara el valor absoluto de la derivada con 1."}]}]
preg={"tex":"\\text{Si}\\ g'(p)=-0.5\\ \\text{en el punto fijo, la iteración}","opciones":["converge, de forma lineal","diverge","converge cuadráticamente","no se puede decir"],"correcta":0,
 "explicacion":"El valor absoluto de la derivada es 0.5, que es menor que 1 y distinto de cero. Entonces la iteración converge de forma lineal, y el signo negativo hace que las aproximaciones oscilen.",
 "verificacion":{"formula":"abs(-0.5)+0*x","a":0,"esperado":0.5},
 "pistas":["Calcula el valor absoluto de la derivada.","Es 0.5, menor que 1.","Como no es cero, la convergencia es lineal."],
 "errores":["","Para divergir haría falta que el valor absoluto superara 1.","La convergencia cuadrática exige que la derivada valga 0 en el punto fijo.","Sí se puede decir, porque el valor de la derivada decide."]}
res=["Un punto fijo cumple g de p igual a p, y se busca iterando x de n más 1 igual a g de x de n.","La iteración converge si el valor absoluto de g prima de p es menor que 1, y lo hace de forma lineal.","Una ecuación se puede escribir como punto fijo de varias maneras, y conviene la que tenga la derivada más pequeña."]
write(lesson("mn-m1-l3","Lección 3 de 4","Iteración de punto fijo",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-puntofijo.json")
