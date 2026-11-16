#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
#mensaje En <asignatura> has sacado <nota> donde <asignatura> es
#cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
#notas introducidas por el usuario.



asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for i in asignaturas:
    pregunta = float (input (f"que nota ha sacado en {i}: "))

    print (f" has sacado un {pregunta} en {i}")