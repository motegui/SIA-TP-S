import random
from TP2.player.player import *

from TP2.config import config

PROBABILIDAD_MUTACION = config['probabolidad_mutacion']
RANGO = config['rango']


def gen(cromosoma):
    if random.random() < PROBABILIDAD_MUTACION:
        var = random.randint(0, len(cromosoma) - 1)
    if var == ALTURA:
        cromosoma[ALTURA] = random.uniform(1.3, 2)
    else:
        cromosoma[var] = random.uniform(cromosoma[var] * RANGO['min'], cromosoma[var] * RANGO['max'])
    return cromosoma


def multi_gen_uniforme(cromosoma):
    for i in range(0, len(cromosoma)):
        if random.random() < PROBABILIDAD_MUTACION:
            if i == ALTURA:
                cromosoma[ALTURA] = random.uniform(1.3, 2)
            else:
                cromosoma[i] = random.uniform(cromosoma[i] * RANGO['min'], cromosoma[i] * RANGO['max'])

    return cromosoma


def completa(cromosoma):
    if random.random() < PROBABILIDAD_MUTACION:
        for i in range(0, len(cromosoma)):
            if i == ALTURA:
                cromosoma[ALTURA] = random.uniform(1.3, 2)
            else:
                cromosoma[i] = random.uniform(cromosoma[i] * RANGO['min'], cromosoma[i] * RANGO['max'])

        return cromosoma
