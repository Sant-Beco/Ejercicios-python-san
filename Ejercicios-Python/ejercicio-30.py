""" 30.	Una distribuidora de huevos quiere contratarlo a usted para que realice un algoritmo que calcule el precio de venta para una cantidad de huevos a llevar por un determinado cliente. Guiándose por la siguiente información:

Precio unitario Huevo	Descuento por cantidades a llevar
Tipo A	Tipo AA	1-100	101-200	201-300	>= a 301
220	250	3%	5%	8%	10%
 """
 
tipo_huevo = str(input("Ingresar tipo digite A o AA: "))
cantidad = int(input("Ingrese la cantidad de huevos: "))

if tipo_huevo == 'A':
  precio_uni = 220
elif tipo_huevo == 'AA':
  precio_uni = 250

if cantidad <= 100 and cantidad >= 1:
  descuento = 0.03
elif cantidad <= 200 and cantidad >= 101:
  descuento = 0.05
elif cantidad <= 300 and cantidad >= 201:
  descuento = 0.08
elif cantidad >= 301:
  descuento = 0.10  
  
precio_total = precio_uni * cantidad

descu_total = precio_total * descuento
  
total = precio_total - descu_total  
  
print(f"Tienes que pagar {total} en total")
