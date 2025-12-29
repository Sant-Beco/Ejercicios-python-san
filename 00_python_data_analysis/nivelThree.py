visitas = 500
ventas = 125

print(f"{ventas / visitas * 100}%")

# 3. Mini reto

# Un video en TikTok tuvo:

# 20,000 vistas

# 4000 likes

# ¿Cuál es el porcentaje de likes?


likes = 4000
visitas_video = 20000

print(f"{likes / visitas_video * 100}%")

# leccion 2

#ejemplo 

anterior = 800
nuevo = 1000

variacion = (nuevo - anterior) / anterior * 100
print(f"La variación porcentual es {variacion:.2f}%")


# 📝 4. Ejercicio guiado (mañana lo haces tú)

# En un módulo, el pH promedio cambió:

# Semana pasada: 4.6

# Esta semana: 5.1

esta_semana = 5.1
semana_pasada = 4.6



print(f"El promedio es {(esta_semana -semana_pasada)  / semana_pasada * 100}%")

# 🔥 Mini reto opcional (rápido)

# Un video tenía 10,000 vistas
# Ahora tiene 13,500

visitas_tenia = 10000
tiene = 13500

print(f"{(tiene - visitas_tenia) / visitas_tenia * 100}%")


nombre_granja = input("Ingrese nombre de la granja: ")
cantidad_huevos = int(input("Ingrese cantidad de huevos: "))
temperatura = float(input("Ingrese el promedio de temperatura: "))
llovio = True

print(f"Hoy en la granja {nombre_granja} se produjeron {cantidad_huevos} huevos, "
      f"con una temperatura promedio de {temperatura}°C y la lluvia fue {llovio}.")
