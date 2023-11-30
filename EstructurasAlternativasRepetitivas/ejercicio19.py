#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 30/11/2023
#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

import time, os
import random
import sys
import os
import time

opcion = ""
horas = 0
minutos = 0
segundos = 0

while opcion < "a" or opcion > "d":
    print("Bienvenido al menu de Gonzalo Rodriguez Martin")
    print("a. Cronometro")
    print("b. Bingo")
    print("c. Limites")
    print("d. Salir")

    while opcion != "d":
        opcion = input("Introduce una opcion: ").lower()

match opcion:
    case "a":
        while True:
            print("Horas:", horas, "Minutos:", minutos, "Segundos:", segundos)
            segundos += 1
            if segundos == 60:
                segundos = 0
                minutos += 1
            if minutos == 60:
                minutos = 0
                horas += 1
            if horas == 24:
                horas = 0
            time.sleep(1)

            os.system("clear")
    case "b":
        while True:
            result = random.randint(1, 100)
            life = "❤"
            numLif = 10
            allLifes = ""
            brokeHeart = "💔"
            nolife = 0

            start_time = time.time()

            for i in range(10):
                for j in range(numLif):
                    allLifes += life
                for j in range(nolife):
                    allLifes += brokeHeart
                print("vidas: ", allLifes)
                numero = input("Introduzca un numero para acertar ")
                os.system("clear")

                if numero:
                    numero = int(numero)
                    if numero == result:
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        print("¡¡Felicidades acertaste el numero!!")
                        print("Realizaste un total de ", i, "intentos")
                        print("Tiempo transcurrido: {:.2f} segundos".format(elapsed_time))
                        break
                    elif result > numero:
                        print("Haz fallado, el numero es mayor que", numero, "\n")
                    else:
                        print("Haz fallado, el numero es menor que", numero, "\n")

                numLif -= 1
                nolife += 1
                allLifes = ""
                current_time = time.time() - start_time
                print("Tiempo transcurrido: {:.2f} segundos".format(current_time))

            print("vidas: ", allLifes, "vaya no lifes hehehehehehe")
            print("Ya realizó 10 intentos, el bingo terminó. El número era: ", result)
    
    case "c":
        while True:
            import os

            limite_inferior = 0
            limite_superior = 0
            suma = 0
            fuera_intervalo = 0
            igual_limite = 0
            numero = 1

            os.system ("clear")

            while limite_inferior >= limite_superior:
                limite_inferior = int(input("Introduce el limite inferior "))
                limite_superior = int(input("Introduce el limite superior "))
                if limite_inferior >= limite_superior:
                    print("El límite inferior debe ser menor que el límite superior.")
            
    case "d":
        print("Saliendo...")
        sys.exit()
    
    
