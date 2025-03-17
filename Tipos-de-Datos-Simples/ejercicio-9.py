
"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión."""

capital = float(input("Ingrese su capital inicial a invertir: "))
interes_anual = float(input('Ingrese el interes anual: '))
num_anos = int(input("cantidad de años: "))

capital_final = (round(capital*(interes_anual / 100 +1)**num_anos, 2))

print(f'Su capital final da un total de {capital_final}') 