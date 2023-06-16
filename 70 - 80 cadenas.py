index = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}
index2 = {0: "a",1: "b",2: "c",3: "d",4: "e",5: "f",6: "g",7: "h",8: "i",9: "j",10: "j",11: "l",12: "m",13: "n",14: "o",15: "p",16: "q",17: "r",18: "s",19: "t",20: "u",21: "v",22: "w",23: "x",24: "y",25: "z"}
# 71. Desarrollar un algoritmo que reciba como entrada un car ́acter y de como salida el n ́umero de
# ocurrencias de dicho car ́acter en una cadena de caracteres.
def ocurrencias(letra, cadena):
    contador = 0
    for i in range(len(cadena)):
        if(cadena[i]==letra):
            contador+=1
    return contador

# 72. Desarrollar un algoritmo que reciba como entrada dos cadenas y determine si la primera es
# subcadena de la segunda. (No se deben usar operaciones de subcadenas propias del lenguaje
# de programaci ́on).
# Ejemplos.
# La cadena “prosa” es subcadena de la cadena “la prosa debe ser armoniosa”.
# La cadena “pepito” no es subcadena de la cadena “el torpe pito de aire”.
# La cadena “pe pito” si esta incluida en la cadena “el torpe pito de aire”.
def subcadena(subcad, cadena):
    posicion = 0
    s = False
    for i in range(len(cadena)):
        if(subcad[posicion]== cadena[i]):
            s = True
            for j in range(len(subcad)):
                s = s and subcad[j] == cadena[i+j]
        if(s):
            return s
    return s
 
# 73. Desarrollar un algoritmo que reciba dos cadenas de caracteres y determine si la primera est ́a
# incluida en la segunda. Se dice que una cadena est ́a incluida en otra, si todos los caracteres
# (con repeticiones) de la cadena est ́a en la segunda cadena sin tener en cuenta el orden de los
# caracteres.
# Ejemplos.
# La cadena “prosa” est ́a incluida en la cadena “la profesora de ingles”.
# La cadena “pepito” no esta incluida en la cadena “un pedazo de tierra”, ya que le
# falta una “p”.
# La cadena “pepito” si esta incluida en la cadena “tijeras o papel”.

def contenida(cont, cadena):
    contContador = 0
    cadenaContador = 0
    for letra in cont:
        for i in range(len(cadena)):
            if(letra == cadena[i]):
                cadenaContador += 1
        for j in range(len(cont)):
            if(letra == cont[j]):
                contContador += 1
    return contContador == cadenaContador



# 74. Desarrollar un algoritmo que invierta una cadena de caracteres.
def invertir(cadena):
    inverso = ""
    for i in range(len(cadena)):
        inverso += cadena[len(cadena)-i-1]
    return inverso



# 75. Desarrollar un algoritmo que determine si una cadena de caracteres es pal ́ındrome. Una cadena
# se dice pal ́ındrome si al invertirla es igual a ella misma.
# Ejemplos.
# “ala” es pal ́ındrome.
# “amor a roma” es pal ́ındrome.
# “al sur de Colombia” NO es pal ́ındrome.
# “anula las alas a la luna” NO es pal ́ındrome. (Al invertirla: “anul al a sala sal
# aluna”) no es igual a la original.
def palindromo(cadena):
    return cadena == invertir(cadena)

# 76. Desarrollar un algoritmo que determina si una cadena de caracteres es frase pal ́ındrome. Una
# cadena se dice frase pal ́ındrome si la cadena al eliminarle los espacios es pal ́ındrome.
# Ejemplos.
# “anula las alas a la luna” es frase pal ́ındrome.
# “amor a roma” es frase pal ́ındrome.
# “dabale arroz a la zorra el abad” es frase pal ́ındrome.
def quitarEspacio(cadena):
    cad = ""
    for i in range(len(cad)):
        if(cadena[i]==" "):
            cad += ""
        else:
            cad += cadena[i] 
    return cad

def frasePalindroma(cadena):
    return palindromo(quitarEspacio(cadena))

