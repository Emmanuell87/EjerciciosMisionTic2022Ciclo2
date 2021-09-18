import os
os.system ('cls')


cubos = [ i**3 for i in range(0, 6)]
print(cubos)
print('*********************************')




mi_diccionario = dict()
for y in range(3, 11):
    mi_diccionario[(y, y**3)] = []
    for x in range(4, 31, 2):
        if x%y == 0:
            mi_diccionario[(y, y**3)].append(x**2)

#print(mi_diccionario)


#EN VEZ DEL CODIGO ANTERIOR PODEMOS CREAR ALGO COMO ESTO EN UNA SOLA LINEA QUE HARA EXACTAMENTE LO MISMO
mi_diccionario = { (x, x**3) : [ y**2 for y in range(4,31,2) if y%x == 0 ] for x in range(3, 11) }
print(mi_diccionario)

multiplos3 = [i for i in range(21) if i%3 == 0 ]
print(multiplos3)
print('****************************')






a = [i*10 for i in range(5, 16)]

print(a)
print('****************************')




#CONVERTIR DICCIONARIO A LISTA, QUE GUARDA CLAVE Y VALOR POR TUPLAS
dicionarios = {
    'clave1' : 56,
    55.6 : 'valor1',
    (34, 'r') : 23
}

lista = list(dicionarios.items())
print(lista)
print('****************************')




nums = [i*2 for i in range(0, 10)]
print(nums)
"""
Que hace el codigo anterior:
a) Una lista de todos los numeros del 0 al 10
b) Una lista de numeros pares entre 0 y 18
c) Una lista de numeros pares entre 0 y 18
"""
# R/= b
print('****************************')




pares = [i**2 for i in range(10) if i%2 == 0]
print(pares)
print('****************************')




#Crear una lista de multiplos del 3  desde 0 hasta el 20
multiplos3 = [i for i in range(21) if i%3 == 0] 
print(multiplos3)
print('****************************')



"""
Crear una lista de numeros multiplicados por 10
en un rango del 5 al 15
"""
multiplos10 = [i*10 for i in range(5, 16)]
print(multiplos10)

lista_num = [1, 2, 3, 4, -4, -1, 5]              # m
l = [num for num in lista_num if num > 0]
print(l)
lista_string = ['M', 'U', 'N', 'D', 'O']          # c
lista3 = [c*3 for c in lista_string]
print(lista3)
lista4 = [c*m for c in lista_string 
                    for m in lista_num
                        if m > 0]
print(lista4)