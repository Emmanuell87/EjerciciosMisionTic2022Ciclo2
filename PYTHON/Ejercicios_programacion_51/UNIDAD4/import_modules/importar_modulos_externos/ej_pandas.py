import os
os.system('cls')


import pandas as pd
ventas= pd.Series([15, 12, 21])
print(ventas)
print('---------------AGREGAR INDICES----------------')
ventas= pd.Series([15, 12, 21], index= ['Ene', 'Feb', 'Mar'])
print(ventas)

print('---------------COMO ACCEDER A LOS VALORES----------------')
print(ventas[0]        , '-> ventas[0]')
print(ventas['Ene']    , '-> ventas["Ene"]')

print('---------------VER EL TIPO----------------')
print(ventas.dtype)

print('---------------ACCERDER A SUS INDICES Y VALUES----------------')
print(ventas.keys())
print(ventas.values)

print('---------------AGREGAR UN NOMBRE----------------')
ventas.name = 'Ventas 2020'
print(ventas)

print('---------------AGREGAR UN NOMBRE A LOS INDICES----------------')
ventas.index.name = 'Meses'
print(ventas)

print('---------------ACCEDER A LOS EJES DE LA SERIE(indice al ser unidimensional)----------------')
print(ventas.axes)

print('---------------ACCEDER AL TAMAÑO DE LA SERIE----------------')
print(ventas.shape)

print('******************************************************\n')

print('----------------CREAR DATAFRAMES A PARTIR DE DICCIONARIOS--------------------')

datos = {'manzanas' : [3, 2, 0, 1], 'naranjas' : [0, 3, 7, 2]}
compras = pd.DataFrame(datos)
print(compras)

print('---------------CREARLO CON NOMBRE DE INDICES DIRECTAMENTE-----------------------')
compras = pd.DataFrame(datos, index= ['Juno', 'Robert', 'Lily', 'David'])
print(compras)
print('---------------ACCEDER A SUS INDICES Y COLUMNAS-----------------------')
print(compras.index)
print(compras.columns)

print('\n-----ACCEDER A LOS EJES DE LA SERIE CON axe(INDICE Y COLUMNA AL SER BIDIMENSIONAL)-----')
print(compras.axes)

print('\n------------------AGREGAR NOMBRE A LA FILA Y COLUMNAS-------------------')
compras.index.name = 'Clientes'
compras.columns.name = 'Frutas'
print(compras)

print('-----------------------------VER EL DATAFRAME EN ARRAY NUMPY-------------------')
print(compras.values)

print('-----------------------------VER EL TAMAÑO DIMENSIONAL CON SHAPE-------------------')
print(compras.shape)

print('***********************************************************************\n')
print('----------------------------------CREAR SERIES--------------------------')
print('---------------UTILIZANDO LISTAS-----------------')

s = pd.Series([7,5,3])
print(s)

print('---------------UTILIZANDO DICCIONARIOS-----------------')
d = {"Ene":7, "Feb":5, "Mar":3 }
s = pd.Series(d)
print(s)



print('---------------CON OTRO DICCIONARIO-----------------')
elementos = { 
    "Numero atómico":[1, 6, 47, 88],
    "Masa atómica":[1.008, 12.011, 107.87, 226],
    "Familia":["No metal", "No metal", "Metal", "Metal"]
}
elementos

tabla_periodica = pd.DataFrame(elementos)
print(tabla_periodica)

print('--------LE AGREGAMOS US RESPECTIVOS INDICES Y COLUMNAS------')
tabla_periodica = pd.DataFrame(elementos,
                               index = ["H", "C", "Ag", "Ra"],
                               columns = ["Familia", "Numero atómico", "Masa atómica"]
)
print(tabla_periodica)



print('---------------UTILIZANDO UN ESCALAR-----------------')
s = pd.Series(7, index = ["Ene", "Feb", "Mar"])
print(s)


print('--------------------METODOS/ HEAD. TAIL. SAMPLE------------------')

print('--------------------CREAMOS UNA SERIE/ "ENTRADAS"-------------------')
entradas = pd.Series([11, 18, 12, 16, 9, 16, 22, 28, 31, 29, 30, 12],
            index = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago",
             "sep", "oct", "nov", "dic"])
print(entradas)

print('--------------------CREAMOS UNA SERIE/ "SALIDAS"-------------------')
salidas = pd.Series([9, 26, 18, 15, 6, 22, 19, 25, 34, 22, 21, 14],
            index = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago",
             "sep", "oct", "nov", "dic"])
print(salidas)

print('------------CREAMOS UN DATAFRAME CON LAS SERIES/ "ALMACEN"---------------')
almacén = pd.DataFrame({"entradas": entradas, "salidas": salidas})
almacén["neto"] = almacén.entradas - almacén.salidas
print(almacén)

print('--------------------HEAD(muestra los primeros 5 elementos)------------------')
print('*****head con la serie "entradas"******')
print(entradas.head())
print('*****head con el dataframe "almacen******')
print(almacén.head())

print('--------------------TAIL(muestra los ultimos 5 elementos)------------------')
print('*****tail con la serie "entradas"******')
print(entradas.tail())
print('*****tail con el dataframe "almacen******')
print(almacén.tail())

print('--------------------SAMPLE(selecciona una muestra al azar)------------------')
print('*****sample con la serie "entradas"******')
print(entradas.sample())
print('*****sample con atributos devuelve la cantidad especificada al azar(5)******')
print(entradas.sample(5))
print('\n*****sample con el dataframe "almacen******')
print(almacén.sample())
print('******sample con atributos devuelve la cantidad especificada al azar(5)******')
print(entradas.sample(5))


print('\n------------------------METODO DESCRIBE------------------\n')
print('*****DEVUELVE LA INFORMACION ESTADISTICA DE LSO DATOS DEL DATAFRAME*******')
print(almacén.describe())

print('\n------------------------METODO INFO------------------\n')
print('******MUESTRA UN RESUMEN DE LA INFORMACION DE UN DATAFRAME*******')
print(almacén.info())

print('\n------------------------METODO VALUE_COUNTS------------------\n')
print('******DEVUELVE AL FRECUENCIA CON LA QUE SE PRESENTA UN VALOR*******')
import numpy as np
s = pd.Series([3, 1, 2, 1, 1, 4, 1, 2, np.nan])
print(s)
print('\nvalue_counts\n',s.value_counts())
print('contar el NaN',s.value_counts(dropna = False))

print('\n\n----------------SELECCIONAR ELEMENTOS CON INDICES POR DEFECTO O POR SU NOMBRE---------')
s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])
print(s)
print(s["a"],s[0],'  -> ej   s["a"],s[0]')
print(s["d"],s[3],'  -> ej   s["d"],s[3]')

print('*********USO DE RANGOS******')
print('***con indices por defecto***')
print(s[1:])
print(s[:3])
print(s[1:3])
print('*** O con indices asignados***')
print(s["a":"c"])
print(s[:"c"])
print(s["b":])

print('--------------------------------METODO LOC------------------------')
print('****Podemos acceder al los indices solo por medio de su etiqueta*****')
print(s.loc["b"])
print('--------------------------------METODO LOC------------------------')
print('****Podemos acceder al los indices solo por medio de su indice*****')
print(s.iloc[1])
