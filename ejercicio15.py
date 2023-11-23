#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 23/11/2023
#Dadas dos variables numéricas A y B, que el usuario debe teclear, 
#se pide realizar un algoritmo que intercambie los valores de ambas variables y 
#muestre cuánto valen al final las dos variables.

A = int(input("Introduzca un valor para A "))
B = int(input("Introduzca un valor para B "))

C = A
A = B
B = C

print()
print("Este es el valor final de A ", A)
print("Este es el valor final de B ", B)
