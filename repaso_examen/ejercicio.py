##Ejercicio 9 
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 

contra = "papa"

while True:
    correcta = input ("cual es la contraseña: ")
    if correcta == contra:
        print ("contraseña correcta")
        break
    else:
                print("contraseña incorrecta vueleve a inetentar: ")
    