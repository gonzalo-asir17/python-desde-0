#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 30/11/2023
#Una persona adquirió un producto para pagar en 20 meses. 
#El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
#Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de
#lo que pagó después de los 20 meses.

#Declaracion de variables
meses = 20
total = 0
pago = 10

#Bucle para calcular el total
for i in range(1, meses + 1):
    total += pago
    print("El mes", i, "pagó", pago, "€")
    pago *= 2

#Mostrar el total
print("El total pagado es", total, "€")
print("Fin del programa")

