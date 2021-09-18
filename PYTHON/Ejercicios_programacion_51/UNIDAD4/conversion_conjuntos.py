#Importaciones para borrar consola al inicio
import os
os.system ("cls")



print('\n\n**********************************CONVERSION DE CADENAS**********************************\n\n')
print('---------CONVERTIR UNA CADENA A LISTA--------')
cadena = "Hola mundo!"
lista = list(cadena)
print(lista)
print('****************************')

print('---------CONVERTIR UNA CADENA A TUPLA--------')
cad = 'Hola'
cad2 = 'adiós'
num = 15
tupla1 = tuple(cad)
tupla_general = (tupla1, num, tuple(cad2))
print(tupla_general)
print('****************************')

print('---------CONVERTIR UNA CADENA A CONJUNTO--------')
cadena = 'hhola'
conjunto = (set(cadena))
print(conjunto)
print('****************************')


print('\n\n**********************************CONVERSION DE LISTAS**********************************\n\n')
print('---------CONVERTIR UNA LISTA A UNA CADENA--------')
lista = ['h', 'o', 'l', 'a']
nueva_cadena = ''.join(lista)
print(nueva_cadena)
print('****************************')

print('---------CONVERTIR UNA LISTA A TUPLA--------')
lista = ['h', 'o', 'l', 'a', 123]
tupla = tuple(lista)
print(tupla)
print('****************************')

print('---------CONVERTIR UNA LISTA A CONJUNTOS--------')
lista = ['h', 'o', 'o', 'l', 'a', 1, 1, 2]
conjunto = (set(lista))
print(conjunto)
print('****************************')


print('\n\n**********************************CONVERSION DE TUPLAS**********************************\n\n')
print('---------CONVERTIR UNA TUPLA A CADENA--------')
tupla = ('h', 'o', 'l', 'a')
cadena = ''.join(tupla)
print(cadena)
print('****************************')

print('---------CONVERTIR UNA TUPLA A LISTA--------')
tupla = ('hola', 111, 'mundo')
lista = list(tupla)
print(lista)
print('****************************')

print('---------CONVERTIR UNA TUPLA A CONJUNTO--------')
tupla = ('hola', 111, 'mundo', 'hola')
conjunto = set(tupla)
conjunto.add(15)
print(conjunto)
print('****************************')


print('\n\n**********************************CONVERSION DE CONJUNTOS**********************************\n\n')
print('---------CONVERTIR UN CONJUNTO A CADENA--------')
conjunto = {'h', 'o', 'l', 'a'}
cadena = ''.join(conjunto)
print(cadena)
print('****************************')

print('---------CONVERTIR UN CONJUNTO A TUPLA--------')
conjunto = {'h', 'o', 'l', 'a'}
tupla = tuple(conjunto)
print(tupla)
print('****************************')

print('---------CONVERTIR UN CONJUNTO A LISTAS--------')
conjunto = {'h', 'o', 'l', 'a'}
lista = list(conjunto)
print(lista)
print('****************************')


print('\n\n**********************************CONVERTIR A DICCIONARIOS**********************************\n\n')
print('---------CONVERTIR DE CADENA A DICCIONARIO--------')
cadena = 'hola'
diccionario = dict(zip(range(len(cadena)), (cadena)))
print(diccionario)
print('****************************')

print('---------CONVERTIR DE LISTA A DICCIONARIO--------')
lista = ['h', 'o', 'l', 'a']
diccionario = dict(zip(range(len(lista)), (lista)))
print(diccionario)
print('****************************')

print('---------CONVERTIR DE TUPLA A DICCIONARIO--------')
tupla = ('h', 'o', 'l', 'a')
diccionario = dict(zip(range(len(tupla)), (tupla)))
print(diccionario)
print('****************************')

print('---------CONVERTIR DE CONJUNTO A DICCIONARIO--------')
conjunto = {'h', 'o', 'l', 'a'}
diccionario = dict(zip(range(len(conjunto)), (conjunto)))
print(diccionario)
print('****************************')

print('\n\n**********************************CONVERTIR DICCIONARIOS**********************************\n\n')
print('---------CONVERTIR DE DICCIONARIO A CADENA--------')
diccionario = {0: 'h', 1: 'o', 2: 'l', 3: 'a'}
cadena = ''.join(diccionario.values())
print(cadena)
print('****************************')


print('---------CONVERTIR DE DICCIONARIO A TUPLA--------')
diccionario ={
    "Clave1" : 56,
    65.5: "valor2",
    (52,6): "valor3"
}
tuplaLlaves = tuple(diccionario.keys())
print(tuplaLlaves)
tuplaValores = tuple(diccionario.values())
print(tuplaValores)
tuplaItems = tuple(diccionario.items())
print(tuplaItems)
print('****************************')

print('---------CONVERTIR DE DICCIONARIO A TUPLA--------')
diccionario ={
    "Clave1" : 56,
    65.5: "valor2",
    (52,6): "valor3"
}
listaLlaves = list(diccionario.keys())
print(listaLlaves)
listaValores = list(diccionario.values())
print(listaValores)
listaItems = list(diccionario.items())
print(listaItems)
print('****************************')

print('---------CONVERTIR DE DICCIONARIO A COJUNTOS--------')
diccionario ={
    "Clave1" : 56,
    65.5: "valor2",
    (52,6): "valor3"
}
conjuntoLlaves = set(diccionario.keys())
print(conjuntoLlaves)
conjuntoValores = set(diccionario.values())
print(conjuntoValores)
conjuntoItems = set(diccionario.items())
print(conjuntoItems)
print('****************************')


print('\n\n**********************************EJERCICIOS**********************************\n\n')
#Tengo una cadena de caracteres y quiero modificar la cadena
#en diferentes posiciones, como lo puedo hacer?

cadena = "abcdef"

lista_cadena = list(cadena)
lista_cadena[3]= "e"
print(lista_cadena, '  ->  LISTA MODIFICADA')

cadena_modificada = ''.join(lista_cadena)
print(cadena_modificada, '     -> CADENA MODIFICADA POR LISTA')

print('****************************')

cadena= "sssddddsssjwerpssspdlll1llllasdf3365"
conjunto_cadena = set(cadena)
print(conjunto_cadena, '      -> CONJUNTO MODIFICADO')

nueva_cadena_desde_conjunto = ''.join(conjunto_cadena)
print(nueva_cadena_desde_conjunto, '      ->    CADENA MODIFICADA POR CONJUNTO')