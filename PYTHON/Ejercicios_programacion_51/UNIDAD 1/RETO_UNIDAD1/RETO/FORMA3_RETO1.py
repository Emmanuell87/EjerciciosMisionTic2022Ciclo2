

numeroDeSuscriptor = str(input("DIGITE SU NÚMERO DE SUSCRIPTOR\n"))
cargoBasico = int(input("DIGITE EL CARGO BASICO DEL SERVICIO\n"))
metrosSubsidiados = int(input("DIGITE LOS METROS SUBSIDIADOS\n"))
cargoPorMetroExtra = int(input("DIGITE EL CARGO POR METRO EXTRA\n"))
metrosConsumidos = int(input("DIGITE LA CANTIDAD TOTAL DE METROS CONSUMIDOS\n"))

def factura_agua(numeroDeSuscriptor= str, cargoBasico= int, metrosSubsidiados= int, cargoPorMetroExtra= int,
 metrosConsumidos= int) -> str:
    
    totalFactura= round((cargoBasico+(metrosConsumidos-metrosSubsidiados)*cargoPorMetroExtra)*(119/100), 3)
    return f"El cliente {numeroDeSuscriptor} debe cancelar: {totalFactura} pesos"


print(factura_agua(numeroDeSuscriptor, cargoBasico, metrosSubsidiados, cargoPorMetroExtra, metrosConsumidos))
