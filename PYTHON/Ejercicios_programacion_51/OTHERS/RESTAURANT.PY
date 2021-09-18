import os
os.system ('cls')

def realizarPedido (sopa: str, plato_principal: str, bebida:str, postre:str):
    menu = {
        "":0,
        "Sopa de pastas":3000, 
        "Pollo apanado":7000, 
        "Albóndigas en salsa":8000, 
        "Jugo de uva":2000, 
        "Limonada":1500, 
        "Merengón":5000, 
        "Leche asada":4000}

    total= 0

    total= menu[sopa] + menu[plato_principal] + menu[bebida] + menu[postre]

    if plato_principal=="Pollo apanado" and postre=="Merengón" or sopa == "Sopa de pastas" and postre=="Merengón":
        total = total * 0.7

    dict = {"sopa":sopa, "plato principal":plato_principal, "bebida":bebida, "postre":postre, "total":int(total)}
    return dict
    
print(realizarPedido("", "Albóndigas en salsa", "Limonada", "Leche asada"))
print(realizarPedido("Sopa de pastas", "", "Jugo de uva", "Merengón"))