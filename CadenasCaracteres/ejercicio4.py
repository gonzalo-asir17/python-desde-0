#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 03/12/2023
#Suponiendo que hemos introducido una cadena por teclado
#que represetna una frase
#realiza un programa que cuente las palabras que tiene

cont = 0
posicion = 0

cad = input("Introduce la cadena por teclado")
#Elimina los espacios
cad = cad.strip()
#Buscar espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
    cont = cont + 1
    while cad[posicion + 1] == " ":
        posicion = posicion + 1
    posicion = cad.find(" ", posicion + 1)
print("La frase tiene", cont + 1,"palabras")


