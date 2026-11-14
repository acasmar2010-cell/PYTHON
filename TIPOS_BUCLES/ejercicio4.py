
#Ejercicio 4 
# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 

resultado = ""
numero = int (input("dime un numero entero positivo: "))

for i in range (numero,0, -1):
    resultado = resultado + str(i) + "," 
    
print (resultado [:-1])
