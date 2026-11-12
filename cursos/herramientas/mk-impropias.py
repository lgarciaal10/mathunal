from mklib import *
graf={"tipo":"area","x":[0.8,8],"y":[0,1.2],"funcion":"1/(x*x)","primitiva":"0-1/x","a":1,"b":7,"franja":0.25,"limite":0.25,
 "etiquetas":["Área acumulada","Altura de la curva"],"rotulos":["área","altura"],"etiquetaSlider":"Posición de x",
 "alt":"Curva de uno sobre x al cuadrado con el área bajo ella sombreada desde x igual a 1 hasta un x que avanza hacia la derecha"}
glos={"impropia":"Una integral impropia es una integral con un límite infinito o con una función que se dispara dentro del intervalo.",
 "converge":"Una integral converge si el límite que la define existe y es un número finito. Si el límite es infinito o no existe, diverge.",
 "lim":"El límite cuando t tiende a infinito dice a qué valor se acerca una expresión cuando t se hace cada vez más grande."}
ver={"duracion":22.0,"capitulos":[
 [0,2.5,"Esta es la curva de f(x) igual a 1 sobre x al cuadrado."],
 [2.5,5,"Se mide el área bajo ella a partir de x igual a 1, y hacia la derecha no hay un final."],
 [5,11,"Al avanzar x, el área crece pero cada vez más despacio. Con x igual a 2 vale 0.5 y con x igual a 4 vale 0.75."],
 [11,16,"Con x igual a 7 el área es 0.857 y la curva casi toca el eje."],
 [16,22,"Aunque x siga creciendo, el área se acerca a 1 y no lo pasa. Por eso esta integral impropia vale 1."]],
 "canales":{"draw":[[0.3,0],[2.4,1]],"hole":[[2.5,0],[3.3,1]],"d":[[5,1.1],[11,4],[15,7],[22,7.8]],"guide":[[11,0],[12,1]]},
 "intervalos":{"ok":[16,22]}}
