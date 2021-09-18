
def costo_anuncio (mensajes:list)-> dict:
    letrasEconomicas = ["f","i","j","k","l","r","t"]
    precio = 0
    resultado = {}
    for i in mensajes:
        for j in i:
            if j in letrasEconomicas:
                precio = precio +50
            else:
                precio = precio + 100
        resultado[i] = precio
        precio=0
    return resultado


