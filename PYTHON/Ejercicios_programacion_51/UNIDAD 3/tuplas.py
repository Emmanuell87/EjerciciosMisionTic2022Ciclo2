import os
from typing import final
os.system ('cls')

txt = "but soft what light in yonder window breaks"
palabras = txt.split()
print(palabras)


l = list()
for subcadena in palabras:
    l.append((len(subcadena), subcadena))
print(l)