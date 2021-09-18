import os
os.system ('cls')

def factura_agua(informacion:dict)-> dict: 
    numero_cliente = informacion['numeroSuscriptor']
    cargoBasico = informacion['cargoBasico']
    metrosSubsidiados = informacion['metrosSubsidiados']
    cargoPorMetroExtra = informacion['cargoPorMetroExtra'] 
    metrosConsumidos = informacion['metrosConsumidos']
    estrato = informacion['estrato']
    
    
    valorImpuesto = 0
    valorlimite = 20000
    impuesto = 1.16
    if metrosConsumidos > metrosSubsidiados:
        subtotal = ((metrosConsumidos-metrosSubsidiados)*cargoPorMetroExtra)+cargoBasico
    else:
        subtotal = cargoBasico
    valorSeguro = 0


    

    if subtotal >= valorlimite:
        valorImpuesto = subtotal * 0.16
        if valorImpuesto > 0 and estrato <=3:
            valorSeguro = 7000
            totalFactura = (subtotal*impuesto) + valorSeguro
        elif valorImpuesto > 0 and estrato > 3:
            valorSeguro = 8000
            totalFactura = (subtotal*impuesto) + valorSeguro 

    

    elif subtotal < valorlimite:
        valorImpuesto = 0
        if valorImpuesto == 0 and estrato <=3:
            valorSeguro = 5000 
            totalFactura = subtotal + valorSeguro 
        elif valorImpuesto == 0 and estrato > 3:
            valorSeguro = 6000
            totalFactura = subtotal + valorSeguro 

    totalFactura= round(totalFactura, 1)

    diccionario_salida = {
        'numeroSuscriptor': numero_cliente,
        'valor_impuesto' : valorImpuesto,
        'valorSeguro' : valorSeguro,
        'totalFactura' : totalFactura
    }
    return(diccionario_salida)
    
datos_entrada = {
    'numeroSuscriptor' : "ABC123",
    'cargoBasico' : 25000 ,
    'metrosSubsidiados' : 11,
    'cargoPorMetroExtra' : 5500 ,
    'metrosConsumidos' : 10,
    'estrato' : 1
}

print(factura_agua(datos_entrada))

def factura_agua(informacion:dict)-> dict: 
    numero_cliente = informacion['numeroSuscriptor']
    cargoBasico = informacion['cargoBasico']
    metrosSubsidiados = informacion['metrosSubsidiados']
    cargoPorMetroExtra = informacion['cargoPorMetroExtra'] 
    metrosConsumidos = informacion['metrosConsumidos']
    estrato = informacion['estrato']
    
    totalFactura = cargoBasico
    valorlimite = 20000
    iva = 1.16
    if metrosConsumidos > metrosSubsidiados:
        subtotal = ((metrosConsumidos-metrosSubsidiados)*cargoPorMetroExtra)+cargoBasico
    else:
        subtotal = cargoBasico
    valorSeguro = 0


    

    if subtotal >= valorlimite:
        valorImpuesto = subtotal * 0.16
        if valorImpuesto > 0 and estrato <=3:
            valorSeguro = 7000
            totalFactura = (totalFactura*iva) + valorSeguro  
        elif valorImpuesto > 0 and estrato > 3:
            valorSeguro = 8000
            totalFactura = (totalFactura*iva) + valorSeguro  

    elif subtotal < valorlimite:
        valorImpuesto = 0
        if valorImpuesto == 0 and estrato <=3:
            valorSeguro = 5000 
            totalFactura = totalFactura + valorSeguro 
        elif valorImpuesto == 0 and estrato > 3:
            valorSeguro = 6000
            totalFactura = totalFactura + valorSeguro 

    totalFactura = round(totalFactura,1)

    diccionario_salida = {
        'numeroSuscriptor': numero_cliente,
        'valor_impuesto' : valorImpuesto,
        'valorSeguro' : valorSeguro,
        'totalFactura' : totalFactura
    }
    return(diccionario_salida)

print("************--------****************")
print(factura_agua(datos_entrada))