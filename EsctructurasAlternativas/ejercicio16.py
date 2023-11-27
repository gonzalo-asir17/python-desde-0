#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, 
#el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos 
#cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, 
#y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 
#15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por 
#cada concepto una persona que realiza una llamada.

tiempo = int(input("Introduzca el tiempo de la llamada "))
dia = input("Introduzca el dia de la llamada (Lunes-Domingo) ")
turno = input("Introduzca el turno de la llamada (M/T) ")

if tiempo <= 5:
    print("El precio de la llamada es 1€")
    precio = 1
elif tiempo <= 8:
    print("El precio de la llamada es 1.8€")
    precio = 1.8
elif tiempo <= 10:
    print("El precio de la llamada es 2.5€")
    precio = 2.5
elif tiempo > 10:
    precio = 2.5 + (0.5 * tiempo)
    print("El precio de la llamada es", precio,"€")

if dia == dia.upper() == 'Domingo':
    print("El impuesto es de un 3%")
    precio = precio + (precio * 0.03)
    print("El precio final es", precio,"€")
elif turno == turno.upper() == 'M':
    print("El impuesto es de un 15%")
    precio = precio + (precio * 0.15)
    print("El precio final es", precio,"€")
else:
    print("El impuesto es de un 10%")
    precio = precio + (precio * 0.1)
    print("El precio final es", precio,"€")

print("Fin del programa")

