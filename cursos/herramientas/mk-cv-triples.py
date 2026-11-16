import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 2 Integrales múltiples"
ZS=[round(0.025*i,4) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(z),f"{(1-z)**2/2:.5f}"] for z in ZS],"c":3},
    {"t":"segmento","a":["x","0"],"b":["x","(1-x)*(1-x)/2"],"c":1},
    {"t":"punto","p":["x","(1-x)*(1-x)/2"],"c":0}]
graf={"tipo":"plano","x":[-0.15,1.15],"y":[-0.08,0.58],"a":0,"b":1,"inicio":0.3,"elementos":EL,
 "lecturas":[{"rotulo":"área de la sección a la altura z, igual a 1 menos z al cuadrado sobre 2","formula":"(1-x)*(1-x)/2"},{"rotulo":"volumen acumulado hasta la altura z","formula":"(1-(1-x)*(1-x)*(1-x))/6"}],
 "etiquetas":["Cada sección horizontal del tetraedro es un triángulo que se encoge con z","El volumen es la suma de las áreas de las secciones, y al llegar a z igual a 1 vale un sexto"],"etiquetaSlider":"Altura z, de 0 a 1",
 "alt":"El tetraedro con vértices en el origen y en los puntos 1, 0, 0, 0, 1, 0 y 0, 0, 1. A la altura z su sección es un triángulo de área 1 menos z al cuadrado sobre 2. La curva muestra esa área al variar z. El volumen es el área bajo la curva, que vale un sexto"}
