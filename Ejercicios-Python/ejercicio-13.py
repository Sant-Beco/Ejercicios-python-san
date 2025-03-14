"""
13.	Realice un algoritmo que, con base en un número proporcionado (1-7), indique el día de la semana que le corresponde (L-D).
"""

numero = int(input("Ingrese un numero del 1-7 para determinar dia de la semana: "))

def nota(numero):
  if numero == 1:
    print("Hoy es Lunes")
  elif numero == 2:
    print("Hoy es Martes")
  elif numero == 3:
    print("Hoy es Miercoles")
  elif numero == 4:
    print("Hoy es Jueves")
  elif numero == 5:
    print("Hoy es Viernes")
  elif numero == 6:
    print("Hoy es Sabado")
  elif numero == 7:
    print("Hoy es Domingo")
  else:
    print("Valor no valido :( ese dia no existe")
  
nota(numero)



