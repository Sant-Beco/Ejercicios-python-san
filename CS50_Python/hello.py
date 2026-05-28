#Ask user for their name

print("Hello, world")

# print("Hello, world"      Bug syntaxError

name = input("Enter your name: ")
print("Hello, " + name)
print("Hello, ", name)
print(f"Hello, {name} your welcome of course!")

# DEFINIR función
def calcular_total(precio, cantidad):
    # parámetros: precio, cantidad
    total = precio * cantidad
    return total  # devuelve el resultado

# LLAMAR función
resultado = calcular_total(10, 5)  # resultado = 50
print(f"Funcion de calcular precio {resultado}")

print(calcular_total(20,2))

