"""🐍 Día 3: Calculadora simple

👉 Haz un programa que:

Pida dos números al usuario.

Pregunte qué operación quiere hacer (suma, resta, multiplicación, división).

Use un if / elif para realizar la operación.

Permita repetir el proceso hasta que el usuario escriba "salir"."""

while True:
    print("Bienvenido a tu calculadora")
    num1 = input("Ingrese su primer numero o SALIR: ")
    if num1.lower() == "salir":
        print("Vuelve pronto  👋")
        break
    num2 = input("Ingrese otro numero")
    operacion = input("¿Qué operación quieres? (suma, resta, multiplicacion, division): ")

    num1 = float(num1)
    num2 = float(num2)

    if operacion == "suma":
        print(f"El total es: {num1 + num2}")
    elif operacion == "resta":
        print(f"El total es: {num1 - num2}")
    elif operacion == "multiplicar":
        print(f"El total es: {num1 * num2}")
    elif operacion == "divicion":
        print(f"El total es: {num1 / num2}")