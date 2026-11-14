import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 2 Vectores en el espacio"
graf={"tipo":"plano","x":[-1.5,6.0],"y":[-1.8,4.9],"a":-1,"b":4,"inicio":2,
 "elementos":[
  {"t":"poligono","puntos":[["0","0"],["2","0"],["3.5","x"],["1.5","x"]],"c":3},
  {"t":"segmento","a":["0","0"],"b":["2","0"],"c":0},
  {"t":"vector","b":["1.5","x"],"nombre":"w","c":1}],
 "lecturas":[{"rotulo":"volumen con signo, a punto b cruz c","formula":"4*x"},{"rotulo":"volumen del paralelepípedo","formula":"4*abs(x)"}],
 "etiquetas":["Triple producto escalar, que cambia de signo si w apunta hacia abajo","Volumen, siempre positivo"],"etiquetaSlider":"Altura de w sobre la base",
 "alt":"Vista lateral de un paralelepípedo. La base de área 4 está en el suelo y el vector w sube con una altura x. El volumen es 4 por x, y se hace cero cuando w queda en el plano de la base"}
glos={"triple":"El triple producto escalar de tres vectores es a punto b cruz c. Es un número, y equivale al determinante de tres por tres.",
 "volumen":"El volumen del paralelepípedo que forman tres vectores es el valor absoluto de su triple producto escalar.",
 "coplanares":"Tres vectores son coplanares si están en un mismo plano. Eso ocurre cuando su triple producto escalar es cero.",
 "base":"El volumen de un paralelepípedo es el área de la base por la altura."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Los vectores u y v forman la base, que tiene área 4. El vector w es la tercera arista y sube con una altura x."],
 [4,9,"El volumen es el área de la base por la altura. Aquí la base vale 4, así que el volumen es 4 por x."],
 [9,13,"Con x igual a 2, el volumen es 8, como el de un cubo de lado 2."],
 [13,18,"Con x igual a 0, w queda en el plano de la base, el volumen es cero y los tres vectores son coplanares."],
 [18,22,"Si w apunta hacia abajo, el triple producto es negativo, pero el volumen es su valor absoluto."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,3],[9,2],[12,2],[13,0],[17,0],[18,-1],[22,-1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[13,22]}}
