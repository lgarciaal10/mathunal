import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 2 Espacios vectoriales y transformaciones"
graf={"tipo":"plano","x":[-3.5,9.33],"y":[-2,5],"a":-2,"b":4,"inicio":3,
 "elementos":[
  {"t":"vector","b":["1","0"],"nombre":"a","c":0},
  {"t":"vector","b":["0","1"],"nombre":"b","c":1},
  {"t":"vector","b":["x","2"],"nombre":"c","c":2},
  {"t":"segmento","a":["0","0"],"b":["x","0"],"guion":True,"nombre":"x por a","c":0,"guia":True},
  {"t":"segmento","a":["x","0"],"b":["x","2"],"guion":True,"nombre":"2 por b","c":1,"guia":True}],
 "lecturas":[{"rotulo":"peso de a","formula":"x"},{"rotulo":"peso de b","formula":"2"}],
 "etiquetas":["Peso de a","Peso de b"],"etiquetaSlider":"Primera componente del vector c",
 "alt":"Los vectores a igual a (1, 0) y b igual a (0, 1) y un tercer vector c igual a (x, 2) que siempre se escribe como x veces a más 2 veces b"}
glos={"independiente":"Un conjunto de vectores es linealmente independiente si la única combinación de ellos que da el vector cero es la que usa todos los coeficientes iguales a cero.",
 "dependiente":"Un conjunto es linealmente dependiente si alguno de sus vectores se puede escribir como combinación de los demás.",
 "generan":"Unos vectores generan un espacio si todos los vectores del espacio se pueden escribir como combinación de ellos. Su conjunto de combinaciones se llama el gen.",
 "base":"Una base de un espacio es un conjunto de vectores linealmente independientes que lo generan.",
 "dimension":"La dimensión de un espacio es el número de vectores de cualquiera de sus bases."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"Estos son tres vectores del plano, a igual a (1, 0), b igual a (0, 1) y c igual a (x, 2)."],
 [3,6,"El tercer vector se puede escribir con los dos primeros, c igual a x veces a más 2 veces b."],
 [6,12,"Al mover c, solo cambian los pesos. Siempre se puede escribir como combinación de a y b."],
 [12,17,"Por eso los tres vectores son dependientes. En el plano no caben más de dos vectores independientes."],
 [17,22,"Con x igual a 3, c es 3 veces a más 2 veces b. Entonces 3a más 2b menos c da el vector cero."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,3],[9,-1.5],[11,3.5],[12,3],[22,3]],"guide":[[3,0],[4,1]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("Unos vectores son {{gl:independiente|linealmente independientes}} si ninguno es combinación de los demás. Son {{gl:dependiente|dependientes}} si alguno sobra, porque se puede armar con los otros. Una {{gl:base|base}} es un conjunto de vectores independientes que {{gl:generan|generan}} todo el espacio. Con estas ideas se mide el tamaño de un espacio, que se llama su {{gl:dimension|dimensión}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira tres vectores del plano. Los dos primeros, a y b, apuntan en las direcciones de los ejes. El tercero, c, se mueve."),EQ("a=(1,0),\\quad b=(0,1),\\quad c=(x,2)"),{"t":"grafica","animar":"dibujar","alt":"Los tres vectores del plano"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con x igual a 3, el vector c es (3, 2). ¿Con qué peso aparece b, el vector (0, 1), cuando se escribe c con a y b?","opciones":[1,2,3,4],"correcta":2,"bien":"Muy bien. Pesa 2, porque la segunda componente de c es 2. Más abajo se ve cómo se arma c.","mal":"Pesa 2, porque la segunda componente de c es 2. Más abajo se ve cómo se arma c."}),
 sec("Armar el vector c","Armar c",P("Mira cómo c se arma con a y b, y cómo cambian solo los pesos."),{"t":"acercando","ds":[-1.5,0,3,3.5],"alt":"El vector c armado con a y b para varios valores de x"},P("Cualquier vector del plano se arma con a y b. Eso quiere decir que a y b <b>generan</b> el plano.")),
 sec("Independencia","Independencia",P("Para ver si unos vectores son independientes, se plantea la combinación que da cero y se mira si solo sirve con todos los pesos en cero."),
   PASOS([("c_{1}(1,3)+c_{2}(2,6)=(0,0)\\ \\Rightarrow\\ c_{1}+2c_{2}=0","El segundo vector es el doble del primero."),
          ("c_{1}=-2,\\ c_{2}=1\\ \\text{sirve}\\ \\Rightarrow\\ \\text{dependientes}","Hay pesos que no son cero y dan el vector cero."),
          ("\\det"+M(1,2,3,5)+"=-1\\ne 0\\ \\Rightarrow\\ \\text{independientes}","Con dos vectores de R2 también se puede usar el determinante de la matriz con ellos como columnas.")]),
   OJO("En un espacio de dimensión n no puede haber más de n vectores independientes. Tres vectores en el plano son siempre dependientes.")),
 sec("Bases y coordenadas","Bases",P("Todo vector se escribe de una sola manera como combinación de los vectores de una base. Esos pesos son las coordenadas del vector en esa base."),
   PASOS([("(3,1)=c_{1}(1,1)+c_{2}(1,-1)\\ \\Rightarrow\\ c_{1}+c_{2}=3,\\ c_{1}-c_{2}=1","Se plantea un sistema para los pesos, con la base {(1, 1), (1, menos 1)}."),
          ("c_{1}=2,\\quad c_{2}=1","Al sumar queda 2c1 igual a 4."),
          ("(3,1)\\ \\text{tiene coordenadas}\\ (2,1)\\ \\text{en esa base}","Se comprueba, 2 por (1, 1) más (1, menos 1) da (3, 1).")])),
 sec("Dimensión","Dimensión",P("La {{gl:dimension|dimensión}} es el número de vectores de una base. Todas las bases del mismo espacio tienen el mismo tamaño."),
   PASOS([("\\dim\\mathbb{R}^{n}=n","La base canónica tiene n vectores."),
          ("n\\ \\text{vectores independientes en}\\ \\mathbb{R}^{n}\\ \\Rightarrow\\ \\text{forman una base}","No hace falta comprobar que generan."),
          ("\\dim\\ \\text{gen}\\{(1,2,3)\\}=1","Un solo vector distinto de cero genera una recta.")])),
 eng("Descomponer una fuerza en dos barras","Una fuerza horizontal de 100 newtons se debe repartir entre dos barras que apuntan en las direcciones (1, 1) y (1, menos 1). Como esas dos direcciones forman una base, la fuerza se escribe de una sola forma como combinación de ellas.","(100,0)=c_{1}(1,1)+c_{2}(1,-1)",
   [("Fuerza","100 N sobre el eje x"),("Direcciones","(1, 1) y (1, −1)"),("Coordenadas","50 y 50")],"El sistema da c1 igual a 50 y c2 igual a 50. Cada barra recibe una componente de 50 por la raíz de 2, o sea unos 70.7 newtons. Es un modelo simplificado, porque supone barras articuladas y una fuerza en el plano."),
 completar("Se hallan las coordenadas de (3, 1) en la base {(1, 1), (1, menos 1)}. Al sumar c1 más c2 igual a 3 con c1 menos c2 igual a 1 se obtiene 2c1 igual a 4.","c_{1}=[[hueco]]",
   [("2","dos"),("1","uno"),("4","cuatro")],0,
   ["","Ese es el valor de c2. Falta dividir 4 entre 2, y eso da c1 igual a 2.","Ese es el lado derecho. Hay que dividir entre 2."],"Divide 4 entre 2.","Al sumar las ecuaciones queda 2c1 igual a 4, así que c1 vale 2. Luego c2 vale 1."),
 error("Alguien analizó tres vectores del plano y se equivocó en un paso. Toca el paso que está mal.",
   [("a=(1,0),\\quad b=(0,1),\\quad c=(2,3)","Son los tres vectores.","a es 1, 0, b es 0, 1, c es 2, 3"),
    ("\\text{Ninguno es múltiplo de otro, así que son independientes}","Este paso es el que falla.","Ninguno es múltiplo de otro, así que son independientes"),
    ("\\text{Forman una base de}\\ \\mathbb{R}^{2}","Depende del paso anterior.","Forman una base de R2")],1,
   "Ser múltiplo de otro es solo una forma de dependencia entre dos vectores. Con tres, basta con que uno sea combinación de los otros, y aquí c es igual a 2a más 3b. En R2 no puede haber tres vectores independientes.",
   "c=2a+3b\\ \\Rightarrow\\ 2a+3b-c=0\\ \\text{(dependientes)}","Intenta escribir c con a y b."),
 ordenar("Estos son los pasos para hallar las coordenadas de (3, 1) en la base de (1, 1) y (1, menos 1), pero están desordenados.",
   [("(3,1)=c_{1}(1,1)+c_{2}(1,-1)","Se plantea la combinación"),
    ("c_{1}+c_{2}=3,\\ \\ c_{1}-c_{2}=1","Se igualan las componentes"),
    ("2c_{1}=4\\ \\Rightarrow\\ c_{1}=2","Se suman las ecuaciones"),
    ("c_{2}=1","Se reemplaza para hallar c2")],[2,0,3,1],
   "Se plantea la combinación, se igualan componentes, se suman las ecuaciones y se halla el otro peso.","Se empieza planteando la combinación."),
]
S+=cierre("Mini simulacro de independencia y bases",[
 banco("al_c2_03","El primer conjunto tiene 3 vectores independientes, porque la matriz es triangular con unos en la diagonal. Los demás tienen menos de 3 vectores o un vector que es múltiplo de otro."),
 banco("al_c2_05","Se resuelve $a+b=5$ y $a-b=3$, y queda $a=4$."),
 banco("al_c2_08","$n$ vectores independientes en un espacio de dimensión $n$ forman una base.")])
prac=[
 {"titulo":"Tres vectores","grafica":{"draw":1},"bloques":[P("Estos son tres vectores del plano."),EQ("a=(1,0),\\quad b=(0,1),\\quad c=(x,2)")]},
 {"titulo":"Mueve c","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El vector c cambia y abajo se ven los pesos con los que se arma con a y b.")]},
 {"titulo":"Se arma con a y b","grafica":{"draw":1,"guide":1},"laboratorio":True,"d":3,"bloques":[P("Las líneas punteadas muestran c como x veces a más 2 veces b. Siempre hay pesos que lo arman.")]},
 {"titulo":"Dependientes","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("3a+2b-c=0"),P("Hay pesos distintos de cero que dan el vector cero, así que los tres vectores son dependientes.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Busca si un vector es suma de los otros."}]}]
preg={"tex":"\\dim\\ \\text{gen}\\{(1,0,1),\\ (0,1,1),\\ (1,1,2)\\}","opciones":["$2$","$3$","$1$","$0$"],"correcta":0,
 "explicacion":"El tercer vector es la suma de los dos primeros, así que sobra. Los dos primeros son independientes, porque ninguno es múltiplo del otro. La dimensión es 2.",
 "verificacion":{"formula":"2+0*x","a":0,"esperado":2},
 "pistas":["Mira si alguno de los vectores se puede armar con los otros.","Suma los dos primeros.","Cuenta cuántos vectores independientes quedan."],
 "errores":["","Son tres vectores, pero el tercero es la suma de los dos primeros, así que no aporta una dirección nueva.","Los dos primeros no son múltiplos entre sí, así que hay al menos dos direcciones.","El gen de vectores que no son cero tiene dimensión al menos 1."]}
res=["Unos vectores son independientes si ninguno es combinación de los otros.","Una base es un conjunto independiente que genera el espacio, y las coordenadas son los pesos de la combinación.","La dimensión es el número de vectores de una base. En R n no hay más de n vectores independientes."]
write(lesson("alglin-m2-l1","Lección 1 de 4","Independencia lineal, base y dimensión",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-indep.json")
