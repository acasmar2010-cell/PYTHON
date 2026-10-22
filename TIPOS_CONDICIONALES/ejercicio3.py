
# Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

numreo = int (input ("dime un numero: "))
divisor = int (input ("dime otra numero: "))



if divisor == 0 : 
    print ("error no se puede dividir entre 0")

else:
    cuenta = (numreo / divisor)

    print (f" el resultado de la division es {cuenta}")