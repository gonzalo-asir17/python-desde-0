#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 24/11/2023
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por
#una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un 
#algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas 
#velocidades (km/h) y con esto determinar y mostrar en qué tiempo (minutos) alcanzará el vehículo más rápido al otro.

distancia = float(input("Introduzca la distancia entre los dos vehiculos "))
v1 = float(input("Introduzca la velocidad del primer vehiculo "))
v2 = float(input("Introduzca la velocidad del segundo vehiculo "))

tiempoM = round(distancia / (v1 - v2) * 60, 3)

print("El tiempo que tardara el segundo vehiculo en alcanzar al primero es de", tiempoM, "minutos")

