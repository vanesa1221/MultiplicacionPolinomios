def MulPolMatrizImaginaria(pA, pB, w):
    # funcion que multiplica dos polinomios con matriz de Vandermonde Imaginaria
    # Parametros de entrada
    #   pA = coeficientes del polinomio a0 + a1*x+a2*x^2+....
    #   pB = coeficientes del polinomio b0 + b1*x+b2*x^2+....
    #   w = raiz (i o -i)
    # Parametros de salida
    #   pP = coeficientes de producto de polinomios p0 + p1*x + p2*x^2 ....
    # 1. coeficientes la longitud de los arreglos es 2*n
    for i in range(len(pA)):
        pA.append(0)
        pB.append(0)
    n = len(pA)
    # Creando Matriz de Vandermonde Imaginaria
    matrizImag = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(w ** (i * j))
        matrizImag.append(fila)
    # 2. Evaluacion matriz * PA y matriz *PB
    vecColMA = np.dot(matrizImag, pA)
    vecColMB = np.dot(matrizImag, pB)
    # 3. Calcular producto punto entre vectores columna
    vProductoPunto = []
    for i in range(len(vecColMA)):
        vProductoPunto.append(vecColMA[i] * vecColMB[i])
    # 4. Interpolacion Matriz inversa de VandermondeImag * vector producto punto
    matrizInversa = np.linalg.inv(matrizImag)
    vectorResultado = np.dot(matrizInversa, vProductoPunto)
    # return vectorResultado
    print(vectorResultado)


# Ejemplo de prueba con raiz w=i
pA = [1, 2]
pB = [1, 1]
w = complex(0, 1)
MulPolMatrizImaginaria(pA, pB, w)
# entrega como resultado [1,4,8,8,3] = 1+4x+8x^2+8x^3+3x^4

# Ejemplo de prueba con raiz w=-i
pA = [1, 2]
pB = [1, 1]
w = complex(0, -1)
MulPolMatrizImaginaria(pA, pB, w)
# entrega como resultado [1,4,8,8,3] = 1+4x+8x^2+8x^3+3x^4
