import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 2 Demostración y conjuntos"
EL=[]
for i in range(1,7):
    for ind_vals,col in (([1 if n>=i else 0 for n in range(7)],3),([1 if n==i else 0 for n in range(7)],2)):
        ind=lagr(ind_vals)
        xr=f"{i}*({ind})"; ylo=f"{i-1}*({ind})+x*(1-({ind}))"; yhi=f"{i}*({ind})+x*(1-({ind}))"
        EL.append({"t":"poligono","puntos":[["0",ylo],[xr,ylo],[xr,yhi],["0",yhi]],"c":col})
graf={"tipo":"plano","x":[-3.4,9.8],"y":[-0.6,6.6],"a":0,"b":6,"inicio":0,"entero":True,"sinejes":True,"elementos":EL,
 "lecturas":[{"rotulo":"cuadros de la escalera con n filas","formula":"x*(x+1)/2"},{"rotulo":"cuadros nuevos al pasar de n a n más 1","formula":"x+1"}],
 "etiquetas":["Suma de 1 hasta n, igual a n por n más 1 entre 2","Tamaño de la fila nueva que se agrega"],"etiquetaSlider":"Número de filas n, de 0 a 6",
 "alt":"Una escalera de cuadros. La fila i tiene i cuadros. Al subir n se agrega una fila nueva, resaltada, con un cuadro más que la anterior. Con 6 filas hay 21 cuadros"}
