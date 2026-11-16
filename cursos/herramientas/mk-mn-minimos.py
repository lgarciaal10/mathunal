import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
MOD="Módulo 3 Ajuste, integración y ecuaciones diferenciales"
PX=[0,1,2,3]; PY=[1,2,3,5]
xb=sum(PX)/4; yb=sum(PY)/4   # 1.5 y 2.75
b0="2.75-x*1.5"
EL=[{"t":"recta","p":["1.5","2.75"],"dir":["1","x"],"c":0}]
for a,b in zip(PX,PY):
    EL.append({"t":"segmento","a":[str(a),str(b)],"b":[str(a),f"2.75+x*({a}-1.5)"],"guion":True,"c":1,"guia":True})
    EL.append({"t":"punto","p":[str(a),str(b)],"c":2})
SXX=5.0; SXY=6.5; SYY=8.75
graf={"tipo":"plano","x":[-1.9,5.1],"y":[-0.9,6.2],"a":0,"b":2.2,"inicio":0.5,"elementos":EL,
 "lecturas":[{"rotulo":"pendiente m de la recta","formula":"x"},{"rotulo":"suma de los errores al cuadrado","formula":"8.75-2*x*6.5+x*x*5"}],
 "etiquetas":["Pendiente de la recta, que pasa por el centro de los datos","Es mínima con m igual a 1.3, el valor de mínimos cuadrados"],"etiquetaSlider":"Pendiente m, de 0 a 2.2",
 "alt":"Cuatro puntos de datos, (0, 1), (1, 2), (2, 3) y (3, 5), y una recta cuya pendiente se cambia con el deslizador. Segmentos punteados marcan los errores verticales entre cada punto y la recta. La suma de los cuadrados de esos errores es la menor posible con la pendiente 1.3"}
glos={"residuo":"El residuo de un punto es la diferencia vertical entre el dato y la recta. Es y de i menos m x de i menos b.",
 "minimos":"El ajuste por mínimos cuadrados elige la recta que hace mínima la suma de los cuadrados de los residuos.",
 "normales":"Las ecuaciones normales son el sistema lineal que dan las derivadas de la suma de cuadrados igualadas a cero.",
 "linealizar":"Linealizar es transformar un modelo no lineal en uno lineal con logaritmos, para ajustarlo por mínimos cuadrados lineales."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Hay cuatro datos y una recta. Cada segmento punteado es el error de un dato."],
 [4,10,"Con pendiente 0.5 los errores son grandes. La lectura de abajo suma sus cuadrados."],
 [10,16,"Al subir la pendiente, la suma de los cuadrados baja, hasta el mínimo, que ocurre con pendiente 1.3."],
 [16,20,"Si la pendiente sigue subiendo, la suma vuelve a crecer. Hay un único mejor valor."],
 [20,24,"Ese mejor valor se obtiene resolviendo las ecuaciones normales, sin probar valores."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.5],[8,0.5],[11,1.3],[14,1.3],[17,2.2],[19,2.2],[22,1.3],[24,1.3]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[10,16]}}
