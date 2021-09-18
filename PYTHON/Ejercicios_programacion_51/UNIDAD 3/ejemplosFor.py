def ejemploFor1():
    print("Comienzo")
    for i in range(3): #[0,1,2]
        print(f"Hola {i} ",end="")
    print()
    print("Final")

#ejemploFor1()

def ejemploFor2():
    print("Comienzo")
    for i in range(20,14,-1): #[20,19,18,17,16,15]
        print(f"Hola {i} ",end="")
    print()
    print("Final")

#ejemploFor2()

def ejemploFor3():
    print("Comienzo")
    for i in []:
        print(f"Hola {i} ",end="")
    print()
    print("Final")

ejemploFor3()



datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}

clave = datos_basicos.keys()
print(clave)
valor = datos_basicos.values()
print(valor)
