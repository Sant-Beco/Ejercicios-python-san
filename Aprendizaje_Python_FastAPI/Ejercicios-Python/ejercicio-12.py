"""
12.	Realice un algoritmo que, con base en una calificación proporcionada (0-10), indique con letra la calificación que le corresponde: 10 es “A”, 9 es “B”, 8 es “C”, 7 y 6 son “D”, y de 5 a 0 son “F”. 
"""

calificacion = int(input("Ingrese su calificacion: "))

def nota(calificacion):
  if calificacion == 10:
    print("Su calificacion es A")
  elif calificacion == 9:
    print("Su calificacion es B")
  elif calificacion == 8:
    print("Su calificacion es C")
  elif calificacion == 7 or calificacion == 6:
    print("Su calificacion es D")
  elif calificacion <= 5 and calificacion >= 0:
    print("Su calificacion es F")
  else:
    print("Valor no valido :(")
    
nota(calificacion)