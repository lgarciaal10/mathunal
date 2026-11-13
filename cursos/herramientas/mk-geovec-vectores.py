import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 1 Vectores y rectas en el plano"
graf={"tipo":"plano","x":[-3.4,9.7],"y":[-2.2,4.95],"a":-2,"b":8,"inicio":3,
 "elementos":[
  {"t":"vector","b":["2","1"],"nombre":"u","c":0},
  {"t":"vector","b":["x","3"],"nombre":"v","c":1}],
 "lecturas":[{"rotulo":"determinante de u y v","formula":"2*3-1*x"},{"rotulo":"longitud de v","formula":"sqrt(x*x+9)"}],
 "etiquetas":["Determinante u1 por v2 menos u2 por v1, es cero si son paralelos","Longitud del vector v"],"etiquetaSlider":"Primera componente de v",
 "alt":"El vector u igual a (2, 1) y el vector v igual a (x, 3). Al mover el deslizador cambia v. Con x igual a 6, v es el triple de u y los dos vectores son paralelos"}
glos={"componentes":"Las componentes de un vector son sus coordenadas. El vector (3, 4) avanza 3 en horizontal y 4 en vertical.",
 "norma":"La norma de un vector es su longitud, la raíz de la suma de los cuadrados de sus componentes.",
 "unitario":"Un vector unitario mide 1. Se obtiene dividiendo un vector entre su norma.",
 "paralelos":"Dos vectores son paralelos si uno es múltiplo del otro. En el plano, eso ocurre cuando u1 por v2 menos u2 por v1 vale cero."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"El vector u es (2, 1) y el vector v es (x, 3), con x variable."],
 [3,8,"La longitud de v es la raíz de x al cuadrado más 9. Crece cuando x se aleja de cero."],
 [8,14,"Dos vectores son paralelos si uno es múltiplo del otro. El determinante u1 por v2 menos u2 por v1 mide cuánto se alejan de serlo."],
 [14,19,"Con x igual a 6, v es (6, 3), que es el triple de u. El determinante vale 0 y los vectores son paralelos."],
 [19,22,"Con cualquier otro valor de x el determinante no es cero y los vectores no son paralelos."]],
 "canales":{"draw":[[0.3,0],[2.8,1]],"d":[[3,0],[8,0],[10,2],[13,4],[14,5],[17,6],[19,6],[22,6]],"guide":[[3,0],[4,1]]},
 "intervalos":{"ok":[14,22]}}
