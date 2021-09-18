import os
os.system ("cls")

Usuarios1 = {
    
    'numeroSuscriptor' : "ABC123",
    'cargoBasico' : 15000,
    'metrosSubsidiados' : 10,
    'cargoPorConsumoExtra' : 5000,
    'metrosConsumidos' : 10,
    'estrato' : 2
   
}

Usuarios2 = {
        'numeroSuscriptor' : "DEF456",
        'cargoBasico' : 25000,
        'metrosSubsidiados' : 11,
        'cargoPorConsumoExtra' : 5500,
        'metrosConsumidos' : 10,
        'estrato' : 1,
}
Usuarios3 = {
        'numeroSuscriptor' : str("OIU895"),
        'cargoBasico' : int(33285),
        'metrosSubsidiados' : int(15),
        'cargoPorConsumoExtra' : int(2500) ,
        'metrosConsumidos' : int(18) ,
        'estrato' : int(5)
    }
Usuarios1.get
print(Usuarios1['numeroSuscriptor'])

def factura_agua(informacion = dict)-> dict:
    

    numeroSuscriptor = informacion ['numeroSuscriptor']
    cargoBasico = informacion['cargoBasico']
    metrosSubsidiados = informacion['metrosSubsidiados']
    cargoPorConsumoExtra = informacion['cargoPorConsumoExtra']
    metrosConsumidos = informacion['metrosConsumidos']
    estrato = informacion['estrato']



    #asegurarme que metros consumidos no sea mayor a los metros subsidiados
    if (metrosSubsidiados < metrosConsumidos) :
        SubTotalFactura= round((cargoBasico+(metrosConsumidos-metrosSubsidiados)
        *cargoPorConsumoExtra), 1)
        print("subtotal con calculo", SubTotalFactura)
    else:
        SubTotalFactura= round((cargoBasico), 1)
        print("subtotal", SubTotalFactura)
        
    #calcular el iva si lo necesita
    if (SubTotalFactura >= 20000):
        valorImpuesto = round(SubTotalFactura*0.16, 1)
        totalFactura = round(SubTotalFactura + valorImpuesto, 1)
        print("totalfactura con impuesto", totalFactura, valorImpuesto)
    else: 
        totalFactura = round(SubTotalFactura)
        valorImpuesto = 0
        print("sin impuesto", totalFactura, valorImpuesto)

    #costo seguro por robo de vivienda
    if ((totalFactura >= 20000) and estrato <= 3):
        valorSeguro = int(7000)
        totalFactura = totalFactura + valorSeguro
        print("totalfactura con seguro", totalFactura, valorSeguro)
    elif ((totalFactura >= 20000) and estrato > 3):
        valorSeguro = int(8000)
        totalFactura = totalFactura + valorSeguro
        print("totalfactura con seguro", totalFactura, valorSeguro)
    elif ((totalFactura < 20000) and estrato <= 3):
        valorSeguro = int(5000)
        totalFactura = totalFactura + valorSeguro
        print("totalfactura con seguro", totalFactura, valorSeguro)
    elif ((totalFactura < 20000) and estrato > 3):
        valorSeguro = int(6000)
        totalFactura = totalFactura + valorSeguro
        print("totalfactura con seguro", totalFactura, valorSeguro)
    
    

    User = dict( numeroSuscriptor = numeroSuscriptor, valorImpuesto = valorImpuesto, valorSeguro = valorSeguro, totalFactura = totalFactura)
    
    return dict(User)


