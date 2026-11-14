import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 2 Transformada de Fourier y EDP de evolución"
TS=[round(k*math.pi/60,5) for k in range(61)]
EL=[{"t":"trazo","puntos":[[str(t),f"exp(-x)*{math.sin(t):.6f}+exp(-9*x)*{math.sin(3*t):.6f}"] for t in TS],"c":0},
    {"t":"trazo","puntos":[[str(t),f"exp(-x)*{math.sin(t):.6f}"] for t in TS],"c":3}]
graf={"tipo":"plano","x":[-1.2,4.4],"y":[-2.0,2.0],"a":0,"b":1,"inicio":0,"elementos":EL,
 "lecturas":[{"rotulo":"amplitud del modo uno, e elevado a menos t","formula":"exp(-x)"},{"rotulo":"amplitud del modo tres, e elevado a menos 9 t","formula":"exp(-9*x)"}],
 "etiquetas":["El modo lento, que domina al final","El modo rápido, que se apaga mucho antes"],"etiquetaSlider":"Tiempo t, de 0 a 1",
 "alt":"El perfil de temperatura de una barra con los extremos a 0, formado al inicio por dos ondas, seno de x y seno de 3x. Al avanzar el tiempo la onda de 3x, que decae como e a la menos 9t, desaparece enseguida, y queda la onda de seno de x, que decae despacio. La curva verde es solo el modo uno"}
