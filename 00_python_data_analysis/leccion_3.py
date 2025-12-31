# Funciones



def evaluar_calidad_huevo (peso_promedio, porcentaje_defectos):
    if peso_promedio > 60 and porcentaje_defectos < 5:
        print(f"Calidad Alta")
    elif 55 > peso_promedio < 60:
        print(f"Calidad Media")
    elif peso_promedio < 55 or porcentaje_defectos > 10:
        print(f"Calidad Baja")
    else:
        print("ups algo salio mal")


resultado = evaluar_calidad_huevo(64, 4)
resultado = evaluar_calidad_huevo(54, 11)
print(resultado)