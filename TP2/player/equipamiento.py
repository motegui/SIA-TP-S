import numpy as np

FUERZA = 0
AGILIDAD = 1
PERICIA = 2
RESISTENCIA = 3
VIDA = 4
SUM_EQUIPAMIENTOS = 150


class Equipamiento:
    def __init__(self, items):
        self.fuerza = items[FUERZA]
        self.agilidad = items[AGILIDAD]
        self.pericia = items[PERICIA]
        self.resistencia = items[RESISTENCIA]
        self.vida = items[VIDA]

        if self.fuerza < 0 or self.agilidad < 0 or self.pericia < 0 or self.resistencia < 0 or self.vida < 0:
            raise ValueError("Ningun atributo puede ser negativo")

        total_sum = sum(items)
        self.fuerza *= SUM_EQUIPAMIENTOS / total_sum
        self.agilidad *= SUM_EQUIPAMIENTOS / total_sum
        self.pericia *= SUM_EQUIPAMIENTOS / total_sum
        self.resistencia *= SUM_EQUIPAMIENTOS / total_sum
        self.vida *= SUM_EQUIPAMIENTOS / total_sum

    def fuerza_p(self):
        return 100 * np.tanh(0.01 * self.fuerza)

    def agilidad_p(self):
        return np.tanh(0.01 * self.agilidad)

    def pericia_p(self):
        return 0.6 * np.tanh(0.01 * self.pericia)

    def resistencia_p(self):
        return np.tanh(0.01 * self.resistencia)

    def vida_p(self):
        return 100 * np.tanh(0.01 * self.vida)

    def get_items(self):
        return [self.fuerza, self.agilidad, self.pericia, self.resistencia, self.vida]
