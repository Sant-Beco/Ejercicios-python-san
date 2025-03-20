"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa 
que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual 
de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total."""

barras_pan = int(input("Ingrese la cantidad de barras de pan: "))
precio = barras_pan * 3.49

print(f"precio habitual es de 3.49€ entonces sin descuento es {precio:.2f} pero con el 60% {precio * .060:.2f}")