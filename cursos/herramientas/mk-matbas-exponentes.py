import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 1 Álgebra y expresiones"
TS=[0.02+4.38*k/100 for k in range(101)]
graf={"tipo":"plano","x":[-0.4,4.6],"y":[-0.6,8.6],"a":0.2,"b":1.5,"inicio":0.5,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"exp(x*ln({t:.4f}))"] for t in TS],"c":2},
  {"t":"recta","p":["4","0"],"dir":["0","1"],"guion":True,"c":3,"guia":True},
  {"t":"punto","p":["4","exp(x*ln(4))"],"c":1}],
 "lecturas":[{"rotulo":"exponente r","formula":"x"},{"rotulo":"4 elevado a r","formula":"exp(x*ln(4))"}],
 "etiquetas":["Exponente r","Valor de 4 elevado a r"],"etiquetaSlider":"Exponente r",
 "alt":"La gráfica de x elevado a r para x positivo, con un punto en x igual a 4. Con r igual a un medio el punto está en 2, que es la raíz cuadrada de 4, y con r igual a 1.5 está en 8"}
glos={"potencia":"Una potencia a elevado a n indica multiplicar a por sí mismo n veces. La base es a y el exponente es n.",
 "radical":"Un radical es una raíz. La raíz n-ésima de un número es el que elevado a n da ese número. Se puede escribir como una potencia con exponente fraccionario.",
 "racionalizar":"Racionalizar es quitar los radicales del denominador de una fracción sin cambiar su valor, multiplicando arriba y abajo por la misma expresión."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La gráfica muestra x elevado a r, para x positivo. Con r igual a un medio, esta es la curva de la raíz cuadrada."],
 [4,8,"En x igual a 4 el punto vale 2, porque 4 elevado a un medio es la raíz cuadrada de 4. Un exponente fraccionario es una raíz."],
 [8,14,"Al subir r, la curva se vuelve más empinada. Con r igual a 1 es la recta y igual a x, y con r mayor que 1 es una curva que sube cada vez más rápido."],
 [14,18,"Con r igual a 1.5 el punto vale 8. Eso es 4 elevado a 3 sobre 2, o sea la raíz de 4, elevada al cubo."],
 [18,22,"Con r igual a un tercio, el punto vale 1.58. Es la raíz cúbica de 4."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.5],[8,0.5],[11,1],[14,1.5],[16,1.5],[17,0.33],[22,0.33]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Las {{gl:potencia|potencias}} y los {{gl:radical|radicales}} son dos formas de escribir lo mismo. Una raíz es una potencia con exponente fraccionario. Con unas pocas leyes de exponentes se puede simplificar casi cualquier expresión, y con la {{gl:racionalizar|racionalización}} se quitan las raíces de los denominadores.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la gráfica de x elevado a r y el punto de x igual a 4."),EQ("4^{r}\\quad\\text{para}\\quad r=\\tfrac{1}{2},\\ 1,\\ \\tfrac{3}{2}"),{"t":"grafica","animar":"dibujar","alt":"La gráfica de x elevado a r"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Al multiplicar potencias de la misma base se suman los exponentes. En x a la 5 por x a la menos 2, ¿qué exponente queda?","opciones":[3,7,-10,-3],"correcta":3,"bien":"Muy bien. Queda x a la 3. Más abajo se ven las demás leyes.","mal":"Queda x a la 3, porque 5 más menos 2 es 3. Más abajo se ven las demás leyes."}),
 sec("Cambiando el exponente","El exponente",P("Mira cómo cambia el valor en x igual a 4 al variar el exponente."),{"t":"acercando","ds":[0.5,1,1.5,0.33],"alt":"El valor de 4 elevado a r para varios r"},P("Con r igual a un medio da 2, la raíz cuadrada. Con r igual a un tercio da la raíz cúbica de 4, unos 1.58.")),
 sec("Las leyes de exponentes","Leyes",P("Estas son las leyes que se usan en casi todos los ejercicios."),
   PASOS([("a^{m}\\cdot a^{n}=a^{m+n},\\qquad \\dfrac{a^{m}}{a^{n}}=a^{m-n}","Para multiplicar se suman los exponentes y para dividir se restan."),
          ("\\left(a^{m}\\right)^{n}=a^{mn},\\qquad (ab)^{n}=a^{n}b^{n}","Una potencia de una potencia multiplica los exponentes."),
          ("a^{-n}=\\dfrac{1}{a^{n}},\\qquad a^{0}=1\\ \\ (a\\ne 0)","El exponente negativo invierte, y el exponente cero da 1."),
          ("\\sqrt[n]{a^{m}}=a^{m/n}","Una raíz es un exponente fraccionario.")]),
   OJO("Al restar exponentes hay que cuidar el signo. Si el exponente de abajo es negativo, restar un negativo es sumar.")),
 sec("Radicales","Radicales",P("Con el exponente fraccionario, simplificar un radical es simplificar una potencia."),
   PASOS([("\\sqrt[3]{27x^{6}}=\\left(27x^{6}\\right)^{1/3}","Se escribe como potencia."),
          ("=27^{1/3}\\,x^{6/3}","Cada factor se eleva a un tercio."),
          ("=3x^{2}","La raíz cúbica de 27 es 3 y 6 sobre 3 es 2.")]),
   OJO("La raíz cuadrada de x al cuadrado es el valor absoluto de x, no simplemente x. Solo es x cuando se sabe que x es positivo.")),
 sec("Racionalizar","Racionalizar",P("Si hay una raíz en el denominador, se multiplica arriba y abajo por una expresión que la quite."),
   PASOS([("\\dfrac{6}{\\sqrt{3}}=\\dfrac{6}{\\sqrt{3}}\\cdot\\dfrac{\\sqrt{3}}{\\sqrt{3}}=\\dfrac{6\\sqrt{3}}{3}=2\\sqrt{3}","Con una sola raíz, se multiplica por esa misma raíz."),
          ("\\dfrac{2}{\\sqrt{5}-\\sqrt{3}}\\cdot\\dfrac{\\sqrt{5}+\\sqrt{3}}{\\sqrt{5}+\\sqrt{3}}=\\dfrac{2(\\sqrt{5}+\\sqrt{3})}{5-3}=\\sqrt{5}+\\sqrt{3}","Con una resta de raíces, se multiplica por el conjugado, y abajo queda una diferencia de cuadrados.")])),
 eng("El caudal por un orificio","El caudal que sale por un orificio en un tanque no es proporcional a la presión, sino a su raíz cuadrada. Con exponente fraccionario se ve directo.","Q=C_{d}\\,A\\,\\sqrt{\\dfrac{2\\,\\Delta P}{\\rho}}",
   [("Presión","50 kPa"),("Área","1 cm²"),("Coeficiente","0.6")],"Con agua de densidad 1000 kilogramos por metro cúbico, la velocidad es la raíz de 100, o sea 10 metros por segundo, y el caudal es 0.6 litros por segundo. Si la presión se multiplica por 4, el caudal se multiplica por la raíz de 4, o sea 2, y llega a 1.2 litros por segundo. Es una fórmula simplificada, porque supone un fluido ideal y un coeficiente constante."),
 completar("Se simplifica una potencia de una potencia.","\\left(x^{3}\\right)^{2}=x^{[[hueco]]}",
   [("6","seis"),("5","cinco"),("9","nueve")],0,
   ["","Sumar los exponentes es la regla del producto. Aquí hay una potencia de una potencia.","Elevar el exponente a la potencia 2 sería 3 al cuadrado, y no es lo que pide la regla."],"En una potencia de una potencia se multiplican los exponentes.","3 por 2 es 6."),
 error("Alguien simplificó una expresión con exponentes y se equivocó en un paso. Toca el paso que está mal.",
   [("x^{5}\\cdot x^{-2}=x^{3}","Se suman los exponentes.","se suman los exponentes y queda x a la 3"),
    ("\\dfrac{x^{3}}{x^{-3}}=x^{3-3}","Este paso es el que falla.","se restan los exponentes y queda x a la 3 menos 3"),
    ("=x^{0}=1","El resultado final.","queda x a la 0, que es 1")],1,
   "Al restar exponentes hay que restar el negativo, que es sumar. El exponente es 3 menos menos 3, o sea 6, y el resultado es x a la 6.",
   "\\dfrac{x^{3}}{x^{-3}}=x^{3-(-3)}=x^{6}","Cuida el signo del exponente de abajo."),
 ordenar("Estos son los pasos para racionalizar 6 sobre raíz de 3, pero están desordenados.",
   [("\\dfrac{6}{\\sqrt{3}}","La expresión original"),
    ("\\dfrac{6}{\\sqrt{3}}\\cdot\\dfrac{\\sqrt{3}}{\\sqrt{3}}","Se multiplica por raíz de 3 sobre raíz de 3"),
    ("\\dfrac{6\\sqrt{3}}{3}","Se multiplican las raíces de abajo"),
    ("2\\sqrt{3}","Se simplifica")],[2,0,3,1],
   "Se multiplica arriba y abajo por la misma raíz, abajo queda un número y se simplifica.","Se empieza con la expresión original."),
]
S+=cierre("Mini simulacro de exponentes y radicales",[
 banco("mb_c1_02","La raíz cúbica de $27$ es $3$ y la de $x^{6}$ es $x^{2}$, porque se dividen los exponentes entre $3$."),
 banco("mb_c1_03","Se calcula $2^{-1}+3^{-1}=\\tfrac{5}{6}$ y su inverso es $\\tfrac{6}{5}=1.2$."),
 banco("mb_c1_04","Se multiplica arriba y abajo por $\\sqrt{3}$ y queda $\\dfrac{6\\sqrt{3}}{3}=2\\sqrt{3}$.")])
