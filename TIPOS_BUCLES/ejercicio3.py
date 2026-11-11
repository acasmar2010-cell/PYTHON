#Ejercicio 3 
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.



num = int (input("dime un numero entero positivo: "))

resultado = ""
for i in range(1, num ):
    
    if i % 2 != 0: 
        
        resultado = resultado + str(i) + ", "
print (resultado)
