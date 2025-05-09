"""🧪 Mini Ejercicio: Calculadora Segura
🎯 Objetivo:
Crear una función que sume dos números, manejando errores si el usuario escribe mal los datos."""


print("🎯 Calculadora")

try:
    num_one = int(input('Ingrese un numero: '))
    num_two = int(input('Ingrese un numero: '))
    suma = num_one + num_two

    print(f"\nSuma uno = {suma}")
    print(f"\nSuma = {num_one + num_two}")
    print(f"\nResta = {num_one - num_two}")
    print(f"\nMultiplicacion = {num_one * num_two}")
    print(f"\nDivicion = {num_one / num_two}")
    print(f"\nModulo = {num_one // num_two}")

except:
    print("❌ Please enter a valid integer.")





