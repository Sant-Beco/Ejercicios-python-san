"""🎯 Goal:
Create a program that asks the user's age and tells them what kind of movie they can watch."""

age = int(input("Ingrese su edad: "))

if age < 0:
    print("❌ Invalid age. Please try again.") 

elif age <= 12:
    print("You can watch cartoons 🎨")

elif 17 <= age >= 13:
    print("You can watch teen movies 🍿")

elif age >= 18:
    print("You can watch all movies 🎥")
