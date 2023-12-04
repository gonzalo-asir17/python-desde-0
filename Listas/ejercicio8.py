#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 04/12/2023
#Queremos guardos los nombres y las edades de los alumnos de un curso
#Realiza un programa que introduzca el nombre y la edada de cada alumno
#EL proceso de lectura de datos terminara cuando se introduzca como nombre un asterisco. 
#Al finalizar se muestra los siguientes datos:
#Todos los alumnos mayores de edad
#Los alumnos mayores ( los que tiene mas edad)

nombres = []
edades = []

while True:
    nombre = input("Dime el nombre del alumno: ")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime su edad: ")))
    if nombre == "*": break;

#Calcular la edad maxima
edad_max = max(edades)
#Alumnos mayores de edad
print("Alumnos mayores de edad")
print("=======================")
for nombre,edad in zip(nombre,edades):
    if edad >= 18:
        print(nombre)

#Alumnos mayores
print("Alumnos mayores")
print("===============")
for nombre,edad in zip(nombre,edades):
    if edad == edad_max:
        print(nombre)
