#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 24/11/2023
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Introduzca su nombre ")
apellido1 = input("Introduzca su primer apellido ")
apellido2 = input("Introduzca su segundo apellido ")

inicial1 = nombre[0]
inicial2 = apellido1[0]
inicial3 = apellido2[0]

iniciales = inicial1 + inicial2 + inicial3

print("Las iniciales son", iniciales)