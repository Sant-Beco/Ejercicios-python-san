"""Problema 2 de 20
Escribe un programa que solicite un entero y muestre exactamente una de estas respuestas:

text
Par
Impar"""

numero = int(input("Ingrese un numero: "))

modulo = numero % 2 

if numero == 0:
    print("par")
else:
    print("inpar")


# falta agregar la logica necesaria para que el numero sea dividido hasta que de 0 o residuo no me cuerdo bien como funciona %