import os
os.system ("cls")
"""
numero = int(input("Ingrese su numero\n"))
while numero < 50:
    print (numero)
    if numero > 0:
        if (numero==2 or numero==3 or numero ==5):
            print("Es primo")
        elif((numero%2)==1):
            if((numero%5)==0 or (numero%3)==0):
                print("no es primo")
            else:
                print("Es primo")
    else:
        print("no cumple")
    numero = numero + 1
"""


def es_primo(n) -> bool:
    i = 1
    numerosDivisores = 0
    while i<=n:
        if(n % i == 0):
            numerosDivisores +=1
        i +=1
    
    if(numerosDivisores == 2):
        resultado = True
    else:
        resultado = False

    return resultado

print(es_primo(5))


def siguientePrimo(m) -> int:
    numero = m
    while es_primo(numero) == False:
        numero += 1
        
    return numero

print(siguientePrimo(15))

print(siguientePrimo(23))

print(siguientePrimo(182938))