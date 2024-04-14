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


def multi_gen_limitada(cromosoma, probabilidad_mutacion):
    # elegimos la cantidad de genes que se van a iterar
    cantidad = random.randint(0, len(cromosoma))
    genes_iterados = []  # arreglo donde guardamos los genes que ya se iteraron

    for i in range(0, cantidad):
        # elegimos un gen random para mutar
        gen_a_iterar = random.randint(0, len(cromosoma)-1)
        if random.random() < probabilidad_mutacion:
            # si este gen ya fue iterado no hacemos nada
            if gen_a_iterar in genes_iterados:
                break
            if gen_a_iterar == ALTURA:
                cromosoma[ALTURA] = random.uniform(1.3, 2)
            else:
                cromosoma[gen_a_iterar] = random.uniform(cromosoma[gen_a_iterar] * RANGO['min'], cromosoma[gen_a_iterar] * RANGO['max'])
            genes_iterados.append(gen_a_iterar)  # guardamos el gen para no repetirlo

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
