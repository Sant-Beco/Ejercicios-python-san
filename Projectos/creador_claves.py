import string
import random

print("\n//** Programa con el que puedes crear una contraseña **//\n")
longitud = int(input("Ingrese el tamaño de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

clave = "".join(random.choice(caracteres) for i in range(longitud))

print("\nLa contraseña generada es: " + clave)
print("\n")