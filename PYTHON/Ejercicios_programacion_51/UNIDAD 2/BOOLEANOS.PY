def EsBisiesto(Año):
    A = Año % 4 == 0
    B = Año % 100 == 0
    C= Año % 400 == 0

    if (A) and (not B or C):
        resultado = "Es bisiesto"

    else:
        resultado = "No es bisisesto"

    return f"El {Año} es {resultado}"

print(EsBisiesto(2000))
print(EsBisiesto(2021))
print(EsBisiesto(2400))
print(EsBisiesto(1905))

