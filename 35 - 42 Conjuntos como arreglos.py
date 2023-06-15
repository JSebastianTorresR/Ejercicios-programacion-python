# 35. Uni ́on: Calcula en un arreglo la uni ́on de los conjuntos y la imprime.

def union(arr1,arr2):
    uni = [*arr1]
    for i in range(len(arr2)):
        if(not arr2[i] in uni):
            uni.append(arr2[i])
    return uni
# print(union([1,2,3,4,5],[1,2,3,6,7,8,9]))
# 36. Intersecci ́on: Calcula en un arreglo la intersecci ́on de los conjuntos y la imprime.
def interseccion(arr1,arr2):
    inter = []
    for i in range(len(arr1)):
        if(arr2[i] in arr1):
            inter.append(arr2[i])
    return inter

# 37. Diferencia: Calcula en un arreglo la diferencia del primero con el segundo y la imprime.
def diferencia(arr1,arr2):
    dif = []
    for i in range(len(arr1)):
        if(not arr1[i] in arr2):
            dif.append(arr1[i])
    return dif
# print(diferencia([1,2,3,4,5],[1,2,3,6,7,8,9]))

# 38. Diferencia sim ́etrica: Calcula en un arreglo la diferencia sim ́etrica de los conjuntos y la
# imprime.
def diferenciaSimetrica(arr1,arr2):
    dif = diferencia(arr1,arr2)
    dif += diferencia(arr2, arr1)
    return dif

# 39. Pertenece: Lee un entero y determina si el elemento pertenece o no a cada uno de los
# conjuntos y lo imprime.
def pertenece(num,arr1, arr2):
    s = False
    for i in range(len(arr1)):
        if(num == arr1[i]):
            s = True
        if(s):
            return s + " arr1"
    for i in range(len(arr2)):
        if(num == arr2[i]):
            s = True
        if(s):
            return s + " arr2"
    return s

# 40. Contenido: Determina s ́ı el primer conjunto esta contenido en el segundo y lo imprime.
def contenido(arr1, arr2):
    control = []
    for i in range(len[arr1]):
        if(arr1[i] in arr2):
            control.append(True)
    return len(arr1) == len(control)
# 41. Salir: Permite al usuario salir de la aplicaci ́on.
# 4
# Despu ́es de realizada la operaci ́on, el men ́u se debe presentar de nuevo hasta que el usuario desee
# salir.

# Se debe verificar que el arreglo no tenga elementos repetidos.
# Suponga ahora que los elementos de tipo Tse encuentran ordenados totalmente. La representaci ́on
# anterior se puede modificar de tal manera que las operaciones anteriores sean implementadas de
# manera m ́as eficiente. La idea es mantener el conjunto de manera ordenada.
#
#  42. Desarrollar el programa anterior usando la representaci ́on modificada con las operaciones entre
# conjuntos optimizadas