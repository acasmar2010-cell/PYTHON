#Ejercicio 10 
# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es un número primo o no. 


num = int(input("Dime un número entero: "))

if num <= 1:
    print("No es primo")
else:
    es_primo = True  
    
    for i in range(2, num):
        if num % i == 0:  
            es_primo = False  
            break  

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")