# Cada reel: id, curso, titulo (con | para salto), frases [ (texto, LaTeX o None, nota o None, efecto o None) ]
O='\\textcolor{#FFB48A}{%s}'
R='\\textcolor{#FF6B6B}{%s}'
G='\\textcolor{#3DDC84}{%s}'
SPECS=[
 dict(id='basicas',curso='Matemáticas Básicas',titulo='Cuadrado|de un binomio',fr=[
  ("¿Cuánto es x más tres, al cuadrado? Casi todos dicen x al cuadrado más nueve, y se equivocan.",None,None,None),
  ("Cuadrado quiere decir multiplicar por sí mismo.",'(x+3)^{2}',None,None),
  ("Entonces escribimos el factor dos veces.",'(x+3)(x+3)',None,None),
  ("Ahora repartimos cada término con cada término.",'x^{2}+3x+3x+9',None,None),
  ("Los dos del medio son iguales, y se suman.",'x^{2}+'+O%'6x'+'+9','Aquí está lo que se olvida',None),
  ("Esos seis x son el doble producto, y nunca se pierden.",'x^{2}+'+O%'6x'+'+9',None,'ring')]),
 dict(id='diferencial',curso='Cálculo Diferencial',titulo='Derivada|de un producto',fr=[
  ("¿Cuál es la derivada de x al cuadrado por seno de x? No es el producto de las derivadas.",None,None,None),
  ("Esta es la función.",'\\dfrac{d}{dx}\\left(x^{2}\\sin x\\right)',None,None),
  ("La regla del producto dice, derivada del primero por el segundo, más el primero por la derivada del segundo.",'\\left(x^{2}\\right)^{\\prime}\\sin x+x^{2}(\\sin x)^{\\prime}','Regla del producto',None),
  ("La derivada de x al cuadrado es dos x, y la de seno es coseno.",'2x\\sin x+x^{2}\\cos x',None,None),
  ("Y así queda la derivada completa.",O%'2x\\sin x+x^{2}\\cos x',None,'ring')]),
 dict(id='integral',curso='Cálculo Integral',titulo='Integral|por sustitución',fr=[
  ("Esta integral parece difícil, pero tiene un truco que la vuelve sencilla.",None,None,None),
  ("Tenemos dos x por coseno de x al cuadrado.",'\\int 2x\\cos\\left(x^{2}\\right)dx',None,None),
  ("Llamamos u a lo de adentro, x al cuadrado. Y su diferencial es dos x dx.",'\\int \\cos u\\,du','u = x² , du = 2x dx',None),
  ("La integral de coseno es seno.",'\\sin u+C',None,None),
  ("Volvemos a x, y listo.",O%'\\sin\\left(x^{2}\\right)+C',None,'ring')]),
 dict(id='algebra',curso='Álgebra Lineal',titulo='Valores|propios',fr=[
  ("Un valor propio dice por cuánto se estira un vector que no cambia de dirección.",None,None,None),
  ("Buscamos números lambda que cumplan esto.",'A v=\\lambda v',None,None),
  ("Se resuelve con el determinante de A menos lambda por la identidad, igual a cero.",'\\det(A-\\lambda I)=0',None,None),
  ("Con la matriz tres, uno, dos, dos, queda esta ecuación.",'\\lambda^{2}-5\\lambda+4=0',None,None),
  ("Se factoriza como lambda menos uno, por lambda menos cuatro.",'(\\lambda-1)(\\lambda-4)=0',None,None),
  ("Los valores propios son uno y cuatro.",O%'\\lambda=1\\quad\\lambda=4',None,'ring')]),
 dict(id='edo',curso='Ecuaciones Diferenciales',titulo='Variables|separables',fr=[
  ("Algunas ecuaciones se resuelven separando las variables, cada una de su lado.",None,None,None),
  ("Esta dice que y prima es dos x por y.",'y^{\\prime}=2xy',None,None),
  ("Pasamos las y a un lado y las x al otro.",'\\dfrac{dy}{y}=2x\\,dx','Cada variable de su lado',None),
  ("Integramos los dos lados.",'\\ln|y|=x^{2}+C',None,None),
  ("Y despejamos y con la exponencial.",O%'y=Ce^{x^{2}}',None,'ring')]),
 dict(id='fundamentos',curso='Fundamentos de Matemáticas',titulo='Negar|un para todo',fr=[
  ("¿Cómo se niega que algo se cumple para todos? Mucha gente se confunde aquí.",None,None,None),
  ("Esta es la afirmación, para todo x, se cumple P.",'\\forall x\\ P(x)',None,None),
  ("Negarla es poner un no delante.",'\\neg\\left(\\forall x\\ P(x)\\right)',None,None),
  ("Basta con que falle en un solo caso.",'\\exists x\\ \\neg P(x)','Un contraejemplo basta',None),
  ("Existe un x para el que no se cumple. Esa es la negación.",O%'\\exists x\\ \\neg P(x)',None,'ring')]),
 dict(id='geometria',curso='Geometría Vectorial',titulo='Ángulo entre|vectores',fr=[
  ("El producto punto sirve para hallar el ángulo entre dos vectores.",None,None,None),
  ("Esta es la fórmula.",'\\mathbf{u}\\cdot\\mathbf{v}=|\\mathbf{u}||\\mathbf{v}|\\cos\\theta',None,None),
  ("Despejamos el coseno.",'\\cos\\theta=\\dfrac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{u}||\\mathbf{v}|}',None,None),
  ("Con u igual a uno, cero, y v igual a uno, uno, el producto punto es uno, y la longitud de v es raíz de dos.",'\\cos\\theta=\\dfrac{1}{\\sqrt{2}}',None,None),
  ("Ese coseno corresponde a cuarenta y cinco grados.",O%'\\theta=45^{\\circ}',None,'ring')]),
 dict(id='discretas',curso='Matemáticas Discretas',titulo='Combinaciones|sin orden',fr=[
  ("¿De cuántas formas puedes escoger dos personas de un grupo de cinco? El orden no importa.",None,None,None),
  ("Se llama combinación de cinco en dos.",'C(5,2)',None,None),
  ("Se calcula con factoriales.",'\\dfrac{5!}{2!\\,3!}',None,None),
  ("Simplificamos el tres factorial.",'\\dfrac{5\\cdot4}{2}','Se cancela el 3!',None),
  ("Y hay diez formas.",O%'10',None,'ring')]),
 dict(id='numericos',curso='Métodos Numéricos',titulo='El método|de bisección',fr=[
  ("¿Cómo se encuentra una raíz cuando no se puede despejar? Cortando el intervalo por la mitad.",None,None,None),
  ("Buscamos donde x al cuadrado menos dos vale cero.",'f(x)=x^{2}-2',None,None),
  ("En uno es negativa, y en dos es positiva. Hay una raíz en medio.",'f(1)=-1<0,\\ f(2)=2>0',None,None),
  ("Tomamos el punto medio.",'c=\\dfrac{1+2}{2}=1.5',None,None),
  ("Ahí la función vale cero punto veinticinco, positiva.",'f(1.5)=0.25>0',None,None),
  ("La raíz queda entre uno y uno punto cinco. Repetimos.",O%'[1,\\ 1.5]',None,'ring')]),
 dict(id='especiales',curso='Matemáticas Especiales',titulo='La fórmula|de Euler',fr=[
  ("Hay una igualdad famosa que junta los números más importantes.",None,None,None),
  ("La fórmula de Euler une la exponencial con seno y coseno.",'e^{i\\theta}=\\cos\\theta+i\\sin\\theta',None,None),
  ("Con theta igual a pi.",'e^{i\\pi}=\\cos\\pi+i\\sin\\pi',None,None),
  ("Coseno de pi es menos uno, y seno de pi es cero.",'e^{i\\pi}=-1+0',None,None),
  ("Pasando el uno al otro lado, queda la identidad de Euler.",O%'e^{i\\pi}+1=0',None,'ring')]),
 dict(id='varias',curso='Cálculo en Varias Variables',titulo='El gradiente|y su magnitud',fr=[
  ("El gradiente apunta hacia donde la función crece más rápido.",None,None,None),
  ("Tomemos f igual a x al cuadrado más y al cuadrado.",'f=x^{2}+y^{2}',None,None),
  ("El gradiente son las derivadas parciales.",'\\nabla f=(2x,\\,2y)',None,None),
  ("En el punto uno, dos, vale dos, cuatro.",'\\nabla f(1,2)=(2,4)',None,None),
  ("Su magnitud es raíz de veinte, la máxima razón de cambio.",O%'\\|\\nabla f\\|=\\sqrt{20}',None,'ring')]),
]
OUTRO=["Lo hiciste muy bien. Con práctica, esto se vuelve natural.","Practica con preguntas reales de parciales en MathUNAL."]
