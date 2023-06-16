# 50. Desarrollar un algoritmo que permita sumar dos matrices de n ́umeros reales (enteros).
def suma(mat1, mat2):
    suma = []
    for i in range(len(mat1)):
        suma.append([])
        for j in range(len(mat1[i])):
            suma[i].append(mat1[i][j] + mat2[i][j])
    return suma

# 51. Desarrollar un algoritmo que permita multiplicar dos matrices de n ́umeros reales (enteros).
def multiplicacion(mat1, mat2):
    mul = []
    for i in range(len(mat1)):
        mul.append([])
        for j in range(len(mat1[i])):
            mul[i].append(mat1[i][j] * mat2[j][i])
    return

# 52. Desarrollar un programa que sume los elementos de una columna dada de una matriz.
def columna(num , matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][num]
    return suma
# 53. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
def columna(num , matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[num][i]
    return suma

# 54. Desarrollar un algoritmo que determine si una matriz es m ́agica. Se dice que una matriz
# cuadrada es m ́agica si la suma de cada una de sus filas, de cada una de sus columnas y de
# cada diagonal es igual.


# 55. Desarrollar un algoritmo que dado un entero, reemplace en una matriz todos los n ́umeros
# mayores a un n ́umero dado por un uno y todos los menores o iguales por un cero


# 56. Desarrollar un programa que calcule el determinante de una matriz cuadrada.


# 57. Desarrollar un programa que dadas una matriz cuadrada A y un arreglo de n ́umeros reales
# del mismo tama ̃no B, calcule una soluci ́on x para el sistema de ecuaciones lineales Ax =B.


# 58. Desarrollar un programa que calcule la inversa de una matriz cuadrada.


# 59. Desarrollar un programa que tome un arreglo de tama ̃no n2 y llene en espiral hacia adentro
# una matriz cuadrada de tama ̃no n.