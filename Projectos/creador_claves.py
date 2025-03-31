import string
import random
import pyfiglet

texto = "CrearClave"
resultado = pyfiglet.figlet_format(texto)
print(resultado)


print("\n --- Generador de Contraseñas Seguras ---\n")

# validar entrada

while True:
    try:
        longitud = int(input("Ingrese el tamaño de la contraseña (minimo 8): "))
        if longitud < 8:
            print("⚠ La contraseña debe tener al menos 8 caracteres.")
            continue
        break
    except ValueError:
        print("❌ Error: Ingrese un número válido.")

caracteres = string.ascii_letters + string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation

clave = "".join(random.choice(caracteres) for i in range(longitud))

print("\n✅La contraseña generada es: " + clave)
print("\n")




