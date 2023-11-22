#!/usr/bin/python3
#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. 
#Recordar que la fórmula para la conversión es:
#C = (F-32)*5/9

import math

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = round((fahrenheit-32)*5/9 , 3)
print("La temperatura en grados Celsius es: ", celsius)


