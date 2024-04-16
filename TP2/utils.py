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
    'boltzmann': boltzmann,
    'determinista': torneo_deterministico,
    'probabilistica': torneo_probabilistico,
    'ranking': ranking

}

metodo_cruce = {
    'un_punto': un_punto,
    'dos_puntos': dos_puntos,
    'anular': anular,
    'uniforme': uniforme
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

metodo_seleccion_cruce = {
    "puntas": cruzar_poblacion_puntas,
    "escalonado": cruzar_poblacion_escalonado,
    "fitness": cruzar_poblacion_escalonado
}


def mejor_fitness(poblacion):
    mejor_actual = poblacion[0]
    for individuo in poblacion[1:]:
        if individuo.fitness > mejor_actual.fitness:
            mejor_actual = individuo
    return mejor_actual


def peor_fitness(poblacion):
    peor_actual = poblacion[0]
    for individuo in poblacion[1:]:
        if individuo.fitness < peor_actual.fitness:
            peor_actual = individuo
    return peor_actual


def fitness_promedio(poblacion):
    suma_valores = sum(individuo.fitness for individuo in poblacion)
    cantidad_objetos = len(poblacion)

    return suma_valores / cantidad_objetos


# Para una configuracion dada, corro 100 veces
def simular_100_veces(archivo_config):
    simulaciones = []
    for i in range(100):
        iter = iteracion(archivo_config)
        simulaciones.append(iter)

    return simulaciones



def crear_configuracion_mutacion(probabilidad_mutacion, metodo_mutacion, funcion_no_uniforme):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if probabilidad_mutacion is not None:
        config_data['mutacion']['probabilidad'] = probabilidad_mutacion

    if metodo_mutacion is not None:
        config_data['mutacion']['metodo'] = metodo_mutacion
    config_data['mutacion']['no_uniforme']['funcion'] = funcion_no_uniforme

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def crear_configuracion_n(n):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if n is not None:
        config_data['n'] = n

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def crear_configuracion_sesgo(sesgo_joven: bool):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if sesgo_joven is not None:
        config_data['sesgo']['joven'] = sesgo_joven

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def crear_configuracion_b(b):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if b is not None:
        config_data['reemplazo']['B'] = b

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def crear_configuracion_cruce(metodo_cruce, metodo_seleccion):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if metodo_cruce is not None:
        config_data['cruce']['metodo'] = metodo_cruce

    if metodo_seleccion is not None:
        config_data['cruce']['metodo_seleccion_cruce'] = metodo_seleccion

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def crear_configuracion_seleccion(metodo1, metodo2):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if metodo1 is not None:
        config_data['seleccion']['metodo1'] = metodo1
    if metodo2 is not None:
        config_data['seleccion']['metodo2'] = metodo2

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def crear_configuracion_clase(clase):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if clase is not None:
        config_data['clase'] = clase

    with open('custom_config.json', 'w') as file:
        json.dump(config_data, file, indent=4)
        file.flush()
    file.close()


def crear_configuracion_reemplazo(metodo3, metodo4):
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    if metodo3 is not None:
        config_data['reemplazo']['metodo3'] = metodo3
    if metodo4 is not None:
        config_data['reemplazo']['metodo4'] = metodo4

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
        A = config.get("seleccion").get("A")
        B = config.get("reemplazo").get("B")

        padres = (metodos_seleccion[config.get('seleccion').get('metodo1')](poblacion=poblacion_actual,
                                                                            n=math.floor(K * A),
                                                                            generacion=generacion_actual) +
                  metodos_seleccion[config.get('seleccion').get('metodo2')](poblacion=poblacion_actual,
                                                                            n=K - math.floor(K * A),
                                                                            generacion=generacion_actual))

        if config.get("cruce").get("metodo_seleccion_cruce") == 'fitness':
            padres = sorted(padres, key=lambda x: x.fitness, reverse=True)
        cromosomas_hijos = metodo_seleccion_cruce[config.get("cruce").get("metodo_seleccion_cruce")](padres,
                                                                                                     metodo_cruce[
                                                                                                         config.get(
                                                                                                             'cruce').get(
                                                                                                             'metodo')])

        prob_mutacion = config.get('mutacion').get('probabilidad')
        if config.get('mutacion').get('no_uniforme').get('funcion') is not None:
            prob_mutacion = (metodos_no_uniformes[config.get('mutacion').get('no_uniforme').get('funcion')]
                             (prob_mutacion,
                              generacion_actual, config.get('mutacion').get('no_uniforme').get('factor')
                              ))

        cromosomas_mutados = mutar_poblacion(cromosomas_hijos,
                                             metodos_mutacion_uniforme[config.get("mutacion").get("metodo")],
                                             prob_mutacion)

        hijos = []
        for cromosoma in cromosomas_mutados:
            hijos.append(Player(Clase[clase], cromosoma))

        if not config.get('sesgo').get('joven'):
            poblacion_k_mas_n = poblacion_actual + hijos
            poblacion_actual = (
                    metodos_seleccion[config.get('reemplazo').get('metodo3')](poblacion=poblacion_k_mas_n,
                                                                              n=math.floor(n * B),
                                                                              generacion=generacion_actual)
                    + metodos_seleccion[config.get('reemplazo').get('metodo4')](poblacion=poblacion_k_mas_n,
                                                                                n=n - math.floor(n * B),
                                                                                generacion=generacion_actual))
        else:
            if K >= n:
                poblacion_actual = (
                        metodos_seleccion[config.get('reemplazo').get('metodo3')](poblacion=hijos,
                                                                                  size=math.floor(n * B))
                        + metodos_seleccion[config.get('reemplazo').get('metodo4')](poblacion=hijos,
                                                                                    n=n - math.floor(n * B),
                                                                                    generacion=generacion_actual))
            else:
                poblacion_actual = hijos + (
                        metodos_seleccion[config.get('reemplazo').get('metodo3')](poblacion=poblacion_actual,
                                                                                  n=math.floor((n - K) * B),
                                                                                  generacion=generacion_actual)
                        + metodos_seleccion[config.get('reemplazo').get('metodo4')](poblacion=poblacion_actual,
                                                                                    n=(n - K) - math.floor((n - K) * B),
                                                                                    generacion=generacion_actual))
        generacion_actual += 1

    return [
        generacion_actual,
        mejor_fitness(poblacion_actual),
        fitness_promedio(poblacion_actual),
        peor_fitness(poblacion_actual)
    ]


