#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 23/11/2023
#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
#Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?
#Formula para hacer la raiz cubica: https://www.youtube.com/watch?v=Q0bn8ZDikz0 numero**(1/3)

import math

numero = int(input("Introduzca un numero "))

cuadrado = round(math.sqrt(numero), 4)
cubica = round(numero**(1/3), 4)

print("Esta es la raiz cuadrada del numero que introdujo ", cuadrado)
print("Esta es la raiz cubica del numero que introdujo ", cubica)
