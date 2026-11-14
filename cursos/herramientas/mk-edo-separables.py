import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 1 EDO de primer orden"
EL=[]
for i in range(-8,9):
    for j in range(-3,4):
        x0=i*0.25; y0=j*0.3
        if abs(x0)<0.01 and False: pass
        m=-x0*y0; n=math.hypot(1,m); d=0.1
        EL.append({"t":"segmento","a":[f"{x0-d/n:.4f}",f"{y0-d*m/n:.4f}"],"b":[f"{x0+d/n:.4f}",f"{y0+d*m/n:.4f}"],"c":0})
EL=EL[::1]
TR=[[f"{-2.1+4.2*k/48:.4f}",f"x*exp(0-0.5*({-2.1+4.2*k/48:.4f})*({-2.1+4.2*k/48:.4f}))"] for k in range(49)]
EL+= [{"t":"trazo","puntos":TR,"c":2},{"t":"punto","p":["0","x"],"c":1,"nombre":"y(0) = C"}]
graf={"tipo":"plano","x":[-2.2,2.2],"y":[-1.2,1.2],"a":-1,"b":1,"inicio":0.8,"elementos":EL,
 "lecturas":[{"rotulo":"C","formula":"x"},{"rotulo":"y(1)","formula":"x*exp(-0.5)"}],
 "etiquetas":["Condición inicial C","Valor de y en x igual a 1"],"etiquetaSlider":"Condición inicial y(0)",
 "alt":"El campo de pendientes de la ecuación y prima igual a menos x por y, con segmentos cortos, y la curva solución que pasa por el punto de altura C sobre el eje y"}
