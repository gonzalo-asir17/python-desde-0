#!/usr/bin/python3
#Hecho por Gonzalo Rodriguez Martin 04/12/2023
#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas
#por un alumnas . A continuacion debe mostran todas las notas y la media
#las nota mas alta que ha sacado y la menor

notas = []
for indice in range(1,6):
    while True:
        nota = float(input("Introduce la nota %d: " % indice))
        if nota >= 0 and nota <= 10: break
    notas.append(nota)

#Mostrar resultados
print("Notas: ", end="")
for nota in notas:
    print(nota, " ",end="")
print()
print("Nota media: ", round(sum(notas)/len(notas), 2))
print("Nota maxima: ", max(notas))
print("Ntoa minima: ", min(notas))