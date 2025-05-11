"""🧪 Mini Exercise 14: 🛒 Grocery Shopping List
🎯 Objetivo:
Crear un programa que permita al usuario crear una lista de compras, agregando elementos uno por uno, y luego mostrar el total de elementos y los productos.

📋 Instrucciones:
Pregunta al usuario cuántos productos desea agregar.

Usa un try/except para validar que el número ingresado sea un entero positivo.

Pide al usuario que escriba cada producto uno por uno.

Guarda los productos en una lista.

Al final, imprime:

La lista completa.

Cuántos productos hay en total.

Un mensaje de despedida.

🧾 Ejemplo de salida:
pgsql
Copiar
Editar
🛒 Welcome to the Grocery List Manager!
How many products do you want to add? 3

Enter product 1: Milk
Enter product 2: Eggs
Enter product 3: Bread

✅ Your grocery list: ['Milk', 'Eggs', 'Bread']
You have 3 products in total.
Happy shopping! 🛍️"""

print("\n📋 Choose what you want to enter\n")

cant_productos = int(input("Ingrese la cantidad de productos: "))
option = ""

while cant_productos > 0:
    print("\n📋 Choose what you want to enter:")