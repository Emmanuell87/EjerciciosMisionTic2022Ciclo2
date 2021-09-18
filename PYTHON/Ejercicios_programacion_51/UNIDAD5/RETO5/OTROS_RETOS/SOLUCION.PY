import os
os.system('cls')


import pandas as pd


def estadisticas(data)->dict:
    datosDataFrame = pd.read_csv(data)
    #print(datosDataFrame)
    print(datosDataFrame['PUNT_MATEMATICAS'].mean())
    print(type(datosDataFrame))
    
    
    """
    datosDataFrame = pd.DataFrame(datosDataFrame)
    prom_Nacional = 0
    prom_desemp_Nacional = 0
    barranquilla = 0
    count_barranquilla = 0
    oficial = 0
    count_oficial = 0
    no_oficial = 0
    count_no_oficial = 0
    tupla_desemp = tuple()
    tupla1 = tuple()
    for x in datosDataFrame.index:
        
        for i in (12, 36, 57):
            if i == 12:
                if datosDataFrame.iloc[x][i] == 'BARRANQUILLA':
                    barranquilla += datosDataFrame.iloc[x][59]
                    count_barranquilla += 1
            if i == 36:
                if datosDataFrame.iloc[x][i] == 'OFICIAL':
                    oficial += datosDataFrame.iloc[x][57]
                    count_oficial += 1
                else:
                    no_oficial += datosDataFrame.iloc[x][57]
                    count_no_oficial +=1
            if i == 57:
                prom_Nacional += datosDataFrame.iloc[x][i]
                prom_desemp_Nacional += datosDataFrame.iloc[x][59]
        
        if x == 39999:
            prom_Nacional = prom_Nacional/40000
            prom_desemp_Nacional = prom_desemp_Nacional/40000
            barranquilla = barranquilla/count_barranquilla
            oficial = oficial/count_oficial
            no_oficial = no_oficial/count_no_oficial

        
        if prom_desemp_Nacional > barranquilla:
            tupla_desemp = (prom_desemp_Nacional, 'nacional')
        else:
            tupla_desemp = (barranquilla, 'local')

        if oficial > no_oficial:
            tupla1 = (oficial, 'oficial')
        else:
            tupla1 = (no_oficial, 'no oficial')

    
    resultado = {'nacional_math': prom_Nacional, 'performance_math': tupla_desemp, 'mejor_resultado': tupla1}
    print(prom_Nacional)
    print(prom_desemp_Nacional)
    print(barranquilla)
    print(oficial)
    print(no_oficial)
    print(tupla_desemp)
    print(tupla1)
    print(type(tupla1))
    print(type(tupla_desemp))
    print('****\n', resultado)
    return resultado

"""


"""
            
    print(datosDataFrame.iloc[0][57])
    print(datosDataFrame.iloc[0][36])
    print(datosDataFrame.iloc[0][12])
"""


estadisticas('datos_icfes.csv')

