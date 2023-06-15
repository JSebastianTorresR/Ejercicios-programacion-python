# 5. Funcion potencia de un entero elevado a un entero.
def potencia(base, exponente):
    resultado = base
    for i in range(exponente):
        resultado *= base
    return resultado
    #base**exponente

# 6. Una funci ́on que determine si un n ́umero es divisible por otro.
def divisible(num, divisible):
    return num%divisible==0


# 7. Determinar si un n ́umero es primo.
def primo(num):
    s = True
    for i in range(2,num):
        if (num%i == 0):
            s = False
        if(not s):
            return s
    return s


# 8. Dados dos naturales, determinar si son primos relativos.
def primosRelativos(num1, num2):
    s = True
    for i in range(2,max(num1,num2)):
        if(num1%i==0 and num2%i==0):
            s = False
        if(not s):
            return s 
    return s

# 9. Determinar si un n ́umero es m ́ultiplo de la suma de otros dos n ́umeros.
def sumaMultiplo(multiplo, num1,num2):
    return multiplo%(num1+num2) ==0 


# 10. Dados los coeficientes de un polinomio de grado dos, evaluar el polinomio en un valor dado.
def polinimio2(a,b,c, evaluar):
    return (a*evaluar)**2 + (b*evaluar) + c

# 11. Dados los coeficientes de un polinomio de grado dos, calcular coeficiente lineal de la derivada.

def coeficienteLineal(a,b,c):
    return a

# 12. Dados los coeficientes de un polinomio de grado dos y un n ́umero real, evaluar la derivada del
# polinomio en ese n ́umero.
def evaluarDerivada(a,b,c, evaluar):
    return a*evaluar + b


# 13. Dado un natural, determinar si es un n ́umero de Fibonacci o no.
def numeroFibo(num, x=0, y=1):
   if(num == 0 or num == 1):
       return True
   fibo = x+y
   if(fibo == num):
       return True
   if(num<fibo):
       return False
   if(num>fibo):
       return numeroFibo(num, y, y+x)

