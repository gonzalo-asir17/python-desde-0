#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 28/11/2023
#Crea una aplicación que permita adivinar un número. La aplicación genera un número 
#aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el 
#número a adivinar es mayor o menor que el introducido,a demás de los intentos que te 
#quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el 
#número (además te dice en cuantos intentos lo has acertado), si se llega al limite de 
#intentos te muestra el número que había generado.

import random
import sys
import os



result = random.randint(1, 100)
life = "❤"
numLif= 10
allLifes = ""
brokeHeart = "💔"
nolife = 0

for i in range(10):
    
    for j in range(numLif):
        allLifes += life
    for j in range(nolife):
        allLifes += brokeHeart
    print("vidas: ", allLifes)
    numero = int(input("Introduzca un numero para acertar "))
    os.system ("clear")
    if numero == result:
        print("¡¡Felicidades acertaste el numero!!")
        print("Realizo un total de ", i,"intentos")
        sys.exit()
    elif result > numero:
        print("Haz fallado el numero es mayor que", numero, "\n")
    else:
        print("Haz fallado el numero es menor que", numero, "\n")
    numLif -= 1
    nolife += 1
    allLifes = ""

print("vidas: ", allLifes, "vaya no lifes hehehehehehe")   
print("Ya realizo 10 intentos, el bingo termino, el numero era: ", result)