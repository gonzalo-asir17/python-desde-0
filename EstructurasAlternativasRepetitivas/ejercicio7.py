#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 29/11/2023
#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado

tabla = int(input("Que tabla de multiplicar quieres saber "))

for i in range(1, 11):
    print(tabla, "x", i, "=", tabla * i)    
print("Fin del programa")



