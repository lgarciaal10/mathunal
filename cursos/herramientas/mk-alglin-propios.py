import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 3 Ortogonalidad y valores propios"
graf={"tipo":"plano","x":[-5.5,7.33],"y":[-3,4],"a":0,"b":3.14,"inicio":0.7853981634,
 "elementos":[
  {"t":"recta","p":["0","0"],"dir":["1","1"],"guion":True,"nombre":"dirección propia","c":1,"guia":True},
  {"t":"recta","p":["0","0"],"dir":["1","-1"],"guion":True,"c":3,"guia":True},
  {"t":"vector","b":["cos(x)","sin(x)"],"nombre":"v","c":0},
  {"t":"vector","b":["cos(x)+2*sin(x)","2*cos(x)+sin(x)"],"nombre":"Av","c":2}],
 "lecturas":[{"rotulo":"producto cruzado de v y Av","formula":"2*cos(2*x)"},{"rotulo":"longitud de Av","formula":"sqrt((cos(x)+2*sin(x))^2+(2*cos(x)+sin(x))^2)"}],
 "etiquetas":["Producto cruzado de v y Av","Longitud de Av"],"etiquetaSlider":"Ángulo de v en radianes",
 "alt":"Un vector unitario v que gira y su imagen Av bajo la matriz de filas (1, 2) y (2, 1). Av apunta en la misma dirección que v solo cuando v cae sobre una de las dos rectas punteadas"}
