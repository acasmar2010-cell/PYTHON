#Ejercicio 2 
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


edad = int (input("dime tu edad: "))
print ("estos son todos los años hasta tu edad: ")

for i in range(0, edad):
    print (i)