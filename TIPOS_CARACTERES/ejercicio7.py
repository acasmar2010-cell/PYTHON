#Ejercicio 7
#Escribir un programa que pregunte
#el correo electrónico del usuario en la consola
#y muestre por pantalla otro correo electrónico con el mismo nombre
#(la parte delante de la arroba @) pero con dominio ceu.es.


correo = input ("dime correo: ")


parar = correo.split ('@')
dos = parar [1]


nuevo = "ceu.es"


final = correo.replace (dos,nuevo )


print (f"tu correo despues de ser modificado es {final}")
