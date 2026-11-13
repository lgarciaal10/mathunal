import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 2 Vectores en el espacio"
graf={"tipo":"plano","x":[-4.6,5.8],"y":[-3.6,3.6],"a":-3.1416,"b":3.1416,"inicio":1.5708,
 "elementos":[
  {"t":"poligono","puntos":[["0","0"],["2","0"],["2+3*cos(x)","3*sin(x)"],["3*cos(x)","3*sin(x)"]],"c":3},
  {"t":"vector","b":["2","0"],"nombre":"u","c":0},
  {"t":"vector","b":["3*cos(x)","3*sin(x)"],"nombre":"v","c":1}],
 "lecturas":[{"rotulo":"tercera componente de u por v","formula":"6*sin(x)"},{"rotulo":"longitud de u por v, igual al área","formula":"6*abs(sin(x))"}],
 "etiquetas":["Es positiva si el producto vectorial sale de la hoja hacia quien mira, y negativa si entra en la hoja","Es el área del paralelogramo, siempre positiva"],"etiquetaSlider":"Ángulo de v, en radianes",
 "alt":"El vector u de longitud 2 sobre el eje horizontal y el vector v de longitud 3 que gira. El paralelogramo que forman tiene un área igual a la longitud del producto vectorial, y el signo del producto indica si v queda arriba o abajo de u"}