# 77. Desarrollar un algoritmo que realice el corrimiento circular a izquierda de una cadena de
# caracteres. El corrimiento circular a izquierda es pasar el primer car ́acter de una cadena como
#  ́ultimo car ́acter de la misma.
# Ejemplo.
# Entrada: “al sur de Colombia”.
# Salida: “l sur de Colombiaa”.
# Ejemplo.
# Entrada: “Pepito va al colegio”.
# Salida: “epito va al colegioP”.
def corrimientoCircularIzquierda(cadena):
    arreglo = []
    for i in range(len(cadena)):
        arreglo.append(cadena[i])
    primera = arreglo.pop(0)
    arreglo.append(primera)
    return "".join(arreglo)


# 78. Desarrollar un algoritmo que realice el corrimiento circular a derecha de una cadena de ca-
# racteres. El corrimiento circular a derecha de una cadena es poner el  ́ultimo car ́acter de la
# cadena como primer car ́acter de la misma.
# Ejemplo.
# Entrada: “al sur de Colombia”.
# Salida: “aal sur de Colombi”.
# Ejemplo.
# Entrada: “Pepito va al colegio”.
# Salida: “oPepito va al colegi”.
def corrimientoCircularDerecha(cadena):
    arreglo = []
    for i in range(len(cadena)):
        arreglo.append(cadena[i])
    ultima = arreglo.pop(len(cadena)-1)
    arreglo.insert(0, ultima)
    return "".join(arreglo)

# 79. Desarrollar un algoritmo que codifique una cadena de caracteres mediante una cadena de
# correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer
# car ́acter el car ́acter equivalente para el car ́acter ‘a’, el segundo car ́acter para la ‘b’y as ́ı suce-
# sivamente hasta la ‘z’. No se tiene traducci ́on para las may ́usculas ni para la ‘~n’.
# Ejemplo.
# Entrada: “al sur de Colombia” y “qwertyuiopasdfghjklzxcvbnm”.
# Salida: “qs lxk rt Cgsgdwoq”.
# Ejemplo.
# Entrada: “al sur de Colombia” y “zxcvbnmasdfghjklqwertyuiop”.
# Salida: “zg etw vb Ckgkhxsz”.

def codificar(cadena, codificador):
    if(len(codificador) != 26):
        return "Papi meta una cadena de 26 caracteres (Ñ) no. "
    codigo = ""
    for i in range(len(cadena)):
        if(cadena[i] == " " or cadena[i].isupper()):
            codigo += cadena[i]
        else:
            indice = index[cadena[i]]
            codigo += codificador[indice]
    return codigo

# 80. Desarrollar un algoritmo que decodifique una cadena de caracteres mediante una cadena de
# correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer
# car ́acter el car ́acter equivalente para el car ́acter ‘a’, el segundo car ́acter para la ‘b’y as ́ı suce-
# sivamente hasta la ‘z’. No se tiene traducci ́on para las may ́usculas ni para la ‘~n’.
# Ejemplo.
# Entrada: “qs lxk rt Cgsgdwoq” y “qwertyuiopasdfghjklzxcvbnm”.
# Salida: “al sur de Colombia”.
# Ejemplo.
# Entrada: “zg etw vb Ckgkhxsz” y “zxcvbnmasdfghjklqwertyuiop”.
# Salida: “al sur de Colombia”.
def descodificar(cadena, codificador):
    if(len(codificador) != 26):
        return "Papi meta una cadena de 26 caracteres (Ñ) no. "
    codigo = ""
    for i in range(len(cadena)):
        if(cadena[i] == " " or cadena[i].isupper()):
            codigo += cadena[i]
        else:
            where = dondeEsta(cadena[i], codificador)
            indice = index2[where]
            codigo += indice
    return codigo

def dondeEsta(letra, cadena):
    for i in range(len(cadena)):
        if(cadena[i]==letra):
            return i
    return None

print(descodificar("qs lxk rt Cgsgdwoq","qwertyuiopasdfghjklzxcvbnm"))