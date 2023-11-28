#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023

#Introducir 5 número y contar los números pares.
cont = 0;
for var in range(1,6):
    num = int(input("Dime un número "))
    if num % 2 == 0:
        cont = cont + 1
print("Has introducido",cont,"números pares.")
print("Fin del Programa")

print()
print("Sumar los numeros pares")

#Introducir 5 número y sumar los números pares.
suma = 0
for var in range(1,6):
    num = int(input("Dime un número:"))
    if num % 2 == 0:
        suma = suma + num
print("La suma de los números pares es ",suma)

#Introducir 5 número e indicar si se ha introducido algún número par.
print()
print("Indicar si se ha introducido algún número par")
indicador  =  False;
for var in range(1,6):
    num = int(input("Dime un número "))
    if num % 2 == 0:
        indicador  = True
if indicador:
    print("Has introducido algún número par")
else:
    print("No has introducido algún número par")


