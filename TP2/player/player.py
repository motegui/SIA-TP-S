import random

from TP2.player.equipamiento import Equipamiento

ALTURA = 0
FUERZA = 1
AGILIDAD = 2
PERICIA = 3
RESISTENCIA = 4
VIDA = 5


class Player:
    def __init__(self, clase, cromosoma):  # Un jugador es creado con su clase y con su cromosoma!
        self.clase = clase
        self.altura = cromosoma[ALTURA]
        self.equipamiento = Equipamiento(cromosoma[1:])
        self.cromosoma = [cromosoma[0]] + self.equipamiento.get_items()
        if not 1.3 <= self.altura <= 2:
            raise ValueError("Altura entre 1.3 y 2 metros")
        self.fitness = self.clase.ataque * self.__ataque() + self.clase.defensa * self.__defensa()

    def __ATM(self):
        return 0.5 - (3 * self.altura - 5) ** 4 + (3 * self.altura - 5) ** 2 + self.altura / 2

    def __DEM(self):
        return 2 + (3 * self.altura - 5) ** 4 - (3 * self.altura - 5) ** 2 - self.altura / 2

    def __ataque(self):
        return (
                    self.equipamiento.agilidad_p() + self.equipamiento.pericia_p()) * self.equipamiento.fuerza_p() * self.__ATM()

    def __defensa(self):
        return (
                    self.equipamiento.resistencia_p() + self.equipamiento.pericia_p()) * self.equipamiento.vida_p() * self.__DEM()


def generar_cromosoma():
    puntos_totales = 150
    puntos_asignados = []

    for _ in range(4):
        puntos = round(random.uniform(0, puntos_totales), 2)
        puntos_asignados.append(puntos)
        puntos_totales -= puntos

    puntos_asignados.append(puntos_totales)
    return puntos_asignados
