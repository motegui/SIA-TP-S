import math
import random

from TP2.config import config
from TP2.player.clase import Clase
from TP2.player.player import Player


def un_punto(c1, c2):
    locus = random.randint(0, len(c1) - 1)
    h1 = c1[:locus] + c2[locus:]
    h2 = c2[:locus] + c1[locus:]
    return [h1, h2]


def dos_puntos(c1, c2):
    locus1 = random.randint(0, len(c1) - 1)
    locus2 = random.randint(0, len(c1) - 1)
    if locus1 > locus2:
        aux = locus1
        locus1 = locus2
        locus2 = aux

    h1 = c1[:locus1] + c2[locus1:locus2] + c1[locus2:]
    h2 = c2[:locus1] + c1[locus1:locus2] + c2[locus2:]
    return [h1, h2]


def anular(c1, c2):
    locus = random.randint(0, len(c1) - 1)
    largo = random.randint(0, math.ceil(len(c1) / 2))
    if largo + locus < len(c1):
        # caso sin dar la vuelta
        h1 = c1[:locus] + c2[locus:locus + largo] + c1[locus + largo:]
        h2 = c2[:locus] + c1[locus:locus + largo] + c2[locus + largo:]
    else:
        locus2 = (largo + locus) % len(c1)
        h1 = c1[:locus2] + c2[locus2:locus] + c1[locus:]
        h2 = c2[:locus2] + c1[locus2:locus] + c2[locus:]
    return [h1, h2]


PROBABILIDAD_UNIFORME = config.get('cruce').get('probabilidadUniforme')


def uniforme(c1, c2):
    h1 = []
    h2 = []
    for i in range(len(c1)):
        if random.random() < PROBABILIDAD_UNIFORME:
            h1.append(c2[i])
            h2.append(c1[i])
        else:
            h1.append(c1[i])
            h2.append(c2[i])
    return [h1, h2]


def cruzar_poblacion(poblacion, metodo_de_cruce):
    cromosomas = []
    for i in range(0, len(poblacion)-1, 2):
        cromosomas += metodo_de_cruce(poblacion[i].cromosoma, poblacion[i+1].cromosoma)

    cromosomas += metodo_de_cruce(poblacion[0].cromosoma, poblacion[-1].cromosoma)

    return cromosomas[:len(poblacion)]
