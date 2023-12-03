#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 03/12/2023
#Realizar un pograma que compruebe si una cadena leida por 
#teclado comienza por una subcadena introducida por teclado

cad = input("Introduce una cadena ")
subcad = input("Introduce otra cadena ")

if cad.startswith(subcad):
    print("La cadena empieza por la subcadena")
else:
    print("La cadena no empieza por la subcadean")

print("Fin del programa")