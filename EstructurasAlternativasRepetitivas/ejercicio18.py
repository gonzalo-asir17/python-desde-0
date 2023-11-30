#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 30/11/2023
#Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos. =

horas = 0
minutos = 0
segundos = 0

import time, os

while True:
    print("Horas:", horas, "Minutos:", minutos, "Segundos:", segundos)
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1
    if horas == 24:
        horas = 0
    time.sleep(1)

    os.system("clear")

