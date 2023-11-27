#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
#la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta 
#del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un 
#productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
#se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. 
#Si es de tipo B, se rebajan 30 céntimos cuando es de 
#tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

precio_inicial = float(input("Introduzca el precio inicial de la uva "))
tipo = input("Introduzca de que tipo es la uva (A/B) ")
tamaño = int(input("Introduzca el tamaño de la uva (1/2) "))

if tipo == tipo.upper() == 'A':
    if tamaño == 1:
        print("Es de tipo A y tamaño 1")
        precio_final = precio_inicial + 0.2
        print("El precio final es", precio_final,"€")
    else:
        print("Es de tipo B y tamaño 2")
        precio_final = precio_inicial + 0.3
        print("El precio final es", precio_final,"€")

if tipo == tipo.upper() == 'B':
    if tamaño == 1:
        print("Es de tipo B y tamaño 1")
        precio_final = precio_inicial - 0.2
        print("El precio final es", precio_final,"€")
    else:
        print("Es de tipo B y tamaño 2")
        precio_final = precio_inicial - 0.5
        print("El precio final es", precio_final,"€")

print("Fin Programa")