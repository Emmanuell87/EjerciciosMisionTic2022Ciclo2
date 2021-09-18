import os
os.system ('cls')

def costo_telegrama(mensajes = list)-> dict:

    resultado = dict()
    for i in mensajes:
        lista = list(i.split(' '))
        #print(lista)
        valor = 0
        for x in lista:
            if len(x) <= 6:
                valor +=150
            else:
                valor += 250
        
        if len(lista) > 8:
            valor -= 400
        resultado[i] = valor
        
    
    return resultado
    

x = ["Este mensaje","Es solo para ti"] 
y = ["Bienvenidos tripulantes a misión tic 2022 es un placer que estén aprendiendo programación en la UTP", "Envío un caluroso saludo con mucho amor", "Se pasa a informar que el día 5 de mayo de 2021 entrará a trabajar en el área de mantenimiento"]


print(costo_telegrama(x))
print(costo_telegrama(y))