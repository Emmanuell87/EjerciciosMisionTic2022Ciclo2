

def factura_agua(numeroDeSuscriptor= str, cargoBasico= int, metrosSubsidiados= int, cargoPorMetroExtra= int,
 metrosConsumidos= int) -> str:
    numeroDeSuscriptor = str("DIC986")
    cargoBasico = int(10000)
    metrosSubsidiados = int(10)
    cargoPorMetroExtra = int(2000)
    metrosConsumidos = int(12)
    totalFactura= round((cargoBasico+(metrosConsumidos-metrosSubsidiados)*cargoPorMetroExtra)*(119/100), 1)
    return f"El cliente {numeroDeSuscriptor} debe cancelar: {totalFactura} pesos"


print(factura_agua())