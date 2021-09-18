import os
os.system('cls')

import turtle as t


multiplicar = int(input('Ingrese el numero por el cual desea multiplicar\n'))

def posicion_actual(posicion):
    return lista_posiciones[posicion]


def dibujar_linea (datos, multiplos):
    
    multiplicacion =  datos[0]*multiplos
    while multiplicacion > puntos:
        multiplicacion -= puntos
    ir = lista_posiciones[multiplicacion-1][1]
    t.goto(ir)
    t.goto(datos[1])
    t.circle(tamaño_circle, grados)

    return 1
    
    #circle = t.goto()


def comenzar():
    num1 = 0
    #while i == len(lista_posiciones-1):
    for i in range(len(lista_posiciones)):
        a = dibujar_linea(posicion_actual(num1), multiplicar)
        num1 += a
    


t.goto(0, -280)
t.clear()
puntos = 4
for i in range(0, 501, 100):
    tamaño_circle = 280
    t.speed(1000)
    
    #cuantos puntos quieres?
    grados = 360/puntos
    lista_posiciones = []
    for r in range(1,puntos+1):
        posicion = t.position()
        circle = t.circle(tamaño_circle, grados)
        lista_posiciones.append((r, posicion))
    comenzar()
    puntos += i
    if i >= 500:
        t.done()
    t.clear()