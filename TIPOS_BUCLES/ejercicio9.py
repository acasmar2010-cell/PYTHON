#Ejercicio 9 
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 


contrasenia = "lolo"


while True:
    pre = input ("cual es la contraseña: ")
    if pre == contrasenia:
            print ("contraseña correcta")
            break
    else:
        print ("contraseña incorrecta intentalo de nuevo")
     
            
      


