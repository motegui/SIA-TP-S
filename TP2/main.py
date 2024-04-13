import math
import json
from TP2.algoritmoGenetico.condicion_corte import contenido, estructura, optimo, cantidad_generaciones
from TP2.algoritmoGenetico.cruces import *
from TP2.algoritmoGenetico.no_uniformes import creciente, decreciente
from TP2.algoritmoGenetico.seleccion import *
from TP2.player.clase import Clase
from TP2.player.player import Player
from TP2.config import config
from TP2.player.player import generar_cromosoma
from TP2.algoritmoGenetico.mutacion import mutar_poblacion, gen, multi_gen_uniforme, completa, multi_gen_limitada
from TP2.custom_config import custom_config

PROBABILIDAD_MUTACION = config.get('probabilidad_mutacion')

condiciones_corte = {
    'estructura': estructura,
    'optimo': optimo,
    'contenido': contenido,
    'cantidad_gen': cantidad_generaciones
}

metodos_seleccion = {
    'elite': elite,
    'universal': universal,
    'ruleta': ruleta,
    'boltzman': boltzmann,
    'determinista': torneo_deterministico,
    'probabilistica': torneo_probabilistico,
    'ranking': ranking

}

metodo_cruce = {
    'un_punto': un_punto,
    'dos_puntos': dos_puntos
}

metodos_no_uniformes = {
    "creciente": creciente,
    "decreciente": decreciente
}

metodos_mutacion_uniforme = {
    "gen": gen,
    "multigen": multi_gen_uniforme,
    "completa": completa,
    "limitada": multi_gen_limitada
}


def mejor_fitness(poblacion):
    mejor_actual = poblacion[0].fitness
    for individuo in poblacion[1:]:
        if individuo.fitness > mejor_actual:
            mejor_actual = individuo.fitness
    return mejor_actual


def peor_fitness(poblacion):
    peor_actual = poblacion[0].fitness
    for individuo in poblacion[1:]:
        if individuo.fitness < peor_actual:
            peor_actual = individuo.fitness
    return peor_actual


def fitness_promedio(poblacion):
    suma_valores = sum(individuo.fitness for individuo in poblacion)
    cantidad_objetos = len(poblacion)

    return suma_valores / cantidad_objetos


# Para una configuracion dada, corro 100 veces
def simular_100_veces(archivo_config):
    simulaciones = []
    for i in range(5):
        simulaciones.append(iteracion(archivo_config))
    return simulaciones


def crear_configuracion_mutacion(probabilidad_mutacion, metodo_mutacion, funcion_no_uniforme):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if probabilidad_mutacion is not None:
        config_data['probabilidad_mutacion'] = probabilidad_mutacion
    if metodo_mutacion is not None:
        config_data['metodo_mutacion_uniforme'] = metodo_mutacion
    config_data['funcion_no_uniforme'] = funcion_no_uniforme

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def crear_configuracion_sesgo(sesgo_joven:bool):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if sesgo_joven is not None:
        config_data['favorecer_jovenes'] = sesgo_joven

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def crear_configuracion_seleccion(metodo1, metodo2):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if metodo1 is not None:
        config_data['metodo1'] = metodo1
    if metodo2 is not None:
        config_data['metodo2'] = metodo2

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def iteracion(config=config):
    clase = config.get("clase")
    n = config.get('n')

    poblacion_inicial = []
    for i in range(0, n):
        cromosoma = generar_cromosoma()
        poblacion_inicial.append(Player(Clase[clase], cromosoma))

    poblacion_actual = poblacion_inicial
    generacion_actual = 1
    while not condiciones_corte[config.get('condicion_corte').get('tipo')](poblacion_actual, generacion_actual):
        K = config.get("K")
        A = config.get("A")
        B = config.get("B")

        padres = (metodos_seleccion[config.get('metodo1')](poblacion=poblacion_actual, n=math.floor(K * A),
                                                           generacion=generacion_actual) +
                  metodos_seleccion[config.get('metodo2')](poblacion=poblacion_actual, n=K - math.floor(K * A),
                                                           generacion=generacion_actual))

        cromosomas_hijos = cruzar_poblacion(padres, metodo_cruce[config.get('metodo_cruce')])

        prob_mutacion = config.get('probabilidad_mutacion')
        if config.get('funcion_no_uniforme') is not None:
            prob_mutacion = (metodos_no_uniformes[config.get('funcion_no_uniforme')]
                             (prob_mutacion,
                              generacion_actual, config.get('factor')
                              ))

        cromosomas_mutados = mutar_poblacion(cromosomas_hijos, gen, prob_mutacion)

        hijos = []
        for cromosoma in cromosomas_mutados:
            hijos.append(Player(Clase[clase], cromosoma))

        if not config.get('favorecer_jovenes'):
            poblacion_k_mas_n = poblacion_actual + hijos
            poblacion_actual = (
                    metodos_seleccion[config.get('metodo3')](poblacion=poblacion_k_mas_n, n=math.floor(n * B),
                                                             generacion=generacion_actual)
                    + metodos_seleccion[config.get('metodo4')](poblacion=poblacion_k_mas_n, n=n - math.floor(n * B),
                                                               generacion=generacion_actual))
        else:
            if K >= n:
                poblacion_actual = (
                        metodos_seleccion[config.get('metodo3')](poblacion=hijos, size=math.floor(n * B))
                        + metodos_seleccion[config.get('metodo4')](poblacion=hijos,
                                                                   n=n - math.floor(n * B),
                                                                   generacion=generacion_actual))
            else:
                poblacion_actual = hijos + (
                        metodos_seleccion[config.get('metodo3')](poblacion=poblacion_actual,
                                                                 n=math.floor((n - K) * B),
                                                                 generacion=generacion_actual)
                        + metodos_seleccion[config.get('metodo4')](poblacion=poblacion_actual,
                                                                   n=(n - K) - math.floor((n - K) * B),
                                                                   generacion=generacion_actual))
        generacion_actual += 1

    return [
        generacion_actual,
        mejor_fitness(poblacion_actual),
        fitness_promedio(poblacion_actual),
        peor_fitness(poblacion_actual)
    ]


def main():
    print(iteracion(custom_config))


if __name__ == '__main__':
    crear_configuracion(1, None)
    main()
