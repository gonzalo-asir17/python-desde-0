#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023#
#Escribe un programa que pida un número entero entre uno y
#doce e imprima el número de días que tiene el mes correspondiente

mes = int(input("Introduzca el numero del mes "))
if mes == 1:
    print("Enero tiene 31 dias")
elif mes == 2:  
    print("Febrero tiene 28 dias (29 si es bisiesto)")
elif mes == 3:
    print("Marzo tiene 31 dias")
elif mes == 4:
    print("Abril tiene 30 dias")
elif mes == 5:
    print("Mayo tiene 31 dias")
elif mes == 6:
    print("Junio tiene 30 dias")
elif mes == 7:
    print("Julio tiene 31 dias")
elif mes == 8:
    print("Agosto tiene 31 dias")
elif mes == 9:
    print("Septiembre tiene 30 dias")
elif mes == 10:
    print("Octubre tiene 31 dias")
elif mes == 11:
    print("Noviembre tiene 30 dias")
elif mes == 12:
    print("Diciembre tiene 31 dias")
else:
    print("ERROR: numero incorrecto")
print("Fin del programa")

