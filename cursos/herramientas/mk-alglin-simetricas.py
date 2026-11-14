import os, math
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 3 Ortogonalidad y valores propios"
PTS=[]
for k in range(64):
    th=round(2*math.pi*k/64,6); th2=round(4*math.pi*k/64,6)
    PTS.append([f"cos({th})/sqrt(2+x*sin({th2}))",f"sin({th})/sqrt(2+x*sin({th2}))"])
graf={"tipo":"plano","x":[-5.5,7.33],"y":[-3,4],"a":0,"b":1.9,"inicio":1,
 "elementos":[
  {"t":"recta","p":["0","0"],"dir":["1","1"],"guion":True,"c":1},
  {"t":"recta","p":["0","0"],"dir":["1","-1"],"guion":True,"nombre":"eje mayor","c":3},
  {"t":"poligono","puntos":PTS,"c":2}],
 "lecturas":[{"rotulo":"valor propio mayor","formula":"2+x"},{"rotulo":"valor propio menor","formula":"2-x"}],
 "etiquetas":["Valor propio mayor","Valor propio menor"],"etiquetaSlider":"Valor de b en la matriz de filas (2, b) y (b, 2)",
 "alt":"La curva de nivel igual a 1 de la forma cuadrática de la matriz de filas (2, b) y (b, 2), una elipse que se alarga a lo largo del eje de valor propio menor al subir b"}
