"""  #10   Realice un algoritmo que permita determinar el sueldo semanal de un trabajador con base en las horas trabajadas y el pago por hora, considerando que a 
partir de la hora 41 y hasta la 45, cada hora se le paga el doble, de la hora 46, el triple, y que trabajar de 50 horas no esta permitido   """

horasTrabajadas = int(input("Ingrese sus horas trabajadas esta semana: "))
pagoHora = int(input("Ingrese cuanto de pagan por hora: "))

if horasTrabajadas >= 0 and horasTrabajadas <= 40:
  sueldoSemanal = horasTrabajadas * pagoHora
  print(sueldoSemanal)
elif horasTrabajadas >= 41 and horasTrabajadas <= 45:
  sueldoSemanal = horasTrabajadas * pagoHora * 2
  print(sueldoSemanal)
elif horasTrabajadas >= 46 and horasTrabajadas <= 49:
  sueldoSemanal = horasTrabajadas * pagoHora * 3
  print(sueldoSemanal)
elif horasTrabajadas >= 50:
  print("No esta permitido trabajar mas de 50 horas")
else:
  print("los numeros negativos no funcionan el valor es incorrecto")