glos={"edo":"Una ecuación diferencial ordinaria, o EDO, es una ecuación que relaciona una función con sus derivadas. Su solución es una función, no un número.",
 "separable":"Una EDO es de variables separables si se puede escribir como dy sobre dx igual a g de x por h de y, de modo que cada variable quede de un lado.",
 "pvi":"Un problema de valor inicial es una EDO junto con el valor de la solución en un punto, como y de 0 igual a 3. Con él se escoge una sola solución de la familia.",
 "campo":"El campo de pendientes dibuja en cada punto un segmento corto con la pendiente que la EDO exige ahí. Las soluciones son curvas que siguen esos segmentos."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación y prima igual a menos x por y dice qué pendiente debe tener la solución en cada punto. Los segmentos cortos muestran esas pendientes."],
 [4,8,"Una solución es una curva que sigue los segmentos, como un bote que sigue una corriente."],
 [8,14,"Al cambiar la condición inicial C, la curva cambia, pero todas tienen la misma forma de campana, porque la solución es C por e a la menos x cuadrado sobre 2."],
 [14,18,"La condición inicial y de 0 igual a C escoge una sola curva de toda la familia."],
 [18,22,"Con C igual a 0.8 la solución vale 0.49 en x igual a 1."]],
 "canales":{"draw":[[0.3,0],[7.5,1]],"d":[[8,0.8],[10,-0.8],[12,1],[14,0.8],[22,0.8]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Una {{gl:edo|ecuación diferencial}} es una ecuación cuya incógnita es una función y que trae sus derivadas. Describen cómo cambian las cosas, como la temperatura de un motor, la carga de un condensador o la altura de un líquido. Las de {{gl:separable|variables separables}} son las más sencillas, porque se resuelven separando las variables e integrando cada lado.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la ecuación diferencial siguiente. En cada punto del plano dice qué pendiente debe tener la solución."),EQ("\\dfrac{dy}{dx}=-x\\,y"),P("La gráfica dibuja el {{gl:campo|campo de pendientes}} con segmentos cortos y una curva solución."),{"t":"grafica","animar":"dibujar","alt":"El campo de pendientes y una solución"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En el punto (1, 1) la pendiente que pide la ecuación es menos x por y. ¿Cuánto vale?","opciones":[-1,0,1,2],"correcta":-1,"bien":"Muy bien. Vale menos 1, así que la solución baja ahí. Más abajo se ve el campo.","mal":"Vale menos 1, porque menos 1 por 1 es menos 1. Más abajo se ve el campo."}),
 sec("Seguir las pendientes","Seguir",P("Mira cómo cambia la solución al cambiar su condición inicial."),{"t":"acercando","ds":[-0.8,0.3,0.8,1],"alt":"La curva solución para varios valores iniciales"},P("Todas las soluciones tienen la misma forma. Cambiar la condición inicial solo las estira o las encoge en vertical, porque multiplica por la constante.")),
 sec("Separar las variables","Separar",P("Se pasan todas las y a un lado, con dy, y todas las x al otro, con dx. Luego se integra cada lado."),
   PASOS([("\\dfrac{dy}{dx}=-x\\,y\\ \\Rightarrow\\ \\dfrac{dy}{y}=-x\\,dx","Se divide entre y y se multiplica por dx."),
          ("\\ln|y|=-\\dfrac{x^{2}}{2}+c","Se integra cada lado."),
          ("y=C\\,e^{-x^{2}/2}","Se aplica la exponencial. La constante positiva e a la c y el signo se juntan en una constante C."),
          ("y(0)=3\\ \\Rightarrow\\ C=3","La condición inicial fija C.")]),
   OJO("Al dividir entre y se pierde la solución y igual a 0. Aquí no se pierde, porque sale cuando C vale 0.")),
 sec("Con una condición inicial","Con condición inicial",P("Un {{gl:pvi|problema de valor inicial}} agrega el valor de la solución en un punto. Eso escoge una curva de la familia."),
   PASOS([("y'=3y,\\quad y(0)=2","La ecuación y la condición inicial."),
          ("\\dfrac{dy}{y}=3\\,dx\\ \\Rightarrow\\ \\ln|y|=3x+c\\ \\Rightarrow\\ y=Ce^{3x}","Se separa e integra."),
          ("y(0)=C=2\\ \\Rightarrow\\ y=2e^{3x}","Se reemplaza la condición inicial.")])),
 sec("Qué es una solución","Solución",P("Una solución se comprueba reemplazándola en la ecuación."),
   PASOS([("y=Ce^{-x^{2}/2}\\ \\Rightarrow\\ y'=Ce^{-x^{2}/2}\\cdot(-x)=-x\\,y","Se deriva con la regla de la cadena y se compara."),
          ("\\text{Orden de}\\ y''+(y')^{3}+y=0\\ \\text{es 2}","El orden es la derivada más alta que aparece.")])),
 eng("El enfriamiento de un motor","Un bloque de motor se enfría al apagarlo. La ley de enfriamiento de Newton dice que la temperatura baja a una velocidad proporcional a la diferencia con el ambiente. Es una ecuación de variables separables.","\\dfrac{dT}{dt}=-k\\,(T-T_{a})",
   [("Temperatura inicial","90 °C"),("Temperatura ambiente","20 °C"),("Constante k","0.05 por minuto")],"Al separar e integrar queda T igual a 20 más 70 por e a la menos 0.05 t. A los 30 minutos la temperatura es 20 más 70 por e a la menos 1.5, o sea unos 35.6 grados. Es un modelo simplificado, porque supone un ambiente a temperatura constante y una temperatura uniforme en el bloque."),
 completar("Se separan las variables en la ecuación y prima igual a menos x por y. Falta el lado de las x.","\\dfrac{dy}{y}=[[hueco]]\\,dx",
   [("-x","menos x"),("x","x"),("-\\dfrac{1}{x}","menos uno sobre x")],0,
   ["","Falta el signo menos. La ecuación es y prima igual a menos x por y.","Al dividir entre y no aparece 1 sobre x. Queda menos x por dx."],"Divide los dos lados entre y.","Al dividir entre y, queda dy sobre y igual a menos x por dx."),
 error("Alguien resolvió una ecuación de variables separables y se equivocó en un paso. Toca el paso que está mal.",
   [("\\dfrac{dy}{y}=-x\\,dx","La separación está bien.","dy sobre y es menos x por dx"),
    ("\\ln|y|=-\\dfrac{x^{2}}{2}+c","La integración está bien.","El logaritmo de y es menos x al cuadrado sobre 2 más c"),
    ("y=-\\dfrac{x^{2}}{2}+c","Este paso es el que falla.","Entonces y es menos x al cuadrado sobre 2 más c")],2,
   "Falta aplicar la exponencial a los dos lados. Del logaritmo de y se pasa a y con e elevado a lo del otro lado, y la solución es y igual a C por e a la menos x cuadrado sobre 2.",
   "y=Ce^{-x^{2}/2}","Para quitar el logaritmo hay que aplicar la exponencial."),
 ordenar("Estos son los pasos para resolver y prima igual a 3y con y de 0 igual a 2, pero están desordenados.",
   [("\\dfrac{dy}{y}=3\\,dx","Se separan las variables"),
    ("\\ln|y|=3x+c","Se integra"),
    ("y=Ce^{3x}","Se aplica la exponencial"),
    ("y(0)=2\\ \\Rightarrow\\ y=2e^{3x}","Se usa la condición inicial")],[2,0,3,1],
   "Se separa, se integra, se aplica la exponencial y se usa la condición inicial para hallar C.","Primero se separan las variables."),
]
S+=cierre("Mini simulacro de variables separables",[banco("ed_c1_01","Se separa $\\frac{dy}{y}=2x\\,dx$, se integra $\\ln|y|=x^2+c$ y queda $y=Ce^{x^2}$."),banco("ed_c1_06","Se separa $y\\,dy=x\\,dx$ y se integra para obtener $\\frac{y^2}{2}=\\frac{x^2}{2}+c$."),banco("ed_c1_07","La solución es $y=e^{2x}$ y vale $e^2\\approx 7.3891$ en $x=1$.")])
prac=[
 {"titulo":"El campo","grafica":{"draw":1},"bloques":[P("Los segmentos son las pendientes que pide la ecuación."),EQ("y'=-x\\,y")]},
 {"titulo":"Cambia y(0)","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La curva solución cambia con la condición inicial y siempre sigue los segmentos. Abajo se ven C y el valor de y en x igual a 1.")]},
 {"titulo":"Una condición inicial","grafica":{"draw":1,"ok":True},"laboratorio":True,"d":0.8,"bloques":[EQ("y(0)=0.8\\ \\Rightarrow\\ y=0.8\\,e^{-x^{2}/2},\\quad y(1)=0.49"),P("La solución pasa por el punto marcado en el eje y.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"ok":True,"d":0.8},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Separa, integra y usa la condición inicial."}]}]