glos={"calor":"La ecuación de calor, u sub t igual a k u sub x x, describe cómo se difunde la temperatura. Los picos y los detalles se suavizan con el tiempo.",
 "separacion":"En la separación de variables se busca la solución como un producto de una función de x y una de t.",
 "modo":"Un modo es una solución sencilla, como e elevado a menos n al cuadrado t por seno de n x. Cada modo decae con su propia rapidez.",
 "equilibrio":"El estado de equilibrio es hacia donde tiende la solución cuando el tiempo crece. Con los extremos a cero, es cero en todo el intervalo."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La temperatura inicial es la suma de dos ondas, seno de x y seno de 3x, con los extremos de la barra a cero."],
 [4,10,"Cada onda se amortigua con su propia rapidez. La de seno de 3x decae como e a la menos 9t, mucho más rápido que la de seno de x."],
 [10,16,"Con t igual a 0.3, la onda rápida casi desapareció, y queda seno de x con amplitud 0.74."],
 [16,20,"Con el tiempo todo tiende a cero, que es el estado de equilibrio, porque los extremos están a cero."],
 [20,24,"Los modos de alta frecuencia se disipan primero, y por eso el calor suaviza los detalles."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,0.05],[13,0.3],[16,0.3],[18,1],[24,1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("La ecuación de {{gl:calor|calor}} describe cómo se reparte la temperatura con el tiempo. Se resuelve por {{gl:separacion|separación de variables}}. Cada {{gl:modo|modo}} es un seno de n x que decae como e elevado a menos n al cuadrado t. Con los extremos a temperatura cero, la solución tiende al {{gl:equilibrio|equilibrio}}, que es cero en toda la barra.")),
 sec("Un ejemplo","Un ejemplo",P("La temperatura inicial es la suma de seno de x y seno de 3x. Mueve el tiempo y mira cuál onda sobrevive."),EQ("u_{t}=u_{xx},\\qquad u(x,t)=e^{-t}\\operatorname{sen}x+e^{-9t}\\operatorname{sen}3x"),{"t":"grafica","animar":"dibujar","alt":"El perfil de temperatura que se suaviza"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El modo de seno de 3x decae como e elevado a menos 9t. Con t igual a 0, ¿cuánto vale e elevado a 0?","opciones":[0,1,9,3],"correcta":1,"bien":"Muy bien. Vale 1, así que al inicio el modo conserva su amplitud. Más abajo se ve cómo se apaga.","mal":"Vale 1, porque cualquier número elevado a 0 es 1. Al inicio el modo conserva toda su amplitud. Más abajo se ve cómo se apaga."}),
 sec("El paso del tiempo","El tiempo",P("Mira el perfil con t igual a 0, 0.05, 0.3 y 1."),{"t":"acercando","ds":[0,0.05,0.3,1],"alt":"El perfil de temperatura en cuatro instantes"},P("A t igual a 0.05 el modo de seno de 3x ya perdió más de un tercio y conserva cerca de 64 por ciento, y a t igual a 0.3 casi desapareció, porque queda cerca de 7 por ciento.")),
 sec("Separación de variables","Separación",P("Se busca la solución como un producto, y se obtienen dos ecuaciones sencillas."),
   PASOS([("u(x,t)=X(x)\\,T(t)","Se propone una solución separada."),
          ("\\dfrac{T'}{T}=\\dfrac{X''}{X}=-\\lambda","Cada lado depende de una sola variable, así que son iguales a una constante."),
          ("X(0)=X(\\pi)=0\\ \\Rightarrow\\ X=\\operatorname{sen}nx,\\ \\lambda=n^{2}","Las condiciones en los extremos fijan X y la constante."),
          ("u_{n}=e^{-n^{2}t}\\operatorname{sen}nx","El modo n.")]),
   OJO("La constante de separación es negativa, porque con los extremos fijos hay oscilación en x. Si fuera positiva o cero, la única solución con los extremos en cero es la nula.")),
 sec("La solución general","La solución",P("Se combinan los modos para ajustar el dato inicial."),
   PASOS([("u(x,t)=\\displaystyle\\sum_{n\\ge1}b_{n}\\,e^{-n^{2}t}\\operatorname{sen}nx","La solución, con los b de n del desarrollo de seno del dato inicial."),
          ("u(x,0)=\\operatorname{sen}3x\\ \\Rightarrow\\ u=e^{-9t}\\operatorname{sen}3x","Con un solo modo en el dato inicial."),
          ("n=3,\\ t=1:\\ e^{-9}\\approx0.00012","A t igual a 1 el modo 3 casi no queda."),
          ("t\\to\\infty:\\ u\\to0","Con los extremos a cero, la barra se enfría hasta cero.")]),
   OJO("Si la ecuación es u sub t igual a k u sub x x, el exponente es menos k n al cuadrado t. La constante k, la difusividad, solo cambia la rapidez del proceso.")),
 eng("El enfriamiento de una barra de acero","Una barra de acero de 10 centímetros tiene los extremos mantenidos a cero grados de diferencia con su entorno. Su temperatura interior se reparte según la ecuación de calor, y el modo más lento decae con una constante de tiempo de L al cuadrado entre pi al cuadrado por la difusividad.","\\tau=\\dfrac{L^{2}}{\\pi^{2}\\alpha}\\approx84\\ \\text{s}",
   [("Longitud","0.1 m"),("Difusividad del acero","cerca de 1.2×10⁻⁵ m²/s"),("Constante de tiempo del modo uno","cerca de 84 s")],"Esa constante de tiempo dice que, después de unos 84 segundos, la parte lenta de la temperatura se redujo a 37 por ciento. Los detalles finos, de modos más altos, desaparecen mucho antes. Con esta fórmula se estima cuánto tarda un molde o una pieza en enfriarse, y en la práctica se ajusta con las condiciones reales de contorno."),
 completar("Se halla el exponente del modo n de la ecuación de calor con k igual a 1.","u_{n}(x,t)=e^{-[[hueco]]\\,t}\\operatorname{sen}(nx)",
   [("n^{2}","n al cuadrado"),("n","n"),("1","uno")],0,
   ["","Con exponente n, el modo no cumple la ecuación. La segunda derivada en x da menos n al cuadrado.","Con exponente 1, todos los modos decaerían igual, y no es así."],"La segunda derivada de seno de n x es menos n al cuadrado por seno de n x.","Por eso el exponente es n al cuadrado por k por t."),
 error("Alguien halló el exponente del modo seno de 3x en la ecuación de calor y se equivocó en un paso. Toca el paso que está mal.",
   [("u=e^{-\\lambda t}\\operatorname{sen}3x","Se propone un modo.","el modo con una constante"),
    ("u_{t}=u_{xx}\\ \\Rightarrow\\ -\\lambda=-3","Este paso es el que falla.","queda lambda igual a 3"),
    ("u=e^{-3t}\\operatorname{sen}3x","Resultado.","el modo es e a la menos 3t")],1,
   "La segunda derivada de seno de 3x es menos 9 por seno de 3x, y no menos 3. Entonces lambda vale 9 y el modo es e elevado a menos 9t por seno de 3x.",
   "u_{xx}=-9\\operatorname{sen}3x\\ \\Rightarrow\\ \\lambda=9","Deriva dos veces seno de 3x."),
 ordenar("Estos son los pasos de la separación de variables para la ecuación de calor, pero están desordenados.",
   [("u=X(x)\\,T(t)","Se propone una solución separada"),
    ("\\dfrac{T'}{T}=\\dfrac{X''}{X}=-\\lambda","Se separan las variables"),
    ("X=\\operatorname{sen}nx,\\quad \\lambda=n^{2}","Los extremos fijos determinan X y lambda"),
    ("u=e^{-n^{2}t}\\operatorname{sen}nx","Se arma el modo")],[2,0,3,1],
   "Se propone un producto, se separa en dos ecuaciones, se fija X y se arma el modo.","Se empieza proponiendo una solución separada."),
]
S+=cierre("Mini simulacro de la ecuación de calor",[
 banco("es_c2_19","La ecuación de calor es de primer orden en t y de segundo en x."),
 banco("es_c2_20","El modo de seno de 3x decae como $e^{-9t}$."),
 banco("es_c2_22","Con los extremos a 0, la temperatura tiende a 0.")])
prac=[
 {"titulo":"Dos ondas","grafica":{"draw":1},"bloques":[P("La temperatura inicial es la suma de dos modos."),EQ("u(x,0)=\\operatorname{sen}x+\\operatorname{sen}3x")]},
 {"titulo":"Avanza el tiempo","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la amplitud del modo uno y la del modo tres.")]},
 {"titulo":"Sobrevive el modo uno","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.3,"bloques":[EQ("e^{-0.3}=0.74,\\quad e^{-2.7}=0.07"),P("Con t igual a 0.3, el modo de seno de x conserva 74 por ciento y el de 3x solo 7 por ciento.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El exponente es n al cuadrado por t."}]}]
preg={"tex":"u_{t}=u_{xx},\\ u(x,0)=\\operatorname{sen}2x,\\ u(0,t)=u(\\pi,t)=0.\\ \\text{La solución es}","opciones":["$e^{-4t}\\operatorname{sen}2x$","$e^{-2t}\\operatorname{sen}2x$","$\\operatorname{sen}2x\\cos2t$","$e^{-t}\\operatorname{sen}2x$"],"correcta":0,
 "explicacion":"El modo n igual a 2 decae como e elevado a menos n al cuadrado t, o sea e elevado a menos 4t. La solución es e a la menos 4t por seno de 2x.",
 "verificacion":{"formula":"exp(-4*0.5)+0*x","a":0,"esperado":0.1353},
 "pistas":["El modo n decae con n al cuadrado.","Aquí n es 2.","El exponente es menos 4t."],
 "errores":["","Menos 2t sería con exponente n, y falta elevar al cuadrado.","Con coseno de 2t sería una ecuación de onda, y no de calor.","Menos t sería para el modo n igual a 1."]}
res=["La ecuación de calor suaviza la temperatura, y cada modo seno de n x decae como e elevado a menos n al cuadrado t.","Se resuelve por separación de variables, y con los extremos a cero el equilibrio es cero.","Los modos de frecuencia alta se apagan primero."]
write(lesson("es-m2-l2","Lección 2 de 5","Ecuación de calor",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-calor.json")
