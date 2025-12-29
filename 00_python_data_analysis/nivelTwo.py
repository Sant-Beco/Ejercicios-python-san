# Condicionels if, elif and else

# Define reglas para cloro:

cloro = float(input("Ingrese puntuacion de cloro: "))

if cloro >= 4.1:
    print(f"El cloro esta Muy alto {cloro}")

elif 3.1 <= cloro <= 4:
    print(f"El cloro esta Alto {cloro}")

elif 2.2 <= cloro <= 3:
    print(f"Cloro Normal")


elif 1 <= cloro <= 2.1:
    print(f"Cloro Bajo\n Hecha cloro")

elif 0.9 > cloro:
    print(f"Cloro Muy Bajo\n Hecha cloro")

else: 
    print("Vuelve a intentarlo")

# for

lectura_cl = [2.3, 1.2, 5.6, 7.6, 1.2, 3.4, 2.3]

for i, valor in enumerate(lectura_cl, start=1):
    print(f"Dia {i}: {valor}")

print("\nFor ph")

# Ejercicio for

ph_mes = [4.8, 4.9, 5.0, 4.7, 4.3, 5.5]

for i, val in enumerate(ph_mes, start=1):
    print(f"Dia {i}: {val}")


# Escritura y lectura de archivos