preg={"tex":"y'=-2xy,\\ y(0)=3\\ \\Rightarrow\\ y(1)","opciones":["$1.104$","$3$","$0.405$","$8.155$"],"correcta":0,
 "explicacion":"Se separa dy sobre y igual a menos 2x dx y se integra, ln de y igual a menos x al cuadrado más c. La solución es y igual a C por e a la menos x al cuadrado, y con y de 0 igual a 3 queda C igual a 3. En x igual a 1 vale 3 por e a la menos 1, o sea 1.104.",
 "verificacion":{"formula":"3*exp(0-1)+0*x","a":0,"esperado":1.1036},
 "pistas":["Separa las variables, dy sobre y igual a menos 2x dx.","La solución es C por e a la menos x al cuadrado. Usa y de 0 igual a 3.","Evalúa 3 por e a la menos x al cuadrado en x igual a 1."],
 "errores":["","Ese es el valor inicial. La solución cambia con x.","Revisa la cuenta. 3 por e a la menos 1 es 3 por 0.368.","Con exponente positivo la solución crecería, pero la ecuación tiene un signo menos y la solución decae."]}
res=["Una EDO de variables separables se escribe con cada variable de un lado y se integra.","La solución general trae una constante, y la condición inicial la fija.","El campo de pendientes muestra qué forma tienen las soluciones antes de resolver."]
write(lesson("edo-m1-l1","Lección 1 de 6","Variables separables",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Ecuaciones Diferenciales"),"edo-separables.json")