S=[
 sec("La idea",None,P("Cuando los datos tienen ruido, no conviene que la curva pase por todos los puntos. El ajuste por {{gl:minimos|mínimos cuadrados}} busca la recta que hace mínima la suma de los cuadrados de los {{gl:residuo|residuos}}. Los parámetros salen de las {{gl:normales|ecuaciones normales}}. Y los modelos exponenciales o potenciales se ajustan después de {{gl:linealizar|linealizarlos}} con logaritmos.")),
 sec("Un ejemplo","Un ejemplo",P("Estos cuatro datos no están en una recta. Mueve la pendiente y mira cómo cambia la suma de los cuadrados de los errores."),EQ("S(m,b)=\\sum_{i}\\big(y_{i}-(m\\,x_{i}+b)\\big)^{2}"),{"t":"grafica","animar":"dibujar","alt":"Los datos y la recta de ajuste"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Los puntos (0, 1), (1, 2) y (2, 3) están exactamente en la recta y igual a x más 1. ¿Cuánto vale la pendiente de la recta de mínimos cuadrados?","opciones":[0.5,1,1.5,2],"correcta":1,"bien":"Muy bien. Es 1, porque los puntos están en una recta y el error es cero. Más abajo se ve el caso con ruido.","mal":"Es 1, porque los tres puntos están en una recta de pendiente 1 y se puede ajustar sin error. Más abajo se ve el caso con ruido."}),
 sec("Variando la pendiente","La pendiente",P("Mira la recta con pendientes de 0.5, 1.3 y 2.2."),{"t":"acercando","ds":[0.5,1.3,2.2],"alt":"La recta con tres pendientes"},P("Con 1.3 la suma de los cuadrados es 0.3, la menor posible. Con 0.5 o con 2.2 es mucho mayor.")),
 sec("La recta de mínimos cuadrados","La recta",P("La pendiente óptima sale de los datos, sin tanteo."),
   PASOS([("m=\\dfrac{\\sum(x_{i}-\\bar{x})(y_{i}-\\bar{y})}{\\sum(x_{i}-\\bar{x})^{2}}=\\dfrac{6.5}{5}=1.3","La pendiente, con las medias x barra igual a 1.5 y y barra igual a 2.75."),
          ("b=\\bar{y}-m\\,\\bar{x}=2.75-1.3\\cdot1.5=0.8","El intercepto, porque la recta pasa por el punto de las medias."),
          ("S_{min}=8.75-\\dfrac{6.5^{2}}{5}=0.3","La suma mínima de los cuadrados de los errores."),
          ("(0,1),(1,2),(2,3):\\ m=1,\\ S=0","Con datos en una recta, la pendiente es exacta.")]),
   OJO("La recta pasa siempre por el punto formado por las medias de x y de y. Ese hecho permite buscar solo la pendiente.")),
 sec("Modelos no lineales","Linealizar",P("Algunos modelos se ajustan con una transformación."),
   PASOS([("y=Ce^{Dx}\\ \\Rightarrow\\ \\ln y=\\ln C+Dx","Con logaritmo de y contra x se obtiene una recta."),
          ("y=Cx^{D}\\ \\Rightarrow\\ \\ln y=\\ln C+D\\ln x","Con logaritmo de y contra logaritmo de x se obtiene una recta."),
          ("\\text{se ajusta la recta y se deshace el logaritmo}","El resultado se interpreta de nuevo en el modelo original.")]),
   OJO("Al linealizar se minimiza el error de los logaritmos, y no el de los datos originales. Los puntos con valores grandes pesan menos que en un ajuste directo.")),
 eng("La curva de calibración de un sensor","Un sensor se calibra con cuatro mediciones y se quiere una recta que lo relacione con el valor real. Las mediciones tienen ruido, así que la recta no pasa por todas. Se usa mínimos cuadrados para repartir el error de la mejor manera.","y\\approx1.3\\,x+0.8",
   [("Mediciones","4 puntos"),("Recta de ajuste","y igual a 1.3 x más 0.8"),("Suma de errores al cuadrado","0.3")],"Con esta recta se corrige cada lectura del sensor. Con más mediciones, el ruido se promedia y la recta es más confiable. Si los datos siguen una curva y no una recta, se prueba un polinomio o se linealiza el modelo. Conviene revisar los residuos, porque un patrón en ellos indica que el modelo no es adecuado."),
 completar("Se calcula el intercepto de la recta de ajuste. Falta el valor de y barra.","b=[[hueco]]-1.3\\cdot1.5",
   [("2.75","la media de las y"),("1.5","la media de las x"),("1.3","la pendiente")],0,
   ["","1.5 es la media de las x, y ya se multiplica por la pendiente.","1.3 es la pendiente, que ya aparece multiplicando."],"El intercepto es la media de y menos la pendiente por la media de x.","La media de las y es 2.75, y b da 2.75 menos 1.95, o sea 0.8."),
 error("Alguien eligió el cambio de variable para ajustar y igual a C por e elevado a D por x, y se equivocó en un paso. Toca el paso que está mal.",
   [("y=Ce^{Dx}","El modelo.","un modelo exponencial"),
    ("\\ln y=\\ln C+Dx","El logaritmo.","queda lineal en x"),
    ("\\text{Se ajusta}\\ \\ln y\\ \\text{contra}\\ \\ln x","Este paso es el que falla.","se grafica ln y contra ln x")],2,
   "La ecuación es lineal en x, y no en el logaritmo de x. Se ajusta el logaritmo de y contra x. El logaritmo de x se usa para el modelo potencial.",
   "\\ln y\\ \\text{contra}\\ x","Mira qué variable queda sola en la ecuación linealizada."),
 ordenar("Estos son los pasos para hallar la recta de mínimos cuadrados, pero están desordenados.",
   [("\\bar{x}=1.5,\\quad \\bar{y}=2.75","Se calculan las medias"),
    ("m=\\dfrac{S_{xy}}{S_{xx}}=\\dfrac{6.5}{5}=1.3","Se calcula la pendiente"),
    ("b=\\bar{y}-m\\bar{x}=0.8","Se calcula el intercepto"),
    ("y=1.3x+0.8","Se escribe la recta")],[2,0,3,1],
   "Se calculan las medias, la pendiente y el intercepto, y se escribe la recta.","Se empieza calculando las medias."),
]
S+=cierre("Mini simulacro de mínimos cuadrados y ajuste de curvas",[
 banco("mn_c3_01","Se minimiza la suma de los cuadrados de los residuos."),
 banco("mn_c3_03","$\\ln y=\\ln C+D\\ln x$ es lineal en $\\ln x$."),
 banco("mn_c3_04","Los puntos están en una recta de pendiente 1.")])
prac=[
 {"titulo":"Los datos","grafica":{"draw":1},"bloques":[P("Cuatro datos y una recta con pendiente variable."),EQ("S(m)=8.75-13\\,m+5\\,m^{2}")]},
 {"titulo":"Cambia m","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la pendiente y la suma de los errores al cuadrado.")]},
 {"titulo":"El mínimo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1.3,"bloques":[EQ("m=1.3\\ \\Rightarrow\\ S=0.3"),P("Con pendiente 1.3 la suma de los errores al cuadrado es la menor posible.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1.3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"En el modelo exponencial se grafica el logaritmo de y contra x."}]}]
