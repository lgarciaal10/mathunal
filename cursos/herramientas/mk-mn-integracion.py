import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
MOD="Módulo 3 Ajuste, integración y ecuaciones diferenciales"
def ind(i): return f"(1+(x-{i}-0.37)/abs(x-{i}-0.37))/2"
EL=[{"t":"trazo","puntos":[[str(round(0.05*k,2)),str(round((0.05*k)**2,4))] for k in range(0,41)],"c":0}]
for i in range(8):
    ua=f"{2*i}/x"; ub=f"{2*(i+1)}/x"
    a=f"({ind(i)})*(({ua})+2-abs(({ua})-2))/2"; b=f"({ind(i)})*(({ub})+2-abs(({ub})-2))/2"
    EL.append({"t":"poligono","puntos":[[a,"0"],[b,"0"],[b,f"({b})*({b})"],[a,f"({a})*({a})"]],"c":3})
graf={"tipo":"plano","x":[-0.9,3.0],"y":[-0.7,4.7],"a":1,"b":8,"inicio":2,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"aproximación por n trapecios de la integral de x al cuadrado entre 0 y 2","formula":"8/3+4/(3*x*x)"},{"rotulo":"error, la aproximación menos 8 sobre 3","formula":"4/(3*x*x)"}],
 "etiquetas":["Regla del trapecio compuesta. El valor exacto es 8 entre 3, o sea 2.6667","El error es 4 entre 3 por n al cuadrado, y baja cuando n crece"],"etiquetaSlider":"Número de trapecios n, de 1 a 8",
 "alt":"La curva y igual a x al cuadrado entre 0 y 2 y n trapecios que aproximan el área bajo ella. Con un trapecio el área es 4, con dos es 3 y con cuatro es 2.75. Al aumentar n el área se acerca al valor exacto, 2.6667"}
glos={"trapecio":"La regla del trapecio aproxima el área bajo la curva con trapecios. Su error en la versión compuesta es de orden h al cuadrado.",
 "simpson":"La regla de Simpson aproxima la curva por parábolas. Su error compuesto es de orden h a la cuarta, e integra exactamente los polinomios hasta grado 3.",
 "gauss":"La cuadratura de Gauss-Legendre con n nodos integra exactamente los polinomios de grado hasta 2n menos 1. Elige los nodos y los pesos de la mejor forma posible.",
 "orden":"El orden de un método dice cómo baja el error al achicar el paso h. Con orden 2, al reducir h a la mitad el error baja a la cuarta parte."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se quiere el área bajo x al cuadrado entre 0 y 2, que es 8 entre 3, o 2.6667. Se aproxima con trapecios."],
 [4,9,"Con un solo trapecio el resultado es 4, mucho más que el valor exacto."],
 [9,14,"Con 2 trapecios da 3, y con 4 trapecios da 2.75."],
 [14,19,"El error es 4 entre 3 por n al cuadrado. Al duplicar n, el error baja a la cuarta parte."],
 [19,24,"La regla de Simpson usa parábolas en vez de rectas, y para x al cuadrado da el valor exacto."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,2],[12,4],[15,4],[16,8],[24,8]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[14,24]}}
