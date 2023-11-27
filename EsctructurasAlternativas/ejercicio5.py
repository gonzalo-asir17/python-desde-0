#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.


usuario = input("Introduce el nombre de usuario: ")
contraseña = input("Introduce la contraseña: ")

if usuario == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error")
print("Fin del programa")


