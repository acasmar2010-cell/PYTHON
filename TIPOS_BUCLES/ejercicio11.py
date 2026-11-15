#Ejercicio 11 
# Escribir un programa que pida al usuario una palabra y luego muestre 
# por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input ("dime una palabra: ")
resultado = " "

for i in palabra:
    resultado = str(i) + " " + resultado
print (resultado)