import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 2 Integrales múltiples"
RS=[round(0.05*i,3) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(r),f"{2*math.pi*r**3:.4f}"] for r in RS],"c":3},
    {"t":"trazo","puntos":[[str(r),f"{4*math.pi*r**3/3:.4f}"] for r in RS],"c":0},
    {"t":"punto","p":["x","4*pi*x*x*x/3"],"c":0},
    {"t":"punto","p":["x","2*pi*x*x*x"],"c":3}]
graf={"tipo":"plano","x":[-0.2,2.3],"y":[-4,56],"a":0,"b":2,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"volumen de la esfera de radio R, 4 pi R al cubo sobre 3","formula":"4*pi*x*x*x/3"},{"rotulo":"volumen del cilindro que la rodea, 2 pi R al cubo","formula":"2*pi*x*x*x"}],
 "etiquetas":["Con esféricas, la esfera se integra con rho al cuadrado seno de phi","El cilindro de radio R y altura 2R, y la esfera ocupa dos tercios de él"],"etiquetaSlider":"Radio R, de 0 a 2",
 "alt":"El volumen de una esfera de radio R, que es 4 pi R al cubo sobre 3, comparado con el del cilindro de radio R y altura 2R, que vale 2 pi R al cubo. La esfera siempre ocupa dos tercios del cilindro. Ambos volúmenes se calculan con integrales triples en coordenadas esféricas y cilíndricas"}
