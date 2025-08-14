edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print(f"Tienes {edad} eres menor de edad")
elif edad == 18:
    print(f"Tienes {edad} justo 18 años tienes")
elif edad > 18:
    print(f"Tienes {edad} eres MAYOR de edad")
else:
    print("Error vuelve a ejecutar")    