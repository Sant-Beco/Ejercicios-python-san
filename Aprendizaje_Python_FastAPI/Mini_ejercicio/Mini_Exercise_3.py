"""🧠 Mini reto (en inglés):
¿Quieres practicar un poco más con condicionales?"""

# age = int(input("\nIngrese su edad: "))

# if age >= 18:
#     print("You are an adult\n")
# else:
#     print("You are a minor\n")


# version dos


print("\n📋 Choose what you want to enter:")
print("1. Age")
print("2. Height")
print("3. Name")

option = ""

while option != 4:
    print("\n📋 Choose what you want to enter:")
    print("1. Age")
    print("2. Height")
    print("3. Name")
    print("4. Exit")
    
    option = input("Enter option (1-4): ")

    if option == "1":
        age = int(input("Enter your age: "))
        print(f"You are {age} years old.")

    elif option == "2":
        height = float(input("Enter your height in meters: "))
        print(f"Your height is {height} meters.")

    elif option == "3":
        name = input("Enter your name: ")
        print(f"Hello, {name}!")

    elif option == "4":
        print("Goodbye! see you soon")
        break

    else:
        print("❌ Invalid option. Please enter 1, 2, or 3.")

    print()