#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 24/11/2023
# Algoritmo que pida un número y diga si es positivo, negativo o 0.
num = int(input("Dime el número "))
if num == 0:
    print("Es igual a 0")
else:
    if num > 0:
        print("Es positivo")
    else:
        print("Es negativo")
print("Programa terminado")
