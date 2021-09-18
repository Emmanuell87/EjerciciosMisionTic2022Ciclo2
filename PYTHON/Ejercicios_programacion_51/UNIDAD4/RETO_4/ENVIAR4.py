import os
os.system ('cls')

def imc(info:dict)-> tuple:
    resultado = dict()
    
    for i in info: 
        
        
        peso = info[i]['infoSalud']['peso'] 
        altura =  info[i]['infoSalud']['altura']

        prom_peso = 0

        for x in range(len(peso)):
            prom_peso1 = (peso[x]/(altura[x]**2))
            
            prom_peso += prom_peso1
        
        prom_peso = round((prom_peso/len(peso)), 1)
        resultado[i] = prom_peso
                
    return (resultado, dict(filter(lambda prom_menor: prom_menor[1] < 18.5, resultado.items())))

