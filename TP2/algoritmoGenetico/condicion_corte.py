import copy

from TP2.config import config

MAX_GENERACIONES = config.get('condicion_corte').get('MAX_GENERACION')


def cantidad_generaciones(poblacion, generacion):
    return generacion >= MAX_GENERACIONES


generaciones_sin_cambios = config.get("condicion_corte").get("GENERACIONES_SIN_CAMBIO")
max_fitness = config.get("condicion_corte").get("MAX_FITNESS")
GENERACIONES_IGUAL_FITNESS = config.get('condicion_corte').get('GENERACIONES_IGUAL_FITNESS')


def contenido(poblacion, generacion):
    global max_fitness, generaciones_sin_cambios
    max_fitness_rel = max(poblacion, key=lambda p: p.fitness).fitness
    if max_fitness_rel == max_fitness:
        generaciones_sin_cambios += 1
        return generaciones_sin_cambios >= GENERACIONES_IGUAL_FITNESS
    else:
        generaciones_sin_cambios = 0
        max_fitness = max(max_fitness, max_fitness_rel)
    return False


prev_generation = []
GENERACIONES_IGUALES = config.get('condicion_corte').get('GENERACIONES_IGUALES')


def estructura(poblacion, generacion):
    prop_iguales = 0
    global prev_generation
    nueva_poblacion = [p.cromosoma for p in poblacion]
    for gen in prev_generation:
        if gen in nueva_poblacion:
            nueva_poblacion.remove(gen)
            prop_iguales += 1
    prop_iguales /= len(poblacion)
    if prop_iguales >= GENERACIONES_IGUALES:
        return True
    prev_generation = [p.cromosoma for p in poblacion]
    return False


MAX_FITNESS = config.get('condicion_corte').get('MAX_FITNESS')


def optimo(poblacion, generacion):
    return max(poblacion, key=lambda x: x.fitness).fitness >= MAX_FITNESS
