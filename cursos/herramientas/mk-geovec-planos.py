import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 3 Rectas, planos y cónicas"
graf={"tipo":"plano","x":[-7.7,7.7],"y":[-3.2,5.2],"a":-4,"b":6,"inicio":0,
 "elementos":[
  {"t":"recta","p":["x/5","2*x/5"],"dir":["2","-1"],"c":0},
  {"t":"vector","a":["x/5","2*x/5"],"b":["x/5+1","2*x/5+2"],"nombre":"n","c":1},
  {"t":"vector","b":["1","2"],"nombre":"n","c":3},
  {"t":"segmento","a":["0","0"],"b":["x/5","2*x/5"],"guion":True,"c":2,"guia":True}],
 "lecturas":[{"rotulo":"valor d del plano x más 2y igual a d","formula":"x"},{"rotulo":"distancia del origen al plano","formula":"abs(x)/sqrt(5)"}],
 "etiquetas":["Valor que fija la posición del plano","Longitud del segmento perpendicular desde el origen"],"etiquetaSlider":"Valor d",
 "alt":"Un plano visto de canto, que aparece como una recta. El vector normal n igual a (1, 2) es perpendicular a ella. Al mover el deslizador la recta se desplaza sin girar, y el segmento punteado marca su distancia al origen"}
glos={"plano":"Un plano es el conjunto de puntos r que cumplen n punto r menos r0 igual a cero, donde n es un vector normal y r0 es un punto del plano.",
 "normal":"El vector normal de un plano es perpendicular a él. En la ecuación ax más by más cz igual a d, la normal es (a, b, c).",
 "paralelos":"Dos planos son paralelos si sus vectores normales son paralelos.",
 "general":"La ecuación general de un plano es ax más by más cz igual a d."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Visto de canto, un plano aparece como una recta. Su vector normal, (1, 2), es perpendicular a ella."],
 [4,9,"La ecuación es x más 2y igual a d. Al cambiar d, el plano se desplaza sin girar, y la normal no cambia."],
 [9,14,"Con d igual a 0, el plano pasa por el origen."],
 [14,19,"Con d igual a 5, la distancia del origen al plano es raíz de 5, o sea 2.24."],
 [19,22,"Dos planos con la misma normal son paralelos, y solo se diferencian en el valor de d."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,3],[9,0],[13,0],[14,5],[19,5],[22,5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[14,22]}}
