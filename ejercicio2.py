#!/usr/bin/python3
# Ejercicio 2
# Calcular el perímetro y área de un rectángulo dada su base y su altura.
import math

base = float(input("Introduzca la base: "))
altura = float(input("Introduzca la altura: "))

perimetro = round(2 * (base + altura), 2)
area = round(base * altura, 2)

print("Este es el perímetro:", perimetro)
print("Esta es el área:", area)

