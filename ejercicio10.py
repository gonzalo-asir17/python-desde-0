#!/usr/bin/python3
#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
#Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.


parcial1 = float(input("Introduce la nota del primer parcial "))
parcial2 = float(input("Introduce la nota del segundo parcial "))
parcial3 = float(input("Introduce la nota del tercer parcial "))
examen_final = float(input("Introduce la nota del examen final "))
trabajo_final = float(input("Introduce la nota del trabajo final "))

mediaparciales = (parcial1 + parcial2 + parcial3) / 3
mediaparciales *= 0.55
examen_final *= 0.3
trabajo_final *= 0.15

notafinal = mediaparciales + examen_final + trabajo_final

print("La nota final de la meteria de Algoritmos es ", notafinal)

