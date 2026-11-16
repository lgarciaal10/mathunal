"""Auditoría dura de las lecciones, sobre los JSON y no sobre un volcado de texto.
Uso  python3 -I auditar_json.py ../lecciones > informe.txt

Revisa, para cada lección
 1  estructura de cada actividad (índices en rango, permutaciones, longitudes)
 2  pregunta.verificacion, el límite de la fórmula debe dar el valor esperado y coincidir con la opción correcta
 3  COMPLETAR, si la ecuación es una cadena numérica, la opción correcta la hace verdadera y las demás no
 4  ERROR, si los pasos son cadenas numéricas, el primer paso falso debe ser el marcado
 5  gráficas, todas las fórmulas se evalúan sin errores dentro de la ventana
Todo lo que no se pudo convertir a un cálculo se cuenta como no verificado, no como correcto."""
import json, glob, os, re, sys, math
from collections import Counter
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

TR = standard_transformations + (implicit_multiplication_application, convert_xor)
x = sp.Symbol('x')
LOC = {'x': x, 'pi': sp.pi, 'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'ln': sp.log, 'log': sp.log, 'exp': sp.exp,
       'sqrt': sp.sqrt, 'abs': sp.Abs, 'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan, 'E': sp.E}

# ---------- LaTeX numérico a sympy ----------
def tex_a_expr(s):
    """Convierte un fragmento LaTeX puramente numérico a sympy, o devuelve None."""
    t = s
    t = re.sub(r'\\(left|right|big|Big|bigg|Bigg)\s*', '', t)
    t = t.replace(r'\dfrac', r'\frac').replace(r'\tfrac', r'\frac')
    for a in (r'\ ', r'\,', r'\;', r'\!', r'\quad', r'\qquad', r'\:'):
        t = t.replace(a, ' ')
    t = t.replace(r'\cdot', '*').replace(r'\times', '*').replace(r'\div', '/')
    t = t.replace(r'\pi', ' pi ')
    t = re.sub(r'\\operatorname\{sen\}|\\sin|\\mathrm\{sen\}', ' sin ', t)
    for f in ('cos', 'tan', 'ln', 'log', 'exp', 'arcsin', 'arccos', 'arctan'):
        t = t.replace('\\' + f, ' ' + {'arcsin': 'asin', 'arccos': 'acos', 'arctan': 'atan'}.get(f, f) + ' ')
    # fracciones y raíces con llaves anidadas
    for _ in range(12):
        n = re.sub(r'\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}', r'((\1)/(\2))', t)
        n = re.sub(r'\\sqrt\s*\[(\d+)\]\s*\{([^{}]*)\}', r'((\2)**(1/\1))', n)
        n = re.sub(r'\\sqrt\s*\{([^{}]*)\}', r'sqrt(\1)', n)
        n = re.sub(r'\^\s*\{([^{}]*)\}', r'**(\1)', n)
        if n == t: break
        t = n
    t = re.sub(r'\^\s*(-?\w)', r'**(\1)', t)
    t = t.replace('{', '(').replace('}', ')')
    t = re.sub(r'e\*\*', 'E**', t)
    if '\\' in t or '_' in t: return None
    # solo números, operadores, pi, E, funciones conocidas y x
    letras = re.findall(r'[A-Za-z]+', t)
    ok = {'pi', 'sqrt', 'sin', 'cos', 'tan', 'ln', 'log', 'exp', 'asin', 'acos', 'atan', 'E'}
    if any(l not in ok for l in letras): return None
    t = re.sub(r'(\d),(\d)', r'\1.\2', t) if False else t
    try:
        return parse_expr(t.strip(), local_dict=LOC, transformations=TR, evaluate=True)
    except Exception:
        return None

def dividir_igualdades(tex):
    """Parte una cadena a=b=c en niveles de llaves y paréntesis cero. Devuelve lista de fragmentos y el tipo de relación."""
    t = tex
    if re.search(r'\\(Rightarrow|Leftrightarrow|iff|quad|text|mathbf|begin|vec)', t): t = re.sub(r'\\(quad|qquad)', ' ', t)
    if re.search(r'\\(Rightarrow|Leftrightarrow|iff|text|mathbf|begin|vec|le|ge|neq|ne|lt|gt)', t) or '<' in t or '>' in t or ',' in t: return None
    t = t.replace(r'\approx', '≈').replace(r'\neq', '≠')
    partes, nivel, cur = [], 0, ''
    for ch in t:
        if ch in '{(': nivel += 1
        if ch in '})': nivel -= 1
        if ch in '=≈' and nivel == 0:
            partes.append(cur); cur = ''; partes.append(ch)
        else: cur += ch
    partes.append(cur)
    return partes

def evaluar_cadena(tex, hueco=None):
    """Devuelve True/False si la cadena es numérica y se pudo evaluar, o None si no."""
    t = tex
    if hueco is not None: t = t.replace('[[hueco]]', '(' + hueco + ')')
    partes = dividir_igualdades(t)
    if not partes or len(partes) < 3: return None
    vals, rels = [], []
    for i, p in enumerate(partes):
        if i % 2 == 1: rels.append(p); continue
        e = tex_a_expr(p)
        if e is None or e.free_symbols: return None
        vals.append(e)
    for i in range(len(vals) - 1):
        a, b = vals[i], vals[i + 1]
        try:
            if rels[i] == '=':
                if abs(complex((a - b).evalf(40))) > 1e-15 * max(1, abs(complex(b.evalf(40)))): return False
            else:
                an, bn = float(a), float(b)
                if abs(an - bn) > 0.02 * max(1e-9, abs(bn)) + 0.011: return False
        except Exception:
            return None
    return True

# ---------- fórmulas de la gráfica ----------
def formula_a_expr(f):
    try: return parse_expr(str(f).replace('^', '**'), local_dict=LOC, transformations=TR)
    except Exception: return None

def numerico(expr, xv):
    try:
        v = complex(expr.subs(x, xv).evalf())
        return v.real if abs(v.imag) < 1e-9 else None
    except Exception:
        return None

def recoger_formulas(g):
    out = []
    def walk(o, ruta):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ('formula', 'f', 'y', 'x') and isinstance(v, str): out.append((ruta + '.' + k, v))
                elif k in ('a', 'b', 'p', 'q', 'c', 'x0', 'y0', 'x1', 'y1', 'valor') and isinstance(v, str): out.append((ruta + '.' + k, v))
                elif k in ('a', 'b', 'c', 'p') and isinstance(v, list):
                    for i, z in enumerate(v):
                        if isinstance(z, str): out.append((ruta + '.' + k + '[%d]' % i, z))
                else: walk(v, ruta + '.' + k)
        elif isinstance(o, list):
            for i, v in enumerate(o): walk(v, ruta + '[%d]' % i)
    walk(g, 'grafica')
    return out

# ---------- recorrido ----------
def bloques(d):
    """Todos los bloques con campo t dentro de la lección."""
    res = []
    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get('t'), str): res.append(o)
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(d); return res

