#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 03/12/2023
#Realizar un programa que comprueba si una cadenas contiene 
#subcadena las dos cadenas introducelas por teclado

cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")

if cad.find(subcad) > -1:
    print("La cadena con tiene la subcadena")
else:
    print("La cadena no tiene la subcadena")

#Otra manera de hacerlo
if subcad in cad:
    print("La cadena con tiene la subcadena")
else:
    print("La cadena no tiene la subcadena")