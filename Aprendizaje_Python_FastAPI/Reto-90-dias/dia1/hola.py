import sys

def saludar(nombres="mundo"):
    print(f"!Hola, {nombres}¡")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        saludar(sys.argv[1])
    else:
        saludar()