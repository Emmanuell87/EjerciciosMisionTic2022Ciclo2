import os
os.system ("cls")


def calcularCantidadBaldosas (b_ancho: int, b_largo: int, p_ancho: int, p_largo: int):
    
    area_baldosa = b_ancho*b_largo
    area_piso = p_ancho*p_largo
    cantidad_baldosas = int(area_piso/area_baldosa)

    return f"Es necesario adquirir {cantidad_baldosas} baldosas"

print(calcularCantidadBaldosas(40, 60, 346, 495))    

