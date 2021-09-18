import os
os.system('cls')
import random

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.numerocuenta = random.randint(1000, 10000)
        self.saldo = saldo_inicial

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
            print("----------------------------------")
        else:
            self.saldo = self.saldo - monto
            print("Retiro Exitoso ")
            print("----------------------------------")
            """
            print("Retiro Exitoso ", end="")
            print("Nuevo Saldo", self.saldo)
            """
        
    def consignar(self, monto):
        self.saldo = self.saldo + monto
        print('Consignacion exitosa')
        print("----------------------------------")

    def consultarSaldo(self):
        print('--------------------')
        print("Cuenta: ", self.numerocuenta)
        print("Saldo:  ", self.saldo)
        print('--------------------')


saldoInicial = float(input('Bienvenido al banco XYZ, bara crear su cuenta bancaria, ingrese el saldo incial de la cuenta : \n'))

cuenta = CuentaBancaria(saldoInicial)

while True:
    operacion = input('Ingrese S para cinsultar saldo, R para retirar y C para consignar : \n')

    if operacion == 'S':
        cuenta.consultarSaldo()
    elif operacion == 'R':
        monto = float(input('Ingrese el monto que desee retirar : \n'))
        cuenta.retirar(monto)
    elif operacion == 'C':
        monto = float(input('Ingrese el monto que desee consignar : \n'))
        cuenta.consignar(monto)
    else:
        print('Ingrese una opción valida')
    
"""
cuenta1= CuentaBancaria(50000)

cuenta1.consultarSaldo()

cuenta1.retirar(20000)
cuenta1.consultarSaldo()

cuenta1.retirar(200000)
cuenta1.consultarSaldo()

cuenta1.consignar(500000)
cuenta1.consultarSaldo()

cuenta1.retirar(200000)
cuenta1.consultarSaldo()
"""