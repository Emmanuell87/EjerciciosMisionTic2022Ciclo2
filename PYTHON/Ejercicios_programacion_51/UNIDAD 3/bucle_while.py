import os
os.system ('cls')


def desea_seguir():
    opcion2 = input("Si desea regresar al menú de opciones digite '1' de lo contrario digite '-1'\n")
    if(opcion2=='-1'):
        return print('Hasta pronto')
    else:
        opciones()

#  1
#  Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos 
#  tienen notas mayores o iguales a 7 y cuántos menores.

def notasAlumnos():
    nota = 1
    notaMayores_6 = 0
    notaMenores_7 = 0
    while nota <= 10:
        
        
        value = float(input('Ingrese nota de alumno\n'))
        if value >= 7:
            notaMayores_6 += 1
        else: 
            notaMenores_7 += 1
        nota += 1


    print(f"{notaMayores_6} Alumnos tienen notas mayores o igual a 7 y {notaMenores_7} Alumnos tienen notas menores a 7")
    
    deseaSeguir = desea_seguir()
    return deseaSeguir


#  2
#  Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio 
#  de las personas.

def alturapersonas():
    salir = "Ingresa la altura de la persona o digita -1 si ya has terminado\n"
    
    opcion = float(input(salir))
    altura = 0
    x = 0
    while opcion != -1:
        
        value = float(opcion)
        altura += value
        x += 1
        opcion = float(input(salir))
        

    prom_altura = round(altura/x, 2)

    print(f"\nLa altura promedio de las personas es: {prom_altura}m")

    deseaSeguir = desea_seguir()
    return deseaSeguir



#  3
#   En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
def sueldos():
    salir = "Ingresa el sueldo del empleado o escribe '-1' si ya has acabado de ingresar los datos\n"
    opcion = float(input(salir))

    gastoEnSueldos = 0
    cobro100y300 = 0
    cobroMas300 = 0
    while opcion != -1:
        
        value = float(opcion)
        gastoEnSueldos += value
        if(value >= 100 and value <= 300):
            cobro100y300 += 1
        else:
            cobroMas300 += 1
        opcion = float(input(salir))


    print(f"{cobro100y300} empleados cobran entre $100 y $300 y {cobroMas300} empleados cobran más de 300, además la empresa tiene un gasto total de ${gastoEnSueldos} en sueldo al personal")

    deseaSeguir = desea_seguir()
    return deseaSeguir

#  4  
#  Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)

def serie11():
    x = 0
    serie = 0
    while x < 25:

        serie += 11
        print(serie)
        x += 1

    deseaSeguir = desea_seguir()
    return deseaSeguir

#  5
#  Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.

def multiplos8():
    multiplos8 = 8
    i=1

    while multiplos8 <= 500:
        
        print(F"{i}. {multiplos8}")
        
        multiplos8 += 8
        i+=1

    deseaSeguir = desea_seguir()
    return deseaSeguir

#  6
# Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales") Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
def cualListaEsMayor():
    lista1 = 20
    dato1 = 0
    while dato1<15:
        num1 = lista1*1.25
        lista1 += num1
        dato1 += 1

    lista2 = 200
    dato2 = 0
    while dato2 < 15:
        num2 = lista2 - 5
        lista2 += num2
        dato2 +=1

    if(lista1 > lista2):
        mensaje = "Lista 1 es mayor"
    elif(lista2 > lista1):
        mensaje = "Lista 2 mayor"
    else: 
        mensaje = "Listas iguales"

    print(mensaje)

    deseaSeguir = desea_seguir()
    return deseaSeguir

#  7
#   Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1): if valor%2==0: 

# Colletura de Collatz

def conjetura_Collatz ():
    n = 2
    salir = "Desea seguir? escribe '1', de lo contrario '-1'\n"
    opcion = float(input(salir))
    while opcion != -1:
        
        pasos = 0
        r = n
        par = 0
        impar = 0
        print(n)
        while r > 1:
            if (r % 2 == 0):
                r = int(r/2)
                pasos +=1
                par += 1
                print(r)
            elif(r % 2 != 0):
                r = r*3+1
                pasos +=1
                impar += 1
                print(r)
        print(f'Se necesito realizar la secuencia {pasos} veces para llegar a 1 con el numero {n}, ademas {par} numeros fueron pares y {impar} impares')
        n += 1
        opcion = float(input(salir))  
        
    
    
    deseaSeguir = desea_seguir()
    return deseaSeguir

    




def opciones ():
    
    
    opcion0 = "***Digita el número para la opción correspondiente***\n\t1. Notas alumnos\n\t2. Altura personas\n\t3. Saldo empleados\n\t4. Secuencia 11-22...\n\t5.  Multiplos de 8\n\t6.Cual lista es mayor\n\t7. Cuantos pares e impares"
    print(opcion0)
    
    opcion1 = input("Digite su opción correspondiente\n")

    if(opcion1 == '1'):
        notasAlumnos()
    elif(opcion1 == '2'):
        alturapersonas()
    elif(opcion1 == '3'):
        sueldos()
    elif(opcion1 == '4'):
        serie11()
    elif(opcion1 == '5'):
        multiplos8()
    elif(opcion1 == '6'):
        cualListaEsMayor()
    elif(opcion1 == '7'):
        conjetura_Collatz()
    else: 
        print("Debes ingresar una opción valida")

opciones()



