import os
os.system ('cls')

#Las lsitas son perfectas, para cuando necesitemosmodificar los datos dentro de esta 
itinerarios = [['Santa Marta',1],['Cartagena',2],["San Andres",4] ]
print(itinerarios)
#la funcion append, me agrega nuevos datos a la lista
itinerarios.append(['providencia',2])
print(itinerarios)
#La funcion pop nos elimina un elemento de la lista
itinerarios.pop(1)
print(itinerarios)
#Agrega un dia a dato asignado(en este caso a santa marta)
itinerarios[0][1] = itinerarios[0][1] + 1
print(itinerarios)
#Cambia de posiciones en la lista, el primer y ultimo dato
itinerarios[0], itinerarios[-1] = itinerarios[-1], itinerarios[0]
print(itinerarios)

print("\n\n\n")
for i, destino in enumerate(itinerarios):
    print(f'posición: {i}')
    print(destino)