"""Escribir un programa que lea un entero positivo, n, introducido por el usuario y despues muestre
en pantalla la suma de todos los enteros desde uno a hasta n. la suma de los n primero enteros positivos puede ser calculada de la siguiente forma: """

n = int(input("Ingrese un numero: "))

suma = n *(n+1)/2
print(f"Suma de enteros: {suma}")