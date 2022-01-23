# This is a sample Python script.
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def sumaplx(c1,c2):
    real = c1[0] + c2[0]
    imaginario = c1[1] + c2[1]
    return (real, imaginario)

def multiplicacion(c1, c2):
    real = (c1[0] * c2[0]) - (c1[1] * c2[1])
    imaginario = (c1[0] * c2[1]) + (c2[0] * c1[1])
    return (real, imaginario)

def division(c1, c2):
    real = ((c1[0] * c2[0]) + (c1[1] * c2[1]))// (c2[0] ** 2 + c2[1] ** 2)
    imaginario = ((c2[0] * c1[1]) - (c1[0] * c2[1]))// (c2[0] ** 2 + c2[1] ** 2)
    return (real, imaginario)

def resta(c1, c2):
    real = c1[0] - c2[0]
    imaginario = c1[1] - c2[1]
    return (real, imaginario)

def moduloz(c1):
    return ((c1[0]**2 + c1[1]**2)**0.5)

def conjugado(c1):
    return (c1[0], - c1[1])

def convPolarCartesiano(o):
    a = math.cos(o)
    b = math.sin(o)
    p = ((a ** 2) + (b ** 2) ** 0.5)
    return (a, b, p)

#def faseNumeroComplejo():

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print(sumaplx((3, -1), (1, 4)))
    print(multiplicacion((3, -2), (1, 2)))
    print(division((-2, 1), (1, 2)))
    print(resta((-2, 1), (1, 2)))
    print(moduloz((1, - 1)))
    print(conjugado((-2, 1)))
    print(convPolarCartesiano(45))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
