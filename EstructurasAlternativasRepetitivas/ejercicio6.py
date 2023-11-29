#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 29/11/2023
#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.


numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce otro numero: "))
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()
print("Fin del programa")