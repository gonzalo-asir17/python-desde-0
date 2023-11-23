#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 23/11/2023
#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. 
#Calcula y muestra la distancia entre ellos.
#Formula para calcular la distancia d=√((x_2-x_1)²+(y_2-y_1)²)


import math

x1 = float(input("Introduce las cordenadas para x1: "))
y1 = float(input("Introduce las cordenadas para y1: "))

x2 = float(input("Introduce las cordenadas para x2: "))
y2 = float(input("Introduce las cordenadas para y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  #Formula para calcular la distancia d=√((x_2-x_1)²+(y_2-y_1)²)


print("La distancia entre los puntos es de",distancia)