glos={"base":"El caso base es el primer valor para el que se comprueba la afirmación, normalmente n igual a 1.",
 "hipotesis":"La hipótesis inductiva es el supuesto de que la afirmación vale para un valor m. No se prueba, se usa para el paso siguiente.",
 "paso":"El paso inductivo prueba que si la afirmación vale para m, entonces vale para m más 1.",
 "fuerte":"En la inducción fuerte la hipótesis supone que la afirmación vale para todos los casos desde el base hasta m, y no solo para m."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Cada fila de la escalera tiene un cuadro más que la anterior. Con n filas hay 1 más 2 y así hasta n cuadros."],
 [4,10,"Sube n de 0 a 6. Cuando n pasa de 3 a 4 se agrega una fila de 4 cuadros, que es la fila resaltada."],
 [10,16,"La lectura de abajo lo confirma. Al pasar de n a n más 1, se agregan n más 1 cuadros."],
 [16,20,"Esa es la idea de la inducción. Si la fórmula vale para n, al agregar la fila n más 1 también valdrá para n más 1."],
 [20,24,"Falta el primer escalón, el caso base. Con n igual a 1 hay un cuadro, y la fórmula da 1 por 2 entre 2, igual a 1."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[5,0],[6,1],[8,2],[9,3],[10,3],[11,4],[13,5],[15,6],[16,6],[20,1],[24,1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[20,24]}}
S=[
 sec("La idea",None,P("La inducción prueba que una afirmación vale para todos los enteros desde uno en adelante, como una fila de fichas de dominó. Primero se prueba el {{gl:base|caso base}}, que es empujar la primera ficha. Después se prueba el {{gl:paso|paso inductivo}}, que dice que cada ficha tumba a la siguiente. Para ese paso se usa la {{gl:hipotesis|hipótesis inductiva}}. Con las dos cosas, caen todas.")),
 sec("Un ejemplo","Un ejemplo",P("La escalera tiene n filas, y la fila i tiene i cuadros. El total de cuadros es la suma de los primeros n números."),EQ("1+2+\\cdots+n=\\dfrac{n(n+1)}{2}"),{"t":"grafica","animar":"dibujar","alt":"La escalera de cuadros"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En una fila de fichas de dominó cada ficha tumba a la siguiente. ¿Cuántas fichas hay que empujar a mano para que caigan todas?","opciones":[0,1,2,10],"correcta":1,"bien":"Muy bien. Basta empujar la primera. Esa es la idea del caso base y del paso inductivo.","mal":"Basta con una, la primera. Las demás caen solas porque cada una tumba a la siguiente."}),
 sec("Recorriendo la escalera","La escalera",P("Mira cuántos cuadros hay y cuántos se agregan cuando n vale 1, 3, 4 y 6."),{"t":"acercando","ds":[1,3,4,6],"alt":"La escalera con 1, 3, 4 y 6 filas"},P("Cada vez que n sube a un nuevo valor, se agrega una fila con ese nuevo valor de cuadros. Al pasar de m a m más 1, se agregan m más 1 cuadros. Esa fila nueva es lo que se usa en el paso inductivo.")),
 sec("La demostración","La demostración",P("Estos son los pasos para probar la fórmula de la suma de los primeros n números."),
   PASOS([("n=1:\\quad 1=\\dfrac{1\\cdot2}{2}","El caso base. Se comprueba el primer valor."),
          ("\\displaystyle\\sum_{k=1}^{m}k=\\dfrac{m(m+1)}{2}","La hipótesis inductiva. Se supone que vale para m."),
          ("\\displaystyle\\sum_{k=1}^{m+1}k=\\dfrac{m(m+1)}{2}+(m+1)","Se suma el término nuevo a los dos lados."),
          ("=\\dfrac{m(m+1)+2(m+1)}{2}=\\dfrac{(m+1)(m+2)}{2}","Se factoriza. Queda la misma fórmula, pero con m más 1.")]),
   OJO("Sin caso base la inducción no prueba nada. Con la hipótesis falsa de que todos los números son iguales a su siguiente, el paso inductivo se cumple, pero no hay un primer escalón.")),
 sec("Inducción fuerte","Fuerte",P("A veces para probar el caso m más 1 se necesitan varios casos anteriores, y no solo el último. Entonces se usa la inducción fuerte."),
   PASOS([("P(1)\\wedge P(2)\\wedge\\cdots\\wedge P(m)\\ \\Rightarrow\\ P(m+1)","La hipótesis incluye todos los casos desde el base hasta m."),
          ("\\text{Ejemplo, todo entero}\\ n\\ge2\\ \\text{es producto de primos}","Se parte n en dos factores menores, y cada uno ya es producto de primos por hipótesis.")]),
   OJO("La inducción débil y la fuerte prueban lo mismo. Se elige la que haga más cómodo el paso inductivo.")),
 eng("Los enlaces de una red","En una red de n computadores donde cada uno se conecta con todos los demás, hacen falta n por n menos 1 entre 2 enlaces. Se puede probar por inducción. Al agregar el computador número n más 1, se agregan n enlaces nuevos, uno por cada computador que ya estaba.","E(n)=\\dfrac{n(n-1)}{2}",
   [("Computadores","10"),("Enlaces","45"),("Al agregar uno más","10 enlaces nuevos")],"Con 10 computadores hay 45 enlaces. Al agregar el undécimo se suman 10, y da 55, que es 11 por 10 entre 2. El paso inductivo es justamente esa cuenta. Por eso la red completa se vuelve costosa, porque cada nodo nuevo agrega tantos enlaces como nodos había."),
 completar("Se pasa de m a m más 1 en la suma de los primeros términos. Falta el término que se agrega.","\\displaystyle\\sum_{k=1}^{m+1}k=\\sum_{k=1}^{m}k+[[hueco]]",
   [("m+1","m más 1"),("m","m"),("1","1")],0,
   ["","El término que se agrega es el de índice m más 1, y no el de índice m, que ya estaba en la suma.","Se agrega el último término, que vale m más 1 y no uno."],"El término nuevo es el de índice m más 1.","La suma hasta m más 1 es la suma hasta m más el término m más 1."),
 error("Alguien probó por inducción que la suma de los primeros n impares es n al cuadrado y se equivocó en un paso. Toca el paso que está mal.",
   [("n=1:\\quad 1=1^{2}","El caso base.","con n igual a 1 se cumple"),
    ("\\displaystyle\\sum_{k=1}^{m}(2k-1)=m^{2}","La hipótesis inductiva.","se supone para m"),
    ("\\displaystyle\\sum_{k=1}^{m+1}(2k-1)=m^{2}+(2m-1)","Este paso es el que falla.","se suma el término nuevo")],2,
   "El término nuevo es el de índice m más 1, y vale 2 por m más 1 menos 1, o sea 2m más 1. Sumar 2m menos 1 es repetir el término de índice m.",
   "m^{2}+(2m+1)=(m+1)^{2}","Calcula el término de índice m más 1."),
 ordenar("Estos son los pasos de una demostración por inducción, pero están desordenados.",
   [("n=1\\ \\text{se cumple}","Se verifica el caso base"),
    ("P(m)\\ \\text{se supone}","Se escribe la hipótesis inductiva"),
    ("P(m)\\Rightarrow P(m+1)","Se prueba el paso inductivo"),
    ("\\forall n\\ge1,\\ P(n)","Se concluye para todo n")],[2,0,3,1],
   "Se prueba el caso base, se supone la hipótesis, se prueba el paso y se concluye.","Se empieza por el primer escalón."),
]
S+=cierre("Mini simulacro de inducción matemática",[
 banco("fu_c2_06","El caso base es el primer valor, n igual a 1."),
 banco("fu_c2_07","Con la fórmula, 5 por 6 entre 2 da 15."),
 banco("fu_c2_08","La inducción fuerte supone todos los casos anteriores.")])
prac=[
 {"titulo":"La escalera","grafica":{"draw":1,"guide":1},"bloques":[P("Una escalera de n filas, con i cuadros en la fila i."),EQ("1+2+\\cdots+n=\\dfrac{n(n+1)}{2}")]},
 {"titulo":"Recorre n","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 6. Abajo se lee el total de cuadros y la fila que se agrega.")]},
 {"titulo":"El paso inductivo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("T(3)=6,\\quad T(4)=6+4=10"),P("Con n igual a 3 se pasa a 4 agregando una fila de 4 cuadros.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Piensa qué prueba el paso inductivo y qué prueba el caso base."}]}]
preg={"tex":"\\text{El paso inductivo prueba que}","opciones":["si $P(m)$ es verdadera, entonces $P(m+1)$ es verdadera","$P(1)$ es verdadera","$P(m)$ es verdadera para todo $m$","$P(m+1)$ implica $P(m)$"],"correcta":0,
 "explicacion":"El paso inductivo es un condicional, que dice que si la afirmación vale para m, entonces vale para m más 1. Que P de 1 sea verdadera es el caso base, y que valga para todo m es la conclusión de toda la inducción.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Es un condicional.","Se usa la hipótesis para llegar al caso siguiente.","Va de m a m más 1."],
 "errores":["","Eso es el caso base, y no el paso inductivo.","Eso es la conclusión final de la inducción, no el paso.","Va en el sentido contrario. El paso va de m a m más 1."]}
res=["La inducción tiene dos partes, el caso base y el paso inductivo.","En el paso se supone que vale para m y se prueba que vale para m más 1, usando el término nuevo.","Sin caso base no se prueba nada. La inducción fuerte supone todos los casos anteriores."]
write(lesson("fu-m2-l3","Lección 3 de 4","Inducción matemática",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-induccion.json")
