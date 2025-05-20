"""# Tu reto:
# - Añade atributos marca y modelo
# - Crea un método describir_auto que los imprima

# Aquí empieza tu código:
"""

class Auto:
    def __init__(self, mi_auto, color):
        self.mi_auto = mi_auto
        self.color = color

    # Método normal
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau! 🐶")

mi_auto = Auto()

print(type(Auto))
print(type(mi_auto))

