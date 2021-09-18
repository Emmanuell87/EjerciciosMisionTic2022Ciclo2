
primero = 0
segundo = 1
siguiente = 0
pasos=1
print(primero)
print(segundo)
while pasos<=10:
    
    
    siguiente = primero+segundo
    print(siguiente)
    primero = segundo
    segundo = siguiente
    pasos+= 1
