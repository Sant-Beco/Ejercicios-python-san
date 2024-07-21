"""
9 Se les dará un bono por antigüedad a los empleados de una tienda. Si tienen un año, se les dará $100; si tienen 2 años, 
$200, y así sucesivamente hasta los 5 años. Para los que tengan más de 5, el bono será de $1000. Realice un algoritmo y 
represéntelo mediante el diagrama de flujo, el pseudocódigo y diagrama N/S que permita determinar el bono que recibirá 
un trabajador.
"""

anios = int(input("Ingresa cuantos años llevas en la tienda nexis: "))

def bono_tienda(anios):
  if anios == 1:
    print("Tu bono sera de $100")
  elif anios == 2:
    print("Tu bono sera de $200")
  elif anios == 3:
    print("Tu bono sera de $300")
  elif anios == 4:
    print("Tu bono sera de $400")
  elif anios == 5:
    print("Tu bono sera de $500")
  elif anios > 5:
    print("Tu bono sera de $1000")
  else:
    print("Valor invalido")
    
bono_tienda(anios)