glos={"cilindricas":"En coordenadas cilíndricas un punto se da por r, theta y z. Sirven cuando el sólido tiene simetría alrededor del eje z.",
 "esfericas":"En coordenadas esféricas un punto se da por la distancia rho al origen, el ángulo phi desde el eje z y el ángulo theta. Sirven con esferas y conos.",
 "jac":"El elemento de volumen es r dz dr d theta en cilíndricas y rho al cuadrado seno de phi d rho d phi d theta en esféricas.",
 "phi":"El ángulo phi va de 0 a pi, medido desde el eje z positivo. El ángulo theta va de 0 a 2 pi, alrededor del eje."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se comparan el volumen de una esfera y el del cilindro que la rodea, con radio R y altura 2R."],
 [4,10,"En cilíndricas el volumen del cilindro es pi R al cuadrado por 2R, o sea 2 pi R al cubo."],
 [10,16,"En esféricas la esfera da 4 pi R al cubo entre 3. Con R igual a 1 son 4.19 contra 6.28."],
 [16,20,"Con R igual a 2, la esfera mide 33.5 y el cilindro 50.3. La razón es siempre dos tercios."],
 [20,24,"Con la simetría correcta, la integral se simplifica mucho. El factor adicional es r en cilíndricas y rho al cuadrado seno phi en esféricas."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.5],[8,0.5],[10,1],[13,1],[16,2],[18,2],[24,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Con simetría alrededor del eje z se usan las {{gl:cilindricas|coordenadas cilíndricas}}, y con simetría respecto a un punto, las {{gl:esfericas|esféricas}}. Cada sistema trae su {{gl:jac|factor}} en el elemento de volumen. En esféricas, los ángulos {{gl:phi|phi y theta}} tienen rangos distintos, y no se deben confundir.")),
 sec("Un ejemplo","Un ejemplo",P("Se comparan una esfera y el cilindro que la rodea. Cambia el radio R y mira la razón de los volúmenes."),EQ("V_{esfera}=\\displaystyle\\int_{0}^{2\\pi}\\!\\int_{0}^{\\pi}\\!\\int_{0}^{R}\\rho^{2}\\operatorname{sen}\\phi\\,d\\rho\\,d\\phi\\,d\\theta=\\dfrac{4\\pi R^{3}}{3}"),{"t":"grafica","animar":"dibujar","alt":"Los volúmenes de la esfera y el cilindro"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En cilíndricas, el volumen del cilindro de radio R y altura h es el área de la base por la altura. ¿Cuánto vale la base?","opciones":["pi R al cuadrado","2 pi R","pi R","R al cuadrado"],"correcta":"pi R al cuadrado","bien":"Muy bien. Es el área del círculo, y la altura se multiplica después.","mal":"La base es un círculo de radio R, y su área es pi R al cuadrado."}),
 sec("Distintos radios","Radios",P("Mira los volúmenes con R igual a 0.5, 1, 1.5 y 2."),{"t":"acercando","ds":[0.5,1,1.5,2],"alt":"Los volúmenes con cuatro radios"},P("Siempre se cumple que la esfera es dos tercios del cilindro.")),
 sec("Cilíndricas","Cilíndricas",P("Se usa r, theta y z, con un factor r."),
   PASOS([("x=r\\cos\\theta,\\quad y=r\\operatorname{sen}\\theta,\\quad z=z","El cambio."),
          ("dV=r\\,dz\\,dr\\,d\\theta","El elemento de volumen."),
          ("V=\\displaystyle\\int_{0}^{2\\pi}\\!\\int_{0}^{R}\\!\\int_{0}^{h}r\\,dz\\,dr\\,d\\theta","El cilindro de radio R y altura h."),
          ("V=2\\pi\\cdot\\dfrac{R^{2}}{2}\\cdot h=\\pi R^{2}h","El resultado conocido.")]),
   OJO("El factor es r, y no r al cuadrado. Solo el elemento de la parte horizontal lo lleva, y z queda igual.")),
 sec("Esféricas","Esféricas",P("Se usa rho, phi y theta, con un factor rho al cuadrado por seno de phi."),
   PASOS([("x=\\rho\\operatorname{sen}\\phi\\cos\\theta,\\ y=\\rho\\operatorname{sen}\\phi\\operatorname{sen}\\theta,\\ z=\\rho\\cos\\phi","El cambio."),
          ("dV=\\rho^{2}\\operatorname{sen}\\phi\\,d\\rho\\,d\\phi\\,d\\theta","El elemento de volumen."),
          ("0\\le\\rho\\le R,\\quad 0\\le\\phi\\le\\pi,\\quad 0\\le\\theta\\le2\\pi","Los límites de una esfera."),
          ("V=\\dfrac{R^{3}}{3}\\cdot2\\cdot2\\pi=\\dfrac{4\\pi R^{3}}{3}","El resultado.")]),
   OJO("Phi va de 0 a pi y theta de 0 a 2 pi. Si phi llega hasta 2 pi, los aportes de seno de phi se cancelan y la integral sale mal. Si theta llega solo hasta pi, se cubre solo media esfera.")),
 eng("El tanque esférico","Un tanque esférico de 1.5 metros de radio se llena de agua. El volumen se calcula con una integral triple en esféricas, y con la densidad se obtiene la masa.","V=\\dfrac{4\\pi R^{3}}{3}=\\dfrac{4\\pi(1.5)^{3}}{3}\\approx14.1\\ \\text{m}^{3}",
   [("Radio","1.5 m"),("Volumen","cerca de 14.1 m³"),("Masa de agua","cerca de 14 100 kg")],"Para un tanque a medio llenar, el volumen de agua es el de un casquete, que se obtiene con límites de phi o de rho distintos. El método es el mismo."),
 completar("El elemento de volumen en coordenadas cilíndricas es [[hueco]] dz dr d theta.","dV=[[hueco]]\\,dz\\,dr\\,d\\theta",
   [("r","r"),("r^{2}","r al cuadrado"),("1","uno")],0,
   ["","El factor r al cuadrado es de otras coordenadas, como las esféricas con seno de phi.","Con uno no se corrige la deformación de las áreas lejos del eje."],"Viene del jacobiano de las polares.","Es r."),
 error("Alguien escribió el elemento de volumen en esféricas y se equivocó. Toca el paso que está mal.",
   [("x=\\rho\\operatorname{sen}\\phi\\cos\\theta","El cambio.","el cambio"),
    ("dV=\\rho\\operatorname{sen}\\phi\\,d\\rho\\,d\\phi\\,d\\theta","Este paso es el que falla.","rho a la primera"),
    ("V=\\dfrac{2\\pi R^{2}}{2}","Resultado.","un resultado distinto")],1,
   "El factor es rho al cuadrado por seno de phi, y no rho por seno de phi. Con rho a la primera, las unidades no darían volumen.",
   "dV=\\rho^{2}\\operatorname{sen}\\phi\\,d\\rho\\,d\\phi\\,d\\theta","Cuenta las dimensiones del factor."),
 ordenar("Estos son los pasos para calcular el volumen de una esfera en esféricas, pero están desordenados.",
   [("x,y,z\\to\\rho,\\phi,\\theta","Se hace el cambio"),
    ("dV=\\rho^{2}\\operatorname{sen}\\phi\\,d\\rho\\,d\\phi\\,d\\theta","Se escribe el elemento de volumen"),
    ("0\\le\\rho\\le R,\\ 0\\le\\phi\\le\\pi,\\ 0\\le\\theta\\le2\\pi","Se escriben los límites"),
    ("V=\\dfrac{4\\pi R^{3}}{3}","Se integra")],[2,0,3,1],
   "Primero el cambio, luego el elemento de volumen, después los límites y por último se integra.","Se empieza con el cambio de coordenadas."),
]
S+=cierre("Mini simulacro de cilíndricas y esféricas",[
 banco("cv_c2_12","El elemento de volumen en cilíndricas."),
 banco("cv_c2_13","El elemento de volumen en esféricas."),
 pnum("El volumen de una esfera de radio 3 es (decimal, 1 cifra):","113.1",0.2,"Es 4 pi por 27 entre 3, o sea 36 pi, cerca de 113.1."),
 pnum("El volumen de un cilindro de radio 1 y altura 2 es (decimal, 4 cifras):","6.2832",0.001,"Es pi por 1 al cuadrado por 2, o sea 2 pi.")])
prac=[
 {"titulo":"Esfera y cilindro","grafica":{"draw":1},"bloques":[P("Se comparan el volumen de la esfera y el del cilindro circunscrito."),EQ("V_{cil}=2\\pi R^{3},\\quad V_{esf}=\\tfrac{4}{3}\\pi R^{3}")]},
 {"titulo":"Cambia R","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen los dos volúmenes.")]},
 {"titulo":"Con R igual a 2","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("\\tfrac{4}{3}\\pi(8)\\approx33.5"),P("La esfera mide 33.5 y el cilindro 50.3, y la razón es dos tercios.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Phi va de 0 a pi, y theta de 0 a 2 pi."}]}]
preg={"tex":"\\text{En esféricas, el elemento de volumen es}","opciones":["$\\rho^{2}\\operatorname{sen}\\phi\\,d\\rho\\,d\\phi\\,d\\theta$","$\\rho\\,d\\rho\\,d\\phi\\,d\\theta$","$r\\,dr\\,d\\theta\\,dz$","$\\rho^{2}\\,d\\rho\\,d\\phi\\,d\\theta$"],"correcta":0,
 "explicacion":"El jacobiano de las esféricas es rho al cuadrado por seno de phi. El de cilíndricas es r.",
 "verificacion":{"formula":"2*2*sin(pi/2)+0*x","a":0,"esperado":4},
 "pistas":["Es un factor con rho.","Lleva un seno.","Es rho al cuadrado por seno de phi."],
 "errores":["","Rho a la primera no tiene las dimensiones de un volumen.","Ese es el de las cilíndricas, y no el de las esféricas.","Falta el seno de phi, que corrige los círculos cerca de los polos."]}
res=["En cilíndricas dV es r dz dr d theta, y en esféricas es rho al cuadrado seno de phi d rho d phi d theta.","Phi va de 0 a pi y theta de 0 a 2 pi.","La esfera ocupa dos tercios del cilindro que la rodea."]
write(lesson("cv-m2-l5","Lección 5 de 6","Coordenadas cilíndricas y esféricas",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-cilesf.json")
