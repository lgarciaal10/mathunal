import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 3 Laplace, sistemas y series"
PT=[["0","0"]]+[[f"{6*k/60:.4f}",f"exp(0-(x-1)*{6*k/60:.4f})"] for k in range(61)]+[["6","0"]]
CV=[[f"{6*k/60:.4f}",f"exp(0-(x-1)*{6*k/60:.4f})"] for k in range(61)]
graf={"tipo":"plano","x":[-0.6,6.4],"y":[-0.4,3.4],"a":1.5,"b":4,"inicio":2,
 "elementos":[{"t":"poligono","puntos":PT,"c":0},{"t":"trazo","puntos":CV,"c":2}],
 "lecturas":[{"rotulo":"s","formula":"x"},{"rotulo":"área F(s)","formula":"1/(x-1)"}],
 "etiquetas":["Valor de s","Área bajo la curva"],"etiquetaSlider":"Valor de s",
 "alt":"La curva e a la menos (s menos 1) t, que es e a la t por e a la menos s t, con el área bajo ella sombreada. El área es la transformada de Laplace de e a la t evaluada en s"}
glos={"laplace":"La transformada de Laplace de una función f de t es la integral de 0 a infinito de e a la menos s t por f de t. Convierte la función en otra que depende de s.",
 "pvi":"Un problema de valor inicial es una ecuación diferencial junto con los valores iniciales de la solución y sus derivadas.",
 "tabla":"La tabla de transformadas reúne las transformadas de las funciones más comunes, para no calcular la integral cada vez."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"Se transforma la función e a la t. Se multiplica por e a la menos s t, que la va apagando."],
 [3,7,"La curva que queda, e a la menos (s menos 1) t, empieza en 1 y baja hacia 0."],
 [7,13,"La transformada de Laplace es el área bajo esa curva, de 0 a infinito."],
 [13,18,"Con s más grande, la curva baja más rápido y el área es menor. El área es 1 sobre s menos 1."],
 [18,22,"Con s igual a 2 el área es 1. La transformada de e a la t es 1 sobre s menos 1."]],
 "canales":{"draw":[[0.3,0],[6.5,1]],"d":[[7,2],[10,1.3],[13,3.5],[16,2],[22,2]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("La {{gl:laplace|transformada de Laplace}} cambia una función de t por otra función de s. Su gran ventaja es que convierte derivadas en multiplicaciones, y así una ecuación diferencial se vuelve una ecuación algebraica. Se resuelve el álgebra y se regresa. Es la herramienta principal de la ingeniería de control y de los circuitos.")),
 sec("Un ejemplo","Un ejemplo",P("Mira cómo se calcula la transformada de e a la t."),EQ("\\mathcal{L}\\{e^{t}\\}=\\int_{0}^{\\infty}e^{-st}\\,e^{t}\\,dt=\\int_{0}^{\\infty}e^{-(s-1)t}\\,dt"),{"t":"grafica","animar":"dibujar","alt":"La curva que se integra y su área"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con s igual a 2, la curva es e a la menos t. ¿Cuánto vale en t igual a 0?","opciones":[0,0.5,1,2],"correcta":1,"bien":"Muy bien. Vale 1, porque e a la 0 es 1. Más abajo se ve el área.","mal":"Vale 1, porque e a la 0 es 1. Más abajo se ve el área."}),
 sec("El área","El área",P("Mira cómo cambia el área al subir s."),{"t":"acercando","ds":[1.3,2,3.5],"alt":"El área bajo la curva para varios valores de s"},P("Con s igual a 2 el área vale <b>1</b>. En general vale 1 sobre s menos 1, siempre que s sea mayor que 1.")),
 sec("Calcular la integral","Calcular",PASOS([("\\int_{0}^{\\infty}e^{-(s-1)t}\\,dt=\\lim_{T\\to\\infty}\\left[\\dfrac{-e^{-(s-1)t}}{s-1}\\right]_{0}^{T}","Es una integral impropia."),
          ("=\\dfrac{1}{s-1}\\quad (s>1)","Si s es mayor que 1 el límite es 0, y queda el término de t igual a 0.")]),
   OJO("Si s es menor o igual que 1 la integral diverge y la transformada no existe.")),
 sec("Tabla básica","Tabla",P("Estas son las transformadas que más se usan. Con ellas casi no hace falta integrar."),
   PASOS([("\\mathcal{L}\\{1\\}=\\dfrac{1}{s},\\qquad \\mathcal{L}\\{t\\}=\\dfrac{1}{s^{2}}","La constante y la rampa."),
          ("\\mathcal{L}\\{e^{at}\\}=\\dfrac{1}{s-a}","La exponencial, que es el ejemplo de la lección."),
          ("\\mathcal{L}\\{\\operatorname{sen}\\omega t\\}=\\dfrac{\\omega}{s^{2}+\\omega^{2}},\\quad \\mathcal{L}\\{\\cos\\omega t\\}=\\dfrac{s}{s^{2}+\\omega^{2}}","Las oscilaciones."),
          ("\\mathcal{L}\\{f'\\}=sF(s)-f(0)","La derivada se vuelve una multiplicación.")])),
 sec("Resolver una EDO","Resolver una EDO",P("Se transforma toda la ecuación y se despeja la transformada de la solución."),
   PASOS([("y'+y=1,\\quad y(0)=0","La ecuación del condensador con fuente de 1."),
          ("sY-0+Y=\\dfrac{1}{s}\\ \\Rightarrow\\ Y=\\dfrac{1}{s(s+1)}","Se transforma y se despeja Y."),
          ("Y=\\dfrac{1}{s}-\\dfrac{1}{s+1}\\ \\Rightarrow\\ y=1-e^{-t}","Se parte en fracciones parciales y se regresa con la tabla.")])),
 eng("La respuesta de un circuito","En un circuito RC con una fuente que se enciende en t igual a 0, la transformada de Laplace da el voltaje del condensador con puro álgebra. Se multiplica una función de transferencia por la transformada de la entrada.","V_{c}(s)=\\dfrac{1}{RCs+1}\\cdot\\dfrac{V}{s}",
   [("Fuente","12 V"),("RC","1 s"),("Voltaje a los 2 s","10.4 V")],"Con RC igual a 1, el voltaje es 12 sobre s por (s más 1), que se parte en 12 sobre s menos 12 sobre s más 1. Al regresar queda 12 por (1 menos e a la menos t), igual al resultado de la EDO. A los 2 segundos vale 10.4 voltios. Es un modelo simplificado, porque supone componentes ideales."),
 completar("Se transforma y prima más y igual a 1 con y de 0 igual a 0.","sY(s)+Y(s)=[[hueco]]",
   [("\\dfrac{1}{s}","uno sobre s"),("1","uno"),("s","s")],0,
   ["","La transformada de la constante 1 es 1 sobre s, no 1.","Esa es la variable, no la transformada de 1. La transformada de 1 es 1 sobre s."],"Usa la tabla para la transformada de 1.","La transformada de la constante 1 es 1 sobre s."),
 error("Alguien transformó una derivada y se equivocó en un paso. Toca el paso que está mal.",
   [("y'+2y=0,\\quad y(0)=3","Es el problema.","y prima más 2y igual a 0 con y de 0 igual a 3"),
    ("sY(s)+2Y(s)=0","Este paso es el que falla.","s Y más 2 Y es igual a 0"),
    ("Y(s)=0","Depende del paso anterior.","Entonces Y es igual a 0")],1,
   "Falta el valor inicial. La transformada de y prima es s Y menos y de 0. Queda s Y menos 3 más 2 Y igual a 0, y Y es 3 sobre s más 2.",
   "sY-3+2Y=0\\ \\Rightarrow\\ Y=\\dfrac{3}{s+2}\\ \\Rightarrow\\ y=3e^{-2t}","Revisa la regla de la derivada, que lleva el valor inicial."),
 ordenar("Estos son los pasos para resolver y prima más y igual a 1 con y de 0 igual a 0 usando Laplace, pero están desordenados.",
   [("sY+Y=\\dfrac{1}{s}","Se transforma la ecuación"),
    ("Y=\\dfrac{1}{s(s+1)}","Se despeja Y"),
    ("Y=\\dfrac{1}{s}-\\dfrac{1}{s+1}","Se parte en fracciones parciales"),
    ("y=1-e^{-t}","Se regresa con la tabla")],[2,0,3,1],
   "Se transforma, se despeja Y, se parte en fracciones y se regresa.","Se empieza transformando la ecuación."),
]
S+=cierre("Mini simulacro de transformadas",[banco("ed_c3_06","Es la transformada de una constante."),banco("ed_c3_08","$\\frac{1}{2^2}=0.25$."),banco("ed_c3_10","Es la transformada del seno.")])
prac=[
 {"titulo":"El área","grafica":{"draw":1},"bloques":[P("La transformada es el área bajo la curva."),EQ("\\mathcal{L}\\{e^{t}\\}(s)=\\int_{0}^{\\infty}e^{-(s-1)t}\\,dt")]},
 {"titulo":"Cambia s","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Con s grande la curva baja rápido y el área es pequeña. Abajo se ven s y el área.")]},
 {"titulo":"El resultado","grafica":{"draw":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("\\mathcal{L}\\{e^{t}\\}=\\dfrac{1}{s-1}"),P("Con s igual a 2 el área es 1, que es 1 sobre 2 menos 1.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Usa la tabla y recuerda la regla de la derivada."}]}]
