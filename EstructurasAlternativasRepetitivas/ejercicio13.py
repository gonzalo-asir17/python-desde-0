#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 30/11/2023
#Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) 
#y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

import os
import sys

horas = 0
sueldo = 0
os.system("clear")

for i in range(1, 7):
    print("Dia ", i)
    horas = int(input("Introduzca las horas que ha trabajado hoy "))
    sueldo += horas
    print("")
print("Ha trabajado", sueldo, "horas esta semana")
print("Su sueldo es de", sueldo * 10, "€")
print("Fin del programa")
sys.exit()

