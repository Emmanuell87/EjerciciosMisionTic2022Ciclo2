

def factura_agua(informacion = dict)-> dict:

    numeroSuscriptor = informacion ['numeroSuscriptor']
    cargoBasico = informacion['cargoBasico']
    metrosSubsidiados = informacion['metrosSubsidiados']
    cargoPorConsumoExtra = informacion['cargoPorMetroExtra']
    metrosConsumidos = informacion['metrosConsumidos']
    estrato = informacion['estrato']



    #asegurarme que metros consumidos no sea mayor a los metros subsidiados
    if (metrosSubsidiados < metrosConsumidos) :
        SubTotalFactura= round((cargoBasico+(metrosConsumidos-metrosSubsidiados)*cargoPorConsumoExtra), 1)
    
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
        valorSeguro = int(7000)
        totalFactura = float(round(totalFactura + valorSeguro, 1))
        
    elif ((totalFactura >= 20000) and estrato > 3):
        valorSeguro = int(8000)
        totalFactura = float(round(totalFactura + valorSeguro, 1))
        
    elif ((totalFactura < 20000) and estrato <= 3):
        valorSeguro = int(5000)
        totalFactura = float(round(totalFactura + valorSeguro, 1))
        
    elif ((totalFactura < 20000) and estrato > 3):
        valorSeguro = int(6000)
        totalFactura = float(round(totalFactura + valorSeguro, 1))
        
    
    User = { 'numeroSuscriptor' : numeroSuscriptor, 
    'valorImpuesto' : valorImpuesto, 
    'valorSeguro' : valorSeguro, 
    'totalFactura' : totalFactura}
    return User