prac=[
 {"titulo":"La gráfica","grafica":{"draw":1,"guide":1},"bloques":[P("La curva de x elevado a r, con un punto en x igual a 4."),EQ("y=x^{r}")]},
 {"titulo":"Cambia r","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee cuánto vale 4 elevado a r.")]},
 {"titulo":"Una raíz","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.5,"bloques":[EQ("4^{1/2}=\\sqrt{4}=2"),P("Con r igual a un medio el punto vale 2.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Escribe la raíz como un exponente fraccionario."}]}]
preg={"tex":"\\sqrt[3]{8x^{6}}\\ \\text{(con}\\ x>0\\text{) es igual a}","opciones":["$2x^{2}$","$2x^{3}$","$4x^{2}$","$8x^{2}$"],"correcta":0,
 "explicacion":"La raíz cúbica de 8 es 2 y la raíz cúbica de x a la 6 es x a la 6 sobre 3, o sea x al cuadrado. El resultado es 2 por x al cuadrado.",
 "verificacion":{"formula":"exp(ln(8*x^6)/3)-2*x^2","a":1.5,"esperado":0},
 "pistas":["Escribe la raíz cúbica como exponente un tercio.","Cada factor se eleva a un tercio.","El exponente de x queda 6 sobre 3."],
 "errores":["","Con la raíz cúbica el exponente de x es 6 sobre 3, o sea 2, y no 3.","La raíz cúbica de 8 es 2, no 4. Se pregunta qué número al cubo da 8.","Falta sacar la raíz cúbica de 8. Ese factor también se eleva a un tercio."]}
res=["Una raíz es un exponente fraccionario, y la raíz n-ésima de a a la m es a a la m sobre n.","Al multiplicar potencias de la misma base se suman los exponentes, al dividir se restan, y en una potencia de una potencia se multiplican.","Para racionalizar se multiplica arriba y abajo por la raíz o por el conjugado."]
write(lesson("mb-m1-l1","Lección 1 de 4","Exponentes y radicales",25,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Básicas"),"matbas-exponentes.json")
