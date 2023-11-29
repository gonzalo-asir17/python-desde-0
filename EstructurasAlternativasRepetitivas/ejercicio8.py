#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 29/11/2023

#Escribe un programa que pida el limite inferior y superior de un intervalo. 
#Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
#A continuación se van introduciendo números hasta que introduzcamos el 0. 
#Cuando termine el programa dará las siguientes informaciones:

#La suma de los números que están dentro del intervalo (intervalo abierto).
#Cuantos números están fuera del intervalo.
#He informa si hemos introducido algún número igual a los límites del intervalo.

import os

limite_inferior = 0
limite_superior = 0
suma = 0
fuera_intervalo = 0
igual_limite = 0
numero = 1

os.system ("clear")

while limite_inferior >= limite_superior:
    limite_inferior = int(input("Introduce el limite inferior "))
    limite_superior = int(input("Introduce el limite superior "))
    if limite_inferior >= limite_superior:
        print("El limite inferior debe ser menor que el superior. Introduzca de nuevo los limites")
print("")

while numero != 0:
    numero = int(input("Introduce un numero (0 para salir) "))
    if numero != 0:
        if numero > limite_inferior and numero < limite_superior:
            suma += numero
        elif numero > limite_superior:
            fuera_intervalo += 1
        if numero == limite_inferior or numero == limite_superior:
            igual_limite += 1
print("")

print("Suma de los numeros dentro del intervalo: ", suma)
print("Numeros fuera del intervalo: ", fuera_intervalo)
print("Numeros iguales a los limites del intervalo: ", igual_limite)








