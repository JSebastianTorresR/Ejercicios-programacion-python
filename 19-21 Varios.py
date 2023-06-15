# 19. Si en la UN est ́an podando  ́arboles y cada rama tiene P hojas, y a cada  ́arbol le quitaron K
# ramas, cu ́antos  ́arboles se deben podar para obtener T hojas?.

def cuantosArboles(P, K, T, A=1):
    if(K*P*A >= T):
        return A
    else:
        return cuantosArboles(P,K,T,A+1)

# 20. Si un amigo, no tan amigo, me presta K pesos a i pesos de inter ́es diario, ¿cu ́anto le pagar ́e
# en una semana si el inter ́es es simple?, ¿y cu ́anto si el inter ́es es compuesto?.
def interesSimple(k, i):
    return (k * i/100 * 7) + k

def interesCompuesto(k, i):
    return k*((1+i/100)**7)

def cuantoPago(k, i):
    return interesSimple(k,i),  interesCompuesto(k,i)

# 21. Un ni ̃no se la pas ́o jugando con fichas de lego, tenia dos tipos de fichas de lego, fichas de
# cuadros de 1 × 1 (rojas) y fichas de cuadros de 2 × 1 (azules), y le dieron una base de 1 × n
# cuadritos, ¿de cu ́antas formas distintas puede ubicar las fichas rojas y azules sobre la base?,
# ¿y si le dan una ficha amarilla de 1 × 3?
def formasLego(n):
    return