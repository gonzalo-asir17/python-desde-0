#!/usr/bin/python3
#Dados lo catetos de un triangulo rectangulo, calcular su hipotenusa

import math
cateto1 = float(input("Introduce el cateto 1: "))
cateto2 = float(input("Introduce el cateto 2: "))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print("La hipotenusa es {:.2f}".format(hipotenusa))
 