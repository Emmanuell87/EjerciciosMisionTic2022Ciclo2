import os
os.system('cls')

class empleado:
    def __init__(self):
        self.nombre = input('Ingrese el nombre del empleado: ')
        self.sueldo = float(input('Ingrese el sueldo: '))
    def imprimir_datos(self):
        print('El nombre es: ', self.nombre)
        print('El sueldo es: ', self.sueldo)
    def paga_impuestos(self):
        if self.sueldo > 3000:
            print('Debe pagar impuesto')
        else:
            print('No debe pagar impuesto')

empleadoA = empleado()
empleadoA.imprimir_datos()
empleadoA.paga_impuestos()