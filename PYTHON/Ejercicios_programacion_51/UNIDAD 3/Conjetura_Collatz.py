import os
os.system ("cls")

def conjetura_Collatz (num: int):
    
    r= num
    pasos = 0 
    par = 0   
    impar = 0 
    print(r)
    while r > 1: 
        if (r % 2 == 0): 
            r = int(r/2)
            pasos +=1
            par += 1
            print(r)
        elif(r % 2 != 0): 
            r = r*3+1
            pasos +=1
            impar += 1
            print(r)
    print(f'Se necesito realizar la secuencia {pasos} veces para llegar a 1 con el numero {num}, ademas {par} numeros fueron pares y {impar} impares')


num = int(input("Ingresa un número entero\n"))
conjetura_Collatz(num)