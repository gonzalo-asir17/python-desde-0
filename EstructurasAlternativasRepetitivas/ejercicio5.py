#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 28/11/2023
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso 
#contrario, el programa termina cuando se introduce un espacio.

import math

while True:
    caracter = input("Introduce un caracter (o espacio para salir): ")

    if caracter == ' ':
        break

    if caracter.lower() in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")



     

