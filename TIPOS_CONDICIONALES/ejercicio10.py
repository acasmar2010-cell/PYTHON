#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.


#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.


#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
#en función de su respuesta le muestre un menú 
# con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.


respuesta = input ("quieres pizza vegetariana? responde con si o no: ")

if respuesta == "si":
    vegeteariana = input (" menu: Pimiento y tofu : cual es el ingrediente extra que quieres en la pizza: ") 
    print (f"su pizza es vegetariana y lleva {vegeteariana} , mozzarella y tomate")
else :
    novegetariana = input ("menu: Peperoni, Jamón y Salmón : cual es el ingrediente extra que quieres en la pizza: ")
    print (f"su pizza no es vegetariana y lleva {novegetariana} , mozzarella y  tomate")

   
    