S=[
 sec("La idea",None,P("Un vector del plano se describe con dos {{gl:componentes|componentes}}, y se representa con una flecha desde el origen. De él interesan su longitud, que es la {{gl:norma|norma}}, y su dirección. Los vectores se suman componente a componente, se multiplican por números, y se comparan para saber si son {{gl:paralelos|paralelos}} o perpendiculares.")),
 sec("Un ejemplo","Un ejemplo",P("Mira el vector u igual a (2, 1) y el vector v igual a (x, 3). Al mover x, cambian la longitud de v y su dirección respecto de u."),EQ("\\|v\\|=\\sqrt{x^{2}+9},\\qquad u_{1}v_{2}-u_{2}v_{1}=6-x"),{"t":"grafica","animar":"dibujar","alt":"Los vectores u y v"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El vector v es (6, 3) y el vector u es (2, 1). ¿Por cuánto hay que multiplicar a u para obtener v?","opciones":[2,3,4,6],"correcta":3,"bien":"Muy bien. Por 3, porque 3 por 2 es 6 y 3 por 1 es 3. Por eso son paralelos. Más abajo se ve.","mal":"Por 3, porque 3 por 2 es 6 y 3 por 1 es 3. Como uno es múltiplo del otro, son paralelos. Más abajo se ve."}),
 sec("Moviendo v","Moviendo v",P("Mira el vector v para x igual a 0, 3, 6 y 8."),{"t":"acercando","ds":[0,3,6,8],"alt":"El vector v para cuatro valores de x"},P("Solo con x igual a <b>6</b> los vectores son paralelos. En ese caso el determinante vale cero.")),
 sec("Norma y vector unitario","Norma",P("La norma sale del teorema de Pitágoras con las dos componentes."),
   PASOS([("\\|(3,4)\\|=\\sqrt{9+16}=5","Se suman los cuadrados y se saca la raíz."),
          ("\\|(3,-4)\\|=\\sqrt{9+16}=5","El signo de una componente no cambia la longitud."),
          ("\\hat{u}=\\dfrac{1}{5}(3,4)=(0.6,\\ 0.8)","Dividir entre la norma da un vector unitario."),
          ("\\|\\hat{u}\\|=\\sqrt{0.36+0.64}=1","Se comprueba que mide 1.")])),
 sec("Paralelos y perpendiculares","Paralelos",P("Para decidir cómo se relacionan dos vectores se usan dos cuentas distintas."),
   PASOS([("u=(2,4),\\ v=(-1,-2):\\quad 2(-2)-4(-1)=0","El determinante es cero, así que son paralelos. De hecho, v es menos un medio de u."),
          ("u=(1,2),\\ v=(4,-2):\\quad 1\\cdot4+2(-2)=0","El producto punto es cero, así que son perpendiculares."),
          ("u=(1,2),\\ v=(2,1):\\quad \\text{ni uno ni otro}","Ninguna de las dos cuentas da cero.")]),
   OJO("Paralelos y perpendiculares se detectan con cuentas distintas. El determinante cero indica paralelos, y el producto punto cero indica perpendiculares.")),
 eng("La velocidad resultante de un avión","Un avión vuela a 200 kilómetros por hora hacia el este mientras el viento sopla a 50 kilómetros por hora hacia el norte. La velocidad respecto del suelo es la suma de los dos vectores, y su norma da la rapidez.","\\mathbf{v}=\\mathbf{a}+\\mathbf{w}=(200,50)",
   [("Velocidad del avión","(200, 0) km/h"),("Viento","(0, 50) km/h"),("Rapidez respecto del suelo","206.2 km/h")],"La norma de (200, 50) es la raíz de 40 000 más 2500, o sea 206.2 kilómetros por hora, y la dirección se desvía unos 14 grados hacia el norte. El piloto corrige el rumbo apuntando un poco hacia el sur del este. Es un modelo simplificado, porque supone un viento constante."),
 completar("Se calcula la norma del vector (6, 8). Falta lo que va dentro de la raíz.","\\|(6,8)\\|=\\sqrt{[[hueco]]}",
   [("36+64","treinta y seis más sesenta y cuatro"),("6+8","seis más ocho"),("36\\cdot64","treinta y seis por sesenta y cuatro")],0,
   ["","Hay que elevar al cuadrado cada componente antes de sumar.","Los cuadrados se suman, y no se multiplican."],"Se suman los cuadrados de las componentes.","6 al cuadrado más 8 al cuadrado es 100, y la raíz da 10."),
 error("Alguien analizó dos vectores y se equivocó en un paso. Toca el paso que está mal.",
   [("u=(2,4),\\quad v=(-1,-2)","Son los dos vectores.","u es 2, 4 y v es menos 1, menos 2"),
    ("u_{1}v_{2}-u_{2}v_{1}=-4+4=0","El determinante.","el determinante vale cero"),
    ("\\text{Entonces}\\ u\\ \\text{y}\\ v\\ \\text{son perpendiculares}","Este paso es el que falla.","por tanto son perpendiculares")],2,
   "Un determinante igual a cero indica vectores paralelos, y no perpendiculares. Aquí v es menos un medio de u, así que apuntan en la misma recta.",
   "u_{1}v_{2}-u_{2}v_{1}=0\\ \\Rightarrow\\ u\\parallel v","Recuerda qué indica un determinante cero."),
 ordenar("Estos son los pasos para convertir (3, 4) en un vector unitario, pero están desordenados.",
   [("\\|(3,4)\\|=5","Se calcula la norma"),
    ("\\hat{u}=\\dfrac{1}{5}(3,4)","Se divide el vector entre su norma"),
    ("\\hat{u}=(0.6,\\ 0.8)","Se calculan las componentes"),
    ("\\|\\hat{u}\\|=1","Se comprueba que mide 1")],[2,0,3,1],
   "Se calcula la norma, se divide el vector entre ella y se comprueba que el resultado mide 1.","Se empieza calculando la norma."),
]
S+=cierre("Mini simulacro de vectores en el plano",[
 banco("gv_c1_03","$v=-\\tfrac12 u$, así que son paralelos."),
 banco("gv_c1_07","$\\sqrt{9+16}=5$."),
 banco("gv_c1_08","Paralelos equivale a determinante cero, es decir, uno es múltiplo del otro.")])
prac=[
 {"titulo":"Dos vectores","grafica":{"draw":1},"bloques":[P("Un vector u fijo y un vector v que se mueve."),EQ("u=(2,1),\\qquad v=(x,3)")]},
 {"titulo":"Mueve v","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el determinante y la longitud de v.")]},
 {"titulo":"Paralelos","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":6,"bloques":[EQ("6-x=0\\ \\Rightarrow\\ x=6"),P("Con x igual a 6, v es el triple de u y el determinante es cero.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":6},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Calcula el determinante de los dos vectores."}]}]
preg={"tex":"\\text{Los vectores}\\ (4,6)\\ \\text{y}\\ (6,9)\\ \\text{son}","opciones":["paralelos","perpendiculares","iguales","ninguna de las anteriores"],"correcta":0,
 "explicacion":"El determinante es 4 por 9 menos 6 por 6, o sea 36 menos 36, que da 0. Además (6, 9) es 1.5 veces (4, 6). Son paralelos.",
 "verificacion":{"formula":"4*9-6*6+0*x","a":0,"esperado":0},
 "pistas":["Calcula 4 por 9 menos 6 por 6.","Da 0.","Un determinante cero indica vectores paralelos."],
 "errores":["","Para perpendiculares el producto punto debería ser cero, y aquí es 24 más 54, o sea 78.","Los vectores no son iguales, pero uno es múltiplo del otro.","Sí cumplen una de las dos relaciones. El determinante es cero."]}
res=["La norma de un vector es la raíz de la suma de los cuadrados de sus componentes, y un vector unitario mide 1.","Dos vectores son paralelos si el determinante u1 por v2 menos u2 por v1 es cero.","Dos vectores son perpendiculares si su producto punto es cero."]
write(lesson("gv-m1-l2","Lección 2 de 4","Vectores en el plano",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-vectores.json")
