cadena = "informatica"

#Hacer la cadena enterea mayuscula .lower() es para minuscula
print(cadena.upper())

print("Imprimir numero exacto de la cadena " ,cadena[2])

for letra in cadena:
    print(letra)

cad = "hola, como estas?"
#Hacer mayuscula la primera letra
cad.capitalize

print(cad.capitalize())

#Esto hace que se ponga en mayuscula la primera letra de cada palabra
cad = "hola mundo"
cad.title()
print(cad.title())

#Contar las letras que hay en la cadena
print("Contar las letras que hay en la cadena")
cad = "hola mundo"
cad = "Bienvenido a mi aplicacion"
print(cad.count("a"))
print(cad.count("a",10))
print(cad.count("a",0,13))
print(cad.find("hola"))

print(cad.startswith("B"))

print(cad.replace("a","e"))

hora = "12:23:12"
print(hora.split(":"))

texto = "Linea1\nLinea2\nLinea3"
print(texto)