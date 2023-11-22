#Realiza un programa que reciba una cantidad de minutos 
#y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int(input("Introduzca una cantidad de minutos "))


if minutos < 60:
    print("Es menor de 60 el numero introducido, pongas mas de 60 para poder transformarlo a horas")
else:
    horas = minutos // 60
    minutos_restantes = minutos % 60
    print(f"Introducio {minutos} minutos, eso equivale a {horas} horas y {minutos_restantes} minutos.")
    

