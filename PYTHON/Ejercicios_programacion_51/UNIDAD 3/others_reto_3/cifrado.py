import os
os.system ('cls')


def descifrar_codigo_cesar(texto_cifrado =  str, corrimiento = int)->str:
    descifrado = []

    for i in texto_cifrado:

        if i.isalpha():
            if i.isupper():
                c_index = ord(i) - ord("A")

                # perform the negative shift
                new_index = (c_index - corrimiento) % 26

                # convert to new character
                new_unicode = new_index + ord("A")

                new_character = chr(new_unicode)

                # append to plain string
                descifrado.append(new_character)
            
            else:
                c_index = ord(i) - ord("a")

                # perform the negative shift
                new_index = (c_index - corrimiento) % 26

                # convert to new character
                new_unicode = new_index + ord("a")

                new_character = chr(new_unicode)

                # append to plain string
                descifrado.append(new_character)

        else:
            # since character is not uppercase, leave it as it is
            descifrado.append(i) 

        
    print(descifrado)

    cadena_descifrada = ''.join(descifrado)
    
    return cadena_descifrada




    """
    for i in texto_cifrado:

        if i.isalpha():
            c = chr(ord(i)-corrimiento)
            descifrado.append(c)
        else:
            descifrado.append(i)
            

    print(descifrado)

    cadena_descifrada = ''.join(descifrado)
    
    return cadena_descifrada
    """

x = ['A', 'B', 'C', 'a', 'b', 'c', 'ñ', 'Ñ']

lista = ['s', 4]
print(descifrar_codigo_cesar(lista[0], lista[1]))

lista = ['Tvmqivs tmirws, pyiks ibmwxs', 4]
print(descifrar_codigo_cesar(lista[0], lista[1]))

lista = ['Hñ ghvfliudgr fhvdu hv idflñ', 3]
print(descifrar_codigo_cesar(lista[0], lista[1]))



#Comvertir un caracter a codigo ASCII
"""
c_unicode = ord("c")

A_unicode = ord("A")

print("Unicode of 'c' =", c_unicode)

print("Unicode of 'A' =", A_unicode)
"""

# convertir codigo ASCII a un caracter
"""
character_65 = chr(65)

character_100 = chr(100)

print("Unicode 65 represents", character_65)

print("Unicode 100 represents", character_100)

character_360 = chr(360)

print("Unicode 360 represents", character_360)
"""