preg={"tex":"\\mathcal{L}\\{e^{3t}\\}\\ \\text{en}\\ s=5","opciones":["$0.5$","$0.2$","$2$","$0.125$"],"correcta":0,
 "explicacion":"La transformada de e a la 3t es 1 sobre s menos 3. En s igual a 5 vale 1 sobre 2, o sea 0.5.",
 "verificacion":{"formula":"1/(5-3)+0*x","a":0,"esperado":0.5},
 "pistas":["Usa la tabla, la transformada de e a la at es 1 sobre s menos a.","Aquí a es 3.","Evalúa 1 sobre s menos 3 en s igual a 5."],
 "errores":["","Ese es 1 sobre 5, que olvida restar a. La transformada es 1 sobre s menos 3.","Ese es el valor de s menos 3, no su inverso.","Ese es 1 sobre 8, que sumó 3 en vez de restar."]}
res=["La transformada de Laplace de f es la integral de e a la menos s t por f, de 0 a infinito.","La tabla da las transformadas de 1, t, e a la at, seno y coseno, y la derivada se vuelve s F menos f de 0.","Con Laplace una EDO se vuelve una ecuación algebraica, que se resuelve y se regresa."]
write(lesson("edo-m3-l1","Lección 1 de 5","Transformada de Laplace",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Ecuaciones Diferenciales"),"edo-laplace.json")
