# Funciones



def evaluar_calidad_huevo (peso_promedio, porcentaje_defectos):
    if peso_promedio > 60 and porcentaje_defectos < 5:
        return "Calidad Alta"
    elif 55 <= peso_promedio <= 60:
        return "Calidad Media"
    elif peso_promedio < 55 or porcentaje_defectos > 10:
        return f"Calidad Baja"
    else:
        return "ups datos inconsientes"


resultado = evaluar_calidad_huevo(64, 4)
print(resultado)

resultado = evaluar_calidad_huevo(54, 11)
print(resultado)

# 🧪 MINI RETO FINAL (MUY IMPORTANTE)

# Crea una función:

# def evaluar_produccion(huevos, temperatura):


# Reglas:

# Si huevos > 3000 y temperatura < 30 → "Excelente"

# Si huevos entre 2000 y 3000 → "Aceptable"

# Si huevos < 2000 o temperatura > 32 → "Crítica"

def evaluar_produccion(huevos, temperatura):
    if huevos >= 3000 and temperatura <= 30:
        return "Excelente"
    elif 2000 <= huevos <= 3000:
        return "Aceptable"
    elif huevos <= 2000 and temperatura >= 30:
        return "Critica"
    
igual = evaluar_produccion(3200, 24)
print(igual)

igual = evaluar_produccion(2600, 24)
print(igual)

igual = evaluar_produccion(3000, 30)
print(igual)