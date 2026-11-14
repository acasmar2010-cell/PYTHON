#Ejercicio 8 
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

num = int (input("dime un numero entero: "))
resultado = ""
for i in range (0 , num + 1):
    if i % 2 != 0:
        resultado =  str(i) + " " +resultado 

        print ( resultado)



