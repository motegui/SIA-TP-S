import copy

from TP2.config import config

# MAX_GENERACIONES = config['condicion_corte']['generacion']
MAX_GENERACIONES = 2


def cantidad_generaciones(poblacion, generacion):
    return generacion >= MAX_GENERACIONES


generaciones_sin_cambios = 0
max_fitness = 0
# GENERACIONES_IGUAL_FITNESS = config['condicion_corte']['generacion']
GENERACIONES_IGUAL_FITNESS = 2


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
# GENERACIONES_IGUALES = config['condicion_corte']['generacion']
GENERACIONES_IGUALES = 0.9


def estructura(poblacion, generacion):
    prop_iguales = 0
    global prev_generation
    nueva_poblacion = [p.cromosoma for p in poblacion]
    print(prev_generation)
    print(nueva_poblacion)
    for gen in prev_generation:
        if gen in nueva_poblacion:
            nueva_poblacion.remove(gen)
            prop_iguales += 1
    prop_iguales /= len(poblacion)
    print(prop_iguales)
    if prop_iguales >= GENERACIONES_IGUALES:
        return True
    prev_generation = [p.cromosoma for p in poblacion]
    return False


# MAX_FITNESS = config['condicion_corte']['optimo']
MAX_FITNESS = 100


def optimo(poblacion, generacion):
    return max(poblacion, key=lambda x: x.fitness) >= MAX_FITNESS
