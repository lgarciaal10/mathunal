import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 3 Relaciones y funciones"
EL=[{"t":"trazo","puntos":[[str(t/4),str((t/4)**2)] for t in range(-13,14)],"c":0},
 {"t":"recta","p":["0","x"],"dir":["1","0"],"guion":True,"c":3,"guia":True},
 {"t":"segmento","a":["-sqrt(x)","0"],"b":["sqrt(x)","0"],"c":2},
 {"t":"segmento","a":["sqrt(x)","0"],"b":["sqrt(x)","x"],"c":1,"guia":True,"guion":True},
 {"t":"segmento","a":["-sqrt(x)","0"],"b":["-sqrt(x)","x"],"c":1,"guia":True,"guion":True},
 {"t":"punto","p":["sqrt(x)","x"],"c":2},{"t":"punto","p":["-sqrt(x)","x"],"c":2}]
graf={"tipo":"plano","x":[-4.2,4.2],"y":[-1.8,10.4],"a":0,"b":9,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"extremo superior c del intervalo de salidas","formula":"x"},{"rotulo":"extremo derecho de la imagen inversa","formula":"sqrt(x)"}],
 "etiquetas":["Salidas permitidas, entre 0 y c","Entradas permitidas, entre menos raíz de c y raíz de c"],"etiquetaSlider":"Valor de c, de 0 a 9",
 "alt":"La parábola y igual a x al cuadrado. Una recta horizontal a la altura c marca el límite de las salidas. Sobre el eje horizontal se resalta el intervalo de entradas que producen salidas entre 0 y c, que va de menos raíz de c a raíz de c"}
glos={"imagen":"La imagen directa de C por f es el conjunto de las salidas que producen los elementos de C.",
 "preimagen":"La imagen inversa de D por f reúne todas las entradas cuya salida cae en D. No requiere que f tenga inversa.",
 "codominio":"El codominio es el conjunto donde se declara que caen las salidas, y la imagen es la parte que realmente se alcanza.",
 "monotona":"Una función creciente conserva el orden, y por eso la imagen de un intervalo va de la imagen del extremo izquierdo a la del derecho."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La función es x al cuadrado. Se elige un intervalo de salidas de 0 a c y se buscan las entradas que caen allí."],
 [4,9,"Con c igual a 1, las entradas que dan salidas entre 0 y 1 son las que están entre menos 1 y 1."],
 [9,14,"Con c igual a 4, son las entradas entre menos 2 y 2."],
 [14,19,"Con c igual a 9 son las entradas entre menos 3 y 3. Esa es la imagen inversa del intervalo de 0 a 9."],
 [19,24,"La imagen inversa busca entradas, y la imagen directa busca salidas. No se debe confundir con la función inversa."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[5,1],[8,1],[9,4],[13,4],[14,9],[18,9],[24,9]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[19,24]}}
