"""Escribe un programa que solicite un número entero y muestre exactamente
 una de estas respuestas:

text
Positivo
Negativo
Cero"""

numero = int(input("Ingrese un numero: "))

if numero < 0: 
    print("Negativo")
elif numero > 0:
    print("Positivo")
elif numero == 0:
    print("Cero")
