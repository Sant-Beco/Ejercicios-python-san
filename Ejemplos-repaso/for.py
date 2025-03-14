# Ejemplo 1 Iterar sobre una lista

print("\n")
frutas = ["Peras", "Uvas", "fresas", "Cereza"]

for i in frutas:
    print(i)

# Ejemplo 2 Iterar sobre una cadena

print("\n")
for letra in "Python":
    print(letra)

# Ejemplo 3: Usar range() para iterar un número específico de veces

print("\n")
for i in range(9):
    print(i)

#Ejemplo 4: Iterar sobre un diccionario

persona = {"nombre": "Santiago", "edad": 20, "Ciudad": "Itagui", "estado": "Exelente"}

print("\n")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Ejemplo 5: Usar else con un bucle for

print("\n")
for i in range(5):
    print(i)
else:
    print("Buque terminado")

# Ejemplo 6: Uso de break y continue

print("\n")
for i in range(9):
    if i == 5:
        break
    print(i)


print("\n")
for i in range(8):
    if i == 5:
        continue
    print(i)

# Ejemplo 7: Iterar sobre una lista con índice

frutas = ["manzana", "banana", "cereza", "durazno", "guavana"]

print("\n")
for indice, fruta in enumerate(frutas):
    print(f"indice {indice}, frutas: {fruta}")
print("\n")