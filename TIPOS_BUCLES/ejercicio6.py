#Ejercicio 6 
# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla un triángulo rectángulo como el de más abajo, 
# de altura el número introducido. 

num = int (input ("dime un numero entero: "))

resultado = ""
for i in range (1, num):
    i = "*"
    resultado = resultado + str(i) 

    print (resultado)
