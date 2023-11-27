#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
# Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
#  * El exponente sea positivo, sólo tienes que imprimir la potencia.
#  * El exponente sea 0, el resultado es 1.
#  * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = int(input("Introduce la base "))
exponente = int(input("Introduce el exponente "))
potencia = 0

if exponente > 0:
    potencia = base ** exponente
    print("La potencia es: ", potencia)
elif exponente == 0:
    print("El resultado es 1")
else:   
    potencia = base ** exponente
    print("El resultado es:", 1 / potencia)
print("Fin del programa")
