import os
os.system ('cls')



#EJERCICIO 1
import turtle as t


#DIBUJAR UN CUADRADO
def cuadrado_simple():
    tortuga = t
    tortuga.forward(200)
    tortuga.left(90)
    tortuga.forward(200)
    tortuga.left(90)
    tortuga.forward(200)
    tortuga.left(90)
    tortuga.forward(200)
    t.done()
#cuadrado_simple()


def cuadrado_ciclo():
    tortuga = t
    for i in range(0, 4):
        tortuga.forward(200)
        tortuga.left(90)
    tortuga.done()
#cuadrado_ciclo()


def flor_cuadrado():
    tortuguita = t
    tortuguita.speed(50)
    grados = 0
    for i in range (0, 40):
        for x in range(0, 4):
            tortuguita.forward(200)
            tortuguita.left(90)
        tortuguita.left(grados+10)
    tortuguita.done()

#flor_cuadrado()


#circle =  t.circle(50)




"""
circle = t.circle(t_circle, 180)
#t.left(22.5)
#t.forward(100)
a0 = 0 #(0,0)
a1 = 90 #(100, 100)
a2 = 180 # (0, 200)
a3 = 270  #(-100, 100)

t.goto(70.71,29.29)

a = t.position()
print(a)

t.done()
"""