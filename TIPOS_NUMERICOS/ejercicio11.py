


dinero = float(input("Dime la cantidad de dinero depositada en la cuenta: "))

año1 = round(dinero * 1.04, 2)
año2 = round(año1 * 1.04, 2)
año3 = round(año2 * 1.04, 2)

print(f"La cantidad de ahorros tras el primer año es de {año1}, tras el segundo es {año2} y tras el tercero es {año3}")