"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule indice de masa corporal y lo almacene en una variable y muestre por pantalla  la frase: Tu indice de masa corporal es <imc> donde <imc> el indice corporal calculado redondeado con dos decimales"""

peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altuara en metros: "))

imc = round(peso / altura ** 2, 2)

print(f"Tu indice de masa corporal es <imc>: {imc}")