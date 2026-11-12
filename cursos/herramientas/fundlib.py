import math
def lagr(vals,var="x"):
    """polinomio que vale vals[i] en var=i, para enteros 0..n-1"""
    n=len(vals); t=[]
    for i,v in enumerate(vals):
        if v==0: continue
        num="*".join(f"({var}-{j})" for j in range(n) if j!=i)
        den=1
        for j in range(n):
            if j!=i: den*=(i-j)
        t.append(f"({v}*{num}/({den}))" if num else f"({v})")
    return "+".join(t) if t else "0"
def tabla(cols,filas,W=1.7,H=0.95,x0=0.0,top=0.0,colores=None,sel="x"):
    """tabla de verdad como poligonos. filas: lista de listas de 0/1. La fila resaltada es la del parametro x (entero).
    devuelve (elementos, ventana_x, ventana_y)"""
    el=[]; nc=len(cols); nf=len(filas)
    def rect(xa,ya,xb,yb,c,txt=None,**k):
        d={"t":"poligono","puntos":[[xa,ya],[xb,ya],[xb,yb],[xa,yb]],"c":c}
        if txt is not None: d["nombre"]=txt
        d.update(k); return d
    for ci,h in enumerate(cols):
        xa=x0+ci*W; el.append(rect(str(xa),str(top),str(xa+W),str(top-H),0,h))
    for ri,fila in enumerate(filas):
        for ci,v in enumerate(fila):
            xa=x0+ci*W; ya=top-(ri+1)*H
            el.append(rect(str(xa),str(ya),str(xa+W),str(ya-H),3 if v else 1,"V" if v else "F"))
    xa=x0; xb=x0+nc*W
    ya=f"({top}-({sel}+1)*{H})"; yb=f"({top}-({sel}+2)*{H})"
    el.append(rect(str(xa),ya,str(xb),yb,2))
    ys=(nf+1)*H+0.6; xs=ys*550/300
    xc=x0+nc*W/2
    return el,[round(xc-xs/2,3),round(xc+xs/2,3)],[round(top-(nf+1)*H-0.5,3),round(top+0.5,3)]
