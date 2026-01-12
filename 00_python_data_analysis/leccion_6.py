"""🔥 LECCIÓN 6 – FUNCIONES QUE ANALIZAN DATOS Y GENERAN CRITERIOS

necesito saber la produccion maxima, el promedio, produccion 

¿qué es más peligroso: promedio bajo o mucha variación?

promedio bajo, porque si la variacion es superior al promedio minimo aceptable esta bien

¿La producción fue constante o muy variable?

¿El promedio cumple el mínimo esperado?

¿Hubo días críticos?
"""



def control_produccion(produccion_diaria):
    produccion_minima_aceptable = 80
    produccion_promedio = sum(produccion_diaria) / len(produccion_diaria)
    if produccion_minima_aceptable >= produccion_promedio:
        produccion_minima_semana = min(produccion_diaria)
        return f"Alerta, la produccion mas critica {produccion_minima_semana}"
    elif produccion_minima_aceptable <= produccion_promedio:
        return "Produccion constante"
    else:
        return "Ingresaste un dato no valido, una lista"
    

print(control_produccion([82, 85, 83, 84, 81, 83, 82]))
print(control_produccion([82, 45, 83, 35, 81, 83, 82]))
print(control_produccion([82, 85, 83, 84, 81, 83, 82]))
print(control_produccion([56, 78, 83, 84, 76, 83, 82,]))