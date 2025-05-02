"""🧪 Mini Exercise 11: Multiplication Table
🎯 Goal:
Create a program that asks the user for a number and prints its multiplication table up to 10."""


try:
    number = int(input("Enter into number integer: "))

    print(f"\n📊 Multiplication Table of {number}:\n")

    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

except:
    print("❌ Please enter a valid integer.")