preg={"tex":"\\text{Para ajustar}\\ y=Ce^{Dx}\\ \\text{por mínimos cuadrados lineales se grafica}","opciones":["$\\ln y$ contra $x$","$y$ contra $e^{x}$","$\\ln y$ contra $\\ln x$","$y^{2}$ contra $x$"],"correcta":0,
 "explicacion":"Al tomar logaritmo queda ln y igual a ln C más D por x, que es una recta en x. Se ajusta entonces ln y contra x, y la pendiente es D y el intercepto es ln C.",
 "verificacion":{"formula":"1+0*x","a":0,"esperado":1},
 "pistas":["Toma logaritmo natural en los dos lados.","Queda ln C más D por x.","Es lineal en x, no en ln x."],
 "errores":["","Con y contra e a la x no se obtiene una recta, porque el modelo no es lineal en e a la x.","Ese cambio sirve para el modelo potencial, y no para el exponencial.","Elevar al cuadrado no linealiza el modelo exponencial."]}
res=["El ajuste por mínimos cuadrados elige la recta con menor suma de los cuadrados de los residuos.","La recta pasa por el punto de las medias, con pendiente Sxy entre Sxx.","Los modelos exponencial y potencial se ajustan después de linealizarlos con logaritmos."]
write(lesson("mn-m3-l3","Lección 3 de 4","Mínimos cuadrados y ajuste de curvas",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-minimos.json")
