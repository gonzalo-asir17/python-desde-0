#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 29/11/2023
#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
#si al final de cada mes deposita cantidades variables de dinero; además, 
#se quiere saber cuánto lleva ahorrado cada mes.

import os


ahorro = 0

os.system("clear")

for i in range(1, 13):
    print("Mes ", i)
    mes = 0  # Reset the monthly savings to 0 at the beginning of each month
    for j in range(1, 5):
        print("Semana ", j)
        dinero = float(input("Introduzca el dinero que ha ahorrado hoy "))
        print("")
        mes += dinero
    ahorro += mes
    print("Lleva ahorrado ", mes, "€ en el mes ", i, "\n")
print("Ha ahorrado ", ahorro, "€ en el año")







