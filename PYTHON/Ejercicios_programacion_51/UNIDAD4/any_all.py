print('***********************EJEMPLO ANY********************')
uids = ['B1CD102354', 'B1CDEF2354']
for uid in uids:
    cond = []
    #por lo menos dos letras mayúsculas en el alfabeto inglés.
    cond.append(len(list(filter(lambda x: x.isupper(), list(uid) ))) >= 2)
    #Debe tener por lo menos 3 dígitos.
    cond.append(len(list(filter(lambda x: x.isdigit(), list(uid) ))) >= 3)
    #Contener únicamente dígitos alfanuméricos.
    cond.append(len(list(filter(lambda x: not(x.isalnum())  , list(uid) ))) == 0)
    #No tener repeticiones.
    cond.append(len(uid) == len(set(uid)))
    #Contener exactamente 10 caracteres.
    cond.append(len(uid) == 10)

    if all(cond):
        print('Valido!')
    else:
        print('Invalido!')



print('\n***********************EJEMPLO ANY********************')
info = [int(input()), input().split(' ')]
a = list(map(lambda x:x>0, list(map(int, info[1]))))
b = lambda x: x[0]==x[1] or x[0] == '5'

#y = list(map(lambda x: x[0]==x[1] or x[0] == '5', ))
#print(y)

a = list(zip(info[1], list(map(lambda x:x[-1:(len(x)+1)*-1:-1], info[1]))))




print('True' if all(a) and any(list(map(b, list(zip(info[1], list(map(lambda x:x[-1:(len(x)+1)*-1:-1], info[1]))))))) else 'False')


a =list(map(lambda x: x[0]==x[1], [('8', '8')]))
print(a)
