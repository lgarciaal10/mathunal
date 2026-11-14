# estados LaTeX por escena, fs base en px (tamano KaTeX antes de .1.21)
R='\\textcolor{#FF6B6B}{%s}'; G='\\textcolor{#3DDC84}{%s}'; O='\\textcolor{#FFB48A}{%s}'
SCENES={
 's1':dict(fs=92,states=['\\dfrac{x+3}{x}','\\dfrac{'+R%'x'+'+3}{'+R%'x'+'}','\\dfrac{'+R%'x'+'+3}{'+R%'x'+'}=3']),
 's3':dict(fs=84,states=['\\dfrac{4+2}{2}','\\dfrac{4+2}{2}=\\dfrac{6}{2}='+G%'3']),
 's4':dict(fs=84,states=['\\dfrac{4+2}{2}','\\dfrac{4+'+R%'2'+'}{'+R%'2'+'}','4+1','4+1='+R%'5','4+1='+R%'5'+'\\neq3']),
 's5':dict(fs=84,states=['\\dfrac{x\\cdot3}{x\\cdot5}','\\dfrac{'+G%'x'+'\\cdot3}{'+G%'x'+'\\cdot5}','\\dfrac{3}{5}','\\dfrac{x+3}{x+5}']),
 's6':dict(fs=100,states=['\\dfrac{x^{2}-4}{x^{2}-x-2}','\\dfrac{(x-2)(x+2)}{x^{2}-x-2}','\\dfrac{(x-2)(x+2)}{(x-2)(x+1)}','\\dfrac{'+R%'(x-2)'+'(x+2)}{'+R%'(x-2)'+'(x+1)}','\\dfrac{x+2}{x+1}']),
}
SCENES['sd']=dict(fs=150,states=['\\dfrac{x+2}{x+1}'])
