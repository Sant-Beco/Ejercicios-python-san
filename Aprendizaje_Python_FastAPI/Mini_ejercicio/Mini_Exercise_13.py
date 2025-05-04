"""🧪 Mini Exercise 13: Favorite Things List
🎯 Goal:
Create a program that asks the user to enter their 3 favorite things (like food, hobbies, or colors), stores them in a list, and prints them in a sentence.

Example output:

Enter your first favorite thing: pizza
Enter your second favorite thing: music
Enter your third favorite thing: soccer

Your favorite things are: ['pizza', 'music', 'soccer']
You love pizza, music, and soccer!"""

thing_one = input('Enter your first favorite thing: ')
thing_two = input('Enter your second favorite thing:    ')
thing_three = input('Enter your third favorite thing:   ')

lista = []

lista.extend([thing_one, thing_two, thing_three])

print(f"\nYour favorite things are: {lista}")
print(f"You love {thing_one}, {thing_two}, and {thing_three}!")