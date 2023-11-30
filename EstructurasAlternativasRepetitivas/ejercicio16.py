#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 30/11/2023
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
#Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, 
#calcule cuánto pagó la empresa por los N empleados.

#Declaracion de variables
horas = 0
sueldo = 0
total = 0
empleados = 0

for i in range(1, 6):
    horas = int(input("Introduce las horas trabajadas del empleado " + str(i) + ": "))
    sueldo = int(input("Introduce el sueldo por hora del empleado " + str(i) + ": "))
    total += horas * sueldo
    empleados += 1

print("El total pagado a los", empleados, "empleados es", total, "€")
print("Fin del programa")
