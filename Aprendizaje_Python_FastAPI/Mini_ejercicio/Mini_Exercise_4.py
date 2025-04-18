"""🧪 Mini Exercise 6: Club Entry Checker 🎟️
🎯 Goal:
Check if the user can enter the VIP club."""

age = int(input("Enter your age: "))
is_vip_input = input("Are you a VIP? (yes/no): ").lower()

if is_vip_input == "yes" and age >= 18:
    print("Welcome to the VIP club 🕺")

elif is_vip_input == "no" and age >= 18:
    print("You need a VIP pass to enter 🚫")

elif age < 18:
    print("You must be at least 18 years old 🚷")

else:
    print("❌ Invalid age. Please try again.")


