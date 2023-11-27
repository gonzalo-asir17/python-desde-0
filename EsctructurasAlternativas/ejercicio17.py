#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023#
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al 
#lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) 
#de la cara opuesta al resultado obtenido.
#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
#Ejemplo:
#Introduzca número del dado: 5
#En la cara opuesta está el "dos".

dado = int(input("Introduzca el numero del dado "))

if dado == 1:
    print("En la cara opuesta esta el seis")
elif dado == 2:
    print("En la cara opuesta esta el cinco")
elif dado == 3:
    print("En la cara opuesta esta el cuatro")
elif dado == 4:
    print("En la cara opuesta esta el tres")
elif dado == 5:
    print("En la cara opuesta esta el dos")
elif dado == 6:
    print("En la cara opuesta esta el uno")
else:
    print("ERROR: numero incorrecto")
print("Fin del programa")