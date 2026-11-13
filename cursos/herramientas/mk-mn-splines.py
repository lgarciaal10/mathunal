import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
from fundlib import *
MOD="Módulo 3 Ajuste, integración y ecuaciones diferenciales"
XS=[0,1,2,3]; YS=[0,1,0,1]
M=[0,-4,4,0]
def lin(t):
    i=min(int(t),2); f=t-i; return YS[i]*(1-f)+YS[i+1]*f
def cub(t):
    r=0
    for i in range(4):
        L=1
        for j in range(4):
            if j!=i: L*=(t-XS[j])/(XS[i]-XS[j])
        r+=YS[i]*L
    return r
def spl(t):
    i=min(int(t),2); a=XS[i+1]-t; b=t-XS[i]
    return M[i]*a**3/6+M[i+1]*b**3/6+(YS[i]-M[i]/6)*a+(YS[i+1]-M[i+1]/6)*b
TS=[round(0.1*k,1) for k in range(31)]
EL=[{"t":"trazo","puntos":[[str(t),"("+lagr([round(lin(t),9),round(cub(t),9),round(spl(t),9)])+")"] for t in TS],"c":0}]
for a,b in zip(XS,YS): EL.append({"t":"punto","p":[str(a),str(b)],"c":3})
mx=max(abs(cub(t)) for t in TS)
graf={"tipo":"plano","x":[-0.9,3.9],"y":[-1.5,2.0],"a":0,"b":2,"inicio":2,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"valor del interpolante en x igual a 1.5","formula":"("+lagr([round(lin(1.5),9),round(cub(1.5),9),round(spl(1.5),9)])+")"},{"rotulo":"salto de la derivada en el nodo x igual a 1","formula":"("+lagr([2,0,0])+")"}],
 "etiquetas":["Valor de la curva en la mitad entre dos nodos","Distancia entre la pendiente por la izquierda y por la derecha del nodo. Cero significa curva suave"],"etiquetaSlider":"Interpolante, 0 lineal, 1 cúbico global, 2 spline natural",
 "alt":"Cuatro puntos, (0, 0), (1, 1), (2, 0) y (3, 1), unidos por tres tipos de curvas. La lineal por tramos tiene esquinas. El polinomio cúbico global es suave pero se sale un poco entre los puntos. El spline cúbico natural es suave y se mantiene más cerca de los datos"}
glos={"spline":"Un spline cúbico interpolante es una curva formada por un polinomio cúbico en cada subintervalo, que pasa por los nodos y es suave en los empalmes.",
 "natural":"El spline cúbico natural impone que la segunda derivada valga cero en los dos extremos.",
 "c2":"Una función es de clase C dos si ella, su primera y su segunda derivada son continuas.",
 "nodos":"Los nodos son los puntos de datos por donde pasa la curva."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Hay cuatro puntos, (0, 0), (1, 1), (2, 0) y (3, 1). Se interpolan de tres maneras."],
 [4,9,"Con segmentos rectos la curva pasa por los puntos, pero tiene esquinas, o sea saltos en la derivada."],
 [9,15,"Un polinomio cúbico global es suave, pero se sale un poco entre los puntos, y con más puntos oscilaría mucho."],
 [15,20,"El spline cúbico usa un polinomio por tramo y es suave. La función, la primera y la segunda derivada son continuas."],
 [20,24,"El spline natural pide además que la segunda derivada sea cero en los extremos."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[7,0],[9,1],[12,1],[15,2],[24,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,24]}}
