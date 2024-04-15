import copy

from TP2.config import config


def cantidad_generaciones(poblacion, generacion):
    return generacion >= config.get('condicion_corte').get('cantidad_generaciones').get('max_generacion')


max_fitness = config.get("condicion_corte").get("max_fitness")


def contenido(poblacion, generacion):
    global max_fitness
    generaciones_sin_cambios = config.get('condicion_corte').get('contenido').get('generaciones_sin_cambio')
    generaciones_igual_fitness = config.get('condicion_corte').get('contenido').get('generaciones_igual_fitness')
    max_fitness_rel = max(poblacion, key=lambda p: p.fitness).fitness
    if max_fitness_rel == max_fitness:
        generaciones_sin_cambios += 1
        return generaciones_sin_cambios >= generaciones_igual_fitness
    else:
        generaciones_sin_cambios = 0
        max_fitness = max(max_fitness, max_fitness_rel)
    return False


prev_generation = []


def estructura(poblacion, generacion):
    prop_iguales = 0
    generaciones_iguales = config.get('condicion_corte').get('estructura').get('generaciones_iguales')
    global prev_generation
    nueva_poblacion = [p.cromosoma for p in poblacion]
    for gen in prev_generation:
        if gen in nueva_poblacion:
            nueva_poblacion.remove(gen)
            prop_iguales += 1
    prop_iguales /= len(poblacion)
    if prop_iguales >= generaciones_iguales:
        return True
    prev_generation = [p.cromosoma for p in poblacion]
    return False


def optimo(poblacion, generacion):
    return max(poblacion, key=lambda x: x.fitness).fitness >= max_fitness
