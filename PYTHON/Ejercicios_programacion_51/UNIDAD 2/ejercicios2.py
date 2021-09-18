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

es_primo = num_primos.get(str(num))

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

#  7
"""
num1 = int(input("Ingrese un número entero\n"))
num2 = int(input("Ingrese un número entero\n"))

if (num1 > num2):
    print(f"{num1} es mayor que: {num2}")
else:
    print(f"{num2} es mayor que: {num1}")
"""

#  8
# Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos
# los dígitos.
"""
num1 = int(input("Ingrese un número entero de 2 dígitos\n"))

dec = int(num1/10)
uni = num1- (dec*10)

num2 = int(input("Ingrese un número entero de 2 dígitos\n"))

dec2 = int(num2/10)
uni2 = num2- (dec2*10)

total = int(dec+uni+dec2+uni2)

print(f"La suma te todos los dígitos es: {total}")
"""

#9

"""
num = int(input("Ingrese un número entero de 3 dígitos\n"))

if (num > 99 and num <1000):
    cen = int(num/100)
    num -= cen*100
    dec = int(num/10)
    uni = num- (dec*10)
    if (cen > dec and cen > uni):
        print("El dígito de la centena es mayor que los otros dígitos")
    elif (dec > cen and dec > uni):
        print("El dígito de la decena es mayor que los otros dígitos")
    else: 
        print("El dígito de la unidad es mayor que los otros dígitos")
else:
    print("Por favor ingrese un número de 3 dígitos")

"""

# 10
#Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros
"""
num = int(input("Ingrese un número entero de 3 dígitos\n"))

if (num > 99 and num <1000):
    cen = int(num/100)
    num -= cen*100
    dec = int(num/10)
    uni = num- (dec*10)

    if (cen % dec == 0):
        print(f"El dígito de la centena ({cen}) es multiplo de el dígito de la decena ({dec}")
    if (cen % uni == 0):
        print(f"El dígito de la centena ({cen}) es multiplo de el dígito de la unidad ({uni}")
    if (dec % cen == 0 ):
        print(f"El dígito de la decena ({dec}) es multiplo de el dígito de la centena ({cen}")
    if (dec % uni == 0 ):
        print(f"El dígito de la decena ({dec}) es multiplo de el dígito de la unidad ({uni}")
    if (uni % cen == 0 ):
        print(f"El dígito de la unidad ({uni}) es multiplo de el dígito de la centena ({cen}") 
    if (uni % dec == 0 ):
            print(f"El dígito de la unidad ({uni}) es multiplo de el dígito de la decena ({dec}")  
    else:
            print("Ningun dígito es divisible entre otro dígito del mismo número")
else:
    print("Por favor ingrese un número de 3 dígitos")
"""

#  11
# Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra
# el mayor dígito. 
"""
num1 = int(input("Ingrese un número entero de 2 dígitos\n"))

dec = int(num1/10)
uni = num1- (dec*10)

num2 = int(input("Ingrese un número entero de 2 dígitos\n"))

dec2 = int(num2/10)
uni2 = num2- (dec2*10)

num3 = int(input("Ingrese un número entero de 2 dígitos\n"))

dec3 = int(num3/10)
uni3 = num3- (dec3*10)

numeros = (dec, uni, dec2, uni2, dec3, uni3)
ordenados = sorted(numeros, reverse=True)

print(ordenados)
print(ordenados[0])

if (ordenados[0] == dec):
    print("El dígito de la decena del primer número es el mayor de todos los dígitos")
elif (ordenados[0] == uni):
    print("El dígito de la unidad del primer número es el mayor de todos los dígitos")
elif (ordenados[0] == dec2):
    print("El dígito de la decena del segundo número es el mayor de todos los dígitos")
elif (ordenados[0] == uni2):
    print("El dígito de la unidad del segundo número es el mayor de todos los dígitos")
elif (ordenados[0] == dec3):
    print("El dígito de la decena del tercer número es el mayor de todos los dígitos")
else:
    print("El dígito de la unidad del tercer número es el mayor de todos los dígitos")
"""

#  12


#  13
#Leer un número entero menor que 50 y positivo y determinar si es un número primo. 
"""
try:
    num = int(input("Ingrese un número menor a 50 y positivo\n"))

    num_primos = {
        '2' : True,
        '3' : True , 
        '5' : True, 
        '7' : True, 
        '11' : True, 
        '13' : True, 
        '17' : True,
        '19' : True,
        '23' : True,
        '29' : True,
        '31' : True,
        '37' : True,
        '41' : True,
        '43' : True,
        '47' : True,
    }

    a = num_primos.get(str(num))

    if (a == True):
        print("Su número es primo")
    else:
        print("Su número no es primo")

except:
    print("Por favor ingrese un número entero positivo menor a 50\n")
"""

#  14 
#  Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al
#  penúltimo. 
"""
num = int(input("Ingrese un número entero de 4 dígitos\n"))

if (num > 999 and num < 10000):
    1210
    segundo_dígito = int(num/10-100)
    tercer_dígito = int(num/100-10)

    if(segundo_dígito == tercer_dígito):
        print(f"El segundo ({segundo_dígito}) y penultimo dígito ({tercer_dígito}) son iguales")
    else:
        print(f"El segundo ({segundo_dígito}) y penultimo dígito ({tercer_dígito}) no son iguales")
else:
    print("Debe ingresar un número entero de 4 dígitos")
"""

#  15
#  Leer un número entero y determinar si es múltiplo de 7.
"""
try:
    num = int(input("Ingrese un número entero\n"))

    if(num % 7 == 0):
        print(f"El número {num} es múltiplo de 7")
    else:
        print(f"El número {num} no es múltiplo de 7")

except:
    print("Por favor ingrese un número entero\n")
"""

#  16
#  Leer un número entero menor que mil y determinar cuántos dígitos tiene.
"""
try:
    num = int(input("Ingrese un número menor que 1000"))

    if (num > 99 and num < 1000):
        print(f"El número {num} tiene 3 dígitos")
    elif(num > 9 and num < 100):
        print(f"El número {num} tiene 2 dígitos")
    elif(num >= 0 and num < 10):
        print(f"El número {num} tiene 1 dígito")
    else:
        print("Por favor ingrese un número que cumpla con los requisitos")
except:
    print("Por favor ingrese un número entero menor que 1000")
"""
#  17
#  Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares. 
"""
try:
    num = int(input("Ingrese un número entero"))

    
except:
    """