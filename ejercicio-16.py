"""
16.	Realice un algoritmo que permita determinar la cantidad del bono navideño que recibirá un empleado de una tienda, considerando que si su antigüedad es mayor a cuatro años o su sueldo es menor de dos mil pesos, le corresponderá 25 % de su sueldo, y en caso contrario sólo le corresponderá 20 % de éste.
"""

tiempo = int(input("Ingrese el antiguedad que lleva trabajando en la tienda en años "))
sueldo = int(input("Digita tu salario actual "))

def bonoNavidad(tiempo, sueldo):
  if tiempo > 4 or sueldo < 2000:
    print(f"recibira un bono de 25% que es {sueldo*(25/100)}")
  elif tiempo < 4 or sueldo > 2000:
    print(f"recibira un bono de 20% que es {sueldo*(20/100)}")
  else:
    print("Valor ingresado es incorrecto")
    
bonoNavidad(tiempo, sueldo)