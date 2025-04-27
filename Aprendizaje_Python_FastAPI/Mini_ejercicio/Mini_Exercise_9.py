"""🧪 Mini Exercise 9: 🎒 My Backpack List
🎯 Goal:
Create a program that allows the user to build a backpack list by adding items one by one.

📋 Instructions:
Create an empty list called backpack.

Ask the user how many items they want to add.

Use a loop to ask for each item name and add it to the list.

After all items are added, print the full list.

🧾 Example Output:
🎒 Welcome to Backpack Manager
How many items do you want to add? 3

Enter item 1: Notebook
Enter item 2: Water bottle
Enter item 3: Jacket

✅ Items in your backpack:
['Notebook', 'Water bottle', 'Jacket']"""


print("\n🎒 Welcome to Backpack Manager\n")

try:
    cantidad_elem = int(input("How many items do you want to add? "))
    if cantidad_elem <= 0:
        print("⚠️ Please enter a positive number.")
        
    else:
        counter = 1
        lista = []

        while counter <= cantidad_elem:     
            item = input(f"Enter item {counter}: ")
            lista.append(item)
            counter += 1
        print("\n✅ Items in your backpack:")
        print(lista)


except ValueError:
    print("❌ Invalid input. Please enter a number.")