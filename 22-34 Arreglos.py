import math
# 22. Implementar la criba de Eratostenes para calcular los n ́umeros primos en el rango 1 a n, donde
# n es un n ́umero natural dado por el usuario.
def cribaEratostenes(n):
    criba = []
    primos = []
    for i in range(n+1):
        criba.append(True)

    for j in range(2, math.ceil(n**0.5)):
        for k in range(2, n):
            if(j*k < n):
                criba[j*k] = False

    for i in range(2,n+1):
        if(criba[i]):
            primos.append(i)
    return primos


# 23. Desarrollar un algoritmo que calcule la suma de los elementos de un arreglo de n ́umeros enteros
# (reales).
def sumaArreglo(arreglo):
    suma = 0
    for i in range(arreglo):
        suma += arreglo[i]
    return suma

# 24. Desarrollar un algoritmo que calcule el promedio de un arreglo de enteros (reales).
# 2
def multiplicacionArreglo(arreglo):
    mul = 1
    for i in range(arreglo):
        mul *= arreglo[i]
    return mul

# 25. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de n ́umeros enteros
# (reales) de igual tama ̃no. Sean v =(v1,v2,...,vn)y w =(w1,w2,...,wn)dos arreglos, el
# producto de v y w (notado v ⋅ w) es el n ́umero: v1 ∗ w1 + v2 ∗ w2 + ⋯ + vn ∗ wn.
def productoPunto(arr1,arr2):
    producto = 1 
    for i in range(len(arr1)):
        producto += arr1[i] * arr2[i]
    return producto
# 26. Desarrollar un algoritmo que calcule el m ́ınimo de un arreglo de n ́umeros enteros (reales).
def minimo(arr):
    menor = arr[0]
    for i in range(len(arr)):
        if(arr[i] < menor):
            menor = arr[i]
    return menor

# 27. Desarrollar un algoritmo que calcule el m ́aximo de un arreglo de n ́umeros enteros (reales).
def mayor(arr):
    mayor = arr[0]
    for i in range(len(arr)):
        if(arr[i] > mayor):
            mayor = arr[i]
    return mayor

# 28. Desarrollar un algoritmo que calcule el producto directo de dos arreglos de enteros (reales) de
# igual tama ̃no. Sean v =(v1,v2,...,vn)y w =(w1,w2,...,wn)dos arreglos, el producto directo
# de v y w (notado v ∗ w) es el vector: (v1 ∗ w1,v2 ∗ w2,...,vn ∗ wn).

def productoDirecto(arr1,arr2):
    directo = [] 
    for i in range(len(arr1)):
        directo.append(arr1[i] * arr2[i])
    return directo
# 29. Desarrollar un algoritmo que determine la mediana de un arreglo de enteros (reales). La
# mediana es el n ́umero que queda en la mitad del arreglo despu ́es de ser ordenado.
def ordenar(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
    return arr

def mediana(arr):
    ordenado = ordenar(arr)
    mitad = math.floor(len(arr)/2)
    return ordenado[mitad]

# 30. Hacer un algoritmo que deje al final de un arreglo de n ́umeros todos los ceros que aparezcan
# en dicho arreglo.
# Ejemplo.
# vector original: (1,6,0,7,−3,8,0,−2,11)
# vector salida: (1,6,7,−3,8,−2,11,0,0)
# Ejemplo.
# vector original: (0,11,36,10,0,17,−23,81,0,0,12,11,0)
# vector salida: (11,36,10,17,−23,81,12,11,0,0,0,0,0)
def mueveCeros(arr):
    cereal = []
    for i in range(len(arr)-1):
        if(arr[i]):
            cereal.append(arr[i])
    for i in range(len(arr)-len(cereal)):
        cereal.append(0)
    return cereal


# 31. Suponga que un arreglo de enteros esta lleno de unos y ceros y que el arreglo representa un
# n ́umero binario al rev ́es. Hacer un algoritmo que calcule los n ́umeros en decimal que representa
# dicho arreglo de unos y ceros.
# Ejemplo.
# Entrada: (0,1,0,1,0,1,1)(representa el n ́umero 1101010).
# Salida: 106
# Ejemplo.
# Entrada: (1,0,0,1,0,1,1,1,1)(representa el n ́umero 111101001).
# Salida: 389

def binarioDecimal(arr):
    suma = 0
    for i in range(len(arr)):
        suma += arr[i] * 2 ** (i)
    return suma

# 32. Hacer un algoritmo que dado un n ́umero entero no negativo, cree un arreglo de unos y ceros
# que representa el n ́umero en binario al rev ́es.
# Ejemplo.
# N ́umero: 106
# Arreglo: (0,1,0,1,0,1,1)(representa el n ́umero 1101010)
# 3
# Ejemplo.
# N ́umero: 389
# Arreglo: (1,0,0,1,0,1,1,1,1)(representa el n ́umero 111101001)
def decimalBinario(num):
    almacenador = []
    aux = num
    while(aux != 0):
        division = math.floor(aux/2)
        residuo = aux % 2
        aux = division
        almacenador.append(residuo)
    return almacenador

# 33. Hacer un algoritmo que calcule el M ́aximo Com ́un Divisor (MCD) para un arreglo de enteros
# positivos.
# Ejemplo.
# Arreglo: (12,20,14,124,72,2458)
# MCD del arreglo: 2
def mcd(num1, num2):
    if (num2 > num1):
        num2, num1 = num1, num2
    if(num1 == 0):
        return num2
    if(num2 == 0):
        return num1
    else:
        return mcd(num2, num1%num2)
    
# 34. Hacer un algoritmo que calcule el M ́ınimo Com ́un M ́ultiplo (MCM) para un arreglo de enteros
# positivos.
# Ejemplo.
# Arreglo: (12,20,30,15)
# MCD del arreglo: 60
def mcm(arr):
    return