def num_de_opcion(s):
    s = str(s).strip().replace('−', '-')
    m = re.fullmatch(r'-?\d+(\.\d+)?', s)
    if m: return sp.Rational(s)
    m = re.fullmatch(r'(-?\d+)\s*/\s*(\d+)', s)
    if m: return sp.Rational(int(m.group(1)), int(m.group(2)))
    e = tex_a_expr(s)
    return e if (e is not None and not e.free_symbols) else None

def auditar(path):
    d = json.load(open(path)); stem = os.path.basename(path)[:-5]
    F = []   # hallazgos (gravedad, texto)
    cov = Counter()
    def bad(g, m): F.append((g, m))

    # 1 estructura
    for b in bloques(d):
        t = b['t']
        if t == 'ordenar':
            n = len(b['pasos']); m = b.get('mezcla', [])
            if sorted(m) != list(range(n)): bad('ALTA', 'ordenar, mezcla no es permutación de 0..%d' % (n - 1))
            if m == list(range(n)): bad('MEDIA', 'ordenar, la mezcla es la identidad')
            if len(b.get('txt', [])) != n: bad('MEDIA', 'ordenar, txt con %d y pasos con %d' % (len(b.get('txt', [])), n))
            cov['ordenar'] += 1
        if t == 'error':
            n = len(b['pasos'])
            if not (0 <= b['mal'] < n): bad('ALTA', 'error, mal=%s fuera de rango' % b['mal'])
            cov['error'] += 1
        if t == 'completar':
            n = len(b['opciones'])
            if not (0 <= b['correcta'] < n): bad('ALTA', 'completar, correcta fuera de rango')
            if len(b.get('errores', [])) != n: bad('MEDIA', 'completar, errores con %d y opciones con %d' % (len(b.get('errores', [])), n))
            elif b['errores'][b['correcta']] != '': bad('BAJA', 'completar, la opción correcta tiene texto de error')
            if '[[hueco]]' not in b['tex']: bad('ALTA', 'completar, sin [[hueco]]')
            tx = [o['tex'] for o in b['opciones']]
            if len(set(tx)) != len(tx): bad('ALTA', 'completar, opciones repetidas')
            cov['completar'] += 1
        if t == 'piensa':
            ops = b['opciones']
            if b['correcta'] not in ops: bad('ALTA', 'piensa, correcta=%r no está entre las opciones' % (b['correcta'],))
            if len(set(map(str, ops))) != len(ops): bad('ALTA', 'piensa, opciones repetidas')
            cov['piensa'] += 1
        if t == 'simulacro':
            for q in b.get('preguntas', []):
                if q.get('tipo') == 'mcq':
                    if not (0 <= q['correcta'] < len(q['opciones'])) if isinstance(q.get('correcta'), int) else q.get('correcta') not in q['opciones']:
                        bad('ALTA', 'simulacro mcq, correcta fuera de rango')
                    if len(set(map(str, q['opciones']))) != len(q['opciones']): bad('ALTA', 'simulacro mcq, opciones repetidas')
                cov['simulacro_q'] += 1

    # 2 pregunta.verificacion
    for nom in ('pregunta',):
        q = d.get(nom)
        if q:
            ops = q.get('opciones', [])
            if isinstance(q.get('correcta'), int) and not (0 <= q['correcta'] < len(ops)): bad('ALTA', 'pregunta, correcta fuera de rango')
            if len(set(map(str, ops))) != len(ops): bad('ALTA', 'pregunta, opciones repetidas')
            v = q.get('verificacion')
            if v:
                fx = formula_a_expr(v['formula'])
                if fx is None: bad('MEDIA', 'pregunta.verificacion, la fórmula no se pudo leer'); cov['verif_no'] += 1
                else:
                    try:
                        a0 = sp.nsimplify(v['a']); h = sp.Rational(1, 10**9)
                        L = (fx.subs(x, a0 + h).evalf(40) + fx.subs(x, a0 - h).evalf(40)) / 2
                        esp = sp.nsimplify(v['esperado'])
                        if abs(float(L) - float(esp)) > 2e-4 * max(1, abs(float(esp))): bad('ALTA', 'pregunta.verificacion, el límite da %s y esperado dice %s' % (L, esp))
                        cov['verif_ok'] += 1
                        o = num_de_opcion(ops[q['correcta']]) if isinstance(q.get('correcta'), int) else None
                        if o is not None:
                            if abs(float(o) - float(esp)) > 1e-6 * max(1, abs(float(esp))): bad('ALTA', 'pregunta, la opción correcta (%s) no coincide con esperado (%s)' % (ops[q['correcta']], esp))
                            cov['verif_opcion'] += 1
                    except Exception as e:
                        bad('MEDIA', 'pregunta.verificacion, no se pudo calcular %s' % repr(e)[:80]); cov['verif_no'] += 1

    # 3 completar y 4 error, cadenas numéricas
    for b in bloques(d):
        if b['t'] == 'completar':
            tex = b['tex']
            res = []
            for i, o in enumerate(b['opciones']):
                res.append(evaluar_cadena(tex, o['tex']))
            if all(r is None for r in res): cov['completar_no_verificable'] += 1; continue
            cov['completar_verificado'] += 1
            c = b['correcta']
            if res[c] is False: bad('ALTA', 'completar, la opción marcada como correcta hace falsa la ecuación (%s con %s)' % (tex[:70], b['opciones'][c]['tex']))
            for i, r in enumerate(res):
                if i != c and r is True: bad('ALTA', 'completar, la opción %s también hace verdadera la ecuación (%s)' % (b['opciones'][i]['tex'], tex[:70]))
        if b['t'] == 'error':
            ev = [evaluar_cadena(p['tex']) for p in b['pasos']]
            if all(e is None for e in ev): cov['error_no_verificable'] += 1; continue
            if all(e is not False for e in ev) and all(e is None or e is True for e in ev) and sum(e is True for e in ev) < 2: cov['error_no_verificable'] += 1; continue
            cov['error_verificado'] += 1
            falsos = [i for i, e in enumerate(ev) if e is False]
            if falsos and falsos[0] != b['mal']: bad('ALTA', 'error, el primer paso numéricamente falso es el %d y mal=%d' % (falsos[0] + 1, b['mal'] + 1))
            if not falsos and ev[b['mal']] is True: bad('ALTA', 'error, el paso marcado como erróneo es numéricamente verdadero (%s)' % b['pasos'][b['mal']]['tex'][:70])

    # 5 fórmulas de la gráfica
    g = d.get('grafica')
    if g:
        xr = g.get('x', [-5, 5]); a = g.get('a', 0); bb = g.get('b', 1)
        for ruta, f in recoger_formulas(g):
            fx = formula_a_expr(f)
            if fx is None: bad('MEDIA', 'gráfica, %s no se puede leer %r' % (ruta, f)); cov['graf_no'] += 1; continue
            cov['graf_formulas'] += 1
            for xv in [a, (a + bb) / 2, bb]:
                if numerico(fx, xv) is None and fx.free_symbols - {x}:
                    bad('MEDIA', 'gráfica, %s tiene símbolos libres %r' % (ruta, f)); break
    return stem, F, cov

def main(carpeta):
    todos = Counter(); graves = []; filas = []
    for p in sorted(glob.glob(os.path.join(carpeta, '*.json'))):
        print('...', os.path.basename(p), file=sys.stderr, flush=True)
        try: stem, F, cov = auditar(p)
        except Exception as e:
            print('EXCEPCION', p, repr(e)[:200]); continue
        todos.update(cov); filas.append((stem, F))
    n = sum(len(F) for _, F in filas)
    print('Lecciones', len(filas), 'hallazgos', n)
    print('Cobertura', dict(todos))
    for stem, F in filas:
        for g, m in F: print('%-5s %-24s %s' % (g, stem, m))

if __name__ == '__main__':
    main(sys.argv[1])
