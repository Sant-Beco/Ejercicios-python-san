"""🧪 Mini Exercise 6: Club Entry Checker 🎟️
🎯 Goal:
Check if the user can enter the VIP club."""

age = int(input("Ingrese su edad: "))
is_vip_input = input("Eres VIP (yes/no): ").lower()
is_vip = is_vip_input == "yes"



print(f"\nVIP:{'Yes' if is_vip else 'No'}\n")