glos={"propio":"Un valor propio de una matriz A es un número lambda para el que A por v es igual a lambda por v con v distinto de cero. Ese vector v es un vector propio.",
 "caracteristica":"La ecuación característica de A es el determinante de A menos lambda por la identidad igual a cero. Sus soluciones son los valores propios.",
 "traza":"La traza de una matriz cuadrada es la suma de los números de su diagonal principal."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"La matriz A, de filas (1, 2) y (2, 1), transforma cada vector. Aquí gira un vector unitario v."],
 [3,6,"Casi siempre Av apunta en una dirección distinta de la de v, y además cambia de longitud."],
 [6,12,"Pero hay dos direcciones especiales, las rectas punteadas, donde Av queda sobre la misma recta que v."],
 [12,17,"Con v a 45 grados, Av apunta igual que v y es 3 veces más largo. Entonces 3 es un valor propio."],
 [17,22,"Con v a 135 grados, Av apunta al lado contrario y mide lo mismo. Entonces menos 1 es otro valor propio."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,0.2],[9,1.2],[12,0.7853981634],[16,0.7853981634],[17,2.3561944902],[22,2.3561944902]],"guide":[[6,0],[7,1]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("Una matriz casi siempre cambia la dirección de los vectores. Pero hay direcciones especiales que la matriz solo estira o encoge. Los vectores en esas direcciones se llaman {{gl:propio|vectores propios}}, y el factor por el que se estiran es su valor propio. Son la clave para entender vibraciones, estabilidad y muchos más procesos.")),
 sec("Un ejemplo","Un ejemplo",P("Mira cómo actúa la matriz A sobre un vector unitario v que gira alrededor del origen."),EQ("A="+M(1,2,2,1)+",\\qquad A\\mathbf{v}=\\lambda\\mathbf{v}"),{"t":"grafica","animar":"dibujar","alt":"Un vector que gira y su imagen"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con v a 45 grados, v es casi (0.71, 0.71) y Av es casi (2.12, 2.12). ¿Cuántas veces es más largo Av que v?","opciones":[1,2,3,4],"correcta":3,"bien":"Muy bien. Es 3 veces más largo, y apunta igual. Más abajo se ve.","mal":"Es 3 veces más largo, porque 2.12 entre 0.71 es 3. Más abajo se ve."}),
 sec("Las direcciones especiales","Direcciones",P("Mira cómo se mueven v y Av al girar v."),{"t":"acercando","ds":[0.2,0.7853981634,1.5,2.3561944902],"alt":"El vector v y su imagen para varios ángulos"},P("Con 45 grados y con 135 grados el producto cruzado de v y Av vale 0, o sea que los dos vectores quedan sobre la misma recta. Esas son las direcciones propias.")),
 sec("Hallar los valores propios","Valores propios",P("Se busca lambda para el que A menos lambda por la identidad no sea invertible, o sea con determinante cero. Esa es la {{gl:caracteristica|ecuación característica}}."),
   PASOS([("\\det(A-\\lambda I)=\\det"+M("1-\\lambda",2,2,"1-\\lambda")+"=(1-\\lambda)^{2}-4","Se resta lambda de la diagonal y se calcula el determinante."),
          ("\\lambda^{2}-2\\lambda-3=0\\ \\Rightarrow\\ (\\lambda-3)(\\lambda+1)=0","Se desarrolla y se factoriza."),
          ("\\lambda=3\\quad\\text{o}\\quad\\lambda=-1","Son los dos valores propios.")]),
   OJO("Los valores propios de una matriz que no es triangular no se leen en la diagonal. Hay que resolver la ecuación característica.")),
 sec("Hallar los vectores propios","Vectores propios",P("Para cada valor propio se resuelve el sistema homogéneo A menos lambda por la identidad por v igual a cero."),
   PASOS([("\\lambda=3:\\quad "+M(-2,2,2,-2)+"\\mathbf{v}=0\\ \\Rightarrow\\ \\mathbf{v}=(1,1)","Las dos filas dicen lo mismo, v1 igual a v2."),
          ("\\lambda=-1:\\quad "+M(2,2,2,2)+"\\mathbf{v}=0\\ \\Rightarrow\\ \\mathbf{v}=(1,-1)","Las dos filas dicen v1 más v2 igual a 0."),
          ("A(1,1)=(3,3)=3\\,(1,1)","Se comprueba con el primero.")])),
 sec("Traza y determinante","Traza y determinante",P("Hay dos atajos para revisar los resultados. La suma de los valores propios es la {{gl:traza|traza}} y su producto es el determinante."),
   PASOS([("\\lambda_{1}+\\lambda_{2}=3+(-1)=2=\\operatorname{tr}A","La traza de A es 1 más 1."),
          ("\\lambda_{1}\\lambda_{2}=3\\cdot(-1)=-3=\\det A","El determinante de A es 1 por 1 menos 2 por 2."),
          ("\\lambda=0\\ \\text{es valor propio}\\iff\\det A=0","Si hay un valor propio 0, la matriz no es invertible.")])),
 eng("Las vibraciones de dos masas","Dos masas iguales unidas con resortes vibran de maneras especiales llamadas modos. Los valores propios de la matriz de rigidez dividida entre la masa dan los cuadrados de las frecuencias naturales, y los vectores propios dan la forma de cada modo.","\\dfrac{k}{m}"+M(2,-1,-1,2)+"\\mathbf{v}=\\omega^{2}\\mathbf{v}",
   [("Rigidez entre masa","100 por segundo al cuadrado"),("Modo 1","masas juntas, 10 rad/s"),("Modo 2","masas opuestas, 17.3 rad/s")],"Los valores propios de la matriz son 100 y 300, con vectores propios (1, 1) y (1, menos 1). Las frecuencias son 10 y unos 17.3 radianes por segundo, o sea 1.59 y 2.76 hercios. En el primer modo las masas se mueven juntas y en el segundo se mueven opuestas. Es un modelo simplificado, porque no incluye amortiguamiento."),
 completar("Se halla la ecuación característica de la matriz de filas (1, 2) y (2, 1). Falta el desarrollo.","(1-\\lambda)^{2}-4=[[hueco]]",
   [("\\lambda^{2}-2\\lambda-3","lambda al cuadrado menos dos lambda menos tres"),("\\lambda^{2}-2\\lambda+5","lambda al cuadrado menos dos lambda más cinco"),("\\lambda^{2}-5","lambda al cuadrado menos cinco")],0,
   ["","El término constante es 1 menos 4, o sea menos 3, y no 5.","Falta el término del medio. (1 menos lambda) al cuadrado es 1 menos 2 lambda más lambda al cuadrado."],"Desarrolla el cuadrado y resta 4.","(1 menos lambda) al cuadrado es 1 menos 2 lambda más lambda al cuadrado. Al restar 4 queda lambda al cuadrado menos 2 lambda menos 3."),
 error("Alguien halló los valores propios de una matriz y se equivocó en un paso. Toca el paso que está mal.",
   [("A="+M(1,2,2,1),"Es la matriz.","La matriz tiene filas 1, 2 y 2, 1"),
    ("\\text{Los valores propios son los de la diagonal, o sea 1 y 1}","Este paso es el que falla.","Los valores propios son los de la diagonal, o sea 1 y 1"),
    ("\\text{La matriz tiene un solo valor propio, 1}","Depende del paso anterior.","La matriz tiene un solo valor propio, 1")],1,
   "Los valores propios solo se leen en la diagonal cuando la matriz es triangular. Aquí hay que resolver la ecuación característica, y salen 3 y menos 1. Se comprueba con la traza, 3 más menos 1 es 2.",
   "\\lambda^{2}-2\\lambda-3=0\\ \\Rightarrow\\ \\lambda=3,\\ -1","Comprueba con la traza. ¿La suma de 1 y 1 da la traza de la matriz?"),
 ordenar("Estos son los pasos para hallar los valores propios de la matriz de filas (1, 2) y (2, 1), pero están desordenados.",
   [("\\det(A-\\lambda I)=0","Se plantea la ecuación característica"),
    ("(1-\\lambda)^{2}-4=0","Se calcula el determinante"),
    ("\\lambda^{2}-2\\lambda-3=0\\ \\Rightarrow\\ (\\lambda-3)(\\lambda+1)=0","Se desarrolla y se factoriza"),
    ("\\lambda=3,\\ \\lambda=-1","Son los valores propios")],[2,0,3,1],
   "Se plantea la ecuación, se calcula el determinante, se factoriza y se leen las soluciones.","Se empieza con la ecuación característica."),
]
S+=cierre("Mini simulacro de valores propios",[
 banco("al_c3_11","Es la ecuación característica, porque $A-\\lambda I$ no es invertible."),
 banco("al_c3_12","La suma de los valores propios es la traza, $1+4=5$."),
 banco("al_c3_13","El producto de los valores propios es el determinante, $1\\cdot4-2\\cdot3=-2$.")])
prac=[
 {"titulo":"Un vector que gira","grafica":{"draw":1},"bloques":[P("El vector unitario v gira y la matriz lo transforma en Av."),EQ("A="+M(1,2,2,1))]},
 {"titulo":"Gira v","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador para girar v. Abajo se ven el producto cruzado de v y Av, que mide qué tan lejos está Av de la dirección de v, y la longitud de Av.")]},
 {"titulo":"Direcciones propias","grafica":{"draw":1,"guide":1},"laboratorio":True,"d":0.7853981634,"bloques":[P("Con v a 45 grados, el producto cruzado es 0 y Av mide 3. Av apunta igual que v y es 3 veces más largo.")]},
 {"titulo":"El otro valor propio","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2.3561944902,"bloques":[EQ("\\lambda_{1}=3,\\quad \\lambda_{2}=-1"),P("Con 135 grados, Av mide 1 y apunta al lado contrario. Es el valor propio menos 1.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2.3561944902},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Resuelve la ecuación característica y comprueba con la traza."}]}]
