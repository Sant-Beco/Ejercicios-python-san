while True:
    numero = int(input("Ingrese un numero (0 para salir): "))
    if numero == 0:
        print("Fin del programa")
        break
    elif numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")