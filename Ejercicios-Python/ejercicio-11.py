"""
los alumnos de una escuela desean realizar un viaje de estudios, pero requieren determinar cuanto les costara el pasaje, 
considerando que las tarifasd el autobus son las siguientes: si son mas de 100 alumnos, el costo es de $20; si son 50 y 
100 $35; entre 20 y 49 $40, y si son menos de 20 alumnos, $70 por cada uno. Realice el algoritmo para determinar el costo 
del pasaje de cada alumno. 

"""

cantidadAlumnos = int(input("Ingrese la cantidad de alumnos que van: "))

def valorAlumno(cantidadAlumnos):
  if cantidadAlumnos >= 100:
    print("Costo de pasaje es de $20 por persona")
  elif cantidadAlumnos < 100 and cantidadAlumnos >= 50:
    print("Costo de pasaje es de $35 por persona")
  elif cantidadAlumnos < 49 and cantidadAlumnos >= 20:
    print("Costo de pasaje es de $40 por persona")
  elif cantidadAlumnos < 20:
    print("Costo de pasaje es de $70 por persona")
  else:
    print("Tu dato introducido es incorrecto")
  
valorAlumno(cantidadAlumnos)