preg={"tex":"\\text{Valor propio más pequeño de}\\ "+M(4,1,2,3),"opciones":["$2$","$5$","$1$","$3$"],"correcta":0,
 "explicacion":"La ecuación característica es (4 menos lambda) por (3 menos lambda) menos 2, que queda lambda al cuadrado menos 7 lambda más 10. Se factoriza como (lambda menos 2) por (lambda menos 5). Los valores propios son 2 y 5, y el más pequeño es 2.",
 "verificacion":{"formula":"(7-sqrt(49-4*10))/2+0*x","a":0,"esperado":2},
 "pistas":["Plantea el determinante de A menos lambda por la identidad.","Queda lambda al cuadrado menos 7 lambda más 10. La traza es 7 y el determinante es 10.","Busca dos números que sumen 7 y multipliquen 10."],
 "errores":["","Ese es el valor propio más grande. Se pide el más pequeño.","Los valores propios deben sumar 7, la traza, y multiplicar 10, el determinante. 1 y 7 no los cumplen.","Los valores propios deben sumar 7 y multiplicar 10. Si uno fuera 3, el otro sería 4, y eso da 12."]}
res=["Un vector propio es uno que la matriz solo estira, A v igual a lambda v. Lambda es su valor propio.","Los valores propios salen de det(A menos lambda I) igual a cero, y los vectores propios, del sistema homogéneo.","La suma de los valores propios es la traza, y su producto es el determinante."]
write(lesson("alglin-m3-l1","Lección 1 de 4","Valores y vectores propios",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-propios.json")
