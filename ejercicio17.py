#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 24/11/2023
#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
#Escribir un algoritmo que determine la hora de llegada a la ciudad B.

#Pedimos los datos al usuario
hora = int(input("Introduzca la hora de salida "))
minutos = int(input("Introduzca los minutos de salida "))
segundos = int(input("Introduzca los segundos de salida "))
print("La hora de salida es", hora, ":", minutos, ":", segundos)

tiempo = int(input("Introduzca el tiempo que tardara en llegar a la ciudad B en segundos "))

hora_llegada = hora + (tiempo // 3600) 
# mirar el resultado print(hora_llegada)
minutos_llegada = (minutos + ((tiempo % 3600) // 60)) 
# mirar el resultado print(minutos_llegada)
segundos_llegada = segundos + ((tiempo % 3600) % 60)
# mirar el resultado print(segundos_llegada)

if segundos_llegada >= 60:
    segundos_llegada -= 60
    minutos_llegada += 1
#Probar lo que almacena el este IF print(hora_llegada":"minutos_llegada":", segundos_llegada)

if minutos_llegada >= 60:
    minutos_llegada -= 60
    hora_llegada += 1

print("La hora de llegada a la ciudad B es", hora_llegada,":", minutos_llegada,":", segundos_llegada)


