import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 2 Integrales múltiples"
XS=[round(0.05*i,3) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(xv),f"{xv*xv:.4f}"] for xv in XS],"c":3},
    {"t":"segmento","a":["x","0"],"b":["x","x*x"],"c":3},
    {"t":"segmento","a":["0","0"],"b":["x","0"],"c":3},
    {"t":"punto","p":["0.75*x","0.3*x*x"],"c":0}]
graf={"tipo":"plano","x":[-0.3,2.5],"y":[-0.4,4.4],"a":0.5,"b":2,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"masa de la lámina de densidad 1, a al cubo sobre 3","formula":"x*x*x/3"},{"rotulo":"coordenada x del centroide, 3 a sobre 4","formula":"0.75*x"}],
 "etiquetas":["La lámina está entre la curva y igual a x al cuadrado, el eje x y la recta x igual a a","El punto naranja es el centroide, donde se equilibra la lámina"],"etiquetaSlider":"Extremo a, de 0.5 a 2",
 "alt":"Una lámina plana limitada por la parábola y igual a x al cuadrado, el eje x y la recta vertical x igual a a. Su masa con densidad 1 es a al cubo sobre 3, y su centroide está en 3a sobre 4 y 3a al cuadrado sobre 10. Al crecer a la lámina crece y el centroide se desplaza hacia la derecha y hacia arriba"}
