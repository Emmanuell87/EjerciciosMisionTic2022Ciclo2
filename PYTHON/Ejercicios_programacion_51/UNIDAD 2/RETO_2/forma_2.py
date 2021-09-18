import os
os.system ("cls")


Usuarios = {
    'User1' : {
        'numeroSuscriptor' : "ABC123",
        'cargoBasico' : 15000,
        'metrosSubsidiados' : 10,
        'cargoPorConsumoExtra' : 5000,
        'metrosConsumidos' : 9,
        'estrato' : 2
    },
    
    'User2' : {
        'numeroSuscriptor' : "DEF456",
        'cargoBasico' : 25000,
        'metrosSubsidiados' : 11,
        'cargoPorConsumoExtra' : 5500,
        'metrosConsumidos' : 10,
        'estrato' : 1,
    },

    'User3' : {
        'numeroSuscriptor' : str("OIU895"),
        'cargoBasico' : int(33285),
        'metrosSubsidiados' : int(15),
        'cargoPorConsumoExtra' : int(2500) ,
        'metrosConsumidos' : int(18) ,
        'estrato' : int(5)
    }
}

"""Escriba una función que reciba como parámetros un diccionario en el cual las llaves serían:
numeroSuscriptor, cargoBasico, metrosSubsidiados, cargoPorConsumoExtra,
metrosConsumidos y estrato, que representan respectivamente:"""

def factura_agua(informacion = dict)-> dict:
    numeroSuscriptor = informacion ['User1']['numeroSuscriptor']
    cargoBasico = informacion['User1']['cargoBasico']
    metrosSubsidiados = informacion['User1']['metrosSubsidiados']
    cargoPorConsumoExtra = informacion['User1']['cargoPorConsumoExtra']
    metrosConsumidos = informacion['User1']['metrosConsumidos']
    estrato = informacion['User1']['estrato']
    #asegurarme que metros consumidos no sea mayor a los metros subsidiados
    if (metrosSubsidiados < metrosConsumidos):
        SubTotalFactura= round((cargoBasico+(metrosConsumidos-metrosSubsidiados)
        *cargoPorConsumoExtra), 1)
        
    else:
        SubTotalFactura= round((cargoBasico), 1)
        
    #calcular el iva si lo necesita
    if (SubTotalFactura >= 20000):
        valorImpuesto = round(SubTotalFactura*0.16, 1)
        totalFactura = round(SubTotalFactura + valorImpuesto, 1)
        
        
    else: 
        totalFactura = round(SubTotalFactura)
        valorImpuesto = 0
    #costo seguro por robo de vivienda
    if ((totalFactura >= 20000) and estrato <= 3):
        valorSeguro = (7000)
        totalFactura = float(round(totalFactura + valorSeguro))
    elif ((totalFactura >= 20000) and estrato > 3):
        valorSeguro = (8000)
        totalFactura = totalFactura + valorSeguro
    elif ((totalFactura < 20000) and estrato <= 3):
        valorSeguro = (5000)
        totalFactura = float(round(totalFactura + valorSeguro, 1))
    elif ((totalFactura < 20000) and estrato > 3):
        valorSeguro = (6000)
        totalFactura = round(totalFactura + valorSeguro)
    
    

    User = dict( numeroSuscriptor = numeroSuscriptor, valorImpuesto = valorImpuesto, valorSeguro = valorSeguro, totalFactura = totalFactura)
    return User


"""
"\t El área del cuadrado es", área,"metros²"
{'numeroSuscriptor': 'ABC123', 'valorImpuesto': 0, 'valorSeguro': 5000, 'totalFactura':20000.0}.

Si al usuario se le adiciona un 16% a la factura y el estrato es inferior o igual a 3, entonces
el costo del seguro será de $7000.
• Si al usuario se le adiciona un 16% a la factura y el estrato es superior a 3, entonces el
costo del seguro será de $8000.
• Si al usuario no se le adiciona ningún impuesto y el estrato es inferior o igual a 3; entonces
el costo del seguro será de $ 5000.
• Si al usuario no se le adiciona ningún impuesto, y el estrato es superior a 3; entonces el
costo del seguro será de $6000.
"""
print(factura_agua(Usuarios))

#print(usuario['skills']['base_de_datos'])
