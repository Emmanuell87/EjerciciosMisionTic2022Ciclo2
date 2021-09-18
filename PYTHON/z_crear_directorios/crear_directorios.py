from pathlib import Path
import shutil
a = 1
b = 8
c = 8
for i in range(1, 89):
    path = Path(f'MARATON_RETOS/GRUPOS_{a}al{b}/GRUPO_{i}')
    path.mkdir(parents=True)
    
    for x in range(1, 4):
        shutil.copy(f'z_crear_directorios/reto_{x}.py', f'MARATON_RETOS/GRUPOS_{a}al{b}/GRUPO_{i}')
    if i == c:
        a += 8
        b += 8
        c += 8