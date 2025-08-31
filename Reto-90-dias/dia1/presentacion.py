def saludar(nombres="San",edad="20",ciudad="Itagui"):
    print(f"!Hola, me llamo {nombres}, tengo {edad} años y vivo en {ciudad}¡")

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        saludar(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        saludar()