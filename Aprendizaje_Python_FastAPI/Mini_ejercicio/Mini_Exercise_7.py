"""🧪 Mini Exercise 7: 🏫 Grade Evaluator
🎯 Goal:
Ask the user for their test score and tell them what grade they got."""

score = int(input('Enter your test score: '))

if 90 <= score <= 100:
    print(f'\nExcellent work! 🏆 You got a A.')

elif 80 <= score <= 89:
    print(f'\nGreat job! 👏 You got a B')

elif 70 <= score <= 79:
    print(f'\nGood effort! 👍 You got a C')

elif 60 <= score <= 69:
    print(f'\nYou passed, but study more. You got a D')

elif score < 60:
    print(f'\nYou failed. Try again 💪 You got a E')

else:
    print('❌ Invalid score.')