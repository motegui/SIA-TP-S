import numpy as np

FUERZA = 0
AGILIDAD = 1
PERICIA = 2
RESISTENCIA = 3
VIDA = 4


class Equipamiento:
    def __init__(self, items):
        self.fuerza = items[FUERZA]
        self.agilidad = items[AGILIDAD]
        self.pericia = items[PERICIA]
        self.resistencia = items[RESISTENCIA]
        self.vida = items[VIDA]

        if self.fuerza < 0 or self.agilidad < 0 or self.pericia < 0 or self.resistencia < 0 or self.vida < 0:
            raise ValueError("Ningun atributo puede ser negativo")

        if self.fuerza + self.agilidad + self.pericia + self.resistencia + self.vida != 150:  # TODO no entiendo bien esto de la consigna! Los valores para cada una de las características pueden ser valores decimales
            raise ValueError("La suma de las cualidades debe ser 150")

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
