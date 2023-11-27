#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Introduzca el dia "))
mes = int(input("Introduzca el mes "))
año = int(input("Introduzca el año "))

if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and año > 0:
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")
print("Fin del programa")
