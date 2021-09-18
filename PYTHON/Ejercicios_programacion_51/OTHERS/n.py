import os 
os.system ("cls")
"""
num1= float(input("Ingrese un número\n"))
num2= float(input("Ingrese un número\n"))

if num2 == 0:
    resultado = 0
else: 
    num2 = 1/num2
    resultado = round(num1/num2, 1)


print(f"El resultado de la multiplicacion entre los dos números es: {resultado}")

"""

def mult (a: int, b: int) -> int:
    r = 0
    for i in range(a):
        r += b

    print(r) 

mult(5, 5)
mult(3, 2)