glos={"masa":"La masa de una lámina es la integral doble de la densidad sobre la región, y con densidad 1 es el área.",
 "centroide":"El centro de masa tiene por coordenadas los momentos divididos entre la masa, x barra igual a M sub y entre m.",
 "momento":"El momento M sub y es la integral de x por la densidad, y M sub x es la integral de y por la densidad.",
 "inercia":"El momento de inercia mide la resistencia a girar. Respecto al eje z es la integral de x al cuadrado más y al cuadrado por la densidad."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Una lámina está bajo la parábola y igual a x al cuadrado, entre 0 y a, con densidad 1."],
 [4,10,"La masa es la integral doble de la densidad, o sea el área, que vale a al cubo entre 3."],
 [10,16,"Con a igual a 1 la masa es un tercio, y el centroide está en 0.75 y 0.3."],
 [16,20,"Con a igual a 2 la masa es 2.67, y el centroide está en 1.5 y 1.2."],
 [20,24,"El centroide es el punto de equilibrio, y se calcula con los momentos entre la masa."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.6],[8,0.6],[10,1],[13,1],[16,2],[18,2],[24,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Las integrales dobles calculan la {{gl:masa|masa}} de una lámina cuando se integra la densidad. Con los {{gl:momento|momentos}} se halla el {{gl:centroide|centro de masa}}, y con el cuadrado de la distancia al eje, el momento de {{gl:inercia|inercia}}. Son las aplicaciones más comunes de las integrales múltiples en ingeniería.")),
 sec("Un ejemplo","Un ejemplo",P("La lámina está bajo y igual a x al cuadrado, de 0 a a. Cambia a y mira la masa y el centroide."),EQ("m=\\displaystyle\\int_{0}^{a}\\!\\int_{0}^{x^{2}}dy\\,dx=\\dfrac{a^{3}}{3},\\qquad \\bar{x}=\\dfrac{M_{y}}{m}=\\dfrac{3a}{4}"),{"t":"grafica","animar":"dibujar","alt":"La lámina bajo la parábola y su centroide"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Una lámina de densidad 1 sobre el rectángulo de 2 por 3. ¿Cuál es su masa?","opciones":[6,5,3,2],"correcta":6,"bien":"Muy bien. Con densidad 1, la masa es el área, 2 por 3.","mal":"Con densidad 1 la masa es el área, o sea 2 por 3, que da 6."}),
 sec("Distintos extremos","Extremos",P("Mira la lámina con a igual a 0.6, 1, 1.5 y 2."),{"t":"acercando","ds":[0.6,1,1.5,2],"alt":"La lámina con cuatro valores de a"},P("La coordenada x del centroide está siempre a 3 cuartos de la distancia del origen al extremo, o sea a un cuarto de a antes del extremo.")),
 sec("Masa y centroide","Cálculo",P("Primero la masa, luego los momentos."),
   PASOS([("m=\\displaystyle\\int_{0}^{a}\\!\\int_{0}^{x^{2}}dy\\,dx=\\int_{0}^{a}x^{2}\\,dx=\\dfrac{a^{3}}{3}","La masa, con densidad 1."),
          ("M_{y}=\\displaystyle\\int_{0}^{a}\\!\\int_{0}^{x^{2}}x\\,dy\\,dx=\\int_{0}^{a}x^{3}\\,dx=\\dfrac{a^{4}}{4}","El momento respecto al eje y."),
          ("\\bar{x}=\\dfrac{a^{4}/4}{a^{3}/3}=\\dfrac{3a}{4}","La coordenada x del centroide."),
          ("M_{x}=\\displaystyle\\int_{0}^{a}\\dfrac{x^{4}}{2}\\,dx=\\dfrac{a^{5}}{10}\\ \\Rightarrow\\ \\bar{y}=\\dfrac{3a^{2}}{10}","La coordenada y.")]),
   OJO("El momento M sub y se calcula con x, y da la coordenada x barra. El momento M sub x se calcula con y. Es fácil confundir los nombres.")),
 sec("El momento de inercia","Inercia",P("La inercia pesa más los puntos que están lejos del eje."),
   PASOS([("I_{z}=\\displaystyle\\iint_{D}(x^{2}+y^{2})\\,\\rho\\,dA","Momento de inercia respecto al eje z."),
          ("D:\\ 0\\le x\\le1,\\ 0\\le y\\le1,\\ \\rho=1","Un cuadrado de lado 1."),
          ("I_{z}=\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{1}(x^{2}+y^{2})\\,dy\\,dx=\\dfrac{1}{3}+\\dfrac{1}{3}","Cada término da un tercio."),
          ("I_{z}=\\dfrac{2}{3}","El resultado.")]),
   OJO("La inercia depende del eje respecto al cual se mide. El mismo cuerpo tiene inercias distintas respecto a ejes distintos.")),
 eng("El centro de gravedad de una pieza","Una pieza plana de aluminio, con densidad constante, tiene forma de la región bajo una parábola. Para sostenerla en equilibrio se necesita saber dónde está su centro de masa.","\\bar{x}=\\dfrac{3a}{4},\\qquad \\bar{y}=\\dfrac{3a^{2}}{10}",
   [("a","0.2 m"),("Centro en x","0.15 m"),("Centro en y","0.012 m")],"El punto de apoyo ideal es el centroide. Con una densidad que varía, se calcula con la densidad dentro de las integrales, y el centro cambia de lugar."),
 completar("La masa de una lámina con densidad rho es la integral doble de [[hueco]] sobre la región.","m=\\displaystyle\\iint_{D}[[hueco]]\\,dA",
   [("\\rho(x,y)","la densidad"),("x\\,\\rho","x por la densidad"),("x^{2}+y^{2}","x al cuadrado más y al cuadrado")],0,
   ["","Eso es el integrando del momento respecto al eje y, y no el de la masa.","Eso es el integrando de la inercia, y no el de la masa."],"La masa es la suma de la densidad en cada pedazo.","Es la densidad."),
 error("Alguien calculó el centroide de una lámina y se equivocó. Toca el paso que está mal.",
   [("m=\\dfrac{a^{3}}{3},\\quad M_{y}=\\dfrac{a^{4}}{4}","Masa y momento.","masa y momento"),
    ("\\bar{x}=\\dfrac{m}{M_{y}}","Este paso es el que falla.","invierte el cociente"),
    ("\\bar{x}=\\dfrac{4}{3a}","Resultado.","4 sobre 3a")],1,
   "El centroide es el momento dividido entre la masa, y no al revés. Entonces x barra es a a la cuarta sobre 4, entre a al cubo sobre 3, o sea 3a sobre 4.",
   "\\bar{x}=\\dfrac{M_{y}}{m}=\\dfrac{3a}{4}","El momento va arriba y la masa abajo."),
 ordenar("Estos son los pasos para hallar el centroide de una lámina, pero están desordenados.",
   [("m=\\iint\\rho\\,dA","Se calcula la masa"),
    ("M_{y}=\\iint x\\rho\\,dA,\\ M_{x}=\\iint y\\rho\\,dA","Se calculan los momentos"),
    ("\\bar{x}=\\dfrac{M_{y}}{m},\\ \\bar{y}=\\dfrac{M_{x}}{m}","Se divide"),
    ("(\\bar{x},\\bar{y})","Se escribe el centroide")],[2,0,3,1],
   "Primero la masa, luego los momentos, después los cocientes y por último el punto.","Se empieza con la masa."),
]
S+=cierre("Mini simulacro de aplicaciones de integrales dobles",[
 banco("cv_c2_15","La masa de una lámina de densidad 1 sobre un rectángulo."),
 pnum("La masa de una lámina de densidad $\\rho=x$ sobre el cuadrado $[0,1]\\times[0,1]$ es:","0.5",0.01,"La integral de x sobre el cuadrado es un medio."),
 pnum("La masa de la lámina bajo $y=x^{2}$ entre 0 y $a=2$, con densidad 1, en decimales con 3 cifras, es:","2.667",0.002,"Es a al cubo entre 3, o sea 8 tercios, cerca de 2.667.")])
prac=[
 {"titulo":"La lámina","grafica":{"draw":1},"bloques":[P("Se estudia la lámina bajo la parábola."),EQ("0\\le y\\le x^{2},\\quad 0\\le x\\le a")]},
 {"titulo":"Cambia a","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la masa y la coordenada x del centroide.")]},
 {"titulo":"Con a igual a 2","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("m=\\tfrac{8}{3},\\quad \\bar{x}=1.5"),P("Con a igual a 2 la masa es 2.67 y el centroide está en 1.5.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El centroide es el momento entre la masa."}]}]
preg={"tex":"\\text{La masa con densidad 1 sobre }[0,2]\\times[0,3]\\text{ es}","opciones":["$6$","$5$","$3$","$12$"],"correcta":0,
 "explicacion":"Con densidad 1 la masa es el área del rectángulo, 2 por 3, o sea 6.",
 "verificacion":{"formula":"2*3+0*x","a":0,"esperado":6},
 "pistas":["Con densidad 1, la masa es el área.","El área es base por altura.","2 por 3."],
 "errores":["","El 5 es la suma de los lados.","El 3 es solo uno de los lados.","El 12 sería con un factor 2 de más."]}
res=["La masa es la integral de la densidad, y el centroide es el momento entre la masa.","El momento M sub y usa x, y el M sub x usa y.","La inercia pesa más los puntos lejos del eje."]
write(lesson("cv-m2-l6","Lección 6 de 6","Aplicaciones de las integrales múltiples",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-aplic.json")
