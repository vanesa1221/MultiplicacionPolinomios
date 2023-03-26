def L(i, xi, x):
    """ Función de Lagrange para el punto xi[i] """
    n = len(xi)
    numer = 1
    denom = 1
    for j in range(n):
        if j != i:
            numer *= x - xi[j]
            denom *= xi[i] - xi[j]
    return numer / denom


def multiply_poly(p, q):
    # Calcular el grado del polinomio resultante
    n = len(p) + len(q) - 1

    # Inicializar los coeficientes del polinomio resultante a cero
    r_coeffs = [0] * n

    # Multiplicar los coeficientes de los polinomios
    for i in range(len(p)):
        for j in range(len(q)):
            r_coeffs[i + j] += p[i] * q[j]

    # Construir la lista de puntos xi
    xi = list(range(n))

    # Interpolar los coeficientes del polinomio resultante
    r_poly = 0
    for i in range(n):
        r_poly += r_coeffs[i] * L(i, xi, 2)
    #   r_poly += r_coeffs[i] * L(i, xi, x)

    return r_coeffs  # r_coeffs[::-1]


