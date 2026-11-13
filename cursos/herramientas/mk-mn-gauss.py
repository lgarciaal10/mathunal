import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
from fundlib import *
MOD="Módulo 2 Sistemas lineales e interpolación"
graf={"tipo":"plano","x":[-3.2,7.2],"y":[-2.2,3.5],"a":0,"b":3,"inicio":0,"elementos":[
 {"t":"recta","p":["2","1"],"dir":["-1","2"],"c":0},
 {"t":"recta","p":["2","1"],"dir":["-(3-x)","4-2*x"],"c":1},
 {"t":"punto","p":["2","1"],"c":3}],
 "lecturas":[{"rotulo":"coeficiente de x en la fila 2 después de restar m veces la fila 1","formula":"4-2*x"},{"rotulo":"coeficiente de y en la fila 2 después de restar","formula":"3-x"}],
 "etiquetas":["Es 4 menos 2 por m. Se anula con m igual a 2","Es 3 menos m. Con m igual a 2 vale 1"],"etiquetaSlider":"Multiplicador m, de 0 a 3",
 "alt":"Las rectas 2x más y igual a 5 en azul, y la segunda ecuación después de restarle m veces la primera, en marrón. Ambas pasan por la solución, el punto (2, 1). Con m igual a 2 la segunda ecuación queda horizontal, porque desaparece el término en x"}