glos={"simetrica":"Una matriz simétrica es igual a su traspuesta, o sea que sus entradas son iguales a ambos lados de la diagonal.",
 "forma":"Una forma cuadrática es una expresión con todos los términos de grado dos, como 2x cuadrado más 2xy más 2y cuadrado. Se escribe como x traspuesto por A por x.",
 "definida":"Una forma cuadrática es definida positiva si vale más que cero para todo vector distinto de cero. Es definida negativa si vale menos que cero, e indefinida si toma valores de los dos signos.",
 "espectral":"El teorema espectral dice que una matriz simétrica real se diagonaliza con una matriz ortogonal y tiene valores propios reales."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"Esta es la curva de nivel 1 de una forma cuadrática. La matriz es simétrica, con 2 en la diagonal y b fuera."],
 [3,6,"La curva es una elipse. Sus ejes apuntan en las direcciones propias de la matriz, y esas son perpendiculares."],
 [6,12,"Al subir b, el valor propio mayor sube y el menor baja, y la elipse se alarga en la dirección del menor."],
 [12,17,"Con b igual a 1 los valores propios son 3 y 1. Los dos son positivos, así que la forma es definida positiva y la curva es cerrada."],
 [17,22,"Cuando b se acerca a 2, el valor propio menor se acerca a 0 y la elipse se estira sin límite."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,1],[9,0],[11,1.5],[12,1],[16,1],[17,1.9],[22,1.9]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("Las matrices {{gl:simetrica|simétricas}} son muy bien portadas. Sus valores propios son siempre números reales y sus vectores propios, para valores distintos, son perpendiculares. Eso dice el {{gl:espectral|teorema espectral}}. Aparecen en las {{gl:forma|formas cuadráticas}}, que describen energías, esfuerzos y curvaturas.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la curva donde una forma cuadrática vale 1, para la matriz simétrica que tiene 2 en la diagonal y b fuera de ella."),EQ("Q(x,y)=\\begin{pmatrix}x&y\\end{pmatrix}"+M(2,"b","b",2)+"\\begin{pmatrix}x\\\\y\\end{pmatrix}=2x^{2}+2b\\,xy+2y^{2}"),{"t":"grafica","animar":"dibujar","alt":"La elipse de nivel de la forma cuadrática"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Los valores propios de la matriz son 2 más b y 2 menos b. Con b igual a 1, ¿cuánto vale el mayor?","opciones":[1,2,3,4],"correcta":3,"bien":"Muy bien. Vale 3, y el menor es 1. Más abajo se ve la elipse.","mal":"Vale 3, porque 2 más 1 es 3, y el menor es 1. Más abajo se ve la elipse."}),
 sec("La elipse","La elipse",P("Mira cómo cambia la elipse al subir b."),{"t":"acercando","ds":[0,1,1.5,1.9],"alt":"La elipse para varios valores de b"},P("Cuando b sube, el valor propio menor baja y la elipse se alarga. Los ejes siempre son perpendiculares, en las direcciones (1, 1) y (1, menos 1).")),
 sec("Teorema espectral","Teorema espectral",P("Toda matriz simétrica real se diagonaliza con una matriz ortogonal, y sus valores propios son reales."),
   EQ("A=QDQ^{T}"),
   PASOS([("A="+M(2,1,1,2)+"\\ \\Rightarrow\\ \\lambda_{1}=3,\\ \\lambda_{2}=1","Los valores propios son reales."),
          ("\\mathbf{v}_{1}=(1,1),\\ \\mathbf{v}_{2}=(1,-1),\\quad \\mathbf{v}_{1}\\cdot\\mathbf{v}_{2}=0","Los vectores propios son perpendiculares."),
          ("Q=\\dfrac{1}{\\sqrt{2}}"+M(1,1,1,-1)+",\\quad D="+M(3,0,0,1),"Al normalizarlos, las columnas de Q son ortonormales, y A es Q D Q traspuesta.")])),
 sec("Formas cuadráticas","Formas cuadráticas",P("Una forma cuadrática es x traspuesto por A por x, con A simétrica. Al girar a la base de los vectores propios, queda como una suma de cuadrados con los valores propios de coeficientes."),
   PASOS([("Q(x,y)=2x^{2}+2xy+2y^{2}","Es la forma de la matriz con 2 en la diagonal y 1 fuera."),
          ("Q=3u^{2}+1v^{2}","En las coordenadas u, v de los ejes propios, solo quedan cuadrados."),
          ("Q(1,0)=2>0","Se evalúa en un vector para comprobar.")])),
 sec("Signo de la forma","Definida o no",P("El signo de la forma cuadrática lo deciden los valores propios."),
   PASOS([("\\lambda_{i}>0\\ \\text{para todo}\\ i\\ \\Rightarrow\\ \\text{definida positiva}","La forma es positiva en todo vector distinto de cero. Sus curvas de nivel son elipses."),
          ("\\lambda_{i}<0\\ \\text{para todo}\\ i\\ \\Rightarrow\\ \\text{definida negativa}","Es negativa en todo vector distinto de cero."),
          ("\\text{valores propios de signos opuestos}\\ \\Rightarrow\\ \\text{indefinida}","Sus curvas de nivel son hipérbolas."),
          ("A="+M(1,3,3,1)+"\\ \\Rightarrow\\ \\lambda=4,\\ -2\\ \\Rightarrow\\ \\text{indefinida}","Aunque la diagonal es positiva, hay un valor propio negativo.")]),
   OJO("El signo de los elementos de la diagonal no basta. Hay que mirar los valores propios, o los determinantes de las esquinas de la matriz.")),
 eng("Los esfuerzos principales de una pieza","En un punto de una pieza cargada, los esfuerzos forman una matriz simétrica. Sus valores propios son los esfuerzos principales, los máximos y mínimos, y sus vectores propios, perpendiculares, son las direcciones donde actúan. Es la base del círculo de Mohr.","\\sigma="+M(80,30,30,20)+"\\ \\text{MPa}",
   [("Esfuerzos","80 y 20 MPa, cortante 30 MPa"),("Esfuerzos principales","92.4 y 7.6 MPa"),("Dirección principal","22.5 grados")],"Los valores propios son 50 más y menos 30 por la raíz de 2, o sea 92.4 y 7.6 megapascales. Las direcciones principales son perpendiculares y la primera forma 22.5 grados con el eje x. Con ellos se revisa la resistencia de la pieza. Es un modelo simplificado, porque supone un estado plano de esfuerzos y un material uniforme."),
 completar("Una matriz simétrica de 2 por 2 tiene traza 4 y un valor propio igual a 3. Falta el otro.","\\lambda_{1}+\\lambda_{2}=\\operatorname{tr}A\\ \\Rightarrow\\ \\lambda_{2}=[[hueco]]",
   [("1","uno"),("3","tres"),("4","cuatro")],0,
   ["","Ese es el que ya se conoce. La suma debe dar la traza, 4, y 3 más 3 da 6.","Esa es la traza, y no el otro valor propio. Hay que restar el 3 conocido."],"Resta el valor propio conocido de la traza.","La suma de los valores propios es la traza, 4. Si uno es 3, el otro es 4 menos 3, o sea 1."),
 error("Alguien clasificó una forma cuadrática y se equivocó en un paso. Toca el primer paso donde aparece el error.",
   [("A="+M(1,3,3,1),"Es la matriz.","A tiene filas 1, 3 y 3, 1"),
    ("\\text{Los elementos de la diagonal son positivos, así que es definida positiva}","Este paso es el que falla.","Los elementos de la diagonal son positivos, así que es definida positiva"),
    ("\\text{Sus curvas de nivel son elipses}","Depende del paso anterior.","Sus curvas de nivel son elipses")],1,
   "La diagonal no decide. Los valores propios de A son 4 y menos 2, uno de cada signo, así que la forma es indefinida y sus curvas de nivel son hipérbolas. Por ejemplo, Q(1, menos 1) es 1 menos 6 más 1, o sea menos 4.",
   "\\lambda=4,\\ -2\\ \\Rightarrow\\ \\text{indefinida}","Evalúa la forma en el vector (1, menos 1)."),
 ordenar("Estos son los pasos para clasificar la forma cuadrática de la matriz de filas (1, 3) y (3, 1), pero están desordenados.",
   [("A="+M(1,3,3,1),"Se parte de la matriz"),
    ("\\det(A-\\lambda I)=(1-\\lambda)^{2}-9=0","Se plantea la ecuación característica"),
    ("\\lambda=4,\\quad \\lambda=-2","Se resuelve"),
    ("\\text{Un valor propio positivo y otro negativo}\\ \\Rightarrow\\ \\text{indefinida}","Se clasifica por los signos")],[2,0,3,1],
   "Se halla la ecuación característica, se resuelve y se mira el signo de los valores propios.","Se empieza con la matriz."),
]
S+=cierre("Mini simulacro de matrices simétricas",[
 banco("al_c3_04","Los valores propios son $3$ y $-1$, uno de cada signo."),
 banco("al_c3_16","Es el teorema espectral."),
 banco("al_c3_17","Una forma cuadrática es definida positiva si y solo si todos los valores propios de $A$ son positivos.")])
