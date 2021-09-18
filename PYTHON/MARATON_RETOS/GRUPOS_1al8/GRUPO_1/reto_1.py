


def secuenciaFibonacci(numMax):
    
    secuencia = [0, 1]
    while True:
        z = secuencia[-2] + secuencia[-1]
        if z < numMax:
            secuencia.append(z)   
        else:
            break
    print(secuencia) 

secuenciaFibonacci(100)

def hello (mensaje):
    print(mensaje)

hello("Hello world")