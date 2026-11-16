#Ejercicio 13 
# Escribir un programa que muestre el eco de todo lo que el usuario 
# introduzca hasta que el usuario escriba “salir” que terminará. 
salir = "salir"

while True:
    escribe = input ("introduce lo que quieras: ")
    if escribe == salir:
        break
    else:
        
        print (escribe)


    