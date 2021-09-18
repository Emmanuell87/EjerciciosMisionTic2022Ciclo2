def leucocitos(info:dict)-> tuple:
    # Se accede la información de las cedulas por medio del metodo .keys
    cedulas = info.keys()
    resultado = {}
    
    #Se crea el for inicial que tome todas las cedulas
    for i in cedulas:
        dias = info[i]["infoHemograma"].keys()
        leuco = info[i]["infoHemograma"].values()
        #Se crea el for interno con el objetivo de almacenar el promedio de los leucocitos por paciente
        suma = 0
        for diasItem, leucoItem  in (info[i]["infoHemograma"].items()):
            suma = suma + leucoItem
        resultado[i] = round(suma/len(dias),1)
        #print(len(dias))
        suma =0

    leucoMayor10 = dict(filter(lambda leuco: leuco[1] >= 10.1 ,resultado.items() ))
    return(resultado, leucoMayor10)


info1 = {
    1144154: {
        "nombreCompleto": "Juan Perez",
        "infoHemograma":
            {
                "dia1":22.5,"dia2":25.6,"dia3":26.7,"dia4":19.5,"dia5":20.1
            }
    },
    1088852: {
        "nombreCompleto": "Mariana Pajón",
        "infoHemograma":
            {
                "dia1": 9.5, "dia2": 7.8, "dia3": 12.5, "dia4": 10.5, "dia5": 11.1
            }
    },
    1664558: {
        "nombreCompleto": "Leydi Torres",
        "infoHemograma":
            {
                "dia1":30.5,"dia2":27.6,"dia3":28.7,"dia4":21.5,"dia5":21.1
            }
    },
    1745558: {
        "nombreCompleto": "Leydi Torres",
        "infoHemograma":
            {
                "dia1":40.5,"dia2":25.6,"dia3":15.7,"dia4":17.5,"dia5":18.1
            }
    }
}


({1144154: 22.9, 1088852: 8.3, 1664558: 25.9, 1745558: 23.5}, {1144154: 22.9, 1664558: 25.9, 1745558: 23.5})

print(leucocitos(info1))