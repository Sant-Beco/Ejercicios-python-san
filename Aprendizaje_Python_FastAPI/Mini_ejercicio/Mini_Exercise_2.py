"""🧪 Mini ejercicio 2: ¡Ficha Personal!
🎯 Objetivo:
Crear un programa que pida al usuario su nombre, edad, estatura en metros y si es estudiante, y luego imprima una ficha con esa información."""

name = input("\nIngrese su nombre: ")
age = int(input("Ingrese su edad: "))
height = float(input("Ingrese su altura: "))
is_student_input = input("Eres estudiante (yes/no): ").lower()
is_student = is_student_input == "yes"

print(f"\n🧾 Personal Info Card: \nName:{name}\nAge:{age}\nHeight:{height}\nStudent:{'Yes' if is_student else 'No'}\n")