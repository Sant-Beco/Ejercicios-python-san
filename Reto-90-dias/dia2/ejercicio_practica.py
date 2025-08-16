# import sys

# edad = int(input("Ingresa tu edad: "))

# if edad < 18:
#     print(f"Tienes {edad} eres menor de edad")
# elif edad == 18:
#     print(f"Tienes {edad} justo 18 años tienes")
# elif edad > 18:
#     print(f"Tienes {edad} eres MAYOR de edad")
# else:
#     print("Error vuelve a ejecutar")    


# if __name__ == "__main__":
#     if len(sys.argv) >= 2:
#         edad(sys.argv[1], sys.argv[2], sys.argv[3])
#     else:
#         edad()

import sys

nombre = input("Escribe tu nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Menor de edad")
elif edad == 18:
    print("tienes 18")
elif edad > 18:
    print("eres mayor de edad")

for numero in range(1,edad):
    print(numero)