S=[
 sec("La idea",None,P("Un {{gl:plano|plano}} del espacio se describe con un punto y un vector {{gl:normal|normal}}. Los puntos del plano son los que cumplen n punto r menos r0 igual a cero. Al desarrollar la cuenta sale la {{gl:general|ecuación general}} ax más by más cz igual a d, y los coeficientes son la normal. Dos planos son {{gl:paralelos|paralelos}} si sus normales lo son.")),
 sec("Un ejemplo","Un ejemplo",P("Un plano visto de canto es una recta. Mira cómo se mueve el plano x más 2y igual a d cuando cambia d, mientras la normal se mantiene."),EQ("\\mathbf{n}\\cdot(\\mathbf{r}-\\mathbf{r}_{0})=0\\ \\Longleftrightarrow\\ ax+by+cz=d"),{"t":"grafica","animar":"dibujar","alt":"Un plano visto de canto y su normal"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El plano x más 2y más 3z igual a 0 tiene como vector normal (1, 2, 3). ¿Pasa por el origen?","opciones":["Sí","No"],"correcta":"Sí","bien":"Muy bien. Con x, y y z iguales a cero la ecuación se cumple, así que pasa por el origen. Más abajo se ve con d igual a 0.","mal":"Sí pasa. Con x, y y z iguales a cero la ecuación da 0 igual a 0. Más abajo se ve con d igual a 0."}),
 sec("Moviendo el plano","Moviendo el plano",P("Mira el plano para d igual a 0, 3, 5 y menos 4."),{"t":"acercando","ds":[0,3,5,-4],"alt":"El plano en cuatro posiciones"},P("La normal es siempre la misma. Solo cambia la distancia del plano al origen.")),
 sec("Cómo se arma un plano","Cómo se arma",P("Con un punto y la normal se escribe la ecuación."),
   PASOS([("\\mathbf{n}=(1,2,3),\\ \\mathbf{r}_{0}=\\mathbf{0}\\ \\Rightarrow\\ x+2y+3z=0","Por el origen, no hay término independiente."),
          ("\\mathbf{n}=(1,0,0),\\ \\mathbf{r}_{0}=(1,2,3)\\ \\Rightarrow\\ x-1=0","El plano x igual a 1, paralelo al plano yz."),
          ("2(x-1)+(y-2)-(z-3)=0\\ \\Rightarrow\\ 2x+y-z=1","Con normal (2, 1, menos 1) y el punto (1, 2, 3)."),
          ("ax+by+cz=d\\ \\Rightarrow\\ \\mathbf{n}=(a,b,c)","De la ecuación se lee la normal.")])),
 sec("Paralelos y perpendiculares","Paralelos",P("La posición relativa de dos planos se lee en sus normales."),
   PASOS([("\\mathbf{n}_{1}\\parallel\\mathbf{n}_{2}\\ \\Leftrightarrow\\ \\text{planos paralelos}","Misma dirección de normales."),
          ("\\mathbf{n}_{1}\\cdot\\mathbf{n}_{2}=0\\ \\Leftrightarrow\\ \\text{planos perpendiculares}","Normales perpendiculares."),
          ("x+y+z=1\\ \\text{y}\\ 2x+2y+2z=7","Las normales (1, 1, 1) y (2, 2, 2) son paralelas, así que son planos paralelos.")]),
   OJO("Dos planos con la misma normal pueden ser el mismo plano o planos distintos. Hay que mirar también el término independiente.")),
 eng("El panel solar inclinado","Un panel solar plano se inclina 30 grados, y su normal unitaria es (0, 0.5, 0.866). Los rayos del sol llegan desde arriba, con dirección (0, 0, 1). La energía que recibe es proporcional al producto punto de la normal con la dirección del sol.","I=I_{0}\\,\\hat{\\mathbf{n}}\\cdot\\hat{\\mathbf{s}}=0.866\\,I_{0}",
   [("Normal del panel","(0, 0.5, 0.866)"),("Rayos del sol","(0, 0, 1)"),("Fracción de energía recibida","86.6 %")],"El panel recibe 86.6 por ciento de lo que recibiría uno horizontal con el sol a la vertical. Como el sol cambia de posición durante el día, el ángulo óptimo cambia, y por eso se estudia la normal del panel frente a la dirección del sol. Es un modelo geométrico que no incluye nubes, sombras ni reflejos."),
 completar("Se escribe el plano que pasa por el origen con vector normal (1, 2, 3). Falta el lado izquierdo.","[[hueco]]=0",
   [("x+2y+3z","x más 2y más 3z"),("3x+2y+z","3x más 2y más z"),("x+y+z","x más y más z")],0,
   ["","Los coeficientes están al revés. Deben coincidir con las componentes de la normal.","Esos coeficientes son todos 1, que corresponde a la normal (1, 1, 1)."],"Los coeficientes son las componentes de la normal.","La normal (1, 2, 3) da los coeficientes 1, 2 y 3."),
 error("Alguien halló el plano que pasa por (1, 2, 3) con normal (1, 0, 0) y se equivocó en un paso. Toca el paso que está mal.",
   [("\\mathbf{n}=(1,0,0),\\quad \\mathbf{r}_{0}=(1,2,3)","Los datos.","la normal y el punto"),
    ("\\mathbf{n}\\cdot(\\mathbf{r}-\\mathbf{r}_{0})=x-1=0","Se aplica la ecuación del plano.","queda x menos 1 igual a 0"),
    ("\\text{Entonces el plano es}\\ x=3","Este paso es el que falla.","el plano es x igual a 3")],2,
   "De x menos 1 igual a 0 se despeja x igual a 1, y no 3. El 3 es la tercera componente del punto, que no interviene porque la normal es (1, 0, 0).",
   "x-1=0\\ \\Rightarrow\\ x=1","Despeja x de la ecuación anterior."),
 ordenar("Estos son los pasos para hallar el plano que pasa por (1, 2, 3) con normal (2, 1, menos 1), pero están desordenados.",
   [("\\mathbf{n}\\cdot(\\mathbf{r}-\\mathbf{r}_{0})=0","Se parte de la ecuación vectorial"),
    ("2(x-1)+(y-2)-(z-3)=0","Se sustituye"),
    ("2x-2+y-2-z+3=0","Se expande"),
    ("2x+y-z=1","Se simplifica")],[2,0,3,1],
   "Se sustituye en la ecuación vectorial, se expande y se simplifica.","Se empieza con la ecuación del plano."),
]
S+=cierre("Mini simulacro de planos en el espacio",[
 banco("gv_c3_01","Con normal $(1,2,3)$ y por el origen, la ecuación es $x+2y+3z=0$."),
 banco("gv_c3_07","La ecuación vectorial del plano es $\\mathbf{n}\\cdot(\\mathbf{r}-\\mathbf{r}_0)=0$."),
 banco("gv_c3_08","La normal $(1,0,0)$ da $x-1=0$, o sea $x=1$.")])
prac=[
 {"titulo":"El plano de canto","grafica":{"draw":1},"bloques":[P("Un plano visto de canto, con su normal."),EQ("x+2y=d")]},
 {"titulo":"Mueve el plano","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el valor de d y la distancia del origen al plano.")]},
 {"titulo":"Por el origen","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0,"bloques":[EQ("d=0\\ \\Rightarrow\\ \\text{el plano pasa por el origen}"),P("Con d igual a 0 la distancia al origen es cero.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Los coeficientes de x, y y z son la normal."}]}]
preg={"tex":"\\text{Un vector normal al plano}\\ 2x-y+5z=7\\ \\text{es}","opciones":["$(2,-1,5)$","$(2,1,5)$","$(7,7,7)$","$(1,-2,5)$"],"correcta":0,
 "explicacion":"En la ecuación ax más by más cz igual a d, la normal es (a, b, c). Aquí los coeficientes son 2, menos 1 y 5, así que la normal es (2, menos 1, 5).",
 "verificacion":{"formula":"2+0*x","a":0,"esperado":2},
 "pistas":["Mira los coeficientes de x, y y z.","Son 2, menos 1 y 5.","Importa el signo de cada uno."],
 "errores":["","El signo del segundo coeficiente es negativo, y la normal lo conserva.","Siete es el término independiente, que no entra en la normal.","Los coeficientes se invirtieron y se cambiaron de signo."]}
res=["Un plano se describe con un punto y una normal, y su ecuación es n punto r menos r0 igual a cero.","En ax más by más cz igual a d, la normal es (a, b, c).","Dos planos son paralelos si sus normales lo son, y perpendiculares si el producto punto de las normales es cero."]
write(lesson("gv-m3-l1","Lección 1 de 4","Planos en el espacio",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-planos.json")
