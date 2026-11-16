"""Verifica con sympy, de forma independiente, cada ejercicio generado.
Uso  node exportar.js 200 > /tmp/ej.json && python3 -I verificar.py /tmp/ej.json"""
import json, sys, re
from collections import Counter
import sympy as sp
from sympy import Rational, symbols, sin, cos, exp, log, I, simplify, diff, integrate, limit, Matrix, binomial, oo

x, y, t = symbols('x y t')
LOC = {'x': x, 'y': y, 't': t, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log, 'I': I, 'zoo': sp.zoo}

def S(s):
    return sp.sympify(str(s), locals=LOC)

def eq(a, b):
    try:
        d = sp.simplify(S(a) - S(b))
        return d == 0
    except Exception:
        return False

def verdad(p):
    c = p['chk']; k = c['k']
    if k == 'deriv':
        T = diff(S(c['f']), x); return lambda v: eq(v, T)
    if k == 'limit':
        T = limit(S(c['f']), x, c['x0']); return lambda v: eq(v, T)
    if k == 'newton':
        f = S(c['f']); T = Rational(c['x0']) - f.subs(x, c['x0']) / diff(f, x).subs(x, c['x0']); return lambda v: eq(v, T)
    if k == 'antider':
        g = S(c['f']); return lambda v: sp.simplify(diff(S(v), x) - g) == 0
    if k == 'defint':
        T = integrate(S(c['f']), (x, c['lo'], c['hi'])); return lambda v: eq(v, T)
    if k == 'det':
        T = Matrix(c['M']).det(); return lambda v: eq(v, T)
    if k == 'eig':
        T = sorted(Matrix(c['M']).eigenvals().keys()); return lambda v: sorted([sp.nsimplify(z) for z in v]) == T
    if k == 'linsys':
        A = Matrix(c['A']); T = list(A.LUsolve(Matrix(c['b']))); return lambda v: [sp.nsimplify(z) for z in v] == T
    if k == 'edo':
        y0 = c['y0']; rhs = S(c['rhs'])
        def f(v):
            yy = S(v)
            return sp.simplify(diff(yy, t) - rhs.subs(y, yy)) == 0 and sp.simplify(yy.subs(t, 0) - y0) == 0
        return f
    if k == 'edolim':
        Y = sp.Function('Y'); sol = sp.dsolve(Y(t).diff(t) + c['a'] * Y(t) - c['b'], Y(t), ics={Y(0): c['y0']})
        T = limit(sol.rhs, t, oo); return lambda v: eq(v, T)
    if k == 'expand':
        T = sp.expand(S(c['f'])); return lambda v: sp.simplify(sp.expand(S(v)) - T) == 0
    if k == 'roots':
        T = sorted(sp.solve(S(c['f']), x)); return lambda v: sorted(sp.nsimplify(z) for z in v) == T
    if k == 'perp':
        u = c['u']; vv = c['v']; kk = symbols('kk')
        T = sp.solve(u[0] * vv[0] + u[1] * vv[1] + u[2] * kk, kk)[0]; return lambda v: eq(v, T)
    if k == 'cross':
        T = list(Matrix(c['u']).cross(Matrix(c['v']))); return lambda v: [sp.nsimplify(z) for z in v] == T
    if k == 'comb':
        T = binomial(c['n'], c['kk']); return lambda v: eq(v, T)
    if k == 'grad':
        f = S(c['f']); pt = c['pt']; T = [diff(f, x).subs({x: pt[0], y: pt[1]}), diff(f, y).subs({x: pt[0], y: pt[1]})]
        return lambda v: [sp.nsimplify(z) for z in v] == T
    if k == 'dint':
        T = integrate(S(c['f']), (y, 0, c['q']), (x, 0, c['p'])); return lambda v: eq(v, T)
    if k == 'biseccion':
        L = Rational(c['L']); tol = Rational(1, 10 ** c['e']); n = 0
        while L / 2 ** n >= tol: n += 1
        return lambda v: eq(v, n)
    if k == 'incl':
        T = c['A'] + c['B'] - c['I']; return lambda v: eq(v, T)
    raise SystemExit('tipo sin verificador ' + k)

def main(path):
    ej = json.load(open(path)); malos = []; cuenta = Counter(); vistos = Counter()
    for p in ej:
        cuenta[p['plantilla']] += 1
        try:
            chk = verdad(p)
            oks = [o for o in p['ops'] if o['ok']]
            if len(p['ops']) != 4 or len(oks) != 1: malos.append((p['plantilla'], p['seed'], 'opciones mal formadas')); continue
            for o in p['ops']:
                res = chk(o['v'])
                if o['ok'] and not res: malos.append((p['plantilla'], p['seed'], 'la marcada como correcta es falsa ' + str(o['v'])))
                if (not o['ok']) and res: malos.append((p['plantilla'], p['seed'], 'una incorrecta es verdadera ' + str(o['v'])))
            vistos[p['plantilla']] += 1
        except Exception as e:
            malos.append((p['plantilla'], p['seed'], 'excepcion ' + repr(e)[:120]))
    print('ejercicios', len(ej), 'plantillas', len(cuenta))
    for k in cuenta: print(' ', k, cuenta[k])
    print('FALLAS', len(malos))
    por = Counter(m[0] for m in malos)
    for k, n in por.items(): print('  ', k, n, [m for m in malos if m[0] == k][:2])
    return 1 if malos else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
