"""
14.	El secretario de educación ha decidido otorgar un bono por desempeño a todos los profesores con base en la puntuación siguiente:

Puntos	Premio
0 - 100 - 	1	salario
101 - 150 - 2	salarios mínimos
151 - en adelante - 3	salarios mínimos

Realice un algoritmo que permita determine el monto de bono que recibirá un profesor (debe capturar el valor del salario mínimo y los puntos del profesor).
"""

salarioMinimo = int(input("Ingrese su salario minimo "))
puntos = int(input("Digite su puntaje "))

def bonoProfesores(salarioMinimo, puntos):
  if puntos > 0 and puntos < 100:
    print(f"El profesor recibe 1 salario que es igual a: {salarioMinimo}")
  elif puntos > 101 and puntos < 150:
    print(f"El profesor recibe 2 salario que es igual a: {salarioMinimo * 2}")
  elif puntos > 151:
    print(f"El profesor recibe 3 salario que es igual a: {salarioMinimo * 3}")
  else:
    print("Tus valores ingresados no son validos")
  
bonoProfesores(salarioMinimo, puntos)