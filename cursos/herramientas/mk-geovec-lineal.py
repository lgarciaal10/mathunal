import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 2 Vectores en el espacio"
graf={"tipo":"plano","x":[-4.0,8.5],"y":[-2.5,6.4],"a":-1,"b":3.5,"inicio":1,
 "elementos":[
  {"t":"vector","b":["2*x","x"],"nombre":"a u","c":0},
  {"t":"vector","a":["2*x","x"],"b":["2*x-1","x+2"],"nombre":"v","c":1},
  {"t":"punto","p":["3","4"],"c":3},
  {"t":"punto","p":["2*x-1","x+2"],"c":2}],
 "lecturas":[{"rotulo":"coeficiente a de u","formula":"x"},{"rotulo":"distancia de la punta al objetivo (3, 4)","formula":"sqrt(5)*abs(x-2)"}],
 "etiquetas":["Cuántas veces se toma u, con u igual a (2, 1)","Qué tan lejos queda la punta de a u más v del objetivo"],"etiquetaSlider":"Coeficiente a de u",
 "alt":"Los vectores u igual a (2, 1) y v igual a (menos 1, 2). Se toma a veces u y a continuación se agrega v. La punta del camino es a u más v, y con a igual a 2 llega al punto objetivo (3, 4)"}
glos={"combinacion":"Una combinación lineal de vectores es una suma de múltiplos de ellos, como a u más b v.",
 "generado":"El conjunto generado por unos vectores es el de todas sus combinaciones lineales.",
 "independientes":"Unos vectores son linealmente independientes si la única combinación que da el vector cero es la que tiene todos los coeficientes cero.",
 "dependientes":"Unos vectores son linealmente dependientes si alguno es combinación de los otros, o sea, si hay una combinación no trivial que da cero."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Los vectores u igual a (2, 1) y v igual a (menos 1, 2) se combinan. Primero se toma a veces u, y después se agrega v."],
 [4,10,"La punta del camino es a u más v. El punto marcado es el objetivo, (3, 4)."],
 [10,15,"Con a igual a 2, el camino llega justo al objetivo. Entonces (3, 4) es 2 u más v."],
 [15,19,"Esto se puede con cualquier objetivo del plano, porque u y v no son paralelos. Son linealmente independientes."],
 [19,22,"Si fueran paralelos, solo se alcanzarían los puntos de una recta."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,1],[10,3],[12,2],[19,2],[22,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[10,22]}}
