def celsius_a_farenheit (temp_celsius):
    if temp_celsius >= -273.15:
        resultado = round((temp_celsius * 9/5) + 32, 2)
    else:
        resultado = 'Los grados celsius no pueden ser menor a "-273,15" que es el cero absoluto'
    return resultado

def farenheit_a_celsius (temp_farenheit):
    if temp_farenheit >= -459.67:
        resultado = round(( temp_farenheit - 32) * 5/9)
    else:
        resultado = 'Los grados farenheit no pueden ser menor a "-273,15" que es el cero absoluto'
    
    return resultado

