#Ejercicio 5 
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión. 

dinero = int (input ("dime una cantidad a invertir: "))
interes = int (input ("dime tu intres anual: "))
anios = int (input ("dime el numero de años : "))

for i in range( anios):
    dinero = dinero + interes   
    print(f"Año {i + 1}: {dinero} €")


