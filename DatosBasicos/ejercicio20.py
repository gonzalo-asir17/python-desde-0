#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 24/11/2023
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
#después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

monedas2euros = int(input("Introduzca cuantas monedas de 2€ tiene "))
monedas1euro = int(input("Introduzca cuantas monedas de 1€ tiene "))
monedas50cent = int(input("Introduzca cuantas monedas de 50cent tiene "))
monedas20cent = int(input("Introduzca cuantas monedas de 20cent tiene "))
monedas10cent = int(input("Introduzca cuatnas monedas de 10cent tiene "))

total = (monedas2euros * 2) + (monedas1euro) + (monedas50cent * 0.5) + (monedas20cent * 0.2) + (monedas10cent * 0.1)

print("El total de dinero que tiene es", total, "€")
