import os
os.system ("cls")

"""
num1 = int(input("Ingrese el primer número\n"))
num2 = int(input("Ingrese el segundo número\n"))
num3 = int(input("Ingrese el tercer número\n"))

numeros = (num1, num2, num3)
ordenados = sorted(numeros, reverse=True)

print(ordenados)



if ( num1 + num2 == num3):
    print('La suma de los dos primeros números es igual al tercero')
elif (num1 + num3 == num2):
    print("La suma del primer y tercer número es igual al segundo")
elif (num3 + num2 == num1):
    print("La suma del segundo y tercer numero es igual al primero")
else:
    print("La suma de dos números no es igual al otro")
"""




"""


segundos= int(input("Ingrese tiempo en segundos\n"))

horas = int(segundos / 3600)
segundos -=horas*3600
minutos =int(segundos/60)
segundos -= minutos*60


print(f"{horas}:{minutos}:{segundos}")



"""



"""
try:
    ultima_cifra = int(input("Ingrese un número \n"))

    
    num = int(ultima_cifra/10)
    print(num)
    ultima_cifra -= num*10

    print(f"La ultima cifra de su número es: {ultima_cifra}")
    
except:
        print("Por favor ingrese un número entero")


"""

"""
dia = int(input("Día cumpleaños\n"))
mes = int(input("Mes cumpleaños\n"))

def horoscopo (dia, mes):
    
    if(mes < 13 and dia<32):
        if ((mes==3 and dia >=21) or (mes==4 and dia<=20)):
            horoscopo= "Aries"
        elif ((mes==4 and dia >=21) or (mes==5 and dia<=21)):
            horoscopo = "Tauro"
        elif ((mes==5 and dia >=22) or (mes==6 and dia<=21)):
            horoscopo = "Géminis"
        elif ((mes==6 and dia >=22) or (mes==7 and dia<=22)):
            horoscopo = "Cancer"
        elif ((mes==7 and dia >=23) or (mes==8 and dia<=23)):
            horoscopo = "Leo"
        elif ((mes==8 and dia >=24) or (mes==9 and dia<=23)):
            horoscopo = "Virgo"
        elif ((mes==9 and dia >=24) or (mes==10 and dia<=23)):
            horoscopo = "Libra"
        elif ((mes==10 and dia >=24) or (mes==11 and dia<=22)):
            horoscopo = "Escorpión"
        elif ((mes==11 and dia >=23) or (mes==12 and dia<=21)):
            horoscopo = "Sagitario"
        elif ((mes==12 and dia >=22) or (mes==1 and dia<=20)):
            horoscopo = "Capricorio"
        elif ((mes==1 and dia >=21) or (mes==2 and dia<=18)):
            horoscopo = "Acuario"
        elif(( mes == 2 and dia >=19) or (mes == 3 and dia <= 20)):
            horoscopo = "Piscis"
        
        return f"Usted pertenece al signo zodiacal: {horoscopo}"
    else:
        return f"Los datos son erroneos"

print(horoscopo(dia, mes))
"""