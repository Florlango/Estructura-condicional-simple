#Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el 
#cambio de dólares a pesos y que sea el usuario quién decida qué tipo
#de cambio quiere, si de dólares a pesos o viceversa.

monto = float (input  ("Ingrese el monto a convertir, y luego su moneda: "))
moneda_inicial = str (input ("¿Son dólares o pesos?: "))
if moneda_inicial == ("pesos") :
    dolares = monto / 872.76
    print ("Usted recibirá", dolares, "dólares")
elif moneda_inicial == ("dolares")or("dólares") :
    pesos = monto * 872.76
    print ("Usted recibirá", pesos, "pesos")
print ("Gracias por usar nuestros servicios")
