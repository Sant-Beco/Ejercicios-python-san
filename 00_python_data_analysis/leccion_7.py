"""Preguntas que un sistema serio debe responder:
¿Cuántos días están por debajo del mínimo aceptable?
¿Qué tan lejos está el peor día del promedio?
¿Hay picos que indiquen descontrol?

🎯 Problema a resolver

Diseña una función que reciba:

una lista de producción diaria
un valor mínimo aceptable (ej: 80)

Define reglas con palabras primero:

si hay un valor muy extremo eje el promedio es 81 pero hay un dia de 75 o por el contrario
de 87 es algo poco probable esto es una alerta: Sucede descontrol en produccion

y si hay varios dias por debajo del promedio cuantos dias, si es uno de 7 aceptable, pero
si son varios y mas de 4 puntos dar la lista de estos y revision minisiosa porque la 
produccion esta bajando y mucho

si la produccion es igual o mayor a la produccion normal estamos bien

si la produccion es mayor a la produccion normal 2 puntos o hasta 3 estamos llegando a pico"""