S=[
 sec("La idea",None,P("Para interpolar muchos puntos, un solo polinomio de grado alto oscila demasiado. Un {{gl:spline|spline}} cúbico usa un polinomio cúbico distinto en cada tramo entre {{gl:nodos|nodos}}, y los empalma de forma suave. La condición de suavidad es ser de clase {{gl:c2|C dos}}. El spline {{gl:natural|natural}} agrega que la segunda derivada se anule en los extremos.")),
 sec("Un ejemplo","Un ejemplo",P("Mira los cuatro puntos y las tres curvas que los interpolan. Cambia el tipo de curva con el deslizador."),EQ("S_{i}(x)=a_{i}+b_{i}(x-x_{i})+c_{i}(x-x_{i})^{2}+d_{i}(x-x_{i})^{3}"),{"t":"grafica","animar":"dibujar","alt":"Los tres interpolantes"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Se tienen 4 nodos. Un spline cúbico usa un polinomio por cada tramo entre nodos consecutivos. ¿Cuántos tramos hay?","opciones":[2,3,4,5],"correcta":3,"bien":"Muy bien. Son 3 tramos, uno menos que los nodos. Más abajo se ve el spline.","mal":"Son 3, porque entre 4 nodos hay 3 tramos. Más abajo se ve el spline."}),
 sec("Los tres interpolantes","Las curvas",P("Mira las tres curvas con el mismo conjunto de puntos."),{"t":"acercando","ds":[0,1,2],"alt":"Los tres interpolantes"},P("La lineal tiene esquinas, el polinomio global se sale un poco, y el spline se mantiene suave y cerca de los datos.")),
 sec("Cómo se arma","Cómo se arma",P("Con n tramos hay 4n coeficientes, y se imponen condiciones hasta fijarlos todos."),
   PASOS([("S_{i}(x_{i})=y_{i},\\quad S_{i}(x_{i+1})=y_{i+1}","Cada tramo pasa por sus dos nodos. Son 2n condiciones."),
          ("S_{i}'(x_{i+1})=S_{i+1}'(x_{i+1})","La primera derivada es continua en los nodos interiores."),
          ("S_{i}''(x_{i+1})=S_{i+1}''(x_{i+1})","La segunda derivada es continua. Con las anteriores son 4n menos 2 condiciones."),
          ("S''(x_{0})=S''(x_{n})=0","Las dos condiciones naturales completan las 4n.")]),
   OJO("Con 4 nodos hay 3 polinomios cúbicos, y no un solo polinomio de grado 3. Un solo polinomio por 4 puntos sí existe, pero tiene otras propiedades.")),
 sec("Ventajas del spline","Ventajas",P("Los splines se usan mucho porque se portan bien."),
   PASOS([("\\text{lineal por tramos: continua, derivada con saltos}","Es sencilla, pero con esquinas."),
          ("\\text{polinomio global: muy suave, puede oscilar}","Con muchos nodos aparece el fenómeno de Runge."),
          ("\\text{spline cúbico: }C^{2}\\text{ y sin oscilar}","Un buen equilibrio entre suavidad y cercanía a los datos.")]),
   OJO("Que un spline interpole significa que pasa exactamente por los puntos. Con datos ruidosos, a veces se prefiere un spline de suavizado, que no pasa por todos.")),
 eng("El perfil de una leva","Una leva debe mover un seguidor por varias posiciones, y la trayectoria debe ser suave para que no haya golpes. Si la posición es un spline cúbico, la aceleración, que es la segunda derivada, es continua y no hay saltos bruscos de fuerza.","S\\in C^{2}\\ \\Rightarrow\\ \\text{aceleración continua}",
   [("Puntos de paso","4"),("Polinomios cúbicos","3"),("Aceleración","continua")],"Con una curva lineal por tramos, la velocidad cambia de golpe en los nodos, y la aceleración sería infinita, lo que produce vibraciones. El spline cúbico evita eso. Para velocidades altas se pide más suavidad todavía, y se usan splines de mayor grado, con la derivada de la aceleración continua."),
 completar("Se cuentan los tramos de un spline. Con n más 1 nodos, hay cierta cantidad de polinomios cúbicos.","\\#\\text{cúbicos}=[[hueco]]",
   [("n","n"),("n+1","n más 1"),("1","uno")],0,
   ["","n más 1 es el número de nodos, y no el de tramos entre ellos.","Un solo cúbico sería el polinomio global, y no un spline."],"Hay un tramo entre cada par de nodos consecutivos.","Con n más 1 nodos hay n intervalos entre ellos."),
 error("Alguien escribió las condiciones de un spline cúbico natural y se equivocó en un paso. Toca el paso que está mal.",
   [("S\\in C^{2},\\quad S(x_{i})=y_{i}","Continuidad e interpolación.","clase C dos que interpola los datos"),
    ("S'(x_{0})=S'(x_{n})=0","Este paso es el que falla.","condiciones naturales con la primera derivada"),
    ("\\text{Con esto hay}\\ 4n\\ \\text{condiciones}","Se completa el sistema.","hay 4n condiciones")],1,
   "Las condiciones naturales son sobre la segunda derivada, que vale cero en los extremos. Pedir que la primera derivada se anule da otro tipo de spline, llamado sujeto.",
   "S''(x_{0})=S''(x_{n})=0","Recuerda de qué derivada habla la condición natural."),
 ordenar("Estos son los pasos para armar un spline cúbico natural, pero están desordenados.",
   [("\\text{un cúbico en cada subintervalo}","Se define un cúbico por tramo"),
    ("S(x_{i})=y_{i}","Se imponen los valores en los nodos"),
    ("S',\\ S''\\ \\text{continuas en los nodos}","Se imponen las continuidades"),
    ("S''(x_{0})=S''(x_{n})=0","Se agregan las condiciones naturales")],[2,0,3,1],
   "Se define un cúbico por tramo, se imponen los valores, las continuidades y las condiciones naturales.","Se empieza definiendo un cúbico por tramo."),
]
S+=cierre("Mini simulacro de splines",[
 banco("mn_c3_05","El spline natural impone que la segunda derivada se anule en los extremos."),
 banco("mn_c3_06","Hay un cúbico por cada subintervalo entre nodos, o sea, $n$ para $n+1$ nodos."),
 banco("mn_c3_07","Son continuas la función y las dos primeras derivadas.")])
prac=[
 {"titulo":"Cuatro puntos","grafica":{"draw":1},"bloques":[P("Cuatro puntos y tres formas de interpolarlos."),EQ("(0,0),\\ (1,1),\\ (2,0),\\ (3,1)")]},
 {"titulo":"Cambia la curva","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 2. Abajo se leen el valor en x igual a 1.5 y el salto de la derivada en el nodo 1.")]},
 {"titulo":"El spline","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("S\\in C^{2}\\ \\Rightarrow\\ \\text{salto de la derivada}=0"),P("El spline es suave en los nodos, y el salto de la derivada es cero.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Cuenta los tramos entre nodos consecutivos."}]}]
preg={"tex":"\\text{Un spline cúbico interpolante con 5 nodos está formado por}","opciones":["$4$ polinomios cúbicos","$5$ polinomios cúbicos","$1$ polinomio cúbico","$3$ polinomios cúbicos"],"correcta":0,
 "explicacion":"Con 5 nodos hay 4 tramos entre nodos consecutivos, y en cada uno hay un polinomio cúbico. Son 4 polinomios.",
 "verificacion":{"formula":"5-1+0*x","a":0,"esperado":4},
 "pistas":["Hay un polinomio por tramo.","Cuenta los tramos entre 5 nodos.","Son 4."],
 "errores":["","Cinco es el número de nodos, y no el de tramos.","Un solo polinomio cúbico sería la interpolación global, y no un spline.","Tres son los tramos con 4 nodos, y aquí hay 5."]}
res=["Un spline cúbico usa un polinomio cúbico por tramo y es de clase C dos en los nodos.","El spline natural pide que la segunda derivada valga cero en los extremos.","Un spline evita las oscilaciones de un polinomio de grado alto, y por eso se usa para curvas suaves."]
write(lesson("mn-m3-l4","Lección 4 de 4","Splines",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-splines.json")
print('max cubic',mx)
