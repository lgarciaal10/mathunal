import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
from fundlib import *
MOD="Módulo 2 Sistemas lineales e interpolación"
J=[(0.0,0.0)]; G=[(0.0,0.0)]
for _ in range(6):
    x,y=J[-1]; J.append(((4+y)/5,(3+x)/4))
    x,y=G[-1]; xn=(4+y)/5; yn=(3+xn)/4; G.append((xn,yn))
def L(v): return "("+lagr([round(a,9) for a in v])+")"
EL=[{"t":"recta","p":["0.8","0"],"dir":["1","5"],"c":0},
    {"t":"recta","p":["-3","0"],"dir":["4","1"],"c":0},
    {"t":"punto","p":["1","1"],"c":3},
    {"t":"punto","p":[L([a for a,b in J]),L([b for a,b in J])],"c":1},
    {"t":"punto","p":[L([a for a,b in G]),L([b for a,b in G])],"c":2}]
eJ=[max(abs(a-1),abs(b-1)) for a,b in J]; eG=[max(abs(a-1),abs(b-1)) for a,b in G]
graf={"tipo":"plano","x":[-0.9,2.4],"y":[-0.3,1.5],"a":0,"b":6,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"error de Jacobi, la mayor diferencia con la solución","formula":L(eJ)},{"rotulo":"error de Gauss-Seidel, la mayor diferencia con la solución","formula":L(eG)}],
 "etiquetas":["Distancia máxima de la aproximación de Jacobi a la solución, que es el punto (1, 1)","Distancia máxima de la aproximación de Gauss-Seidel a la solución"],"etiquetaSlider":"Iteración, de 0 a 6",
 "alt":"Dos rectas que son las ecuaciones 5x menos y igual a 4 y menos x más 4y igual a 3. Se cruzan en la solución, el punto (1, 1), en verde. Un punto marcado con el método de Jacobi y otro con Gauss-Seidel parten de (0, 0) y se acercan a la solución, y el de Gauss-Seidel llega más rápido"}
