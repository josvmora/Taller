def BruteForce(lista):
    maximo = 0
    for i in range(0, len(lista)):
        actual = 0
        for j in range(0, len(lista)):
            actual += lista[j]
            if actual > maximo:
                maximo = actual
    return maximo


def DividenConquer(lista, inicio, fin):
    if inicio == fin:
        return lista[inicio]

    medio = (inicio + fin) // 2

    maximo_izquierda = DividenConquer(lista, inicio, medio)
    maximo_derecha = DividenConquer(lista, medio, fin)
    maximo_cross = maxCross(lista, inicio, medio, fin)

    return max(maximo_izquierda, maximo_derecha, maximo_cross)


def maxCross(lista, inicio, medio, fin):
    suma_actual_izquierda = 0
    suma_izquierda = 0
    suma_acutal_derecha = 0
    suma_derecha = 0

    for i in range(inicio, medio):
        suma_izquierda += lista[i]
        if suma_izquierda > suma_actual_izquierda:
            suma_actual_izquierda = suma_izquierda

    for i in range(medio, fin):
        suma_derecha += lista[i]
        if suma_derecha > suma_acutal_derecha:
            suma_acutal_derecha = suma_derecha

    return (suma_actual_izquierda + suma_acutal_derecha)


arreglo = [1, 2, 3]

print(BruteForce(arreglo))
print(DividenConquer(arreglo, 0, len(arreglo) - 1))
