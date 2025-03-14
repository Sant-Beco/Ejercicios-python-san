"""     20.	Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. ¿Cuál es su salario 

al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años? Realice el algoritmo.    """

# meta con funcion lo mas optimo posible

# version uno 

# salario = 1500
# incremento = 10

# salarioPrimer = salario *(incremento/100) + salario
# print(salarioPrimer)

# salarioSegundo = salarioPrimer *(incremento/100) + salarioPrimer
# print(salarioSegundo)

# salarioTercer = salarioSegundo *(incremento/100) + salarioSegundo
# print(salarioTercer)

# salarioCuarto = salarioTercer *(incremento/100) + salarioTercer
# print(salarioCuarto)

# salarioQuinto = salarioCuarto *(incremento/100) + salarioCuarto
# print(salarioQuinto)

# salarioSexto = salarioQuinto *(incremento/100) + salarioQuinto
# print(salarioSexto)

# Version 2

print("\nEjercicio 20\n")

salario = 1500
incremento = 10

def cacularSalario(salario,incremento):
  salarioPrimer = salario *(incremento/100) + salario
  print(f"El primer año el salario con el incremento del 10% del profesor es de {salarioPrimer}")

  salarioSegundo = salarioPrimer *(incremento/100) + salarioPrimer
  print(f"El segundo año el salario con el incremento del 10% del profesor es de {salarioSegundo}")

  salarioTercer = salarioSegundo *(incremento/100) + salarioSegundo
  print(f"El tercer año el salario con el incremento del 10% del profesor es de {salarioTercer}")

  salarioCuarto = salarioTercer *(incremento/100) + salarioTercer
  print(f"El cuarto año el salario con el incremento del 10% del profesor es de {salarioCuarto}")

  salarioQuinto = salarioCuarto *(incremento/100) + salarioCuarto
  print(f"El quinto año es de salario con el incremento del 10% del profesor es de {salarioQuinto}")

  salarioSexto = salarioQuinto *(incremento/100) + salarioQuinto
  print(f"El sexto es de salario con el incremento del 10% del profesor es de {salarioSexto}")


cacularSalario(salario,incremento)


