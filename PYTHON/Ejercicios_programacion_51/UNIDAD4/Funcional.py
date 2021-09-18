import os 
os.system ('cls')


print('**********************************EJEMPLO 1**********************************')
#FUNCION QUE APLIQUE DOS VECES UNA FUNCION
def aplicar_dos_veces(fun, arg):
    return fun(fun(arg))
#LA FUNCION QUE VA A SER APLICADA
def sumar_cinco (x):
    return 5+x
print(aplicar_dos_veces(sumar_cinco, 10))


print('**********************************EJERCICIO**********************************')
"""
Cual es la salida de este codigo?
"""
def prueba(fun, arg):
    return fun(fun(arg))
def mult(x):
    return x*x
print(prueba(mult, 3))


print('**********************************EJEMPLO 2**********************************')
def suma(val1 = 0, val2 = 0):
    return val1 + val2
def operacion(funcion, val1 = 0, val2 = 0):
    return funcion(val1, val2)
funcion_suma = suma
resultado = operacion(funcion_suma, 10, 20)
print(resultado)


print('*****EJEMPLO 2.1********')
def crear_funcion(operador):
    if operador == '+':
        def suma (val1 = 0, val2 = 0):
            return val1 + val2
        return suma
def operacion(funcion, val1 = 0, val2 = 0):
    return funcion(val1, val2)
funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma, 10, 20)
print(resultado)



print('**********************************EJEMPLO FUNCIONES ANONIMAS**********************************')
print('************EJEMPLO 1*************')
suma = lambda val1 = 0, val2 = 0: val1 + val2
operacion = lambda operacion, val1 = 0, val2 = 0: operacion(val1, val2)
resultado = operacion(suma, 10, 20)
print(resultado)


print('************EJEMPLO 2 con funcion lambda*************')
def mi_funcion( f, arg):
    return f(arg)
resultado = mi_funcion(lambda x: 2*x*x, 5)
print(resultado)
print('************EJEMPLO 2 sin funcion lambda*************')
def al_cuadrado_por_2(x):
    return 2*x*x
resultado = mi_funcion(al_cuadrado_por_2, 5)


print('************EJEMPLO 3 sin funcion lambda*************')
def polinomial(x):
    return x**2 + 5*x + 4
print(polinomial(-4))
print('************EJEMPLO 3 con funcion lambda*************')
resultado = ((lambda x: x**2+5*x+4)(-4))
print(resultado)


print('**********EJERCICIO*************')
"""
Crear una funcion lambda que devuelve el cuadrado de su argumento 
y llamarla con el numero 8
"""
resultado = ((lambda x: x*x)(8))
print(resultado)



print('****************************FUNCIONES MAP/FILTER/ZIP/REDUCE**********************************')
print("*************EJEMPLO FUNCION MAP**************")
def cuadrado(elemento =0):
    return elemento * elemento
lista = [0,1,2,3,4,5,6,7,8,9,10]
resultado = list(map(cuadrado, lista))
print(resultado)

print('*******************EJERCICIO*************')
"""
Dada una lista nums, sumar a cada elemento de la lista 20
"""
lista = [0,1,2,3,4,5,6,7,8,9,10]
resultado = list(map(lambda x: x+20, lista))
print(resultado)

print('*******************EJERCICIO 2*************')
"""
Dada una lista, multiplique cada elemento de la lista por 3 usando
la sintaxis lambda
"""
lista_numeros = [7,8,9,10,11,12]
resultado= list(map(lambda x: x*3, lista_numeros))
print(resultado)

print('*******************EJERCICIO 3/ FUNCION LAMBDA CON 2 O MAS ARGUMENTOS*************')
lista_numeros = [7,8,9,10,11,12]
lista_numeros2 = [2,3,4,5,6,7]
resultado= list(map(lambda x,y: x*y  , lista_numeros, lista_numeros2))
print(resultado)



print("*************EJEMPLO FUNCION FILTER**************")
print("*************SIN LAMBDA**************")
def mayor_a_cinco(elemento = 0):
    return elemento>5
tupla = (6,9,10,15,78,5,76,23,18,39,7,1,0,-5)
resultado = tuple(filter(mayor_a_cinco, tupla))
print(tupla)
print(resultado, ' ->  filtro los elemento mayor a 5')

print("*************CON LAMBDA**************")
resultado = tuple(filter(lambda x: x>5, tupla))
print(resultado,  ' ->  filtro los elemento mayor a 5')


print("*************EJEMPLO FUNCION REDUCE**************")
#HAY QUE IMPORTAR LA FUNCION REDUCE
from functools import reduce
print('***************EJERCICIO 1***********')
print("*****SIN LAMBDA******")
lista = [1,2,3,4]
def funcion_acumulador(acumulador = 0, elemento =0 ):
    return acumulador+elemento
resultado = reduce(funcion_acumulador, lista)
print(resultado)

print("*******CON LAMBDA*******")
lista = [1,2,3,4]
resultado = reduce(lambda x,y: x+y, lista)
print(resultado)

print('*************************EJERCICIO 2**********************')
print('***CONCATENAR TODOS LOS ELEMENTOS DE UNA LISTA***')
lista = ['Python', 'Java', 'Ruby', 'Elixir']
resultado = reduce(lambda acumulador='', elemento='': acumulador + " - " + elemento, lista)
print(resultado)

print('*************************EJERCICIO 3**********************')
lista = [1,2,3,4]
resultado = reduce(lambda x, y: x+y, lista, 10)
print(resultado)


print("************************************EJEMPLO FUNCION ZIP***************************")
nombres = ['Raul', 'Pedro', 'Sofia']
apellidos = ['Lopez Briega', 'Perez', 'Gonzales']
nombreApellido = list(zip(nombres, apellidos))
print(nombreApellido)





print("\n\n***********************EJERCICIOS CON MAP, FILTER, REDUCE O ZIP***************************")

print('************EJERCICIO 1*********')
"""
Dada una lista de años de nacimiento, calcular cuantos
años tendran estas personas en el año 2050, y devolver 
la lista resultante
"""
años_nacimiento = [1998, 2006, 2018, 2000, 1999, 1988, 1996, 1972]
resultado = list(map(lambda x: 2050-x, años_nacimiento))
print(resultado)



print('************EJERCICIO 2*********')
"""
Crear una tabla para sumar
"""
def mi_suma(a,b):
    resultado = a+b
    print(f'{a} + {b} = {resultado}')
    return resultado
numeros = [0,1,2,3,4]
reduce(mi_suma, numeros)


print('************EJERCICIO 3*********')
def imprime_mult(n):
    print(f'12 x {n} = {n*12}')
resultado = list(map(imprime_mult, range(1,11)))
print('************EJERCICIO 3.1*********')
def multiplicar(cons, n):
    print(f'{cons} x {n} = {n*cons}')
constante_de_12 = [12 for i in range(1,11)]
print(constante_de_12)
resultado = list(map(multiplicar, constante_de_12, range(1, 11)))