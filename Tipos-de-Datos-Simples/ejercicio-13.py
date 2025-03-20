"""Reto tio luis:
Ecuacion patrimonial activos = pasivo + patrimonio o A = P + Pt 
si P = 61.500.000 pasivo, y A = 9 veces el valor de Pt cual sera el valor de P si el valor de A aumenta 7.2 %
y el valor de Pt disminuye un 3.5%"""


Pasi = 61_500_000
Pt = (Pasi / 8)
Act = Pasi + Pt

Act *= 1.072
Pt *= 0.965

Pasi = Act - Pt

print(f"\nValor de A {Act:,.2f} \nValor de P {Pasi:,.2f} \nValor de Pt {Pt:,.2f} \n")
