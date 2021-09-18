
import os
os.system ('cls')

import pandas as pd

"""FORMA SENCILLA DE RESOLVERLO"""
def calificaciones(ruta_archivo:str)-> dict:
    ruta_archivo = pd.read_csv(ruta_archivo)
    promedioMatematicas = round(ruta_archivo['matematicas'].mean(), 1)
    promedioIngles = round(ruta_archivo['ingles'].mean(), 1)
    promedioSociales = round(ruta_archivo['sociales'].mean(), 1)
    promedioNaturales = round(ruta_archivo['naturales'].mean(), 1)
    promedioLecturaCritica = round(ruta_archivo['lecturaCritica'].mean(), 1)
    promedioGeneral = (promedioMatematicas+promedioIngles+promedioLecturaCritica+promedioNaturales+promedioSociales)/5

    resultado = {'promedioGeneral': promedioGeneral, 'promedioMatematicas' : promedioMatematicas, 'promedioIngles': promedioIngles}

    return resultado

print(calificaciones('https://bitbucket.org/insuasti/datosreto5mintic/raw/c7a27c4a984ee1f427eedca949f8aed22f31f244/calificaciones.csv'))


def calificaciones(ruta_archivo:str)-> dict:
    datosDataFrame = pd.read_csv(ruta_archivo)
    datosDataFrame = pd.DataFrame(datosDataFrame)
    prom_nota_total = 0
    prom_nota_matematicas= 0
    prom_nota_ingles = 0
    for i in datosDataFrame.index:
        
        for x in range(5, 10):
            prom_nota_total += datosDataFrame.iloc[i][x]
            if x == 6:
                prom_nota_matematicas += datosDataFrame.iloc[i][x]
            elif x == 9:
                prom_nota_ingles += datosDataFrame.iloc[i][x]
        
        if i == 999:
            prom_nota_total = round((prom_nota_total/5000), 1)
            prom_nota_matematicas = round((prom_nota_matematicas/1000), 1)
            prom_nota_ingles = round((prom_nota_ingles/1000), 1)
    
    resultado = {'promedioGeneral': prom_nota_total, 'promedioMatematicas' : prom_nota_matematicas, 'promedioIngles': prom_nota_ingles}

    return resultado
            


print(calificaciones('https://bitbucket.org/insuasti/datosreto5mintic/raw/c7a27c4a984ee1f427eedca949f8aed22f31f244/calificaciones.csv'))




