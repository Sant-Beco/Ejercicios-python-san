import string
import random
import pyfiglet

texto = "\n              *CrearClave*\n"
resultado = pyfiglet.figlet_format(texto)
print(resultado)


print("\n")
longitud = int(input("Ingrese el tamaño de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

clave = "".join(random.choice(caracteres) for i in range(longitud))

print("\nLa contraseña generada es: " + clave)
print("\n")




