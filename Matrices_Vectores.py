import numeros_complejos

def adicionV(c1, c2):

    if (len(c1) == len(c2)):
        a = [[0 for i in range(len(c1)-1)] for j in range(len(c1[0]))]
        for i in range(len(c1)):
            for j in range(len(c1[0])-1):
                a[i][j] = numeros_complejos.sumaplx(c1[i], c2[i])
    else:
        return ("Los vectores no son iguales")
    return a

def inversoAditivoV(c1, c2):

    if (len(c1) == len(c2)):
        a = [[0 for i in range(len(c1)-1)] for j in range(len(c1[0]))]
        for i in range(len(c1)):
            for j in range(len(c1[0])-1):
                a[i][j] = numeros_complejos.resta(c1[i], c2[i])
    else:
        return ("Los vectores no son iguales")
    return a

def multiplicacionEscalarV(c, c1):

    a = [[0 for i in range(len(c1))] for j in range(len(c1[0]))]
    for i in range(len(c1)):
        for j in range(len(c1[0])):
            a[i][j] = c * c1[i][j]
    return a

def adicionM(c1, c2):

    if (len(c1) == len(c2)) and (len(c1[0]) == len(c2[0])):
        a = [[0 for i in range(len(c1))] for j in range(len(c1[0]))]
        for i in range(len(c1)):
            for j in range(len(c1[0])):
                a[i][j] = numeros_complejos.sumaplx(c1[i][j], c2[i][j])
    else:
        return ("Las matrices no son iguales")
    return a

def inversaAdicionM(c1, c2):
    if (len(c1) == len(c2)) and (len(c1[0]) == len(c2[0])):
        a = [[0 for i in range(len(c1))] for j in range(len(c1[0]))]
        for i in range(len(c1)):
            for j in range(len(c1[0])):
                a[i][j] = numeros_complejos.resta(c1[i][j], c2[i][j])
    else:
        return ("Las matrices no son iguales")
    return a

def transpuesta(c1):

    a = [[0 for i in range(len(c1[0]))] for j in range(len(c1))]
    for i in range(len(c1[0])):
        for j in range(len(c1)):
            a[i][j] = c1[j][i]
    return a

def conjugada(c1):

    for i in range(len(c1[0])):
        for j in range(len(c1)):
            c1[i][j] = numeros_complejos.conjugado(c1[i][j])
    return c1

"""def adjunta(c1):

    if (len(c1) == len(c1[0])):

        a = [[0 for i in range(len(c1[0]))] for j in range(len(c1))]
        for i in range(len(c1[0])):
            for j in range(len(c1)):
                while ():
                c1[i][j] =
        return c1

    else:

        return("No es una matriz cuadrada")

"""
def productoDosMatrices(c1, c2):

    if (len(c1[0]) == len(c2)):

        a = [[0 for i in range(len(c1))] for j in range(len(c2[0]))]
        for i in range(len(c1)):
            for j in range(len(c2[0])):
                for k in range(len(c1[0])):
                    a[i][j] += c1[i][k] * c2[k][j]
                    return a
    else:

        return("No se puede multiplicar las matrices")

"""def accionMatriz():"""

def productoInternoVectores(c1, c2):

    if (len(c1[0]) != 0 or len(c2[0]) != 0):

        a = 0
        for i in range(len(c1)):
            a += c1[i] * c2[i]
        return a

    else:
        return("No se puede realizar producto interno entre matrices")

def normaVector(c1):

    if (len(c1[0]) != 0):

        a = 0
        for i in range(len(c1)):
            a += c1[i] ** 2
        a ** 0.5
        return a

    else:
        return("No se puede realizar la norma de una matriz")

def distanciaDosVectores(c1, c2):

    if (len(c1[0]) != 0) and (len(c1) == len(c2)):

        a = 0
        for i in range(len(c1)):
            a += (c2[i] - c1[i]) ** 2
        a ** 0.5
        return a

    else:
        return("No se puede realizar la norma")

"""def matrizUnitaria():
def matrizHermitiana():

def productoTensor():"""

if __name__ == '__main__':

    print(adicionV(((1,2), (1,2)), ((2,1), (2,3))))
    print(inversoAditivoV(((1,2), (1,2)), ((2,1), (2,3))))
    print(multiplicacionEscalarV(2, [(2,1), (2,3)]))
    print(adicionM([[(1,2), (1,2)], [(1,2), (1,2)]], [[(2,1), (2,3)], [(2,3), (2,3)]]))
    print(inversaAdicionM([[(1, 2), (1, 2)], [(1, 2), (1, 2)]], [[(2, 1), (2, 3)], [(2, 3), (2, 3)]]))
    print(transpuesta([(1, 2), (2, 2)]))
    print(conjugada([(1, 2), (2, 2)]))
    print(productoDosMatrices([[(1, 2), (2, 2)], [(1, -2), (1, 2)]]))

