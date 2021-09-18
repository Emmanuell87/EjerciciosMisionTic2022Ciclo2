import os
os.system('cls')

import pandas as pd

#CREAR ARCHIVOS EN CUALQUIER FORMATO
"""
data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

#creamos un dataframe con los atributos del diccionario
datosDataFrame = pd.DataFrame(data)

print(datosDataFrame)

#Acaba la implementacion

#datosDataFrame.to_csv('example.csv')
#datosDataFrame.to_sql('example.sql')
datosDataFrame.to_excel('example.xls')
"""

#LEER ARCHIVOS DE CUALQUIER FORMATO
df = pd.read_excel('example.xls')
#print(df)



print('----Manejo de archivos de texto Abrir un archivo para leer o escribir en Python----')
# Abre el archivo para escribir y elimina los archivos anteriores si existen
"""fic = open("Archivos/text.txt", "w")"""
# Abre el archivo para agregar contenido
"""fic = open("Archivos/text.txt", "a")"""
# Abre el archivo en modo lectura
"""fic = open("Archivos/text.txt", "r")"""
#CERRAR EL ARCHIVO
"""fic.close()"""




print('\n\n---------Escribir archivos de texto en Python---------')
data = ["Linea 1", "Linea 2", "Linea 3", "Linea 4", "Linea 5"]

fic = open("text_1.txt", "w")

for line in data:
    fic.write(line)
    fic.write("\n")
    
fic.close()


#-------------
fic = open("text_2.txt", "w")

for line in data:
    print(line, file=fic)
    
fic.close()


#----------
fic = open("text_3.txt", "w")
fic.writelines("%s\n" % s for s in data)
fic.close()


print('\n\n---------Leer el archivo de una vez---------')
fic = open('text_1.txt', "r")
lines = fic.readlines()
print(lines)
fic.close()

#lerlo de linea a linea
fic = open('text_1.txt', "r")
lines = []

for line in fic:
    lines.append(line)

fic.close()
print(lines)

lines1 = [s.rstrip('\n') for s in lines]
print(lines1)



print('----------------ESCRIBIR ARCHIVOS JSON CON PYTHON-------------')
import json

data = {}
data['clients'] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)