from sympy import symbols, Eq, solve

def split_number(n, base):
    """Divide un número en 3 partes según la base"""
    n_str = str(n).rjust(3 * base, '0')
    a2 = int(n_str[:-2*base]) if n_str[:-2*base] else 0
    a1 = int(n_str[-2*base:-base])
    a0 = int(n_str[-base:])
    return [a0, a1, a2]

def combine_parts(coeffs, base):
    """reconstruim el numero amb els seus coeficients polinomics"""
    B = 10 ** base
    result = 0
    for i, c in enumerate(coeffs):
        result += c * (B ** i)
    return result

def toom_cook_3(x, y):
    base = 2  # Para dividir en partes de 2 dígitos

    a = split_number(x, base)
    b = split_number(y, base)

    # Evaluar polinomios en puntos 0,1,-1,-2,infinito
    p = [
        a[0],                    # p(0)
        a[0] + a[1] + a[2],      # p(1)
        a[0] - a[1] + a[2],      # p(-1)
        a[0] - 2*a[1] + 4*a[2],  # p(-2)
        a[2]                     # p(infinito)
    ]

    q = [
        b[0],
        b[0] + b[1] + b[2],
        b[0] - b[1] + b[2],
        b[0] - 2*b[1] + 4*b[2],
        b[2]
    ]

    # Multiplicar valores evaluados
    r = [p[i] * q[i] for i in range(5)]

    # Fem us de sympy para resolver el sistema 
    c0, c1, c2, c3, c4 = symbols('c0 c1 c2 c3 c4')

    # El sistema es:
    # r[0] = c0
    # r[1] = c0 + c1 + c2 + c3 + c4
    # r[2] = c0 - c1 + c2 - c3 + c4
    # r[3] = c0 - 2*c1 + 4*c2 - 8*c3 + 16*c4
    # r[4] = c4

    eq1 = Eq(c0, r[0])
    eq2 = Eq(c0 + c1 + c2 + c3 + c4, r[1])
    eq3 = Eq(c0 - c1 + c2 - c3 + c4, r[2])
    eq4 = Eq(c0 - 2*c1 + 4*c2 - 8*c3 + 16*c4, r[3])
    eq5 = Eq(c4, r[4])

    soluciones = solve((eq1, eq2, eq3, eq4, eq5), (c0, c1, c2, c3, c4))

    # Convertimos soluciones a enteros 
    coeficientes = [int(soluciones[c].evalf()) for c in [c0, c1, c2, c3, c4]]

    # Reconstruir numero resultado
    resultado = combine_parts(coeficientes, base)
    return resultado

while True :

    print("="*50)
    print("====Multiplicadora amb l'algorisme de Toom-Cook 3====")
    print("="*50)
    print("Benvingut a l’eina per multiplicar amb l’algorisme de Toom-Cook 3.")
    x = int(input("Escull el Primer numero:  "))
    y = int(input("Escull el Segon numero:  "))
    print("*"*75)

    resultado = toom_cook_3(x, y)
    print(resultado)
    print(" ")
