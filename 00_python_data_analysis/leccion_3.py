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
