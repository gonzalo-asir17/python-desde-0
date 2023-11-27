#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
#El director de una escuela está organizando un viaje de estudios, 
#y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe 
#pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: 
#si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, 
#el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta 
#del autobús es de 4000 euros, sin importar el número de alumnos.
#Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que 
#debe pagar cada alumno por el viaje.


n_alumnos = int(input("Introduzca cuantos alumnos van al viaje "))

if n_alumnos >= 100:
    print("Cada alumno debe pagar 65€ ")
    preciofinal = n_alumnos * 65 
    print("El precio final del viaje es", preciofinal,"€")
elif n_alumnos >= 50 and n_alumnos <= 99:
    print("Cada alumno debe pagar 70€ ")
    preciofinal = n_alumnos * 70 
    print("El precio final del viaje es", preciofinal,"€")
elif n_alumnos >=30 and n_alumnos <=49:
    print("Cada alumno debe pagar 95€ ")
    preciofinal = n_alumnos * 95
    print("El precio final del viaje es", preciofinal,"€")
else:
    preciofinal = 4000/n_alumnos
    print("Como son menos de 30 alumnos cada uno deber pagar", preciofinal,"€")
print("Fin del programa")

