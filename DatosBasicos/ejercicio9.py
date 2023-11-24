#!/usr/bin/python3
#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
#desea saber cuanto deberá pagar finalmente por su compra.
#para poner el simbolo de € es "\u20AC"

precio = float(input("Introduzca el precio de compra "))

rebaja = precio * 0.15
precio_final = precio - rebaja

print("Este es el precio final de la compra", precio_final , "\u20AC")
