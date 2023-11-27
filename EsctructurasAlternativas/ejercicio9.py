#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

numero1 = int(input("Introduzca el primer numero "))
numero2 = int(input("Introduzca el segundo numero "))
numero3 = int(input("Introduzca el tercer numero "))

if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print("Este es el orden de los numeros", numero1, numero2, numero3)
    else:
        print("Este es el orden de los numeros", numero1, numero3, numero2)
if numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print("Este es el orden de los numeros", numero2, numero1, numero3)
    else:
        print("Este es el orden de los numeros", numero2, numero3, numero1)
if numero3 >= numero1 and numero3 >= numero2:
    if numero1 > numero2:
        print("Este es el orden de los numeros", numero3, numero1, numero2)
    else:
        print("Este es el orden de los numeros", numero3, numero2, numero1)
print("Fin del programa")
