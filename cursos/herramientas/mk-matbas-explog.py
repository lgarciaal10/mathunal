import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 2 Ecuaciones, inecuaciones y sistemas"
TS=[-4.2+8.4*k/100 for k in range(101)]
graf={"tipo":"plano","x":[-4.5,4.5],"y":[-1,9],"a":0.125,"b":8,"inicio":2,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"exp({t:.4f}*ln(2))"] for t in TS],"c":2},
  {"t":"recta","p":["0","x"],"dir":["1","0"],"guion":True,"c":3,"guia":True},
  {"t":"segmento","a":["0","x"],"b":["ln(x)/ln(2)","x"],"c":3,"guia":True},
  {"t":"punto","p":["ln(x)/ln(2)","x"],"c":1}],
 "lecturas":[{"rotulo":"valor k","formula":"x"},{"rotulo":"x en 2^x=k","formula":"ln(x)/ln(2)"}],
 "etiquetas":["Valor k","Solución de dos elevado a x igual a k"],"etiquetaSlider":"Valor k",
 "alt":"La gráfica de dos elevado a x y una recta horizontal de altura k. El punto donde se cruzan tiene como coordenada x el logaritmo en base 2 de k. Con k igual a 8 es 3 y con k igual a un octavo es menos 3"}
glos={"logaritmo":"El logaritmo en base b de un número es el exponente al que hay que elevar b para obtener ese número. Si b elevado a y es igual a k, entonces y es el logaritmo en base b de k.",
 "exponencial":"Una ecuación exponencial tiene la incógnita en el exponente. Se resuelve igualando bases o usando logaritmos.",
 "propiedades":"Los logaritmos convierten productos en sumas, cocientes en restas y potencias en multiplicaciones por el exponente."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La curva es dos elevado a x. Para resolver dos elevado a x igual a k, se busca dónde la curva llega a la altura k."],
 [4,8,"La recta horizontal es la altura k. El punto de cruce tiene la coordenada x que resuelve la ecuación, y esa coordenada es el logaritmo en base 2 de k."],
 [8,14,"Al subir k, la solución crece despacio. Al bajar k hacia 0, la solución se va hacia números negativos y k nunca llega a valer 0."],
 [14,18,"Con k igual a 8 la solución es 3, porque dos al cubo es 8. Con k igual a un octavo es menos 3."],
 [18,22,"Con k igual a 4 la solución es 2. Si la ecuación es dos elevado a x igual a 4, también se puede igualar bases, porque 4 es 2 al cuadrado."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,2],[8,2],[11,8],[13,0.125],[14,8],[16,8],[17,0.125],[18,4],[22,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("En una ecuación exponencial la incógnita está en el exponente. Para sacarla hay dos caminos. Si se pueden escribir los dos lados con la misma base, se igualan los exponentes. Si no, se aplica un {{gl:logaritmo|logaritmo}}, que es justo la operación que deshace una potencia.")),
 sec("Un ejemplo","Un ejemplo",P("Mira cómo se resuelve dos elevado a x igual a k con una gráfica."),EQ("2^{x}=k\\ \\Longleftrightarrow\\ x=\\log_{2}k"),{"t":"grafica","animar":"dibujar","alt":"La curva dos elevado a x"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La ecuación dos elevado a x igual a 8 se resuelve escribiendo 8 como una potencia de 2. ¿Cuánto vale x?","opciones":[2,3,4,6],"correcta":3,"bien":"Muy bien. Vale 3, porque dos al cubo es 8. Más abajo se ve en la gráfica.","mal":"Vale 3, porque 2 por 2 por 2 es 8. Más abajo se ve en la gráfica."}),
 sec("Cambiando k","Cambiando k",P("Mira cómo cambia la solución al mover la altura k."),{"t":"acercando","ds":[8,4,0.125,2],"alt":"La solución para varios k"},P("El logaritmo crece despacio. Duplicar k solo suma 1 a la solución, porque duplicar es multiplicar por 2.")),
 sec("Ecuaciones exponenciales","Exponenciales",P("Primero se intenta igualar las bases. Si no se puede, se aplica un logaritmo."),
   PASOS([("3^{2x}=27=3^{3}\\ \\Rightarrow\\ 2x=3\\ \\Rightarrow\\ x=1.5","Se escribe 27 como 3 al cubo y se igualan los exponentes."),
          ("2^{x}=\\dfrac{1}{8}=2^{-3}\\ \\Rightarrow\\ x=-3","Una fracción se escribe con un exponente negativo."),
          ("5^{x}=7\\ \\Rightarrow\\ x=\\dfrac{\\ln 7}{\\ln 5}\\approx 1.21","Cuando no se igualan bases, se aplica el logaritmo.")])),
 sec("Logaritmos","Logaritmos",P("Las propiedades de los logaritmos permiten juntar varios en uno solo."),
   PASOS([("\\log_{b}(MN)=\\log_{b}M+\\log_{b}N,\\qquad \\log_{b}\\dfrac{M}{N}=\\log_{b}M-\\log_{b}N","El logaritmo de un producto es una suma y el de un cociente es una resta."),
          ("\\log_{b}M^{n}=n\\log_{b}M","El exponente sale multiplicando."),
          ("\\log_{2}8+\\log_{2}4=3+2=5=\\log_{2}32","Se pueden sumar o juntar. Tienen que tener la misma base.")]),
   OJO("El logaritmo solo existe para números positivos. Al resolver una ecuación logarítmica hay que comprobar que las soluciones no dejen un logaritmo de un número negativo o de cero.")),
 sec("Ecuaciones logarítmicas","Logarítmicas",P("Una ecuación logarítmica se resuelve pasando a la forma exponencial."),
   PASOS([("\\log_{3}(x-1)=2\\ \\Rightarrow\\ x-1=3^{2}=9","La definición del logaritmo."),
          ("x=10","Se despeja x."),
          ("\\log_{3}(10-1)=\\log_{3}9=2\\ \\checkmark","Se comprueba que x menos 1 es positivo y que da 2.")])),
 eng("La escala de decibelios","El oído percibe sonidos de intensidades muy distintas, y por eso se miden con una escala logarítmica. El nivel en decibelios es diez veces el logaritmo en base 10 del cociente entre la intensidad y una referencia.","L=10\\log_{10}\\dfrac{I}{I_{0}}",
   [("Conversación","60 dB"),("Un taladro","90 dB"),("Cociente de intensidades","mil veces")],"La diferencia entre 60 y 90 decibelios son 30 decibelios, que corresponden a un cambio de 10 elevado a 3 en la intensidad, o sea mil veces. Cada 10 decibelios multiplican la intensidad por 10. Es un modelo de la intensidad física, y no mide cuán molesto resulta el ruido para una persona."),
 completar("Se resuelve una ecuación logarítmica pasando a la forma exponencial.","\\log_{3}(x-1)=2\\ \\Rightarrow\\ x-1=[[hueco]]",
   [("9","3 al cuadrado"),("6","3 por 2"),("2","dos")],0,
   ["","Eso sería multiplicar la base por el resultado. El logaritmo es un exponente, y se eleva la base a ese valor.","Con 2 se estaría olvidando la base. La forma exponencial es la base elevada al resultado."],"El logaritmo es el exponente al que se eleva la base.","3 al cuadrado es 9."),
 error("Alguien resolvió una ecuación y se equivocó en un paso. Toca el paso que está mal.",
   [("3^{2x}=27","La ecuación.","la ecuación es tres a la 2x igual a 27"),
    ("3^{2x}=3^{3}","Se escribe 27 como potencia de 3.","27 es 3 al cubo"),
    ("2x=3^{3}=27\\ \\Rightarrow\\ x=13.5","Este paso es el que falla.","se iguala 2x a 27")],2,
   "Cuando las bases son iguales se igualan los exponentes, que son 2x y 3. No hay que elevar otra vez 3 al cubo. Queda 2x igual a 3, y x vale 1.5.",
   "2x=3\\ \\Rightarrow\\ x=1.5","Compara solo los exponentes."),
 ordenar("Estos son los pasos para resolver 5 elevado a x igual a 7, pero están desordenados.",
   [("5^{x}=7","La ecuación"),
    ("\\ln\\left(5^{x}\\right)=\\ln 7","Se aplica el logaritmo natural"),
    ("x\\ln 5=\\ln 7","El exponente sale multiplicando"),
    ("x=\\dfrac{\\ln 7}{\\ln 5}","Se despeja x")],[2,0,3,1],
   "Se aplica el logaritmo a los dos lados, el exponente baja y se despeja.","Se empieza con la ecuación."),
]
S+=cierre("Mini simulacro de ecuaciones exponenciales y logarítmicas",[
 banco("mb_c2_08","Se escribe $27=3^{3}$, se igualan los exponentes $2x=3$ y queda $x=1.5$."),
 banco("mb_c2_09","Se pasa a forma exponencial, $x-1=3^{2}=9$, así que $x=10$."),
 banco("mb_c2_10","Se calcula $\\log_{2}8=3$ y $\\log_{2}4=2$, y la suma es $5$.")])
prac=[
 {"titulo":"La curva","grafica":{"draw":1,"guide":1},"bloques":[P("La curva de dos elevado a x y una recta de altura k."),EQ("2^{x}=k")]},
 {"titulo":"Cambia k","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee la solución de la ecuación, el logaritmo en base 2 de k.")]},
 {"titulo":"Un valor exacto","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":8,"bloques":[EQ("2^{x}=8\\ \\Rightarrow\\ x=3"),P("Con k igual a 8 la solución es 3.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":8},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Escribe cada lado como potencia de la misma base."}]}]
preg={"tex":"2^{x}=\\dfrac{1}{16}\\ \\text{tiene como solución}\\ x=","opciones":["$-4$","$4$","$-8$","$\\tfrac{1}{4}$"],"correcta":0,
 "explicacion":"Un dieciseisavo es 2 a la menos 4. Con las bases iguales se igualan los exponentes, y x vale menos 4.",
 "verificacion":{"formula":"exp((0-4)*ln(2))-1/16+0*x","a":0,"esperado":0},
 "pistas":["Escribe 16 como potencia de 2.","Un dieciseisavo es 2 elevado a un exponente negativo.","Iguala los exponentes."],
 "errores":["","Con 4 positivo da 16, y no un dieciseisavo. El exponente debe ser negativo.","Con menos 8 daría uno sobre 256. Se necesita 2 a la 4 en el denominador, no a la 8.","Esa es la raíz cuarta de la base. La incógnita está en el exponente, y no se resuelve así."]}
res=["Si se pueden escribir los dos lados con la misma base, se igualan los exponentes.","Si no, se aplica un logaritmo y el exponente baja multiplicando.","Una ecuación logarítmica se pasa a la forma exponencial, y se comprueba que el argumento sea positivo."]
write(lesson("mb-m2-l1","Lección 1 de 5","Ecuaciones exponenciales y logarítmicas",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=7,curso="Matemáticas Básicas"),"matbas-explog.json")
