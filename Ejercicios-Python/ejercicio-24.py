""" 24.	Se desea saber cuántos pinos y cuantos cedros se pueden sembrar en un terreno que mide n cantidad de metros. El dueño ha establecido que sembrará el 35% del terreno en pinos y el 65% en cedros. Las normas de agricultura establecen que en 10 metros cuadrados se pueden sembrar 4 pinos y en 15 metros cuadrados 5 cedros.  """


"""
pinos = 35% * 4 en 15 metros
cedros = 65% * 5 en 15 metros
"""

cantidad_terreno = int(input("Ingrese una cantidad de terreno en metros cuadrados: "))

def calcular(cantidad_terreno):
  
  pinos = .35 * cantidad_terreno
  cedros = .65 * cantidad_terreno

  metro_pino = 4
  metro_cedro = 5

  pinos_total = (pinos / 10) * metro_pino
  cedros_total = (cedros / 15) * metro_cedro

  print(f"el total de pinos es {pinos_total} y de cedros es {cedros_total}")

calcular(cantidad_terreno)



