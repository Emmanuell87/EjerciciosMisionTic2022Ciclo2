import os
os.system ('cls')



def realizarPedido (sopa = str, plato_principal = str, bebida = str, postre = str):
    
    menu = {
        'sopa' : {
            '' : 0,
            'Sopa de pastas' : 3000
        },
        'plato_principal' : {
            '' : 0,
            'Pollo apanado' : 7000,
            'Albóndigas en salsa' : 8000
        },
        'bebida' : {
            '' : 0,
            'Jugo de uva': 2000,
            'Limonada': 1500
        },
        'postre' : {
            '' : 0,
            'Merengón': 5000,
            'Leche asada': 4000
        }
    }

    
    sopa1 = menu['sopa'][sopa]

    plato1 = menu['plato_principal'][plato_principal]
    
    bebida1 = menu['bebida'][bebida]

    postre1 = menu['postre'][postre]

    resultado = sopa1 + plato1 + bebida1 + postre1


    if postre == 'Postre de Merengón' and plato_principal == 'Pollo apanado' or (postre == 'Merengón' and sopa =='Sopa de pastas'):
        resultado = round(resultado*0.7)

    
    diccionario = {'sopa' : sopa, 'plato principal' : plato_principal, 'bebida' : bebida, 'postre' : postre, 'total' : resultado}
    
    return diccionario

orden= dict(sopa = '', plato_principal= 'Albóndigas en salsa', bebida= 'Limonada', postre= 'Merengón')

print(realizarPedido(orden['sopa'], orden['plato_principal'], orden['bebida'], orden['postre']))