glos={"cruz":"El producto vectorial de dos vectores del espacio es otro vector, perpendicular a los dos. Su longitud es el área del paralelogramo que forman.",
 "mano":"La regla de la mano derecha dice hacia dónde apunta el producto vectorial. Los dedos van de u hacia v y el pulgar marca la dirección.",
 "anticonmutativo":"El producto vectorial es anticonmutativo, porque al cambiar el orden de los vectores el resultado cambia de signo.",
 "torque":"El torque es el producto vectorial del vector de posición por la fuerza. Mide la tendencia a girar."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"En este plano, u mide 2 y está sobre el eje. El vector v mide 3 y puede girar. El producto vectorial apunta perpendicular a la hoja."],
 [4,9,"Su tercera componente es 6 por el seno del ángulo. Con 90 grados vale 6, y es el máximo."],
 [9,13,"Con 0 grados, v es paralelo a u y el producto vectorial vale cero."],
 [13,18,"Si v pasa al otro lado, el seno es negativo y el producto apunta hacia el otro lado de la hoja, aunque su longitud es la misma."],
 [18,22,"La longitud del producto vectorial es siempre el área del paralelogramo."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1.5708],[8,1.5708],[10,0],[13,0],[15,-1.5708],[22,-1.5708]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("El {{gl:cruz|producto vectorial}} toma dos vectores del espacio y da un tercero que es perpendicular a los dos. Su longitud es el área del paralelogramo que forman, y su sentido lo da la {{gl:mano|regla de la mano derecha}}. Es {{gl:anticonmutativo|anticonmutativo}}, porque el orden importa. Se usa para el {{gl:torque|torque}} y para hallar normales.")),
 sec("Un ejemplo","Un ejemplo",P("Para verlo en una hoja, se toman dos vectores del plano. El producto vectorial apunta perpendicular a la hoja, y se lee en su tercera componente."),EQ("\\mathbf{u}\\times\\mathbf{v}=(0,0,\\ u_{1}v_{2}-u_{2}v_{1})"),{"t":"grafica","animar":"dibujar","alt":"El paralelogramo de u y v"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Si dos vectores son paralelos, el paralelogramo que forman se aplasta. ¿Cuánto vale su área?","opciones":[0,1,2,6],"correcta":0,"bien":"Muy bien. Vale 0, y por eso el producto vectorial de vectores paralelos es el vector cero. Más abajo se ve.","mal":"Vale 0, porque el paralelogramo se aplasta en un segmento. Por eso el producto vectorial de vectores paralelos es el vector cero. Más abajo se ve."}),
 sec("Girando v","Girando",P("Mira el producto vectorial con ángulos de 90 grados, 0 y menos 90 grados."),{"t":"acercando","ds":[1.5708,0,-1.5708],"alt":"El paralelogramo para tres ángulos de v"},P("A 90 grados el producto vale 6 y a menos 90 vale menos 6. Con 0 grados vale cero.")),
 sec("Cómo se calcula","Cómo se calcula",P("Cada componente es un determinante de dos por dos."),
   PASOS([("\\mathbf{u}\\times\\mathbf{v}=(u_{2}v_{3}-u_{3}v_{2},\\ u_{3}v_{1}-u_{1}v_{3},\\ u_{1}v_{2}-u_{2}v_{1})","La fórmula completa."),
          ("\\mathbf{i}\\times\\mathbf{j}=\\mathbf{k}","Los vectores de la base dan el tercero."),
          ("(2,1,0)\\times(1,3,0)=(0,0,\\ 2\\cdot3-1\\cdot1)=(0,0,5)","Con dos vectores del plano, solo queda la tercera componente."),
          ("\\|\\mathbf{u}\\times\\mathbf{v}\\|=\\|\\mathbf{u}\\|\\,\\|\\mathbf{v}\\|\\operatorname{sen}\\theta","La longitud del producto vectorial.")])),
 sec("Propiedades","Propiedades",P("El producto vectorial se comporta distinto del producto de números."),
   PASOS([("\\mathbf{u}\\times\\mathbf{v}=-(\\mathbf{v}\\times\\mathbf{u})","Anticonmutativo. Al cambiar el orden cambia el signo."),
          ("\\mathbf{u}\\times\\mathbf{u}=\\mathbf{0}","Un vector con él mismo da el vector cero."),
          ("(\\mathbf{u}\\times\\mathbf{v})\\cdot\\mathbf{u}=0","El resultado es perpendicular a u y también a v."),
          ("\\mathbf{u}\\parallel\\mathbf{v}\\ \\Leftrightarrow\\ \\mathbf{u}\\times\\mathbf{v}=\\mathbf{0}","Es cero si y solo si los vectores son paralelos.")]),
   OJO("El producto vectorial solo existe en el espacio de tres dimensiones, y no es asociativo. El orden de los factores importa.")),
 eng("El torque de una fuerza","Se aplica una fuerza de 100 newtons hacia arriba en el extremo de una llave de 0.5 metros. El torque es el producto vectorial del vector de posición por la fuerza, y apunta perpendicular a las dos, a lo largo del eje del tornillo.","\\boldsymbol{\\tau}=\\mathbf{r}\\times\\mathbf{F}=(0,0,50)",
   [("Posición","(0.5, 0, 0) m"),("Fuerza","(0, 100, 0) N"),("Torque","(0, 0, 50) N·m")],"El torque vale 50 newton metro y apunta a lo largo del eje, que es la dirección en que el tornillo avanza o retrocede. Si la fuerza se aplicara paralela a la llave, el producto vectorial sería cero y no habría giro. Por eso las llaves largas ayudan, ya que a mayor distancia hay mayor torque con la misma fuerza."),
 completar("Se aplica la anticonmutatividad del producto vectorial. Falta el resultado.","\\mathbf{j}\\times\\mathbf{i}=[[hueco]]",
   [("-\\mathbf{k}","menos k"),("\\mathbf{k}","k"),("\\mathbf{0}","el vector cero")],0,
   ["","Con i por j se obtiene k, pero al invertir el orden el resultado cambia de signo.","El vector cero solo aparece con vectores paralelos, y estos son perpendiculares."],"Al cambiar el orden cambia el signo.","i cruz j es k, y j cruz i es menos k."),
 error("Alguien analizó el producto vectorial de i y j y se equivocó en un paso. Toca el paso que está mal.",
   [("\\mathbf{u}=\\mathbf{i},\\quad \\mathbf{v}=\\mathbf{j}","Son los dos vectores.","u es i y v es j"),
    ("\\mathbf{u}\\times\\mathbf{v}=\\mathbf{k}","El producto.","el producto es k"),
    ("\\text{Entonces}\\ \\mathbf{v}\\times\\mathbf{u}=\\mathbf{k}","Este paso es el que falla.","por tanto j cruz i también es k")],2,
   "El producto vectorial es anticonmutativo. Al cambiar el orden cambia el signo, así que j cruz i es menos k.",
   "\\mathbf{v}\\times\\mathbf{u}=-\\mathbf{k}","Recuerda qué pasa al cambiar el orden."),
 ordenar("Estos son los pasos para hallar la tercera componente de (2, 1, 0) por (1, 3, 0), pero están desordenados.",
   [("\\mathbf{u}=(2,1,0),\\ \\mathbf{v}=(1,3,0)","Se escriben los vectores"),
    ("(\\mathbf{u}\\times\\mathbf{v})_{3}=u_{1}v_{2}-u_{2}v_{1}","Se escribe la tercera componente"),
    ("2\\cdot3-1\\cdot1","Se sustituye"),
    ("5","Se calcula")],[2,0,3,1],
   "Se escribe la fórmula de la tercera componente, se sustituye y se calcula.","Se empieza con los vectores."),
]
S+=cierre("Mini simulacro del producto vectorial",[
 banco("gv_c2_01","Con la regla de la mano derecha, i cruz j es k."),
 banco("gv_c2_12","Es el área del rectángulo de lados 2 y 3."),
 banco("gv_c2_13","El producto vectorial es anticonmutativo.")])
prac=[
 {"titulo":"Dos vectores","grafica":{"draw":1},"bloques":[P("Un vector u fijo y un vector v que gira, en una hoja."),EQ("(\\mathbf{u}\\times\\mathbf{v})_{3}=6\\operatorname{sen}\\theta")]},
 {"titulo":"Gira v","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la tercera componente del producto y su longitud.")]},
 {"titulo":"Ángulo recto","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1.5708,"bloques":[EQ("\\theta=90^{\\circ}\\ \\Rightarrow\\ \\|\\mathbf{u}\\times\\mathbf{v}\\|=6"),P("Con 90 grados el producto vectorial es el mayor posible.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1.5708},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Los vectores paralelos tienen un paralelogramo de área cero."}]}]
preg={"tex":"\\text{El producto vectorial}\\ (1,2,3)\\times(2,4,6)\\ \\text{es}","opciones":["$\\mathbf{0}$","$(0,0,1)$","$(2,8,18)$","$28$"],"correcta":0,
 "explicacion":"Los vectores son paralelos, porque (2, 4, 6) es el doble de (1, 2, 3). El paralelogramo que forman se aplasta, y su área es cero. Por eso el producto vectorial es el vector cero.",
 "verificacion":{"formula":"2*6-3*4+0*x","a":0,"esperado":0},
 "pistas":["Mira si un vector es múltiplo del otro.","Sí lo es, es el doble.","Entonces el área es cero."],
 "errores":["","Ese vector no es perpendicular a los dos. Aquí el resultado es único y no depende de una elección.","Eso sale de multiplicar componente por componente, que no es el producto vectorial.","Eso es el producto punto, y es un número. El producto vectorial da un vector."]}
res=["El producto vectorial de dos vectores es perpendicular a los dos, y su longitud es el área del paralelogramo.","Es anticonmutativo y vale cero cuando los vectores son paralelos.","Se calcula con determinantes de dos por dos, y la regla de la mano derecha da el sentido."]
write(lesson("gv-m2-l1","Lección 1 de 4","Producto vectorial",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-cruz.json")
