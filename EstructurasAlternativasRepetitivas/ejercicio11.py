#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 29/11/2023
#Escribe un programa que diga si un número introducido por teclado es o no primo. 
#Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
#Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

import os
import math

os.system ("clear")

numero = int(input("Introduzca un numero "))
raiz = int(math.sqrt(numero))
primo = True

for i in range(2, raiz + 1):
    if numero % i == 0:
        primo = False
if primo:
    print("El numero es primo")
else:
    print("El numero no es primo")
print("Fin del programa")

