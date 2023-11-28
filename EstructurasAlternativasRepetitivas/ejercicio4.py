#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 28/11/2023
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
#El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.


import random
import os
import sys


mayor = 0
cero = 0
menor = 0

result = random.randint(5, 15)
print
for i in range(result):
    
    numero = int(input("Introducir un numero "))
    if numero == 0:
        cero = cero + 1
    elif numero > 0:
        mayor += 1
    else:
        menor += 1
os.system ("clear")    

print("Hay", cero, "cero(s) en los numeros introducidos")
print("Hay", mayor, "numeros mayores que cero en los numeros introducidos")
print("Hay", menor, "numeros menores que cero en los numeros introducidos")

        