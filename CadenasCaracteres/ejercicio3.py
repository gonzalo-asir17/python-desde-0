#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
#Pide una cadena y un caracter por teclado
#(valida que sea un caracter) y muestra cuantas veces
#aparece el caraceter en la cadena

cad = input("Introduce una cadena ")
while True:
    car = input("Introduce un caracter ")
    if len(car) > 1:
            print("Dame solo un caracter")
    if len(car) == 1: break

print("En la cadena", cad, "aparecen", cad.count(car), "veces el caracter")