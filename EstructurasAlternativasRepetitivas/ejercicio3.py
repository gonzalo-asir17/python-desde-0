#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 28/11/2023
#Algoritmo que pida números hasta que se introduzca un cero. 
#Debe imprimir la suma y la media de todos los números introducidos.

import math
iterator = 0
suma = 0
numero = -1
while numero != 0:
    iterator += 1
    numero = int(input("Introduzca un numero "))
    suma = round(suma + numero, 4)
    
media = suma / (iterator - 1)
print("La suma de todos los numero introducidos es ", suma)
print("La media de los numeros introducidos ", media)

print("Fin del programa")