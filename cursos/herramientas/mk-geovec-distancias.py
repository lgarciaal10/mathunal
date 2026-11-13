import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 3 Rectas, planos y cónicas"
graf={"tipo":"plano","x":[-8.6,8.6],"y":[-3.2,6.2],"a":-2,"b":6,"inicio":0,
 "elementos":[
  {"t":"recta","p":["0","2"],"dir":["1","0"],"c":0},
  {"t":"segmento","a":["1.5","x"],"b":["1.5","2"],"guion":True,"c":3,"guia":True},
  {"t":"punto","p":["1.5","2"],"c":1},
  {"t":"punto","p":["1.5","x"],"c":2}],
 "lecturas":[{"rotulo":"numerador, valor absoluto de 2x más 2y más z menos 6","formula":"3*abs(x-2)"},{"rotulo":"distancia del punto al plano","formula":"abs(x-2)"}],
 "etiquetas":["Es la distancia multiplicada por la longitud de la normal, que vale 3","Longitud del segmento perpendicular al plano"],"etiquetaSlider":"Altura del punto a lo largo de la normal",
 "alt":"Un corte que contiene la normal del plano 2x más 2y más z igual a 6. La normal apunta hacia arriba y el plano es la recta horizontal a altura 2. Un punto se mueve a lo largo de la normal y el segmento vertical punteado marca su distancia al plano"}
glos={"distpunto":"La distancia de un punto a un plano es la longitud del segmento perpendicular. Es el valor absoluto de la ecuación evaluada en el punto, dividido entre la longitud de la normal.",
 "normal":"El vector normal del plano ax más by más cz igual a d es (a, b, c), y su longitud es la raíz de a al cuadrado más b al cuadrado más c al cuadrado.",
 "paralelas":"La distancia entre dos rectas paralelas es la distancia de un punto de una de ellas a la otra.",
 "pie":"El pie de la perpendicular es el punto del plano más cercano al punto dado."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"El plano 2x más 2y más z igual a 6 tiene normal (2, 2, 1), de longitud 3. En este corte la normal apunta hacia arriba y el plano es la recta a altura 2."],
 [4,9,"El punto se mueve a lo largo de la normal. La distancia es el segmento vertical, perpendicular al plano."],
 [9,14,"Con el punto en el origen, a altura 0, la distancia al plano es 2."],
 [14,19,"Con el punto a altura 5, la distancia es 3."],
 [19,22,"La fórmula divide el valor de la ecuación entre la longitud de la normal."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,3],[10,0],[14,0],[15,5],[19,5],[22,5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[14,22]}}
