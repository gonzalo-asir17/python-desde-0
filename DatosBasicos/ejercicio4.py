#!/usr/bin/python3
#Ejercicio 4
#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

import math

numero1 = float(input("Introduzca un numero "))
numero2 = float(input("Introduzca otro numero "))

suma = round(numero1 + numero2)
resta = round(numero1 - numero2)
division = round(numero1 / numero2)
multiplicacion = round(numero1 * numero2)

print("Este es el resultado de la suma", suma)
print("Este es el resultado de la resta", resta)
print("Este es el resultado de la division", division)
print("Este es el resultado de la multiplicacion", multiplicacion)


