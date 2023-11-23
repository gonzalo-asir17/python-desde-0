#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 23/11/2023
#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 

numero = int(input("Introduzca un numero de dos cifras "))
decenas = numero // 10
unidades = numero % 10
numero_invertido = (unidades * 10) + decenas

print("El numero invertido es", numero_invertido)


