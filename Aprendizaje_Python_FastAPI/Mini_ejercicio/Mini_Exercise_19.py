"""# Tu reto:
# - Añade atributos marca y modelo
# - Crea un método describir_auto que los imprima

# Aquí empieza tu código:
"""

class Auto:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    # Método normal
    def decir_modelo(self):
        print(f"{self.marca} Toyota tornado")

    def describir_auto(self):
        print(f"Este auto es un {self.marca} de color {self.color}.")


mi_auto = Auto("nissan","negro")


mi_auto.decir_modelo()
mi_auto.describir_auto()

print(type(Auto))
print(type(mi_auto))