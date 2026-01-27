""" 25.	Leer tres valores por pantalla, determinar e imprimir el mayor, el medio y el menor """

x = int(input("Ingresar numero uno "))
y = int(input("Ingresar numero dos "))
z = int(input("Ingresar numero tres "))

def ordenar(x, y, z):
    if x > y:
        if x > z:
            mayor = x
            if y > z:
                medio = y
                menor = z
            else:
                medio = z
                menor = y
        else:
            mayor = z
            medio = x
            menor = y
    else:
        if y > z:
            mayor = y
            if x > z:
                medio = x
                menor = z
            else:
                medio = z
                menor = x
        else:
            mayor = z
            medio = y
            menor = x
    
    print(f"MAYOR: {mayor}")
    print(f"MEDio: {medio}")
    print(f"menor: {menor}")

ordenar(x,y,z)

  