S=[
 sec("La idea",None,P("La {{gl:distpunto|distancia de un punto a un plano}} es la longitud del segmento perpendicular que los une, y el punto donde cae es el {{gl:pie|pie}} de la perpendicular. Se calcula evaluando la ecuación del plano en el punto y dividiendo entre la longitud de la {{gl:normal|normal}}. Con la misma idea se halla la distancia entre planos paralelos y entre {{gl:paralelas|rectas paralelas}}.")),
 sec("Un ejemplo","Un ejemplo",P("Para ver la idea en una hoja, se toma un corte que contiene la normal del plano. El plano aparece como una recta horizontal, y el punto se mueve hacia arriba y hacia abajo."),EQ("d=\\dfrac{|ax_{0}+by_{0}+cz_{0}+d_{0}|}{\\sqrt{a^{2}+b^{2}+c^{2}}}"),{"t":"grafica","animar":"dibujar","alt":"El plano de canto con un punto y su distancia"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La normal del plano 2x más 2y más z igual a 6 es (2, 2, 1). ¿Cuánto vale la raíz de 4 más 4 más 1?","opciones":[2,3,5,9],"correcta":3,"bien":"Muy bien. Vale 3, la longitud de la normal. Más abajo se ve cómo se usa.","mal":"Vale 3, porque 4 más 4 más 1 es 9 y la raíz de 9 es 3. Es la longitud de la normal. Más abajo se ve cómo se usa."}),
 sec("Moviendo el punto","El punto",P("Mira la distancia con el punto a alturas de 0, 3, 5 y menos 2."),{"t":"acercando","ds":[0,3,5,-2],"alt":"El punto a cuatro alturas"},P("La distancia es siempre positiva. Con el punto en altura 2, está sobre el plano y la distancia es cero.")),
 sec("La fórmula","La fórmula",P("Se evalúa la ecuación del plano en el punto y se divide entre la longitud de la normal."),
   PASOS([("d=\\dfrac{|ax_{0}+by_{0}+cz_{0}+d_{0}|}{\\sqrt{a^{2}+b^{2}+c^{2}}}","La fórmula, con el plano escrito como ax más by más cz más d0 igual a cero."),
          ("(1,1,1),\\ x+y+z=0:\\quad \\dfrac{3}{\\sqrt{3}}=1.732","Distancia de un punto a un plano que pasa por el origen."),
          ("(3,0,0),\\ x=0:\\quad \\dfrac{|3|}{1}=3","Con el plano coordenado la cuenta es inmediata."),
          ("(0,0,0),\\ 2x+2y+z-6=0:\\quad \\dfrac{6}{3}=2","La distancia del origen al plano.")])),
 sec("Rectas y planos paralelos","Paralelos",P("La distancia entre objetos paralelos se reduce a la de un punto a un objeto."),
   PASOS([("x+y+z=0\\ \\text{y}\\ x+y+z=3","Dos planos paralelos."),
          ("(0,0,0)\\in\\text{primero}:\\quad d=\\dfrac{3}{\\sqrt{3}}=\\sqrt{3}","Se toma un punto del primero y se mide al segundo."),
          ("\\text{rectas paralelas}\\ \\Rightarrow\\ \\text{punto de una, distancia a la otra}","El mismo método sirve para dos rectas paralelas.")]),
   OJO("El numerador se toma con valor absoluto, porque la distancia no tiene signo. Y el denominador usa los coeficientes de la ecuación, nunca el término independiente.")),
 eng("La altura de un dron sobre una ladera","Un terreno inclinado se describe con el plano 2x más 2y más z igual a 6, con medidas en metros. Un dron está en el punto (3, 2, 5). Su distancia perpendicular al terreno es la que importa para no chocar.","d=\\dfrac{|2\\cdot3+2\\cdot2+5-6|}{\\sqrt{4+4+1}}=\\dfrac{9}{3}=3",
   [("Plano del terreno","2x + 2y + z = 6"),("Posición del dron","(3, 2, 5) m"),("Distancia al terreno","3 m")],"El numerador vale 9 y la normal mide 3, así que el dron está a 3 metros del terreno. Esa distancia es perpendicular a la ladera, y es menor que la altura vertical sobre ella. Por eso un dron que sigue una ladera no debe medir su altura solo con el eje vertical."),
 completar("Se calcula la distancia del punto (0, 0, 5) al plano 2x más 2y más z igual a 0. Falta el radicando.","d=\\dfrac{|0+0+5|}{\\sqrt{[[hueco]]}}",
   [("9","nueve"),("5","cinco"),("3","tres")],0,
   ["","Cinco sale de sumar los coeficientes 2, 2 y 1 sin elevarlos al cuadrado.","Tres es la raíz que ya se saca, y dentro de la raíz va la suma de cuadrados."],"Se suman los cuadrados de los coeficientes.","4 más 4 más 1 es 9, y la raíz es 3."),
 error("Alguien calculó la distancia del punto (0, 0, 5) al plano 2x más 2y más z igual a 0 y se equivocó en un paso. Toca el paso que está mal.",
   [("P=(0,0,5),\\quad 2x+2y+z=0","Los datos.","el punto y el plano"),
    ("|2\\cdot0+2\\cdot0+5|=5","El numerador.","el numerador vale 5"),
    ("d=\\dfrac{5}{\\sqrt{2+2+1}}=\\dfrac{5}{\\sqrt{5}}","Este paso es el que falla.","la distancia es 5 entre raíz de 5")],2,
   "En la raíz van los cuadrados de los coeficientes, o sea 4 más 4 más 1, que da 9. La norma de la normal es 3 y la distancia es 5 sobre 3.",
   "d=\\dfrac{5}{\\sqrt{4+4+1}}=\\dfrac{5}{3}","Eleva al cuadrado cada coeficiente."),
 ordenar("Estos son los pasos para hallar la distancia del origen al plano 2x más 2y más z igual a 6, pero están desordenados.",
   [("2x+2y+z-6=0","Se lleva todo a un lado"),
    ("|2\\cdot0+2\\cdot0+0-6|=6","Se evalúa en el origen"),
    ("\\sqrt{4+4+1}=3","Se calcula la longitud de la normal"),
    ("d=\\dfrac{6}{3}=2","Se divide")],[2,0,3,1],
   "Se escribe el plano igualado a cero, se evalúa en el punto, se calcula la normal y se divide.","Se empieza llevando todo a un lado."),
]
S+=cierre("Mini simulacro de distancias en R³",[
 banco("gv_c3_13","El numerador es el valor absoluto de la ecuación evaluada en el punto, y el denominador es la longitud de la normal."),
 banco("gv_c3_15","$\\dfrac{|{-6}|}{\\sqrt{4+4+1}}=\\dfrac{6}{3}=2$."),
 banco("gv_c3_16","Un punto de una recta se mide a la otra.")])
prac=[
 {"titulo":"El corte","grafica":{"draw":1},"bloques":[P("Un corte con la normal hacia arriba, y el plano como una recta horizontal."),EQ("2x+2y+z=6")]},
 {"titulo":"Mueve el punto","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el numerador y la distancia al plano.")]},
 {"titulo":"A altura 5","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5,"bloques":[EQ("d=|5-2|=3"),P("Con el punto a altura 5, la distancia al plano es 3.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Evalúa la ecuación en el punto y divide entre la longitud de la normal."}]}]
preg={"tex":"\\text{Distancia de}\\ (1,2,2)\\ \\text{al plano}\\ x+2y+2z=0","opciones":["$3$","$9$","$1$","$\\tfrac13$"],"correcta":0,
 "explicacion":"La ecuación evaluada en el punto da 1 más 4 más 4, o sea 9. La longitud de la normal es la raíz de 1 más 4 más 4, que es 3. La distancia es 9 entre 3, o sea 3.",
 "verificacion":{"formula":"abs(1+4+4)/sqrt(1+4+4)+0*x","a":0,"esperado":3},
 "pistas":["Evalúa x más 2y más 2z en el punto.","Da 9. Calcula la longitud de la normal.","Es 3. Divide 9 entre 3."],
 "errores":["","Nueve es solo el numerador. Falta dividir entre la longitud de la normal.","Uno sale de dividir entre la suma de cuadrados y no entre su raíz.","Un tercio invierte el cociente, con la normal arriba."]}
res=["La distancia de un punto a un plano es el valor absoluto de la ecuación evaluada en el punto, entre la longitud de la normal.","La distancia entre planos paralelos se halla con un punto de uno de ellos.","Para dos rectas paralelas se toma un punto de una y se mide su distancia a la otra."]
write(lesson("gv-m3-l2","Lección 2 de 4","Distancias en R³",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-distancias.json")
