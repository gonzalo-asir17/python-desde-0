#!/usr/bin/python3
#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, 
#el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las 
#tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

import math

sueldo_base = float(input("Introduzca su sueldo base: "))

venta1 = float(input("Introduzca el valor de la primera venta: "))
venta2 = float(input("Introduzca el valor de la segunda venta: "))
venta3 = float(input("Introduzca el valor de la tercera venta: "))

comision = round(((venta1 + venta2 + venta3) * 0.1), 3)
total = round((sueldo_base + comision), 3)
print()
print("Dinero obtenido por la comisión de las ventas:", comision)
print("Dinero obtenido por el sueldo base + comisiones:", total)




