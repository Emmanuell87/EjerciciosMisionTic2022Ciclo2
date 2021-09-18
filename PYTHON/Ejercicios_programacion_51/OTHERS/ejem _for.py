"""
def ejem_listas_paralelas():
    nombres=[]
    edades=[]

    for x in range(5): #range(0:2)-------------- [0,1,2,3,4]
        nom = input("Ingrese el nombre de la persona: ")
        nombres.append(nom)
        edad = int(input("Ingrese la edad de la persona: "))
        edades.append(edad)

    print("Nombre de las personas mayores de edad: ")
    for y in range(5):#------------ [0,1,2,3,4]
        if edades[y] >= 18:
            print(f"{nombres[y]} con edad de {edades[y]}")

ejem_listas_paralelas()
"""

Lista= [
    [1, 2, 3],
    [4, 5, 6],
    [7,8, 9]
]
"""
print (Lista[1][1:])

for i in Lista:
    print(Lista[i][0])
for i in Lista[0]:
    print(i)
"""
lista2= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

for i in range(len(lista2)): 
    for j in lista2[i]: 
        print(lista2[ i ][ j ])

