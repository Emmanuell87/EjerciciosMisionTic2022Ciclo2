import os
os.system ('cls')


#   8
#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:a) De cada triángulo la medida de su base, su altura y su superficie.b) La cantidad de triángulos cuya superficie es mayor a 12.


#datos_triangulo = {(i): [ x for x in range(5)] for i in range(6)}
"""
datos_triangulo = {
    2 : 5,
    3 : 6.5, 
    5 : 5,
    6 : 11, 
    4.5 : 6.4,
    8 : 4
}
base = datos_triangulo.keys()
altura = datos_triangulo.values()

cantidad_datos = datos_triangulo.items()

for base, altura in cantidad_datos:
    superficie = (base*altura)/2
    print(f'La base del triángulo es {base}cm, su altura es {altura}cm y su superficie es {superficie}cm²')

"""
#   9
#Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados
"""
x = []
for i in range(10):
    y = float(input('Ingrese un número\n'))
    if i >= 5:
        x += [y]
print(x)
"""

#  10
#Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)
"""
for i in range(5, 51, 5):
    print(i)
"""

#  11
#Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

"""
num= int(input('Ingrese un número del 1 al 10\n'))
for i in range(1, 13):
    tabla_multiplicar= num*i
    print(tabla_multiplicar)
"""

#  12
#  Realizar un programa que lea los lados de n triángulos, e informar: a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual) b) Cantidad de triángulos de cada tipo.
"""
lados_triangulo = [(3, 3, 3), (4, 5, 6), (5, 7, 5), (4, 7, 5), (6, 6, 6), (9, 4, 9)]

for i in lados_triangulo:
    print(i)
    lados = set(i)
    h = ''
    for x in i:
        h += f'{str(x)}, ' 
        
    if len(lados)==1:
        print(f'Equilátero')
    if len(lados)==2:
        print(f'Isósceles')
    if len(lados)==3:
        print(f'Escaleno')   

"""
