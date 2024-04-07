import math
import random


def elite(poblacion, size):
    poblacion_len = len(poblacion)
    nueva_poblacion = []
    sorted_poblacion = sorted(poblacion, key=lambda x: x.fitness, reverse=True)
    iter = 0

    while iter != size:
        nueva_poblacion.append(sorted_poblacion[iter % poblacion_len])
        iter += 1
    return nueva_poblacion


def ruleta(poblacion, size):
    nueva_poblacion = []
    sum_aptitudes = sum(p.fitness for p in poblacion)
    fitness_acumulado_iter = 0
    fitness_acumulado = []
    for p in poblacion:
        fitness_acumulado_iter += p.fitness / sum_aptitudes
        fitness_acumulado.append(fitness_acumulado_iter)
    # en esta posicion ya tengo el array con el fitness acumulado

    for i in range(size):
        x = random.random()
        for j, f in enumerate(fitness_acumulado):
            if x <= f:
                nueva_poblacion.append(poblacion[j])
                break

    return nueva_poblacion


def universal(poblacion, size):
    nueva_poblacion = []
    sum_aptitudes = sum(p.fitness for p in poblacion)
    fitness_acumulado_iter = 0
    fitness_acumulado = []
    for p in poblacion:
        fitness_acumulado_iter += p.fitness / sum_aptitudes
        fitness_acumulado.append(fitness_acumulado_iter)
    # en esta posicion ya tengo el array con el fitness acumulado
    for i in range(size):
        x = (random.random() + i) / size
        for j, f in enumerate(fitness_acumulado):
            if x <= f:
                nueva_poblacion.append(poblacion[j])
                break
    return nueva_poblacion


# TORNEO_DETERMINISTICO_MUESTRA = config['seleccion']['torneoDeterministico']
TORNEO_DETERMINISTICO_MUESTRA = 2


def torneo_deterministico(poblacion, size):
    nueva_poblacion = []
    for i in range(size):
        random_sample = random.sample(poblacion, TORNEO_DETERMINISTICO_MUESTRA)
        nueva_poblacion.append(max(random_sample, key=lambda x: x.fitness))
    return nueva_poblacion


TORNEO_PROBABILISTICO_THRESHOLD = 0.7  # todo validar que este entre 0.5 y 1


def torneo_probabilistico(poblacion, size):
    nueva_poblacion = []
    for i in range(size):
        p_max = poblacion[random.randint(0, len(poblacion) - 1)]
        p_min = poblacion[random.randint(0, len(poblacion) - 1)]
        if p_max.fitness < p_min.fitness:
            aux = p_max
            p_max = p_min
            p_min = aux

        r = random.random()
        if r < TORNEO_PROBABILISTICO_THRESHOLD:
            nueva_poblacion.append(p_max)
        else:
            nueva_poblacion.append(p_min)

    return nueva_poblacion


BOLTZMANN_TEMPERATURA = 10


def ruleta_pseudo_aptitud(poblacion, aptitudes, size):
    nueva_poblacion = []
    # como tengo la nueva aptitud de cada uno pero no el acumulado, calculo el acumulado en el for de aptitud
    # es = a la ruleta solo que le agrego la suma de acumulado
    for i in range(size):
        x = (random.random() + i) / size
        acumulado = 0
        for j, prob in enumerate(aptitudes):
            acumulado += prob
            if acumulado >= x:
                nueva_poblacion.append(poblacion[j])
                break
    return nueva_poblacion


def boltzmann(poblacion, size):
    #calculo la suma de todos los boltzmann asi obtengo el exp_val relativo de cada individuo
    sum_boltz_pob = sum(math.exp(p.fitness / BOLTZMANN_TEMPERATURA) for p in poblacion)
    exp_val = [math.exp(p.fitness / BOLTZMANN_TEMPERATURA) / sum_boltz_pob for p in poblacion]
    return ruleta_pseudo_aptitud(poblacion, exp_val, size)


def ranking(poblacion, size):
    #primero ordeno la poblacion segun su fitness de mayor a menor
    poblacion_ordenada = sorted(poblacion, key=lambda x: x.fitness, reverse=True)
    max_fitness = poblacion_ordenada[0].fitness
    pseudo_aptitud = [(max_fitness - p.fitness) / max_fitness for p in poblacion_ordenada]
    return ruleta_pseudo_aptitud(poblacion, pseudo_aptitud, size)
