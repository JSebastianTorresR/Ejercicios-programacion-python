# 14. Dadas la pendiente y el punto de corte de dos rectas, determinar si son paralelas, perpendi-
# culares o ninguna de las anteriores.
def parelalasPerpendiculares(m1, c1, m2, c2):
    if(m1 == m2 and c1 != c2):
        return "Paralelas"
    if(m1 == -1/m2):
        return "Perpendiculares"
    else:
        return "ninguna"
# 15. Dadas la pendiente y el punto de corte de dos rectas, determinar los puntos de intersecci ́on al
# origen.
def puntoDeInterseccion(m1,c1,m2,c2):
    corteX1 = -c1/m1
    corteX2 = -c2/m2
    recta1 = [corteX1, c1]
    recta2 = [corteX2, c2]
    return recta1, recta2


# 16. Dado el radio de un c ́ırculo, calcular el  ́area del triangulo que circunscribe el circulo (triangulo
# afuera).
def trianguloCircunscrito(r):
    return (((3**0.5)*r)*r/2) * 6


# 17. Dado el radio de un c ́ırculo, calcular el  ́area y per ́ımetro del cuadrado, pent ́agono y hex ́agono
# adentro (inscrito en un c ́ırculo) y afuera (inscribiendo al c ́ırculo).


# 18. Si una ara ̃na utiliza un patr ́on de hex ́agono regular para su telara ̃na, y cada hex ́agono est ́a
# separado del otro por 1cm, y la ara ̃na quiere hacer una telara ̃na de πr2, ¿qu ́e cantidad de
# telara ̃na requiere la ara ̃na?.