# Ejercicio 

print("\nleccion 2")
nombre_granja = "Esperanza"
produce_huevos = 3200
temperatura = 25

if temperatura > 30:
    print(f"La temperatura esta muy alta {temperatura}% no es normal!")
    estado = "alerta"

elif produce_huevos < 2000: 
    print(f"produccion baja {produce_huevos}")
    estado = "alerta"
elif produce_huevos > 2500:
     print(f"produccion alta {produce_huevos} Super :)")
     estado = "normal"

print("\n")
print(f"Granja: {nombre_granja}")
print(f"produccion: {produce_huevos} huevos")
print(f"Estado: {estado}")
print("\n")