# 1) Si una vaca necesita M metros cuadrados de pasto para producir X litros de leche, ¿cuantos
# litros de leche se producen en la granja

def litrosLeche(metros, n, m):
    corral = n*m
    return corral/metros

# 2. Si 1~3 de las aves que hay en la granja son gallinas, y la mitad de las gallinas ponen 1 huevo
# cada 3 d ́ıas y la otra mitad 1 huevo cada 5 d ́ıas, ¿en un mes cu ́antos huevos producen?
# (1 mes ≡30 d ́ıas)

def cuantosHuevos(A):
    return A/6 * 10 + A/6 * 6

#3. Si los escorpiones de la granja se venden a China, y hay escorpiones de tres diferentes tama ̃nos:
# peque ̃nos (con un peso de 20 gramos), medianos (con un peso 30 gramos) y grandes (con
# un peso de 50 gramos), ¿cu ́antos kilos de escorpiones se pueden vender sin que decrezca la
# poblaci ́on a menos de 2~3?

def kilosEscorpion(E, g, m, p):
    limite = E/3
    poblacionRestante = limite
    if(g >= limite):
        return poblacionRestante * 0.05
    poblacionRestante -= g
    if(g+m >= limite):
        return g*0.05 + poblacionRestante * 0.03
    poblacionRestante -= m
    if(g+m+p >= limite):
        return g*0.05 + m*0.03 + poblacionRestante*0.02
    
# Al granjero se le da ̃no el corral y no sabe si volver a cercar el corral con madera, alambre de
# p ́uas o poner reja de metal. Si va a cercar con madera debe poner 4 hileras de tablas, con
# varilla 8 hileras y con alambre solo 5 hileras,  ́el quiere saber que es lo menos costoso para
# cercar si sabe que el alambre de p ́uas vale P por metro, las tablas a Q por metro y las varillas
# S por metro. Dado el tama ̃no del corral y los precios de los elementos, ¿cu ́al cerramiento es
# el m ́as econ ́omico?

def cercar(P,Q,S, N, M):
    tamaño = 2*N + 2*M
    precioMadera = 4*Q*tamaño
    precioVarilla = 8*S*tamaño
    precioPuas = 5*P*tamaño
    return min(precioMadera, precioPuas, precioVarilla)
