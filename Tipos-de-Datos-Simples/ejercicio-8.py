"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> 
donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente."""

numero_uno = int(input('Introduzca un numero entero: '))
numero_dos = int(input('Introduzca otro numero entero: '))

divicion = numero_uno // numero_dos
divi = numero_uno % numero_dos

print(f"El conciente {divicion} y el resto {divi}")