S=[
 sec("La idea",None,P("Tres vectores del espacio forman un paralelepípedo. Su {{gl:volumen|volumen}} se obtiene con el {{gl:triple|triple producto escalar}}, que combina el producto vectorial y el producto punto. Si el resultado es cero, los vectores son {{gl:coplanares|coplanares}} y el sólido se aplasta. En el fondo es la fórmula de {{gl:base|base por altura}}.")),
 sec("Un ejemplo","Un ejemplo",P("En esta vista lateral, la base del paralelepípedo tiene área 4 y el vector w sube con altura x. Al mover x cambia el volumen."),EQ("V=\\left|\\mathbf{a}\\cdot(\\mathbf{b}\\times\\mathbf{c})\\right|=\\text{área de la base}\\times\\text{altura}"),{"t":"grafica","animar":"dibujar","alt":"Vista lateral del paralelepípedo"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La base tiene área 4 y la altura es 2. ¿Cuánto vale el volumen del paralelepípedo?","opciones":[2,4,6,8],"correcta":8,"bien":"Muy bien. Es base por altura, o sea 8. Más abajo se ve cómo cambia con la altura.","mal":"Es base por altura, 4 por 2, o sea 8. Más abajo se ve cómo cambia con la altura."}),
 sec("Cambiando la altura","La altura",P("Mira el volumen con alturas de menos 1, 0, 2 y 4."),{"t":"acercando","ds":[-1,0,2,4],"alt":"El paralelepípedo con cuatro alturas"},P("Con altura 0 el volumen es cero. Con altura menos 1 el triple producto es menos 4, pero el volumen sigue siendo 4.")),
 sec("Cómo se calcula","Cómo se calcula",P("Primero se hace el producto vectorial y después el producto punto."),
   PASOS([("V=|\\mathbf{a}\\cdot(\\mathbf{b}\\times\\mathbf{c})|","La fórmula del volumen."),
          ("\\mathbf{a}=(2,0,0),\\ \\mathbf{b}=(0,2,0),\\ \\mathbf{c}=(0,0,2)","Una caja cúbica de lado 2."),
          ("\\mathbf{b}\\times\\mathbf{c}=(4,0,0),\\quad \\mathbf{a}\\cdot(4,0,0)=8","Se calcula el producto vectorial y luego el punto."),
          ("\\det\\begin{pmatrix}2&0&0\\\\0&2&0\\\\0&0&2\\end{pmatrix}=8","Es el mismo valor que el determinante de tres por tres.")])),
 sec("Vectores coplanares","Coplanares",P("Cuando el volumen es cero, los tres vectores están en el mismo plano."),
   PASOS([("\\mathbf{a}\\cdot(\\mathbf{b}\\times\\mathbf{c})=0\\ \\Leftrightarrow\\ \\mathbf{a},\\mathbf{b},\\mathbf{c}\\ \\text{coplanares}","El criterio de coplanaridad."),
          ("(1,0,0),\\ (0,1,0),\\ (1,1,0)","Los tres están en el plano z igual a 0."),
          ("\\mathbf{b}\\times\\mathbf{c}=(0,0,-1),\\quad \\mathbf{a}\\cdot(0,0,-1)=0","El triple producto es cero, y por tanto son coplanares.")]),
   OJO("Que el triple producto sea cero no significa que los vectores sean paralelos. Pueden ser tres vectores distintos de un mismo plano.")),
 eng("La celda unitaria de un cristal","Un cristal se describe con una celda formada por tres vectores a1, a2 y a3. El volumen de la celda es el valor absoluto del triple producto. Para una celda cúbica de arista 0.4 nanómetros, el volumen es 0.4 al cubo.","V=\\left|\\mathbf{a}_{1}\\cdot(\\mathbf{a}_{2}\\times\\mathbf{a}_{3})\\right|=0.064\\ \\text{nm}^{3}",
   [("Arista","0.4 nm"),("Celdas en un volumen dado","se cuentan con V"),("Volumen de la celda","0.064 nm³")],"Con el volumen de la celda y la masa de los átomos que contiene se calcula la densidad del material. Si el triple producto fuera cero, los tres vectores serían coplanares y no definirían un cristal tridimensional. Para celdas no cúbicas el triple producto sigue funcionando, y es la forma estándar de obtener su volumen."),
 completar("Se calcula el volumen de la caja de aristas (2, 0, 0), (0, 3, 0) y (0, 0, 4). Falta el resultado.","V=2\\cdot3\\cdot4=[[hueco]]",
   [("24","veinticuatro"),("9","nueve"),("12","doce")],0,
   ["","Nueve es la suma de las aristas. El volumen se obtiene multiplicando.","Doce es el producto de solo dos de las aristas, y falta la tercera."],"Se multiplican las tres aristas.","2 por 3 por 4 es 24."),
 error("Alguien analizó tres vectores y se equivocó en un paso. Toca el paso que está mal.",
   [("\\mathbf{b}\\times\\mathbf{c}=(0,0,-1)","Con b igual a (0, 1, 0) y c igual a (1, 1, 0).","el producto vectorial es este"),
    ("\\mathbf{a}\\cdot(0,0,-1)=0","Con a igual a (1, 0, 0).","el producto punto es cero"),
    ("\\text{Entonces forman una caja de volumen 1}","Este paso es el que falla.","queda una caja de volumen 1")],2,
   "Un triple producto igual a cero significa que el volumen es cero y que los vectores son coplanares. Aquí los tres están en el plano z igual a 0.",
   "V=0\\ \\Rightarrow\\ \\text{coplanares}","Recuerda qué indica un volumen cero."),
 ordenar("Estos son los pasos para calcular el volumen de la caja de aristas (2, 0, 0), (0, 2, 0) y (0, 0, 2), pero están desordenados.",
   [("\\mathbf{b}\\times\\mathbf{c}=(4,0,0)","Se calcula b cruz c"),
    ("\\mathbf{a}\\cdot(4,0,0)","Se hace el producto punto con a"),
    ("2\\cdot4=8","Se calcula"),
    ("V=|8|=8","Se toma el valor absoluto")],[2,0,3,1],
   "Se calcula el producto vectorial, se hace el producto punto con a y se toma el valor absoluto.","Se empieza con el producto vectorial."),
]
S+=cierre("Mini simulacro del triple producto escalar",[
 banco("gv_c2_15","El volumen es el valor absoluto del triple producto escalar."),
 banco("gv_c2_16","El volumen es el producto de las tres aristas, $1\\cdot2\\cdot3=6$."),
 banco("gv_c2_17","Un triple producto cero indica que los vectores son coplanares.")])
prac=[
 {"titulo":"La caja","grafica":{"draw":1},"bloques":[P("Una vista lateral del paralelepípedo, con base de área 4."),EQ("V=4\\,|x|")]},
 {"titulo":"Cambia la altura","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el triple producto con signo y el volumen.")]},
 {"titulo":"Vectores coplanares","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0,"bloques":[EQ("x=0\\ \\Rightarrow\\ V=0"),P("Con altura cero, w queda en el plano de la base y el volumen es cero.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Calcula el determinante de tres por tres con los vectores como filas."}]}]
preg={"tex":"\\text{Volumen, aristas}\\ (1,1,0),(0,1,1),(1,0,1)","opciones":["$2$","$0$","$3$","$1$"],"correcta":0,
 "explicacion":"El determinante de tres por tres es 1 por (1 por 1 menos 1 por 0) menos 1 por (0 por 1 menos 1 por 1) más 0, que da 1 más 1, o sea 2. El volumen es 2.",
 "verificacion":{"formula":"1*(1*1-1*0)-1*(0*1-1*1)+0*x","a":0,"esperado":2},
 "pistas":["Desarrolla el determinante por la primera fila.","Da 1 más 1.","El volumen es 2."],
 "errores":["","Cero indicaría vectores coplanares, y este determinante no se anula.","Tres no sale de un desarrollo correcto del determinante. Revisa los signos de los cofactores.","Uno es solo el primer término. Falta el segundo."]}
res=["El triple producto a punto b cruz c da el volumen con signo del paralelepípedo.","El volumen es su valor absoluto, y es igual al área de la base por la altura.","Si es cero, los tres vectores son coplanares."]
write(lesson("gv-m2-l2","Lección 2 de 4","Triple producto escalar y volumen",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-triple.json")