S=[
 sec("La idea",None,P("Cuando una integral no se puede calcular a mano, o solo se tienen datos, se aproxima con sumas. La regla del {{gl:trapecio|trapecio}} usa trapecios, la de {{gl:simpson|Simpson}} usa parábolas y la cuadratura de {{gl:gauss|Gauss}} escoge los puntos de la mejor manera. Cada método tiene un {{gl:orden|orden}}, que dice qué tan rápido baja el error al achicar el paso.")),
 sec("Un ejemplo","Un ejemplo",P("Se aproxima el área bajo x al cuadrado entre 0 y 2 con n trapecios. Mueve n y mira cómo se acerca al valor exacto."),EQ("T_{n}=\\dfrac{h}{2}\\left(f_{0}+2f_{1}+\\cdots+2f_{n-1}+f_{n}\\right),\\quad h=\\dfrac{b-a}{n}"),{"t":"grafica","animar":"dibujar","alt":"Los trapecios bajo la curva"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con un trapecio entre 0 y 2, el área es la base 2 por el promedio de las alturas 0 y 4. ¿Cuánto vale?","opciones":[2,3,4,8],"correcta":4,"bien":"Muy bien. Es 2 por 2, o sea 4. Más abajo se ve que mejora con más trapecios.","mal":"Es 4, porque el promedio de 0 y 4 es 2, y 2 por 2 es 4. Más abajo se ve que mejora con más trapecios."}),
 sec("Más trapecios","Más trapecios",P("Mira la aproximación con 1, 2, 4 y 8 trapecios."),{"t":"acercando","ds":[1,2,4,8],"alt":"Los trapecios para cuatro valores de n"},P("Los valores son 4, 3, 2.75 y 2.6875. Se acercan al valor exacto, 2.6667.")),
 sec("Trapecio y Simpson","Las reglas",P("Cada regla tiene su fórmula y su orden de error."),
   PASOS([("\\displaystyle\\int_{0}^{2}x\\,dx\\approx\\dfrac{2}{2}(0+2)=2","El trapecio simple es exacto con funciones lineales."),
          ("S=\\dfrac{h}{3}\\left(f_{0}+4f_{1}+f_{2}\\right),\\ h=1:\\ \\dfrac{1}{3}(0+4+4)=\\dfrac{8}{3}","Simpson simple, con la parábola por tres puntos. Da el valor exacto de x al cuadrado."),
          ("\\text{trapecio compuesto: error}\\ O(h^{2})","Al reducir h a la mitad, el error baja a la cuarta parte."),
          ("\\text{Simpson compuesto: error}\\ O(h^{4})","Baja a la dieciseisava parte, y es exacto hasta grado 3.")])),
 sec("Gauss-Legendre","Gauss",P("Si se escogen bien los nodos, se obtiene más con menos evaluaciones."),
   PASOS([("\\displaystyle\\int_{-1}^{1}f(x)\\,dx\\approx f\\left(-\\dfrac{1}{\\sqrt{3}}\\right)+f\\left(\\dfrac{1}{\\sqrt{3}}\\right)","Dos nodos y pesos iguales a 1."),
          ("f(x)=x^{2}:\\ \\dfrac13+\\dfrac13=\\dfrac23=0.6667","El resultado exacto de la integral de x al cuadrado entre menos 1 y 1."),
          ("n\\ \\text{nodos}\\ \\Rightarrow\\ \\text{exacto hasta grado}\\ 2n-1","Con 2 nodos, hasta grado 3.")]),
   OJO("Las reglas compuestas dividen el intervalo en partes y aplican la regla en cada una. Una regla de orden alto no ayuda si la función tiene saltos o puntas, y ahí conviene dividir en esas partes.")),
 eng("El trabajo de una fuerza medida","Se mide la fuerza que ejerce un resorte no lineal en tres posiciones, 0, 1 y 2 metros, y se obtienen 0, 100 y 400 newtons. El trabajo es la integral de la fuerza sobre la posición, y se estima con la regla del trapecio.","W=\\displaystyle\\int_{0}^{2}F\\,dx\\approx\\dfrac{1}{2}(0+2\\cdot100+400)=300\\ \\text{J}",
   [("Fuerza medida en 0, 1 y 2 m","0, 100 y 400 N"),("Trabajo con trapecios","300 J"),("Valor exacto si F igual a 100 x²","266.7 J")],"El trapecio sobreestima el trabajo, porque la fuerza es convexa y los trapecios quedan por encima. Con más mediciones se acercaría al valor real. Si se tuviera un punto en 0.5, 1 y 1.5 metros también, la regla de Simpson daría el valor exacto, porque la fuerza es un polinomio de grado 2."),
 completar("Se calcula la regla del trapecio con 2 subintervalos para x al cuadrado entre 0 y 2. Falta el resultado.","T_{2}=\\dfrac{1}{2}(0+2\\cdot1+4)=[[hueco]]",
   [("3","tres"),("6","seis"),("2","dos")],0,
   ["","Seis es la suma sin el factor un medio de h entre 2.","Dos sale de olvidar el término del extremo derecho, el 4."],"Se suman los términos y se multiplica por h entre 2.","0 más 2 más 4 es 6, y la mitad es 3."),
 error("Alguien calculó Simpson simple para x al cuadrado entre 0 y 2 y se equivocó en un paso. Toca el paso que está mal.",
   [("h=1,\\quad f_{0}=0,\\ f_{1}=1,\\ f_{2}=4","Los datos.","los valores de la función"),
    ("S=\\dfrac{h}{3}\\left(f_{0}+f_{1}+f_{2}\\right)=\\dfrac{5}{3}","Este paso es el que falla.","se suman los tres valores"),
    ("\\text{El resultado es}\\ 1.6667","Depende del paso anterior.","queda 1.6667")],1,
   "En la regla de Simpson el valor del centro se multiplica por 4. Queda un tercio de 0 más 4 por 1 más 4, o sea 8 sobre 3, que es el valor exacto.",
   "S=\\dfrac{1}{3}(0+4\\cdot1+4)=\\dfrac{8}{3}","Recuerda el factor del punto medio."),
 ordenar("Estos son los pasos para calcular el trapecio compuesto con n igual a 2 para x al cuadrado entre 0 y 2, pero están desordenados.",
   [("h=\\dfrac{b-a}{n}=1","Se calcula el paso"),
    ("f_{0}=0,\\ f_{1}=1,\\ f_{2}=4","Se evalúa la función en los nodos"),
    ("T=\\dfrac{h}{2}(f_{0}+2f_{1}+f_{2})","Se arma la fórmula"),
    ("T=3","Se calcula")],[2,0,3,1],
   "Se calcula el paso, se evalúa f en los nodos, se aplica la fórmula y se calcula.","Se empieza calculando el paso."),
]
S+=cierre("Mini simulacro de integración numérica",[
 banco("mn_c3_09","$\\dfrac{1}{3}(0+4\\cdot1+4)=2.6667$."),
 banco("mn_c3_10","El error del trapecio compuesto es de orden $h^2$."),
 banco("mn_c3_11","El error de Simpson compuesto es de orden $h^4$.")])
prac=[
 {"titulo":"Los trapecios","grafica":{"draw":1},"bloques":[P("n trapecios bajo la curva x al cuadrado."),EQ("\\displaystyle\\int_{0}^{2}x^{2}dx=\\dfrac{8}{3}")]},
 {"titulo":"Cambia n","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 1 a 8. Abajo se leen la aproximación y su error.")]},
 {"titulo":"Cuatro trapecios","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":4,"bloques":[EQ("T_{4}=2.75,\\quad \\text{error}=0.0833"),P("Con 4 trapecios el error baja a 0.0833.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":4},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El error es proporcional a uno entre n al cuadrado."}]}]
preg={"tex":"\\text{Con 4 trapecios, la aproximación de}\\ \\displaystyle\\int_{0}^{2}x^{2}dx\\ \\text{es}","opciones":["$2.75$","$3$","$2.6667$","$2.5$"],"correcta":0,
 "explicacion":"Con h igual a 0.5 y los valores 0, 0.25, 1, 2.25 y 4, la fórmula da 0.25 por (0 más 2 por 0.25 más 2 por 1 más 2 por 2.25 más 4), o sea 0.25 por 11, que es 2.75.",
 "verificacion":{"formula":"8/3+4/(3*16)+0*x","a":0,"esperado":2.75},
 "pistas":["h es 0.5.","Los valores de f son 0, 0.25, 1, 2.25 y 4.","Suma el primero, el último y el doble de los del medio, y multiplica por h entre 2."],
 "errores":["","Tres es el valor con 2 trapecios.","Ese es el valor exacto, y el trapecio con 4 trapecios no lo alcanza.","Es menor que el valor exacto, y el trapecio sobreestima en una función convexa."]}
res=["Las reglas de integración numérica aproximan el área con trapecios, parábolas o nodos de Gauss.","El trapecio compuesto tiene error de orden h al cuadrado, y Simpson compuesto de orden h a la cuarta.","Simpson integra exactamente los polinomios hasta grado 3, y Gauss con n nodos hasta grado 2n menos 1."]
write(lesson("mn-m3-l1","Lección 1 de 4","Integración numérica",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-integracion.json")
