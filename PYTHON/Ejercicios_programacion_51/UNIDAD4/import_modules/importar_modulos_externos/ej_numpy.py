import os
os.system ('cls')

import numpy as np

x = [0, 1, 2, 3, 4, 5]
print(x)
x_numpy = np.array([0, 1, 2, 3, 4, 5])
x_numpy2 = np.array(x)
print(x_numpy)
print(x_numpy2)



################ NUMPY ARRAYS

print('-------------------------NUMPY ARRAYS--------------------------')
## ARRAY CONVENCIONAL SIN NP
y_list = ([1,2,3], [4,5,6], [7,8,9])
print(y_list)

### ARRAYS = ARREGLOS - > ARREGLOS MULTIDIMENSIONALES
array_unidimensional = np.array([1,2,3,4,5,6])

array_bidimensional = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
print(array_bidimensional)

#ndim -> retorna el numero de dimensiones del array
print(array_bidimensional.ndim)
print(array_unidimensional.ndim)

# size -> retorna el numero total de elementos del array
print(array_bidimensional.size)
print(array_unidimensional.size)

# shape -> retorna una tupla que indica el numero de elementos de cada dimension

print(array_bidimensional.shape)
print(array_unidimensional.shape)

"""
Como importa la libreria numpy
"""
import numpy as np


"""
Cree un array de tipo numpy de 4 elementos e
impriman el tercer elemento del array
"""
A = np.array([0,1,2,3])
print(A[2])

"""
Que retorna la propiedad shape:
a) tuple
b) list
c) array
"""
#retorna un tuple

print('-----------------')

## agregar otro valor al array con append
B = np.array([10,15,4,65,1,2,3,4,5,6,7,8])
print(B)
B = np.append(B, 4)
print(B)
# Eliminar un valor del array
B = np.delete(B, 0)
print(B)
# organizar el array en orden ascendente con sort
B = np.sort(B)
print(B)



print('--------------------RANGE CON NUMPY----------------')

z = np.arange(3, 20, 4) #range(10), range(2, 9), range(1, 10, 2)

"""
Que devuelve este codigo
"""
x = np.arange(2, 8, 2)      # [2, 4, 6]
x = np.append(x, x.size)    # [2, 4, 6, 3]
x = np.sort(x)              # [2, 3, 4, 6]
print(x[1])                 # 3
#R = DEVUELVE '3' 


print('-------------------FUNCION RESHAPE-----------------')

c = np.arange(1, 7)
print(c)
print(c.shape)
d = c.reshape(3, 2)
print(d)
print(d.shape)

print('-------------------FUNCION RESHAPE INVERSO-----------------')
c = np.array([[1,2],[3, 4],[5, 6]])
print(c)
d = c.reshape(6)
print(d)


print('-------------------ejercicio--------------------')
"""
Cual es la salida de este codigo?
"""
d = np.arange(1,8,3)    #[1,4,7]
f = d.reshape(3,1)      #[[1], [4], [7]]
print(f[1][0])          # 4


print('-------------------INDEXING AND SLICING- INDICES Y REBANADAS--------------------')

x = np.arange(1, 10)
print(x)
print(x[0:2])#imprimir los dos primeros elementos
print(x[5:])#imprimir desla posicion 5
print(x[-1])#imprimir el ultimo elemento




print("-------------condiciones--------------------")

x = np.arange(1,20)
print(x)
#tomar los elementos menores a 8
print(x[x<8])
##tomar los elementos mayores a 5 y que sean pares
print(x[(x>5) & (x%2 ==0) ])


print('---------------EJERCICIO------------------')
"""
de un array "y" dado, realice la expresion donde me filtre
los elementos mayores a 15
"""
y = np.array([32,5,6,9,8,54,2,6,5,45])
z = y[y>15]
print(z)
print(z.size)


###OPERACIONES SOBRE ARRAYS

print("-------------OPERACIONES SOBRE ARRAYS--------------------")


#sum(), min(), max()

y = np.array([32,5,6,9,8,54,2,6,5,45])

print(y.sum())

print(y.min())
print(y.max())

print("-------------OPERACIONES SOBRE ARRAYS / BROADCASTING--------------------")



y = np.array([32,5,6,9,8,54,2,6,5,45])
print(y)
z = y * 2 
print(z)

print('----------')
lista_python = [1,2,3,4]
print(lista_python)
resultado_mul = lista_python * 2
print(resultado_mul)


print('--------------------EJERCICIO----------------')
"""
Convertir todos los valores en el array de megabytes a kilobytes. (1 megabyte
es 1024 kilobytes)
"""
datos_mb = np.array([2,4,10,3,65,32,28])
datos_kb = datos_mb * 1024
print(datos_kb)
print(datos_kb.max())


print("-------------OPERACIONES SOBRE ARRAYS / ESTADISTICAS--------------------")
x = np.array([5,6,8,14,65,39,52])
print(x)
print('MEDIA                 ->', np.mean(x))
print('MEDIANA               ->', np.median(x))
print('VARIANZA              ->', np.var(x))
print('DESVIACION ESTANDAR   ->', np.std(x))