glos={"triple":"Una integral triple suma una función sobre una región del espacio, y con f igual a 1 da el volumen de la región.",
 "seccion":"Una sección es la figura que resulta de cortar el sólido con un plano. La integral triple se puede ver como la suma de las áreas de las secciones.",
 "orden":"Hay seis órdenes posibles para una integral triple, y conviene elegir el que tenga los límites más sencillos.",
 "dv":"El elemento de volumen es dV igual a dx dy dz, y en otras coordenadas lleva un factor adicional."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se quiere el volumen del tetraedro limitado por los planos de coordenadas y por x más y más z igual a 1."],
 [4,10,"A cada altura z, la sección es un triángulo con x más y menor o igual a 1 menos z, y su área es 1 menos z al cuadrado entre 2."],
 [10,16,"Con z igual a 0.3, el área de la sección es 0.245, y el volumen acumulado ya es 0.11."],
 [16,20,"Con z igual a 1 la sección se reduce a un punto, y el volumen acumulado llega a un sexto, cerca de 0.167."],
 [20,24,"Una integral triple suma el área de las secciones, igual que una integral doble suma los largos de los cortes."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,0.3],[13,0.3],[16,1],[18,1],[24,1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Una {{gl:triple|integral triple}} suma una función sobre un sólido. Se calcula como tres integrales iteradas, y se puede pensar como la suma de las áreas de las {{gl:seccion|secciones}}. Se escoge el {{gl:orden|orden}} con límites más simples, y el {{gl:dv|elemento de volumen}} es dx dy dz.")),
 sec("Un ejemplo","Un ejemplo",P("El tetraedro tiene vértices en el origen y en los puntos 1, 0, 0, 0, 1, 0 y 0, 0, 1. Mueve la altura z y mira el área de la sección."),EQ("V=\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{1-z}\\!\\int_{0}^{1-z-y}dx\\,dy\\,dz=\\int_{0}^{1}\\dfrac{(1-z)^{2}}{2}\\,dz=\\dfrac{1}{6}"),{"t":"grafica","animar":"dibujar","alt":"El área de la sección según la altura"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La sección a la altura z es un triángulo de catetos 1 menos z. ¿Cuál es su área?","opciones":["1 menos z, al cuadrado, entre 2","1 menos z","1 menos z, al cuadrado","un medio"],"correcta":"1 menos z, al cuadrado, entre 2","bien":"Muy bien. El área de un triángulo rectángulo es base por altura entre 2.","mal":"Es un triángulo rectángulo de catetos 1 menos z, y su área es el producto entre 2, o sea 1 menos z al cuadrado entre 2."}),
 sec("A varias alturas","Alturas",P("Mira la sección con z igual a 0, 0.3, 0.6 y 0.9."),{"t":"acercando","ds":[0,0.3,0.6,0.9],"alt":"La sección a cuatro alturas"},P("La sección se encoge cuando z sube, y el volumen es el área bajo esta curva.")),
 sec("Una integral sencilla","Caja",P("Sobre una caja los límites son constantes, y el orden no importa."),
   PASOS([("\\displaystyle\\iiint_{[0,1]^{3}}x\\,dV=\\int_{0}^{1}\\!\\int_{0}^{1}\\!\\int_{0}^{1}x\\,dx\\,dy\\,dz","La integral."),
          ("\\displaystyle\\int_{0}^{1}x\\,dx=\\dfrac{1}{2}","Se integra respecto a x."),
          ("\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{1}\\dfrac{1}{2}\\,dy\\,dz=\\dfrac{1}{2}","Las otras dos integran una constante sobre un cuadrado de área 1."),
          ("\\displaystyle\\iiint_{[0,1]\\times[0,2]\\times[0,3]}dV=1\\cdot2\\cdot3=6","El volumen de una caja es el producto de sus lados.")]),
   OJO("Cuando la función no depende de una variable, la integral en esa variable solo multiplica por la longitud del intervalo.")),
 sec("El tetraedro","Tetraedro",P("Aquí los límites dependen de las otras variables."),
   PASOS([("x+y+z\\le1,\\quad x,y,z\\ge0","La región."),
          ("0\\le x\\le1-y-z,\\quad 0\\le y\\le1-z,\\quad 0\\le z\\le1","Los límites, de adentro hacia afuera."),
          ("\\displaystyle\\int_{0}^{1-y-z}dx=1-y-z","La primera integral."),
          ("\\displaystyle\\int_{0}^{1}\\dfrac{(1-z)^{2}}{2}\\,dz=\\dfrac{1}{6}","Al final queda un sexto.")]),
   OJO("Los límites de la integral de afuera son constantes, y los de adentro pueden depender de las variables que están más afuera. Dibuja el sólido para no equivocarte.")),
 eng("El volumen de un sólido de carga","Un sólido tiene forma de tetraedro y una densidad de carga constante. La carga total es la densidad por el volumen, que sale de una integral triple.","Q=\\displaystyle\\iiint_{T}\\rho\\,dV=\\rho\\cdot\\dfrac{1}{6}",
   [("Volumen","un sexto de unidad cúbica"),("Densidad","constante"),("Carga","densidad entre 6")],"Si la densidad depende de la posición, se integra la función en lugar de una constante. Es el mismo cálculo, con un integrando más complicado."),
 completar("El volumen de la caja de lados 1, 2 y 3 es la integral triple de 1, que vale [[hueco]].","\\displaystyle\\iiint_{[0,1]\\times[0,2]\\times[0,3]}1\\,dV=[[hueco]]",
   [("6","seis"),("1","uno"),("5","cinco")],0,
   ["","Uno es el volumen de la caja unidad, y esta es más grande.","Cinco sería la suma de los lados, y no el producto."],"El volumen de una caja es el producto de los tres lados.","Es 6."),
 error("Alguien calculó el volumen del tetraedro por secciones y se equivocó. Toca el paso que está mal.",
   [("A(z)=\\dfrac{(1-z)^{2}}{2}","Área de la sección.","área"),
    ("V=\\displaystyle\\int_{0}^{1}A(z)\\,dz=\\int_{0}^{1}\\dfrac{(1-z)^{2}}{2}dz=\\dfrac{1}{2}","Este paso es el que falla.","da un medio"),
    ("V=\\dfrac{1}{2}","Resultado.","un medio")],1,
   "La integral de uno menos z al cuadrado entre 2, de 0 a 1, es un tercio de un medio, o sea un sexto. Se olvidó el factor un tercio de la integral de la potencia.",
   "\\displaystyle\\int_{0}^{1}\\dfrac{(1-z)^{2}}{2}dz=\\dfrac{1}{2}\\cdot\\dfrac{1}{3}=\\dfrac{1}{6}","Integra una potencia con la regla de la potencia."),
 ordenar("Estos son los pasos para calcular el volumen de un sólido con una integral triple, pero están desordenados.",
   [("x+y+z\\le1","Se dibuja el sólido"),
    ("0\\le z\\le1,\\ 0\\le y\\le1-z,\\ 0\\le x\\le1-y-z","Se escriben los límites"),
    ("\\displaystyle\\int\\!\\int\\!\\int dx\\,dy\\,dz","Se plantea la integral"),
    ("V=\\dfrac{1}{6}","Se calcula de adentro hacia afuera")],[2,0,3,1],
   "Primero el sólido, luego los límites, después la integral y por último se calcula.","Se empieza dibujando el sólido."),
]
S+=cierre("Mini simulacro de integrales triples",[
 banco("cv_c2_05","La integral de x sobre el cubo unidad."),
 pnum("El volumen de la caja $[0,1]\\times[0,2]\\times[0,3]$ es:","6",0.01,"Es el producto de los lados, 1 por 2 por 3."),
 pnum("El volumen del tetraedro $x+y+z\\le1$ en el primer octante, en decimales con 3 cifras, es:","0.167",0.001,"Es un sexto, cerca de 0.167.")])
prac=[
 {"titulo":"El sólido","grafica":{"draw":1},"bloques":[P("Se calcula el volumen del tetraedro por secciones."),EQ("x+y+z\\le1,\\quad x,y,z\\ge0")]},
 {"titulo":"Sube z","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el área de la sección y el volumen acumulado.")]},
 {"titulo":"El volumen total","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("V=\\dfrac{1}{6}\\approx0.167"),P("Con z igual a 1 se completó el tetraedro.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Una integral triple es una suma de secciones."}]}]
preg={"tex":"\\displaystyle\\iiint_{[0,1]^{3}}x\\,dV\\ \\text{vale}","opciones":["$\\dfrac{1}{2}$","$1$","$\\dfrac{1}{3}$","$0$"],"correcta":0,
 "explicacion":"La integral de x de 0 a 1 es un medio, y las otras dos integran una constante sobre longitud 1. El resultado es un medio.",
 "verificacion":{"formula":"0.5*1*1+0*x","a":0,"esperado":0.5},
 "pistas":["Integra respecto a x primero.","La integral de x de 0 a 1 es un medio.","Las otras integrales multiplican por 1."],
 "errores":["","Uno sería la integral de 1, y no de x.","Un tercio sería la integral de x al cuadrado.","Cero sería con una función impar en un intervalo simétrico."]}
res=["Una integral triple suma una función sobre un sólido, y con f igual a 1 da el volumen.","Se calcula con tres integrales iteradas, de adentro hacia afuera.","Dibujar el sólido ayuda a escribir los límites."]
write(lesson("cv-m2-l4","Lección 4 de 6","Integrales triples",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-triples.json")