glos={"eliminacion":"La eliminación gaussiana convierte un sistema en uno triangular restando múltiplos de unas filas a otras.",
 "multiplicador":"El multiplicador m21 es el cociente entre el elemento a eliminar y el pivote. Aquí es 4 entre 2, o sea 2.",
 "lu":"La factorización LU escribe A como L por U, con L triangular inferior con unos en la diagonal y U triangular superior. Guarda los multiplicadores en L.",
 "pivoteo":"El pivoteo parcial intercambia filas para que el pivote sea el de mayor valor absoluto de su columna. Evita multiplicadores grandes y errores de redondeo."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Hay dos ecuaciones, 2x más y igual a 5, y 4x más 3y igual a 11. Las rectas se cruzan en la solución, el punto (2, 1)."],
 [4,9,"Eliminar es restar m veces la fila 1 de la fila 2. La nueva fila 2 sigue pasando por la solución."],
 [9,14,"Con m igual a 2 el coeficiente de x desaparece, y la ecuación queda y igual a 1, una recta horizontal."],
 [14,19,"Ese m, igual a 2, es el multiplicador. Se guarda en L, y la matriz triangular que queda es U."],
 [19,22,"Con A igual a L por U, resolver sistemas se reduce a dos sustituciones sencillas."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[7,1],[9,2],[19,2],[22,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[9,22]}}
S=[
 sec("La idea",None,P("La {{gl:eliminacion|eliminación gaussiana}} resuelve un sistema lineal convirtiéndolo en uno triangular. Cada paso resta de una fila un múltiplo de otra, con un {{gl:multiplicador|multiplicador}}. Si se guardan los multiplicadores se obtiene la factorización {{gl:lu|LU}}, que permite resolver muchos sistemas con la misma matriz. Para evitar errores se usa el {{gl:pivoteo|pivoteo}} parcial.")),
 sec("Un ejemplo","Un ejemplo",P("El sistema 2x más y igual a 5, y 4x más 3y igual a 11. Mueve m y mira cómo cambia la segunda ecuación sin perder la solución."),EQ("R_{2}\\leftarrow R_{2}-m\\,R_{1},\\qquad m=\\dfrac{4}{2}=2"),{"t":"grafica","animar":"dibujar","alt":"Las rectas y la eliminación"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El elemento a eliminar es 4 y el pivote es 2. ¿Cuánto vale el multiplicador, que es 4 entre 2?","opciones":[1,2,3,4],"correcta":2,"bien":"Muy bien. Es 2. Más abajo se ve que con m igual a 2 desaparece el coeficiente de x.","mal":"Es 2, porque 4 entre 2 da 2. Más abajo se ve que con m igual a 2 desaparece el coeficiente de x."}),
 sec("Variando el multiplicador","El multiplicador",P("Mira la segunda ecuación con m igual a 0, 1, 2 y 3."),{"t":"acercando","ds":[0,1,2,3],"alt":"La segunda ecuación con cuatro valores de m"},P("Todas las rectas pasan por (2, 1). Con m igual a 2 la recta es horizontal, y es la fila de U.")),
 sec("La eliminación","La eliminación",P("Se eliminan las variables de abajo hacia arriba."),
   PASOS([("m_{21}=\\dfrac{4}{2}=2","El multiplicador."),
          ("R_{2}\\leftarrow R_{2}-2R_{1}:\\ (4-4,\\ 3-2,\\ 11-10)=(0,\\ 1,\\ 1)","La nueva fila 2."),
          ("U=\\begin{pmatrix}2&1\\\\0&1\\end{pmatrix},\\quad y=1,\\ x=2","El sistema triangular y su solución por sustitución hacia atrás."),
          ("L=\\begin{pmatrix}1&0\\\\2&1\\end{pmatrix}","L guarda el multiplicador, con unos en la diagonal.")])),
 sec("Resolver con LU","Con LU",P("Con A igual a LU se resuelve en dos pasos."),
   PASOS([("A=LU,\\quad A\\mathbf{x}=\\mathbf{b}\\ \\Rightarrow\\ L(U\\mathbf{x})=\\mathbf{b}","Se reemplaza A por el producto."),
          ("L\\mathbf{y}=\\mathbf{b}","Sustitución hacia adelante, porque L es triangular inferior."),
          ("U\\mathbf{x}=\\mathbf{y}","Sustitución hacia atrás, porque U es triangular superior."),
          ("\\varepsilon\\to0:\\ m_{21}=\\dfrac{1}{\\varepsilon}\\ \\text{sin pivoteo}","Un pivote pequeño da un multiplicador enorme y errores de redondeo.")]),
   OJO("El pivoteo parcial intercambia filas para que el pivote sea el de mayor valor absoluto de su columna. Así los multiplicadores nunca superan 1 en valor absoluto, y se controla el error.")),
 eng("Muchas cargas, una factorización","En el análisis de una armadura se resuelve A por x igual a b, donde b son las cargas. Si se quieren probar 200 combinaciones de cargas, se factoriza A una sola vez y para cada b solo se hacen las dos sustituciones, que son mucho más baratas.","A=LU,\\qquad L\\mathbf{y}=\\mathbf{b},\\quad U\\mathbf{x}=\\mathbf{y}",
   [("Combinaciones de carga","200"),("Factorizaciones","1"),("Pares de sustituciones","200")],"Factorizar cuesta del orden de n al cubo operaciones, mientras que cada par de sustituciones cuesta del orden de n al cuadrado. Para una matriz de 1000 por 1000, eso es unas mil veces menos trabajo por cada carga nueva. Por eso los programas de estructuras guardan la factorización y la reutilizan."),
 completar("Se calcula el multiplicador para eliminar el 4 usando el pivote 2.","m_{21}=\\dfrac{4}{[[hueco]]}",
   [("2","el pivote"),("4","el elemento a eliminar"),("1","uno")],0,
   ["","El elemento a eliminar va arriba, y el pivote abajo.","Con uno no se obtiene el multiplicador correcto."],"El multiplicador es el elemento entre el pivote.","4 entre 2 es 2."),
 error("Alguien hizo la eliminación del sistema del ejemplo y se equivocó en un paso. Toca el paso que está mal.",
   [("R_{2}\\leftarrow R_{2}-2R_{1}","La operación.","se resta 2 veces la fila 1"),
    ("(4-2\\cdot2,\\ \\ 3-2\\cdot1)=(0,\\ 1)","Los coeficientes de la nueva fila.","quedan 0 y 1"),
    ("U=\\begin{pmatrix}2&1\\\\0&3\\end{pmatrix}","Este paso es el que falla.","la segunda fila de U es 0, 3")],2,
   "La segunda fila de U es la que se calculó, (0, 1). El 3 es el valor original, antes de restar. Quedaría 3 menos 2, o sea 1.",
   "U=\\begin{pmatrix}2&1\\\\0&1\\end{pmatrix}","Usa la fila que se acaba de calcular."),
 ordenar("Estos son los pasos para resolver un sistema con la factorización LU, pero están desordenados.",
   [("A=LU","Se factoriza la matriz"),
    ("L\\mathbf{y}=\\mathbf{b}","Se resuelve hacia adelante"),
    ("U\\mathbf{x}=\\mathbf{y}","Se resuelve hacia atrás"),
    ("\\mathbf{x}","Se obtiene la solución")],[2,0,3,1],
   "Se factoriza, se resuelve L por y igual a b, y después U por x igual a y.","Se empieza factorizando la matriz."),
]
S+=cierre("Mini simulacro de eliminación gaussiana y factorización LU",[
 banco("mn_c2_01","El pivoteo parcial intercambia filas para que el pivote sea el mayor en valor absoluto de su columna."),
 banco("mn_c2_02","En Doolittle, $L$ es triangular inferior con unos en la diagonal."),
 banco("mn_c2_03","$m_{21}=4/2=2$.")])
prac=[
 {"titulo":"Dos ecuaciones","grafica":{"draw":1},"bloques":[P("Las dos rectas se cruzan en la solución, el punto (2, 1)."),EQ("2x+y=5,\\quad 4x+3y=11")]},
 {"titulo":"Mueve m","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 3. Abajo se leen los coeficientes de la nueva fila 2.")]},
 {"titulo":"Eliminar x","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("m=2\\ \\Rightarrow\\ (0,\\ 1\\mid1)"),P("Con m igual a 2 el coeficiente de x se anula, y la ecuación queda y igual a 1.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"L guarda los multiplicadores y tiene unos en la diagonal."}]}]
preg={"tex":"\\text{En la factorización de Doolittle, la diagonal de}\\ L\\ \\text{vale}","opciones":["$1$","$0$","la de $A$","$-1$"],"correcta":0,
 "explicacion":"En la factorización de Doolittle, L es triangular inferior con unos en la diagonal. Debajo de la diagonal guarda los multiplicadores de la eliminación.",
 "verificacion":{"formula":"1+0*x","a":0,"esperado":1},
 "pistas":["Piensa en la matriz L del ejemplo.","Tiene (1, 0) y (2, 1) como filas.","La diagonal son unos."],
 "errores":["","Un cero en la diagonal haría a L no invertible.","La diagonal de A está en U, y no en L.","Menos uno no es lo que se usa en la convención de Doolittle."]}
res=["La eliminación gaussiana resta múltiplos de filas, y el multiplicador es el elemento a eliminar entre el pivote.","A igual a LU guarda los multiplicadores en L, y se resuelve con dos sustituciones.","El pivoteo parcial evita multiplicadores grandes y errores de redondeo."]
write(lesson("mn-m2-l4","Lección 4 de 4","Eliminación gaussiana y factorización LU",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-gauss.json")
