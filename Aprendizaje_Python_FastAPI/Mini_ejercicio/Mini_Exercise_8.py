"""🧪 Mini Exercise 8: 🔢 Count with Loops
🎯 Goal:
Create a small menu that lets the user choose a loop type, then counts from 1 to 5 using the selected loop."""

print("Choose a loop:\n1. for loop\n2. while loop")

opcion_select = int(input("Enter option: "))



if opcion_select == 1:
    for i in range(1, 5):
        print(i)

elif opcion_select == 2:
    counter = 1
    while counter < 6:
        print(counter)
        counter += 1

else:
    print("Invalid option")