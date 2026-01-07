"""
¿Cuál fue el promedio semanal?

normalmente por encima de guia, ejemplo 82% en pico de produccion 

¿Cuál fue el máximo?

el maximo fue 84%

¿Hoy está por encima, igual o debajo?

hoy fue 83%

¿La temperatura invalida un buen número?

Depende si sube o baja mucho, al otro dia puede tener repercusiones, pero si ha buena temperatura hay buena 
produccion.
"""

"""✍️ Anota en tu cuaderno

Qué significa “mejor que la semana”

mas arriba del promedio de la semana y mas exacto superior a la guia

Qué significa “normal”

que esta en el promedio de la semana, o igual a la guia o un poco superios

Cuándo una temperatura anula un buen resultado

cuando al dia siguiente el promedio baja por causa de la temperatura"""

produccion_semana = [82, 85, 83, 84, 81, 83, 82]

produccion = 83
temperatura = 24

promedio_semanal = sum(produccion_semana) / len(produccion_semana)
promedio_maximo =  max(promedio_semanal)

def estado_granja(produccion_semana, produccion, temperatura):
    promedio_semanal = sum(produccion_semana) / len(produccion_semana)
    return promedio_semanal
    promedio_maximo =  max(produccion_semana)
    return promedio_maximo
    