prac=[
 {"titulo":"La elipse","grafica":{"draw":1},"bloques":[P("Esta es la curva de nivel 1 de la forma cuadrática."),EQ("2x^{2}+2b\\,xy+2y^{2}=1")]},
 {"titulo":"Cambia b","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La elipse se alarga a medida que b sube. Abajo se ven los dos valores propios.")]},
 {"titulo":"Los ejes","grafica":{"draw":1},"laboratorio":True,"d":1,"bloques":[P("Con b igual a 1, los valores propios son 3 y 1. Los ejes de la elipse son perpendiculares y apuntan en las direcciones propias.")]},
 {"titulo":"Casi sin curvatura","grafica":{"draw":1},"laboratorio":True,"d":1.9,"bloques":[EQ("b\\to 2\\ \\Rightarrow\\ \\lambda_{2}=2-b\\to 0"),P("Con b cerca de 2, el valor propio menor casi es 0, y la elipse se estira mucho. Con b igual a 2 la forma deja de ser definida positiva.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"d":1.9},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Halla los valores propios y mira sus signos."}]}]
preg={"tex":"\\text{forma de}\\ "+M(5,2,2,2),"encabezado":"La forma cuadrática de la matriz de filas (5, 2) y (2, 2) es:","opciones":["definida positiva","indefinida","definida negativa","definida positiva solo si x es positivo"],"correcta":0,
 "explicacion":"La traza es 7 y el determinante es 5 por 2 menos 2 por 2, o sea 6. Los valores propios suman 7 y multiplican 6, así que son 6 y 1. Los dos son positivos, y la forma es definida positiva.",
 "pistas":["Mira la traza y el determinante de la matriz.","La traza es 7 y el determinante es 6. Los valores propios suman 7 y multiplican 6.","Los valores propios son 6 y 1. ¿Qué signos tienen?"],
 "errores":["","Una forma indefinida necesita valores propios de signos opuestos, pero aquí el determinante es positivo, así que tienen el mismo signo, y la traza positiva dice que ese signo es más.","Para ser definida negativa los valores propios serían negativos, pero su suma es la traza, que es 7.","El signo de una forma no depende de que x sea positivo. Se decide por los valores propios."]}
res=["Una matriz simétrica tiene valores propios reales y vectores propios perpendiculares, y se escribe A igual a Q D Q traspuesta.","Una forma cuadrática x traspuesto A x es definida positiva si y solo si todos los valores propios de A son positivos.","El signo de la diagonal no decide. Valores propios de signos opuestos dan una forma indefinida."]
write(lesson("alglin-m3-l4","Lección 4 de 4","Matrices simétricas y formas cuadráticas",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-simetricas.json")
