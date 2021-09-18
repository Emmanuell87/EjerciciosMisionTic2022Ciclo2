

def tiempo_llenado_tanque():
    """Se pide al usuario que ingrese el alto, ancho y largo del tanque"""
    Alto = float(input("Alto del tanque\n"))
    Ancho = float(input("Ancho del tanque\n"))
    Largo = float(input("Largo del tanque\n"))
    """operacion basicas para calcular los datos necesarios para el reto(capacidad cubica del tanque,
    minutos que se tarda la motobomba en llenarlo y la conversion a horas"""
    capacidad_cubica = Alto*Ancho*Largo
    minutos = (capacidad_cubica/0.5)*3
    horas = minutos/60
    return f"La motobomba llenará el tanque en {minutos} minutos, equivalente a {horas} horas"




print(tiempo_llenado_tanque())