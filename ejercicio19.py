#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 24/11/2023
#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, 
#por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

#Pedimos los datos al usuario
correctas = int(input("Introduce el numero de respuestas correctas "))
incorrectas = int(input("Introduce el numero de respuestas incorrectas "))
blanco = int(input("Introduce el numero de respuestas en blanco "))

correctas *=5
incorrectas *= -1
blanco *= 0

nota = correctas + incorrectas + blanco 

print("La nota final es", nota)

