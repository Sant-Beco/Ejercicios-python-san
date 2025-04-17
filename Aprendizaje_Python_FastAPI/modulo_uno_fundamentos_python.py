nombre = "Sara"
edad = 10

# Ejemplo de variables y type data

Nombre = "Ana maria"
edad = 22
altura = 1.70
estudiante = True

print(Nombre, edad, altura, estudiante)

# example code - Data types

name = "San"             # str
age = 19                 # int
height = 1.83            # float
is_student = True        # bool
hobbies = ["code", "read", "guitar"]  # list
profile = {"name": "San", "age": 19}  # dict
coordinates = (10.5, 20.5)            # tuple
unique_numbers = {1, 2, 3, 3}         # set (duplicates removed)

print(name, age, height, is_student, hobbies, profile, coordinates, unique_numbers)

# if elif else 17 de marzo

age = int(input("Enter your age: "))

if age < 18:
    print("You're a minor.")
elif age == 18:
    print("You're exactly 18!")
else:
    print("You're an adult.")

#if condition:
    # Code if condition is True
#elif another_condition:
    # Code if another condition is True
#else:
    # Code if none of the above are True

has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the cinema 🎬")
else:
    print("Sorry, access denied 🚫")

# loops For and While

for i in range(8):
    print(f"Number: {i}")