S=[
 sec("La idea",None,P("Una {{gl:impropia|integral impropia}} es una integral que no se puede calcular de frente, porque el intervalo no tiene final o porque la función se dispara en un extremo. Se define con un {{gl:lim|límite}}. Si el límite existe y es finito, la integral {{gl:converge|converge}}, y si no, diverge.")),
 sec("Un ejemplo","Un ejemplo",P("Mira esta integral, que mide el área bajo una curva que se extiende hacia la derecha sin parar."),EQ("\\int_{1}^{\\infty}\\dfrac{dx}{x^{2}}"),{"t":"grafica","animar":"dibujar","alt":"Curva que se dibuja y marca el punto de partida en x igual a 1"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Cuando x vale 2, ¿cuánto vale 1 sobre x al cuadrado?","opciones":[0.25,0.5,1,2],"correcta":0.25,"bien":"Muy bien. Vale 1 sobre 4, o sea 0.25. Más abajo se ve cómo se acumula el área.","mal":"Vale 1 sobre 4, o sea 0.25. Más abajo se ve cómo se acumula el área."}),
 sec("El área que se acumula","El área",P("Mira cómo se llena el área y qué valen el área y la altura en cada x."),{"t":"acercando","ds":[2,4,6,7.5],"alt":"El área bajo la curva que va creciendo cada vez más despacio mientras x avanza"},P("Con x igual a 7.5 el área acumulada es <b>0.8667</b> y sigue creciendo muy poco. Parece que se acerca a 1.")),
 sec("Con un límite","Con un límite",P("Para estar seguros, se cambia el infinito por una letra t y se calcula el límite cuando t crece."),
   PASOS([("\\int_{1}^{\\infty}\\dfrac{dx}{x^{2}}=\\lim_{t\\to\\infty}\\int_{1}^{t}\\dfrac{dx}{x^{2}}","Se reemplaza el infinito por t y se calcula la integral hasta t."),
          ("\\int_{1}^{t}\\dfrac{dx}{x^{2}}=\\left[-\\dfrac{1}{x}\\right]_{1}^{t}=1-\\dfrac{1}{t}","Se integra y se evalúa."),
          ("\\lim_{t\\to\\infty}\\left(1-\\dfrac{1}{t}\\right)=1","Cuando t se hace enorme, 1 sobre t se acerca a 0. La integral converge a 1, como mostraba el área.")]),
   OJO("El resultado 1 sale de un límite, no de reemplazar t por infinito en la primitiva sin pensar. Siempre se escribe el límite.")),
 sec("Un caso que diverge","Diverge",P("No todas convergen. A veces el área crece sin parar, aunque la curva se acerque al eje."),
   PASOS([("\\int_{1}^{\\infty}\\dfrac{dx}{x^{2/3}}=\\lim_{t\\to\\infty}\\left[3x^{1/3}\\right]_{1}^{t}","Se integra hasta t."),
          ("=\\lim_{t\\to\\infty}\\left(3t^{1/3}-3\\right)=\\infty","Crece sin límite. La integral diverge.")])),
 sec("El criterio p","Criterio p",P("Las integrales de 1 sobre x a la p son el patrón de comparación más usado."),
   EQ("\\int_{1}^{\\infty}\\dfrac{dx}{x^{p}}\\ \\text{converge si}\\ p>1,\\ \\text{y vale}\\ \\dfrac{1}{p-1}"),
   PASOS([("p=2:\\quad \\int_{1}^{\\infty}\\dfrac{dx}{x^{2}}=1","Converge, porque 2 es mayor que 1."),
          ("p=\\dfrac{3}{2}:\\quad \\int_{1}^{\\infty}\\dfrac{dx}{x^{3/2}}=2","También converge y vale 1 sobre 3 sobre 2 menos 1."),
          ("p\\le 1:\\quad \\text{diverge}","Para p igual a 1 sale el logaritmo, que crece sin límite, y para p menor que 1 crece todavía más rápido.")])),
 sec("Cuando la función se dispara","Se dispara",P("Si la función no está acotada en un extremo, el límite se toma en ese extremo."),
   PASOS([("\\int_{0}^{1}\\dfrac{dx}{\\sqrt{x}}=\\lim_{a\\to 0^{+}}\\int_{a}^{1}x^{-1/2}\\,dx","La función se dispara en x igual a 0. Se empieza en a y se acerca a 0 por la derecha."),
          ("=\\lim_{a\\to 0^{+}}\\left(2-2\\sqrt{a}\\right)=2","Se integra, se evalúa y se hace tender a a 0. Converge a 2.")]),
   P("En este caso el criterio se invierte. La integral de 1 sobre x a la p entre 0 y 1 converge si p es menor que 1."),
   OJO("Antes de integrar hay que revisar si la función se dispara dentro del intervalo. Si no se revisa, se pueden obtener resultados absurdos.")),
 eng("Escapar de la gravedad","Para lanzar una nave a una distancia infinita de la Tierra, hay que hacerle un trabajo contra la gravedad que va disminuyendo con la distancia. Ese trabajo es una integral impropia.","W=\\int_{R}^{\\infty}\\dfrac{GMm}{r^{2}}\\,dr=\\dfrac{GMm}{R}",
   [("Radio de la Tierra","6 371 km"),("Gravedad en la superficie","9.81 m/s²"),("Trabajo por kilogramo","unos 62.5 MJ")],"La integral converge, y por cada kilogramo da gR, o sea unos 62.5 millones de julios. Igualando a la energía cinética sale la velocidad de escape, unos 11.2 kilómetros por segundo. Es un modelo simplificado, porque no tiene en cuenta el aire ni los demás cuerpos del sistema solar."),
 completar("Se calcula la integral de 1 sobre x al cubo desde 1 hasta infinito. La primitiva es menos 1 sobre 2x al cuadrado.","\\lim_{t\\to\\infty}\\left[-\\dfrac{1}{2x^{2}}\\right]_{1}^{t}=\\lim_{t\\to\\infty}\\left(-\\dfrac{1}{2t^{2}}\\right)+[[hueco]]",
   [("\\dfrac{1}{2}","un medio"),("-\\dfrac{1}{2}","menos un medio"),("1","uno")],0,
   ["","Se resta el valor en x igual a 1, que es menos un medio. Restar un negativo da un más, así que queda más un medio.","La primitiva en x igual a 1 vale menos un medio y no menos 1. Al restarla queda más un medio."],"Evalúa la primitiva en 1 y réstala.","La primitiva en x igual a 1 vale menos un medio y se resta. El otro término tiende a 0, así que la integral converge a un medio."),
 error("Alguien analizó esta integral y se equivocó en un paso. Toca el paso que está mal.",
   [("\\text{Se quiere saber si}\\ \\displaystyle\\int_{1}^{\\infty}\\dfrac{dx}{\\sqrt{x}}\\ \\text{converge}","Es la pregunta de partida.","Se quiere saber si la integral de 1 a infinito de 1 sobre raíz de x converge"),
    ("\\text{El integrando tiende a 0, así que la integral converge}","Este paso es el que falla.","El integrando tiende a 0, así que la integral converge"),
    ("\\text{Entonces el área bajo la curva es finita}","La conclusión depende del paso anterior.","Entonces el área bajo la curva es finita")],1,
   "Que el integrando tienda a 0 no basta. Esta integral vale el límite de 2 por la raíz de t menos 2, que es infinito, y diverge. Con el criterio p, el exponente es un medio, que no es mayor que 1.",
   "\\int_{1}^{\\infty}\\dfrac{dx}{\\sqrt{x}}=\\lim_{t\\to\\infty}\\left(2\\sqrt{t}-2\\right)=\\infty","Calcula el límite y no te fíes de que el integrando se acerque a 0."),
 ordenar("Estos son los pasos para integrar 1 sobre la raíz de x entre 0 y 1, pero están desordenados.",
   [("\\displaystyle\\int_{0}^{1}\\dfrac{dx}{\\sqrt{x}}=\\lim_{a\\to 0^{+}}\\int_{a}^{1}\\dfrac{dx}{\\sqrt{x}}","La integral es el límite, cuando a tiende a 0 por la derecha, de la integral de a a 1"),
    ("=\\lim_{a\\to 0^{+}}\\bigl[2\\sqrt{x}\\bigr]_{a}^{1}","Se evalúa la primitiva 2 raíz de x entre a y 1"),
    ("=\\lim_{a\\to 0^{+}}\\left(2-2\\sqrt{a}\\right)","Queda 2 menos 2 raíz de a"),
    ("=2","El límite es 2, así que converge")],[2,0,3,1],
   "Se escribe el límite, se integra, se evalúa en los extremos y se toma el límite final.","Se empieza escribiendo la integral como límite."),
]
S+=cierre("Mini simulacro de integrales impropias",[
 mcq("La integral $\\displaystyle\\int_0^{1}\\frac{dx}{x}$",["Diverge","Converge a $1$","Converge a $0$","Converge a $2$"],0,"La primitiva es $\\ln x$ y $\\ln a\\to-\\infty$ cuando $a\\to0^{+}$, así que diverge."),
 mcq("$\\displaystyle\\int_{1}^{\\infty} \\dfrac{dx}{x}$:",["diverge","converge a $1$","converge a $0$","converge a $\\ln 2$"],0,"La primitiva es $\\ln x$ y $\\ln t\\to\\infty$, así que diverge."),
 mcq("La integral $\\displaystyle\\int_{1}^{\\infty} \\dfrac{dx}{x^{p}}$ converge si y solo si:",["$p > 1$","$p < 1$","$p \\ge 0$","$p \\ne 1$"],0,"Converge solo si $p>1$, y entonces vale $\\frac{1}{p-1}$.")])
prac=[
 {"titulo":"La curva","grafica":{"draw":1},"bloques":[P("Se mide el área bajo esta curva, hacia la derecha."),EQ("f(x)=\\dfrac{1}{x^{2}}")]},
 {"titulo":"El punto de partida","grafica":{"draw":1,"hole":1},"bloques":[P("El área se empieza a medir desde x igual a 1.")]},
 {"titulo":"Mueve x","grafica":{"draw":1,"hole":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La zona sombreada crece y abajo se ve el área y la altura de la curva en x.")]},
 {"titulo":"Cada vez más despacio","grafica":{"draw":1,"hole":1,"guide":1},"laboratorio":True,"d":4,"bloques":[P("Con x igual a 4 el área vale 0.75. La franja amarilla es muy baja y el área casi no crece.")]},
 {"titulo":"El límite","grafica":{"draw":1,"hole":1,"guide":1,"ok":True},"laboratorio":True,"d":6.5,"bloques":[EQ("\\int_{1}^{\\infty}\\dfrac{dx}{x^{2}}=\\lim_{t\\to\\infty}\\left(1-\\dfrac{1}{t}\\right)=1"),P("Con x igual a 6.5 el área ya es 0.846. A medida que x crece, se acerca a 1 sin pasarlo.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"hole":1,"guide":1,"ok":True,"d":6.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Escribe el límite, integra y evalúa."}]}]
preg={"tex":"\\int_{0}^{\\infty}e^{-2x}\\,dx","opciones":["$\\dfrac{1}{2}$","$2$","$1$","Diverge"],"correcta":0,
 "explicacion":"La primitiva de e a la menos 2x es menos un medio de e a la menos 2x. Entre 0 y t queda un medio menos un medio de e a la menos 2t. Cuando t crece, ese último término tiende a 0 y el resultado es un medio.",
 "verificacion":{"formula":"(1-exp(0-2*100))/2+0*x","a":0,"esperado":0.5},
 "pistas":["Escribe la integral como un límite cuando t tiende a infinito.","La primitiva de e a la menos 2x es menos un medio de e a la menos 2x, porque hay que dividir entre el 2 de adentro.","Evalúa entre 0 y t y haz t tender a infinito. e a la menos 2t tiende a 0."],
 "errores":["","Se multiplicó por 2 en vez de dividir. La primitiva lleva un medio, porque al derivar menos un medio de e a la menos 2x aparece un 2.","Ese es el valor de la integral de e a la menos x. Con menos 2x hay que dividir entre 2.","La exponencial decae muy rápido y el área es finita. Calcula el límite y verás que converge."]}
res=["Una integral impropia se define con un límite. Si el límite es finito, converge.","La integral de 1 sobre x a la p desde 1 hasta infinito converge si p es mayor que 1.","Si la función se dispara en un extremo, el límite se toma en ese extremo. Que el integrando tienda a 0 no basta para converger."]
write(lesson("calcint-m2-l4","Lección 4 de 4","Integrales impropias",26,graf,glos,ver,S,prac,preg,res,modulo="Módulo 2 Técnicas avanzadas e impropias"),"calcint-impropias.json")