glos={"jacobi":"En el método de Jacobi cada incógnita se calcula con los valores de la iteración anterior de todas las demás.",
 "seidel":"En Gauss-Seidel se usan los valores recién calculados dentro de la misma iteración, y por eso suele converger más rápido.",
 "dominante":"Una matriz es estrictamente diagonal dominante si, en cada fila, el valor absoluto del elemento de la diagonal es mayor que la suma de los valores absolutos de los demás.",
 "sor":"El método SOR agrega un parámetro omega que acelera Gauss-Seidel. Con omega igual a 1 coincide con él."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Las dos rectas son las ecuaciones del sistema, y se cruzan en la solución, el punto (1, 1)."],
 [4,9,"Los métodos iterativos parten de (0, 0) y se acercan paso a paso."],
 [9,14,"Jacobi usa solo los valores de la iteración anterior. Gauss-Seidel usa los que ya se actualizaron."],
 [14,19,"Gauss-Seidel se acerca más rápido, y su error baja antes."],
 [19,22,"La matriz es diagonal dominante, y por eso los dos métodos convergen desde cualquier punto de partida."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[7,1],[9,2],[12,3],[16,4],[19,5],[22,5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[14,22]}}
S=[
 sec("La idea",None,P("Para sistemas grandes se evita la eliminación directa y se usan métodos iterativos, que parten de una aproximación y la mejoran. El método de {{gl:jacobi|Jacobi}} actualiza todas las incógnitas con los valores anteriores. El de Gauss-{{gl:seidel|Seidel}} usa de inmediato los valores nuevos, y el {{gl:sor|SOR}} agrega un parámetro de aceleración. Convergen si la matriz es {{gl:dominante|diagonal dominante}}.")),
 sec("Un ejemplo","Un ejemplo",P("El sistema 5x menos y igual a 4 y menos x más 4y igual a 3 tiene solución (1, 1). Mira cómo se acercan los dos métodos desde (0, 0)."),EQ("\\begin{cases}5x-y=4\\\\-x+4y=3\\end{cases}"),{"t":"grafica","animar":"dibujar","alt":"Las rectas y los iterados de Jacobi y Gauss-Seidel"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En la matriz con filas (5, menos 1) y (menos 1, 4), el elemento de la diagonal de la primera fila es 5 y el otro es menos 1. ¿Es 5 mayor que el valor absoluto de menos 1?","opciones":["Sí","No"],"correcta":"Sí","bien":"Muy bien. 5 es mayor que 1, y en la segunda fila 4 es mayor que 1. La matriz es diagonal dominante. Más abajo se ve cómo se acercan los métodos.","mal":"Sí es mayor. 5 supera a 1, y en la segunda fila 4 supera a 1, así que la matriz es diagonal dominante. Más abajo se ve cómo se acercan los métodos."}),
 sec("Las iteraciones","Las iteraciones",P("Mira las aproximaciones en las iteraciones 0, 1, 2 y 4."),{"t":"acercando","ds":[0,1,2,4],"alt":"Los dos métodos en cuatro iteraciones"},P("En la iteración 4, Gauss-Seidel está más cerca de la solución que Jacobi.")),
 sec("Las fórmulas","Las fórmulas",P("Se despeja cada incógnita de su ecuación."),
   PASOS([("x^{(k+1)}=\\dfrac{4+y^{(k)}}{5},\\quad y^{(k+1)}=\\dfrac{3+x^{(k)}}{4}","Jacobi. Los dos lados usan solo valores de la iteración k."),
          ("x^{(k+1)}=\\dfrac{4+y^{(k)}}{5},\\quad y^{(k+1)}=\\dfrac{3+x^{(k+1)}}{4}","Gauss-Seidel. La y usa el x recién calculado."),
          ("(0,0)\\to(0.8,\\ 0.75)\\to(0.95,\\ 0.95)","Primeras iteraciones de Jacobi."),
          ("(0,0)\\to(0.8,\\ 0.95)\\to(0.99,\\ 0.9975)","Primeras iteraciones de Gauss-Seidel.")]),
   OJO("En Jacobi el orden de las incógnitas no importa. En Gauss-Seidel sí importa, porque cada una usa las anteriores ya actualizadas.")),
 sec("Cuándo convergen","Convergencia",P("La convergencia no es automática."),
   PASOS([("|a_{ii}|>\\sum_{j\\neq i}|a_{ij}|\\ \\Rightarrow\\ \\text{converge}","Si la matriz es estrictamente diagonal dominante, Jacobi y Gauss-Seidel convergen desde cualquier x0."),
          ("\\begin{pmatrix}5&-1\\\\-1&4\\end{pmatrix}:\\ 5>1,\\ 4>1","La matriz del ejemplo es diagonal dominante."),
          ("A\\ \\text{simétrica y definida positiva}\\ \\Rightarrow\\ \\text{Gauss-Seidel converge}","Otra condición que basta para Gauss-Seidel."),
          ("\\omega=1\\ \\Rightarrow\\ \\text{SOR}=\\text{Gauss-Seidel}","SOR con omega igual a 1.")]),
   OJO("Si la matriz no es diagonal dominante, el método puede converger o no. A veces conviene reordenar las ecuaciones para que la diagonal quede dominante.")),
 eng("Una red de resistencias","El voltaje en los nodos de una red de resistencias se obtiene de un sistema lineal. En una red grande, con miles de nodos, la matriz es casi toda ceros y diagonal dominante. Un método iterativo ahorra memoria y tiempo frente a la eliminación.","A\\mathbf{v}=\\mathbf{i}",
   [("Nodos","miles"),("Matriz","casi toda ceros y diagonal dominante"),("Método","Gauss-Seidel o SOR")],"En cada iteración solo se usan las conexiones de cada nodo, que son pocas, y el costo por iteración es proporcional al número de nodos. Se detiene cuando el cambio entre iteraciones es menor que la tolerancia. Mismos principios se usan en simulaciones de calor, de fluidos y de estructuras con elementos finitos."),
 completar("Se aplica Jacobi al sistema del ejemplo, desde (0, 0). Falta el valor de x en la iteración 1.","x^{(1)}=\\dfrac{4+0}{[[hueco]]}",
   [("5","cinco"),("4","cuatro"),("1","uno")],0,
   ["","Cuatro es el coeficiente de y en la segunda ecuación. La ecuación de x se divide entre su coeficiente, 5.","Con uno no se despeja x correctamente."],"Se divide entre el coeficiente de x en su ecuación.","La primera ecuación es 5x menos y igual a 4, y x vale 4 más y, entre 5."),
 error("Alguien decidió si una matriz es diagonal dominante y se equivocó en un paso. Toca el paso que está mal.",
   [("A=\\begin{pmatrix}5&-1\\\\-1&4\\end{pmatrix}","La matriz.","la matriz del ejemplo"),
    ("\\text{No, porque tiene entradas negativas}","Este paso es el que falla.","no es diagonal dominante por los negativos"),
    ("\\text{Entonces Jacobi no converge}","Depende del paso anterior.","por tanto Jacobi no converge")],1,
   "Se comparan valores absolutos, así que los signos no importan. Como 5 es mayor que 1 y 4 es mayor que 1, la matriz es diagonal dominante.",
   "|5|>|-1|\\ \\ \\text{y}\\ \\ |4|>|-1|","Toma los valores absolutos de los elementos."),
 ordenar("Estos son los pasos de una iteración de Gauss-Seidel para el sistema del ejemplo, pero están desordenados.",
   [("x^{(k+1)}=\\dfrac{4+y^{(k)}}{5}","Se calcula la nueva x con la y anterior"),
    ("y^{(k+1)}=\\dfrac{3+x^{(k+1)}}{4}","Se calcula la nueva y con la x recién calculada"),
    ("|x^{(k+1)}-x^{(k)}|<\\text{tol}","Se compara el cambio con la tolerancia"),
    ("\\text{se repite o se detiene}","Se decide si se continúa")],[2,0,3,1],
   "Se calcula x, luego y con el nuevo x, se compara el cambio y se decide si se repite.","Se empieza calculando la nueva x."),
]
S+=cierre("Mini simulacro de métodos iterativos",[
 banco("mn_c2_05","Una matriz estrictamente diagonal dominante garantiza la convergencia desde cualquier punto de partida."),
 banco("mn_c2_06","Se comparan valores absolutos, y $5>1$ y $4>1$."),
 banco("mn_c2_07","Gauss-Seidel usa de inmediato los valores recién calculados.")])
prac=[
 {"titulo":"Dos rectas","grafica":{"draw":1},"bloques":[P("Las ecuaciones del sistema se cruzan en la solución."),EQ("5x-y=4,\\quad -x+4y=3")]},
 {"titulo":"Itera","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 6. Abajo se leen los errores de Jacobi y de Gauss-Seidel.")]},
 {"titulo":"Iteración 4","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":4,"bloques":[EQ("\\text{error}_{GS}<\\text{error}_{J}"),P("En la iteración 4, Gauss-Seidel está más cerca de la solución.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":4},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Con omega igual a 1, SOR coincide con otro método."}]}]
preg={"tex":"\\text{El método SOR con}\\ \\omega=1\\ \\text{coincide con}","opciones":["Gauss-Seidel","Jacobi","la eliminación gaussiana","el método de Newton"],"correcta":0,
 "explicacion":"SOR agrega un factor omega a Gauss-Seidel. Con omega igual a 1 no hay aceleración, y se reduce exactamente a Gauss-Seidel.",
 "verificacion":{"formula":"1+0*x","a":0,"esperado":1},
 "pistas":["SOR es una variante de uno de los dos métodos.","El parámetro omega vale 1.","Sin aceleración, es el método base."],
 "errores":["","Jacobi no es la base de SOR. SOR parte de Gauss-Seidel.","La eliminación gaussiana es un método directo, y SOR es iterativo.","Newton resuelve ecuaciones no lineales, y SOR sistemas lineales."]}
res=["Jacobi usa los valores de la iteración anterior, y Gauss-Seidel usa los recién calculados.","Si la matriz es estrictamente diagonal dominante, los dos convergen desde cualquier punto de partida.","SOR con omega igual a 1 es Gauss-Seidel, y los métodos iterativos son útiles para sistemas grandes y casi vacíos."]
write(lesson("mn-m2-l2","Lección 2 de 4","Métodos iterativos",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-iterativos.json")
