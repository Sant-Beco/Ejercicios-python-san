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

