import os
os.system ('cls')

shift = 3 # defining the shift count

encrypted_text = "QHOOR ZRUOG"

plain_text = ""

for c in encrypted_text:

    # check if character is an uppercase letter
    if c.isupper():

        

        c_index = ord(c) - ord("A")

        # perform the negative shift
        new_index = (c_index - shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to plain string
        plain_text = plain_text + new_character

    else:

        # since character is not uppercase, leave it as it is
        plain_text += c

print("Encrypted text:",encrypted_text)

print("Decrypted text:",plain_text)