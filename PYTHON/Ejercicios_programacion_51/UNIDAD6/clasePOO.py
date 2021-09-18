import os
os.system ('cls')

##Primera clase: gato

class Gato:
    def __init__(self, color, patas):
        self.color = color
        self.patas = patas
        
    def maullar (self):
        return 'miau!!!!'

felix = Gato('Cafe', 4)
rover = Gato('Amarillo', 3)
thor  = Gato('Negro', 4)

print(f'El gato Felix es de color{felix.color} y tiene {felix.patas} patas y maulla así: {felix.maullar()}')

class Perro:
    def __init__(self, raza, nombre, color):
        self.raza = raza
        self.nombre = nombre
        self.color = color
    
    def ladrar (self):
        return 'guau!!'