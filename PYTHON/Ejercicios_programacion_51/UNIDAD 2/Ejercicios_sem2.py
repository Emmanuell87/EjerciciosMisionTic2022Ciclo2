import os
os.system ("cls")

#  1 
#  Leer un número entero y determinar si es un número terminado en 4. 
"""
num = int(input("Ingrese un número entero\n"))

num1 = int(num/10)
num -= num1*10

if (num == 4):
    print("su número termina en 4")
else:
    print("su número no termina en 4")
"""

#  2
#  Leer un número entero y determinar si tiene 3 dígitos. 
"""
num = int(input("ingrese un número\n"))

if (num>99 and num<1000):
    print("Su número tiene 3 dígitos")
else:
    print("Su número no es de 3 dígitos")
"""

#  3
# Leer un número entero de dos dígitos y determinar si ambos dígitos son pares. 

"""
num = int(input("Ingrese un número entero de 2 dígitos\n"))
dec = int(num/10)
print(dec)
uni = num- (dec*10)
print(uni)

if(num < 100 and num > 9):
    if (dec % 2 ==0 and uni % 2 ==0):
        print("Ambos dígitos son pares")
    else:
        print("Ambos dígitos no son pares")
else:
    print("Por favor ingrese un número de 2 dígitos")
"""

#  4
#  Leer un número entero de dos dígitos menor que 20 y determinar si es primo. 

num = int(input("ingrese un número menor a 20\n"))

num_primos = {
    '2' : True,
    '3' : True , 
    '5' : True, 
    '7' : True, 
    '11' : True, 
    '13' : True, 
    '17' : True,
    '19' : True
}

es_primo = num_primos.get(str(2))

if (es_primo == True):
    print("Es un número primo")
else:
    print("No es un número primo")
























#  5
#  Leer un número entero de dos dígitos y determinar si es primo y además si es negativo. 
"""
num = int(input("ingrese un número menor a 20\n"))

num_primos = {
    '2' : True,
    '3' : True , 
    '5' : True, 
    '7' : True, 
    '11' : True, 
    '13' : True, 
    '17' : True
}

a = num_primos.get(str(num))

if (a == True):
    print("Es un número primo")
elif (num<0):
    print("Es un número negativo")
else:
    print("El número no es primo ni negativo")
"""

#  6
#  Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
"""
num = int(input("Ingrese un número entero de 2 dígitos\n"))

dec = int(num/10)
uni = num- (dec*10)

if(num >= 10 and num < 100 ):
    if (dec == uni):
        print("Los dos dígitos son iguales")
    else:
        print("Los dígitos no son iguales")
else:
    print("Por favor ingrese un número de dos dígitos")
"""