import os
os.system ('cls')

diccionarioEstudiantes = { 
  'E3454fdf':{
    'nombres': 'Laura',
    'apellidos': 'Jaramillo',
    'acudientes': ['Andrea','Juan'], 
    'promedio':5.0
    },
  'Egg56dfg':{
    'nombres': 'Samir',
    'apellidos': 'Gomez',
    'acudientes': ['Alejandro','Soffe'], 
    'promedio':5.0
    },
  'FHT435231':{
    'nombres': 'Sara',
    'apellidos': 'Cabrera',
    'acudientes': ['Carloss', 'Amparos'], 
    'promedio':5.0
    },
  'Z4edkdf':{
    'nombres': 'Ivan',
    'apellidos': 'Arcila',
    'acudientes': ['Esposa'],
    'promedio':5.0,
    123:'Este estudiante es alergico at mani'
  }
}

for i, estudiantes in enumerate(diccionarioEstudiantes):
    print("Numero ", i)
    print(estudiantes)