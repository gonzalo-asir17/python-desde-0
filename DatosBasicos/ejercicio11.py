#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 23/11/2023
#Pide al usuario dos números y muestra la “distancia” entre ellos 
#(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

numero1 = int(input("Introduzca un numero "))
numero2 = int(input("Introduzca otro numero "))


distancia = abs (numero1 - numero2)

print("La distancia entre los numeros es", distancia)

