from enum import Enum


class Clase(Enum):
    GUERRERO = (0.6, 0.4)
    ARQUERO = (0.9, 0.1)
    DEFENSOR = (0.1, 0.9)
    INFILTRADO = (0.8, 0.3)

    def __init__(self, ataque, defensa):
        self.ataque = ataque
        self.defensa = defensa
