# break, continue, pass

print("\nBreak")
for i in range(1, 10):
    if i == 7:
        break  # Se detiene cuando i es 7
    print(i)

print("\nContinue")

for i in range(1, 6):
    if i == 3:
        continue  # Se salta el 3
    print(i)


for i in range(3):
    pass  # Aquí no hacemos nada todavía


# funciones y manejo de errores

def nombre_de_la_funcion():
    # cuerpo de la función
    print("Hola")


def saludar():
    print("¡Hola, bienvenido!")

saludar()


def sumar(a, b):  # 'a' y 'b' son argumentos
    return a + b  # devuelve la suma


resultado = sumar(3, 4)
print(resultado)  # Output: 7



try:
    numero = int(input("Ingresa un número: "))
    print("10 dividido entre tu número:", 10 / numero)

except ValueError:
    print("❌ Eso no es un número.")

except ZeroDivisionError:
    print("❌ No puedes dividir entre 0.")

finally:
    print("Gracias por intentar 🙏")