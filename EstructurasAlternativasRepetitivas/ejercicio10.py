#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 29/11/2023
#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

import os

os.system ("clear")

for i in range(1,6):
    print("Tabla del ", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("") 
print("Fin del programa")