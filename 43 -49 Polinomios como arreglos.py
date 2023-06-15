# Un polinomio de grado n, como P(x)=anxn + an−1xn−1 + ⋯ + a1x1 + a0x0 se puede representar
# mediante un arreglo de reales de la siguiente manera: (a0,a1,...,an−1,an).
# Usando esta representaci ́on hacer un programa que le permita al usuario leer dos polinomios y
# escoger mediante un men ́u, una de las siguientes operaciones sobre dichos polinomios:


# 43. Evaluar: Lee un real e imprime la evaluaci ́on de los dos polinomios en dicho dato.

def evaluar(num, pol1, pol2):
    eval1 = 0
    for i in range(len(pol1)):
        eval1 += pol1[i]*(num**i)
    eval2 = 0
    for i in range(len(pol2)):
        eval2 += pol2[i]*(num**i)
    return eval1, eval2

# 44. Sumar: Calcula el polinomio suma y lo imprime.
def sumar(pol1, pol2):
    suma = []
    for i in range(len(pol2)):
        suma.append(pol1[i]+pol2[i])
    return suma
# 45. Resta: Calcula el polinomio resta y lo imprime.
def resta(pol1, pol2):
    resta = []
    for i in range(len(pol2)):
        resta.append(pol1[i]-pol2[i])
    return resta

# 46. Multiplicar: Calcula el polinomio multiplicaci ́on y lo imprime.
def multiplicar(pol1, pol2):
    mul = []
    for i in range(len(pol1)):
        for j in range(len(pol2)):
            mul.append(pol1[i]*pol2[j])
    return mul
# 47. Dividir: Calcula el polinomio divisi ́on del primer polinomio por el segundo y lo imprime.
def dividir(pol1, pol2):
    div = []
    for i in range(len(pol1)):
        for j in range(len(pol2)):
            div.append(pol1[i]/pol2[j])
    return div
# 48. Residuo: Calcula el polinomio residuo de la divisi ́on del primero por el segundo y lo imprime.

def residuo(pol1, pol2):
    res = []
    for i in range(len(pol1)):
        for j in range(len(pol2)):
            res.append(pol1[i]%pol2[j])
    return res

# 49. Salir: Permite salir de la aplicaci ́on al usuario.
# Despu ́es de realizada la operaci ́on el men ́u se debe presentar de nuevo hasta que el usuario desee
# salir