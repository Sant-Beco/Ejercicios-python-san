# variables 

estado = True
placa = "Gzd15h"
modelo = 2021
marca = "Yamaha"

inspecciones = {
    "estado": True,
    "placa": "GZD15H",
    "marca": "Yamaha",
    "proceso": "Traslado",
    "motor": 110
}

print(inspecciones)

aspectos = ["Luces", "llantas", "Espejos retrovisores", "aceite", "tablero"]

print(aspectos)

# ejemplo cloro

cloro = 3
ph = 4.6

control_agua = {
    
    "lugar": "modulo 100",
    "cloro": 1.5,
    "ph": 5
}

print(control_agua)

# Listas

enero_control_agua = ["4.4", "4.7", "4.9"]

print(enero_control_agua)

# funciones

nombre = (input("ingrese su nombre: "))
dia = (input("ingrese la fecha actual: "))

def saludar(nombre, dia):
    print(f"Hola {nombre} hoy es {dia}")
    return nombre, dia

saludar(nombre, dia)
saludar("isa", "12-11-2025")

# imports

# from fastapi import fastAPI
# from app.database import SessionLocal
# from app.models import Inspeccion

# Condicionales if, elif o else

ph =  7
cloro = 5

if ph < 5.6 and ph > 4 and cloro > 2 and cloro < 4:
    print(f"El ph es {ph} y el cloro es {cloro} esta aceptable")
elif ph > 6 and cloro > 4:
    print(f"El ph es {ph} y el cloro es {cloro} esta alto hay que revisarlo")
else:
    print("Algo salio mal")

# ejercicio 

cloro = 1.2

if cloro < 0.5:
    print(f"Cloro muy bajo {cloro}")
elif cloro < 2.0 and cloro > 0.5:
    print(f"Cloro dentro del rango {cloro}")
elif cloro < 0.5:
    print(f"Cloro muy alto {cloro}")

# Bucle

valores_ph = [4.8, 5.2, 4.7, 3.6, 5.6, 4.9, 4.2, 4.4]

for valor in valores_ph:
    print(f"El ph registrado en el modulo de los 600 fue: {valor}")

contador = 1

while contador <= 6:
    print(f"Dia: {contador}")
    contador += 1

lecturas_cloro = [1.1, 0.8, 1.4, 1.9]

for i in lecturas_cloro and range(6):
    contador = 1
    print(f"Dia {i}: {lecturas_cloro}")
    contador += 1

# clases

class granja:
    def __init__(self, cloro, ph):
        self.cloro = cloro
        self.ph = ph

m1 = granja("La esperanza", 2025)

print(m1.cloro)

class controlAgua:
    def __init__(self, lugar, ph, cloro):
        self.lugar = lugar
        self.ph = ph 
        self.cloro = cloro 

m2 = controlAgua("Esperanza", 5.2, 3.0)

print(m2.ph)

registro = controlAgua("modulo 200", 4.2, 2.5)

print(registro.ph)

# archivos

with open("ph.txt", "w") as f:
    f.write("ph 5.2\n")

with open("ph.txt", "w") as f:
    contenido = f.read()
    print(contenido)

with open("ph.txt", "w") as f:
    contenido = f.write()
    print(contenido)


# ejercicio 4

lecturas = [5.2, 5.3, 5.6]

for i in lecturas:
    with open("ph.txt", "w") as f:
    i = f.write()
    print(i)