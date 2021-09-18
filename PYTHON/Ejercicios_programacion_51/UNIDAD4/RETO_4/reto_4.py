import os
os.system ('cls')

def imc(info:dict)-> tuple:
    resultado = dict()
    
    for i in info: 
        
        
        peso = info[i]['infoSalud']['peso'] 
        altura =  info[i]['infoSalud']['altura']

        prom_peso = 0

        for x in range(5):
            prom_peso1 = (peso[x]/(altura[x]**2))
            
            prom_peso += prom_peso1
        
        prom_peso = round((prom_peso/5), 1)
        resultado[i] = prom_peso
    
    
    return (resultado, dict(filter(lambda prom_menor: prom_menor[1] < 18.5, resultado.items())))


info2 = {
    6668145: {
        "nombreCompleto": "Pablo Perez",
        "infoSalud":
            {
                "peso": [70, 75, 85, 85, 86],
                "altura": [1.6, 1.6, 1.6, 1.6, 1.6]
            }
    },
    7412589: {
        "nombreCompleto": "Juan Esteban Sanchez",
        "infoSalud":
            {
                "peso": [40, 50, 41, 42, 43],
                "altura": [1.45, 1.46, 1.47, 1.48, 1.5]
            }
    },
    9632145: {
        "nombreCompleto": "Daniel Molano",
        "infoSalud":
            {
                "peso": [60, 61, 62, 63, 64],
                "altura": [1.55, 1.55, 1.55, 1.55, 1.55]
            }
    }
}
print(imc(info2))

"""
def imc(info:dict)-> tuple:
    imc = []
    resultado = dict()
    
    for i in info: 
        j = 0
        peso = info[i]['infoSalud']['peso'] 
        altura =  info[i]['infoSalud']['altura']

        while j < len(peso) and j < len(altura):
            imc.append(peso[j]/altura[j]**2)
            j+= 1
        resultado[i] = round(sum(imc)/len(imc), 1)

    print(imc)
    print('*********')
    print(resultado)
    menores_resultados = {}
    for i in resultado:
        if resultado[i] <18.5:
            menores_resultados[i] = resultado[i]
    print(menores_resultados) 
    lista = [resultado, menores_resultados]
    print('*************')
    print(lista)
    print('************')

    return tuple(lista)
       
"""






"""
def imc(info:dict)-> tuple:
    cedulas= (list(info.keys()))
    valores = info.values()
    pesos_alturas = (list(i['infoSalud'] for i in valores if i['infoSalud'] != 1) [ 0:len(cedulas)])
    listaPesos = (list(i['peso'] for i in pesos_alturas)[0:len(pesos_alturas)])
    listaAlturas = (list(i['altura'] for i in pesos_alturas)[0:len(pesos_alturas)])
    #print(pesos_alturas)
    #print(listaPesos)
    #print(listaAlturas)


    listaCuadrados = []
    for i in range(len(listaAlturas)):
        listaCuadrados.append([])
        
        r = -1
        for k in listaAlturas[i]:
            r += 1
            cua = (listaPesos[i][r]/(k*k))
            listaCuadrados[i].append(cua)
        #print(listaCuadrados)
        
    print(listaCuadrados)

    resultado = []
    for k in listaCuadrados:
        prom_ind = round((sum(k))/(len(k)), 1)
        resultado.append(prom_ind)

    salida1 = dict(zip(cedulas, resultado))

    salida2 = dict(filter(lambda x: x[1] < 18.5, salida1.items()))

    salida = (salida1, salida2)

    return (salida)


"""








info1 = {
 1144154: {
 "nombreCompleto": "Lina Maria Valencia",
 "infoSalud":
 {
 "peso": [60, 55, 45, 43, 55],
 "altura": [1.8, 1.8, 1.8, 1.8, 1.8]
 }
 },
 1088852: {
 "nombreCompleto": "Mariana Sandoval",
 "infoSalud":
 {
 "peso": [55, 50, 60, 62, 70],
 "altura": [1.7, 1.7, 1.7, 1.7, 1.7]
 }
 },
 1664558: {
 "nombreCompleto": "Sara Torres",
 "infoSalud":
 {
 "peso": [45, 40, 44, 40, 50],
 "altura": [1.50, 1.51, 1.52, 1.55, 1.6]
 }
 }
}

print(imc(info1))
my_dictionary = {'asd':3, 'frt': 4}
my_dictionary = {k: (v) for k, v in my_dictionary.items()}

#print(my_dictionary)
