import random
from TP2.player.player import *

from TP2.config import config

PROBABILIDAD_MUTACION = config.get('probabilidad_mutacion')

RANGO = config['rango']


def gen(cromosoma, probabilidad_mutacion):
    if random.random() < probabilidad_mutacion:
        var = random.randint(0, len(cromosoma) - 1)
        if var == ALTURA:
            cromosoma[ALTURA] = random.uniform(1.3, 2)
        else:
            cromosoma[var] = random.uniform(cromosoma[var] * RANGO['min'], cromosoma[var] * RANGO['max'])
    return cromosoma


def multi_gen_uniforme(cromosoma, probabilidad_mutacion):
    for i in range(0, len(cromosoma)):
        if random.random() < probabilidad_mutacion:
            if i == ALTURA:
                cromosoma[ALTURA] = random.uniform(1.3, 2)
            else:
                cromosoma[i] = random.uniform(cromosoma[i] * RANGO['min'], cromosoma[i] * RANGO['max'])

    return cromosoma


def completa(cromosoma, probabilidad_mutacion):
    if random.random() < probabilidad_mutacion:
        for i in range(0, len(cromosoma)):
            if i == ALTURA:
                cromosoma[ALTURA] = random.uniform(1.3, 2)
            else:
                cromosoma[i] = random.uniform(cromosoma[i] * RANGO['min'], cromosoma[i] * RANGO['max'])

        return cromosoma


def mutar_poblacion(cromosomas, metodo, probabilidad_mutacion):
    mutados = []
    for cromosoma in cromosomas:
        mutados.append(metodo(cromosoma, probabilidad_mutacion))
    return mutados
