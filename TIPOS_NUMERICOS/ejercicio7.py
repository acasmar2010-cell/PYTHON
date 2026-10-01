peso =  float (input ("dime tu peso en kg: "))
estatura = float (input ("ahora dime tu estatura en metros: "))


masacor = (peso / (estatura ** 2))
imc = round(peso / (estatura ** 2), 2)


print (f"Tu índice de masa corporal es {masacor} donde {imc} es el índice de masa corporal calculado redondeado con dos decimales. ")

