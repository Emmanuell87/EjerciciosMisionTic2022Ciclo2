import os
os.system ("cls")

"""
def factura_agua(numeroDeSuscriptor= str, cargoBasico= int, metrosSubsidiados= int, cargoPorMetroExtra= int,
 metrosConsumidos= int) -> str:
    iva = float(119/100)
    totalFactura= round((cargoBasico+(metrosConsumidos-metrosSubsidiados)*cargoPorMetroExtra)*iva, 1)
    return f"El cliente {numeroDeSuscriptor} debe cancelar: {totalFactura} pesos"

print(factura_agua(str("DIC986"), 11111, 10,
2000, 12 ))
"""





def Nombre_function (num1= int, num2= int, num3= int):
    
    resultado= num1 + num2 + num3

    
    return f"El total es {resultado} "


print(Nombre_function(4, 6, 11))