"""Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde."""

horas = int(input("Ingrese sus horas trabajadas: "))
coste = int(input("Ingrese el costo por hora: "))

print(f"Su paga es de: {horas * coste}")