# 60. Union: Calcula e imprime la relaci ́on uni ́on.
def union(rel1, rel2):
    uni = [*rel1]
    for i in range(len(rel1)):
        for j in range(len(rel1[i])):
            if(rel2[i][j]):
                uni[i][j] = rel2
    return uni

# 61. Intersecci ́on: Calcula e imprime la relaci ́on intersecci ́on.
def interseccion(rel1, rel2):
    inter = []
    for i in range(len(rel1)):
        inter.append([])
        for j in range(len(rel1[i])):
            if(rel2[i][j] == rel1[i][j]):
                inter[i].append(rel2[i][j])
            else:
                inter[i].append(0)
    return inter


# 62. Simetr ́ıa: Determina si la primer relaci ́on es sim ́etrica o no.
def simetria(rel):
    s = True
    trans = transpuesta(rel)
    for i in range(len(rel)):
        for j in range(len(rel[i])):
            s = s and trans[i][j] == rel[i][j]
            if(not s):
                return s
    return s
def transpuesta(mat):
    trans = []
    for i in range(len(mat)):
        trans.append([])
        for j in range(len(mat[i])):
            trans.append(mat[j][i])
    return trans
# 63. Reflexividad: Determina si la primer relaci ́on es reflexiva o no.
def reflexiva(rel):
    s = True
    for i in range(len(rel)):
        s = s and rel[i][i]
        if(not s):
            return s
    return s

# 64. Transitividad: Determina si la primer relaci ́on le ́ıda es transitiva o no.


# 65. Orden: Determina si la primer relaci ́on le ́ıda es relaci ́on de orden o no.


# 66. Equivalencia: Determina si la primer relaci ́on le ́ıda es una relaci ́on de equivalencia.


# 67. Funci ́on: Determina si la relaci ́on es una funci ́on o no.


# 68. Inyectividad: Determina si la relaci ́on es una funci ́on inyectiva.


# 69. Sobreyectividad: Determina si la relaci ́on es una funci ́on sobreyectiva.


# 70. Salir: Permite al usuario salir del programa