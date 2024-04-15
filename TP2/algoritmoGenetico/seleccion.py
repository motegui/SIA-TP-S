import math
import random
from TP2.config import config


def elite(poblacion, n, generacion):
    poblacion_len = len(poblacion)
    nueva_poblacion = []
    sorted_poblacion = sorted(poblacion, key=lambda x: x.fitness, reverse=True)
    iter = 0

    while iter != n:
        nueva_poblacion.append(sorted_poblacion[iter % poblacion_len])
        iter += 1

    return nueva_poblacion


def ruleta(poblacion, n, generacion):
    nueva_poblacion = []
    sum_aptitudes = sum(p.fitness for p in poblacion)
    fitness_acumulado_iter = 0
    fitness_acumulado = []
    for p in poblacion:
        fitness_acumulado_iter += p.fitness / sum_aptitudes
        fitness_acumulado.append(fitness_acumulado_iter)
    # en esta posicion ya tengo el array con el fitness acumulado

    for i in range(n):
        x = random.random()
        for j, f in enumerate(fitness_acumulado):
            if x <= f:
                nueva_poblacion.append(poblacion[j])
                break

    return nueva_poblacion


def universal(poblacion, n, generacion):
    nueva_poblacion = []
    sum_aptitudes = sum(p.fitness for p in poblacion)
    fitness_acumulado_iter = 0
    fitness_acumulado = []
    for p in poblacion:
        fitness_acumulado_iter += p.fitness / sum_aptitudes
        fitness_acumulado.append(fitness_acumulado_iter)
    # en esta posicion ya tengo el array con el fitness acumulado
    for i in range(n):
        x = (random.random() + i) / n
        for j, f in enumerate(fitness_acumulado):
            if x <= f:
                nueva_poblacion.append(poblacion[j])
                break
    return nueva_poblacion


TORNEO_DETERMINISTICO_MUESTRA = config.get('seleccion').get('torneo_deterministico').get('muestra')


def torneo_deterministico(poblacion, n, generacion):
    nueva_poblacion = []
    for i in range(n):
        random_sample = random.sample(poblacion, TORNEO_DETERMINISTICO_MUESTRA)
        nueva_poblacion.append(max(random_sample, key=lambda x: x.fitness))
    return nueva_poblacion


TORNEO_PROBABILISTICO_THRESHOLD = config.get('seleccion').get('torneo_probabilistico').get('threshold')


def torneo_probabilistico(poblacion, n, generacion):
    nueva_poblacion = []
    for i in range(n):
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


def ruleta_pseudo_aptitud(poblacion, aptitudes, n):
    nueva_poblacion = []
    # como tengo la nueva aptitud de cada uno pero no el acumulado, calculo el acumulado en el for de aptitud
    # es = a la ruleta solo que le agrego la suma de acumulado
    for i in range(n):
        x = (random.random() + i) / n
        acumulado = 0
        for j, prob in enumerate(aptitudes):
            acumulado += prob
            if acumulado >= x:
                nueva_poblacion.append(poblacion[j])
                break
    return nueva_poblacion


# gen es el nro de generacion
def __temperatura(gen):
    T_C = config.get('seleccion').get('boltzmann').get('T_C')
    T_0 = config.get('seleccion').get('boltzmann').get('T_0')
    T_K = config.get('seleccion').get('boltzmann').get('T_K')
    return T_C + (T_0 - T_C) * math.exp(-T_K * gen)


def boltzmann(poblacion, n, generacion):
    # calculo la suma de todos los boltzmann asi obtengo el exp_val relativo de cada individuo
    sum_boltz_pob = sum(math.exp(p.fitness / __temperatura(generacion)) for p in poblacion)
    exp_val = [math.exp(p.fitness / __temperatura(generacion)) / sum_boltz_pob for p in poblacion]
    return ruleta_pseudo_aptitud(poblacion, exp_val, n)


def ranking(poblacion, n, generacion):
    # primero ordeno la poblacion segun su fitness de mayor a menor
    poblacion_ordenada = sorted(poblacion, key=lambda x: x.fitness, reverse=True)
    tamano = len(poblacion_ordenada)
    pseudo_aptitud = []
    for i in range(0, tamano):
        pseudo_aptitud.append((tamano - i + 1) / tamano)
    return ruleta_pseudo_aptitud(poblacion_ordenada, pseudo_aptitud, n)
