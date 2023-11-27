#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 24/11/2023
# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.

#Petición de datos
numero1 = float(input("Introduce el primer numero: "))
numero2 = float(input("Introduce el segundo numero: "))
#Comprobación de datos
if numero2 == 0:
    print("No se puede dividir entre 0")
else:   
    print("La division de los numeros es: ", numero1/numero2)

    