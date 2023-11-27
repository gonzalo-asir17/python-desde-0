#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones 
#de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

A = int(input("Introduzca el lado A "))
B = int(input("Introduzca el lado B "))
C = int(input("Introduzca el lado C "))

if A == B and A == C:
    print("El triangulo es rectangulo, todos sus lados son iguales")
elif A == B and A != C or B == C and A != B:
    print("El triangulo es isoceles, tiene dos lados iguales")
elif A != B and A != C and B != C:
    print("El triangulo es escaleno, todos sus lados son diferentes")
else:
    print("El triangulo es rectangulo, cumple el teorema de pitagoras")
print("Fin del programa")


