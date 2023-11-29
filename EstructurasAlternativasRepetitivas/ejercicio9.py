#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 29/11/2023
#Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), 
#saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

import os

os.system ("clear")
resultado = 1

numero_real = int(input("Introduce la base: "))
entero_positivo = int(input("Introduce el exponente: "))

for i in range(entero_positivo):
    resultado *= numero_real
print("El resultado es ", resultado)
print("Fin del programa")


