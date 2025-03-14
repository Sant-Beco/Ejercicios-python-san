"""
15.	Realice un algoritmo que permitan determinar qué paquete se puede comprar una persona con el dinero que recibirá en diciembre, considerando lo siguiente: 
• Paquete A. Si recibe $50,000 o más se comprará una televisión, un modular, tres pares de zapatos, cinco camisas y cinco pantalones. 
• Paquete B. Si recibe menos de $50,000 pero más (o igual) de $20,000, se comprará una grabadora, tres pares de zapatos, cinco camisas y cinco pantalones. 
• Paquete C. Si recibe menos de $20,000 pero más (o igual) de $10,000, se comprará dos pares de zapatos, tres camisas y tres pantalones. 
• Paquete D. Si recibe menos de $10,000, se tendrá que conformar con un par de zapatos, dos camisas y dos pantalones.
"""

dineroDiciembre =int(input("Ingrese el dinero que recibiras en diciembre "))

def compraDiciembre(dineroDiciembre):
  if dineroDiciembre >= 50000:
   print("Paquete A y compraras; una televisión, un modular, tres pares de zapatos, cinco camisas y cinco pantalones.")
  elif dineroDiciembre < 50000 and dineroDiciembre >= 20000:
    print("Paquete B y compraras; una grabadora, tres pares de zapatos, cinco camisas y cinco pantalones.")
  elif dineroDiciembre < 20000 and dineroDiciembre >= 10000:
    print("Paquete C y compraras; dos pares de zapatos, tres camisas y tres pantalones. ")
  elif dineroDiciembre < 10000:
    print("Paquete D y compraras; un par de zapatos, dos camisas y dos pantalones.")
  else:
    print("El valor ingresado es incorrecto")
    
compraDiciembre(dineroDiciembre)

