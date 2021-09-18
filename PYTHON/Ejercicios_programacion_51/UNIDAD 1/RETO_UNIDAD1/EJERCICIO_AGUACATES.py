

aguacatesxarbol = 40
prom_caja_aguacates_hass = float(10.0)
prom_peso_aguacate = float(0.25)

def número_arboles_aguacate_hass():
    "El usuario inserta las toneladas del cargamento y nos devuelve un valor tipo float"
    toneladas_cargamento = float(input ("Toneladas de cargamento de aguacates hass \n"))
    "Pasamos las toneladas a kilogramos"
    KG_cargamento = toneladas_cargamento*1000
    """Se calcula la cantidad de aguacates hass dividiendo el peso en Kg del cargamento
    entre el peso promedio de un aguacate hass"""
    aguacates = KG_cargamento/prom_peso_aguacate
    """Se calcula la cantidad de arboles necesarios para recoger el total de aguacates"""
    arboles = aguacates/aguacatesxarbol
    """agrege un if para comparar el valor de tonelada_cargamento es igual a uno me devuelva un string  
    = tonelada, sino uno = toneladas"""
    if (toneladas_cargamento==1):
        name = str("tonelada")
    else:
        name = str("toneladas")
    
    return f"para completar {toneladas_cargamento} {name} del cargamento, se recogierón"\
        f" {aguacates} aguacates de {arboles} árboles"





print(número_arboles_aguacate_hass())