S=[
 sec("La idea",None,P("Una {{gl:combinacion|combinación lineal}} suma múltiplos de unos vectores. Todas las combinaciones forman el conjunto {{gl:generado|generado}} por ellos. Si cada vector aporta una dirección nueva, son {{gl:independientes|linealmente independientes}}. Si alguno se puede armar con los otros, son {{gl:dependientes|dependientes}} y sobra alguno.")),
 sec("Un ejemplo","Un ejemplo",P("Se quiere llegar al punto (3, 4) combinando u igual a (2, 1) y v igual a (menos 1, 2). Mueve a hasta que la punta llegue."),EQ("a(2,1)+(-1,2)=(2a-1,\\ a+2)"),{"t":"grafica","animar":"dibujar","alt":"El camino de u y v hacia el objetivo"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con a igual a 2, 2 por (2, 1) es (4, 2). Si se le suma (menos 1, 2), ¿cuánto vale la segunda componente del resultado?","opciones":[2,3,4,5],"correcta":4,"bien":"Muy bien. Es 2 más 2, o sea 4. Y la primera es 4 menos 1, o sea 3. Más abajo se ve que llega al objetivo.","mal":"Es 2 más 2, o sea 4. Y la primera componente es 4 menos 1, o sea 3. Más abajo se ve que llega al objetivo."}),
 sec("Moviendo el coeficiente","El coeficiente",P("Mira el camino con a igual a 0, 1, 2 y 3."),{"t":"acercando","ds":[0,1,2,3],"alt":"El camino con cuatro valores de a"},P("Con a igual a <b>2</b> la punta coincide con el objetivo y la distancia es cero.")),
 sec("Dependencia e independencia","Independencia",P("Para decidir si unos vectores son independientes se busca una combinación no trivial que dé cero."),
   PASOS([("(1,2,3),\\ (2,4,6),\\ (0,0,1)","Los tres vectores del ejemplo del banco."),
          ("2(1,2,3)-(2,4,6)+0(0,0,1)=\\mathbf{0}","Hay una combinación con coeficientes no todos cero que da cero."),
          ("\\text{Entonces son linealmente dependientes}","Porque (2, 4, 6) es el doble de (1, 2, 3)."),
          ("\\{(1,0,0),(0,1,0),(1,1,0)\\}\\ \\text{dependiente}","Porque (1, 1, 0) es la suma de los dos primeros.")])),
 sec("El determinante","Con el determinante",P("En R³, tres vectores son independientes si y solo si el determinante que forman es distinto de cero."),
   PASOS([("\\det\\begin{pmatrix}1&0&0\\\\0&1&0\\\\0&0&1\\end{pmatrix}=1","Los vectores de la base son independientes."),
          ("\\det\\neq0\\ \\Leftrightarrow\\ \\text{independientes}","El criterio del determinante."),
          ("\\det=0\\ \\Leftrightarrow\\ \\text{dependientes, o sea, coplanares}","Si es cero, los tres están en un mismo plano.")]),
   OJO("Independientes no significa perpendiculares. Dos vectores pueden formar cualquier ángulo distinto de cero y de 180 grados y ser independientes.")),
 eng("Los movimientos de un robot","Un robot tiene dos actuadores que mueven la herramienta en las direcciones (2, 1) y (menos 1, 2). Cualquier posición del plano se alcanza como combinación de ellas. Es posible porque las dos direcciones son independientes.","\\det\\begin{pmatrix}2&-1\\\\1&2\\end{pmatrix}=5",
   [("Actuador 1","(2, 1)"),("Actuador 2","(menos 1, 2)"),("Determinante","5, alcanza todo el plano")],"Como el determinante es distinto de cero, el robot alcanza cualquier punto del plano. Si las dos direcciones fueran paralelas, el determinante sería cero y la herramienta solo podría moverse sobre una recta. Esas posiciones, llamadas singularidades, se evitan al diseñar el robot."),
 completar("Se calcula una combinación de los vectores de la base. Falta el resultado.","2(1,0)+3(0,1)=[[hueco]]",
   [("(2,3)","dos, tres"),("(3,2)","tres, dos"),("(5,5)","cinco, cinco")],0,
   ["","Los coeficientes se invirtieron. El 2 multiplica a (1, 0) y va en la primera componente.","Se sumaron los coeficientes como si fueran una sola componente."],"Cada coeficiente multiplica a su vector.","2 por (1, 0) es (2, 0), 3 por (0, 1) es (0, 3), y su suma es (2, 3)."),
 error("Alguien analizó tres vectores y se equivocó en un paso. Toca el paso que está mal.",
   [("(2,4,6)=2(1,2,3)","Un vector es múltiplo de otro.","el segundo es el doble del primero"),
    ("2(1,2,3)-(2,4,6)=\\mathbf{0}","Hay una combinación no trivial que da cero.","la combinación da cero"),
    ("\\text{Entonces son linealmente independientes}","Este paso es el que falla.","por tanto son independientes")],2,
   "Si existe una combinación con coeficientes no todos cero que da el vector cero, los vectores son dependientes. Aquí (2, 4, 6) es el doble de (1, 2, 3).",
   "\\text{combinación no trivial}=\\mathbf{0}\\ \\Rightarrow\\ \\text{dependientes}","Recuerda qué significa una combinación no trivial que da cero."),
 ordenar("Estos son los pasos para escribir (3, 4) como 2 por (2, 1) más (menos 1, 2), pero están desordenados.",
   [("2(2,1)=(4,2)","Se calcula 2u"),
    ("v=(-1,2)","Se toma v"),
    ("(4-1,\\ 2+2)","Se suman componente a componente"),
    ("(3,4)","Es el objetivo")],[2,0,3,1],
   "Se multiplica u por 2, se suma v componente a componente y se obtiene el objetivo.","Se empieza multiplicando u por 2."),
]
S+=cierre("Mini simulacro de combinaciones lineales y dependencia",[
 banco("gv_c2_04","$(2,4,6)=2(1,2,3)$, así que son dependientes."),
 banco("gv_c2_18","Son independientes si y solo si el determinante es distinto de cero."),
 banco("gv_c2_20","$(1,1,0)$ es la suma de los otros dos.")])
prac=[
 {"titulo":"El camino","grafica":{"draw":1},"bloques":[P("Se toma a veces u y se agrega v."),EQ("a(2,1)+(-1,2)")]},
 {"titulo":"Mueve a","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el coeficiente y la distancia de la punta al objetivo.")]},
 {"titulo":"Llegar al objetivo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("2(2,1)+(-1,2)=(3,4)"),P("Con a igual a 2 la punta coincide con el objetivo.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Calcula el determinante de los tres vectores."}]}]
preg={"tex":"\\text{Los vectores}\\ (1,0,0),\\ (0,1,0),\\ (0,0,2)\\ \\text{son}","opciones":["linealmente independientes","linealmente dependientes","coplanares","paralelos"],"correcta":0,
 "explicacion":"El determinante que forman es 1 por 1 por 2, o sea 2, que es distinto de cero. Entonces son linealmente independientes y no son coplanares.",
 "verificacion":{"formula":"1*(1*2-0*0)-0+0*x","a":0,"esperado":2},
 "pistas":["Calcula el determinante de tres por tres.","Es una matriz diagonal.","El determinante es 2, distinto de cero."],
 "errores":["","El determinante no es cero, así que no hay una combinación no trivial que dé cero.","Coplanares exigiría un determinante cero, y aquí vale 2.","Ninguno es múltiplo de otro, así que no son paralelos."]}
res=["Una combinación lineal suma múltiplos de vectores, y todas las combinaciones forman su conjunto generado.","Unos vectores son dependientes si una combinación no trivial da cero, y entonces alguno sobra.","En R³, tres vectores son independientes si y solo si su determinante es distinto de cero."]
write(lesson("gv-m2-l4","Lección 4 de 4","Combinaciones lineales y dependencia",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-lineal.json")
