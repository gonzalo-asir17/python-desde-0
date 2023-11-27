#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 27/11/2023
# Una compañía de transporte internacional tiene servicio en algunos países de 
# América del Norte, América Central, América del Sur, Europa y Asia. El costo 
# por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. 
# Lo anterior se muestra en la tabla:
# Zona
# Ubicación
# Costo/gramo

# América del Norte  24.00 euros
# América Central  20.00 euros
# América del Sur  21.00 euros
# Europa  10.00 euros
# Asia  18.00 euros

# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, 
# esto por cuestiones de logística y de seguridad.
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

peso = float(input("Introduzca el peso del paquete en Kg "))
zona = input("A que zona quiere enviar su pedido (Norte/Central/Sur/Europa/Asia) ")

if peso >= 5:
    print("El paquete pesa mas de 5 Kg ")
else:
    if zona == 'Norte':
        precio = 24 * peso
        print(precio)
        print("El precio de envio a America del Norte es", precio,"€")
    elif zona == 'Central':
        precio = 20 * peso
        print("El precio de envio a Amercia Central es", precio,"€")
    elif zona == 'Sur':
        precio = 21 * peso
        print("El precio de envio a America del Sur", precio,"€")
    elif zona == 'Europa':
        precio = 10 * peso
        print("El precio de envio a Europa es", precio,"€")
    elif zona == 'Asia':
        precio = 18 * peso
        print("El precio de envio a Asia es", precio,"€")
    else:
        print("La zona introducida no es correcta")
print("Fin del programa")

