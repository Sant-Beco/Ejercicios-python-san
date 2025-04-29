"""🧪 Mini Exercise 10: Personal Info Dictionary
🎯 Goal:
Create a program that asks for your name, age, country, and favorite color.
Store this information in a dictionary and print it in a friendly message."""

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age old: "))
    country = input("Enter your country: ")
    favorite_color = input("Enter your favorite color: ")

    diccionario = {
        "name": name,
        "age": age,
        "country": country,
        "favorite_color": favorite_color
    }

    print(f"Your dates is {diccionario} happy day")

    print(f"\nHello {name}! 👋")
    print(f"You are {age} years old, live in {country}, and your favorite color is {favorite_color}. 🎨\n")
    print(f"\nremenber that save in dictionary {diccionario}\n")

except ValueError:
    print("❌ Age must be a number. Please try again.")