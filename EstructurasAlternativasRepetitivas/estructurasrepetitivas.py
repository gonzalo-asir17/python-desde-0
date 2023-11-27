#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023

#Como hacer un bucle while
secreto = "asdasd"

clave = input("Dime la clave: ")
while clave != secreto:
    print("Clave incorrecta!!!")
    clave = input("Dime la clave: ")

print("Bienvenido!!!")
print("Programa terminado")