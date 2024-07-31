#Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.
sexo = input("Ingrese F o M según corresponda: ")
if sexo == "F" :
    print ("Vota en mesa femenina")
elif sexo == "M" :
    print ("Vota en mesa masculina")
else:
    print ("El dato ingresado no es válido")
