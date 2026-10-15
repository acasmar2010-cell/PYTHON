#Ejercicio 8
# Escribir un programa que pregunte por consola
# el precio de un producto en euros con dos decimales
# y muestre por pantalla el número de euros y el número
# de céntimos del precio introducido.




precio = input("Dime cuál es el precio del producto: ")


# Reemplazamos la coma por punto (por si acaso) y luego separamos
dinero = precio.split('.')


euros = dinero[0]
centimos = dinero[1]


print(f"Cuesta {euros} euros con {centimos} céntimos")