S=[
 sec("La idea",None,P("Una función se puede mirar en dos direcciones. La {{gl:imagen|imagen directa}} de un conjunto de entradas son las salidas que producen. La {{gl:preimagen|imagen inversa}} de un conjunto de salidas son las entradas que caen allí. Esta segunda no necesita que la función sea invertible, y se usa mucho para describir condiciones del tipo cuáles entradas cumplen una restricción.")),
 sec("Un ejemplo","Un ejemplo",P("Con f de x igual a x al cuadrado, se pide qué entradas dan una salida entre 0 y c. Mueve c y mira el intervalo de entradas."),EQ("f^{-1}([0,c])=\\{x:\\ 0\\le x^{2}\\le c\\}"),{"t":"grafica","animar":"dibujar","alt":"La parábola con el intervalo de entradas resaltado"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con f de x igual a x al cuadrado, ¿cuántos números enteros x tienen una salida entre 0 y 9?","opciones":[3,5,7,9],"correcta":7,"bien":"Muy bien. Son los enteros de menos 3 a 3, o sea 7. Más abajo se ve el intervalo completo.","mal":"Son 7, los enteros de menos 3 a 3, porque el cuadrado de cada uno de ellos es 9 o menos. Más abajo se ve el intervalo completo."}),
 sec("Recorriendo los valores de c","Valores de c",P("Mira las entradas permitidas con c igual a 1, 4 y 9."),{"t":"acercando","ds":[1,4,9],"alt":"El intervalo de entradas para tres valores de c"},P("Cada vez el intervalo de entradas es simétrico, porque el cuadrado de x y el de menos x son iguales.")),
 sec("Las dos definiciones","Definiciones",P("Se distinguen las dos direcciones con la misma función."),
   PASOS([("f(C)=\\{f(x):\\ x\\in C\\}","Imagen directa. Se aplican la función a las entradas."),
          ("f^{-1}(D)=\\{x\\in A:\\ f(x)\\in D\\}","Imagen inversa. Se buscan las entradas cuya salida cae en D."),
          ("f([1,2])=[1,4]","Con x al cuadrado, que crece en ese intervalo, las salidas van de 1 a 4."),
          ("f^{-1}([0,9])=[-3,3]","Las entradas con cuadrado entre 0 y 9.")]),
   OJO("La imagen inversa no es la función inversa. Se puede calcular la imagen inversa de cualquier función, aunque no sea invertible, y el resultado siempre es un conjunto.")),
 sec("Propiedades","Propiedades",P("La imagen inversa se porta muy bien con las operaciones de conjuntos, y la imagen directa no tanto."),
   PASOS([("f^{-1}(D_1\\cup D_2)=f^{-1}(D_1)\\cup f^{-1}(D_2)","La imagen inversa respeta uniones."),
          ("f^{-1}(D_1\\cap D_2)=f^{-1}(D_1)\\cap f^{-1}(D_2)","Y también intersecciones."),
          ("f(C_1\\cap C_2)\\subseteq f(C_1)\\cap f(C_2)","La imagen directa solo da una contención."),
          ("C_1=[-1,0],\\ C_2=[0,1]\\ \\Rightarrow\\ f(C_1\\cap C_2)=\\{0\\},\\ f(C_1)\\cap f(C_2)=[0,1]","Con x al cuadrado se ve que no hay igualdad.")]),
   OJO("Con la imagen directa, la imagen de una intersección puede ser más pequeña que la intersección de las imágenes. Con la imagen inversa eso no pasa.")),
 eng("La corriente que soporta una resistencia","La potencia que disipa una resistencia de 1 ohmio es P igual a I al cuadrado. Si la potencia máxima admisible es 9 vatios, las corrientes admisibles son las entradas I cuya salida cae en el intervalo de 0 a 9. Eso es la imagen inversa.","P=I^{2},\\quad P\\in[0,9]\\ \\Leftrightarrow\\ I\\in[-3,3]",
   [("Potencia máxima","9 W"),("Corriente admisible","entre menos 3 A y 3 A"),("Resistencia","1 ohmio")],"Una restricción sobre las salidas se traduce en una condición sobre las entradas. Así se pasa de la potencia máxima a la corriente máxima, y de ahí se dimensiona el cable. Entender la imagen inversa permite plantear estos límites de diseño sin invertir la función, aunque la función no sea invertible."),
 completar("Se calcula la imagen inversa de un intervalo por la función x al cuadrado.","f^{-1}([0,4])=[[hueco]]",
   [("[-2,2]","de menos 2 a 2"),("[0,2]","de 0 a 2"),("[0,16]","de 0 a 16")],0,
   ["","Falta la parte negativa, porque menos 1 también da una salida de 1.","Esos son los cuadrados de las salidas, y no las entradas."],"Busca las entradas cuyo cuadrado esté entre 0 y 4.","Las entradas con cuadrado entre 0 y 4 son las que están entre menos 2 y 2."),
 error("Alguien calculó la imagen directa del intervalo de menos 2 a 3 por x al cuadrado y se equivocó en un paso. Toca el paso que está mal.",
   [("f(-2)=4","Se evalúa el extremo izquierdo.","en menos 2 da 4"),
    ("f(3)=9","Se evalúa el extremo derecho.","en 3 da 9"),
    ("\\text{Entonces}\\ f([-2,3])=[4,9]","Este paso es el que falla.","el resultado es de 4 a 9")],2,
   "La función no es creciente en todo el intervalo. Baja hasta el 0 y luego sube, así que el menor valor es 0, y el mayor es 9. La imagen es el intervalo de 0 a 9.",
   "f([-2,3])=[0,9]","Mira qué pasa con la función cerca de x igual a 0."),
 ordenar("Estos son los pasos para calcular la imagen inversa del intervalo de 0 a 9 por x al cuadrado, pero están desordenados.",
   [("f^{-1}([0,9])=\\{x:\\ 0\\le x^{2}\\le9\\}","Se escribe la definición"),
    ("x^{2}\\le9","La condición de que sea al menos 0 siempre se cumple"),
    ("|x|\\le3","Se saca la raíz y queda el valor absoluto"),
    ("x\\in[-3,3]","Se escribe como intervalo")],[2,0,3,1],
   "Se parte de la definición, se simplifica la condición y se escribe el intervalo.","Se empieza con la definición."),
]
S+=cierre("Mini simulacro de imagen e imagen inversa",[
 banco("fu_c3_15","Las entradas con cuadrado entre 0 y 9 son las que están entre menos 3 y 3."),
 banco("fu_c3_16","La función crece en el intervalo, así que las salidas van de f de 1 a f de 2."),
 banco("fu_c3_17","La imagen inversa son las entradas cuya salida cae en el conjunto.")])
prac=[
 {"titulo":"Las dos direcciones","grafica":{"draw":1,"guide":1},"bloques":[P("La imagen inversa busca entradas a partir de las salidas."),EQ("f^{-1}(D)=\\{x:\\ f(x)\\in D\\}")]},
 {"titulo":"Mueve c","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 9. Abajo se lee el límite de las salidas y el extremo derecho de las entradas.")]},
 {"titulo":"Con c igual a 9","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":9,"bloques":[EQ("f^{-1}([0,9])=[-3,3]"),P("Con c igual a 9 las entradas van de menos 3 a 3.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":9},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Busca el menor y el mayor valor que toma la función en el intervalo."}]}]
preg={"tex":"\\text{Con}\\ f(x)=x^{2},\\ \\text{la imagen directa}\\ f([-1,2])\\ \\text{es}","opciones":["$[0,4]$","$[1,4]$","$[-1,4]$","$[0,2]$"],"correcta":0,
 "explicacion":"En el intervalo de menos 1 a 2 la función baja hasta 0, en x igual a 0, y sube hasta 4, en x igual a 2. Entonces las salidas van de 0 a 4. En el extremo izquierdo f de menos 1 vale 1, pero no es el mínimo.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Mira el valor en x igual a 0.","El mayor valor está en el extremo derecho.","Va de 0 a 4."],
 "errores":["","Se olvida que x igual a 0 está en el intervalo y da una salida menor que 1.","El cuadrado nunca es negativo, así que no puede llegar a menos 1.","Esos son los valores de x más altos, y no los de las salidas."]}
res=["La imagen directa son las salidas de un conjunto de entradas, y la imagen inversa son las entradas cuya salida cae en un conjunto.","La imagen inversa existe para cualquier función, aunque no sea invertible, y respeta uniones e intersecciones.","Para la imagen directa de un intervalo hay que buscar el menor y el mayor valor de la función en él."]
write(lesson("fu-m3-l5","Lección 5 de 5","Imagen e imagen inversa",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-imagen.json")
