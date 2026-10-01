
cantidad = float (input ("dime una cantidad a invertir " ))
interesa = float (input ("dime tu interes anual  " ))
anos = int (input ("dime el numero de años  " ))

capitalobtenido = cantidad * (1 + interesa / 100) ** anos

print ("el capital obtenido en la inversion es de : ", capitalobtenido)