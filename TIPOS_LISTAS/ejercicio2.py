#Ejercicio 2
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
#pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada
#una de las asignaturas de la lista.

import random


asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

aleatorio = random.randint(0, 4) 

estudio = asignaturas[aleatorio]

print (f"yo estudio {estudio}")