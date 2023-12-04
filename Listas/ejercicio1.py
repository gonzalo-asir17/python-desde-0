#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
#Realizar un programa que inicialice una lista con 10 valores aleatorios
#y posteriormente muestre en pantalla cada elemento de la lista junto
# a su cubp

import random
lista_numero= []

for indice in range(1,11):
    lista_numero.append(random.randint(1,10))

for numero in lista_numero:
    print(numero, " ",numero ** 2," ",numero ** 3)
